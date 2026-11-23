
import numpy as np


def _validate_spectra(spectra):
    """Validate a 2D array of spectra (samples x spectral bands)."""
    data = np.asarray(spectra, dtype=float)

    if data.ndim != 2:
        raise ValueError("Spectra must be a 2D array.")

    if data.shape[0] == 0 or data.shape[1] == 0:
        raise ValueError("Spectra cannot be empty.")

    if not np.isfinite(data).all():
        raise ValueError(
            "Spectra contain NaN or infinite values. "
            "Handle invalid measurements before preprocessing."
        )

    return data


def snv_normalize(spectra, epsilon=1e-12):
    """
    Apply Standard Normal Variate normalization independently
    to each spectrum.

    Input shape: (samples, spectral_bands)
    """
    data = _validate_spectra(spectra)

    if epsilon <= 0:
        raise ValueError("Epsilon must be positive.")

    row_means = np.mean(data, axis=1, keepdims=True)
    row_stds = np.std(data, axis=1, keepdims=True)

    if np.any(row_stds <= epsilon):
        raise ValueError(
            "SNV cannot normalize a constant or near-constant spectrum."
        )

    return (data - row_means) / row_stds


def moving_average_smoothing(spectra, window_size=5):
    """
    Apply moving-average smoothing along the spectral-band axis.

    The window size must be a positive odd integer.
    Edge values are padded to preserve the original shape.
    """
    data = _validate_spectra(spectra)

    if not isinstance(window_size, (int, np.integer)):
        raise ValueError("Window size must be an integer.")

    if window_size < 1 or window_size % 2 == 0:
        raise ValueError("Window size must be a positive odd integer.")

    if window_size > data.shape[1]:
        raise ValueError(
            "Window size cannot exceed the number of spectral bands."
        )

    if window_size == 1:
        return data.copy()

    padding = window_size // 2
    kernel = np.ones(window_size, dtype=float) / window_size

    padded = np.pad(
        data,
        pad_width=((0, 0), (padding, padding)),
        mode="edge",
    )

    smoothed = np.apply_along_axis(
        lambda row: np.convolve(row, kernel, mode="valid"),
        axis=1,
        arr=padded,
    )

    return smoothed
