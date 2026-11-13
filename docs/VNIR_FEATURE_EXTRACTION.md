# TerraSpectra – VNIR Spectral Feature Extraction and Correlation Analysis

## 1. Introduction

This document describes the spectral feature extraction and correlation analysis performed as part of the TerraSpectra – Hyperspectral Crop Disease Forecasting project.

The analysis focuses on the selected Visible and Near-Infrared (VNIR) hyperspectral scans.

The main objective was to investigate the spectral characteristics of the data, extract useful statistical and exploratory features, understand relationships between spectral bands, and identify potential redundancy before machine-learning model development.

This work forms the foundation for the next stage: final feature dataset preparation and validation.

## 2. Dataset Used

The analysis was performed using the selected VNIR scans:

- `01_D`
- `04_D`
- `07_D`
- `10_D`

Each hyperspectral cube contains:

| Property | Value |
|---|---:|
| Number of lines | 1,370 |
| Spectral bands | 216 |
| Number of samples | 1,024 |
| Wavelength range | Approximately 411.36–993.17 nm |
| Annotated pixel samples | 272,912 |

Ten leaf annotation files were examined during the dataset analysis.

The extracted pixel-level dataset contains 216 spectral-band columns and four additional metadata columns, resulting in a combined shape of 272,912 × 220.

## 3. Spectral Characteristics Analysis

The VNIR spectral range was investigated to understand how wavelength information is distributed across the 216 bands.

For exploratory analysis, the wavelength range was divided into five regions.

| Spectral region | Wavelength range | Number of bands |
|---|---:|---:|
| Blue | 411–500 nm | 33 |
| Green | 500–600 nm | 37 |
| Red | 600–700 nm | 37 |
| Red Edge | 700–750 nm | 19 |
| Near-Infrared (NIR) | 750–993 nm | 89 |
| Total | 411–993 nm | 215* |

*The region counts are the reported exploratory grouping. The exact band assignment at wavelength boundaries should be checked against the original wavelength array before treating these counts as a complete, mutually exclusive partition of all 216 bands.*

### Purpose

The wavelength grouping helps organize the spectral information into interpretable regions.

It supports:
- Understanding wavelength distribution.
- Comparing spectral regions.
- Investigating potentially informative wavelengths.
- Preparing for later feature selection.

## 4. Statistical Spectral Feature Extraction

Eight statistical measurements were calculated for each of the ten leaf mean spectral profiles.

The extracted features were:

1. Mean
2. Median
3. Standard deviation
4. Minimum
5. Maximum
6. 25th percentile
7. 75th percentile
8. Interquartile range (IQR)

### Purpose

These measurements summarize the distribution of spectral intensity values across wavelengths for each leaf.

They provide a compact statistical description that can be investigated during subsequent analysis.

The extracted statistics are exploratory features and are not yet confirmed to be predictive of disease.

## 5. Exploratory Spectral Indices

Three exploratory intensity-based ratios were calculated using selected wavelengths.

The wavelengths investigated were:

| Spectral region | Wavelength |
|---|---:|
| Green | 549.371 nm |
| Red | 679.264 nm |
| Red Edge | 706.325 nm |
| NIR | 860.573 nm |

The calculations included:

- Green–Red ratio.
- NDVI-like intensity ratio.
- NDRE-like intensity ratio.

### Scientific consideration

The current VNIR measurements are raw intensity measurements. They have not been established as calibrated reflectance values.

Therefore, the calculated ratios are exploratory intensity-based features.

They must not be presented as standard reflectance-based NDVI or NDRE.

Further calibration and methodological verification would be necessary before making such claims.

## 6. Correlation Analysis

Pearson correlation analysis was performed between all 216 VNIR spectral bands using 272,912 annotated pixel samples.

The purpose was to investigate the strength of relationships between different wavelength bands.

### 6.1 Correlation results

| Measurement | Result |
|---|---:|
| Spectral bands | 216 |
| Annotated pixel samples | 272,912 |
| Total unique band pairs | 23,220 |
| Pairs with absolute correlation ≥ 0.98 | 14 |
| Pairs with absolute correlation ≥ 0.95 | 4,670 |

### 6.2 Interpretation

The analysis indicates that many VNIR spectral bands have strong correlations.

The strongest correlations were mostly observed between nearby red-edge wavelengths.

The highest mean absolute correlations were observed around the 541–557 nm wavelength region.

These findings indicate substantial redundancy among some spectral bands.

However, high correlation alone does not establish that a particular band is unnecessary.

Further feature selection experiments are required to investigate whether reducing redundant bands improves model efficiency without losing useful disease-related information.

## 7. Preprocessing and Smoothing Considerations

During VNIR preprocessing, data quality was examined for invalid values, zero values and missing spectral measurements.

Short internal gaps of one or two bands were interpolated while preserving the original raw spectra.

The combined dataset was also checked for remaining missing values.

### Savitzky–Golay smoothing evaluation

Savitzky–Golay smoothing was evaluated using:

| Parameter | Value |
|---|---:|
| Window size | 11 |
| Polynomial order | 2 |
| Average smoothing change | Approximately 0.861% |

The smoothing method was investigated to understand its effect on spectral measurements.

It was not applied to the primary dataset at this stage.

The original data were retained, and smoothing remains an optional preprocessing approach for future comparison.

## 8. Important Data Quality Results

The following results were reported during the earlier preprocessing stage:

| Measurement | Result |
|---|---:|
| Combined pixel samples | 272,912 |
| Spectral bands per pixel | 216 |
| Combined dataset columns | 220 |
| Zero percentage | Approximately 0.05265% |
| 65535-value percentage | Approximately 0.00207% |
| Interpolated values | 24,695 |
| Remaining NaN values | 7,559 |

The remaining missing values must be handled carefully before model training.

Missing-value treatment should be determined using the training data only where applicable, to avoid information leakage during evaluation.

## 9. Generated Outputs

The following outputs were generated during VNIR feature extraction and analysis.

### Spectral characteristics

- `VNIR_spectral_characteristics.csv`
- `VNIR_spectral_characteristics.png`
- `VNIR_leaf_mean_spectra.csv`
- `VNIR_cleaned_mean_spectra.csv`
- `VNIR_leaf_spectral_comparison.png`

### Statistical and exploratory features

- `VNIR_statistical_features.csv`
- `VNIR_exploratory_spectral_indices.csv`

### Correlation and data quality

- `VNIR_band_correlation_pairs.csv`
- `VNIR_band_correlation_summary.csv`
- `VNIR_band_quality_report.csv`
- `VNIR_quality_report.csv`

### Smoothing evaluation

- `VNIR_smoothing_comparison.png`
- `VNIR_smoothing_evaluation.csv`

These outputs provide the basis for reviewing the extracted spectral information and preparing the final feature dataset.

Large raw and processed datasets remain stored locally and are excluded from Git commits to avoid unnecessary repository size increases.

## 10. Scientific Limitations

The following limitations must be considered when interpreting the results:

### 10.1 Raw intensity measurements

The VNIR data have not been established as calibrated reflectance. Reflectance-based vegetation index interpretations cannot be assumed.

### 10.2 Correlation does not establish feature importance

Highly correlated bands may contain overlapping information, but they may still contribute to classification performance.

### 10.3 Pixel-level dependence

Multiple pixels may belong to the same leaf or scan. These observations cannot automatically be treated as independent samples.

Training and testing must use an appropriate grouped splitting strategy.

### 10.4 Limited selected scans

The current analysis focuses on four selected scans and ten leaf annotation files. Broader generalization must be investigated using suitable independent observations.

### 10.5 Disease-related relevance

The extracted features have not yet been proven to distinguish healthy and infected leaves.

Their predictive value must be evaluated through properly designed experiments.

## 11. Pending Work – Step 3.5

The next stage is final feature dataset preparation.

Planned activities:

1. Review the extracted statistical and exploratory features.
2. Investigate remaining missing values.
3. Examine feature distributions.
4. Identify potential outliers.
5. Investigate redundant features.
6. Apply suitable feature selection techniques.
7. Validate the final feature dataset.
8. Preserve sample and group identifiers for leakage-safe model evaluation.

Feature selection decisions will be based on experimental evidence rather than correlation thresholds alone.

## 12. Conclusion

The VNIR spectral feature extraction and correlation analysis established an initial understanding of the selected hyperspectral data.

The work covered wavelength-region analysis, statistical feature extraction, exploratory intensity-based ratios, smoothing evaluation, data quality checks and correlation analysis across 216 spectral bands.

The results revealed substantial redundancy among some spectral bands and identified important considerations for subsequent feature preparation.

The next priority is to prepare and validate a reliable feature dataset before selecting and training machine-learning models.

No disease classification performance or early-detection capability is claimed at this stage.

---

**Project:** TerraSpectra – Hyperspectral Crop Disease Forecasting  
**Domain:** Data Science and Machine Learning  
**Analysis:** VNIR Spectral Feature Extraction  
**Status:** Steps 3.1–3.4 completed; Step 3.5 pending  
**Last Updated:** 13 November 2026