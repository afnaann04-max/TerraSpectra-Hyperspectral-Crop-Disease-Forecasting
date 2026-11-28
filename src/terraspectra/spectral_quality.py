
from dataclasses import dataclass
from typing import Iterable

import numpy as np


@dataclass
class SpectralQualityReport:
    """Summary of quality checks for a spectral matrix."""

    sample_count: int
    band_count: int
    nan_count: int
    positive_infinity_count: int
    negative_infinity_count: int
    invalid_value_counts: dict
    invalid_value_counts_per_band: dict
    invalid_percentage_per_band: dict
    total_invalid_count: int
    total_invalid_percentage: float
    constant_bands: list
    entirely_invalid_bands: list


def audit_spectral_quality(
    spectra,
    invalid_codes: Iterable[float] = (),
    tolerance: float = 0.0,
):
    """
    Audit a 2D spectral matrix without modifying its measurements.

    Parameters
    ----------
    spectra:
        Numeric array shaped (samples, spectral_bands).
    invalid_codes:
        Optional dataset-specific values that should be treated as invalid.
    tolerance:
        Maximum difference between valid values for a band to be
        considered constant. Must be finite and non-negative.
    """
    try:
        data = np.asarray(spectra, dtype=float)
    except (TypeError, ValueError) as exc:
        raise ValueError("Spectra must contain numeric values.") from exc

    if data.ndim != 2:
        raise ValueError("Spectra must be a 2D array.")

    if data.shape[0] == 0 or data.shape[1] == 0:
        raise ValueError("Spectra cannot be empty.")

    if not np.isfinite(tolerance) or tolerance < 0:
        raise ValueError("Tolerance must be finite and non-negative.")

    try:
        codes = list(invalid_codes)
        codes = np.asarray(codes, dtype=float)
    except (TypeError, ValueError) as exc:
        raise ValueError("Invalid codes must be numeric.") from exc

    if codes.ndim != 1:
        raise ValueError("Invalid codes must be a one-dimensional collection.")

    if not np.isfinite(codes).all():
        raise ValueError("Invalid codes must be finite numeric values.")

    nan_mask = np.isnan(data)
    positive_inf_mask = np.isposinf(data)
    negative_inf_mask = np.isneginf(data)

    non_finite_mask = ~np.isfinite(data)
    code_masks = {
        float(code): data == code
        for code in np.unique(codes)
    }

    code_invalid_mask = np.zeros(data.shape, dtype=bool)

    for mask in code_masks.values():
        code_invalid_mask |= mask

    invalid_mask = non_finite_mask | code_invalid_mask

    invalid_value_counts = {
        code: int(mask.sum())
        for code, mask in code_masks.items()
    }

    invalid_value_counts_per_band = {
        band: {
            code: int(mask[:, band].sum())
            for code, mask in code_masks.items()
        }
        for band in range(data.shape[1])
    }

    invalid_percentage_per_band = {
        band: float(invalid_mask[:, band].sum() / data.shape[0] * 100)
        for band in range(data.shape[1])
    }

    constant_bands = []
    entirely_invalid_bands = []

    for band in range(data.shape[1]):
        valid_values = data[~invalid_mask[:, band], band]

        if valid_values.size == 0:
            entirely_invalid_bands.append(band)
            continue

        if np.max(valid_values) - np.min(valid_values) <= tolerance:
            constant_bands.append(band)

    total_invalid_count = int(invalid_mask.sum())
    total_values = data.size

    return SpectralQualityReport(
        sample_count=int(data.shape[0]),
        band_count=int(data.shape[1]),
        nan_count=int(nan_mask.sum()),
        positive_infinity_count=int(positive_inf_mask.sum()),
        negative_infinity_count=int(negative_inf_mask.sum()),
        invalid_value_counts=invalid_value_counts,
        invalid_value_counts_per_band=invalid_value_counts_per_band,
        invalid_percentage_per_band=invalid_percentage_per_band,
        total_invalid_count=total_invalid_count,
        total_invalid_percentage=float(
            total_invalid_count / total_values * 100
        ),
        constant_bands=constant_bands,
        entirely_invalid_bands=entirely_invalid_bands,
    )
