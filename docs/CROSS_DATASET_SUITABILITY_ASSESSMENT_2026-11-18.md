# TerraSpectra — Cross-Dataset Suitability Assessment

**Date:** 18 November 2026
**Prepared by:** Hiba
**Status:** Draft — pending team investigation updates and review

## 1. Purpose

This document evaluates the available datasets for TerraSpectra: Hyperspectral Crop Disease Forecasting.

The assessment compares five candidate datasets across:

- Disease detection
- Disease classification
- Disease severity assessment
- Disease forecasting

It also provides preliminary dataset-selection recommendations, experimental design requirements, and conditions for future multimodal integration.

**Important:** These are evidence-based suitability recommendations, not results from trained models. No dataset is considered fully approved for modelling until its outstanding source, licence, label and sample-structure checks are completed.

## 2. Cross-dataset comparison

| Dataset | Modality | Crop and disease | Reported data | Main limitations |
|---|---|---|---|---|
| VNIR Wheat Septoria | VNIR hyperspectral | Wheat — Septoria | 48 metadata pots; 216 bands in inspected subset | Small inspected subset, calibration uncertainty, scan-treatment confounding and biological tracking uncertainty |
| SWIR Wheat Septoria | SWIR hyperspectral | Wheat — Septoria | 48 pot records, 279 leaf-level records, 256 channels; 96 scans historically reported | Local calibration and scan-label evidence require further verification; biological tracking uncertainty |
| Rice Sheath Blight | RGB | Rice — sheath blight | 1,609 original images and six severity levels reported | Exact severity class definitions, annotation mapping and licence require verification |
| NWRD Wheat Rust | RGB | Wheat — rust | 100 field images and binary masks reported | Dataset reuse licence, archive contents, image-mask matching and split discrepancy unresolved |
| CCMT Tomato | RGB | Tomato — disease details pending | Insufficient verified information | Official source, licence, image count, labels and annotation structure not yet established |

### 2.1 VNIR Wheat Septoria

The available metadata describes 48 pots, comprising 24 infected and 24 non-infected pots across two wheat genotypes. Eighteen DPI dates are represented in the metadata.

The inspected processed subset contains four scans from four pots, ten leaves and 272,912 pixel records across 216 bands. The inspected subset has one pot per genotype-treatment combination, and treatment is confounded with scan identity.

The local calibration status and preprocessing-script provenance remain unresolved. Pixels and leaves are nested within scans and pots and must not be treated as independent biological samples.

**Preliminary conclusion:** Suitable for exploratory spectral investigation. Disease detection and classification remain conditional. Severity assessment and forecasting are not established.

### 2.2 SWIR Wheat Septoria

The dataset is described in the Recherche Data Gouv repository under DOI `10.57745/WVP0FJ`.

The metadata contains 48 pot records and 279 leaf-level records. The instrument is described in the associated 2025 paper as a HySpex SWIR-384 system covering approximately 964–2494 nm with 256 channels.

A previous investigation reported 96 expected and 96 actual scans. This is historical team-reported verification; the original filename-to-pot-side matching evidence is not independently preserved in the current report.

The paper describes dark-current correction and reflectance calculation, but the application of calibration to the local data files remains unverified. Repeated DPI dates do not establish that the same biological samples were tracked over time.

**Preliminary conclusion:** Promising for exploratory spectral analysis. Detection and classification remain conditional. Severity assessment and forecasting are not established.

### 2.3 RGB Rice Sheath Blight

The dataset is described as the Colour-Mix Augmentation Dataset for Rice Sheath Blight Severity Estimation.

- Mendeley Data DOI: `10.17632/489spnkhp5.1`
- Reported original image count: 1,609 JPG images.
- Reported severity categories: six progressive levels.

The dataset is potentially useful for severity estimation. However, the exact six class names, severity boundaries, scoring definitions and annotation mapping have not yet been verified. The dataset licence and archive contents also require confirmation.

**Preliminary conclusion:** Promising candidate for severity estimation, conditional on label, annotation and licence verification.

### 2.4 NWRD Wheat Rust

The NUST Wheat Rust Disease Dataset is described in Zenodo under DOI `10.5281/zenodo.21672928`.

The reported dataset contains 100 field images and binary Rust/Non-rust segmentation masks. The associated paper describes manual pixel-level annotations.

Important unresolved issues:

- The dataset reuse licence is not explicitly established by the available Zenodo rights statement.
- The archive has not been independently inspected.
- Image-mask pairing and exact mask pixel values remain unverified.
- Zenodo and the GitHub README describe different training/validation split arrangements.

**Preliminary conclusion:** Conditional candidate for binary rust segmentation. Do not approve use until licence and archive verification are completed.

### 2.5 CCMT Tomato

The available evidence is insufficient to establish the official dataset source, licence, image count, disease labels, annotation format or sample structure.

**Preliminary conclusion:** Not approved for selection until the assigned source investigation is completed.

## 3. Dataset suitability by research objective

The following categories describe the strength of current evidence:

- **Potentially suitable:** Available evidence supports investigating the objective, subject to normal validation.
- **Conditional:** The objective may be feasible, but important verification or validation remains.
- **Not established:** Current evidence does not support the objective.
- **Not assessed:** Available information is insufficient for a meaningful assessment.

| Dataset | Disease detection | Disease classification | Severity assessment | Forecasting |
|---|---|---|---|---|
| VNIR Wheat Septoria | Conditional | Conditional | Not established | Not established |
| SWIR Wheat Septoria | Conditional | Conditional | Not established | Not established |
| Rice Sheath Blight | Conditional | Conditional | Conditional | Not established |
| NWRD Wheat Rust | Potentially suitable for segmentation | Conditional | Not established | Not established |
| CCMT Tomato | Not assessed | Not assessed | Not assessed | Not assessed |

### Interpretation

- VNIR and SWIR provide spectral information for investigating wheat Septoria, but neither currently supports a claim of validated disease prediction.
- Rice Sheath Blight is the clearest candidate for investigating severity estimation, provided its severity labels are verified.
- NWRD is potentially useful for pixel-level rust segmentation. Segmentation should not automatically be described as image-level disease classification.
- CCMT cannot yet be evaluated.
- None of the current datasets provides sufficient verified evidence for a forecasting claim.

## 4. Preliminary dataset-selection recommendations

### 4.1 Promising candidates

**Rice Sheath Blight — RGB**

Proposed use: Severity estimation.

Reason: The dataset reports six progressive severity levels and is specifically intended for severity estimation.

Conditions before approval:
- Verify all six class names and definitions.
- Verify the scoring scale and class boundaries.
- Verify image-to-label mapping.
- Confirm the dataset licence and access conditions.

**SWIR Wheat Septoria**

Proposed use: Exploratory spectral analysis and conditional disease detection/classification.

Reason: The dataset has 256 spectral channels and detailed pot-level and leaf-level metadata.

Conditions before approval:
- Verify calibration provenance.
- Establish reliable scan-to-sample linkage.
- Clarify biological experimental units.
- Document acquisition settings where available.

### 4.2 Conditional candidates

**NWRD Wheat Rust — RGB**

Proposed use: Binary rust segmentation.

Conditions:
- Confirm the dataset reuse licence.
- Inspect archive contents.
- Verify image-mask pairing and mask values.
- Resolve the train/validation split discrepancy.

**VNIR Wheat Septoria**

Proposed use: Exploratory spectral analysis and comparison with SWIR.

Conditions:
- Establish calibration provenance.
- Investigate usable scan coverage.
- Address treatment confounding with scan identity.
- Clarify biological sample tracking.

### 4.3 Not approved yet

**CCMT Tomato**

The dataset should remain outside the selected modelling scope until its official source, licence, labels and data structure are verified.

### 4.4 Recommended project direction

1. Prioritise Rice Sheath Blight for severity-estimation investigation, subject to label verification.
2. Investigate NWRD for binary rust segmentation, subject to licence and archive verification.
3. Retain VNIR and SWIR as separate exploratory spectral research pipelines.
4. Consider CCMT only after the pending source investigation.
5. Treat multimodal fusion and forecasting as future research directions, not confirmed deliverables.

These are provisional recommendations. Final selection must incorporate the outstanding Member 2 and Member 3 investigation results.

## 5. Experimental design recommendations

### 5.1 Experimental units

| Dataset | Proposed grouping unit | Required caution |
|---|---|---|
| VNIR Wheat | Pot or biological plant, after verification | Leaves and pixels from one biological unit must remain together |
| SWIR Wheat | Pot or biological plant, after verification | Multiple leaves and scans may belong to the same pot |
| Rice Sheath Blight | Original plant/specimen if identifiable; otherwise original image | Augmented copies must remain with their original image |
| NWRD Wheat Rust | Original field image or plant grouping, if identifiable | Image patches and masks from one image must remain together |
| CCMT Tomato | Undetermined | Establish sample structure first |

The true biological experimental unit must be confirmed from the dataset protocol. A pot or image is only a provisional grouping unit and must not automatically be treated as an independent biological replicate.

### 5.2 Data splitting

A possible starting arrangement is 70% training, 15% validation and 15% testing. These percentages are illustrative, not fixed requirements.

The split must be group-aware:

- Keep all related scans from one biological unit in the same partition.
- Keep leaves and pixels from the same biological unit together.
- Keep original and augmented images in the same partition.
- Use group-aware cross-validation when the number of independent groups is limited.
- Do not use the test set for model tuning.

If there are too few independent biological groups, report the limitation rather than forcing an arbitrary split.

### 5.3 Data leakage prevention

The following safeguards are required:

1. Split data before fitting preprocessing transformations.
2. Fit normalization and feature-selection parameters using training data only.
3. Keep related samples and augmented copies together.
4. Avoid random pixel-level splitting when pixels originate from the same scan or biological unit.
5. Keep the final test set independent from model selection and hyperparameter tuning.
6. Record sample IDs and group IDs throughout the workflow.

### 5.4 Preprocessing recommendations

| Modality | Proposed checks |
|---|---|
| VNIR | Ignore values, missing bands, calibration, spectral quality and normalization |
| SWIR | Wavelength metadata, invalid values, calibration, scan quality and normalization |
| RGB | Image quality, resizing, consistent colour handling and verified mask/label mapping |

These are proposed investigations only. No preprocessing should be executed until dataset selection and experimental design are approved.

### 5.5 Evaluation metrics

| Research task | Recommended metrics |
|---|---|
| Disease classification | Accuracy, precision, recall, F1-score, ROC-AUC where appropriate |
| Disease detection | Precision, recall, F1-score, sensitivity and specificity |
| Segmentation | Dice score, IoU, precision and recall |
| Severity estimation | Macro-F1, confusion matrix, weighted kappa; MAE if verified numeric severity scores are available |
| Forecasting | MAE, RMSE and future-time holdout evaluation, only when longitudinal tracking is established |

Accuracy alone is insufficient, especially when class distributions are imbalanced. Metrics must match the actual prediction task and label structure.

## 6. Multimodal integration requirements

TerraSpectra investigates three imaging modalities:

- **VNIR:** Visible and near-infrared spectral information.
- **SWIR:** Short-wave infrared spectral information.
- **RGB:** Visible colour, texture and lesion patterns.

Before combining modalities, the following conditions must be satisfied:

| Requirement | Why it matters |
|---|---|
| Same biological samples | Modalities must represent corresponding biological units |
| Compatible disease labels | Target definitions must be consistent |
| Acquisition correspondence | Measurements should represent comparable conditions and time points |
| Spatial alignment | Needed for pixel-level fusion or corresponding image regions |
| Spectral calibration | Measurements must be sufficiently comparable |
| Metadata consistency | Crop, disease, treatment and sample identifiers must be reliable |
| Independent evaluation | Fusion must be tested without data leakage |

**Current decision:** Keep VNIR, SWIR and RGB pipelines separate.

The current investigation has not established that these datasets share corresponding biological samples. The RGB datasets also cover different crops and diseases. They must not simply be merged with wheat hyperspectral data as if they formed one homogeneous classification dataset.

Multimodal fusion may be investigated later if sample correspondence, label compatibility, acquisition information and evaluation design support it.

## 7. Forecasting requirements

Disease detection, classification, severity estimation and forecasting are different research objectives.

- **Detection:** Is disease present or visible now?
- **Classification:** Which disease category is present?
- **Severity estimation:** How severe is the disease now?
- **Forecasting:** What will the disease state or severity be at a future time?

A valid forecasting experiment requires:

1. Reliable plant or biological sample identifiers.
2. Repeated observations of the same biological units.
3. Correct chronological timestamps or DPI mapping.
4. Verified disease progression or severity labels at each observation.
5. Enough independent samples and time points.
6. A future-time holdout evaluation.
7. No use of future information during training.

### 7.1 Current forecasting readiness

| Dataset | Available temporal evidence | Decision |
|---|---|---|
| VNIR Wheat | 18 DPI dates; individual sample tracking uncertain | Not established |
| SWIR Wheat | 18 DPI dates; biological linkage uncertain | Not established |
| Rice Sheath Blight | No verified repeated observations | Not established |
| NWRD Wheat Rust | No verified longitudinal tracking | Not established |
| CCMT Tomato | Insufficient information | Not assessed |

Repeated DPI metadata alone does not establish longitudinal tracking. Forecasting should remain a future research direction unless the required biological tracking and temporal labels can be verified.

## 8. Recommended development sequence

1. **Independent dataset investigation:** Complete source, licence, label and sample verification.
2. **Separate modality experiments:** Develop and evaluate RGB, VNIR and SWIR independently.
3. **Model comparison:** Compare results only where tasks, labels and evaluation conditions are meaningfully comparable.
4. **Multimodal investigation:** Consider fusion only if matching biological samples and compatible measurements become available.
5. **Forecasting investigation:** Consider forecasting only if longitudinal tracking and future-time evaluation are supported.

## 9. Recommended project description

> TerraSpectra is a multi-dataset crop disease analysis research project investigating RGB and hyperspectral imaging for disease detection, classification and severity assessment, with multimodal integration and disease forecasting considered as future research directions subject to data suitability.

This description reflects the current evidence without promising an unverified forecasting or fusion capability.

## 10. Outstanding questions and dependencies

### VNIR
- Can local NPZ calibration be established?
- Can the original correction and preprocessing scripts be located?
- What is the true biological experimental unit?
- Can repeated observations be linked to the same plants or leaves?
- Which metadata pots have usable spectral files?

### SWIR
- Can original scan-to-pot-side matching evidence be recovered?
- What were the exact integration time, frame period and scan speed?
- Can local calibration be independently verified?
- What is the biological experimental unit?
- What is the protocol behind the leaf confidence scores?

### Rice Sheath Blight
- What are the exact six severity class names and definitions?
- What are the severity scoring boundaries?
- How are labels mapped to original images?
- What licence governs dataset reuse?

### NWRD
- What licence permits dataset reuse?
- Do the archive contents match the reported image and mask counts?
- Are all image-mask pairs valid?
- What are the exact mask pixel values?
- Which train/validation/test split is authoritative?

### CCMT Tomato
- What is the official dataset source?
- What licence and access conditions apply?
- What are the image count, disease labels and annotation format?
- What sample grouping and collection information are available?

### Overall project
- Which datasets will be approved after the member investigations?
- Which task will become the primary modelling objective?
- Is there enough evidence for any multimodal or forecasting experiment?

## 11. References and source records

1. VNIR Wheat Septoria: Existing project records — `docs/VNIR_FINAL_SUITABILITY_ASSESSMENT_2026-11-17.md` and related VNIR progress reports.
2. SWIR Wheat Septoria: Recherche Data Gouv, DOI `10.57745/WVP0FJ` — https://entrepot.recherche.data.gouv.fr/dataset.xhtml?persistentId=doi:10.57745/WVP0FJ
3. SWIR associated paper: Latchoumane et al. (2025), *Data in Brief*, 59, 111404 — https://pmc.ncbi.nlm.nih.gov/articles/PMC11919375/
4. Rice Sheath Blight: Mendeley Data, DOI `10.17632/489spnkhp5.1` — https://data.mendeley.com/datasets/489spnkhp5/1
5. NWRD Wheat Rust: Zenodo, DOI `10.5281/zenodo.21672928` — https://zenodo.org/records/21672928
6. NWRD associated paper — https://pmc.ncbi.nlm.nih.gov/articles/PMC10422341/
7. NWRD GitHub repository — https://github.com/dll-ncai/NUST-Wheat-Rust-Disease-NWRD

The source references above identify the reported dataset and publication records. They do not imply that every archive, licence, label or acquisition detail has been independently verified.

## 12. Assessment status

**Completed in this draft:**
- Existing VNIR, SWIR, Rice and NWRD evidence review.
- Cross-dataset comparison.
- Objective suitability evaluation.
- Preliminary dataset-selection recommendations.
- Experimental design recommendations.
- Multimodal integration requirements.
- Forecasting requirements and limitations.

**Still pending:**
- CCMT source verification.
- Today's SWIR and RGB member investigation updates.
- Final dataset selection and approval.
- Team review of this assessment.
- Documentation and reference verification.
- Git diff review and approval before commit/push.

**Current conclusion:** TerraSpectra has a defensible research direction, but dataset approvals and modelling scope must remain conditional until the outstanding evidence is resolved.
