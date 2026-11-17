
"""Group-aware dataset splitting for TerraSpectra experiments."""

import pandas as pd
from sklearn.model_selection import GroupShuffleSplit


def split_dataset(
    data: pd.DataFrame,
    label_col: str,
    group_col: str,
    test_size: float = 0.20,
    val_size: float = 0.20,
    random_state: int = 42,
):
    """
    Split observations into train, validation and test sets.

    Observations sharing a group identifier are kept in the same
    partition to reduce biological-sample leakage.

    Note:
        GroupShuffleSplit does not guarantee stratified class
        proportions. Always inspect the returned class distribution.
    """
    if not isinstance(data, pd.DataFrame):
        raise TypeError("data must be a pandas DataFrame.")

    if label_col not in data.columns or group_col not in data.columns:
        raise ValueError("Label or group column was not found.")

    if data.empty:
        raise ValueError("data cannot be empty.")

    if data[label_col].isna().any() or data[group_col].isna().any():
        raise ValueError("Labels and group identifiers cannot be missing.")

    if not (0 < test_size < 1 and 0 < val_size < 1):
        raise ValueError("Split proportions must be between 0 and 1.")

    if test_size + val_size >= 1:
        raise ValueError("test_size + val_size must be less than 1.")

    if data[group_col].nunique() < 3:
        raise ValueError("At least three independent groups are required.")

    # First, reserve the independent test groups.
    first_split = GroupShuffleSplit(
        n_splits=1,
        test_size=test_size,
        random_state=random_state,
    )

    train_val_idx, test_idx = next(
        first_split.split(data, groups=data[group_col])
    )

    train_val = data.iloc[train_val_idx].copy()
    test = data.iloc[test_idx].copy()

    # Calculate validation proportion relative to the remaining data.
    relative_val_size = val_size / (1 - test_size)

    second_split = GroupShuffleSplit(
        n_splits=1,
        test_size=relative_val_size,
        random_state=random_state,
    )

    train_idx, val_idx = next(
        second_split.split(train_val, groups=train_val[group_col])
    )

    train = train_val.iloc[train_idx].copy()
    validation = train_val.iloc[val_idx].copy()

    # Verify that no group occurs in multiple partitions.
    train_groups = set(train[group_col])
    val_groups = set(validation[group_col])
    test_groups = set(test[group_col])

    if train_groups & val_groups:
        raise RuntimeError("Group leakage detected between train and validation.")

    if train_groups & test_groups:
        raise RuntimeError("Group leakage detected between train and test.")

    if val_groups & test_groups:
        raise RuntimeError("Group leakage detected between validation and test.")

    # Summarize class distribution for inspection.
    distribution = pd.DataFrame({
        "train": train[label_col].value_counts(normalize=True),
        "validation": validation[label_col].value_counts(normalize=True),
        "test": test[label_col].value_counts(normalize=True),
    }).fillna(0)

    return {
        "train": train,
        "validation": validation,
        "test": test,
        "class_distribution": distribution,
    }
