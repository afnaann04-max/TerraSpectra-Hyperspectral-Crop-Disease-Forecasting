# TerraSpectra Dataset Inventory Status

**Date:** 14 November 2026

## 1. Dataset inventory

| Dataset | Modality | Local status | Findings |
|---|---|---|---|
| Wheat Septoria | VNIR | Available | Four raw scans, four headers, four preview images and ten leaf annotation CSVs. |
| Wheat Septoria | SWIR | Partially available | SWIR metadata file found; raw SWIR scans not located. |
| NWRD Wheat Rust | RGB | Not located | No matching dataset files found in the project. |
| CCMT Tomato | RGB | Not located | No matching dataset files found in the project. |
| Rice Sheath Blight | RGB | Not located | No matching dataset files found in the project. |

## 2. Verified VNIR files

Location: `data/raw/VNIR/20210311/`

- Four hyperspectral raw files (`.hyspex`)
- Four header files (`.hdr`)
- Four preview images (`.jpg`)
- Ten leaf annotation files (`.csv`)

The four raw hyperspectral files are approximately 581.35 MB each.

## 3. SWIR findings

- Metadata file: `data/metadata/SWIR_data.csv`
- File format uses semicolon-separated data and includes explanatory notes.
- Raw SWIR files were not found in the project search.
- SWIR raw-data availability requires further confirmation.

## 4. RGB findings

No matching files for the three planned RGB datasets were found in the project search.

Their availability from other team members has not yet been confirmed.

## 5. Important limitations

1. The complete availability of all five dataset components has not been established.
2. The current VNIR work covers four selected scans, not necessarily the complete original VNIR collection.
3. SWIR and RGB processing cannot begin until their raw data and metadata are obtained and verified.
4. Dataset compatibility must be assessed before attempting multimodal fusion.

## 6. Next actions

1. Confirm whether team members possess SWIR and RGB datasets.
2. Complete the remaining VNIR missing-value and sensor-calibration assessments.
3. Assess class imbalance and determine whether additional independent samples are needed.
4. Establish whether temporal forecasting is supported by the available data.
5. Assess VNIR, SWIR and RGB compatibility for possible integration.
6. Update this report when additional datasets and evidence are verified.

## 7. Status interpretation

"Not located" means the files were not found in the searched local project folders. It does not prove that the datasets are unavailable elsewhere.
