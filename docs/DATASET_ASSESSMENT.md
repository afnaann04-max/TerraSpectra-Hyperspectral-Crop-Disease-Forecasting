
# TerraSpectra
## Dataset Assessment

### 1. Purpose

This document records the datasets proposed for the TerraSpectra project. Each dataset will be checked for availability, image quality, labels, file formats, licence and suitability before model development.

### 2. Proposed Dataset Summary

| Crop | Dataset | Data Type | Intended Use | Status |
|---|---|---|---|---|
| Wheat | NWRD | Real-world RGB field images | Wheat disease detection and segmentation | Proposed |
| Tomato | CCMT | Real-world RGB images | Tomato disease classification | Proposed |
| Rice | Rice sheath blight dataset | Field RGB images | Rice disease classification | Pending verification |
| Wheat | Septoria hyperspectral dataset | VNIR and SWIR hyperspectral images | Spectral analysis and early disease detection | Metadata reviewed |

### 3. Wheat – NWRD Dataset

**Data type:** Real-world RGB field images.

**Proposed use:**
- Identify visible wheat disease symptoms.
- Investigate disease-region segmentation using available annotations.
- Evaluate performance under field image conditions.

**Verification required:**
- Confirm image download and access.
- Inspect image formats and dimensions.
- Verify disease classes and annotations.
- Check dataset licence.

### 4. Tomato – CCMT Dataset

**Data type:** RGB crop images.

**Proposed use:**
- Classify healthy and diseased tomato leaves.
- Evaluate performance across the available disease classes.

**Verification required:**
- Confirm access to original images.
- Inspect class distribution.
- Check image quality and duplicates.
- Verify licence and dataset documentation.

### 5. Rice – Sheath Blight Dataset

**Data type:** Proposed real-world RGB field images.

**Proposed use:**
- Investigate rice sheath blight symptoms.
- Develop a crop-specific disease classification model if the dataset is suitable.

**Verification required:**
- Confirm actual field image availability.
- Inspect healthy and diseased labels.
- Check image quality, sample count and licence.

### 6. Wheat – Septoria Hyperspectral Dataset

**Source:** Recherche Data Gouv

**DOI:** 10.57745/WVP0FJ

**Data type:** Laboratory hyperspectral images.

**Available spectral ranges:**
- VNIR – Visible and Near-Infrared.
- SWIR – Short-Wave Infrared.

**Metadata reviewed:**
- Data_description.csv
- VNIR_data.csv
- SWIR_data.csv

**Dataset characteristics:**
- Durum wheat.
- Genotypes EPO_67 and EPO_68.
- Inoculated and non-inoculated plants.
- Measurements from -1 to 20 days post-inoculation.

**Proposed use:**
- Analyse spectral differences between control and inoculated plants.
- Investigate early disease-related spectral changes.
- Develop and evaluate a hyperspectral classification model.

**Verification still required:**
- Inspect the contents of the actual ZIP archives.
- Identify image formats and spectral metadata.
- Match image files with CSV records.
- Confirm sample counts and usable labels.
- Select a manageable subset for initial experiments.

### 7. Dataset Handling Strategy

- Keep RGB and hyperspectral data in separate processing pipelines.
- Do not combine incompatible spectral measurements.
- Preserve original labels and metadata.
- Check for duplicate images and data leakage.
- Split data appropriately for training, validation and testing.
- Record dataset sources and licences.

### 8. Dataset Approval Status

| Dataset | Current Status |
|---|---|
| Wheat NWRD | Proposed – verification pending |
| Tomato CCMT | Proposed – verification pending |
| Rice sheath blight | Pending verification |
| Wheat Septoria hyperspectral | Metadata reviewed – image inspection pending |

### 9. Important Limitations

The wheat hyperspectral dataset was collected under controlled laboratory conditions. Its results cannot automatically be generalised to real-world farm environments.

The RGB and hyperspectral models will be developed and evaluated separately. Claims about early prediction or field-scale forecasting will depend on experimental evidence.

### 10. SWIR Archive Inspection – 12 November 2026

The online ZIP preview of `20210311.zip` was inspected without downloading the complete archive.

**Identified file structure:**

Files are organised by pot number and leaf side (D and G). The inspected entries include:

- `.hdr` – Hyperspectral image header and acquisition metadata.
- `.hyspex` – Raw hyperspectral measurements.
- `.jpg` – Visual image associated with the scan.
- `_leaf1.csv`, `_leaf2.csv`, `_leaf3.csv` – Files containing integer coordinate pairs, potentially identifying leaf regions.

**Verified details from `01_D.hdr`:**

| Property | Value |
|---|---|
| Dimensions | 420 × 320 pixels |
| Spectral bands | 256 |
| Spectral range | 964–2494 nm |
| Wavelength unit | nm |
| Data type | Unsigned 16-bit integer |
| Interleave | BIL |
| Acquisition date | 11 March 2021 |
| Header offset | 1,974,272 bytes |
| Ignore value | 16383 |

**Pending verification:**

- Confirm the relationship between archive pot numbers and metadata pot identifiers.
- Verify the coordinate CSV files against their corresponding JPG images.
- Test reading the raw `.hyspex` measurements.
- Confirm the usable sample count and file mapping.

**Storage status:**

- Only three metadata CSV files have been downloaded.
- No raw hyperspectral archives have been downloaded.
- Available C: drive space: approximately 60.70 GB.
- Large-scale downloading is postponed until sample selection and storage requirements are confirmed.