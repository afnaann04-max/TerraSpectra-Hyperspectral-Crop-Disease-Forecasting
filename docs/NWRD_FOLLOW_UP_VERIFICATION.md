# NWRD Wheat Rust — Follow-up Verification Report

**Project:** TerraSpectra – Hyperspectral Crop Disease Forecasting
**Assigned responsibility:** Member 3 – RGB Dataset Investigation
**Investigation date:** 18 November 2026
**Dataset:** NUST Wheat Rust Disease Dataset (NWRD)
**Status:** Public-source follow-up completed; archive-level verification and author clarification pending

---

## 1. Purpose

This report records follow-up verification of the NWRD Wheat Rust dataset, focusing on:

1. The difference between the research paper's 80/10/10 split and the GitHub README's 90/10 split.
2. Dataset licence clarification and available author contact channels.
3. Reported image count, mask count and image-mask pairing questions.

No dataset archive was downloaded or modified.

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

### 5.4 Unresolved archive-level questions

The following details cannot be confirmed without inspecting the archive:

- Actual number of JPG images.
- Actual number of PNG masks.
- Number of images in each split.
- Number of masks in each split.
- Whether every image has a corresponding mask.
- Whether image and mask filenames follow a consistent naming convention.
- Whether any images or masks are missing or duplicated.
- Whether the validation data are stored separately or generated dynamically.
- Whether the archive directory structure matches the README.

No archive was downloaded for this investigation.

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
| Exact split implementation | Unresolved |
| Dataset reuse licence | Unresolved |
| GitHub code licence | MIT displayed |
| Public author contact person | Hirra Anwar identified |
| Public author email | Not verified |
| Actual image count | Not verified |
| Actual mask count | Not verified |
| Image-mask pairing | Not verified |

## 7. Next Steps

1. Seek author clarification on the 80/10/10 versus 90/10 split descriptions.
2. Seek explicit clarification of the dataset image and mask reuse licence.
3. Ask for confirmation of the actual image and mask counts.
4. Ask whether every image has a corresponding binary segmentation mask.
5. Obtain permission before downloading or modifying the archive if required by the project.
6. Perform archive-level inventory only after explicit authorization.

## 8. Restrictions and Investigation Notes

- No dataset archive was downloaded.
- No original files were modified or deleted.
- No image-mask pairing was claimed as verified.
- No preprocessing or augmentation was performed.
- No model training was performed.
- The dataset has not been approved for modelling.
- The GitHub repository's MIT code licence was not assumed to cover the dataset.

## 9. References

1. Zenodo dataset record: https://zenodo.org/records/21672928
2. GitHub repository: https://github.com/dll-ncai/NUST-Wheat-Rust-Disease-NWRD
3. GitHub README: https://github.com/dll-ncai/NUST-Wheat-Rust-Disease-NWRD/blob/main/README.md
4. GitHub issues: https://github.com/dll-ncai/NUST-Wheat-Rust-Disease-NWRD/issues
5. Research paper: https://doi.org/10.3390/s23156942

**Investigation date:** 18 November 2026
**Prepared by:** Member 3 – RGB Dataset Investigation
**Final status:** Public-source follow-up completed; author clarification and archive-level verification pending.
