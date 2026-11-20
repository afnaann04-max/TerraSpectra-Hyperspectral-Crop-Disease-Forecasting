# CCMT Tomato Dataset — Source & Archive Verification Report

**Project:** TerraSpectra – Hyperspectral Crop Disease Forecasting  
**Assigned responsibility:** Member 3 – RGB Dataset Investigation  
**Investigation date:** 18–20 November 2026  
**Dataset:** CCMT – Dataset for Crop Pest and Disease Detection  
**Crop investigated:** Tomato  
**Status:** Public source verification and partial archive-level verification completed

---

## 1. Dataset Identification

- **Dataset name:** Dataset for Crop Pest and Disease Detection (CCMT)
- **Official source:** Mendeley Data
- **DOI:** `10.17632/bwh3zbpkpv.1`
- **Dataset URL:** https://data.mendeley.com/datasets/bwh3zbpkpv/1
- **Publication:** CCMT: Dataset for Crop Pest and Disease Detection
- **Publication DOI:** https://doi.org/10.1016/j.dib.2023.109306
- **Publication platform:** Data in Brief
- **Publication year:** 2023

The dataset contains images from four crops: cashew, cassava, maize and tomato. This investigation focuses only on the tomato subset.

---

## 2. Source and Availability

The dataset is publicly listed on Mendeley Data.

The publication and dataset record provide information about the dataset and its availability.

- **Access status:** Publicly listed dataset
- **Archive inspection status:** Archive contents inspected using PowerShell
- **Archive-level verification:** Partially completed

The tomato dataset archive was inspected to verify its folder structure, class folders, train/test image counts and class distribution.

Some file-level checks were also performed, including train/test filename matching and SHA256 comparison.

---

## 3. Dataset Licence

The Mendeley Data record lists the dataset licence as **Creative Commons Attribution 4.0 International (CC BY 4.0)**.

Licence reference: https://creativecommons.org/licenses/by/4.0/

The licence permits sharing and adaptation subject to its conditions, including appropriate attribution and indicating whether changes were made.

The dataset licence should be followed when reusing or adapting the data. The publication licence and dataset licence should not be treated as interchangeable.

---

## 4. Reported Image Counts vs Archive-Verified Counts

The dataset description and publication report the following tomato image counts:

| Dataset portion | Source-reported count |
|---|---:|
| Tomato raw images | 5,435 |
| Tomato augmented images | 27,178 |

The archive was subsequently inspected and image files were counted in the tomato train and test folders.

### Archive-verified counts

| Dataset portion | Verified image count |
|---|---:|
| Train set | 21,723 |
| Test set | 5,435 |
| **Total inspected** | **27,158** |

The archive-level total is **27,158 images**, which differs from the publication's reported augmented tomato count of **27,178**.

**Discrepancy: 20 images.**

This discrepancy has been recorded and requires clarification or further investigation. The source-reported count and archive-verified count are retained separately.

---

## 5. Tomato Disease Classes

The dataset contains five tomato classes:

1. Healthy
2. Leaf blight
3. Leaf curl
4. Septoria leaf spot
5. Verticillium wilt

### 5.1 Archive-verified class distribution

| Class | Train set | Test set | Total |
|---|---:|---:|---:|
| Healthy | 2,000 | 500 | 2,500 |
| Leaf blight | 5,200 | 1,309 | 6,509 |
| Leaf curl | 2,050 | 532 | 2,582 |
| Septoria leaf spot | 9,373 | 2,330 | 11,703 |
| Verticillium wilt | 3,100 | 764 | 3,864 |
| **Total** | **21,723** | **5,435** | **27,158** |

These counts were obtained by inspecting the actual archive folders using PowerShell.

### 5.2 Class distribution observations

- **Septoria leaf spot** is the largest class.
- **Healthy** is the smallest class.
- The dataset has an unequal class distribution.
- The class distribution should be considered during future dataset evaluation.

The counts above represent archive-inspected files, not the earlier publication-reported raw image counts.

---

## 6. Train/Test Split Verification

The archive contains separate folders for:

- `train_set`
- `test_set`

### Verified split counts

| Split | Number of images |
|---|---:|
| Train | 21,723 |
| Test | 5,435 |
| Total | 27,158 |

The archive therefore contains a predefined train/test split.

### 6.1 Train/test class comparison

A filename-based matching investigation was conducted to compare train/test files and their class folders.

The matching results showed the following class-pair groupings:

| Train class | Test class | Count |
|---|---|---:|
| Septoria leaf spot | Septoria leaf spot | 1,755 |
| Leaf blight | Leaf blight | 982 |
| Verticillium wilt | Verticillium wilt | 573 |
| Leaf curl | Leaf curl | 397 |
| Healthy | Healthy | 377 |
| Septoria leaf spot | Leaf blight | 1 |

One cross-class pairing was detected:

- **Train class:** Septoria leaf spot
- **Test class:** Leaf blight
- **Count:** 1

The corresponding train and test files were checked using SHA256 hashes. The inspected files had different hashes, indicating that they are not identical files.

This result should be treated as a detected filename-based pairing anomaly. The full train/test relationship and potential data leakage have not yet been comprehensively verified.

---

## 7. Image Format and Annotation

The publication reports JPEG images organised according to crop and disease class.

The described labelling process involved plant virologists and pathologists, followed by expert review and consensus.

The source information supports image-level class labels.

The reviewed information does not establish that the tomato subset contains:

- Bounding-box annotations
- Pixel-level segmentation masks
- A separate segmentation annotation file

The exact annotation-file format and image-to-label mapping have not been comprehensively verified.

---

## 8. Image Acquisition Conditions

The publication reports the following acquisition information:

| Field | Reported information |
|---|---|
| Collection location | Farms in Ghana |
| Collection period | October–December 2022 |
| Capture period | Daytime |
| Camera | Canon EOS Rebel T7 DSLR |
| Lens | EF-A 18–55 mm |
| Image format | JPEG |
| Image dimensions | Variable |
| Annotation period | December 2022–January 2023 |
| Annotation contributors | Plant virologists and pathologists |

The publication describes images captured under different backgrounds and conditions, including white, dark, illuminated and real backgrounds.

The University of Energy and Natural Resources in Sunyani, Ghana, is identified as a data-source institution.

Exact GPS coordinates, image-level capture dates and camera settings for every image have not been verified.

---

## 9. Archive Folder Structure and Inventory

The archive inspection confirmed the presence of separate tomato training and testing folders, with images organised into disease-class directories.

The inspected class folders include:

- `healthy`
- `leaf blight`
- `leaf curl`
- `septoria leaf spot`
- `verticillium wilt`

### Verified archive inventory

| Folder | Image count |
|---|---:|
| `train_set` | 21,723 |
| `test_set` | 5,435 |
| **Total** | **27,158** |

The folder-level class counts were independently inspected.

Remaining inventory checks include:

- Complete file inventory
- All image dimensions
- Image integrity across every file
- Comprehensive duplicate-image detection
- Full image-to-label verification
- Augmented/original image identification

---

## 10. Dataset Relevance to TerraSpectra

The CCMT tomato subset may be useful as an RGB image-classification candidate because it contains images grouped into five tomato health/disease categories.

However, the dataset is **not yet approved for modelling**.

Before selection, the following need to be evaluated:

- Actual number of usable images
- Verified class distribution
- Availability and consistency of image-level labels
- Duplicate or near-duplicate images
- Differences between original and augmented images
- Potential data leakage between train and test
- Image acquisition conditions and dataset suitability
- Licence and attribution requirements

The dataset must remain separate from the NWRD Wheat Rust and Rice Sheath Blight datasets during investigation.

---

## 11. Verified, Reported and Unresolved Information

### A. Verified from public source records

- Dataset record is available on Mendeley Data.
- Dataset DOI is `10.17632/bwh3zbpkpv.1`.
- The dataset covers four crops, including tomato.
- The Mendeley record lists CC BY 4.0.

### B. Reported by the publication or dataset description

- 5,435 raw tomato images.
- 27,178 augmented tomato images.
- Five tomato classes.
- Class-wise raw image counts.
- JPEG image format.
- Canon EOS Rebel T7 camera and EF-A 18–55 mm lens.
- Collection in Ghana during October–December 2022.
- Expert image-labelling and review process.

These details are source-reported and must be distinguished from archive-verified findings.

### C. Verified from archive inspection

- Train set contains **21,723** images.
- Test set contains **5,435** images.
- Archive total is **27,158** images.
- Five tomato class folders were inspected.
- Train/test class counts were inspected.
- A filename-based train/test matching check was performed.
- One cross-class pairing was detected in the matching output.
- SHA256 comparison was performed for the inspected mismatched pair.

### D. Unresolved

- Explanation for the 20-image difference between the source-reported augmented count and the inspected archive count.
- Comprehensive train/test image pairing.
- Potential augmented-image leakage between train and test.
- Exact annotation-file format.
- Complete image-to-label mapping.
- Image dimensions for every image.
- Duplicate and near-duplicate image status.
- Full image integrity verification.
- Exact metadata availability for individual images.

---

## 12. Restrictions and Investigation Notes

- Archive contents were inspected.
- No original files were modified or deleted.
- No preprocessing was performed.
- No additional augmentation was performed.
- No model training was performed.
- No dataset merging was performed.
- The dataset has not been approved for modelling.
- Source-reported figures and archive-verified counts are kept separate.
- The detected class-pair mismatch should not be generalized to the entire dataset without further verification.

---

## 13. References

1. Mendeley Data – Dataset for Crop Pest and Disease Detection:  
   https://data.mendeley.com/datasets/bwh3zbpkpv/1

2. Dataset DOI:  
   https://doi.org/10.17632/bwh3zbpkpv.1

3. Research publication – Data in Brief:  
   https://doi.org/10.1016/j.dib.2023.109306

4. Creative Commons Attribution 4.0 International:  
   https://creativecommons.org/licenses/by/4.0/

---

**Investigation update:** 20 November 2026  
**Prepared by:** Member 3 – RGB Dataset Investigation  
**Final status:** Public source verification and partial archive-level verification completed; further integrity and leakage checks pending.

## 14. Additional Archive Integrity and Train/Test Leakage Verification (20 November 2026)

Further read-only archive verification was performed using PowerShell and SHA256 hashing directly on files inside the ZIP archive. No files were extracted or modified.

### 14.1 Raw Tomato Archive Count

The raw Tomato folder was independently counted by class.

| Class | Raw images |
|---|---:|
| Healthy | 470 |
| Leaf blight | 1,301 |
| Leaf curl | 518 |
| Septoria leaf spot | 2,743 |
| Verticulium wilt | 773 |
| **Total** | **5,805** |

The inspected raw Tomato folder contains 5,805 image files, which is 370 more than the source-reported raw count of 5,435.

### 14.2 Exact Raw-to-Augmented Image Matches

SHA256 hashes were calculated for raw Tomato files and augmented Tomato train/test files inside the ZIP archive.

- **Exact raw-to-augmented matches: 5,627**

This confirms exact binary matches between files in the raw Tomato folder and files in the augmented dataset. This result does not independently establish the original-image lineage of every augmented file.

### 14.3 Exact Train/Test Overlap Verification

SHA256 comparison was performed between the augmented Tomato train and test folders.

- Train images: 21,723
- Test images: 5,435
- Exact Train–Test matching test files: **4,084**

The matching test files were grouped by class:

| Test class | Exact Train–Test matching files |
|---|---:|
| Healthy | 377 |
| Leaf blight | 982 |
| Leaf curl | 397 |
| Septoria leaf spot | 1,755 |
| Verticulium wilt | 573 |
| **Total** | **4,084** |

### 14.4 Proportion of Test Files with Exact Train Matches

Of the 5,435 test files, 4,084 were found to have an exact SHA256 match in the training set.

- Exact overlap: 4,084 / 5,435
- Percentage: **75.1%**
- Test files without an exact Train match: **1,351 (24.9%)**

This indicates substantial exact-file overlap between the predefined train and test folders.

### 14.5 Interpretation and Limitations

The exact hash comparison confirms that identical file contents exist across the train and test folders. This is evidence of train/test contamination at the exact-file level and raises a serious concern about the independence of the evaluation split.

However, this investigation does not yet establish:

- The number of unique original photographs represented by these matches.
- Whether non-identical augmented variants of the same original image also cross the train/test boundary.
- The extent to which model performance metrics would be affected.
- Whether all exact matches represent the same underlying capture or photograph lineage beyond identical file content.

The results are limited to exact binary file matching using SHA256. Similar-image or transformed-image matching has not been performed.

### 14.6 Verification Method

- Archive inspected directly using PowerShell/.NET ZIP access.
- File contents streamed for SHA256 calculation.
- No archive extraction performed.
- No image preprocessing performed.
- No augmentation performed.
- No model training performed.
- No original dataset files modified or deleted.

These findings are archive-verified and should be distinguished from publication-reported statistics.