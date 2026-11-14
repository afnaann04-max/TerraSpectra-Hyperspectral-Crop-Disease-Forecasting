# VNIR Final Feature Dataset Structure

## Purpose
Prepare and validate two pixel-level VNIR feature datasets for later modelling.

## Dataset versions

### 1. Baseline dataset
- Pixel records: 272,912
- Metadata columns: 7
- Spectral feature columns: 216
- Total columns: 223

### 2. Candidate dataset
- Pixel records: 272,912
- Metadata columns: 7
- Spectral feature columns: 30
- Candidate wavelength range: 730.680-809.157 nm
- Total columns: 37

## Metadata columns
1. Scan_ID
2. Leaf_ID
3. X
4. Y
5. Treatment
6. Genotype
7. Confidence

## Target and feature rules
- Target: Treatment (Infected / Non-infected).
- Spectral intensity columns are the model feature candidates.
- Scan_ID and Leaf_ID are grouping identifiers, not model predictors.
- X and Y preserve spatial pixel identity.
- Genotype and Confidence are retained for traceability.
- Metadata columns must not be accidentally included as spectral predictors.

## Data handling
- Preserve the original combined VNIR dataset.
- Keep missing values visible; do not silently impute or delete rows.
- Keep baseline and candidate datasets separate.
- The candidate dataset contains 30 selected bands from the baseline.
- Use group-aware validation in later modelling to prevent pixel-level leakage.
- The corrected NPZ spectra are a separate processing output and must not be assumed identical to the original combined CSV.

## Validation results
- All 272,912 pixel records are retained.
- All 10 leaves are represented.
- NPZ coordinates match the combined, baseline and candidate datasets.
- Coordinate order is preserved.
- Baseline spectral values match the combined dataset.
- Candidate spectral values match the corresponding 30 baseline bands.
- No duplicate, missing or extra coordinates were detected.

## Current status
Baseline and candidate dataset generation and structural validation are complete.
Further modelling preparation, missing-value handling and group-aware model evaluation remain.
