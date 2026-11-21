# Rice Sheath Blight - Severity Label Verification Report

**Project:** TerraSpectra - RGB Dataset Investigation
**Team Member:** Member 3  
**Date:** 16 November 2026

## 1. Dataset Identification

- **Dataset:** Colour-Mix Augmentation Dataset for Rice Sheath Blight Severity Estimation
- **Source:** Mendeley Data
- **DOI:** 10.17632/489spnkhp5.1
- **Dataset URL:** https://data.mendeley.com/datasets/489spnkhp5/1
- **Reported original images:** 1,609 JPG images
- **Reported severity classes:** Six
- **Download status:** Not downloaded
- **Dataset status:** Candidate only; not finally approved

## 2. Severity Class Investigation

The official Mendeley description confirms that every image is annotated into one of six progressive disease severity levels.

However, the exact names, numerical codes and definitions of the six classes are not provided in the publicly accessible description.

| Class number | Exact class name/code | Severity definition |
|---|---|---|
| 1 | Not disclosed | Not disclosed |
| 2 | Not disclosed | Not disclosed |
| 3 | Not disclosed | Not disclosed |
| 4 | Not disclosed | Not disclosed |
| 5 | Not disclosed | Not disclosed |
| 6 | Not disclosed | Not disclosed |

No class names or severity boundaries have been assumed or invented.

## 3. Documented Severity Assessment Criteria

According to the official dataset description, visual severity assessment considers:

- Lesion extent.
- Lesion height progression along the sheath.
- Symptom colour intensity.
- Lesion density and spatial spread.

The images were reviewed by a domain expert from the Department of Plant Pathology, College of Agriculture, Padannakkad, Kasargod.

The description mentions visual scoring using a standard evaluation scale but does not identify the exact scale or provide its numerical scoring criteria.

## 4. Severity Measurement Method

| Measurement | Verification status |
|---|---|
| Lesion extent | Mentioned |
| Lesion height progression | Mentioned |
| Symptom colour intensity | Mentioned |
| Lesion density and spatial spread | Mentioned |
| Percentage of affected sheath | Not explicitly specified |
| Lesion area percentage | Not explicitly specified |
| Relative lesion height (RLH) | Not confirmed |
| Exact severity thresholds | Not disclosed |

Other rice sheath blight studies use standard evaluation systems and relative lesion height. However, the use of a particular system in this dataset cannot be assumed without explicit documentation.

## 5. Annotation Investigation

- Image-level severity annotation is reported in the Mendeley description.
- An annotation file is not identified in the public documentation.
- CSV, Excel, JSON or text annotation formats are not specified.
- Folder-based class labels are not verified.
- The mapping between individual image filenames and severity labels cannot currently be independently confirmed.
- Segmentation masks, bounding boxes and pixel-level annotations are not documented in the accessible description.

The NLM catalogue also lists no associated publication data and no supplementary data for this dataset.

## 6. Research Paper Investigation

The official Mendeley dataset description and available catalogue information were examined.

An accessible associated research paper containing the exact six class definitions could not be located.

A related research listing by the contributor was found, but its full text was not accessible for verification. Therefore, it has not been used as evidence for the six severity labels.

## 7. Unresolved Questions

1. What are the exact names or numerical codes of the six severity classes?
2. What is the definition of each severity class?
3. Which standard disease severity evaluation scale was used?
4. Are the classes based on relative lesion height, percentage of affected sheath, lesion area or a combination of visual criteria?
5. Are numerical severity scores available for each image?
6. Is there a separate CSV, Excel, JSON or text annotation file?
7. Are severity labels encoded in image filenames or folder names?
8. Can every original image be mapped to its corresponding severity label?
9. Is there a research paper or supplementary document containing the full scoring rubric?

## 8. Conclusion

**Verification Status: Partially Verified**

The Rice Sheath Blight dataset was investigated using the official Mendeley dataset record and the downloaded archive's README documentation.

### Verified Findings
- Dataset reports 1,609 original images.
- Six severity classes (Stage-1 to Stage-6) are present.
- Severity stage descriptions were verified from the archive README.
- Image counts for all six severity folders were reconciled, totaling 1,609 images.
- The dataset README describes severity assessment based on lesion progression, lesion height, colour intensity, lesion density, and spatial spread.
- The archive-level folder organization and class grouping were verified.

### Remaining Limitations
- The exact named reference or standard numerical severity scale remains unconfirmed.
- Additional numeric severity thresholds beyond the README's stage descriptions have not been established.
- Individual image-to-label mapping has not been independently verified beyond the class-folder organization.
- A separate annotation file and its format have not been confirmed.
- Images were not extracted or visually inspected.

The standard 0–9 rice sheath blight severity scale must not be assumed to apply to this dataset.

**Final status:** Dataset structure, stage descriptions, and counts are verified at the documentation/archive level. Severity-scale clarification and individual annotation mapping remain unresolved. The dataset remains a candidate pending suitability review.

## 9. Sources

1. Official Mendeley Data record: https://data.mendeley.com/datasets/489spnkhp5/1
2. NLM Dataset Catalogue: https://datasetcatalog.nlm.nih.gov/dataset?q=0001394886
3. Related contributor research listing: https://www.researchgate.net/publication/403426363_Context-Aware_Explanation_Drift_Detection_CA-EDD_For_Plant_Disease_Severity_Estimation
4. Example of separate rice sheath blight severity assessment research: https://pmc.ncbi.nlm.nih.gov/articles/PMC10642295/

## Follow-up Verification — 19 November 2026

### Additional Official-Source Review

The official Mendeley Data record was reviewed again, followed by archive-level README verification to investigate severity classes, class definitions, image counts, and annotation details.

The dataset README inside the downloaded archive provided additional information that was not available in the initial dataset description.

### Verified Severity Stage Definitions

| Class | Verified description |
|---|---|
| Stage-1 | Healthy (Mild symptoms) |
| Stage-2 | Initial infection; small lesions restricted to lower sheath |
| Stage-3 | Progressive spread; lesions covering less than 25% of plant height |
| Stage-4 | Moderate severity; lesions reaching 25–50% plant height |
| Stage-5 | High severity; lesions reaching 50–75% plant height |
| Stage-6 | Extreme severity; lesions reaching the flag leaf or more than 75% plant height |

### Verified Image Counts

| Severity Class | Image Count |
|---|---:|
| Stage-1 | 157 |
| Stage-2 | 326 |
| Stage-3 | 410 |
| Stage-4 | 355 |
| Stage-5 | 263 |
| Stage-6 | 98 |
| **Total** | **1,609** |

The six folder counts reconcile exactly with the reported total of 1,609 images.

### Annotation and Severity Assessment Information

The README describes severity assessment using:

- Vertical lesion progression relative to plant height.
- Chromatic intensity, ranging from water-soaked green symptoms to necrotic grayish-white or brown areas.
- Lesion density, spatial spread, and coalescence of necrotic patches on the sheath.

### Remaining Unresolved Information

- The exact reference or name of the standard severity evaluation scale.
- Additional numerical boundaries or scoring thresholds beyond the stage definitions documented in the README.
- Independent confirmation of image-to-label mapping beyond the class-folder organization.
- Whether a separate annotation file exists and, if so, its format and location.
- Visual quality and characteristics of the images, as image files were not extracted or inspected.

The standard 0–9 rice sheath blight severity scale must not be assumed to apply to this dataset.

### Updated Verification Status

The severity stage descriptions, folder organization, and image counts are verified from the downloaded archive documentation.

The severity scale reference, additional scoring boundaries, and individual image-to-label mapping remain unresolved. No author contact was made.

**Updated conclusion:** The dataset's severity documentation is better understood following archive README verification. However, the remaining annotation and scale uncertainties should be considered during dataset suitability assessment. The dataset remains a candidate rather than receiving final approval.

### Clarification Following Archive README Verification

The initial follow-up identified several severity-label details as unverified. Subsequent archive-level verification of the README (`reaadme.txt`) clarified the six severity-stage names and definitions.

**Now verified from the archive README:**
- Six severity classes, Stage-1 through Stage-6.
- Stage descriptions and severity progression criteria.
- Folder-based class organization.
- Image counts reconciled to 1,609.

**Still unresolved:**
- Exact reference or name of the standard numerical severity scale.
- Additional scoring thresholds beyond the README stage definitions.
- Independent verification of individual image-to-label mapping.
- Separate annotation file and its format/location.

The earlier statements about unavailable class definitions reflect the initial investigation stage and have been superseded by the archive README verification documented in Section 10.

No standard 0–9 scale has been assumed.

## 10. Archive-Level Verification - README, Severity Classes, and Image Counts

### 10.1 Archive Inspection

The dataset archive `SBSeverity.zip` was downloaded and inspected using archive-listing commands without extracting the image files.

The archive contains the following six severity folders:

- `Stage-1`
- `Stage-2`
- `Stage-3`
- `Stage-4`
- `Stage-5`
- `Stage-6`

The archive includes a text file named `reaadme.txt` (filename as present in the archive). Its contents provide the severity-stage definitions, annotation protocol, dataset information, and contributor contact details.

### 10.2 Severity Class Definitions Verified from the Archive README

| Folder | Severity definition |
|---|---|
| Stage-1 | Healthy (Mild symptoms) |
| Stage-2 | Initial infection; small lesions restricted to the lower sheath |
| Stage-3 | Progressive spread; lesions covering less than 25% of the plant height |
| Stage-4 | Moderate severity; lesions reaching 25-50% of the plant height |
| Stage-5 | High severity; lesions reaching 50-75% of the plant height |
| Stage-6 | Extreme severity; lesions reaching the flag leaf or more than 75% of plant height |

### 10.3 Annotation Protocol

According to the archive README, severity levels were assigned considering:

- **Vertical Progression:** Height of the highest lesion relative to the total plant height.
- **Chromatic Intensity:** Transition from water-soaked green to necrotic grayish-white/brown.
- **Lesion Density:** Spatial spread and coalescence of necrotic patches on the sheath.

### 10.4 Archive Image Count Verification

Image files were counted from the archive listing without extracting the images.

| Severity folder | Verified image count |
|---|---:|
| Stage-1 | 157 |
| Stage-2 | 326 |
| Stage-3 | 410 |
| Stage-4 | 355 |
| Stage-5 | 263 |
| Stage-6 | 98 |
| **Total** | **1,609** |

The total archive image count matches the README-reported count of 1,609 images.

**Count reconciliation:**

- README-reported total: 1,609
- Archive inventory total: 1,609
- Difference: 0

### 10.5 Dataset Metadata Observed in the README

- Image formats reported: JPG / PNG
- Resolution reported: 3024 x 4032
- Total images reported: 1,609

### 10.6 Contributor Contact Information Found

The archive README provides the following contact information:

- **Name:** Sonu Varghese K
- **Institution:** Sahrdaya College of Engineering and Technology, Thrissur, Kerala
- **Email:** sonuvk13@gmail.com

This is a contact route identified from the dataset's own README. No email contact attempt has been made as part of this investigation.

### 10.7 Remaining Verification Limitations

Although the archive README provides six severity-stage descriptions and the image files are organized into six corresponding folders, the following items remain unverified:

- A separate annotation file (CSV, Excel, or other metadata file) has not been confirmed.
- The exact reference or name of the standard numerical severity evaluation scale has not been verified.
- Additional numeric scoring thresholds beyond the README stage descriptions have not been established.
- Individual image-to-label mapping has not been independently verified beyond the folder-based organization.
- The image files themselves were not extracted, opened, or visually inspected.

**Updated status:** Six severity-stage descriptions verified from the archive README; folder structure verified; archive image counts reconciled to 1,609; contributor contact identified. Remaining annotation and scoring limitations are documented.