
import unittest
import pandas as pd

from terraspectra.dataset_validation import validate_dataset


class TestDatasetValidation(unittest.TestCase):

    def setUp(self):
        self.data = pd.DataFrame({
            "spectral_band_1": [0.25, 0.35, 0.45, 0.55],
            "disease_status": ["healthy", "infected", "healthy", "infected"],
            "sample_id": ["S1", "S2", "S3", "S4"],
        })

    def test_valid_dataset(self):
        report = validate_dataset(
            self.data, "disease_status", "sample_id"
        )
        self.assertTrue(report.valid)
        self.assertEqual(report.rows, 4)
        self.assertEqual(report.columns, 3)

    def test_missing_values_detected(self):
        data = self.data.copy()
        data.loc[0, "spectral_band_1"] = None

        report = validate_dataset(data, "disease_status", "sample_id")
        self.assertEqual(report.missing_values, 1)
        self.assertFalse(report.valid)

    def test_duplicate_rows_detected(self):
        data = pd.concat([self.data, self.data.iloc[[0]]], ignore_index=True)

        report = validate_dataset(data, "disease_status", "sample_id")
        self.assertEqual(report.duplicate_rows, 1)
        self.assertFalse(report.valid)

    def test_missing_labels_detected(self):
        data = self.data.copy()
        data.loc[0, "disease_status"] = None

        report = validate_dataset(data, "disease_status", "sample_id")
        self.assertEqual(report.missing_labels, 1)
        self.assertFalse(report.valid)

    def test_missing_groups_detected(self):
        data = self.data.copy()
        data.loc[0, "sample_id"] = None

        report = validate_dataset(data, "disease_status", "sample_id")
        self.assertEqual(report.missing_groups, 1)
        self.assertFalse(report.valid)

    def test_missing_required_column(self):
        with self.assertRaises(ValueError):
            validate_dataset(self.data, "unknown_label", "sample_id")

    def test_empty_dataset_rejected(self):
        with self.assertRaises(ValueError):
            validate_dataset(
                pd.DataFrame(columns=self.data.columns),
                "disease_status",
                "sample_id",
            )

    def test_non_dataframe_rejected(self):
        with self.assertRaises(TypeError):
            validate_dataset([], "disease_status", "sample_id")


if __name__ == "__main__":
    unittest.main()
