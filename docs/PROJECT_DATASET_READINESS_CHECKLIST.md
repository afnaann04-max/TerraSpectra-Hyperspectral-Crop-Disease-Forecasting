\# TerraSpectra — Project Dataset Readiness Checklist



\## 1. Purpose



This checklist defines the verification requirements that must be satisfied before the TerraSpectra project proceeds to preprocessing, model development, evaluation and application integration.



The project uses VNIR, SWIR and RGB data for crop disease detection and forecasting research.



The checklist distinguishes completed investigations from pending verification and scientific decisions. A dataset must not be considered model-ready merely because its files are available.



\## 2. Dataset Inventory



| Dataset | Modality | Current status |

|---|---|---|

| VNIR | Hyperspectral | Initial dataset investigation and validation completed; scientific limitations remain |

| Wheat Septoria | SWIR hyperspectral | Verification pending |

| NWRD Wheat Rust | RGB | Availability and suitability verification pending |

| CCMT Tomato | RGB | Availability and suitability verification pending |

| Rice Sheath Blight | RGB | Availability and suitability verification pending |



\## 3. General Dataset Verification



For every dataset, verify the following:



\- \[ ] Identify the official dataset source.

\- \[ ] Record the official dataset URL and DOI, where available.

\- \[ ] Verify the dataset licence and permitted usage.

\- \[ ] Record the original publication or accompanying documentation.

\- \[ ] Confirm the downloaded archive and extracted directory structure.

\- \[ ] Record expected and actual file counts.

\- \[ ] Check filenames and file extensions.

\- \[ ] Identify missing, duplicate or unexpected files.

\- \[ ] Verify acquisition dates and experimental metadata, where available.

\- \[ ] Identify crop species, disease classes and sample labels.

\- \[ ] Preserve original data without modifying source files.

\- \[ ] Record all verification procedures and findings.



\## 4. VNIR Readiness



\### Completed investigation



\- \[x] Reconciliation of combined, baseline and candidate VNIR datasets.

\- \[x] Verification of spectral dimensions and wavelength information.

\- \[x] Candidate feature subset comparison against baseline features.

\- \[x] Coordinate alignment checks across the available leaf datasets.

\- \[x] Investigation of invalid values, saturation values and missing observations.

\- \[x] Numerical validation of corrected NPZ outputs.

\- \[x] Documentation of VNIR dataset structure and validation findings.



\### Pending scientific decisions



\- \[ ] Confirm independent biological sample units.

\- \[ ] Investigate possible scan, acquisition-session and treatment confounding.

\- \[ ] Determine an appropriate missing-value strategy.

\- \[ ] Investigate sensor calibration and reflectance correction.

\- \[ ] Assess class imbalance and the need for additional samples.

\- \[ ] Determine whether genuine temporal forecasting is supported.

\- \[ ] Finalize a scientifically justified preprocessing protocol.



\## 5. SWIR Readiness



\- \[ ] Verify the official Wheat Septoria SWIR source.

\- \[ ] Independently verify DOI, source URL and licence.

\- \[ ] Inspect the existing downloaded archive.

\- \[ ] Verify the expected scan count and filenames against the source.

\- \[ ] Inspect spectral dimensions and wavelength metadata.

\- \[ ] Examine acquisition conditions and sample information.

\- \[ ] Check data quality, missing values and invalid measurements.

\- \[ ] Document preprocessing requirements.

\- \[ ] Record limitations and unresolved verification questions.



\*\*Status:\*\* Verification is in progress. Reported scan counts and metadata must be independently supported before being marked verified.



\## 6. RGB Readiness



For NWRD Wheat Rust, CCMT Tomato and Rice Sheath Blight:



\- \[ ] Confirm the official dataset source and licence.

\- \[ ] Verify downloaded image files and directory structure.

\- \[ ] Inspect image dimensions, formats and colour channels.

\- \[ ] Verify annotations, labels and disease categories.

\- \[ ] Identify duplicate, corrupted or unreadable images.

\- \[ ] Inspect class distribution and imbalance.

\- \[ ] Check sample identity and acquisition metadata.

\- \[ ] Identify whether images contain leaf-level or plant-level observations.

\- \[ ] Document any dataset-specific limitations.



\## 7. Experimental Design and Data Leakage Prevention



Before model training:



\- \[ ] Define the independent experimental sample unit.

\- \[ ] Identify plant, leaf, scan, image and acquisition-session relationships.

\- \[ ] Prevent related observations from appearing across training and testing splits.

\- \[ ] Use group-aware splitting where required.

\- \[ ] Keep an independent test set.

\- \[ ] Fit imputation and preprocessing transformations using training data only.

\- \[ ] Document class distribution across all splits.

\- \[ ] Define evaluation metrics appropriate to the dataset and class balance.



\## 8. Cross-Dataset Compatibility



Before combining VNIR, SWIR and RGB:



\- \[ ] Confirm crop species compatibility.

\- \[ ] Confirm disease-label compatibility.

\- \[ ] Check sample identity and correspondence.

\- \[ ] Compare acquisition conditions and experimental designs.

\- \[ ] Examine differences in spatial and spectral resolution.

\- \[ ] Determine whether a valid multimodal analysis is scientifically justified.



Different datasets must not be combined solely because they concern crop diseases.



\## 9. Model Training Readiness



Model development should begin only after the relevant dataset and experimental-design checks are complete.



Potential models for evaluation include:



\- Logistic Regression

\- Random Forest

\- Support Vector Machine

\- XGBoost or LightGBM

\- One-dimensional CNN for suitable spectral data

\- Two-dimensional CNN for suitable image or hyperspectral cube data



Model selection must depend on the actual data structure, sample size and scientific objective.



\## 10. Evaluation and Explainability



\- \[ ] Define baseline models.

\- \[ ] Evaluate using suitable classification metrics.

\- \[ ] Generate confusion matrices.

\- \[ ] Report precision, recall and F1-score.

\- \[ ] Consider balanced accuracy and ROC-AUC or PR-AUC where appropriate.

\- \[ ] Perform error analysis.

\- \[ ] Evaluate generalization using independent samples.

\- \[ ] Investigate important spectral wavelengths or regions where applicable.

\- \[ ] Apply suitable explainability methods.

\- \[ ] Document model limitations and uncertainty.



\## 11. Final Readiness Decision



A dataset should be marked model-ready only when:



1\. Its source and usage permissions are established.

2\. Its files and metadata have been verified.

3\. Its labels and sample identities are sufficiently understood.

4\. Data quality issues have been investigated.

5\. Its preprocessing strategy is documented.

6\. Its experimental split prevents data leakage.

7\. Remaining limitations are explicitly documented.



\## 12. Documentation and Change Tracking



For every dataset, maintain:



\- Source and licence information.

\- Dataset inventory.

\- Verification report.

\- Data-quality report.

\- Preprocessing decisions.

\- Known limitations.

\- Experimental-design decisions.

\- Validation results.



\*\*Important:\*\* This checklist is a project-level planning and verification document. It does not claim that pending dataset investigations, model training or forecasting experiments have been completed.

