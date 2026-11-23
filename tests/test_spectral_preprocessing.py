import unittest
import numpy as np

from terraspectra.spectral_preprocessing import (
    snv_normalize,
    moving_average_smoothing,
)


class TestSpectralPreprocessing(unittest.TestCase):

    def setUp(self):
        self.spectra = np.array([
            [1.0, 2.0, 3.0, 4.0, 5.0],
            [2.0, 4.0, 6.0, 8.0, 10.0],
        ])

    def test_snv_zero_mean(self):
        result = snv_normalize(self.spectra)
        np.testing.assert_allclose(
            result.mean(axis=1), [0.0, 0.0], atol=1e-12
        )

    def test_snv_unit_standard_deviation(self):
        result = snv_normalize(self.spectra)
        np.testing.assert_allclose(
            result.std(axis=1), [1.0, 1.0], atol=1e-12
        )

    def test_snv_preserves_shape(self):
        self.assertEqual(
            snv_normalize(self.spectra).shape, self.spectra.shape
        )

    def test_snv_rejects_constant_spectrum(self):
        with self.assertRaises(ValueError):
            snv_normalize(np.array([[2.0, 2.0, 2.0]]))

    def test_snv_rejects_non_finite_values(self):
        with self.assertRaises(ValueError):
            snv_normalize(np.array([[1.0, np.nan, 3.0]]))

    def test_smoothing_preserves_shape(self):
        result = moving_average_smoothing(self.spectra, window_size=3)
        self.assertEqual(result.shape, self.spectra.shape)

    def test_smoothing_reduces_local_spike(self):
        spectrum = np.array([[1.0, 1.0, 10.0, 1.0, 1.0]])
        result = moving_average_smoothing(spectrum, window_size=3)
        self.assertLess(result[0, 2], spectrum[0, 2])

    def test_smoothing_window_one_returns_same_values(self):
        result = moving_average_smoothing(self.spectra, window_size=1)
        np.testing.assert_array_equal(result, self.spectra)

    def test_smoothing_rejects_even_window(self):
        with self.assertRaises(ValueError):
            moving_average_smoothing(self.spectra, window_size=2)

    def test_smoothing_rejects_window_larger_than_bands(self):
        with self.assertRaises(ValueError):
            moving_average_smoothing(self.spectra, window_size=7)

    def test_smoothing_rejects_non_finite_values(self):
        with self.assertRaises(ValueError):
            moving_average_smoothing(
                np.array([[1.0, np.inf, 3.0]]), window_size=3
            )


if __name__ == "__main__":
    unittest.main()