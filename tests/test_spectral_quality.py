
import unittest

import numpy as np

from terraspectra.spectral_quality import audit_spectral_quality


class TestSpectralQuality(unittest.TestCase):

    def setUp(self):
        self.spectra = np.array([
            [1.0, 2.0, 0.0],
            [1.0, 3.0, 0.0],
            [1.0, np.nan, 0.0],
        ])

    def test_report_contains_sample_and_band_counts(self):
        report = audit_spectral_quality(self.spectra, invalid_codes=[0])

        self.assertEqual(report.sample_count, 3)
        self.assertEqual(report.band_count, 3)

    def test_nan_values_are_counted(self):
        report = audit_spectral_quality(self.spectra)

        self.assertEqual(report.nan_count, 1)
        self.assertEqual(report.total_invalid_count, 1)

    def test_infinity_values_are_counted(self):
        spectra = np.array([[1.0, np.inf], [2.0, -np.inf]])

        report = audit_spectral_quality(spectra)

        self.assertEqual(report.positive_infinity_count, 1)
        self.assertEqual(report.negative_infinity_count, 1)
        self.assertEqual(report.total_invalid_count, 2)

    def test_configured_invalid_codes_are_counted(self):
        report = audit_spectral_quality(
            self.spectra,
            invalid_codes=[0],
        )

        self.assertEqual(report.invalid_value_counts[0.0], 3)
        self.assertEqual(report.total_invalid_count, 4)

    def test_invalid_percentage_per_band(self):
        report = audit_spectral_quality(
            self.spectra,
            invalid_codes=[0],
        )

        self.assertAlmostEqual(
            report.invalid_percentage_per_band[0], 0.0
        )
        self.assertAlmostEqual(
            report.invalid_percentage_per_band[1], 100 / 3
        )
        self.assertAlmostEqual(
            report.invalid_percentage_per_band[2], 100.0
        )

    def test_invalid_code_counts_per_band(self):
        report = audit_spectral_quality(
            self.spectra,
            invalid_codes=[0],
        )

        self.assertEqual(
            report.invalid_value_counts_per_band[2][0.0], 3
        )

    def test_constant_band_is_detected(self):
        report = audit_spectral_quality(self.spectra)

        self.assertIn(0, report.constant_bands)

    def test_entirely_invalid_band_is_detected(self):
        report = audit_spectral_quality(
            self.spectra,
            invalid_codes=[0],
        )

        self.assertIn(2, report.entirely_invalid_bands)

    def test_original_data_is_not_modified(self):
        spectra = np.array([[1.0, 0.0], [2.0, 0.0]])
        original = spectra.copy()

        audit_spectral_quality(spectra, invalid_codes=[0])

        np.testing.assert_array_equal(spectra, original)

    def test_rejects_non_2d_input(self):
        with self.assertRaises(ValueError):
            audit_spectral_quality(np.array([1.0, 2.0, 3.0]))

    def test_rejects_empty_input(self):
        with self.assertRaises(ValueError):
            audit_spectral_quality(np.empty((0, 3)))

    def test_rejects_negative_tolerance(self):
        with self.assertRaises(ValueError):
            audit_spectral_quality(self.spectra, tolerance=-1)

    def test_rejects_non_numeric_input(self):
        with self.assertRaises(ValueError):
            audit_spectral_quality([["a", "b"]])


if __name__ == "__main__":
    unittest.main()
