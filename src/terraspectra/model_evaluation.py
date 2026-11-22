
import numpy as np
from sklearn.metrics import (
    accuracy_score,
    balanced_accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    confusion_matrix,
    roc_auc_score,
)
from sklearn.utils.multiclass import unique_labels


def evaluate_classifier(y_true, y_pred, y_proba=None):
    """
    Evaluate a classification model using standard classification metrics.

    y_proba:
        Optional predicted probabilities.
        For binary classification, provide positive-class probabilities
        as a 1D array or probabilities for both classes as a 2D array.
        For multiclass classification, provide one probability column
        per class, in sorted class-label order.
    """

    y_true = np.asarray(y_true)
    y_pred = np.asarray(y_pred)

    if y_true.ndim != 1 or y_pred.ndim != 1:
        raise ValueError("y_true and y_pred must be one-dimensional.")

    if len(y_true) == 0 or len(y_pred) == 0:
        raise ValueError("Prediction arrays cannot be empty.")

    if len(y_true) != len(y_pred):
        raise ValueError("y_true and y_pred must have equal lengths.")

    if pd_is_missing(y_true) or pd_is_missing(y_pred):
        raise ValueError("Labels cannot contain missing values.")

    labels = unique_labels(y_true, y_pred)

    if len(labels) < 2:
        raise ValueError("At least two classes are required.")

    results = {
        "accuracy": float(accuracy_score(y_true, y_pred)),
        "balanced_accuracy": float(
            balanced_accuracy_score(y_true, y_pred)
        ),
        "precision_macro": float(
            precision_score(
                y_true, y_pred, average="macro",
                labels=labels, zero_division=0
            )
        ),
        "recall_macro": float(
            recall_score(
                y_true, y_pred, average="macro",
                labels=labels, zero_division=0
            )
        ),
        "f1_macro": float(
            f1_score(
                y_true, y_pred, average="macro",
                labels=labels, zero_division=0
            )
        ),
        "precision_weighted": float(
            precision_score(
                y_true, y_pred, average="weighted",
                labels=labels, zero_division=0
            )
        ),
        "recall_weighted": float(
            recall_score(
                y_true, y_pred, average="weighted",
                labels=labels, zero_division=0
            )
        ),
        "f1_weighted": float(
            f1_score(
                y_true, y_pred, average="weighted",
                labels=labels, zero_division=0
            )
        ),
        "class_labels": labels.tolist(),
        "confusion_matrix": confusion_matrix(
            y_true, y_pred, labels=labels
        ).tolist(),
    }

    if y_proba is not None:
        probabilities = np.asarray(y_proba, dtype=float)

        if not np.isfinite(probabilities).all():
            raise ValueError("Probabilities must be finite.")

        if np.any(probabilities < 0) or np.any(probabilities > 1):
            raise ValueError("Probabilities must be between 0 and 1.")

        if len(labels) == 2:
            if probabilities.ndim == 2:
                if probabilities.shape != (len(y_true), 2):
                    raise ValueError(
                        "Binary probabilities must have two columns."
                    )
                probabilities = probabilities[:, 1]
            elif probabilities.ndim != 1 or len(probabilities) != len(y_true):
                raise ValueError(
                    "Binary probabilities must have one value per sample."
                )

            results["roc_auc"] = float(
                roc_auc_score(y_true, probabilities)
            )

        else:
            if probabilities.shape != (len(y_true), len(labels)):
                raise ValueError(
                    "Multiclass probabilities must have one column "
                    "per class."
                )

            if not np.allclose(probabilities.sum(axis=1), 1.0):
                raise ValueError(
                    "Each multiclass probability row must sum to 1."
                )

            results["roc_auc"] = float(
                roc_auc_score(
                    y_true,
                    probabilities,
                    labels=labels,
                    multi_class="ovr",
                    average="macro",
                )
            )

    return results


def pd_is_missing(values):
    """Check for missing values in a label array."""
    try:
        return bool(np.asarray(values != values).any()) or any(
            value is None for value in values
        )
    except (TypeError, ValueError):
        return any(value is None for value in values)
