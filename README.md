# TerraSpectra — Hyperspectral Crop Disease Analysis and Forecasting

**Research project | Data Science and Machine Learning**

## 1. Project Overview

TerraSpectra is a multi-dataset crop disease research project investigating RGB and hyperspectral imaging for crop disease detection, classification and severity assessment.

The project examines three imaging modalities:

- **RGB imaging:** Visible colour, texture and disease symptoms.
- **VNIR imaging:** Visible and near-infrared spectral information.
- **SWIR imaging:** Short-wave infrared spectral information.

The research aims to evaluate the suitability, reliability and scientific limitations of available crop disease datasets before selecting appropriate experimental objectives.

Multimodal integration and disease forecasting are considered future research directions, subject to sufficient evidence of sample correspondence, biological tracking and temporal consistency.

## 2. Research Objectives

1. Investigate the technical quality and suitability of RGB, VNIR and SWIR crop disease datasets.
2. Verify dataset sources, licences, metadata, annotations and sample information.
3. Assess disease labels, severity definitions and image or spectral data integrity.
4. Identify potential data leakage and establish defensible validation strategies.
5. Determine appropriate biological experimental units and grouping requirements.
6. Develop scientifically justified experimental designs for suitable research tasks.
7. Investigate multimodal integration and forecasting only when the required evidence is available.

## 3. Dataset Investigations

The project currently investigates five dataset candidates across three imaging modalities.

### 3.1 RGB Datasets

| Dataset | Crop / Disease | Proposed research task | Current status |
|---|---|---|---|
| CCMT Tomato | Tomato diseases | Five-class image classification | Conditional exploratory candidate; supplied Test split unsuitable for independent evaluation; label conflicts and biological grouping unresolved |
| Rice Sheath Blight | Rice sheath blight | Six-level disease severity estimation | Conditional exploratory candidate; duplicate-label conflicts, severity criteria and biological grouping unresolved |
| NWRD Wheat Rust | Wheat rust | Binary disease segmentation | Conditional exploratory candidate; reuse permission and annotation consistency unresolved |

### 3.2 Hyperspectral Datasets

| Dataset | Modality | Proposed research task | Current status |
|---|---|---|---|
| Wheat Septoria | VNIR | Exploratory spectral analysis | Not approved for modelling |
| Wheat Septoria | SWIR | Exploratory spectral analysis | Technical and metadata investigation documented; calibration provenance unresolved; modelling not approved |

**Important:** These datasets are being investigated independently. Their availability does not imply approval for preprocessing, model training or integration.

## 4. Current Investigation Findings

### CCMT Tomato — RGB

- The inspected archive contains 5,805 raw images, 21,723 training images and 5,445 test images.
- SHA-256 and CRC32 comparisons identified 4,084 unique shared contents and 4,085 matching Train–Test file pairs; 4,084 Test entries have at least one exact-content match in Train.
- Raw-to-augmented inspection identified 6,202 exact file pairs; 4,771 raw entries had at least one exact-content match, while 1,034 had no exact-content match.
- Two cross-class exact-content conflict groups were identified. Their correct labels remain unresolved.
- Class imbalance is substantial: Septoria has approximately 5.84 times as many raw images as Healthy.
- Biological sample independence is unestablished.
- The supplied Test partition is not accepted as an independent evaluation set.

### Rice Sheath Blight — RGB

- The archive inventory identifies six folder-based severity stages.
- Total reported inventory: 1,609 images.
- The six class counts are 157, 326, 410, 355, 263 and 98.
- SHA-256 inspection identified 1,602 unique image contents and seven duplicate groups: five within the same stage and two across different stages.
- The two cross-stage duplicate groups contain identical image content assigned to different severity stages; the correct labels remain unresolved.
- The public dataset record reports a CC BY 4.0 licence.
- Exact severity boundaries, individual image-label correctness and biological grouping still require verification.

### NWRD Wheat Rust — RGB

- The archive inventory reports 100 RGB images and 100 corresponding masks.
- The archive checksum and filename-level image-mask pairing have been verified.
- Image-mask dimensions match for 99 of 100 pairs. The image `train/images/101.jpg` is 19 pixels wider and 21 pixels taller than its mask.
- The RGB images contain one byte-identical duplicate pair (`train/images/15.jpg` and `train/images/32.jpg`), but their masks differ in foreground coverage.
- No exact duplicate RGB image was identified across the supplied Train and Test partitions.
- Dataset reuse permission and the intended meaning of mask foreground pixels remain unresolved; the duplicate-image mask difference requires annotation review.
- Mask values are recorded as 0 and 255; foreground semantics and the published-versus-README split discrepancy still require verification.

### Wheat Septoria — VNIR

- Four inspected ENVI headers contain 1,370 lines, 1,024 samples and 216 spectral bands.
- The inspected headers record wavelengths in nanometres and an ignore value of 4095.
- Original and corrected spectral data are maintained as separate artifacts.
- Calibration provenance, processing reproducibility and biological sample tracking remain unresolved.
- The current evidence supports exploratory investigation only.

### Wheat Septoria — SWIR

- The official dataset archive was downloaded and its MD5 checksum verified.
- Read-only inventory confirmed 96 HYSPEX files, 96 matching headers, 96 JPG files and 259 CSV files.
- The inspected headers contain 256 spectral bands across 964.181280–2494.388419 nm.
- All 96 scan IDs match the 96 official pot-side metadata groups. This mapping does not establish 96 independent biological samples or plants.
- The metadata contains 279 leaf records, while coordinate CSVs exist for 259 leaf IDs. Twenty metadata leaf IDs have no corresponding coordinate CSV; no CSV leaf ID was unmatched to the metadata.
- The publication documents column 1 as the vertical line coordinate and column 2 as the horizontal sample coordinate. A recheck of `24_G_leaf3.csv` found no out-of-range rows under that convention; visual annotation correspondence has not been independently validated.
- The `18_D` HYSPEX/header/JPG files are stored under the `18_G` folder, while the `18_D` coordinate CSVs are stored under `18_D`.
- Calibration-reference correspondence and whether the archived cubes are calibrated reflectance remain unverified. The header field `CalibAvailable=1` alone does not establish calibration.
- Preprocessing and modelling have not been approved.

## 5. Scientific Methodology and Data Integrity

TerraSpectra follows evidence-based dataset assessment and experimental-design principles.

### Data preservation

- Original raw measurements, images and masks must remain unchanged.
- Derived datasets must retain traceable provenance.
- Dataset inspection and verification must be documented.
- Unverified calibration or processing steps must not be presented as established facts.

### Leakage prevention

- Related scans, leaves, images and augmented copies must remain in the same data partition where they originate from the same sample or source.
- Random pixel-level splitting must not be used when pixels originate from the same biological sample.
- Training, validation and testing must be designed around appropriate grouping units.
- Test data must remain independent of model selection and hyperparameter tuning.

### Biological independence

Pixels, image patches and multiple leaves from the same biological unit must not automatically be treated as independent observations.

The true experimental unit must be established from authoritative dataset protocols and sample records.

### Forecasting requirements

Forecasting requires repeated observations of identifiable biological units, reliable chronological information, verified progression labels and future-time holdout evaluation.

Repeated acquisition dates alone do not establish longitudinal tracking.

## 6. Multimodal Research Direction

The project investigates RGB, VNIR and SWIR imaging as separate research pipelines.

Multimodal integration may be considered only when:

- The modalities represent corresponding biological samples.
- Disease labels and target definitions are compatible.
- Acquisition conditions and metadata can be reconciled.
- Required spatial or sample-level correspondence is established.
- Independent evaluation can be performed without leakage.

**Current decision:** RGB, VNIR and SWIR remain separate. A unified multimodal forecasting experiment has not been established or approved.

## 7. Team Responsibilities

| Team member | Responsibility |
|---|---|
| Hiba | VNIR investigation, project coordination, experimental design and documentation integration |
| Fahma | SWIR dataset investigation and technical verification |
| Afnan | RGB dataset investigation: CCMT Tomato, Rice Sheath Blight and NWRD Wheat Rust |

Investigation findings are incorporated into the central project documentation after evidence review.

## 8. Repository Structure

```text
TerraSpectra-Hyperspectral-Crop-Disease-Forecasting/
│
├── README.md
│
├── data/
│   └── raw/
│
├── docs/
│   ├── PROJECT_SCOPE.md
│   ├── DATASET_ASSESSMENT.md
│   ├── DATASET_INVENTORY.md
│   ├── CROSS_DATASET_SUITABILITY_ASSESSMENT_2026-11-18.md
│   ├── CONSOLIDATED_EXPERIMENTAL_DESIGN_2026-11-21.md
│   ├── TEAM_INVESTIGATION_TRACKER_2026-11-17.md
│   ├── RGB_PROGRESS_REPORT_2026-11-16.md
│   ├── VNIR_PROGRESS_REPORT_2026-11-25.md
│   ├── VNIR_FINAL_SUITABILITY_ASSESSMENT_2026-11-17.md
│   ├── SWIR_INVESTIGATION_REPORT_UPDATED.md
│   ├── RICE_SHEATH_BLIGHT_SEVERITY_LABEL_VERIFICATION.md
│   ├── NWRD_FOLLOW_UP_VERIFICATION.md
│   └── TOMATO_DATASET_SOURCE_VERIFICATION.md
│
└── research/
    ├── RGB/
    ├── VNIR/
    └── SWIR/
```

The structure above identifies important project documentation and intended research areas. The actual contents of local research folders may vary.

## 9. Current Project Status

**Project stage:** Dataset investigation, evidence consolidation and experimental-design review.

| Research area | Status |
|---|---|
| VNIR investigation | Selected-scan technical verification documented; calibration and biological tracking unresolved |
| SWIR investigation | Archive, headers and scan-to-pot-side metadata mapping verified; calibration provenance and leaf-level annotation limitations documented |
| CCMT Tomato | Exact Train–Test overlap and raw-to-augmented lineage investigated; label conflicts and independent evaluation limitations remain |
| Rice Sheath Blight | Archive inventory and duplicate groups verified; cross-stage label conflicts and biological grouping unresolved |
| NWRD Wheat Rust | Image-mask pairing, dimensions and duplicate-image issue investigated; reuse permission and annotation meaning unresolved |
| Final dataset selection | Pending |
| Experimental-design approval | Pending |
| Preprocessing and model training | Not approved or started |
| Multimodal integration | Future research direction |
| Disease forecasting | Future research direction, subject to longitudinal evidence |

## 10. Project Documentation

For detailed investigation findings and decisions, refer to:

- [Project Scope](docs/PROJECT_SCOPE.md)
- [Dataset Assessment](docs/DATASET_ASSESSMENT.md)
- [Dataset Inventory](docs/DATASET_INVENTORY.md)
- [Cross-Dataset Suitability Assessment](docs/CROSS_DATASET_SUITABILITY_ASSESSMENT_2026-11-18.md)
- [Consolidated Experimental Design](docs/CONSOLIDATED_EXPERIMENTAL_DESIGN_2026-11-21.md)
- [Team Investigation Tracker](docs/TEAM_INVESTIGATION_TRACKER_2026-11-17.md)
- [VNIR Progress Report](docs/VNIR_PROGRESS_REPORT_2026-11-25.md)
- [SWIR Investigation Report](docs/SWIR_INVESTIGATION_REPORT_UPDATED.md)
- [Rice Sheath Blight Verification](docs/RICE_SHEATH_BLIGHT_SEVERITY_LABEL_VERIFICATION.md)
- [NWRD Follow-up Verification](docs/NWRD_FOLLOW_UP_VERIFICATION.md)
- [CCMT Tomato Source Verification](docs/TOMATO_DATASET_SOURCE_VERIFICATION.md)

## 11. Research Restrictions

Until dataset selection and experimental-design approval:

- Do not modify original raw data.
- Do not start preprocessing or calibration transformations.
- Do not perform feature engineering or model training.
- Do not combine RGB, VNIR and SWIR datasets without verified correspondence.
- Do not treat the supplied CCMT Test partition as independent.
- Do not claim biological independence without sample-level evidence.
- Do not claim forecasting capability without validated longitudinal tracking.

All conclusions must distinguish verified findings, previously reported information, assumptions and unresolved questions.

## 12. Project Direction

The immediate priority is to resolve dataset-integrity, licensing, annotation, calibration, biological-grouping and leakage questions.

The project will select research objectives only when the available evidence supports a scientifically defensible experiment.

> **TerraSpectra aims to establish reliable dataset foundations and experimental design before developing crop disease analysis models.**
