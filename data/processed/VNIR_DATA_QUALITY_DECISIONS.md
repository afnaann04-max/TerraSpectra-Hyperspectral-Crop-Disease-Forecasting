# VNIR Data Quality Decisions

Date: 13 November 2026
Additional corrected-NPZ verification: 14 November 2026

## 1. Original combined VNIR dataset

The original combined VNIR CSV contains:
- 272,912 pixel records.
- 216 spectral bands.
- 7,559 missing spectral values.

### Missing-value gap classification

               Gap_Sequences  Missing_Values
Gap_Type
Leading edge             555             715
Long internal           1434            6358
Trailing edge            249             486

Total missing values classified: 7559

These missing values were retained in the original combined dataset.

## 2. Original dataset handling decisions

- Leading and trailing edge gaps: retained as NaN.
- Internal gaps of 3 or more bands: retained as NaN.
- No additional interpolation or deletion was performed on the original combined CSV.
- Original spectral measurements were preserved.

## 3. Corrected NPZ processing verification

The raw VNIR headers declare 4095 as the data ignore value.

The corrected NPZ files were audited for three invalid raw-value categories:

| Raw value | Meaning | Total occurrences |
|---|---|---:|
| 0 | Zero values | 31,036 |
| 65535 | Saturation values | 1,218 |
| 4095 | Header-declared ignore value | 723 |
| Total | | 32,977 |

The corrected NPZ audit verified:
- All 4095 values were converted to NaN.
- Invalid internal gaps of 1-2 bands were interpolated where possible.
- Internal gaps of 3 or more bands were retained as NaN.
- Leading and trailing gaps were retained as NaN.
- All 24,695 finite replacement values matched linear interpolation between neighbouring valid spectral bands.
- No valid raw measurements were changed.
- Total corrected NPZ NaNs: 8,282.

The original combined CSV and corrected NPZ spectra are not identical. Their coordinates match, but the corrected NPZ contains 723 additional NaNs corresponding to header-ignore values.

## 4. Outlier decisions

- IQR-flagged values: 11,191,908
- Values at or above 65,000: 1,974
- IQR flags are statistical indicators, not proof of measurement errors.
- High-intensity values are retained for further review.
- No spectral values were deleted based on these flags.

## 5. Baseline and candidate CSV datasets

- Baseline missing spectral values: 7,559.
- Candidate missing spectral values: 13.
- Candidate missing-value count matches the selected baseline bands.
- Candidate values match the corresponding baseline spectral values.

These CSV datasets retain their original validated values. The corrected NPZ processing should be treated as a separate output.

## 6. Conclusion

The original combined VNIR CSV remains unchanged.
The corrected NPZ outputs have passed the numerical invalid-value and interpolation checks.
The baseline and candidate CSV datasets have passed structural and cross-dataset consistency checks.

Missing-value handling for model training must be decided within the modelling workflow, using training data only where applicable.
