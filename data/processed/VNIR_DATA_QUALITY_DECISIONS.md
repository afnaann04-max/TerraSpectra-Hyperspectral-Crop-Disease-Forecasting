# VNIR Data Quality Decisions

Date: 13 November 2026

## Missing-value gap classification

               Gap_Sequences  Missing_Values
Gap_Type                                    
Leading edge             555             715
Long internal           1434            6358
Trailing edge            249             486

Total missing values classified: 7559

## Handling decisions

- Leading and trailing edge gaps: retained as NaN.
- Internal gaps of 3 or more bands: retained as NaN.
- Short internal gaps of 1-2 bands: none remain.
- No additional interpolation was performed.
- Original spectral measurements were preserved.

## Outlier decisions

- IQR-flagged values: 11191908
- Values at or above 65,000: 1974
- IQR flags are statistical indicators, not proof of measurement errors.
- High-intensity values are retained for further review.
- No spectral values were deleted based on these flags.

## Validation

- Missing values before handling: 7559
- Missing values after handling: 7559
- Original combined dataset modified: No
- Missing-value preservation check: PASS

## Conclusion

The missing-value patterns have been classified and documented.
No further interpolation or deletion is justified at this stage.
The combined VNIR dataset remains unchanged.
