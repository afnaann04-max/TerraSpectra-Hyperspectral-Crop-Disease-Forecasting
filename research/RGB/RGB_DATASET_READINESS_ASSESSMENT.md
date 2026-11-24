# TerraSpectra – RGB Dataset Readiness Assessment

**Project:** TerraSpectra – Hyperspectral Crop Disease Forecasting
**Responsibility:** Member 3 – RGB Dataset Investigation
**Assessment date:** 24 November 2026
**Branch:** `Afnan`
**Report status:** Dataset investigation and evidence-based suitability assessment

---

## 1. Objective

The objective of this assessment is to evaluate three RGB crop disease datasets for their potential use in the TerraSpectra project.

The investigation focuses on:

1. Dataset source and provenance.
2. Image inventory, formats and reported characteristics.
3. Disease and severity label definitions.
4. Biological sample independence and possible repeated observations.
5. Suitability for disease classification, severity classification, early detection and temporal forecasting.
6. Dataset limitations and recommendations for further use.

The assessment is based on existing source-verification reports, archive-level inventory results and filename metadata analysis.

**Investigation restrictions:** No raw images were modified. No image preprocessing, feature extraction, feature engineering, visual inspection or model training was performed.

## 2. Evidence Classification

The following terms are used throughout this report:

- **Verified:** Confirmed through archive inventory, file metadata, checksum or filename-level checks.
- **Source-reported:** Information documented by the dataset publisher, research paper or README.
- **Inferred:** A cautious interpretation based on available evidence.
- **Unresolved:** Information that could not be established using the available evidence.

Archive-level verification does not establish visual image quality, annotation correctness or biological sample independence.

---

## 3. Dataset Overview

| Dataset | Source | Main crop/disease | Main annotation type |
|---|---|---|---|
| NWRD Wheat Rust | Zenodo | Wheat stripe rust | Binary segmentation masks |
| CCMT Tomato | Mendeley Data | Five tomato categories | Class-wise folders |
| Rice Sheath Blight | Mendeley Data | Rice sheath blight | Six severity-stage folders |

### 3.1 NWRD Wheat Rust

**Dataset name:** NUST Wheat Rust Disease Dataset (NWRD)
**DOI:** 10.5281/zenodo.21672928
**Official source:** https://zenodo.org/records/21672928
**GitHub:** https://github.com/dll-ncai/NUST-Wheat-Rust-Disease-NWRD
**Research paper:** https://doi.org/10.3390/s23156942

**Source-reported characteristics:**

- 100 RGB images.
- JPG original images and PNG segmentation masks.
- Binary segmentation classes: Rust and Non-rust.
- Reported resolutions: 6016 × 4000 and 4608 × 3456 pixels.
- Collection location: National Agricultural Research Centre (NARC), Islamabad, Pakistan.
- Collection period: 2021–2022.
- Images include aerial, ground and front views.
- Different viewing distances, illumination conditions and crop densities are represented.

**Archive-verified characteristics:**

| Characteristic | Verified result |
|---|---:|
| Total JPG images | 100 |
| Total PNG masks | 100 |
| Training images | 90 |
| Training masks | 90 |
| Testing images | 10 |
| Testing masks | 10 |
| Unmatched image-mask filenames | 0 |
| Shared train-test filenames | 0 |
| Separate validation folder | Not found |

The downloaded archive matched the official MD5 checksum.

**Annotation information:**

The research paper reports manual pixel-level binary segmentation annotations.

- Rust: Pixels representing visible wheat stripe rust.
- Non-rust: Healthy leaves, stems, soil, shadows and other non-rust regions.

The exact mask pixel values and visual alignment have not been verified.

**Biological sample independence:**

The available documentation does not establish unique leaf, plant, plot or experimental-unit identifiers. Multiple wheat leaves may appear in one field image.

The absence of shared filenames between train and test does not establish that the images represent biologically independent samples.

**Unresolved information:**

- Wheat variety.
- Camera model and acquisition settings.
- Exact image-level collection dates.
- Biological sample identifiers and grouping.
- Visual image-mask alignment.
- Visual duplicates under different filenames.
- Dataset image and mask reuse rights.
- Exact validation-split methodology.

The NLM Dataset Catalog lists CC BY 4.0, but the Zenodo rights information and other licence displays are inconsistent. The GitHub MIT licence must not automatically be treated as the licence for the image and mask assets.

### 3.2 CCMT Tomato Dataset

**Dataset name:** Dataset for Crop Pest and Disease Detection
**Source:** Mendeley Data
**DOI:** 10.17632/bwh3zbpkpv.1
**Source:** https://data.mendeley.com/datasets/bwh3zbpkpv/1
**Licence:** CC BY 4.0, as reported in the dataset assessment.

The dataset contains four crops: Cashew, Cassava, Maize and Tomato.

**Source-reported tomato characteristics:**

- Five categories.
- Reported raw Tomato images: 5,435.
- Reported augmented Tomato images: 27,178.
- RGB images collected from local farms in Ghana.
- JPG image format.
- Image dimensions vary.

**Tomato categories:**

1. Healthy
2. Leaf blight
3. Leaf curl
4. Septoria leaf spot
5. Verticillium wilt

**Archive-verified inventory:**

| Class | Raw images | Augmented train | Augmented test | Augmented total |
|---|---:|---:|---:|---:|
| Healthy | 470 | 2,000 | 500 | 2,500 |
| Leaf blight | 1,301 | 5,200 | 1,309 | 6,509 |
| Leaf curl | 518 | 2,050 | 532 | 2,582 |
| Septoria leaf spot | 2,743 | 9,373 | 2,340 | 11,713 |
| Verticillium wilt | 773 | 3,100 | 764 | 3,864 |
| **Total** | **5,805** | **21,723** | **5,445** | **27,168** |

The archive contains 27,168 augmented Tomato images, while the published dataset description reports 27,178. The difference of 10 images remains unresolved.

The archive raw count of 5,805 also differs from the publication's reported raw Tomato count of 5,435.

**Data leakage findings:**

Exact-image comparisons identified:

- 4,084 exact-image matches between augmented training and testing sets.
- 5,443 of 5,445 test filenames had a corresponding normalized filename pattern in training.
- Original-to-augmented image lineage remains unverified.

The exact-image overlap is a substantial problem for the existing train/test split. It should not be treated as a reliable independent evaluation split.

**Biological sample independence:**

The available documentation does not establish unique plant, leaf, farm plot or experimental-unit identifiers.

It is also unresolved whether multiple photographs or augmented variants of the same original biological sample are distributed across the training and testing sets.

The exact-image overlap confirms a file-level overlap problem, but it does not independently establish the complete biological relationship between all images.

**Unresolved information:**

- Remaining publication/archive count discrepancies.
- Original-to-augmented image lineage.
- Biological sample identifiers and grouping.
- Near-duplicate relationships beyond exact-image matches.
- Whether the source collection includes repeated observations of the same plant over time.

### 3.3 Rice Sheath Blight Dataset

**Dataset name:** Colour-Mix Augmentation Dataset for Rice Sheath Blight Severity Estimation
**Source:** Mendeley Data
**DOI:** 10.17632/489spnkhp5.1
**Dataset:** https://data.mendeley.com/datasets/489spnkhp5/1
**Licence:** CC BY 4.0, as reported in the dataset investigation.

The dataset is intended for fine-grained rice sheath blight severity estimation.

The README identifies the disease as rice sheath blight caused by *Rhizoctonia solani*.

**Source-reported characteristics:**

- 1,609 images.
- JPG and PNG formats.
- Reported resolution: 3024 × 4032 pixels.
- Images collected directly from agricultural fields.
- Natural lighting and environmental backgrounds.
- Soil, water and varying growth stages are represented.

**Archive-verified folder inventory:**

| Folder | Severity description | Image count |
|---|---|---:|
| Stage-1 | Healthy / mild symptoms | 157 |
| Stage-2 | Initial infection | 326 |
| Stage-3 | Lesions covering less than 25% of plant height | 410 |
| Stage-4 | Lesions reaching 25–50% of plant height | 355 |
| Stage-5 | Lesions reaching 50–75% of plant height | 263 |
| Stage-6 | Lesions reaching flag leaf or more than 75% | 98 |
| **Total** | | **1,609** |

The archive inventory confirms the six stage folders and their file counts. The reported image dimensions have not been independently confirmed through image inspection.

**Severity-label information:**

The README describes severity using:

- Vertical progression of lesions relative to total plant height.
- Chromatic intensity, from water-soaked green to necrotic gray-white or brown.
- Lesion density and spatial spread.
- Lesion coalescence.

The six folder labels provide a structured severity-category system.

However, some definitions remain incomplete:

- Stage-2 is described as small lesions restricted to the lower sheath without a precise numerical boundary.
- Stage-6 includes reaching the flag leaf or more than 75% of plant height.
- The exact numerical scoring scale and reference standard are not established.

The standard 0–9 severity scale must not be assumed to apply to this dataset.

No separate CSV, JSON, XML or other annotation metadata file was identified in the archive inventory. Folder assignment is structurally verified, but the correctness of individual image labels has not been visually verified.

**Filename and sample-grouping investigation:**

The archive filenames include identifiers such as `IMG_<number>@<date-like-text>`.

Filename analysis found:

- 179 repeated image-number identifiers.
- 1,545 files under repeated image-number identifiers.
- All 179 repeated identifiers appeared across multiple severity-stage folders.
- Only one matching image-number/date-like key was found across different stages: `IMG_4@10MAR25-KTK`, appearing in Stage-4 and Stage-5 with a `(2)` suffix on one filename.

The two files have different SHA-256 hashes. This confirms different file contents at the byte level, but does not establish whether they show different plants, the same plant or related photographs.

**Important interpretation:**

Repeated image-number identifiers do not prove repeated observations of the same plant. The identifiers may be reused across different plants or collections.

Similarly, different dates in filenames do not establish longitudinal progression of an identified plant.

**Biological sample independence:**

The README does not provide a verified mapping between image identifiers and unique plants, leaves, plots or experimental units.

Therefore, biological sample independence remains unverified.

The dataset must not be treated as having independent biological samples solely because images are stored in separate severity folders.

**Unresolved information:**

- Unique plant, leaf or plot identifiers.
- Whether repeated image-number identifiers represent the same biological samples.
- Exact severity boundaries for all six stages.
- Independent confirmation of image-level label correctness.
- Whether observations form genuine longitudinal progression records.
- Exact acquisition dates and sample-level collection schedules.

---

## 4. Biological Sample Independence Assessment

Biological sample independence is important when designing training, validation and testing splits.

Multiple images of the same leaf or plant must not automatically be treated as independent samples. Otherwise, a model may encounter related biological material in both training and testing data.

| Dataset | Unique biological sample IDs | Grouping information | Independence status |
|---|---|---|---|
| NWRD | Not documented | No verified plant/leaf/plot grouping | Unverified |
| Tomato CCMT | Not documented | Original-to-augmented lineage unresolved | Unverified |
| Rice Sheath Blight | Not documented | Repeated image-number identifiers require interpretation | Unverified |

### 4.1 Implications for Dataset Splitting

- NWRD: Filename-level separation is verified, but biological independence is not.
- Tomato: Exact-image overlap already exists between the augmented training and testing sets. The current split is unsuitable for reliable independent evaluation.
- Rice: Images with related filename identifiers may represent related samples, but this relationship has not been established.

### 4.2 Required Principle

If unique biological sample identifiers become available, all images belonging to the same biological sample should be assigned to a single partition.

A random image-level split should not be assumed to provide biological independence.

---

## 5. Suitability Assessment by Research Task

### 5.1 Disease Classification

**NWRD:** Potentially suitable for wheat rust classification, subject to image-content and label verification. The dataset was primarily designed for semantic segmentation.

**Tomato CCMT:** Potentially suitable for five-class tomato disease classification. The existing augmented train/test split has substantial exact-image overlap and should not be used as an independent evaluation split.

**Rice Sheath Blight:** Potentially suitable for classification of six severity-stage categories. Image-level label correctness and biological grouping remain unresolved.

### 5.2 Severity Classification

**NWRD:** Not established. The documented annotation is binary rust/non-rust segmentation, not a verified severity scale.

**Tomato CCMT:** Not established. Its five classes represent healthy and disease categories, not documented severity levels.

**Rice Sheath Blight:** The strongest candidate among the three for severity classification because six severity-stage folders and descriptive criteria are provided. Exact label boundaries and biological sample grouping still require verification.

### 5.3 Early Disease Detection

None of the three datasets currently provides sufficient verified evidence for an early-detection claim.

Rice includes an initial-infection stage, but its image-level labels and relationship to later observations of the same biological samples have not been verified.

NWRD and Tomato do not provide verified early-stage labels in the reviewed evidence.

### 5.4 Temporal Disease Forecasting

None of the three datasets currently supports a verified temporal forecasting claim.

A forecasting dataset would require evidence such as:

- Unique plant or plot identifiers.
- Repeated observations of the same biological units.
- Reliable observation dates or time intervals.
- Verified disease-stage progression.
- A defined future outcome or prediction target.

The available filename patterns and severity folders are insufficient to establish these requirements.

---

## 6. Comparative Readiness Summary

| Evaluation criterion | NWRD | Tomato CCMT | Rice Sheath Blight |
|---|---|---|---|
| Public source identified | Yes | Yes | Yes |
| Archive inventory verified | Yes | Yes | Yes |
| Disease categories documented | Yes | Yes | Yes |
| Severity categories documented | No | No | Six stages |
| Annotation structure | Binary masks | Class folders | Severity folders |
| Biological sample IDs verified | No | No | No |
| Biological independence verified | No | No | No |
| Exact-image train/test overlap identified | Not checked | 4,084 matches | Not established |
| Temporal progression verified | No | No | No |
| Reuse rights fully resolved | No | Source reports CC BY 4.0 | Source reports CC BY 4.0 |

---

## 7. Dataset-Specific Recommendations

### 7.1 NWRD Wheat Rust

**Recommendation:** Retain as a potential wheat rust segmentation dataset, subject to licence and annotation-quality clarification.

Before use:

1. Resolve reuse rights for the images and masks.
2. Verify mask alignment and pixel values if image inspection is authorized.
3. Establish biological sample grouping if possible.
4. Review the validation-split methodology.
5. Do not assume filename-level separation proves biological independence.

### 7.2 Tomato CCMT

**Recommendation:** Retain as a candidate for disease classification, but do not use its existing train/test split for independent evaluation.

Before use:

1. Resolve the published and archive count discrepancies.
2. Establish original-to-augmented image lineage.
3. Investigate biological sample grouping.
4. Establish a suitable independent evaluation strategy if the required evidence becomes available.
5. Keep the exact-image overlap finding documented.

### 7.3 Rice Sheath Blight

**Recommendation:** Prioritize for further investigation as a potential severity-classification dataset.

Before use:

1. Clarify the six severity-stage definitions.
2. Establish the meaning of repeated image-number identifiers.
3. Determine whether plant, leaf or plot identifiers exist.
4. Verify image-level labels if inspection is authorized.
5. Establish whether any genuine longitudinal observations exist.

Do not claim temporal forecasting suitability based only on stage folders or date-like filename components.

---

## 8. Overall Conclusion

The three RGB datasets offer different potential contributions to TerraSpectra:

- NWRD provides binary wheat rust segmentation annotations.
- Tomato CCMT provides five tomato disease categories.
- Rice Sheath Blight provides six severity-stage categories.

Rice Sheath Blight is the strongest current candidate for severity-classification investigation because its README documents six stages and provides descriptive severity criteria.

Tomato CCMT is a candidate for disease classification, but its existing augmented training and testing sets contain 4,084 exact-image matches. This is a major evaluation limitation.

NWRD is a potential wheat rust segmentation dataset with verified archive-level image-mask filename pairing. However, its small size, unresolved biological independence and dataset reuse rights require further consideration.

**No dataset currently has verified biological sample independence. None currently provides sufficient evidence to support temporal disease forecasting.**

Final dataset selection should depend on the project's exact research objective, biological sample grouping, annotation reliability, evaluation design and reuse permissions.

---

## 9. Investigation Restrictions and Reproducibility

The following restrictions were maintained during this investigation:

- Raw image files were not modified.
- No image preprocessing was performed.
- No feature extraction or feature engineering was performed.
- No model training was performed.
- No datasets were merged.
- Rice and Tomato filename metadata were investigated without image extraction.
- NWRD archive counts, checksum and filename pairing were verified at archive level.
- Visual image quality and annotation correctness were not claimed as verified.
- No author contact was initiated.

Existing dataset-specific reports and evidence were retained in the repository.

---

## 10. Existing Supporting Reports

The following reports support this consolidated assessment:

1. `docs/NWRD_WHEAT_RUST_SOURCE_VERIFICATION.md`
2. `docs/NWRD_FOLLOW_UP_VERIFICATION.md`
3. `docs/TOMATO_DATASET_ASSESSMENT.md`
4. `docs/TOMATO_DATASET_SOURCE_VERIFICATION.md`
5. `docs/RICE_SHEATH_BLIGHT_SEVERITY_LABEL_VERIFICATION.md`
6. `docs/DATASET_INVENTORY_CHECKLIST.md`

---

## 11. Final Status

**RGB dataset investigation:** Consolidated assessment prepared.

**Biological sample independence:** Unverified for all three datasets.

**Severity classification:** Rice Sheath Blight is the strongest candidate for further investigation.

**Disease classification:** Tomato CCMT and NWRD remain conditional candidates.

**Temporal forecasting:** Not supported by the currently verified evidence.

**Further work:** Requires clarification of biological sample grouping, label reliability, evaluation methodology and dataset reuse permissions.

**Prepared by:** Member 3 – RGB Dataset Investigation
**Date:** 24 November 2026
