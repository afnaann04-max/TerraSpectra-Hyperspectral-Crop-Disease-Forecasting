

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
