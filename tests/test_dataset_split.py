
import sys
import unittest
from pathlib import Path

import pandas as pd

# Make the src package available during testing.
sys.path.insert(
    0,
    str(Path(__file__).resolve().parents[1] / "src")
)

from terraspectra.dataset_split import split_dataset


def create_synthetic_data():
    """Create artificial grouped data for testing only."""
    rows = []

    for group_number in range(20):
        label = "infected" if group_number % 2 == 0 else "healthy"

        for observation in range(5):
            rows.append({
                "sample_id": f"sample_{group_number}",
                "label": label,
                "feature": group_number + observation,
            })

    return pd.DataFrame(rows)


class TestDatasetSplit(unittest.TestCase):

    def setUp(self):
        self.data = create_synthetic_data()

    def test_all_splits_are_created(self):
        result = split_dataset(
            self.data,
            label_col="label",
            group_col="sample_id",
        )

        self.assertEqual(
            set(result.keys()),
            {"train", "validation", "test", "class_distribution"},
        )

        self.assertGreater(len(result["train"]), 0)
        self.assertGreater(len(result["validation"]), 0)
        self.assertGreater(len(result["test"]), 0)

    def test_no_group_leakage(self):
        result = split_dataset(
            self.data,
            label_col="label",
            group_col="sample_id",
        )

        train = set(result["train"]["sample_id"])
        validation = set(result["validation"]["sample_id"])
        test = set(result["test"]["sample_id"])

        self.assertFalse(train & validation)
        self.assertFalse(train & test)
        self.assertFalse(validation & test)

    def test_reproducible_with_same_seed(self):
        first = split_dataset(
            self.data, "label", "sample_id", random_state=42
        )

        second = split_dataset(
            self.data, "label", "sample_id", random_state=42
        )

        for split_name in ("train", "validation", "test"):
            self.assertEqual(
                first[split_name].index.tolist(),
                second[split_name].index.tolist(),
            )

    def test_invalid_split_proportions(self):
        with self.assertRaises(ValueError):
            split_dataset(
                self.data,
                "label",
                "sample_id",
                test_size=0.7,
                val_size=0.4,
            )

    def test_missing_group_identifiers_are_rejected(self):
        invalid_data = self.data.copy()
        invalid_data.loc[0, "sample_id"] = None

        with self.assertRaises(ValueError):
            split_dataset(invalid_data, "label", "sample_id")

    def test_missing_labels_are_rejected(self):
        invalid_data = self.data.copy()
        invalid_data.loc[0, "label"] = None

        with self.assertRaises(ValueError):
            split_dataset(invalid_data, "label", "sample_id")


if __name__ == "__main__":
    unittest.main()
