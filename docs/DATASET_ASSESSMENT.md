
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
## SWIR Scan Quality Investigation � 01_D

### 1. Zero-value readings
- 527 zero readings were identified across the 256 spectral bands.
- Zero readings occurred in 80 bands.
- Their spatial distribution was more dispersed than the saturation patterns.

### 2. Saturated readings
- 3,577 readings had the maximum value of 65,535.
- Saturation occurred in 9 spectral bands.
- The affected pixels were concentrated in 13 spatial columns.

### 3. Spatial comparison
- 493 spatial pixels contained at least one zero reading.
- 3,577 spatial pixels contained at least one saturated reading.
- 39 pixels contained both zero and saturated readings.
- Saturation showed a strong column-localised pattern.

### 4. Leaf-region comparison
For sample 01_D, the CSV contains 3,846 selected coordinates.

Using the proposed CSV-to-raw mapping:
- Selected region: 1 zero reading and 0 saturated readings.
- Remaining scan: 526 zero readings and 3,577 saturated readings.
- Selected-region mean intensity: 1,537.47.
- Remaining-scan mean intensity: 1,538.63.

### 5. Interpretation and limitations
The selected region contains very few zero readings and no saturated readings, while the remaining scan contains most of the identified anomalies.

The saturation pattern may indicate column-localised acquisition or sensor artefacts. However, the exact cause has not been established.

The CSV coordinate convention was identified from the dataset documentation. The exact spatial alignment between the reconstructed JPG and raw SWIR scan has not yet been independently confirmed. Therefore, the leaf-region comparison is provisional.

These findings apply to the inspected 01_D scan and should not be generalised to the entire dataset without further inspection.

## Task 2 � Leaf and Remaining-Scan Spectral Signature Analysis

### 1. Spectral comparison

The mean spectral signatures were calculated using 256 wavelength bands from the SWIR scan `01_D.hyspex`.

The mean leaf-region spectrum was compared with the mean spectrum of the remaining scan region. A comparison graph was generated and saved as:

`01_D_spectral_comparison.png`

The numerical mean signatures were saved as:

`01_D_mean_spectral_signatures.csv`

### 2. Observations

- Total wavelengths analysed: 256.
- Leaf-region mean was higher at 136 wavelengths.
- Remaining-scan mean was higher at 120 wavelengths.
- Largest absolute difference: approximately 320.52 intensity units at 1486.25 nm.
- Leaf-region maximum mean intensity: 2392.58.
- Remaining-scan maximum mean intensity: 2557.50.

At 1486.25 nm, the leaf-region mean was 1781.80, while the remaining-scan mean was 2102.32.

### 3. Interpretation

The two regions show differences in their average spectral intensity patterns across the measured wavelength range. The direction and magnitude of the differences vary across wavelengths.

These observations demonstrate spectral variation within the scan. However, they do not establish a disease-related spectral signature.

### 4. Limitations

- The spatial alignment of the leaf-coordinate CSV with the raw SWIR scan has not been independently confirmed.
- The remaining scan region is not a verified background-only region.
- The analysis uses one scan and does not establish general patterns across plants or samples.
- Further validation with confirmed spatial alignment and additional samples is required before drawing biological or disease-related conclusions.


## Task 3 - Raw SWIR File and Metadata Matching

### 1. Official SWIR Archive

The official SWIR archive `20210311.zip` was downloaded successfully.

- Archive size: approximately 4.60 GB
- Total raw SWIR scans: 96
- Unique pot-side scan identities: 96
- Expected scans: 96

### 2. Archive Completeness Check

The archive was checked against all 48 pot IDs and their two sides (G and D).

- Duplicate scan identities: 0
- Missing scan identities: 0
- Unexpected scan identities: 0

All 96 expected pot-side scan identities were found.

One folder organisation inconsistency was identified: `18_D` files are stored inside the `18_G` directory. The scan filename is correct, and filename-based matching confirms that no scan is missing.

### 3. Metadata Matching

The SWIR metadata contains 48 pot records.

All 96 raw scan identities matched the expected pot-side identities derived from the metadata.

Sample metadata checks:

- Pot 01: EPO_68, Infected
- Pot 18: EPO_68, Non-infected
- Pot 48: EPO_67, Non-infected

No unmatched or missing scan identities were found.

### 4. Header Information

The inspected sample `01_D.hyspex` has the following properties:

- Acquisition date: 2021-03-11
- Acquisition start time: 08:53:43
- Sensor: SWIR_320me
- Dimensions: 420 lines x 256 bands x 320 samples
- Data format: BIL

### 5. Acquisition Date and DPI

The header confirms the calendar acquisition date but does not contain a DPI value.

The available research information does not establish the calendar inoculation date. Therefore, the exact DPI of the inspected sample remains unverified.

### 6. Limitations and Conclusion

The official archive inventory and filename-based matching against all 48 metadata pot records are complete.

The archive contains all 96 expected raw scans, with one folder-naming inconsistency involving `18_D`.

The exact DPI of the inspected sample remains unverified. Filename-based matching confirms pot-side identities, while the genotype and treatment information are taken from the corresponding pot records.


## Task 4 - Initial SWIR Spectral Analysis

### 1. Representative scans

Four representative D-side scans were selected for an initial comparison:

| Genotype | Treatment | Scan |
|---|---|---|
| EPO_67 | Infected | 07_D |
| EPO_67 | Non-infected | 10_D |
| EPO_68 | Infected | 01_D |
| EPO_68 | Non-infected | 04_D |

### 2. Spectral extraction

- Each scan contains 420 lines, 320 samples and 256 spectral bands.
- Mean intensity was calculated for each wavelength across the complete scan.
- The common wavelength range is approximately 964.18 to 2494.39 nm.
- Extracted results were saved in `TerraSpectra_four_scan_mean_spectra.csv`.

### 3. Initial comparison

| Genotype | Infected mean | Control mean | Difference (infected - control) |
|---|---:|---:|---:|
| EPO_67 | 1501.67 | 1511.01 | -9.35 |
| EPO_68 | 1538.60 | 1553.00 | -14.40 |

- For EPO_67, the control scan had higher intensity at 183 of 256 wavelengths.
- For EPO_68, the control scan had higher intensity at 177 of 256 wavelengths.
- The largest absolute difference occurred at 1942.31 nm for EPO_67 and 1504.25 nm for EPO_68.

### 4. Interpretation and limitations

Both selected infected scans had lower whole-scan mean intensity than their corresponding non-infected scans. This is an exploratory observation only.

The comparison uses one scan per genotype-treatment group. The calculated means include all scan pixels, not only leaf pixels. Differences may also reflect individual plant variation, scan conditions or other factors.

Therefore, these results do not establish a disease-specific spectral signature or prove that infection causes lower intensity. Further analysis using multiple plants, appropriate leaf regions and statistical testing is required.

### 5. Output files

- Mean spectral data: `TerraSpectra_four_scan_mean_spectra.csv`
- Comparison graph: `TerraSpectra_four_scan_spectral_comparison.png`



## Task 5 - VNIR Leaf-Level Spectral Analysis and Sensor Comparison

### 1. Representative VNIR scans

The same four representative D-side scans used in the initial SWIR analysis were selected:

| Genotype | Treatment | Scan |
|---|---|---|
| EPO_67 | Infected | 07_D |
| EPO_67 | Non-infected | 10_D |
| EPO_68 | Infected | 01_D |
| EPO_68 | Non-infected | 04_D |

### 2. Leaf annotation validation

- Ten leaf annotation CSV files were inspected across the four scans.
- The annotation files contain individual pixel coordinates.
- All annotated coordinates were within the VNIR image dimensions.
- No duplicate coordinates were found.
- The annotations cover 2 or 3 leaves per selected scan.

### 3. VNIR spectral extraction

- Each selected VNIR scan contains 1370 lines, 1024 samples and 216 spectral bands.
- The binary files were verified against their expected dimensions and file sizes.
- Mean spectral intensity was calculated using the annotated pixels of each leaf.
- Ten leaf-level mean spectra were extracted successfully.
- The VNIR wavelength range is approximately 411.36 to 993.17 nm.
- All extracted values are finite, and wavelengths are in increasing order.

### 4. VNIR outputs

- Leaf-level mean spectra: `data/processed/VNIR_leaf_mean_spectra.csv`
- Leaf spectral comparison graph: `data/processed/VNIR_leaf_spectral_comparison.png`

### 5. VNIR and SWIR spectral coverage

- VNIR covers approximately 411.36 to 993.17 nm across 216 bands.
- SWIR covers approximately 964.18 to 2494.39 nm across 256 bands.
- The two sensors have a narrow overlapping wavelength region of approximately 964.18 to 993.17 nm.
- Their spectral coverage is complementary, but their sensor characteristics and spatial dimensions differ.

### 6. Comparison limitations

VNIR leaf-level spectra and the previously calculated SWIR whole-scan mean spectra are not directly equivalent measurements. The SWIR leaf annotation files were not available in the inspected project data, so a matching leaf-level comparison could not be completed.

The current analysis is exploratory and uses only four representative scans. It does not establish a disease-specific spectral signature or demonstrate classification performance. Further work should use appropriately matched leaf regions, more samples and careful validation before combining data from the two sensors.

