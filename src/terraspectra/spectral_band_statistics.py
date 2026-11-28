
from dataclasses import dataclass
from typing import Iterable

import numpy as np


@dataclass
class SpectralBandStatistics:
    """Descriptive statistics calculated independently for each band."""

    band_count: int
    valid_count: np.ndarray
    mean: np.ndarray
    standard_deviation: np.ndarray
    minimum: np.ndarray
    maximum: np.ndarray
    median: np.ndarray
    percentile_25: np.ndarray
    percentile_75: np.ndarray


def calculate_band_statistics(
    spectra,
    invalid_codes: Iterable[float] = (),
):
    """
    Calculate descriptive statistics for each spectral band.

    Parameters
    ----------
    spectra:
        Numeric array shaped (samples, spectral_bands).
    invalid_codes:
        Optional dataset-specific values to exclude from calculations.

    Non-finite values and configured invalid codes are excluded.
    The input data is not modified.
    """
    try:
        data = np.asarray(spectra, dtype=float)
    except (TypeError, ValueError) as exc:
        raise ValueError("Spectra must contain numeric values.") from exc

    if data.ndim != 2:
        raise ValueError("Spectra must be a 2D array.")

    if data.shape[0] == 0 or data.shape[1] == 0:
        raise ValueError("Spectra cannot be empty.")

    try:
        codes = np.asarray(list(invalid_codes), dtype=float)
    except (TypeError, ValueError) as exc:
        raise ValueError("Invalid codes must be numeric.") from exc

    if codes.ndim != 1:
        raise ValueError("Invalid codes must be a one-dimensional collection.")

    if not np.isfinite(codes).all():
        raise ValueError("Invalid codes must be finite numeric values.")

    valid_mask = np.isfinite(data)

    for code in np.unique(codes):
        valid_mask &= data != code

    band_count = data.shape[1]
    valid_counts = valid_mask.sum(axis=0).astype(int)

    statistic_names = (
        "mean",
        "standard_deviation",
        "minimum",
        "maximum",
        "median",
        "percentile_25",
        "percentile_75",
    )

    results = {
        name: np.full(band_count, np.nan, dtype=float)
        for name in statistic_names
    }

    for band in range(band_count):
        values = data[valid_mask[:, band], band]

        if values.size == 0:
            continue

        results["mean"][band] = np.mean(values)
        results["standard_deviation"][band] = np.std(values)
        results["minimum"][band] = np.min(values)
        results["maximum"][band] = np.max(values)
        results["median"][band] = np.median(values)
        results["percentile_25"][band] = np.percentile(values, 25)
        results["percentile_75"][band] = np.percentile(values, 75)

    return SpectralBandStatistics(
        band_count=band_count,
        valid_count=valid_counts,
        **results,
    )
