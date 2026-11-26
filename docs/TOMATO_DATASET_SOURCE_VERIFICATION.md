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

The dataset description and publication report the following Tomato image counts:

| Dataset portion | Source-reported count |
|---|---:|
| Tomato raw images | 5,435 |
| Tomato augmented images | 27,178 |

The archive was subsequently inspected and image files were counted in the Tomato folders.

### Archive-verified counts

| Dataset portion | Verified image count |
|---|---:|
| Train set | 21,723 |
| Test set | 5,445 |
| **Total inspected** | **27,168** |

The archive-level total was initially reported as 27,158 images. Subsequent follow-up verification corrected the augmented Tomato archive total to **27,168 images**, which differs from the publication-reported count of 27,178 by **10 images**.

The count discrepancy was retained for documentation. The source-reported figure and archive-verified figure are kept separate.

**Updated verified archive total: 27,168 images.**

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
| Septoria leaf spot | 9,373 | 2,340 | 11,713 |
| Verticillium wilt | 3,100 | 764 | 3,864 |
| **Total** | **21,723** | **5,445** | **27,168** |

These counts reflect the corrected follow-up verification for Leaf Curl and Septoria Leaf Spot. The total augmented Tomato archive count is 27,168 images.

The class counts represent archive-inspected files. The remaining 10-image difference from the source-reported augmented Tomato total of 27,178 remains unresolved.

### 5.2 Class distribution observations

- **Septoria leaf spot** is the largest class.
- **Healthy** is the smallest class.
- The dataset has an unequal class distribution.
- The class distribution should be considered during future dataset evaluation.

The counts above are reconciled from the updated class-level counts recorded during follow-up verification. The updated test-set and total counts have not yet been independently re-counted from the archive in this step.

---

## 6. Train/Test Split Verification

The archive contains separate folders for:

- `train_set`
- `test_set`

### Verified split counts

| Split | Number of images |
|---|---:|
| Train | 21,723 |
| Test | 5,445 |
| Total | 27,168 |

The archive contains a predefined train/test split. The updated class-level counts reconcile to 21,723 training images and 5,445 testing images, totaling 27,168 images.

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
| `test_set` | 5,445 |
| **Total** | **27,168** |

The updated class-level counts reconcile to the corrected archive total of 27,168 images.

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
- The previously recorded test-set count was **5,435** images; the updated class-level count reconciles to **5,445** images, pending independent archive recount.
- The previously recorded archive total was **27,158** images; the updated class-level total reconciles to **27,168** images, pending independent archive recount.
- Five tomato class folders were inspected during the earlier archive verification.
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
**Prepared by:** Member 3 - RGB Dataset Investigation
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
- Previously recorded test images: 5,435
- Updated class-count-reconciled test images: 5,445 (independent archive recount pending)
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

Using the updated class-count-reconciled test total of 5,445 files (independent archive recount pending), 4,084 files were previously recorded as having an exact SHA256 match in the training set.

- Exact overlap: 4,084 / 5,445
- Percentage: **75.0%**
- Test files without an exact Train match: **1,361 (25.0%)**

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

### 14.7 Exact Raw-to-Augmented Matches by Split and Class

A further SHA256 comparison was conducted between the raw Tomato folder and the augmented train/test folders. Files were streamed directly from the ZIP archive; no extraction or modification was performed.

| Class | Raw-to-Train exact matches | Raw-to-Test exact matches |
|---|---:|---:|
| Healthy | 376 | 32 |
| Leaf blight | 1,029 | 323 |
| Leaf curl | 403 | 51 |
| Septoria leaf spot | 1,837 | 918 |
| Verticulium wilt | 619 | 39 |
| **Total** | **4,264** | **1,363** |

The total raw-to-augmented exact matches were 5,627, consisting of 4,264 train matches and 1,363 test matches.

These counts identify exact file-content matches between raw images and the augmented split files. They do not establish the complete lineage of non-identical transformed or augmented images.

The raw-to-train and raw-to-test match counts are separate from the train/test exact-overlap count of 4,084. The overlap investigation and raw-to-augmented investigation measure different file relationships.

Further original-image lineage verification remains unresolved.

### 14.8 Independent CRC32 Archive Verification (22 November 2026)

An independent read-only verification was performed using Python's built-in ZIP metadata support. CRC32 checksums were compared for the Raw Tomato, augmented Train and augmented Test folders. The archive was not extracted, and no image files were modified.

#### Archive file counts

| Dataset portion | Image files |
|---|---:|
| Raw Tomato | 5,805 |
| Augmented Train | 21,723 |
| Augmented Test | 5,445 |
| Total Augmented | 27,168 |

#### Unique CRC32 counts

| Dataset portion | Unique CRC32 values |
|---|---:|
| Raw | 5,351 |
| Train | 21,721 |
| Test | 5,445 |

#### CRC overlap results

| Comparison | Unique matching CRC32 values |
|---|---:|
| Raw and Train | 4,263 |
| Raw and Test | 1,363 |
| Train and Test | 4,084 |
| Raw, Train and Test simultaneously | 1,241 |

The comparison also counted 4,264 Raw-to-Train matching file entries, associated with 4,263 unique matching CRC values. Raw-to-Test matching file entries totalled 1,363.

The Train/Test comparison found 4,084 unique CRC32 values present in both splits. The sample archive paths inspected showed that matching-content files may have different filenames across Train and Test.

#### Interpretation

These results provide additional evidence of substantial file-content overlap between the predefined Train and Test folders. The finding is a serious split-integrity concern and may affect the independence of evaluation.

CRC32 is a checksum and is not cryptographic proof of file identity. These results should be described as CRC-based matches, not as a new cryptographic verification. The earlier SHA256 results documented in this report remain a separate historical verification.

The CRC comparison does not establish the complete lineage of non-identical transformed or augmented images. It does not determine the impact on model metrics, and visual or transformed-image similarity analysis has not been performed.

#### Verification limitations and restrictions

- ZIP metadata was read without extracting image files.
- No preprocessing, augmentation, visualization or model training was performed.
- No dataset files were changed.
- CRC32 was used for this independent comparison.
- The unique checksum counts are not the same as matching file-entry counts.
- Transformed or near-duplicate image lineage across Train and Test remains unresolved.
- The dataset remains unapproved for modelling.

## 14.9 Published Count Discrepancy — Follow-up Verification (22 November 2026)

### Verified Archive Counts
The current verified archive contains:
- Raw Tomato images: 5,805
- Augmented Train images: 21,723
- Augmented Test images: 5,445
- Total augmented images: 27,168

### Published Counts
The publication reports:
- Raw Tomato images: 5,435
- Augmented images: 27,178

### Discrepancy
- Raw dataset count difference: 370 images
- Augmented dataset count difference: 10 images

The current verified augmented archive count (27,168) supersedes the earlier count of 27,158 recorded during preliminary verification.

### Finding
The available publication information does not explain the 10-image discrepancy between the reported augmented count (27,178) and the verified archive count (27,168).

This discrepancy is classified as **unresolved**. We cannot conclude that files are missing, corrupted, or intentionally excluded without additional source evidence.

### Status
- Archive counts: Verified
- Published counts: Source-reported
- Explanation for count discrepancy: Unresolved
- Dataset completeness relative to publication: Not established

## 14.10 Filename Lineage and External Research Follow-up (22 November 2026)

### Filename Pattern Verification

Sample filenames were inspected from the Raw, Train, and Test archive folders using ZIP metadata only.

**Raw examples:**
- `healthy100_.jpg`
- `healthy101_.jpg`

**Train examples:**
- `0tomato_train_healthy.JPG`
- `1001tomato_train_healthy.JPG`

**Test examples:**
- `104tomato_valid_healthy.JPG`
- `101tomato_valid_healthy.JPG`

The Raw filenames use class-based numbering, while Train and Test filenames use numeric prefixes with split and class identifiers.

### Filename Lineage Finding

The inspected filename samples do not provide an explicit mapping between an original Raw image and its augmented Train/Test variants.

Filename patterns alone cannot establish augmentation parent-child relationships.

### External Research Follow-up

External research reports concerns regarding train/test leakage in the CCMT augmented dataset, including identical images and augmented variants across splits.

This is external supporting evidence and is not a substitute for independent verification of every augmentation lineage relationship in our archive.

### Split Methodology Limitation

The available dataset documentation does not establish that source images were separated before augmentation in a way that guarantees all variants of an original image remain within one partition.

Therefore, source-image-independent splitting cannot be confirmed.

### Independent Count Corroboration

A separate research source reports the Tomato augmented split counts:
- Train: 21,723
- Test: 5,445
- Total: 27,168

These counts corroborate our verified archive total of 27,168. The original publication's reported total of 27,178 remains discrepant by 10 images.

### Remaining Limitations

- Complete original-to-augmented mapping: Unverified
- Non-identical augmentation lineage across splits: Unverified
- Near-duplicate detection: Not performed
- Source-image-independent split: Not established
- Dataset leakage risk: Supported by exact overlap findings and external reports
- Leakage-free status: Cannot be claimed

### Verification Restrictions

No images were extracted, opened, visually inspected, preprocessed, or used for training during this follow-up.

### Conclusion

The archive shows significant exact-content overlap between Raw, Train, and Test, while filename metadata does not reveal complete original-image lineage.

The dataset's augmentation lineage and split independence remain unresolved. The evidence indicates a serious data leakage concern, and the dataset should not be assumed to provide an independent Train/Test evaluation.

## 14.11 Raw-to-Augmented SHA-256 Reverification and Cross-Class Label Conflict (26 November 2026)

### Verification Method

A fresh SHA-256 verification was performed using the current archive:

`Dataset for Crop Pest and Disease Detection.zip`

The verification script streamed image contents directly from ZIP entries. No images were extracted, modified, or deleted.

Script:
`scripts/verify_ccmt_raw_to_augmented_lineage.py`

Machine-readable outputs:
- `reports/ccmt_raw_to_augmented/ccmt_raw_to_augmented_summary.json`
- `reports/ccmt_raw_to_augmented/ccmt_raw_to_augmented_exact_matches.csv`

### Verified Archive Inventory

| Dataset portion | Image files |
|---|---:|
| Raw Tomato | 5,805 |
| Augmented Train | 21,723 |
| Augmented Test | 5,445 |
| Total augmented | 27,168 |

### Reconciled Raw-to-Augmented Exact-Match Results

The fresh verification identified the following measurements:

| Measurement | Verified count |
|---|---:|
| Raw file entries with at least one exact match | 4,771 |
| Unique matched Raw SHA-256 values | 4,385 |
| Distinct augmented Train files matched | 4,264 |
| Distinct augmented Test files matched | 1,363 |
| **Distinct augmented files matched** | **5,627** |
| Raw-to-Augmented matching file pairs | 6,202 |

The distinct augmented-file count reproduces the historical result of 5,627.

The 6,202 matching file pairs are higher because multiple Raw file entries can contain identical content and therefore match the same augmented file. Pair counts must not be interpreted as distinct augmented-image counts.

### Class-wise Exact Matches

| Class | Raw-to-Train matches | Raw-to-Test matches |
|---|---:|---:|
| Healthy | 376 | 32 |
| Leaf blight | 1,029 | 323 |
| Leaf curl | 403 | 51 |
| Septoria leaf spot | 1,837 | 918 |
| Verticulium wilt | 619 | 39 |
| **Total** | **4,264** | **1,363** |

These fresh class-wise counts reproduce the historical Section 14.7 counts.

### Verified Cross-Class Duplicate and Label Conflict

One SHA-256 content value was found in two Raw class folders and two augmented Train class folders.

SHA-256:

`4e69cc3e3073bd2336e75447aab0a14e8476bb6916c14d9d1557ead234708c6e`

The four exact-content matching pairs were:

| Raw class | Augmented Train class | Label agreement |
|---|---|---|
| Leaf blight | Leaf blight | Yes |
| Leaf blight | Septoria leaf spot | No |
| Septoria leaf spot | Leaf blight | No |
| Septoria leaf spot | Septoria leaf spot | Yes |

The two Raw files are:
- `leaf blight/leaf blight1315_.jpg`
- `septoria leaf spot/septoria leaf spot47_.jpg`

The two augmented Train files are:
- `leaf blight/4449tomato_train_leaf blight.JPG`
- `septoria leaf spot/8911tomato_train_septoria leaf spot.JPG`

All four records have identical file content according to SHA-256.

### Interpretation

- The same image content is stored under both Leaf blight and Septoria leaf spot in the Raw dataset.
- The same content is also stored under both labels in augmented Train.
- This is a verified cross-class duplicate and label inconsistency.
- The correct disease label cannot be established from hashes or folder names alone.
- This finding raises a label-reliability concern for five-class image classification.
- The finding should not be generalized to other images without further evidence.

### Limitations and Status

- Exact Raw-to-Augmented content matches: Reverified.
- Historical distinct augmented-file count of 5,627: Reconciled.
- Raw-to-Augmented pair count of 6,202: Verified.
- Cross-class duplicate and conflicting label assignment: Verified.
- Correct disease label for the conflicting image: Unresolved.
- Complete transformed-image lineage: Unresolved.
- Biological sample identity: Not established.
- Dataset approval for modelling: Not granted by this verification.

The SHA-256 results establish identical file content, not biological sample identity or complete augmentation lineage.

No raw images were extracted or modified. No preprocessing, feature extraction, or model training was performed.

**Investigation update:** 26 November 2026
**Prepared by:** Member 3 - RGB Dataset Investigation

## 14.12 Biological Sample Identifier Investigation (26 November 2026)

### Objective
Determine whether CCMT Tomato filenames or archive metadata provide plant, leaf, specimen or biological sample identifiers that could support group-based data partitioning.

### Verification performed
1. Searched the CCMT dataset archive for potential metadata and identifier files using terms including README, metadata, label, annotation, sample, plant, specimen and mapping. No matching files were found within the CCMT dataset folder.
2. Searched the complete ZIP archive for documentation filenames containing README, metadata, annotation, description, dataset_info, license or licence. No matching files were found.
3. Inspected Raw, Train and Test image filename patterns.
4. Parsed numeric suffixes from Raw filenames matching the observed pattern, for example healthy100_.jpg.

### Verified findings
- Raw images: 5,805.
- Augmented Train images: 21,723.
- Augmented Test images: 5,445.
- Raw filenames matching the numeric-suffix pattern: 5,425.
- Numeric suffixes reused across multiple disease classes: 1,271.
- Examples such as 100, 101 and 102 occur across all five disease classes.
- Raw and augmented images use different filename conventions.

### Interpretation
The numeric suffixes are not globally unique across disease classes and cannot be treated as verified biological sample identifiers. No separate biological metadata or documentation explaining the numbering convention was identified in the inspected ZIP archive.

### Limitations and unresolved questions
- The absence of matching documentation filenames does not prove that biological identifiers are unavailable from every possible external source.
- The numeric suffixes may represent class-specific image numbering, file sequence numbers or another convention; their intended meaning is unverified.
- No plant, leaf or specimen-level grouping has been established.
- Biological independence between Train and Test therefore cannot be claimed.
- A leakage-safe biological group split cannot currently be demonstrated from the available archive evidence.

### Recommendation
Do not use filename numbers as plant or specimen group IDs. Treat biological sample identity as unresolved. Any future evaluation should use verified biological grouping information if it becomes available; otherwise, clearly state this limitation and avoid claiming biological independence.

### Processing restrictions
This investigation used archive filenames and metadata searches only. Original images and masks were not modified, and no preprocessing, augmentation, feature extraction or model training was performed.

**Prepared by:** Member 3 - RGB Dataset Investigation

## 14.13 CCMT Train-Test Leakage and Split Feasibility Assessment (26 November 2026)

### Objective
Assess whether the supplied CCMT Train-Test partition can support independent evaluation and whether a new leakage-reduced split can be established.

### Verified exact-content overlap
The existing SHA-256 Train-Test verification identified:
- Train entries: 21,723.
- Test entries: 5,445.
- Test entries with exact SHA-256 matches in Train: 4,084.
- Test entries without exact Train content matches: 1,361.

Approximately 75% of supplied Test entries have identical file content in Train. Therefore, the supplied Test partition must not be treated as an independent test set.

### Near-duplicate investigation
A 64-bit difference-hash comparison was performed on the 1,361 Test entries without exact SHA-256 Train matches.
- 361 Test entries had at least one Train candidate at a difference-hash distance of 8 or less.
- Six selected candidate pairs were visually compared.
- Five of the six selected pairs appeared to show the same photograph.
- The six pairs were selected from close perceptual-hash candidates and are not a representative random sample.
- Perceptual-hash similarity is candidate evidence, not proof of duplicate identity.

These findings provide additional evidence of possible Train-Test image leakage beyond exact byte matches. They do not establish that all 361 candidates are duplicates.

### Label consistency limitation
The raw-to-augmented SHA-256 investigation identified two class-label disagreement file pairs involving one unique image content represented in two Raw classes and two Train classes.
The correct disease label remains unresolved. This conflict must be investigated before using the affected image content in a classification experiment.

### Biological grouping limitation
The archive investigation did not establish plant, leaf or specimen identifiers. Filename numbers are reused across disease classes and cannot be treated as biological group IDs.
Consequently, biological independence between partitions cannot be demonstrated.

### Split feasibility recommendation
1. Do not use the supplied Test partition as an independent evaluation set.
2. A new image-content leakage-reduced split may be feasible after grouping exact duplicate content across all partitions.
3. Near-duplicate candidates require further review and grouping before partition assignment.
4. Conflicting-label image content must be resolved using reliable ground truth or excluded from a defensible classification experiment.
5. Biological group independence cannot be guaranteed without verified plant, leaf or specimen identifiers.
6. Any future split must clearly state whether it controls exact duplicates, reviewed near-duplicates and biological grouping separately.

### Overall assessment
The current CCMT archive does not establish a scientifically defensible independent Train-Test evaluation split. A provisional image-content leakage-reduced split may be possible, but it must not be described as biologically independent or fully leakage-safe.

The five-class image-level classification suitability remains conditional on resolving label reliability concerns and clearly acknowledging the absence of verified biological sample identities.

### Processing restrictions
No original images were modified. This assessment did not involve preprocessing, augmentation, feature engineering or model training.

**Prepared by:** Member 3 - RGB Dataset Investigation
