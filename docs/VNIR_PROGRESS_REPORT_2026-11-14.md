# VNIR Progress Report — 14 November 2026

## Project status
VNIR dataset investigation, preprocessing validation, biological replication review and acquisition-confounding assessment.

## 1. Completed work

- Inspected repository structure and available datasets.
- Created the dataset inventory.
- Validated the corrected VNIR spectral data and NPZ quality checks.
- Investigated biological replication and repeated sampling.
- Reviewed acquisition metadata for the four selected raw VNIR scans.
- Documented the limitations affecting machine-learning evaluation.

## 2. Biological replication findings

- The VNIR sampling metadata contains 48 pot records.
- Pots 01–12 have sampling records at six DPI dates.
- Pots 13–48 have sampling records at 18 DPI dates.
- One technical NA entry was recorded at DPI 10.
- The metadata does not provide individual plant IDs.
- The number of plants per pot could not be confirmed.
- Pot is therefore the available experimental grouping unit, but its equivalence to one individual plant is unconfirmed.

## 3. Acquisition and confounding findings

The selected raw VNIR scans represent four pots:

- 01_D: EPO_68, infected
- 04_D: EPO_68, non-infected
- 07_D: EPO_67, infected
- 10_D: EPO_67, non-infected

All four scans have identical recorded image dimensions, spectral bands, integration time and frame period.

However, both infected scans were acquired before both non-infected scans on 11 March 2021.

This creates a potential acquisition-time confounder. There is only one pot per genotype-treatment combination in this selected subset.

## 4. Machine-learning implications

- Pixels are not independent biological samples.
- Random pixel-level splitting risks data leakage.
- Independent biological groups should be used for validation.
- The selected four-scan subset supports exploratory analysis, not strong generalization claims.
- More independent samples and acquisition information are needed for reliable disease-classification evaluation.

## 5. Current limitations

- Plant count per pot is unconfirmed.
- Individual plant identifiers are unavailable.
- Selected raw VNIR scans have low biological replication.
- Acquisition-time ordering is aligned with treatment.
- Corrected NPZ generation-script provenance remains unconfirmed.

## 6. Next project activities

- Complete SWIR and RGB dataset investigations.
- Confirm dataset availability and metadata across modalities.
- Establish a leakage-resistant experimental design.
- Select suitable models only after validating the independent experimental units.
- Integrate explainability and the demonstration application.

## 7. Overall status

VNIR dataset investigation: completed for the currently available selected scans.

Preprocessing and numerical quality validation: completed.

Biological replication and acquisition limitations: investigated and documented.

Model training: not started; experimental design limitations must be addressed first.
