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

**Additional header verification — 25 November 2026:**

- All four available VNIR ENVI headers (01_D, 04_D, 07_D and 10_D) specify an ignore value of 4095.
- All four report dimensions of 1370 lines, 1024 samples and 216 spectral bands, with wavelength units in nanometres.
- The value 16383 was observed in an inspected SWIR header; it is not a contradiction in the inspected VNIR headers.
- This confirms header metadata only. It does not establish reflectance calibration or processing provenance.

**VNIR data provenance and preservation:**

- Keep the original raw ENVI measurements, the original combined CSV and the corrected NPZ identified as separate data artifacts. The corrected NPZ is a derived dataset and must not be treated as the original raw measurement data.
- The original combined CSV and baseline dataset each contain 7,559 missing values.
- The corrected NPZ retains 723 values corresponding to the VNIR ignore value of 4095 as missing. Interpolation was limited to internal gaps of one or two spectral bands; larger gaps and edge gaps remain missing.
- Validation compared 10 VNIR files against three CSV reference datasets (30 comparisons). Pixel counts and coordinate ordering passed the reported checks, while the corrected NPZ remained distinct from the original combined CSV.
- The original NPZ generation and correction scripts have not been located in the repository search. The complete processing implementation and execution environment therefore remain unverified.
- The publication describes reflectance calculation using a Spectralon reference and dark-current measurements, but the local NPZ processing has not been shown to apply that calculation. The processed VNIR spectra must therefore continue to be described as processed spectral-intensity data; calibrated reflectance is unverified.
- Preserve the original raw measurements unchanged and maintain separate, traceable records for derived datasets and any future processing steps. This documentation does not approve preprocessing, calibration transformations or model development.

**Proposed experimental direction:**

- Preserve the original spectral measurements.
- Verify data format and calibration provenance before processing.
- Conduct exploratory spectral-quality and distribution analysis only after data-readiness approval.
- Investigate whether disease-related spectral differences can be distinguished from acquisition and experimental confounding.

**Current decision:** Exploratory analysis only. Validated classification, severity estimation and forecasting are not approved.

### 3.2 SWIR – Wheat Septoria

**Proposed initial objective:** Exploratory spectral analysis, conditional on resolving calibration, annotation and biological-sample provenance.

**Published study context:**

The dataset publication describes a wheat Septoria experiment involving 48 pots, two wheat genotypes and infected and non-infected treatments. It reports 279 leaf-level records collected across multiple days post-inoculation. These are publication-level descriptions and should not be treated as proof that every biological sample and acquisition relationship has been mapped within the downloaded archive.

The 25 November 2026 archive investigation by Member 2 verified:

- The official SWIR archive was downloaded outside the repository.
- The local MD5 checksum matches the published checksum.
- The archive contains 96 `.hyspex` files, 96 matching `.hdr` files, 96 JPG files and 259 CSV files.
- All 96 raw/header pairs were checked, with no missing matching headers or binary-size mismatches reported.
- All inspected headers report 256 bands and a wavelength range of 964.181280–2494.388419 nm.
- Common configuration: 420 lines × 320 samples × 256 bands, ENVI data type 12 (unsigned 16-bit integer), little-endian byte order and BIL interleave.
- Headers specify wavelength units in nanometres and an ignore value of 16383.
- All 259 CSV files were structurally checked: 922,064 rows, with two numeric values per row.

**Outstanding limitations:**

- Dark-current and white-reference correspondence has not been established.
- CSV annotation meaning and coordinate convention remain unconfirmed.
- Biological sample, leaf, pot and side relationships require verification.
- `18_D.hdr` and `18_D.hyspex` are located inside the `18_G` folder; this irregularity requires clarification.
- `CalibAvailable = 1` does not independently establish calibrated reflectance or a reproducible calibration procedure.
- The archive was inspected read-only without extraction.

**Proposed experimental direction:**

- Preserve the downloaded original archive unchanged and outside the repository.
- Resolve calibration-reference availability and acquisition metadata.
- Clarify CSV annotation semantics and sample-to-scan correspondence.
- Investigate the folder-placement irregularity.
- Establish biological experimental units and group-aware validation before predictive experiments.
- Consider exploratory spectral analysis only after technical and scientific readiness review.

**Current decision:** Archive integrity and raw/header inventory have been verified. SWIR is suitable for continued technical investigation, but calibration, annotation semantics and biological mapping remain unresolved. Preprocessing, calibration transformations, feature extraction and supervised modelling are not approved.

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

**Proposed objective:** Five-class image-level classification, conditional on resolving data lineage and establishing a defensible evaluation split.

The 25 November 2026 verification by Member 3 reports the following archive inventory:

- Raw Tomato images: 5,805.
- Augmented Train images: 21,723.
- Augmented Test images: 5,445.
- Total augmented images: 27,168.
- The publication reports 27,178 augmented images, leaving a 10-image discrepancy that remains unresolved.

**Exact-content Train-Test overlap verification:**

A reproducible script compared image contents directly from ZIP entry streams using SHA-256 and CRC32. Both methods returned identical counts:

- 4,084 unique shared image contents.
- 4,084 Test entries with at least one Train match.
- 4,085 matching Train-Test file pairs.
- 1,361 Test entries without an exact Train content match.
- Approximately 75.0% of Test entries have an exact-content match in Train.

The difference between 4,084 unique shared contents and 4,085 file pairs occurs because one shared content appears in two Train entries and one Test entry. Those two Train entries have different class labels, indicating a label-consistency issue requiring investigation.

**Outstanding limitations:**

- Exact binary matching does not identify near-duplicates.
- Original-to-augmented image lineage remains unresolved.
- Biological plant, leaf or specimen identity cannot be inferred from these hash results.
- Biological independence between Train and Test has not been established.
- The publication-versus-archive count discrepancy remains unresolved.

**Proposed experimental direction:**

- Investigate the repeated-content group and its conflicting Train labels.
- Establish original-image and augmented-image relationships.
- Investigate near-duplicates and biological sample grouping.
- Determine whether a defensible group-aware split can be constructed.
- Reconcile the archive and publication counts.
- Do not use the supplied Test partition as an independent evaluation set until the overlap and grouping issues are resolved.

**Current decision:** Exact-content overlap is reproducibly verified. The supplied Train-Test partition is not currently suitable as an independent test set. Classification modelling and performance evaluation remain on hold pending lineage, label and split review.

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
| Gate 3 – Label readiness | Labels and annotations verified | Pending for Rice and NWRD; CCMT lineage and label consistency unresolved |
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

- Resolve CCMT original-to-augmented lineage, repeated-content label inconsistency and leakage-safe split feasibility.
- Verify Rice severity definitions and image-to-label mapping.
- Investigate NWRD reuse permission and archive verification.

## 12. Current conclusion

TerraSpectra should proceed with separate, evidence-driven experimental tracks rather than attempting immediate multimodal disease forecasting.

The most important next milestone is to establish technical readiness, reliable labels and defensible sample-level validation for each selected dataset.

**No preprocessing, feature engineering, model training, multimodal fusion or forecasting claim is approved by this framework.**

Final experimental scope requires team review and explicit approval after the remaining investigations are completed.
