# TerraSpectra – RGB Dataset Suitability Assessment

**Project:** TerraSpectra – Hyperspectral Crop Disease Forecasting
**Team Member:** Member 3 – RGB Dataset Investigation
**Assessment Date:** 27 November 2026
**Branch:** Afnan

---

## 1. Executive Summary

This report consolidates the investigation of three RGB crop disease datasets:

1. CCMT – Tomato
2. Rice Sheath Blight Severity Dataset
3. NWRD – Wheat Rust

The datasets represent different crops, disease categories, annotation formats and computer-vision tasks. They must therefore be assessed independently rather than treated as one combined dataset.

The investigation identified substantial Train-Test overlap in CCMT, duplicate-content label conflicts in Rice Sheath Blight, and image-mask quality concerns in NWRD.

**Overall conclusion:** All three datasets remain research candidates with different suitability limitations. None should be considered fully validated for independent model evaluation at this stage.

## 2. Dataset Overview

| Attribute | CCMT Tomato | Rice Sheath Blight | NWRD Wheat Rust |
|---|---|---|---|
| Crop | Tomato | Rice | Wheat |
| Disease | Multiple tomato diseases | Rice sheath blight | Wheat stripe/yellow rust |
| Image count | 27,168 augmented images | 1,609 images | 100 RGB images |
| Labels | Five classes | Six severity stages | Binary segmentation masks |
| Annotation type | Folder-based classification | Folder-based severity classification | Pixel-level masks |
| Intended task | Image classification | Severity classification | Semantic segmentation |
| Main concern | Train-Test content overlap | Duplicate severity-label conflicts | Duplicate RGB with different masks |

Note: CCMT also contains 5,805 raw images. Its 27,168 augmented images comprise 21,723 Train and 5,445 Test entries.

## 3. CCMT Tomato Dataset Assessment

### 3.1 Inventory

| Dataset portion | Image count |
|---|---:|
| Raw Tomato | 5,805 |
| Augmented Train | 21,723 |
| Augmented Test | 5,445 |
| Total augmented | 27,168 |


**Verified class-wise image distribution**

| Disease class | Raw images | Train images | Test images |
|---|---:|---:|---:|
| Healthy | 470 | 2,000 | 500 |
| Leaf blight | 1,301 | 5,200 | 1,309 |
| Leaf curl | 518 | 2,050 | 532 |
| Septoria leaf spot | 2,743 | 9,373 | 2,340 |
| Verticillium wilt | 773 | 3,100 | 764 |
| **Total** | **5,805** | **21,723** | **5,445** |

These counts were verified directly from the downloaded ZIP archive. The raw and augmented collections have different class distributions.

The five classes are:

- Healthy
- Leaf blight
- Leaf curl
- Septoria leaf spot
- Verticillium wilt

### 3.1.1 Class Distribution and Imbalance Analysis

The raw CCMT Tomato dataset contains five classes with an uneven distribution.

| Disease class | Raw images | Percentage |
|---|---:|---:|
| Healthy | 470 | 8.1% |
| Leaf blight | 1,301 | 22.4% |
| Leaf curl | 518 | 8.9% |
| Septoria leaf spot | 2,743 | 47.2% |
| Verticillium wilt | 773 | 13.3% |
| **Total** | **5,805** | **100%** |

Septoria leaf spot is the dominant class, accounting for approximately 47.2% of the raw dataset. Healthy is the least represented class, accounting for approximately 8.1%.

The largest class contains approximately 5.84 times as many images as the smallest class. This indicates substantial class imbalance.

**Implications for future model evaluation:**

- Overall accuracy alone may not adequately describe performance across all five classes.
- Per-class precision, recall and F1-score should be examined.
- A confusion matrix should be used to identify class-specific misclassification patterns.
- Class balancing strategies may be investigated during future model development.

No model training or performance evaluation was performed as part of this dataset investigation.

### 3.1.2 Raw vs Augmented Class Distribution Analysis

The raw and augmented Tomato datasets were compared to examine changes in class proportions and image counts.

| Disease class | Raw images | Raw % | Augmented images | Augmented % | Augmentation factor |
|---|---:|---:|---:|---:|---:|
| Healthy | 470 | 8.10% | 2,500 | 9.20% | 5.32x |
| Leaf blight | 1,301 | 22.41% | 6,509 | 23.96% | 5.00x |
| Leaf curl | 518 | 8.92% | 2,582 | 9.50% | 4.98x |
| Septoria leaf spot | 2,743 | 47.25% | 11,713 | 43.11% | 4.27x |
| Verticillium wilt | 773 | 13.32% | 3,864 | 14.22% | 5.00x |
| **Total** | **5,805** | **100%** | **27,168** | **100%** | **4.68x overall** |

**Findings:**

- The augmented dataset has a different class distribution from the raw dataset.
- Healthy has the highest count-based augmentation factor (5.32x).
- Septoria leaf spot has the lowest factor (4.27x).
- Septoria's share decreases from 47.25% in the raw dataset to 43.11% in the augmented dataset.
- Class imbalance remains in the augmented collection.

These factors compare image counts only. They do not establish unique original-image lineage for every augmented entry. The earlier exact-content investigation identified only partial raw-to-augmented lineage.

No new augmentation or preprocessing was performed as part of this analysis.

### 3.1.3 Train-Test Class Distribution Analysis

The augmented Tomato dataset contains 21,723 training images and 5,445 testing images, representing an overall split of approximately 80:20.

The class distribution within each partition was calculated to examine whether the five classes are proportionally represented.

| Disease class | Train images | Train % | Test images | Test % |
|---|---:|---:|---:|---:|
| Healthy | 2,000 | 9.21% | 500 | 9.18% |
| Leaf blight | 5,200 | 23.94% | 1,309 | 24.04% |
| Leaf curl | 2,050 | 9.44% | 532 | 9.77% |
| Septoria leaf spot | 9,373 | 43.15% | 2,340 | 42.98% |
| Verticillium wilt | 3,100 | 14.27% | 764 | 14.03% |
| **Total** | **21,723** | **100%** | **5,445** | **100%** |

**Findings:**

- The overall Train-Test ratio is approximately 80:20.
- The class proportions are similar across the two partitions.
- The largest difference in class proportion is for Leaf curl, at approximately 0.33 percentage points.
- The supplied split appears approximately stratified by class.

**Important limitation:**

Similar class proportions do not establish independent Train-Test partitions. The earlier SHA-256 investigation identified 4,084 unique shared content hashes between Train and Test, with 4,085 matching file pairs.

Therefore, the supplied Test partition remains unsuitable for independent model evaluation despite its similar class distribution.

No model training or performance evaluation was performed as part of this analysis.

### 3.2 Original-to-Augmented Lineage

SHA-256 comparison between the raw Tomato images and augmented Train-Test images identified:

- 5,805 raw image entries.
- 4,771 raw file entries with at least one exact-content match in the augmented dataset.
- 1,034 raw file entries without an exact-content match.
- 4,385 unique raw SHA-256 values with an augmented match.
- 6,202 Raw-to-Augmented exact file pairs.
- 4,651 Train exact-match pairs.
- 1,551 Test exact-match pairs.
- 6,200 class-label agreement pairs.
- Two class-label disagreement pairs.

The two disagreement pairs share one SHA-256 content hash:

`4e69cc3e3073bd2336e75447aab0a14e8476bb6916c14d9d1557ead234708c6e`

The conflicting content is associated with the following raw and augmented entries:

| Dataset portion | Class | Filename |
|---|---|---|
| Raw | Leaf blight | `leaf blight1315_.jpg` |
| Raw | Septoria leaf spot | `septoria leaf spot47_.jpg` |
| Train | Septoria leaf spot | `8911tomato_train_septoria leaf spot.JPG` |
| Train | Leaf blight | `4449tomato_train_leaf blight.JPG` |

The raw images and augmented Train images contain identical content within this hash group, but the folder labels disagree. The correct disease label has not been independently established.

A separate cross-class exact-content group was identified in the Train-Test hash inventory:

`4de9b764d1e45150519e26a523a2d3158ef532fd267a9403e74b2fa7f5353acd`

| Split | Class | Filename |
|---|---|---|
| Train | Leaf blight | `1011tomato_train_leaf blight.JPG` |
| Train | Septoria leaf spot | `1835tomato_train_septoria leaf spot.JPG` |
| Test | Leaf blight | `314tomato_valid_leaf blight.JPG` |

These three entries have identical file contents despite being assigned to different classes. No exact raw-image content match was identified for this second group. This does not rule out a transformed raw source.

The exact-content investigation establishes partial lineage only. Non-matching files may contain transformed versions of raw images, but their original-image relationships have not been established.

The publication reports 5,435 raw Tomato images and 27,178 augmented Tomato images. The current archive contains 5,805 raw images and 27,168 augmented images. The differences of 370 raw images and 10 augmented images remain unresolved.


### 3.3 Train-Test Leakage Investigation

Exact SHA-256 comparison between the supplied Train and Test partitions found:

- 4,084 unique shared content hashes.
- 4,084 Test entries with at least one exact Train content match.
- 4,085 matching Train-Test file pairs.
- 1,361 Test entries without an exact Train content match.

Approximately 75.0% of Test entries have exact file-content matches in Train.

SHA-256 and CRC32 comparisons produced consistent overlap counts. SHA-256 was used as the stronger evidence of exact binary content equality.

A perceptual-hash investigation was conducted on the 1,361 Test entries without exact Train matches.

| Perceptual comparison | Test entries |
|---|---:|
| Nearest dHash distance <= 2 | 48 |
| Nearest dHash distance <= 4 | 85 |
| Nearest dHash distance <= 6 | 151 |
| Nearest dHash distance <= 8 | 361 |

Eight non-exact Test entries had a nearest dHash distance of zero. Perceptual hash similarity does not establish identical image content.

Six candidate Train-Test pairs were selected for read-only visual inspection:

- Five pairs appeared to contain the same photograph.
- One pair appeared to contain different photographs.

These six pairs were selected from similarity candidates and are not a representative sample of the entire dataset. Their results must not be used to estimate the overall duplicate rate.

The combined exact-content and visual findings demonstrate substantial overlap between the supplied Train and Test partitions.

The supplied Test partition must not be treated as an independent evaluation set for a model trained on the supplied Train partition.

The remaining perceptual candidates require further verification. The investigation also does not establish biological sample independence because reliable plant, leaf or specimen identifiers have not been verified.

### 3.4 Biological Grouping

No reliable plant, leaf or specimen identifiers were established from the available archive metadata.

Filename numbers are not globally unique biological sample identifiers.

Therefore, image-level duplicate grouping alone cannot establish biological independence.


### 3.5 Suitability Recommendation

CCMT provides a large Tomato image collection with five classification classes. However, several issues affect its reliability:

- Approximately 75.0% of supplied Test entries have exact file-content matches in Train.
- Five of six visually inspected perceptual-similarity candidates appeared to contain the same photograph.
- Cross-class exact-content label conflicts were identified.
- Original-to-augmented lineage is only partially established.
- Publication and archive image counts remain inconsistent.
- Biological sample independence has not been established.

The supplied Train-Test split is unsuitable for independent model evaluation.

A new leakage-aware partition should be investigated only after reviewing cross-class label conflicts, verifying original-image relationships and grouping known repeated content. Biological independence must not be claimed without reliable sample-level evidence.

**Assessment:** Conditional candidate for exploratory Tomato classification. Do not use the supplied Test partition as an independent evaluation set.

Supporting documentation:

- `docs/TOMATO_DATASET_SOURCE_VERIFICATION.md`
- `docs/CCMT_TRAIN_TEST_HASH_OVERLAP_VERIFICATION.md`

## 4. Rice Sheath Blight Dataset Assessment

### 4.1 Dataset Identification

**Dataset:** Colour-Mix Augmentation Dataset for Rice Sheath Blight Severity Estimation
**Source:** Mendeley Data
**DOI:** 10.17632/489spnkhp5.1

The archive contains 1,609 JPG images organized into six severity-stage folders.

### 4.2 Severity Classes and Counts

| Stage | Documented description | Images |
|---|---|---:|
| Stage-1 | Healthy (Mild symptoms) | 157 |
| Stage-2 | Initial infection; small lesions restricted to lower sheath | 326 |
| Stage-3 | Lesions covering less than 25% of plant height | 410 |
| Stage-4 | Lesions reaching 25–50% of plant height | 355 |
| Stage-5 | Lesions reaching 50–75% of plant height | 263 |
| Stage-6 | Lesions reaching the flag leaf or more than 75% of plant height | 98 |
| **Total** | | **1,609** |

The archive README describes severity assessment using vertical lesion progression, chromatic intensity, lesion density and spatial spread.

The exact reference or name of the standard numerical severity scale remains unresolved. The standard 0–9 scale must not be assumed to apply.

### 4.3 Duplicate-Content Investigation

SHA-256 comparison identified:

- 1,609 images checked.
- 1,602 unique image hashes.
- Seven exact duplicate-content groups.
- Five same-stage duplicate groups.
- Two cross-stage duplicate groups.

The two cross-stage conflicts are:

1. Stage-2 `IMG_11@18FEB25-KTK.JPG` and Stage-3 `IMG_167@18FEB25-KTK.JPG`.
2. Stage-2 `IMG_166@18FEB25-KTK.JPG` and Stage-3 `IMG_10@18FEB25-KTK.JPG`.

Visual comparison indicated that the images in each pair appeared identical. The correct severity label could not be determined from the available evidence.

### 4.4 Biological Grouping and Partitioning

Filename patterns contain image-number and date/location-like components.

The investigation identified 292 candidate image-number/location groups. A total of 187 groups appeared across multiple dates, and 184 appeared across multiple severity stages.

These are candidate filename-based groups only. They do not prove that images belong to the same plant, leaf or biological specimen.

The archive does not provide separate Train-Test partitions. Therefore, no supplied partition leakage assessment is possible.

### 4.5 Suitability Recommendation

The dataset has six documented severity stages and a reconciled image inventory.

However, cross-stage duplicate-content conflicts, unresolved biological grouping and incomplete numerical severity-scale information limit its reliability for independent severity classification.

Before partitioning, exact duplicates should be grouped, cross-stage label conflicts investigated and candidate biological groups reviewed.

**Assessment:** Conditional candidate for exploratory six-stage rice sheath blight severity classification.

Supporting documentation:

- `docs/RICE_SHEATH_BLIGHT_SEVERITY_LABEL_VERIFICATION.md`

## 5. NWRD Wheat Rust Dataset Assessment

### 5.1 Dataset Identification and Inventory

The NWRD archive contains 100 RGB images and 100 PNG masks.

| Partition | RGB images | Masks |
|---|---:|---:|
| Train | 90 | 90 |
| Test | 10 | 10 |
| **Total** | **100** | **100** |

A filename-stem comparison confirmed that all 100 RGB images have corresponding masks:
- Train: 90 matched pairs; no missing images or masks.
- Test: 10 matched pairs; no missing images or masks.

This confirms filename pairing, not annotation correctness.

### 5.2 Image and Mask Dimensions

99 of the 100 image-mask pairs have matching dimensions.

One mismatch was identified:

| File | RGB dimensions | Mask dimensions |
|---|---|---|
| `train/images/101.jpg` | 3612 × 3456 | 3593 × 3435 |

The mask is 19 pixels narrower and 21 pixels shorter than the RGB image. This needs resolution before using this pair for segmentation.

### 5.3 Mask Format and Pixel Values

All 100 masks were inspected directly from the ZIP archive.

Verified findings:
- All masks use grayscale mode (`L`).
- All masks contain only pixel values 0 and 255.
- All masks contain non-zero white foreground pixels.
- White-pixel coverage ranges from 0.03125% to 2.98851%.
- No zero-white masks were found.

The numerical values were verified, but the exact semantic mapping of 0 and 255 to rust and background was not independently established from the archive.

### 5.4 Exact Duplicate Investigation

SHA-256 comparison identified:

| Check | Result |
|---|---:|
| RGB images inspected | 100 |
| Unique RGB image contents | 99 |
| Exact duplicate RGB groups | 1 |
| Masks inspected | 100 |
| Unique mask contents | 100 |
| Exact duplicate mask groups | 0 |
| Exact duplicate groups across Train-Test | 0 |

The duplicate RGB group consists of:
- `train/images/15.jpg`
- `train/images/32.jpg`

These two RGB files are byte-identical. Their corresponding masks are different.

### 5.5 Duplicate RGB with Different Masks: Visual Review

Both images have dimensions of 6016 × 4000.

| Measurement | Mask 15 | Mask 32 |
|---|---:|---:|
| Dimensions | 6016 × 4000 | 6016 × 4000 |
| White pixels | 25,371 | 40,832 |
| White coverage | 0.105431% | 0.169681% |

A visual comparison showed that both masks mark the same main visible region on a central leaf. Mask 32 also appears to include an additional small region near the lower-right edge.

This is a potential annotation inconsistency because identical RGB content has different mask annotations.

The visual inspection does not establish whether the additional region is a valid rust annotation or an annotation error. Expert confirmation is required.

### 5.6 Train-Test Duplicate Investigation

The SHA-256 comparison found no exact duplicate RGB images or masks across Train and Test.

This is limited to exact byte-level duplicates. It does not rule out visually similar images, shared plants or specimens, or other forms of biological leakage.

### 5.7 Visual Validation Limitations

The duplicate RGB and mask pair was visually inspected using the original archive files without modifying them.

A representative visual alignment review of all image-mask pairs has not been completed. Therefore, the investigation does not establish that every mask is correctly aligned or accurately annotated.

### 5.8 Licence and Documentation

The downloaded archive contains image and mask files but no accompanying README, licence file or annotation guide.

Previously reviewed public-source information includes:
- The GitHub documentation describes binary wheat rust/non-rust segmentation.
- The GitHub MIT licence must not automatically be applied to dataset image and mask assets.
- The NLM Dataset Catalog lists CC BY 4.0.
- Previously reviewed Zenodo rights information displays a copyright statement.

These rights statements have not been conclusively reconciled. Dataset image and mask reuse permission remains unresolved.

No author contact was initiated.

### 5.9 Suitability Recommendation

NWRD provides 100 filename-matched RGB-mask pairs for exploratory wheat rust segmentation.

However, the following limitations remain:
- One RGB-mask dimension mismatch.
- One exact duplicate RGB group with different mask annotations.
- Unresolved semantic mapping of mask pixel values.
- No representative visual validation of all image-mask pairs.
- Biological independence has not been established.
- Dataset image and mask reuse permissions remain unresolved.

**Assessment:** Conditional candidate for exploratory wheat rust segmentation. Further annotation, dimension, biological grouping and licence verification is required before final dataset approval or independent model evaluation.

Supporting documentation:

- `docs/NWRD_FOLLOW_UP_VERIFICATION.md`

## 6. Comparative Risk Assessment

| Risk area | CCMT | Rice Sheath Blight | NWRD |
|---|---|---|---|
| Exact duplicate content | 4,084 shared Train-Test contents; 4,085 matching file pairs | Seven duplicate groups | One duplicate RGB group |
| Cross-label conflict | Raw-to-augmented disagreements and an additional cross-class Train-Test group | Two cross-stage duplicate conflicts | Different masks for identical RGB |
| Near-duplicate risk | 361 Test candidates at dHash distance <= 8; six visually inspected | Not fully assessed | Not fully assessed |
| Biological independence | Unresolved | Unresolved | Unresolved |
| Annotation consistency | Cross-class label conflicts identified | Cross-stage severity conflicts identified | Duplicate-mask inconsistency |
| Partition reliability | Supplied split unsuitable for independent evaluation | No supplied split | No exact cross-partition duplicates detected |
| Licence certainty | Requires source-specific confirmation | Requires source-specific confirmation | Conflicting evidence; unresolved |

## 7. Overall Recommendations

### CCMT Tomato

Do not use the supplied Train-Test split for independent evaluation. Investigate a new content-grouped split and resolve label conflicts before relying on the five-class labels.

### Rice Sheath Blight

Retain as a candidate for severity classification. Investigate cross-stage duplicate labels and possible biological grouping before designing a partition.

### NWRD Wheat Rust

Retain as a candidate for segmentation. Review duplicate masks, the Image 101 dimension mismatch, mask-value semantics and reuse permissions.

### Cross-Dataset Recommendation

The three datasets must remain separate because they represent different crops, diseases and prediction tasks.

No dataset should be declared fully validated or biologically independent based only on the current archive-level investigation.

## 8. Investigation Scope and Restrictions

The investigation focused on source verification, archive inventory, filename analysis, exact content hashing, selected perceptual-hash comparisons, label consistency and selected visual inspection.

The following restrictions were maintained:

- Original images and masks were not overwritten or modified.
- Temporary in-memory operations were used only for inspection.
- No model training was performed.
- No feature extraction or feature engineering was performed.
- No new augmentation or preprocessing pipeline was developed.
- No author contact was initiated.
- No unsupported biological-independence claims were made.

## 9. Final Conclusion

The investigation identified three RGB dataset candidates with different strengths and limitations.

CCMT offers a large Tomato image collection but has substantial exact Train-Test content overlap, visually observed repeated photographs, cross-class label conflicts and incomplete original-to-augmented lineage. Its supplied Test partition is unsuitable for independent model evaluation.

Rice Sheath Blight offers six documented severity stages, but duplicate images with conflicting stage assignments and unresolved biological grouping affect its reliability.

NWRD offers paired RGB images and binary masks for wheat rust segmentation, but has a duplicate-image annotation inconsistency, a dimension mismatch and unresolved asset reuse permissions.

**Final recommendation:** Retain all three datasets as conditional research candidates. Further verification is required before approving any of them for final independent model evaluation.

**Prepared by:** Member 3 – RGB Dataset Investigation
**Date:** 27 November 2026

## 10. Latest Follow-up Verification - 27 November 2026

### 10.1 CCMT Tomato - Supplementary Perceptual Hash Analysis

A supplementary difference hash (dHash) analysis was performed using a separate Python implementation with Pillow.

This analysis is reported separately from the earlier dHash investigation because the implementations differ. Its results must not be combined with or substituted for the earlier results.

The supplementary analysis processed:
- 21,723 Train images.
- 1,361 Test images without exact Train content matches.
- 550 candidate Train-Test pairs with dHash distance <= 8.
- 312 same-class candidate pairs.
- 238 cross-class candidate pairs.
- 13 cross-class candidate pairs with distance <= 3.

Additional findings:
- 105 unique Test images occurred in the cross-class candidate set.
- 217 unique Train images occurred in the cross-class candidate set.
- Eight Test images had a nearest dHash distance of zero.
- A contact sheet was generated for the 13 closest cross-class candidates.

These candidates indicate potential visual similarity and possible annotation or leakage concerns. They do not independently establish that every candidate is the same original photograph.

The earlier six-pair visual inspection remains a separate, similarity-focused review. The supplementary contact sheet does not establish a verified duplicate rate.

**Updated recommendation:** The supplied CCMT Test partition remains unsuitable for independent evaluation. Cross-class candidates and unresolved labels require further review before a new content-grouped split can be considered reliable.

### 10.2 Rice Sheath Blight - Visual Confirmation of Cross-Stage Duplicates

Two cross-stage exact duplicate groups were visually inspected.

The following image pairs appeared visually identical:

1. Stage-2 `IMG_11@18FEB25-KTK.JPG` and Stage-3 `IMG_167@18FEB25-KTK.JPG`.
2. Stage-2 `IMG_166@18FEB25-KTK.JPG` and Stage-3 `IMG_10@18FEB25-KTK.JPG`.

The images have conflicting severity-stage folder labels despite identical visual content.

The correct severity label for either pair has not been established. No labels were changed.

The archive does not provide verified plant, leaf or specimen identifiers. The correct biological experimental unit therefore remains unresolved.

**Updated recommendation:** Keep exact duplicate images in the same future partition or exclude duplicate copies. Resolve cross-stage label conflicts before treating the six severity classes as fully reliable.

### 10.3 NWRD Wheat Rust - Complete Mask Pixel Audit

All 100 PNG masks were inspected directly from the original ZIP archive using Python, Pillow and NumPy.

| Finding | Result |
|---|---:|
| Total masks inspected | 100 |
| Unique pixel values | 0 and 255 |
| Masks with unexpected pixel values | 0 |
| Black pixels | 1,812,039,224 |
| White pixels | 10,464,923 |
| Total pixels | 1,822,504,147 |

Approximate pixel distribution:
- Black: 99.43%
- White: 0.57%

All masks use consistent binary pixel values. However, the semantic meaning of white and black has not been independently confirmed. Binary consistency does not prove annotation correctness or RGB-mask alignment.

### 10.4 NWRD Wheat Rust - Image and Mask Reuse Permission

The official Zenodo record, GitHub repository and associated research paper were reviewed.

The GitHub MIT licence applies to repository source code and does not automatically establish reuse permission for separately distributed image and mask assets.

The research paper's CC BY 4.0 licence also does not automatically establish that the dataset assets are covered by that licence.

The inspected Zenodo rights information displays a copyright notice without a clearly identified dataset-specific reuse licence.

**Conclusion:** Public access is established, but unrestricted reuse, modification and redistribution of the RGB images and masks remain unconfirmed. No author contact was made.

### 10.5 NWRD Wheat Rust - Leakage-Safe Split Feasibility

The archive contains:
- 90 Train RGB images and masks.
- 10 Test RGB images and masks.
- One exact duplicate RGB pair: `train/images/15.jpg` and `train/images/32.jpg`.
- No exact RGB duplicate detected across the existing Train-Test partitions.

The identified duplicate pair occurs entirely within Train.

However, verified plant, leaf, plot or specimen identifiers are unavailable. Near-duplicate and biological sample leakage have not been fully established.

**Conclusion:** The existing split has no detected exact RGB duplicate overlap between Train and Test. This does not establish biological independence. A fully leakage-safe biological evaluation cannot currently be guaranteed.

The known duplicate RGB pair should remain in the same partition or one copy should be excluded.

### 10.6 Updated Overall RGB Dataset Recommendation

| Dataset | Updated assessment |
|---|---|
| CCMT Tomato | Conditional candidate for exploratory five-class classification. Supplied Test split unsuitable for independent evaluation because of substantial exact content overlap and additional similarity and label concerns. |
| Rice Sheath Blight | Conditional candidate for exploratory six-stage severity classification. Cross-stage duplicate labels and biological grouping remain unresolved. |
| NWRD Wheat Rust | Conditional candidate for exploratory segmentation. Binary mask values are consistent, but annotation semantics, one dimension mismatch, duplicate RGB with different masks and asset reuse permissions remain unresolved. |

All three datasets must remain separate because they represent different crops and prediction tasks.

No dataset is currently established as fully validated for independent biological evaluation.

The investigation did not modify original images or masks, perform model training, or contact dataset authors.