# VNIR Final Feature Dataset Structure

## Purpose
Prepare two pixel-level VNIR feature datasets for later modelling.

## Dataset versions

### 1. Baseline dataset
- Metadata columns: 7
- Spectral feature columns: 216
- Expected total columns: 223

### 2. Candidate dataset
- Metadata columns: 7
- Spectral feature columns: 30
- Candidate wavelength range: 730-810 nm
- Expected total columns: 37

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
- Do not remove spectral bands at this preparation stage.
- Keep baseline and candidate datasets separate.
- Use group-aware validation in later modelling to prevent pixel-level leakage.

## Current status
Structure defined. Dataset generation and validation are pending.
