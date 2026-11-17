# NWRD Wheat Rust – Initial Source Verification Report

**Project:** TerraSpectra – RGB Dataset Investigation  
**Date:** 17 November 2026  

## 1. Dataset Identification

- **Dataset Name:** NUST Wheat Rust Disease Dataset (NWRD)
- **DOI:** 10.5281/zenodo.21672928
- **Official Source:** https://zenodo.org/records/21672928
- **Research Paper:** https://pmc.ncbi.nlm.nih.gov/articles/PMC10422341/
- **Official GitHub Repository:** https://github.com/dll-ncai/NUST-Wheat-Rust-Disease-NWRD
- **Institutional Download Page:** https://dll.seecs.nust.edu.pk/downloads/
- **Archive:** NWRD.zip
- **Reported Archive Size:** 608.9 MB
- **Version:** 1.0
- **Publication Date:** 4 August 2023

## 2. Source and Access Verification

The official Zenodo record lists the NWRD.zip archive for download. The dataset is publicly listed and does not indicate an access-permission application requirement.

The GitHub README also identifies an institutional NUST download page.

The institutional download page timed out during this investigation. Therefore, its current accessibility could not be confirmed.

**Download status:** Not downloaded.

## 3. Licence and Usage Conditions

The Zenodo Rights section displays:

Copyright (C) 2023 The Authors.

No specific dataset licence, such as CC BY 4.0, is clearly identified in the accessible record.

The associated research paper is open access under a Creative Commons Attribution (CC BY) licence. This paper licence must not be assumed to apply automatically to the separate dataset archive.

**Pending:** Obtain explicit confirmation of the dataset's reuse, redistribution and modification permissions from the authors.

## 4. Dataset Characteristics

| Characteristic | Reported information |
|---|---|
| Number of images | 100 |
| Image type | RGB |
| Main disease | Wheat stripe rust |
| Dataset task | Semantic segmentation |
| Image format | JPG |
| Mask format | PNG |
| Segmentation classes | Rust and non-rust |
| Image resolutions | 6016 × 4000 and 4608 × 3456 |
| Collection location | NARC, Islamabad, Pakistan |
| Collection period | 2021–2022 |
| Wheat variety | Not specified |

The dataset contains multiple wheat leaves in each field image, including healthy and rust-affected leaves.

The 100-image count is reported by the official dataset description and paper. It has not been independently counted from the archive.

## 5. Labels and Annotation Information

NWRD is a binary semantic segmentation dataset.

| Class | Definition |
|---|---|
| Rust | Pixels representing visible wheat stripe rust |
| Non-rust | Healthy leaves, stems, soil, shadows and other non-rust regions |

The research paper reports manual, pixel-level annotations represented as binary segmentation masks.

**Documented formats:**
- Original RGB images: JPG
- Segmentation masks: PNG

The exact pixel values used for the two classes are not confirmed. A separate CSV or Excel annotation file is not documented in the accessible repository README.

## 6. Image Collection Conditions

According to the research paper:

- The wheat crop was cultivated from November 2021 and harvested in May 2022.
- Images were collected at the National Agricultural Research Centre (NARC), Islamabad, Pakistan.
- Images were captured during morning and afternoon periods.
- Natural field and weather conditions were represented.
- Images include aerial, ground and front views.
- The dataset includes different viewing distances, illumination conditions, crop densities and complex backgrounds.

The specific wheat variety, camera model, camera settings and exact image-level collection dates are not specified in the accessible documentation.

## 7. Documented Folder Structure

The official GitHub README documents:

NWRD/
- test/
  - images/
  - masks/
- train/
  - images/
  - masks/

Image formats:
- images: JPG
- masks: PNG

The README reports a 90% train-plus-validation and 10% test split. It does not display a separate validation directory in the documented folder tree.

Exact image counts per folder and total file counts remain unverified because the archive was not downloaded.

## 8. Unresolved Questions

1. What is the exact licence for the dataset archive?
2. What reuse and redistribution conditions apply?
3. Which wheat variety was used?
4. Which camera model and acquisition settings were used?
5. How many images and masks are present in each folder?
6. Are all RGB images correctly matched with their corresponding masks?
7. What exact pixel values represent rust and non-rust?
8. Is a separate validation folder present in the archive?
9. Is the institutional download page operational?

## 9. Conclusion

**Source verification status: COMPLETED**

The official Zenodo record, associated research paper and GitHub repository identify NWRD as a publicly listed 100-image wheat stripe rust segmentation dataset with JPG RGB images and PNG binary masks.

**Licence status: NOT VERIFIED**

The Zenodo record shows copyright information but does not clearly specify the dataset licence. Author clarification is required before confirming reuse permissions.

**Inventory status: PARTIALLY VERIFIED**

The documented folder structure and file formats are available from the GitHub README. Actual archive-level file counts and image-mask pairing have not been inspected.

## 10. Restrictions Followed

- The 608.9 MB archive was not downloaded.
- No original dataset files were modified or deleted.
- No preprocessing was performed.
- No machine learning model was trained.
- No datasets were merged.

## 11. Sources

1. Zenodo official dataset record: https://zenodo.org/records/21672928
2. Research paper: https://pmc.ncbi.nlm.nih.gov/articles/PMC10422341/
3. Official GitHub repository README: https://github.com/dll-ncai/NUST-Wheat-Rust-Disease-NWRD/blob/main/README.md
4. NUST institutional downloads page: https://dll.seecs.nust.edu.pk/downloads/

**End of report.**