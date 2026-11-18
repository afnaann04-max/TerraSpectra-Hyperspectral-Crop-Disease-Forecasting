
from dataclasses import dataclass
import pandas as pd


@dataclass
class ValidationReport:
    rows: int
    columns: int
    missing_values: int
    duplicate_rows: int
    missing_labels: int
    missing_groups: int
    valid: bool
    issues: list


def validate_dataset(data, label_col, group_col):
    """Validate basic dataset quality before ML experiments."""

    if not isinstance(data, pd.DataFrame):
        raise TypeError("Input must be a pandas DataFrame.")

    if data.empty:
        raise ValueError("Dataset cannot be empty.")

    required_columns = [label_col, group_col]

    for column in required_columns:
        if column not in data.columns:
            raise ValueError(f"Required column not found: {column}")

    missing_values = int(data.isna().sum().sum())
    duplicate_rows = int(data.duplicated().sum())
    missing_labels = int(data[label_col].isna().sum())
    missing_groups = int(data[group_col].isna().sum())

    issues = []

    if missing_values:
        issues.append("Dataset contains missing values.")

    if duplicate_rows:
        issues.append("Dataset contains duplicate rows.")

    if missing_labels:
        issues.append("Target labels contain missing values.")

    if missing_groups:
        issues.append("Group identifiers contain missing values.")

    return ValidationReport(
        rows=len(data),
        columns=len(data.columns),
        missing_values=missing_values,
        duplicate_rows=duplicate_rows,
        missing_labels=missing_labels,
        missing_groups=missing_groups,
        valid=len(issues) == 0,
        issues=issues,
    )
