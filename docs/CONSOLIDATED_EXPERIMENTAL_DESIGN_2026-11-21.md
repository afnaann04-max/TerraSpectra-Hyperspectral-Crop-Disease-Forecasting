# TerraSpectra – Consolidated Experimental Design Framework

**Project:** TerraSpectra – Hyperspectral Crop Disease Forecasting
**Document date:** 21 November 2026
**Status:** Preliminary experimental-design framework – pending team review
**Prepared by:** Hiba
**Project stage:** Dataset suitability and experimental-design review

---

## 1. Purpose

This document defines a scientifically defensible experimental approach for the available VNIR, SWIR and RGB datasets.

The objectives are to:

- Define a suitable research task for each dataset.
- Identify the correct experimental or grouping unit.
- Establish leakage-resistant validation principles.
- Select appropriate evaluation metrics.
- Identify evidence required before preprocessing and model development.
- Avoid unsupported disease-forecasting and multimodal-fusion claims.

The experimental scope remains provisional until the outstanding dataset investigations are reviewed.

## 2. Overall experimental strategy

The project will initially follow three separate experimental tracks:

1. VNIR hyperspectral analysis – Wheat Septoria.
2. SWIR hyperspectral analysis – Wheat Septoria.
3. RGB image analysis – selected crop-disease datasets.

The three tracks must remain independent during initial experiments.

VNIR, SWIR and RGB datasets must not be directly combined merely because they concern crop diseases. Their crops, acquisition systems, spectral characteristics, experimental conditions and labels differ.

A common project-level evaluation framework can be used, but individual models and results must be reported separately.

## 3. Dataset-specific experimental objectives

### 3.1 VNIR – Wheat Septoria

**Proposed initial objective:** Exploratory spectral analysis.

Available evidence includes four inspected raw hyperspectral scans, a 216-band baseline and metadata covering 48 pots and 279 leaf-level records.

Important limitations:

- Only four raw scans were found in the inspected VNIR directory.
- Reflectance-calibration provenance for the local processed data remains unverified.
- Individual leaf tracking across sampling dates is uncertain.
- Acquisition-time differences may confound infected and non-infected comparisons.
- Four scans are insufficient to establish reliable independent classification or generalisation.

**Proposed experimental direction:**

- Preserve the original spectral measurements.
- Verify data format and calibration provenance before processing.
- Conduct exploratory spectral-quality and distribution analysis only after data-readiness approval.
- Investigate whether disease-related spectral differences can be distinguished from acquisition and experimental confounding.

**Current decision:** Exploratory analysis only. Validated classification, severity estimation and forecasting are not approved.

### 3.2 SWIR – Wheat Septoria

**Proposed initial objective:** Exploratory spectral analysis and conditional disease-detection investigation.

The published dataset description reports:

- 48 pots.
- Two wheat genotypes.
- Infected and non-infected treatments.
- 279 leaf-level records.
- 256 spectral channels.
- Multiple days post inoculation.

The historical 96/96 pot-side scan matching result is documented, but original raw headers and calibration references remain unavailable for independent technical verification.

**Proposed experimental direction:**

- Obtain the original archive and supporting acquisition files.
- Verify header metadata, spectral bands, dimensions and raw binary layout.
- Confirm calibration references and acquisition settings.
- Assess missing observations and biological sample relationships.
- Design exploratory spectral analysis only after technical readiness is established.

**Current decision:** Technical verification is pending. Preprocessing and supervised modelling are not approved.

### 3.3 RGB – Rice Sheath Blight

**Proposed objective:** Image-level severity estimation.

The dataset description reports 1,609 original field images and six progressive severity levels.

However, the exact class definitions, severity boundaries and image-to-label mapping remain unresolved.

**Proposed experimental direction:**

- Verify the six severity definitions and annotation structure.
- Inspect the archive and establish image-to-label correspondence.
- Identify original plant or specimen groupings if available.
- Determine whether the six labels represent ordered severity levels.
- If supported, evaluate both classification performance and severity-aware errors.

**Current decision:** Promising severity-estimation candidate, but supervised modelling remains on hold until labels and archive structure are verified.

### 3.4 RGB – NWRD Wheat Rust

**Proposed objective:** Binary rust segmentation.

The source reports 100 images and corresponding binary segmentation masks.

Outstanding issues include dataset reuse permission, archive integrity, image-mask pairing and the discrepancy between the paper and repository split descriptions.

**Proposed experimental direction:**

- Confirm permission to reuse the dataset.
- Verify image and mask counts and correspondence.
- Inspect mask pixel values and annotation meaning.
- Establish the authoritative split and whether sample grouping is available.
- If verified, conduct a separate binary segmentation experiment.

**Current decision:** Conditional candidate. Modelling remains on hold.

### 3.5 RGB – CCMT Tomato

**Proposed objective:** Five-class image-level classification.

The available archive inspection identified 27,158 images:

- 21,723 training images.
- 5,435 test images.

The archive contains five reported tomato classes. The publication reports 27,178 augmented images, leaving a 20-image discrepancy.

Filename-based matching produced 4,085 matches. This is not a verified duplicate count. The inspected cross-class filename pair had different SHA-256 hashes.

Outstanding issues include original-to-augmented relationships, possible train/test leakage, near-duplicates and biological sample grouping.

**Proposed experimental direction:**

- Resolve the 20-image discrepancy.
- Establish original-to-augmented relationships.
- Investigate possible leakage across the supplied train/test partitions.
- Determine whether a defensible group-aware split can be constructed.
- Confirm the final class-to-image mapping.

**Current decision:** Conditional classification candidate. Modelling approval remains pending.

## 4. Experimental units and grouping

The experimental unit must represent the independent biological or observational unit supported by the dataset protocol.

| Dataset | Provisional grouping unit | Required clarification |
|---|---|---|
| VNIR Wheat | Pot or biological plant | Confirm plant structure and leaf tracking |
| SWIR Wheat | Pot or biological plant | Confirm leaf-to-pot and scan relationships |
| Rice Sheath Blight | Original plant/specimen, if identifiable | Confirm image-to-specimen relationships |
| NWRD Wheat Rust | Original field image or plant group | Confirm image grouping and mask correspondence |
| CCMT Tomato | Undetermined | Establish original-image and augmented-image relationships |

A leaf, pixel, image patch or augmented copy must not automatically be treated as an independent biological replicate.

If multiple observations originate from the same biological unit, they must remain in the same data partition.

## 5. Data splitting and leakage prevention

The following principles apply to every experimental track:

1. Identify the grouping unit before splitting.
2. Keep observations from the same biological sample in one partition.
3. Keep an original image and its augmented derivatives in the same partition.
4. Keep image patches and their source image in the same partition.
5. Fit data-dependent transformations using training data only.
6. Apply the fitted transformations to validation and test data without refitting.
7. Do not use the test set for model selection or hyperparameter tuning.
8. Preserve a final independent test set where the available sample structure permits it.

**Preferred validation approach:** Group-aware splitting, using the verified biological or original-image grouping unit.

If reliable biological grouping cannot be established, the limitation must be documented. An image-level split must not be presented as evidence of biological generalisation.

## 6. Evaluation metrics

Metrics must match the experimental objective.

| Objective | Primary metrics | Additional reporting |
|---|---|---|
| Multiclass classification | Macro F1-score, balanced accuracy | Per-class precision, recall, confusion matrix |
| Binary classification | Precision, recall, F1-score | ROC-AUC and PR-AUC where appropriate |
| Binary segmentation | Dice coefficient, IoU | Pixel precision, recall and visual mask inspection |
| Ordered severity estimation | Macro F1-score and balanced accuracy | Confusion matrix and ordinal error analysis |
| Exploratory spectral analysis | Data-quality and distribution summaries | Spectral variability and uncertainty |

Accuracy alone is insufficient when class distributions are imbalanced.

Results must include the test-set definition, sample counts, grouping strategy and relevant limitations.

## 7. Preprocessing and model-development sequence

Preprocessing must begin only after the relevant dataset passes its readiness checks.

The proposed sequence is:

1. Confirm source, licence and data access.
2. Verify archive structure and file integrity.
3. Verify labels, annotations and metadata.
4. Establish experimental units and sample relationships.
5. Define leakage-resistant data partitions.
6. Approve a modality-specific preprocessing workflow.
7. Conduct exploratory data analysis.
8. Establish a simple baseline.
9. Evaluate using the predefined validation strategy.
10. Perform error analysis and document limitations.

Raw files must remain unchanged. Processed outputs must be stored separately with reproducible scripts and documented parameters.

VNIR and SWIR calibration and preprocessing must be based on verified instrument metadata. RGB preprocessing must preserve the original image and annotation relationships.

## 8. Forecasting feasibility

The project title includes disease forecasting, but forecasting is not currently established by the available evidence.

Repeated DPI values alone do not demonstrate longitudinal tracking of the same biological samples.

A forecasting experiment would require:

- Identifiable repeated observations of the same biological units.
- Reliable observation timestamps.
- Verified disease progression labels.
- A clearly defined prediction target and future prediction horizon.
- A temporal validation strategy that prevents future observations from leaking into training.

Until these conditions are met, the project must describe its work as exploratory spectral analysis, detection, classification, segmentation or severity estimation, as appropriate to each dataset.

## 9. Multimodal integration

VNIR, SWIR and RGB fusion is not part of the initial experimental scope.

Before fusion can be considered, the team must establish:

- A shared biological sample or plant identity.
- Corresponding observations across modalities.
- Compatible disease labels.
- Relevant acquisition-time relationships.
- A scientifically justified fusion strategy.

The current datasets cover different crops and diseases, and direct sample correspondence has not been established.

Therefore, modality-specific experiments must be completed and evaluated independently before any fusion proposal.

## 10. Approval gates

| Gate | Requirement | Current status |
|---|---|---|
| Gate 1 – Source and access | Source, licence and archive access verified | Partially complete |
| Gate 2 – Technical readiness | File structure, metadata and calibration verified | Pending for VNIR/SWIR and some RGB datasets |
| Gate 3 – Label readiness | Labels and annotations verified | Pending for Rice and NWRD; CCMT follow-up ongoing |
| Gate 4 – Experimental design | Experimental units and leakage-safe splits established | Provisional |
| Gate 5 – Preprocessing | Modality-specific workflow reviewed and approved | Not approved |
| Gate 6 – Modelling | Baseline and evaluation protocol approved | Not approved |
| Gate 7 – Forecasting/fusion | Required temporal or cross-modal evidence established | Not established |

A dataset must not proceed to a later gate merely because its documentation has been completed.

## 11. Immediate team actions

**Hiba – Coordination and VNIR**

- Maintain this consolidated experimental-design framework.
- Review the updated SWIR and RGB evidence.
- Resolve any changes required in the dataset suitability decisions.
- Coordinate the final team review and approval gates.

**Member 2 – SWIR**

- Continue the original archive and technical-file access investigation.
- Provide independently verified technical evidence or document the access blocker.

**Member 3 – RGB**

- Continue CCMT archive relationship and leakage investigation.
- Verify Rice severity definitions and image-to-label mapping.
- Investigate NWRD reuse permission and archive verification.

## 12. Current conclusion

TerraSpectra should proceed with separate, evidence-driven experimental tracks rather than attempting immediate multimodal disease forecasting.

The most important next milestone is to establish technical readiness, reliable labels and defensible sample-level validation for each selected dataset.

**No preprocessing, feature engineering, model training, multimodal fusion or forecasting claim is approved by this framework.**

Final experimental scope requires team review and explicit approval after the remaining investigations are completed.