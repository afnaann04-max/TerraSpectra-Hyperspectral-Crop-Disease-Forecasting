# VNIR Final Dataset Validation Report

**Date:** 13 November 2026  
**Project:** TerraSpectra ? Hyperspectral Crop Disease Forecasting  
**Status:** All final dataset validation checks passed

## 1. Dataset overview

Two VNIR feature datasets were prepared:

| Dataset | Pixel records | Metadata columns | Spectral bands | Total columns |
|---|---:|---:|---:|---:|
| Baseline | 272,912 | 7 | 216 | 223 |
| Candidate | 272,912 | 7 | 30 | 37 |

Metadata columns:
- Scan_ID
- Leaf_ID
- X
- Y
- Treatment
- Genotype
- Confidence

The prediction target is `Treatment`. Scan_ID and Leaf_ID identify the sample groups. Genotype and Confidence are retained for traceability.

## 2. Sample identity and label validation

Both datasets passed the following checks:

- 272,912 pixel records.
- 10 expected leaves.
- Zero duplicate pixel identities.
- No leaf linked to multiple scans.
- No leaf with conflicting treatment labels.
- Zero label mismatches.
- No unexpected or missing leaves.
- Baseline and candidate contain identical pixel identities and labels.

Treatment distribution:
- Infected: 6 leaves.
- Non-infected: 4 leaves.

The pixel identities and treatment labels match exactly between the two datasets.

## 3. Spectral data quality validation

| Check | Baseline | Candidate |
|---|---:|---:|
| Missing spectral values | 7,559 | 13 |
| Infinite values | 0 | 0 |
| Negative values | 0 | 0 |
| Zero values | 0 | 0 |
| Exact 65,535 values | 0 | 0 |
| Values above 65,535 | 0 | 0 |
| Missing metadata values | 0 | 0 |
| Minimum finite intensity | 1 | 1 |
| Maximum finite intensity | 65,534 | 65,524 |

Both datasets contain the expected 272,912 records.

Missing spectral values were retained rather than silently imputed or removed. Their handling must be decided within the modelling workflow, using training data only where applicable.
### Processing-stage distinction

The 7,559 missing values in the baseline CSV correspond to the original combined VNIR dataset.

The separately corrected NPZ spectra contain 8,282 NaNs. The additional 723 NaNs correspond to raw values of 4095, which are declared as data ignore values in the VNIR headers.

The corrected NPZ outputs and the CSV feature datasets therefore have matching pixel coordinates but are not spectrally identical.

The candidate CSV contains 13 missing values because it retains only the selected 30 baseline bands.

## 4. Baseline and candidate consistency

The cross-dataset comparison confirmed:

- Both datasets have the same row count.
- Metadata and pixel order match exactly.
- All 30 candidate bands exist in the 216-band baseline.
- Candidate metadata matches the expected structure.
- Candidate contains exactly 30 spectral bands.
- All candidate spectral values match the corresponding baseline values across all 272,912 records.

Therefore, the candidate dataset is a consistent reduced-feature version of the baseline dataset.
The baseline and candidate comparisons above apply to the CSV feature datasets. They do not establish spectral identity between those CSV files and the separately corrected NPZ outputs.

## 5. Final validation result

| Validation area | Result |
|---|---|
| Dataset dimensions and structure | PASS |
| Pixel identity and label validation | PASS |
| Missing-value and invalid-value inspection | PASS |
| Baseline/candidate consistency | PASS |

All four validation areas passed.

## 6. Important limitations and modelling considerations

1. The current validated datasets represent the selected VNIR data only. This does not establish completion of SWIR or RGB integration.
2. The spectral values are raw intensity measurements, not calibrated reflectance.
3. Missing spectral values remain in both datasets and require an explicit modelling-stage handling strategy.
4. The data contain 10 leaf samples across four scans. Pixel-level random splitting could cause data leakage.
5. Model evaluation should use appropriate group-aware splitting, keeping related pixels from the same leaf or scan together as required by the experimental design.
6. The candidate 30-band dataset is a reduced-feature experiment, not yet proven superior to the 216-band baseline.
7. These checks validate dataset structure and consistency; they do not demonstrate disease prediction performance or early-detection capability.

## 7. Conclusion

The VNIR baseline and candidate feature datasets passed the final structural, identity, label, data-quality, and cross-dataset consistency checks.

Both datasets are preserved with their original validated pixel records and metadata. They are ready to enter the next modelling preparation stage, where missing-value handling, group-aware data splitting, feature selection evaluation, and model training will be addressed.

**Final status: VNIR Step 3.5 CSV dataset validation completed successfully.**


The corrected NPZ outputs have also passed the separate numerical invalid-value, interpolation and coordinate-alignment audits.
