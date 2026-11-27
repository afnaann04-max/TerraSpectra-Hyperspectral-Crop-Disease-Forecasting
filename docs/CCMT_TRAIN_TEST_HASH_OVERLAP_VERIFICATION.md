

# CCMT Train–Test Hash Overlap Verification



**Project:** TerraSpectra – Hyperspectral Crop Disease Forecasting

**Dataset:** CCMT Tomato – Augmented Dataset

**Verification date:** 25 November 2026

**Branch:** Afnan

**Status:** Read-only archive verification completed



---



## 1. Objective



The objective was to reproduce and clarify the previously reported exact-content overlap between the CCMT Tomato augmented training and testing datasets.



The verification was designed to establish:



- The exact number of Train and Test image files.

- The number of unique shared file contents.

- The number of matching Train and Test entries.

- The number of Train–Test matching file pairs.

- Whether SHA-256 and CRC32 comparisons produced consistent results.



The original ZIP archive was inspected directly. No images were extracted, modified, preprocessed, or used for model training.



## 2. Archive and Folder Structure



The inspected archive was:



`Dataset for Crop Pest and Disease Detection (1).zip`



The relevant folders were:



- `CCMT Dataset-Augmented/Tomato/train_set/`

- `CCMT Dataset-Augmented/Tomato/test_set/`



Both splits contain five class folders:



1. Healthy

2. Leaf blight

3. Leaf curl

4. Septoria leaf spot

5. Verticulium wilt



## 3. Verified Image Inventory



The archive was independently recounted on 25 November 2026 using PowerShell and exact CCMT Tomato folder-path filtering.



| Class | Train | Test | Total |

|---|---:|---:|---:|

| Healthy | 2,000 | 500 | 2,500 |

| Leaf blight | 5,200 | 1,309 | 6,509 |

| Leaf curl | 2,050 | 532 | 2,582 |

| Septoria leaf spot | 9,373 | 2,340 | 11,713 |

| Verticulium wilt | 3,100 | 764 | 3,864 |

| **Total** | **21,723** | **5,445** | **27,168** |



These counts agree with the corrected inventory in the existing dataset documentation.



## 4. Verification Methods



A reproducible Python script was created:



`scripts/verify_ccmt_train_test_hash_overlap.py`



The script uses Python standard-library modules.



### 4.1 SHA-256



- Each selected ZIP entry was opened as a read-only stream.

- File contents were processed in chunks.

- SHA-256 digests were calculated using `hashlib.sha256()`.

- Train and Test digest groups were compared.



SHA-256 provides strong evidence of exact binary file-content equality.



### 4.2 CRC32



- File contents were independently processed using `zlib.crc32()`.

- CRC32 values were calculated while streaming the same ZIP entries.

- Train and Test CRC32 groups were compared separately.



CRC32 is a checksum, not a cryptographic hash. It is useful as an independent consistency check but is not collision-resistant.



### 4.3 File Comparison Procedure



1. Open the ZIP archive without extracting its contents.

2. Select image entries only from the exact CCMT Tomato Train and Test folders.

3. Calculate SHA-256 and CRC32 for every selected image.

4. Group file entries by their calculated hash values.

5. Identify hash values present in both splits.

6. Count unique shared hash values, matching entries, and matching Train–Test file pairs separately.

7. Compare the SHA-256 and CRC32 results.



No image preprocessing, visual inspection, augmentation, or model training was performed.



## 5. Verification Results



### 5.1 SHA-256 Results



| Measurement | Count |

|---|---:|

| Unique shared SHA-256 values | 4,084 |

| Test entries with a Train match | 4,084 |

| Train entries with a Test match | 4,085 |

| Train–Test matching file pairs | 4,085 |

| Unmatched Test entries | 1,361 |



### 5.2 CRC32 Results



| Measurement | Count |

|---|---:|

| Unique shared CRC32 values | 4,084 |

| Test entries with a Train match | 4,084 |

| Train entries with a Test match | 4,085 |

| Train–Test matching file pairs | 4,085 |

| Unmatched Test entries | 1,361 |



### 5.3 Comparison of Both Methods



Both independently calculated methods produced the same counts for:



- Unique shared hash values.

- Matching Test entries.

- Matching Train entries.

- Train–Test matching file pairs.

- Unmatched Test entries.



This agreement supports the reproducibility of the observed overlap counts. SHA-256 remains the stronger evidence for exact binary content matching; CRC32 agreement does not eliminate the theoretical possibility of checksum collisions.



## 6. Clarification of the 4,084 and 4,085 Counts



The earlier figure of 4,084 requires a precise definition.



The new verification distinguishes three measurements:



| Measurement | Verified result |

|---|---:|

| Unique shared file contents | 4,084 |

| Test entries with at least one Train match | 4,084 |

| Train–Test matching file pairs | 4,085 |



The difference occurs because one shared content hash appears in two Train entries and one Test entry.



Therefore:



- 4,084 represents unique shared content hashes.

- 4,084 Test entries have a matching Train content hash.

- 4,085 Train–Test file pairs are formed when all matching entries are paired.



The 4,084 figure should not be described as the total number of matching file pairs.



## 7. Identified Repeated Content Group



One shared SHA-256 digest was found in two Train files and one Test file.



**SHA-256:**



`4de9b764d1e45150519e26a523a2d3158ef532fd267a9403e74b2fa7f5353acd`



| Split | Class | Filename |

|---|---|---|

| Train | Leaf blight | `1011tomato_train_leaf blight.JPG` |

| Train | Septoria leaf spot | `1835tomato_train_septoria leaf spot.JPG` |

| Test | Leaf blight | `314tomato_valid_leaf blight.JPG` |



All three entries have identical file contents according to the calculated SHA-256 digest.



The two Train entries are stored under different class labels. This is a cross-class label inconsistency that requires further investigation.



No visual inspection was performed, so this verification does not establish which class label is correct.



## 8. Overlap Percentage



Using the verified Test inventory:



- Matching Test entries: 4,084

- Total Test entries: 5,445



The proportion of Test entries with an exact Train content match is:



`4,084 / 5,445 × 100 = approximately 75.0%`



This is a file-content overlap measurement. It is not a model performance measurement.



## 9. Supporting Verification Outputs



The script generates the following files:



| File | Purpose |

|---|---|

| `scripts/verify_ccmt_train_test_hash_overlap.py` | Reproducible hash-comparison script |

| `reports/ccmt_hash_overlap/ccmt_hash_overlap_summary.json` | Summary of inventory, hash counts, and method comparison |

| `reports/ccmt_hash_overlap/ccmt_hash_file_inventory.csv` | Per-file split, class, size, SHA-256, and CRC32 inventory |

| `reports/ccmt_hash_overlap/ccmt_train_test_hash_matches.csv` | Matching Train–Test file pairs and their hashes |



These outputs preserve the evidence required to reproduce and review the comparison.



## 10. Limitations and Unresolved Questions



The verification establishes exact binary file-content matches only.



It does not establish:



1. Whether files with different contents are near-duplicates.

2. Whether images with different filenames originate from the same original photograph.

3. Whether augmented images can be traced to particular original images.

4. Whether different photographs represent the same plant, leaf, or biological sample.

5. Whether Train and Test contain biologically independent samples.

6. Whether all possible forms of data leakage have been identified.

7. Which label is correct for the identified cross-class repeated content group.



Filename similarity, exact file-content equality, augmentation lineage, and biological sample identity are separate concepts and must not be treated as interchangeable.



The existing Train–Test split should not be declared leakage-free based on this verification.



## 11. Relationship to Existing Dataset Counts



The current archive inventory is:



| Dataset portion | Verified count |

|---|---:|

| Raw Tomato | 5,805 |

| Augmented Train | 21,723 |

| Augmented Test | 5,445 |

| Total augmented | 27,168 |



The publication-reported counts remain:



- Raw Tomato: 5,435.

- Augmented Tomato: 27,178.



The differences of 370 raw images and 10 augmented images remain unresolved.



These publication discrepancies are separate from the Train–Test hash overlap investigation.



## 12. Reproduction



From the repository root, run:



```powershell

python scripts\\verify_ccmt_train_test_hash_overlap.py

```



The default archive path is:



`%USERPROFILE%\\Downloads\\Dataset for Crop Pest and Disease Detection (1).zip`



The script reads the ZIP directly and writes its outputs under:



`reports/ccmt_hash_overlap/`





## 13. Availability of Original Historical Script and Logs



The original standalone script and execution log used for the earlier historical 4,084-match comparison were not available in the reviewed repository files.



The earlier SHA-256 result was documented in the existing Tomato dataset investigation report. However, the original execution script and standalone raw output could not be located for direct inspection.



To provide reproducible evidence, a new verification script was created on 25 November 2026:



`scripts/verify_ccmt_train_test_hash_overlap.py`



This script independently recalculates SHA-256 and CRC32 values directly from the current ZIP archive and generates JSON and CSV evidence files.



The newly generated results reproduce the previously documented 4,084 unique shared content count and clarify that the matching Train–Test file-pair count is 4,085.



The new script and outputs are therefore reproducibility evidence for the current verification, not the original historical script or logs.



## 14. Consistency Review of Existing Documentation

The following documents were reviewed against the 25 November 2026 archive verification:

1. `docs/TOMATO_DATASET_ASSESSMENT.md`
2. `docs/TOMATO_DATASET_SOURCE_VERIFICATION.md`
3. `research/RGB/RGB_DATASET_READINESS_ASSESSMENT.md`

The corrected archive inventory is consistent across the latest verification records:

- Raw Tomato: 5,805
- Train: 21,723
- Test: 5,445
- Total augmented: 27,168

The 4,084 exact-content overlap figure is clarified as the number of unique shared contents and matching Test entries. The corresponding Train–Test file-pair count is 4,085.

Earlier preliminary counts and publication-reported counts are retained as historical or source-reported information. The discrepancies of 370 raw images and 10 augmented images remain unresolved.

No existing report was modified as part of this consistency review.



## 15. Verification Conclusion



The CCMT Tomato archive contains 21,723 Train images and 5,445 Test images.



The reproduced comparison identified:



- 4,084 unique shared file contents.

- 4,084 Test entries with a matching Train entry.

- 4,085 matching Train–Test file pairs.

- 1,361 Test entries without an exact Train content match.



SHA-256 and CRC32 produced identical comparison counts.



The existing split therefore contains substantial exact file-content overlap. The results are evidence of file-level overlap, not proof of biological sample identity or complete augmentation lineage.



**Verification status:** Completed

**Documentation status:** Prepared for review

**Git status:** Not committed or pushed

## 16. Train-Test Perceptual Similarity and Visual Verification

### 16.1 Perceptual Hash Method

A 64-bit Difference Hash (dHash) comparison was performed between the 21,723 Train images and 5,445 Test images.

The comparison was used to identify visually similar candidates beyond exact SHA-256 matches. Perceptual hash similarity does not establish that two files contain the same photograph.

### 16.2 Corrected Train-Test Results

The analysis excluded Test entries that already had exact SHA-256 matches in Train before counting non-exact perceptual candidates.

| Measurement | Result |
|---|---:|
| Total Test images | 5,445 |
| Exact SHA-256 Test matches in Train | 4,084 |
| Test images without exact Train matches | 1,361 |
| Non-exact Test images with dHash distance <= 8 | 361 |
| Nearest distance <= 2 | 48 |
| Nearest distance <= 4 | 85 |
| Nearest distance <= 6 | 151 |
| Nearest distance <= 8 | 361 |

Eight non-exact Test entries had a nearest dHash distance of zero. Identical perceptual hashes do not establish identical image content.

### 16.3 Manual Visual Verification

Six candidate Train-Test pairs were selected for read-only visual inspection.

| Test image | Train image | Observation |
|---|---|---|
| 11tomato_valid_leaf blight.JPG | 1855tomato_train_leaf blight.JPG | Same photograph observed |
| 126tomato_valid_leaf blight.JPG | 5300tomato_train_septoria leaf spot.JPG | Different photographs observed |
| 16tomato_valid_leaf blight.JPG | 1902tomato_train_leaf blight.JPG | Same photograph observed |
| 38tomato_valid_leaf blight.JPG | 1703tomato_train_leaf blight.JPG | Same photograph observed |
| 728tomato_valid_leaf blight.JPG | 759tomato_train_leaf blight.JPG | Same photograph observed |
| 493tomato_valid_leaf blight.JPG | 4319tomato_train_leaf blight.JPG | Same photograph observed |

Five of the six inspected pairs appeared to contain the same photograph despite different filenames and non-identical file contents.

This is direct visual evidence of repeated photographs across the supplied Train and Test partitions. The six pairs were selected from similarity candidates and are not a representative sample from which to estimate the dataset-wide duplication rate.

### 16.4 Raw Filename Inconsistency Investigation

Fourteen images in the raw Verticillium wilt folder had filenames beginning with the prefix "leaf blight" instead of the expected "verticulium wilt" prefix.

Exact SHA-256 comparison against the augmented Train and Test folders found:

- 12 exact-content matches in the augmented Verticillium wilt class.
- 11 matches in Train.
- 1 match in Test.
- 2 raw files without exact-content matches.

**Independent filename verification (27 November 2026):**

A separate read-only SHA-256 comparison was performed against the original CCMT ZIP archive. All 14 raw images with filenames beginning with `leaf blight` were identified. The comparison independently reproduced the result of 12 exact-content matches and 2 unmatched files.

The two unmatched raw filenames were:

- `leaf blight914_.jpg`
- `leaf blight918_.jpg`

This confirms the filenames and exact-content matching results reported above. It does not independently establish the biological disease labels of these images.

The two unmatched raw images were compared with their closest dHash candidates through read-only visual inspection. No obvious same-photograph match was observed among the inspected candidates.

The filename inconsistency is verified, but the actual disease labels of these images have not been independently established.

### 16.5 Interpretation and Limitations

The combined exact-hash and visual findings indicate substantial overlap between the supplied Train and Test partitions.

The supplied Test partition should not be treated as an independent evaluation set for a model trained on the supplied Train partition.

A new leakage-aware partition should be considered using verified original-image groups. However, biological independence cannot be guaranteed without plant, leaf or specimen identifiers.

The dHash results are candidate matches, not confirmed duplicates. Only six Train-Test candidate pairs were visually inspected. The remaining candidates require further verification before being classified as duplicates.

The investigation did not modify, preprocess or overwrite any original images.

### 16.6 Updated Recommendation

The supplied CCMT Train-Test split is unsuitable as an independent evaluation split based on the verified exact-content overlap and visually observed repeated photographs.

A new split should be designed after resolving original-image lineage and, where possible, biological sample grouping. If reliable grouping information is unavailable, the limitation must be documented rather than assuming biological independence.

**Verification status:** Exact-hash and initial visual investigation completed

**Remaining work:** Broader candidate verification, biological grouping investigation and complete original-to-augmented lineage assessment

**Documentation status:** Updated for review


## 17. Additional Cross-Class Label Conflict Investigation — 27 November 2026

### 17.1 Objective

An additional investigation was performed to identify exact-content duplicates assigned to different disease classes and determine whether the conflicting content could be traced to the raw Tomato dataset.

The investigation used the existing SHA-256 inventory and raw-to-augmented lineage CSV outputs. No original image content or labels were modified.

### 17.2 Conflicting Hash Group 1 — Raw and Augmented Train

**SHA-256:**

`4e69cc3e3073bd2336e75447aab0a14e8476bb6916c14d9d1557ead234708c6e`

The same binary image content appears in two raw files and two augmented Train files:

| Dataset portion | Class | Filename |
|---|---|---|
| Raw | Leaf blight | `leaf blight1315_.jpg` |
| Raw | Septoria leaf spot | `septoria leaf spot47_.jpg` |
| Train | Septoria leaf spot | `8911tomato_train_septoria leaf spot.JPG` |
| Train | Leaf blight | `4449tomato_train_leaf blight.JPG` |

All four entries have the same SHA-256 content hash according to the existing lineage and inventory reports.

This establishes an exact-content class-label conflict in both the raw and augmented data.

The correct disease label cannot be determined from hash equality alone. No conclusion is made about which class is biologically correct.

### 17.3 Conflicting Hash Group 2 — Train and Test

**SHA-256:**

`4de9b764d1e45150519e26a523a2d3158ef532fd267a9403e74b2fa7f5353acd`

The same binary image content appears in three augmented entries:

| Split | Class | Filename |
|---|---|---|
| Train | Leaf blight | `1011tomato_train_leaf blight.JPG` |
| Train | Septoria leaf spot | `1835tomato_train_septoria leaf spot.JPG` |
| Test | Leaf blight | `314tomato_valid_leaf blight.JPG` |

The three files have identical SHA-256 content.

The raw-to-augmented exact-match CSV contains no record for this hash. Therefore, its exact raw-image source has not been identified through the current exact-content comparison.

This group demonstrates both cross-class label inconsistency and exact-content overlap between Train and Test.

### 17.4 Consolidated Findings

Two distinct SHA-256 groups with conflicting class assignments have been identified:

| Hash group | Number of augmented entries | Classes | Raw exact match |
|---|---:|---|---|
| `4e69cc3e...` | 2 | Leaf blight, Septoria leaf spot | Identified |
| `4de9b764...` | 3 | Leaf blight, Septoria leaf spot | Not identified |

The first group is also present as two raw entries with conflicting class labels.

The second group contains an exact Train–Test duplicate.

These two groups are additional findings within the existing hash investigation. They must not be added again as extra unique shared hashes or matching file pairs without recalculating the relevant totals.

### 17.5 Limitations

- Exact SHA-256 equality establishes identical file content, not disease identity.
- The investigation does not establish which conflicting class label is correct.
- The absence of an exact raw-image match does not prove that no transformed raw source exists.
- Biological sample identity remains unknown.
- Dataset-author clarification and further visual investigation are needed.

No images were relabelled, deleted, or modified.

**Investigation date:** 27 November 2026
**Status:** Two conflicting-content groups identified; label correctness unresolved

## 18. Supplementary Train-Test dHash Candidate Investigation — 27 November 2026

### 18.1 Objective

A supplementary perceptual similarity investigation was performed to generate a detailed candidate-pair list for non-exact Train-Test image matches.

The existing SHA-256 inventory was reused. Test entries with exact SHA-256 matches in Train were excluded before perceptual comparison.

Images were read directly from the original ZIP archive. No original images were extracted, modified or overwritten.

### 18.2 dHash Implementation

A 64-bit Difference Hash (dHash) was calculated using Pillow:

- Images converted to grayscale.
- Images resized to 9 × 8 pixels using LANCZOS resampling.
- Adjacent horizontal pixel intensities compared.
- The resulting 64-bit hashes compared using Hamming distance.
- Candidate threshold: Hamming distance ≤ 8.

The original implementation used for the earlier Section 16 analysis was not preserved. Therefore, this supplementary implementation is documented separately. Its counts must not be treated as a direct reproduction or replacement of the earlier results.

### 18.3 Supplementary Results

| Measurement | Result |
|---|---:|
| Train images processed | 21,723 |
| Total Test images | 5,445 |
| Exact SHA-256 Test matches excluded | 4,084 |
| Non-exact Test images compared | 1,361 |
| Test images successfully compared | 1,361 |
| Candidate pairs with dHash distance ≤ 8 | 550 |
| Test images with nearest distance ≤ 2 | 45 |
| Test images with nearest distance ≤ 4 | 70 |
| Test images with nearest distance ≤ 6 | 118 |
| Test images with nearest distance ≤ 8 | 219 |
| Test images with nearest distance 0 | 8 |

The 550 candidate pairs involve 219 Test images with at least one Train match at distance ≤ 8. Pair counts and unique Test-image counts are different measurements.

### 18.4 Same-Class and Cross-Class Candidate Analysis

The 550 candidate pairs were divided according to their assigned class labels.

| Candidate type | Number of pairs |
|---|---:|
| Same-class pairs | 312 |
| Cross-class pairs | 238 |
| Total | 550 |

The 238 cross-class candidate pairs involve:

- 105 unique Test images.
- 217 unique Train images.

Thirteen cross-class pairs had a dHash distance ≤ 3.

These results identify potential cross-class similarity and possible label or partition concerns. They do not establish that the images are identical photographs or that either assigned label is incorrect.

### 18.5 Strong Cross-Class Candidate Pairs

The following 13 pairs had dHash distances of 1–3:

| Test image | Test class | Train image | Train class | Distance |
|---|---|---|---|---:|
| 550tomato_valid_verticulium wilt.JPG | Verticulium wilt | 1187tomato_train_leaf curl.JPG | Leaf curl | 1 |
| 736tomato_valid_verticulium wilt.JPG | Verticulium wilt | 2007tomato_train_leaf curl.JPG | Leaf curl | 1 |
| 736tomato_valid_verticulium wilt.JPG | Verticulium wilt | 1184tomato_train_leaf curl.JPG | Leaf curl | 1 |
| 71tomato_valid_verticulium wilt.JPG | Verticulium wilt | 7175tomato_train_septoria leaf spot.JPG | Septoria leaf spot | 1 |
| 736tomato_valid_verticulium wilt.JPG | Verticulium wilt | 1180tomato_train_leaf curl.JPG | Leaf curl | 2 |
| 38tomato_valid_leaf blight.JPG | Leaf blight | 683tomato_train_septoria leaf spot.JPG | Septoria leaf spot | 2 |
| 523tomato_valid_leaf curl.JPG | Leaf curl | 3037tomato_train_verticulium wilt.JPG | Verticulium wilt | 2 |
| 523tomato_valid_leaf curl.JPG | Leaf curl | 2028tomato_train_verticulium wilt.JPG | Verticulium wilt | 2 |
| 550tomato_valid_verticulium wilt.JPG | Verticulium wilt | 1183tomato_train_leaf curl.JPG | Leaf curl | 3 |
| 1250tomato_valid_septoria leaf spot.JPG | Septoria leaf spot | 995tomato_train_leaf curl.JPG | Leaf curl | 3 |
| 1025tomato_valid_septoria leaf spot.JPG | Septoria leaf spot | 1735tomato_train_verticulium wilt.JPG | Verticulium wilt | 3 |
| 133tomato_valid_leaf blight.JPG | Leaf blight | 1454tomato_train_septoria leaf spot.JPG | Septoria leaf spot | 3 |
| 736tomato_valid_verticulium wilt.JPG | Verticulium wilt | 2006tomato_train_leaf curl.JPG | Leaf curl | 3 |

Some Test images appear in multiple candidate pairs. Therefore, these 13 rows do not represent 13 independent Test photographs.

### 18.6 Visual Candidate Review

A contact sheet was generated for the 13 strongest cross-class candidates:

`reports/ccmt_hash_overlap/ccmt_cross_class_top13_contact_sheet.jpg`

The contact sheet provides a side-by-side visual comparison of the candidate images.

The displayed images show visual similarities in leaf appearance, orientation and visible damage. However, the contact sheet was viewed at reduced size, and the visual review does not establish that all candidate pairs contain the same original photograph.

The 13 pairs remain perceptual similarity candidates. Full-resolution pair-by-pair verification is required before classifying them as confirmed repeated photographs or label conflicts.

### 18.7 Generated Evidence Files

The supplementary analysis generated:

| File | Purpose |
|---|---|
| `ccmt_dhash_candidate_pairs_le8.csv` | All Train-Test candidate pairs with distance ≤ 8 |
| `ccmt_dhash_nearest_train_matches.csv` | Nearest Train match for each non-exact Test image |
| `ccmt_dhash_candidate_summary.json` | Overall supplementary dHash results |
| `ccmt_dhash_cross_class_candidates.csv` | Cross-class candidate pairs |
| `ccmt_dhash_cross_class_summary.json` | Cross-class candidate summary |
| `ccmt_cross_class_top13_contact_sheet.jpg` | Visual comparison of the 13 strongest cross-class candidates |

### 18.8 Interpretation and Limitations

- Perceptual hash similarity identifies visually similar candidates; it does not prove photograph identity.
- A dHash distance of zero does not establish identical file content.
- The 550 candidate pairs are not 550 confirmed duplicate photographs.
- Cross-class similarity does not establish which disease label is correct.
- The supplementary implementation differs from the earlier undocumented dHash implementation. Its results must remain separate from the earlier Section 16 results.
- Biological sample independence cannot be established without reliable plant, leaf or specimen identifiers.
- Candidate lineage and transformed original-image relationships remain incompletely verified.

### 18.9 Updated Recommendation

The supplementary dHash investigation adds further evidence of potential Train-Test similarity and cross-class inconsistency.

The supplied Train-Test split remains unsuitable as an independent evaluation split because of the previously verified exact-content overlap and visually observed repeated photographs.

A leakage-aware partition should be considered only after original-image groups have been verified. Biological independence must not be claimed without reliable biological sample identifiers.

No original images or labels were modified.

**Investigation date:** 27 November 2026

**Status:** Supplementary dHash candidate analysis completed; broader visual verification remains pending

**Documentation status:** Prepared for review

## 19. Biological Metadata and Identifier Audit - 27 November 2026

### 19.1 Objective

A read-only audit was performed on all 5,805 raw Tomato images to determine whether filename patterns or embedded EXIF metadata could support biological sample grouping.

### 19.2 Results

| Check | Result |
|---|---:|
| Raw Tomato images checked | 5,805 |
| Images containing EXIF metadata | 0 |
| Filenames containing numbers | 5,805 |
| Filenames containing four or more digits | 2,109 |
| Filenames matching broad biological-identifier keyword search | 4,576 |

No EXIF metadata was available.

Although filenames contain numeric values and some contain words such as leaf, these patterns do not establish plant, leaf, specimen or sample identity.

### 19.3 Biological Grouping Conclusion

Reliable biological sample identifiers could not be established from the available raw-image filenames or EXIF metadata.

The numeric filename components must not be interpreted as unique plant or specimen identifiers without supporting evidence.

Therefore:

- Biological independence between images cannot be verified.
- A biological-grouped Train-Test split cannot currently be guaranteed.
- Exact-content and verified original-image groups can still be used for image-level leakage control.
- Any remaining biological-independence limitation must be explicitly documented.

No original images or metadata were modified.

**Investigation date:** 27 November 2026

**Status:** Available filename and EXIF metadata audit completed; biological grouping unresolved
