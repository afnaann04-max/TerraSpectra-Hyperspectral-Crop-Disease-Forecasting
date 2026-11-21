
# TerraSpectra – Tomato RGB Dataset Assessment

## 1. Dataset Overview

**Dataset Name:** Dataset for Crop Pest and Disease Detection  
**Source:** Mendeley Data  
**Published:** 27 April 2023  
**Version:** 1  
**DOI:** 10.17632/bwh3zbpkpv.1  
**License:** CC BY 4.0

This dataset contains RGB images collected from local farms in Ghana for crop pest and disease detection.

## 2. Dataset Composition

The dataset covers four crops:

- Cashew
- Cassava
- Maize
- Tomato

According to the dataset description:

| Dataset Type | Number of Images |
|---|---:|
| Raw images | 24,881 |
| Augmented images | 102,976 |
| Raw tomato images | 5,435 |
| Augmented tomato images | 27,178 |

The complete dataset download size is approximately 7.86 GB.

## 3. Tomato Disease Classes

The Tomato dataset contains five classes:

1. Healthy
2. Leaf blight
3. Leaf curl
4. Septoria leaf spot
5. Verticillium wilt

These classes can support a multi-class tomato disease classification task.

## 4. Folder Structure

The Mendeley repository displays two main folders:

- Raw Data
- CCMT Dataset-Augmented

The augmented Tomato folder contains:

- train_set
- test_set

The training and testing folders contain class-wise subfolders.

## 5. Image Characteristics

- Image format: JPG
- Image dimensions vary.
- Reported dimensions include 400 × 400, 487 × 1080, 1080 × 518, 3024 × 4032 and 4032 × 3024 pixels.
- Images were captured under different backgrounds and illumination conditions.

## 6. Relevance to TerraSpectra

This dataset is a potential source for the Tomato RGB image classification pipeline.

It provides healthy and disease-affected tomato images across five classes.

It can be evaluated for training and testing a tomato disease classification model.

## 7. Limitations and Checks Required

Before using this dataset, the following checks are required:

- Download and inspect the selected Tomato images.
- Verify the number of images in each class.
- Check image quality and corrupted files.
- Identify duplicate or near-duplicate images.
- Inspect the existing training and testing split.
- Check for possible data leakage between training and testing sets.
- Confirm whether the raw or augmented dataset will be used.

The dataset description alone does not confirm that the existing split is free from data leakage.

## 8. Current Status

**Status: Archive-Level Verification Completed — Suitability Review Pending**

The initial dataset assessment and follow-up archive verification have been completed for the selected Tomato classes.

Verified findings include raw and augmented image counts for Leaf Curl and Septoria Leaf Spot, corrected augmented counts, filename pattern differences, and exact-image overlap between training and testing sets.

The verification identified **4,084 exact-image matches between the augmented training and testing sets**, indicating that the existing split has significant data leakage concerns.

The augmented Tomato archive count was verified as 27,168, while the published dataset description reports 27,178. The remaining 10-image discrepancy is unresolved.

Original-to-augmented image lineage has not been established. Images have not been extracted or visually inspected.

**Current decision:** The dataset remains a candidate for further evaluation, but the existing train/test split should not be used as a reliable leakage-free evaluation split without further investigation.

## 9. Dataset Reference

Mensah Kwabena, P., et al. (2023). Dataset for Crop Pest and Disease Detection. Mendeley Data, Version 1.

https://doi.org/10.17632/bwh3zbpkpv.1

## 10. Follow-Up Verification – 21 November 2026

### 10.1 Corrected Augmented Image Count

A recheck of the archive confirmed the following counts:

| Class | Raw Images | Augmented Train | Augmented Test | Augmented Total |
|---|---:|---:|---:|---:|
| Leaf Curl | 518 | 2,050 | 532 | 2,582 |
| Septoria Leaf Spot | 2,743 | 9,373 | 2,340 | 11,713 |

The previously reported Septoria augmented count of 11,703 was incorrect. The verified count is 11,713.

The corrected total augmented Tomato archive count is 27,168, compared with the published count of 27,178. The remaining difference is 10 images.

### 10.2 Original and Augmented Filename Investigation

Original Leaf Curl filenames were observed in the Raw Data folder, with examples such as:

- leaf curl100_.jpg
- leaf curl101_.jpg
- leaf curl102_.jpg

Augmented training filenames were observed in the CCMT Dataset-Augmented folder, with examples such as:

- 0tomato_train_leaf curl.JPG
- 1000tomato_train_leaf curl.JPG
- 1001tomato_train_leaf curl.JPG

The observed filename patterns differ. The filenames do not provide a clear direct mapping between original images and their augmented versions.

Filename-based augmentation lineage therefore remains unverified. No image extraction or visual inspection was performed during this check.

### 10.3 Data Leakage Finding

The previously conducted exact-image comparison identified 4,084 exact image matches between the augmented training and testing sets.

This indicates substantial exact-image overlap between the two splits. The existing train/test split should not be considered leakage-free.

### 10.4 Updated Verification Status

- [x] Raw Leaf Curl count verified
- [x] Augmented Leaf Curl train/test counts verified
- [x] Raw Septoria Leaf Spot count verified
- [x] Augmented Septoria Leaf Spot train/test counts rechecked
- [x] Corrected total augmented Tomato count
- [x] Original and augmented filename patterns inspected
- [x] Filename-based lineage limitation documented
- [x] Previously identified train/test exact-image overlap retained
- [ ] Remaining 10-image publication/archive discrepancy resolved
- [ ] Original-to-augmented image lineage established

### 10.5 Scope and Limitations

This follow-up was conducted through archive filename listing and count verification. Images were not extracted or visually inspected. No preprocessing, feature engineering, or model training was performed.

