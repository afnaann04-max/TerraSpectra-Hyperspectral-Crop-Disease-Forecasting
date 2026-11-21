# TerraSpectra — Cross-Dataset Suitability Assessment

**Assessment date:** 18 November 2026
**Updated:** 21 November 2026
**Prepared by:** Hiba
**Status:** Updated draft — pending final team investigation updates and review

## 1. Purpose

This document evaluates five candidate datasets for TerraSpectra: Hyperspectral Crop Disease Forecasting.

The assessment compares the available datasets across:

- Disease detection
- Disease classification
- Disease severity assessment
- Disease forecasting

It also provides preliminary dataset-selection recommendations, experimental design requirements, and conditions for future multimodal integration.

**Important:** These are evidence-based suitability recommendations, not results from trained models. No dataset is fully approved for modelling until the outstanding source, licence, label, archive and sample-structure checks have been completed.

## 2. Cross-dataset comparison

| Dataset | Modality | Crop and disease | Reported or verified data | Main limitations |
|---|---|---|---|---|
| VNIR Wheat Septoria | VNIR hyperspectral | Wheat — Septoria | 48 metadata pots; 216 bands in inspected subset | Small inspected subset, calibration uncertainty, scan-treatment confounding and biological tracking uncertainty |
| SWIR Wheat Septoria | SWIR hyperspectral | Wheat — Septoria | 48 pot records, 279 leaf-level records, 256 channels; 96 scans historically reported | Original raw headers and calibration references unavailable for verification; acquisition settings and biological tracking require clarification |
| Rice Sheath Blight | RGB | Rice — sheath blight | 1,609 original field images and six progressive severity levels reported | Exact severity class names, boundaries and image-to-label mapping unresolved; archive not inspected |
| NWRD Wheat Rust | RGB | Wheat — rust | 100 images and binary segmentation masks reported | Dataset reuse licence unresolved; archive and image-mask pairing unverified; paper and README split discrepancy |
| CCMT Tomato | RGB | Tomato — five reported disease/health classes | 27,158 images inspected: 21,723 train and 5,435 test; publication reports 27,178 augmented images | 20-image discrepancy, original-to-augmented mapping, comprehensive leakage checks, near-duplicates and biological sample grouping unresolved |

The values above distinguish published descriptions, historical team-reported checks and archive-level inspections. Archive inspection has been completed for CCMT, but not for every dataset. The reported figures should not be interpreted as proof that all datasets have been independently verified.

### 2.1 VNIR Wheat Septoria

The available metadata describes 48 pots, comprising 24 infected and 24 non-infected pots across two wheat genotypes. Eighteen DPI dates are represented in the metadata.

The inspected processed subset contains four scans from four pots, ten leaves and 272,912 pixel records across 216 bands. The inspected subset has one pot per genotype-treatment combination, and treatment is confounded with scan identity.

The local calibration status and preprocessing-script provenance remain unresolved. Pixels and leaves are nested within scans and pots and must not be treated as independent biological samples.

**Preliminary conclusion:** Suitable for exploratory spectral investigation. Disease detection and classification remain conditional. Severity assessment and forecasting are not established.

### 2.2 SWIR Wheat Septoria

The dataset is described in the Recherche Data Gouv repository under DOI `10.57745/WVP0FJ`.

The metadata contains 48 pot records and 279 leaf-level records. The instrument is described in the associated 2025 paper as a HySpex SWIR-384 system covering approximately 964–2494 nm with 256 channels.

A previous investigation reported 96 expected and 96 actual scans. This is historical team-reported verification; the original filename-to-pot-side matching evidence is not independently preserved in the current report.

The paper describes dark-current correction and reflectance calculation, but the application of calibration to the local data files remains unverified. Original raw headers and calibration references have not been obtained for technical verification. Important acquisition properties, including exact integration time, frame period and scan speed, remain unresolved.

Repeated DPI dates do not establish that the same biological samples were tracked over time.

**Preliminary conclusion:** Promising for exploratory spectral analysis. Detection and classification remain conditional. Severity assessment and forecasting are not established. Raw-data preprocessing should not begin until the necessary file-format and calibration information is available.

### 2.3 RGB Rice Sheath Blight

The dataset is titled *Colour-Mix Augmentation Dataset for Rice Sheath Blight Severity Estimation*.

- Mendeley Data DOI: `10.17632/489spnkhp5.1`
- Reported image count: 1,609 original JPG field images.
- Reported severity categories: six progressive levels.
- Crop and disease: rice sheath blight.
- Collection context: Jyotsna rice variety, Puncha season, January–March, in fields at Kottekkad and Kuttur, Thrissur, Kerala.
- Image acquisition: iPhone 6s, 12 MP camera, according to the dataset description.
- Expert review: the description reports review by an expert from the Department of Plant Pathology, College of Agriculture, Padannakkad, Kasaragod.

The dataset description reports that blurred and duplicate images were removed and that the supplied 1,609 images are original field images rather than synthetic augmented derivatives. The dataset title refers to Colour-Mix Augmentation, but this does not establish that augmented images are included in the supplied archive.

The public Mendeley record displays a CC BY 4.0 licence. This is a public-record licence finding; the archive itself has not been downloaded or inspected.

The six progressive severity levels are reported, and the description identifies severity-related characteristics such as lesion extent, lesion height progression along the sheath, symptom colour intensity and lesion density or spatial spread. However, the exact six class names, numerical boundaries, specific scoring-scale reference and image-to-label mapping remain unresolved.

No evidence currently establishes that the dataset provides segmentation masks or bounding-box annotations. Repeated observation periods mentioned in the description also do not establish that the same plants or leaves were tracked longitudinally.

**Preliminary conclusion:** Promising candidate for severity-estimation investigation, conditional on verification of the six class definitions, scoring boundaries and image-to-label mapping. The archive and sample structure must be inspected before supervised modelling is approved.

### 2.4 NWRD Wheat Rust

The NUST Wheat Rust Disease Dataset is described in Zenodo under DOI `10.5281/zenodo.21672928`. Its associated publication is available under DOI `10.3390/s23156942`.

The public-source investigation reports:

- 100 field images.
- JPG images and PNG binary segmentation masks.
- Manual pixel-level annotations described in the associated paper.
- A GitHub repository containing dataset documentation and split information.

The dataset is a potential candidate for binary wheat-rust segmentation. However, several issues remain unresolved:

- The Zenodo rights information displays `Copyright (C) 2023 The Authors`; an explicit dataset reuse licence has not been established.
- The GitHub repository displays an MIT licence, but this does not automatically establish that the dataset images and masks are covered by the same licence.
- The archive has not been downloaded and independently inspected.
- Actual image and mask counts, valid image-mask pairing, missing files and mask pixel values remain unverified.
- The paper reports an 80/10/10 train/validation/test split, whereas the GitHub README describes 90% training and validation data combined and 10% testing. The configuration also refers to a validation split of 0.1. These descriptions may reflect a two-stage split, but the exact implementation, sample counts and split assignment have not been confirmed.

**Preliminary conclusion:** Conditional candidate for binary rust segmentation. Dataset reuse permission, archive integrity, image-mask pairing and the split discrepancy must be resolved before modelling approval. Segmentation results should not automatically be presented as image-level disease classification results.

### 2.5 CCMT Tomato

The dataset is titled *Dataset for Crop Pest and Disease Detection (CCMT)*.

- Mendeley Data DOI: `10.17632/bwh3zbpkpv.1`
- Associated publication DOI: `10.1016/j.dib.2023.109306`
- Crops covered: cashew, cassava, maize and tomato.
- Five reported tomato classes: Healthy, Leaf blight, Leaf curl, Septoria leaf spot and Verticillium wilt.
- Public dataset record lists a CC BY 4.0 licence. The dataset licence should be distinguished from the licence governing the associated publication.

#### Published dataset information

The publication reports 5,435 raw tomato images and 27,178 augmented tomato images.

The reported raw tomato class counts are:

| Tomato class | Published raw image count |
|---|---:|
| Healthy | 500 |
| Leaf blight | 1,301 |
| Leaf curl | 518 |
| Septoria leaf spot | 2,343 |
| Verticillium wilt | 773 |
| **Total** | **5,435** |

The source description reports JPEG images captured using a Canon EOS Rebel T7 DSLR with an EF-S 18–55 mm lens on farms in Ghana between October and December 2022. Annotation reportedly took place between December 2022 and January 2023, involving plant virologists or pathologists and expert review.

#### Archive-level verification — 20 November 2026

Member 3 (Afnan) completed an inspection of the available CCMT tomato archive and documented the following counts:

| Archive partition | Image count |
|---|---:|
| Train | 21,723 |
| Test | 5,435 |
| **Total inspected** | **27,158** |

The inspected archive contains 20 fewer images than the 27,178 augmented tomato images reported in the publication. The reason for this difference remains unresolved.

The verified archive class distribution is:

| Tomato class | Train | Test | Total |
|---|---:|---:|---:|
| Healthy | 2,000 | 500 | 2,500 |
| Leaf blight | 5,200 | 1,309 | 6,509 |
| Leaf curl | 2,050 | 532 | 2,582 |
| Septoria leaf spot | 9,373 | 2,330 | 11,703 |
| Verticillium wilt | 3,100 | 764 | 3,864 |
| **Total** | **21,723** | **5,435** | **27,158** |

The archive class totals are internally consistent. However, the published raw class counts and the inspected test-partition class counts are not identical. Their relationship requires further clarification.

#### Filename matching and duplicate investigation

Filename-based matching between the train and test partitions identified the following class-pair groupings:

| Train class | Test class | Filename matches |
|---|---|---:|
| Septoria leaf spot | Septoria leaf spot | 1,755 |
| Leaf blight | Leaf blight | 982 |
| Verticillium wilt | Verticillium wilt | 573 |
| Leaf curl | Leaf curl | 397 |
| Healthy | Healthy | 377 |
| Septoria leaf spot | Leaf blight | 1 |

One cross-class filename pairing was identified between a Septoria leaf spot training image and a Leaf blight test image. The SHA-256 hashes of the inspected pair were different. Therefore, this pair is not confirmed as an exact byte-identical duplicate.

The filename-based matching results total 4,085 matches. This is a filename-matching count, not a verified duplicate count. The inspected cross-class pair had different SHA-256 hashes, so it was not an exact byte-identical duplicate.

The filename matches do not establish complete original-to-augmented relationships or prove that the archive is free from train/test leakage. Near-duplicate images and augmentation relationships remain unresolved.

#### Annotation and sample structure

The available evidence supports image-level tomato class labels. It does not establish bounding-box or segmentation-mask annotations.

The following issues remain unresolved:

- The exact cause of the 20-image difference between the publication-reported augmented count and inspected archive count.
- Complete original-to-augmented image relationships.
- Comprehensive duplicate and near-duplicate status.
- Full train/test leakage assessment.
- Complete image-to-label mapping and annotation-file details.
- Biological sample identifiers and grouping information.
- Full archive integrity and metadata verification.

Augmented derivatives, once identified, must remain in the same data partition as their original images. A random image-level split should not be treated as leakage-safe until these relationships are investigated.

**Preliminary conclusion:** CCMT is a conditional candidate for five-class RGB image-level tomato disease classification. The archive counts and class distribution have now been inspected and documented. However, the 20-image discrepancy, original-to-augmented mapping, duplicate status, complete leakage assessment and biological sample grouping remain unresolved. Exploratory archive analysis is supported, but modelling approval and a final leakage-safe evaluation split remain pending.

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
| CCMT Tomato | Not assessed | Conditional | Not established | Not established |

### Interpretation

- VNIR and SWIR provide spectral information for investigating wheat Septoria, but neither currently supports a claim of validated disease prediction.
- Rice Sheath Blight is the clearest candidate for investigating severity estimation, provided its severity labels are verified.
- NWRD is potentially useful for pixel-level rust segmentation. Segmentation should not automatically be described as image-level disease classification.
- CCMT is a conditional candidate for image-level tomato disease classification. Its archive counts and class distribution have been inspected, but complete label mapping, augmentation relationships, leakage checks and biological sample grouping remain unresolved.
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
- Inspect the archive and confirm the available annotation structure.
- Retain the CC BY 4.0 public-record finding and comply with the stated attribution requirements.

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

### 4.3 Not approved for modelling yet

**VNIR Wheat Septoria**

Proposed use: Exploratory spectral analysis and comparison with SWIR.

Conditions:

- Establish calibration provenance.
- Investigate usable scan coverage.
- Address treatment confounding with scan identity.
- Clarify biological sample tracking.

**CCMT Tomato**

CCMT is a conditional candidate for RGB image-level disease classification. Its public dataset record, reported CC BY 4.0 licence, five tomato classes and published image counts have been reviewed.

The available CCMT tomato archive has now been inspected. The verified archive contains 27,158 images: 21,723 in the training set and 5,435 in the test set. The class distribution across both sets has also been checked. However, this total differs by 20 images from the publication-reported augmented count of 27,178.

Complete train/test leakage checks, near-duplicate verification, original-to-augmented image mapping, comprehensive file-to-label verification and biological sample grouping remain unresolved. One cross-class filename pairing was identified, but its SHA-256 hashes differ, so it is not a byte-identical duplicate.

Modelling approval should therefore remain pending until the remaining data-integrity and leakage checks are addressed and a defensible validation strategy is established.

### 4.4 Recommended project direction

1. Prioritise Rice Sheath Blight for severity-estimation investigation, subject to label verification.
2. Investigate NWRD for binary rust segmentation, subject to licence and archive verification.
3. Retain VNIR and SWIR as separate exploratory spectral research pipelines.
4. Consider CCMT for image-level classification. Its archive inventory and class distribution have been inspected, but remaining integrity and leakage checks must be completed before modelling approval.
5. Treat multimodal fusion and forecasting as future research directions, not confirmed deliverables.

These are provisional recommendations. Final selection must incorporate the remaining Member 2 and Member 3 investigation results and the team's overall project feasibility.

## 5. Experimental design recommendations

### 5.1 Experimental units

| Dataset | Proposed grouping unit | Required caution |
|---|---|---|
| VNIR Wheat | Pot or biological plant, after verification | Leaves and pixels from one biological unit must remain together |
| SWIR Wheat | Pot or biological plant, after verification | Multiple leaves and scans may belong to the same pot |
| Rice Sheath Blight | Original plant/specimen if identifiable; otherwise original image | Augmented copies must remain with their original image |
| NWRD Wheat Rust | Original field image or plant grouping, if identifiable | Image patches and masks from one image must remain together |
| CCMT Tomato | Undetermined | Establish sample structure and original-to-augmented relationships first |

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
- Does the archive contain any additional annotation files?

### NWRD

- What licence permits dataset reuse?
- Do the archive contents match the reported image and mask counts?
- Are all image-mask pairs valid?
- What are the exact mask pixel values?
- Which train/validation/test split is authoritative?

### CCMT Tomato

- What is the exact cause of the 20-image difference between the inspected archive count and the publication-reported augmented count?
- What is the complete image-to-label mapping and archive hierarchy?
- Can original images be reliably linked to augmented derivatives?
- Are there duplicate or near-duplicate images across the train and test partitions?
- Has the full train/test leakage assessment been completed?
- What biological sample grouping and collection information are available?

### Overall project

- Which datasets will be approved after the member investigations?
- Which task will become the primary modelling objective?
- Is there enough evidence for any multimodal or forecasting experiment?
- Can the selected datasets and objectives be completed within the project deadline?

## 11. References and source records

1. VNIR Wheat Septoria: Existing project records — `docs/VNIR_FINAL_SUITABILITY_ASSESSMENT_2026-11-17.md` and related VNIR progress reports.
2. SWIR Wheat Septoria: Recherche Data Gouv, DOI `10.57745/WVP0FJ` — https://entrepot.recherche.data.gouv.fr/dataset.xhtml?persistentId=doi:10.57745/WVP0FJ
3. SWIR associated paper: Latchoumane et al. (2025), *Data in Brief*, 59, 111404 — https://pmc.ncbi.nlm.nih.gov/articles/PMC11919375/
4. Rice Sheath Blight: Mendeley Data, DOI `10.17632/489spnkhp5.1` — https://data.mendeley.com/datasets/489spnkhp5/1
5. NWRD Wheat Rust: Zenodo, DOI `10.5281/zenodo.21672928` — https://zenodo.org/records/21672928
6. NWRD associated paper — https://pmc.ncbi.nlm.nih.gov/articles/PMC10422341/
7. NWRD GitHub repository — https://github.com/dll-ncai/NUST-Wheat-Rust-Disease-NWRD
8. CCMT Tomato: Mendeley Data, DOI `10.17632/bwh3zbpkpv.1` — https://data.mendeley.com/datasets/bwh3zbpkpv/1
9. CCMT associated paper, DOI `10.1016/j.dib.2023.109306`.

The source references identify the reported dataset and publication records. They do not imply that every archive, licence, label or acquisition detail has been independently verified.

## 12. Assessment status

**Completed in this assessment:**

- Existing VNIR evidence review.
- SWIR public-source investigation and readiness assessment review.
- Rice Sheath Blight public-source and severity-label evidence review.
- NWRD public-source and segmentation-label evidence review.
- CCMT official public-source investigation.
- CCMT archive-level image-count and class-distribution inspection.
- CCMT filename-based train/test matching and hash check of the identified cross-class pair.
- Cross-dataset comparison.
- Objective suitability evaluation.
- Preliminary dataset-selection recommendations.
- Experimental design recommendations.
- Multimodal integration requirements.
- Forecasting requirements and limitations.

**Still pending:**

- VNIR calibration and sample-linkage verification.
- SWIR raw-header, calibration and acquisition verification.
- Rice severity-class definitions, boundaries and image-to-label mapping.
- NWRD dataset reuse permission, archive inspection, image-mask pairing and split clarification.
- CCMT explanation of the 20-image discrepancy, complete original-to-augmented mapping, comprehensive duplicate and leakage checks, full label mapping and biological sample-grouping assessment.
- Final dataset selection and modelling approval.
- Remaining team investigation updates and team review.
- Documentation and reference verification.
- Git diff review and explicit approval before commit/push.

**Current conclusion:** TerraSpectra has a defensible research direction, but dataset approvals and modelling scope must remain conditional until the outstanding evidence is resolved. The project should prioritise scientifically supportable objectives and avoid claiming forecasting or multimodal fusion without adequate data.