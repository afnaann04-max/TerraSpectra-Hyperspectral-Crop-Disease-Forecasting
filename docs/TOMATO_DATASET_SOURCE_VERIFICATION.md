# CCMT Tomato Dataset — Source Verification Report

**Project:** TerraSpectra – Hyperspectral Crop Disease Forecasting
**Assigned responsibility:** Member 3 – RGB Dataset Investigation
**Investigation date:** 18 November 2026
**Dataset:** CCMT – Dataset for Crop Pest and Disease Detection
**Crop investigated:** Tomato
**Status:** Initial source verification completed; archive-level verification pending

---

## 1. Dataset Identification

- **Dataset name:** Dataset for Crop Pest and Disease Detection (CCMT)
- **Official source:** Mendeley Data
- **DOI:** `10.17632/bwh3zbpkpv.1`
- **Dataset URL:** https://data.mendeley.com/datasets/bwh3zbpkpv/1
- **Publication:** CCMT: Dataset for Crop Pest and Disease Detection
- **Publication DOI:** https://doi.org/10.1016/j.dib.2023.109306
- **Publication platform:** Data in Brief
- **Publication date:** 2023

The dataset contains images from four crops: cashew, cassava, maize and tomato. This investigation focuses only on the tomato subset.

## 2. Source and Availability

The dataset is publicly listed on Mendeley Data.

The publication and dataset record provide information about the dataset and its availability. The record provides access to the dataset files.

**Access status:** Publicly listed dataset.

**Download status:** Not downloaded.

**Important:** No archive has been downloaded or extracted during this investigation. Therefore, the actual downloaded file structure, file counts, image integrity and annotation mapping have not been independently verified.

## 3. Dataset Licence

The Mendeley Data record lists the dataset licence as **Creative Commons Attribution 4.0 International (CC BY 4.0)**.

Licence reference: https://creativecommons.org/licenses/by/4.0/

The licence permits sharing and adaptation subject to its conditions, including appropriate attribution and indicating whether changes were made.

The dataset licence should be followed when reusing or adapting the data. The publication licence and dataset licence should not be treated as interchangeable.

## 4. Reported Image Counts

According to the dataset description and publication:

| Dataset portion | Reported image count |
|---|---:|
| Tomato raw images | 5,435 |
| Tomato augmented images | 27,178 |

These are published figures, not independently verified archive counts.

The full CCMT dataset covers four crops and reports 24,881 raw images and 102,976 augmented images across the dataset.

The tomato subset must be kept separate from the other crop datasets during investigation.

## 5. Tomato Disease Classes

The publication reports five tomato image classes:

1. Healthy
2. Leaf blight
3. Leaf curl
4. Septoria leaf spot
5. Verticillium wilt

### Reported raw tomato class distribution

| Class | Reported image count |
|---|---:|
| Healthy | 500 |
| Leaf blight | 1,301 |
| Leaf curl | 518 |
| Septoria leaf spot | 2,343 |
| Verticillium wilt | 773 |
| **Total** | **5,435** |

The counts above are taken from the publication's reported class distribution. They have not been independently checked against the archive.

## 6. Annotation Format

The publication describes the dataset as labelled images organised according to crop and disease classes.

The described labelling process involved plant virologists and pathologists, followed by expert review and consensus.

The available source information supports **image-level class labels**.

The reviewed source information does not establish that the tomato subset contains:
- Bounding-box annotations
- Pixel-level segmentation masks
- A separate segmentation annotation file

The exact annotation-file format and image-to-label mapping remain to be verified from the actual files.

## 7. Image Acquisition Conditions

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

## 8. Folder Structure

The publication describes raw and augmented data organised by crop and disease class.

The previously observed folder structure indicates a tomato directory containing five class folders.

However, the complete archive hierarchy has not been inspected.

The following details remain pending:
- Exact raw folder and file names
- Exact augmented folder and file names
- Number of images in each extracted class folder
- Whether every image has a corresponding label entry
- Presence and format of any separate annotation files
- Whether augmented images can be distinguished from original images by filename or metadata

No archive-level folder structure or file count is claimed as verified.

## 9. Dataset Relevance to TerraSpectra

The CCMT tomato subset may be useful as an RGB image-classification candidate because it contains images grouped into five reported tomato health/disease categories.

However, the dataset is not yet approved for modelling.

Before selection, the following need to be evaluated:
- Actual number of usable original images
- Class distribution after file-level verification
- Availability and consistency of image-level labels
- Duplicate or near-duplicate images
- Differences between original and augmented images
- Suitability of the image acquisition conditions for the intended project
- Licence and attribution requirements

The dataset should remain separate from the NWRD Wheat Rust and Rice Sheath Blight datasets.

## 10. Verified, Reported and Unresolved Information

### A. Verified from public source records

- Dataset record is available on Mendeley Data.
- Dataset DOI is `10.17632/bwh3zbpkpv.1`.
- The dataset covers four crops, including tomato.
- The Mendeley record lists CC BY 4.0.

### B. Reported by the publication or dataset description

- 5,435 raw tomato images.
- 27,178 augmented tomato images.
- Five tomato classes.
- Class-wise raw image counts listed in this report.
- JPEG image format.
- Canon EOS Rebel T7 camera and EF-A 18–55 mm lens.
- Collection in Ghana during October–December 2022.
- Expert image-labelling and review process.

These details are source-reported and have not been independently verified against the archive.

### C. Unresolved

- Actual archive-level image counts.
- Exact extracted folder structure.
- Exact annotation-file format.
- Whether any additional annotation files are supplied.
- Image-to-label mapping at file level.
- Exact image dimensions for every image.
- Duplicate and image-integrity status.
- Exact metadata availability for individual images.

## 11. Restrictions and Investigation Notes

- No dataset archive was downloaded.
- No original files were modified or deleted.
- No preprocessing or augmentation was performed.
- No model training was performed.
- The dataset has not been approved for modelling.
- Published counts must not be described as independently verified file counts.

## 12. References

1. Mendeley Data – Dataset for Crop Pest and Disease Detection:
   https://data.mendeley.com/datasets/bwh3zbpkpv/1

2. Dataset DOI:
   https://doi.org/10.17632/bwh3zbpkpv.1

3. Research publication – Data in Brief:
   https://doi.org/10.1016/j.dib.2023.109306

4. Creative Commons Attribution 4.0 International:
   https://creativecommons.org/licenses/by/4.0/

**Investigation date:** 18 November 2026
**Prepared by:** Member 3 – RGB Dataset Investigation
**Final status:** Public source verification completed; archive-level verification pending.
