
import unittest

import numpy as np

from terraspectra.spectral_band_statistics import (
    calculate_band_statistics,
)


class TestSpectralBandStatistics(unittest.TestCase):

    def setUp(self):
        self.spectra = np.array([
            [1.0, 10.0, 5.0],
            [2.0, 20.0, 5.0],
            [3.0, 30.0, 5.0],
            [4.0, 40.0, 5.0],
        ])

    def test_band_count(self):
        result = calculate_band_statistics(self.spectra)
        self.assertEqual(result.band_count, 3)

    def test_valid_count_per_band(self):
        result = calculate_band_statistics(self.spectra)
        np.testing.assert_array_equal(result.valid_count, [4, 4, 4])

    def test_mean_per_band(self):
        result = calculate_band_statistics(self.spectra)
        np.testing.assert_allclose(result.mean, [2.5, 25.0, 5.0])

    def test_standard_deviation_per_band(self):
        result = calculate_band_statistics(self.spectra)
        np.testing.assert_allclose(
            result.standard_deviation,
            [np.std([1, 2, 3, 4]), np.std([10, 20, 30, 40]), 0.0],
        )

    def test_minimum_and_maximum(self):
        result = calculate_band_statistics(self.spectra)
        np.testing.assert_allclose(result.minimum, [1, 10, 5])
        np.testing.assert_allclose(result.maximum, [4, 40, 5])

    def test_median(self):
        result = calculate_band_statistics(self.spectra)
        np.testing.assert_allclose(result.median, [2.5, 25.0, 5.0])

    def test_quartiles(self):
        result = calculate_band_statistics(self.spectra)
        np.testing.assert_allclose(result.percentile_25, [1.75, 17.5, 5.0])
        np.testing.assert_allclose(result.percentile_75, [3.25, 32.5, 5.0])

    def test_non_finite_values_are_excluded(self):
        spectra = np.array([
            [1.0, np.nan],
            [3.0, 2.0],
            [np.inf, 4.0],
        ])

        result = calculate_band_statistics(spectra)

        np.testing.assert_array_equal(result.valid_count, [2, 2])
        np.testing.assert_allclose(result.mean, [2.0, 3.0])

    def test_configured_invalid_codes_are_excluded(self):
        spectra = np.array([
            [1.0, 10.0],
            [0.0, 20.0],
            [3.0, 0.0],
        ])

        result = calculate_band_statistics(
            spectra,
            invalid_codes=[0],
        )

        np.testing.assert_array_equal(result.valid_count, [2, 2])
        np.testing.assert_allclose(result.mean, [2.0, 15.0])

    def test_entirely_invalid_band_returns_nan_statistics(self):
        spectra = np.array([
            [0.0, 1.0],
            [0.0, 2.0],
        ])

        result = calculate_band_statistics(
            spectra,
            invalid_codes=[0],
        )

        self.assertEqual(result.valid_count[0], 0)
        self.assertTrue(np.isnan(result.mean[0]))
        self.assertTrue(np.isnan(result.median[0]))

    def test_input_is_not_modified(self):
        original = self.spectra.copy()

        calculate_band_statistics(self.spectra)

        np.testing.assert_array_equal(self.spectra, original)

    def test_rejects_non_2d_input(self):
        with self.assertRaises(ValueError):
            calculate_band_statistics(np.array([1.0, 2.0]))

    def test_rejects_empty_input(self):
        with self.assertRaises(ValueError):
            calculate_band_statistics(np.empty((0, 3)))

    def test_rejects_non_numeric_input(self):
        with self.assertRaises(ValueError):
            calculate_band_statistics([["a", "b"]])


if __name__ == "__main__":
    unittest.main()
