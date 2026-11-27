# NWRD Wheat Rust — Follow-up Verification Report

**Project:** TerraSpectra – Hyperspectral Crop Disease Forecasting
**Assigned responsibility:** Member 3 – RGB Dataset Investigation
**Investigation date:** 18 November 2026
**Dataset:** NUST Wheat Rust Disease Dataset (NWRD)
**Status:** Public-source follow-up and archive-level verification completed; dataset licence clarification and split methodology remain pending.

---

## 1. Purpose

This report records follow-up verification of the NWRD Wheat Rust dataset, focusing on:

1. The difference between the research paper's 80/10/10 split and the GitHub README's 90/10 split.
2. Dataset licence clarification and available author contact channels.
3. Reported image count, mask count and image-mask pairing questions.

The dataset archive was downloaded and verified using archive-listing commands; image files were not extracted or modified.

## 2. Dataset Sources

- **Zenodo record:** https://zenodo.org/records/21672928
- **Zenodo DOI:** https://doi.org/10.5281/zenodo.21672928
- **GitHub repository:** https://github.com/dll-ncai/NUST-Wheat-Rust-Disease-NWRD
- **GitHub README:** https://github.com/dll-ncai/NUST-Wheat-Rust-Disease-NWRD/blob/main/README.md
- **Research paper:** https://www.mdpi.com/1424-8220/23/15/6942
- **Research paper DOI:** https://doi.org/10.3390/s23156942

## 3. Dataset Split Discrepancy

### 3.1 Research paper

The research paper reports that the images were randomly divided into:

| Split | Percentage |
|---|---:|
| Training | 80% |
| Validation | 10% |
| Testing | 10% |
| Total | 100% |

### 3.2 GitHub README

The GitHub README reports:

| Split | Percentage |
|---|---:|
| Train + Validation | 90% |
| Test | 10% |
| Total | 100% |

The README also shows a configuration parameter:

`validation_split: 0.1`

This parameter indicates a validation portion of 0.1 in the data-loader configuration.

### 3.3 Follow-up interpretation

One possible explanation is that the README describes an initial division of 90% for training plus validation and 10% for testing. The 90% portion may then be divided into training and validation using the `validation_split` configuration.

However, this interpretation has not been confirmed by the dataset authors.

The exact split implementation, random seed, image identifiers in each split and final image counts remain unverified.

**Conclusion:** The difference between the two descriptions remains unresolved pending author clarification or inspection of the actual split files.

## 4. Dataset Licence and Author Contact

### 4.1 Zenodo record

The Zenodo record identifies:

- Hirra Anwar — Contact person
- Faisal Shafait — Supervisor

The rights information displayed on the Zenodo record is:

`Copyright (C) 2023 The Authors`

No explicit dataset reuse licence was identified in the accessible rights information.

### 4.2 GitHub repository licence

The GitHub repository displays an MIT licence.

This is evidence of a licence for the repository's software/code. It must not automatically be interpreted as a licence for the dataset images and segmentation masks.

### 4.3 Author contact availability

The Zenodo record identifies Hirra Anwar as the contact person. However, a publicly displayed email address could not be verified from the accessible record.

The GitHub repository provides an Issues section:

https://github.com/dll-ncai/NUST-Wheat-Rust-Disease-NWRD/issues

Two existing issues were found concerning dataset download-link availability:

- Issue #1, opened 25 April 2024: The link to the dataset does not work.
- Issue #2, opened 10 April 2025: Dataset link is not working.

No author clarification about the dataset licence or split discrepancy was found in the reviewed issue pages.

**Conclusion:** Dataset reuse permission and licence remain unresolved. Author clarification is required before making assumptions about redistribution or modification rights.

### 4.4 Additional Licence Evidence — NLM Dataset Catalog

A further verification check was conducted using the NLM Dataset Catalog entry for the same NWRD dataset and Zenodo record.

The NLM Dataset Catalog lists the dataset rights as:

**Creative Commons Attribution 4.0 International (CC BY 4.0).**

The catalog entry links to the same Zenodo dataset DOI: `10.5281/zenodo.21672928`.

This provides additional licence evidence. However, the Zenodo record's visible rights information was previously recorded as `Copyright (C) 2023 The Authors`, so the licence information is not consistently displayed across the sources reviewed.

The research paper is itself published under CC BY 4.0, but the publication licence and dataset licence should be distinguished.

**Updated interpretation:**

- NLM Dataset Catalog: explicitly lists CC BY 4.0 for the dataset.
- Zenodo record: visible rights statement is Copyright (C) 2023 The Authors.
- GitHub repository: MIT licence displayed for repository software; not automatically assumed to apply to dataset images and masks.
- Research paper: CC BY 4.0 publication licence.

The NLM catalog listing is positive evidence of dataset reuse rights, but because of the differing rights displays, explicit confirmation from the dataset authors or clarification on the primary Zenodo record is still recommended before final project approval.

**Status: Licence evidence improved; discrepancy and author clarification remain pending.**

## 5. Image Count and Image-Mask Pairing

### 5.1 Published image count

The Zenodo record and GitHub README report a total of 100 images.

This is a published dataset count, not an independently verified archive count.

### 5.2 Reported file formats

The GitHub README describes:

- Original images: JPG format
- Binary segmentation masks: PNG format

### 5.3 Reported directory structure

The README displays the following structure:

```text
NWRD/
├── test/
│   ├── images/
│   └── masks/
└── train/
    ├── images/
    └── masks/
```

### 5.4 Archive-Level Verification

The downloaded archive was independently inventoried without extracting the dataset images.

Verified results:

- Actual JPG image count: 100
- Actual PNG mask count: 100
- Training images: 90
- Training masks: 90
- Testing images: 10
- Testing masks: 10
- Image-mask filename pairing: verified with zero unmatched filenames
- Train-test filename overlap: zero shared filenames
- Archive structure: train and test folders; no separate validation folder found
- Archive checksum: verified against the official MD5

Detailed archive-level results are documented in Section 10.

Visual content, mask correctness, image resolution, and visual duplicates under different filenames have not been inspected.

## 6. Verification Status

| Verification item | Status |
|---|---|
| Zenodo dataset record identified | Verified |
| GitHub repository identified | Verified |
| Research paper identified | Verified |
| Published total image count | Reported as 100 |
| Research paper split | Reported as 80/10/10 |
| GitHub README split | Reported as 90/10 |
| Validation split configuration | `validation_split: 0.1` shown |
| Actual archive train/test split | Verified: 90 train / 10 test |
| Actual image count | Verified: 100 JPG |
| Actual mask count | Verified: 100 PNG |
| Train image-mask filename pairing | Verified: 0 unmatched |
| Test image-mask filename pairing | Verified: 0 unmatched |
| Train-test filename overlap | Verified: 0 shared filenames |
| Archive file types | Verified: JPG and PNG only |
| Separate validation folder | Not present in inspected archive |
| Exact validation split implementation | Unresolved |
| Dataset reuse licence | Licence evidence conflicting; clarification pending |
| GitHub code licence | MIT displayed |
| Public author contact person | Hirra Anwar identified |
| Public author email | Not verified |
| Visual mask correctness/alignment | Not checked |
| Visual duplicate images under different filenames | Not checked |
| Image resolution | Not verified |
| Model suitability approval | Pending |

The archive-level checks are completed. Remaining unresolved items primarily concern dataset licensing, the validation methodology discrepancy, and visual inspection of images and masks.

## 7. Next Steps

1. Seek author clarification on the 80/10/10 split described in the research paper versus the 90/10 archive split.
2. Clarify how the validation split is generated or used, since no separate validation folder was found in the downloaded archive.
3. Seek confirmation that CC BY 4.0 applies to the dataset images and segmentation masks, given the conflicting rights information.
4. If authorized for further inspection, visually inspect sample images and masks to assess image-mask alignment and mask quality.
5. Check image resolution and mask pixel values if these become necessary for dataset suitability assessment.
6. Assess potential visual duplicates under different filenames if required.
7. Complete the final dataset suitability assessment for the TerraSpectra project after the remaining questions are resolved.

## 8. Restrictions and Investigation Notes

- The official NWRD archive was downloaded and checksum-verified.
- Archive contents were inspected using listing commands; dataset images were not extracted.
- Image and mask filenames were compared within the train and test splits.
- No unmatched image or mask filenames were found.
- No filename overlap was detected between train and test images.
- Image and mask contents were not visually inspected.
- No original image or mask files were modified or deleted.
- No preprocessing or augmentation was performed.
- No model training was performed.
- Visual duplicate content under different filenames has not been checked.
- Dataset licence clarification remains pending.
- The GitHub repository's MIT code licence was not assumed to cover the dataset images and masks.
- Final dataset suitability approval remains pending.

## 9. References

1. Zenodo dataset record: https://zenodo.org/records/21672928
2. GitHub repository: https://github.com/dll-ncai/NUST-Wheat-Rust-Disease-NWRD
3. GitHub README: https://github.com/dll-ncai/NUST-Wheat-Rust-Disease-NWRD/blob/main/README.md
4. GitHub issues: https://github.com/dll-ncai/NUST-Wheat-Rust-Disease-NWRD/issues
5. Research paper: https://doi.org/10.3390/s23156942
6. NLM Dataset Catalog — Dataset rights listing for NWRD (CC BY 4.0):
   https://datasetcatalog.nlm.nih.gov/dataset?q=0003216471

**Investigation date:** 18 November 2026
**Prepared by:** Member 3 – RGB Dataset Investigation
**Final status:** Public-source follow-up and archive-level verification completed; dataset licence clarification, split methodology, and visual quality assessment remain pending.

## 10. Downloaded Archive Verification

### 10.1 Download Verification

The official NWRD archive was downloaded from the Zenodo dataset record.

- Archive name: `NWRD.zip`
- Downloaded file size: 608,898,312 bytes
- Approximate size: 608.9 MB
- Expected MD5: `7b9193efebe1ed8c60b10c9f05d11e14`
- Actual MD5: `7B9193EFEBE1ED8C60B10C9F05D11E14`
- Checksum result: **MATCH**

The downloaded archive matches the official MD5 checksum.

### 10.2 Actual Archive File Inventory

The archive was inventoried without extracting the images.

| Split | Images (.jpg) | Masks (.png) |
|---|---:|---:|
| Train | 90 | 90 |
| Test | 10 | 10 |
| Total | 100 | 100 |

| File type | Count |
|---|---:|
| JPG | 100 |
| PNG | 100 |
| Total files | 200 |

No other file types were found.

### 10.3 Image-Mask Filename Pairing

Image and mask filenames were compared by filename stem within each split.

| Split | Images without matching masks | Masks without matching images |
|---|---:|---:|
| Train | 0 | 0 |
| Test | 0 | 0 |

All 90 training images and all 10 testing images have corresponding mask filenames.

This verifies filename-level pairing only. Mask pixel correctness and visual alignment have not been inspected.

### 10.4 Train-Test Filename Overlap

Training and testing image filename identifiers were compared.

| Metric | Result |
|---|---:|
| Train image IDs | 90 |
| Test image IDs | 10 |
| Shared filenames | 0 |

No filename overlap was detected. Identical or near-identical visual content under different filenames has not been checked.

### 10.5 Archive Structure

The verified archive contains:

```text
NWRD/
|-- train/
|   |-- images/  (90 JPG files)
|   |-- masks/  (90 PNG files)
|-- test/
    |-- images/ (10 JPG files)
    |-- masks/ (10 PNG files)
```

No separate validation folder was found in the archive listing.

### 10.6 Verification Limitations

- Images were not extracted or opened.
- Masks were not visually inspected.
- Image resolution was not independently verified.
- Mask pixel values and segmentation quality were not examined.
- Visual duplicates under different filenames were not checked.
- Disease-class labels were not independently verified from image contents.
- No preprocessing, augmentation, or model training was performed.

### 10.7 Updated Conclusion

The NWRD archive-level verification is completed.

The downloaded ZIP matches the official MD5 checksum. It contains 100 JPG images and 100 PNG masks, with 90 image-mask pairs in train and 10 in test. Filename pairing was verified with zero unmatched files, and no filename overlap was found between train and test.

The archive contains train and test folders only; no separate validation folder was found. The earlier split-description discrepancy is partially clarified by the actual archive structure, but the exact validation procedure described in the README and paper remains unresolved.

Dataset licence clarification remains pending because the previously reviewed sources displayed inconsistent rights information.

**Updated status: Download and archive-level verification completed. Visual inspection, licence clarification, and final dataset suitability assessment remain pending.**

## Additional Licence and Dataset Reuse Verification

### Public-source licence review

A further review was conducted to distinguish the licensing of the NWRD software repository from the licensing of the wheat rust dataset itself.

#### Findings

- **Zenodo dataset:** The record provides public access to the dataset, but an explicit reuse licence for the images and masks could not be confirmed from the reviewed evidence.
- **Copyright statement:** The dataset record includes a copyright notice identifying the authors.
- **Research paper:** The paper's open-access licence applies to the publication. It does not independently confirm the licence of all downloadable dataset assets.
- **GitHub repository:** The repository declares an MIT licence. However, the reviewed information does not clearly establish that the MIT licence covers the dataset's images and segmentation masks rather than repository code.
- **Public availability:** The dataset can be downloaded publicly, but availability alone is not sufficient evidence of permission for dataset reuse or redistribution.

### Licence status

| Asset | Licence status |
|---|---|
| Repository code | MIT declared |
| Wheat rust RGB images | Reuse licence not confirmed |
| Segmentation masks | Reuse licence not confirmed |
| Dataset redistribution rights | Unresolved |
| Explicit dataset reuse permission | Not verified from reviewed public sources |

### Conclusion

The NWRD dataset's public accessibility has been established, but reuse rights for the dataset images and masks remain unresolved. The GitHub MIT licence should not be assumed to apply to the dataset assets without explicit supporting evidence.

No author contact was initiated.

### Remaining blocker

Before treating NWRD as licence-cleared for reuse in TerraSpectra, explicit licensing or permission covering the dataset assets must be established. Until then, dataset reuse rights remain unresolved.

## 11. Extended Archive-Level and Visual Verification — 27 November 2026

### 11.1 Image and Mask Pairing

A further read-only inspection was performed directly from the downloaded `NWRD.zip` archive.

| Split | RGB images | Masks | Missing masks | Missing images |
|---|---:|---:|---:|---:|
| Train | 90 | 90 | 0 | 0 |
| Test | 10 | 10 | 0 | 0 |
| Total | 100 | 100 | 0 | 0 |

All image-mask filenames were successfully matched using their filename stems.

### 11.2 Image and Mask Dimensions

99 of the 100 image-mask pairs have matching dimensions.

One mismatch was identified:

| Image | RGB dimensions | Mask dimensions |
|---|---|---|
| `train/images/101.jpg` | 3612 × 3456 | `train/masks/101.png`: 3593 × 3435 |

The mask is 19 pixels narrower and 21 pixels shorter than its corresponding RGB image.

A visual inspection and temporary overlay were performed. The mask-positive regions appeared broadly associated with the wheat vegetation, but exact pixel-level alignment and segmentation correctness could not be established.

The original image and mask were not modified. Resizing was performed only on a temporary in-memory copy for visual inspection.

**Finding:** Image 101 has a dimension inconsistency that must be considered before segmentation use.

### 11.3 Binary Mask Encoding

All 100 masks were inspected for image mode and distinct pixel values.

Verified findings:

- All masks use grayscale mode (`L`).
- All masks contain exactly two pixel values: `0` and `255`.
- No additional grayscale values were found.

This confirms binary mask encoding.

The public dataset documentation describes the task as wheat rust/non-rust semantic segmentation. However, the numerical mapping of `0` and `255` to the respective classes was not independently confirmed from an explicit pixel-value specification.

### 11.4 Exact Duplicate Image and Mask Investigation

SHA-256 hashes were calculated for all 200 image and mask files.

One exact duplicate RGB image group was found within Train:

| File | Finding |
|---|---|
| `train/images/15.jpg` | Exact duplicate |
| `train/images/32.jpg` | Exact duplicate |

Both files have the same SHA-256 hash:

`a281c494f2b690a5b988a9401c0264caa709538bbf79263239aa05f0eca757a8`

No exact duplicate mask groups were identified.

### 11.5 Duplicate RGB Images with Different Masks

The corresponding masks for the duplicate RGB images were compared.

| Measurement | Mask 15 | Mask 32 |
|---|---:|---:|
| Dimensions | 6016 × 4000 | 6016 × 4000 |
| White pixels | 25,371 | 40,832 |
| Foreground coverage | Approximately 0.105% | Approximately 0.170% |

Additional findings:

- Different pixels: 16,653.
- Difference bounding box: `(1106, 1578, 5370, 4000)`.
- Mask 15 bounding box: `(1106, 1577, 3969, 2176)`.
- Mask 32 bounding box: `(1106, 1577, 5370, 4000)`.

Visual comparison confirmed that the RGB images depict the same photograph, while the corresponding masks differ.

**Interpretation:** This is a potential annotation inconsistency. The correct segmentation cannot be determined from the available evidence alone.

### 11.6 Train-Test Exact Duplicate Verification

SHA-256 comparisons were performed separately for RGB images and masks across Train and Test.

| Check | Exact duplicate groups |
|---|---:|
| RGB images across Train-Test | 0 |
| Masks across Train-Test | 0 |
| Total | 0 |

No exact cross-partition duplicate content was detected.

This does not establish biological independence. Near-duplicate photographs, related plants or specimens, and other forms of biological overlap have not been ruled out.

### 11.7 Foreground Coverage Investigation

All 100 masks were checked for the percentage of white foreground pixels.

| Measurement | Result |
|---|---:|
| Masks checked | 100 |
| Masks with zero foreground | 0 |
| Masks with more than 50% foreground | 0 |
| Lowest foreground coverage | 0.0312% |
| Highest foreground coverage | 2.9885% |

Examples:

- Lowest: `train/masks/22.png` — 0.0312%.
- Highest: `train/masks/19.png` — 2.9885%.

Visual inspection of these two examples showed small foreground regions in Mask 22 and multiple narrow foreground regions in Mask 19.

These observations do not independently establish that all foreground regions represent rust lesions. The dataset's exact annotation convention and biological correctness require further validation.

### 11.8 Public Documentation and Licence Findings

The archive contains only Train and Test directories, with JPG images and PNG masks. No README, licence file, annotation guide, or other documentation file was present inside the downloaded ZIP.

The public GitHub documentation describes binary semantic segmentation for wheat rust and non-rust regions.

The following distinctions remain important:

- The GitHub MIT licence must not automatically be applied to dataset images and masks.
- The NLM Dataset Catalog lists CC BY 4.0 for NWRD.
- The Zenodo record's previously reviewed rights information displays a copyright notice.
- The differing rights statements have not been conclusively reconciled.
- The research paper's publication licence is not automatically the dataset licence.

**Status:** There is positive CC BY 4.0 evidence from the NLM Dataset Catalog, but dataset asset reuse permissions should remain subject to rights verification.

No author contact was initiated.

### 11.9 Updated Verification Status

| Verification item | Status |
|---|---|
| RGB-mask filename pairing | Verified: 100/100 |
| Matching image-mask dimensions | 99/100 |
| Binary mask encoding | Verified: values 0 and 255 |
| Exact duplicate RGB images | One group within Train |
| Exact duplicate masks | None found |
| Duplicate RGB with different masks | Confirmed |
| Exact Train-Test RGB overlap | None found |
| Exact Train-Test mask overlap | None found |
| Empty masks | None found |
| Foreground coverage | 0.0312%–2.9885% |
| Sample visual inspection | Completed |
| Exact alignment of all masks | Not verified |
| Numeric foreground/background mapping | Not explicitly verified |
| Biological sample independence | Unresolved |
| Dataset asset reuse permission | Conflicting evidence; unresolved |
| Split methodology discrepancy | Partially clarified; exact procedure unresolved |

### 11.10 Updated Dataset Suitability Recommendation

NWRD is a promising candidate for exploratory wheat stripe rust segmentation because it provides 100 RGB images and corresponding binary masks.

However, its suitability remains conditional because:

1. One RGB image and mask have mismatching dimensions.
2. Two identical RGB images have different segmentation masks.
3. The numerical mapping of binary mask values requires explicit confirmation.
4. Biological independence across Train and Test has not been established.
5. Dataset image and mask reuse permissions remain subject to rights clarification.

No model training, preprocessing, augmentation, feature extraction, or modification of original images or masks was performed.

**Updated recommendation:** Retain NWRD as a conditionally suitable candidate for further segmentation research. Do not describe it as fully validated, biologically independent, or licence-cleared.

### 11.11 Investigation Restrictions

- Original archive files were read directly without modifying them.
- Visual comparisons used temporary in-memory image displays.
- A common top-left coordinate area was used only for the Image 101 diagnostic overlay; original files were not resized or      modified.
- No original image or mask was overwritten, resized, deleted, or redistributed.
- No preprocessing, feature extraction, augmentation, or model training was performed.
- No author contact was initiated.

**Investigation date:** 27 November 2026
**Prepared by:** Member 3 – RGB Dataset Investigation

## NWRD RGB–Mask Pairing and Visual Validation — 27 November 2026

### 1. Filename Pairing Verification

The NWRD archive was checked for matching RGB image and mask filenames using filename stems.

| Partition | RGB images | Masks | Missing masks | Missing images |
|---|---:|---:|---:|---:|
| Train | 90 | 90 | 0 | 0 |
| Test | 10 | 10 | 0 | 0 |
| **Total** | **100** | **100** | **0** | **0** |

All 100 RGB images have corresponding masks by filename.

This confirms filename pairing only, not annotation correctness.

### 2. Image and Mask Dimension Verification

All 100 image-mask pairs were inspected.

- 99 pairs have matching RGB and mask dimensions.
- One mismatch was identified.

| File | RGB dimensions | Mask dimensions |
|---|---|---|
| `train/images/101.jpg` | 3612 × 3456 | 3593 × 3435 |

The mask is 19 pixels narrower and 21 pixels shorter than the RGB image.

### 3. Mask Format and Pixel Values

All 100 masks were inspected directly from the archive.

Verified findings:
- All masks use grayscale mode (`L`).
- All masks contain only pixel values 0 and 255.
- All masks contain non-zero white foreground pixels.
- White-pixel coverage ranges from 0.03125% to 2.98851%.
- No zero-white masks were found.

The semantic mapping of 0 and 255 to rust and background has not been independently confirmed.

### 4. Exact Duplicate Verification

SHA-256 comparison produced the following results:

| Check | Result |
|---|---:|
| RGB images | 100 |
| Unique RGB contents | 99 |
| Exact duplicate RGB groups | 1 |
| Masks | 100 |
| Unique mask contents | 100 |
| Exact duplicate mask groups | 0 |
| Cross-Train-Test exact duplicate groups | 0 |

The exact duplicate RGB files are:
- `train/images/15.jpg`
- `train/images/32.jpg`

### 5. Duplicate Image with Different Masks

Both RGB images have dimensions of 6016 × 4000 and identical SHA-256 hashes.

Their corresponding masks differ:

| Measurement | Mask 15 | Mask 32 |
|---|---:|---:|
| Dimensions | 6016 × 4000 | 6016 × 4000 |
| White pixels | 25,371 | 40,832 |
| White coverage | 0.105431% | 0.169681% |

Visual comparison indicated that both masks mark the same main visible region on a central leaf. Mask 32 also appears to include an additional small region near the lower-right edge.

This is a potential annotation inconsistency. The available visual evidence does not establish whether the additional region is a valid rust annotation or an annotation error.

### 6. Preliminary Visual Alignment Review

Five dimension-matched pairs were visually inspected using RGB-mask overlays:

- Train: Images 2, 64 and 100.
- Test: Images 105 and 123.

The highlighted regions generally appeared spatially associated with visible plant or leaf structures. No obvious gross alignment failure was observed in these five examples.

However:
- Some regions are difficult to assess because of overlapping vegetation.
- Visual association with a leaf does not prove that a region represents rust.
- Five examples do not constitute representative full-dataset validation.

Therefore, annotation accuracy and alignment across all 100 pairs remain unverified.

### 7. Image 101 Dimension Mismatch Investigation

Image 101 was examined separately.

Metadata findings:
- RGB format: JPEG.
- Mask format: PNG.
- RGB mode: RGB.
- Mask mode: grayscale (`L`).
- Neither file contains EXIF metadata.
- The JPEG contains JFIF, DPI and ICC-profile information.
- The mask contains no additional metadata.

Boundary inspection found zero white pixels along all four mask edges.

A diagnostic overlay was created using only the common top-left coordinate area of the original image and mask. The overlay showed several highlighted regions over visible plant structures, but this does not establish correct spatial correspondence.

The dimension difference could be related to cropping or different image versions, but neither explanation has been verified.

**Recommendation:** Exclude Image 101 from segmentation experiments until its image-mask spatial correspondence is verified. Do not resize or crop the original files merely to force matching dimensions.

### 8. Updated NWRD Suitability Assessment

Positive findings:
- All 100 image-mask filenames match.
- 99 pairs have matching dimensions.
- All masks contain binary values 0 and 255.
- No exact duplicate masks were found.
- No exact duplicate content was detected across Train and Test.
- Five selected overlays showed no obvious gross alignment failure.

Outstanding concerns:
- One RGB-mask dimension mismatch.
- One duplicate RGB image group with different masks.
- Unresolved semantic interpretation of mask pixel values.
- Full-dataset annotation alignment has not been validated.
- Biological independence remains unestablished.
- Dataset image and mask reuse permissions remain unresolved.

**Conclusion:** NWRD remains a conditional candidate for exploratory wheat rust segmentation. Further verification is required before final dataset approval or independent model evaluation.

### 9. Investigation Restrictions

- Original RGB images and masks were not modified.
- Inspection was performed directly from the ZIP archive.
- No resizing, cropping, preprocessing or augmentation was applied to the source files.
- No model training or feature extraction was performed.
- No author contact was initiated.

## NWRD Dataset Image and Mask Licence Verification — 27 November 2026

### 1. Purpose

This investigation reviews the publicly available licence information for the NWRD Wheat Rust dataset.

The objective is to distinguish the licensing status of:
- GitHub source code.
- Research paper.
- Dataset RGB images and segmentation masks.

A licence associated with one of these resources must not automatically be assumed to apply to the others.

### 2. Source Verification

#### 2.1 Zenodo Dataset Record

**Source:** https://zenodo.org/records/21672928

The Zenodo record identifies the dataset authors and displays the rights statement:

`Copyright (C) 2023 The Authors`

An explicit Creative Commons or other dataset reuse licence was not identified in the previously reviewed Rights information.

**Finding:** Dataset image and mask reuse permission is not established by this rights statement alone.

#### 2.2 GitHub Repository

**Source:** https://github.com/dll-ncai/NUST-Wheat-Rust-Disease-NWRD

The GitHub repository declares an MIT licence.

The MIT licence applies to the repository's licensed software/code. It must not automatically be interpreted as permission to reuse separately hosted dataset images and segmentation masks.

**Finding:** The repository's MIT licence does not independently establish the asset licence.

#### 2.3 NLM Dataset Catalog

**Source:** https://www.ncbi.nlm.nih.gov/gds/

The previously reviewed NLM Dataset Catalog entry for NWRD lists Creative Commons Attribution 4.0 International (CC BY 4.0).

However, the relationship between this catalog metadata and an explicit licence declaration by the dataset creators has not been independently established.

**Finding:** CC BY 4.0 is listed in the catalog, but its authority for the original dataset assets remains unresolved.

#### 2.4 Research Paper

**Source:** https://www.mdpi.com/1424-8220/23/15/6942

The associated research paper is published under CC BY 4.0.

The paper's licence applies to the paper and does not automatically establish the reuse rights of the separately distributed RGB images and segmentation masks.

**Finding:** The paper's licence cannot be treated as definitive dataset asset permission.

### 3. Comparative Licence Assessment

| Resource | Publicly displayed licence or rights | Assessment |
|---|---|---|
| GitHub source