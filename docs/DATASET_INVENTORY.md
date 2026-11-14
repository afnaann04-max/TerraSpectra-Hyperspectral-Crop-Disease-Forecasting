# TerraSpectra — Dataset Inventory

**Status:** Initial repository-level inventory
**Date:** 14 November 2026

## 1. Project dataset overview

The project investigates VNIR, SWIR and RGB data for crop disease detection.
Dataset availability must be verified before combining modalities or starting
model training.

## 2. VNIR — Wheat Septoria

**Status: Available in repository**

- Raw scan folders are present under `data/raw/VNIR/20210311/`.
- Four scan folders: `01_D`, `04_D`, `07_D`, and `10_D`.
- Ten leaf-level CSV files have been matched to the available metadata.
- Four scan files and their associated metadata are available.
- The validated feature datasets contain 272,912 pixel observations.
- Spectral coverage: 216 bands, approximately 411–993 nm.
- Corrected NPZ outputs have been numerically audited and are maintained locally.

**Limitations:**
- Only four pot IDs are represented in the selected scans.
- Biological replication and repeated-measurement structure require further investigation.
- Pixels must not be treated as independent biological samples.
- The original corrected-NPZ generation script provenance has not been confirmed.

## 3. SWIR — Wheat Septoria

**Status: Metadata found; raw data not confirmed in repository**

- SWIR sampling metadata is available.
- The metadata describes leaf counts by pot and sampling date.
- Raw SWIR spectral measurements have not been located in the repository.

**Next requirement:** Obtain the raw SWIR data and verify its acquisition files,
spectral dimensions, sample identities and quality.

## 4. RGB datasets

The following datasets are required for the RGB component:

| Dataset | Intended crop/disease | Repository status |
|---|---|---|
| NWRD | Wheat Rust | Not found |
| CCMT | Tomato diseases | Not found |
| Rice Sheath Blight | Rice disease | Not found |

The repository image-file inspection found images inside the VNIR scan folders.
These are not sufficient evidence that the required independent RGB datasets
are available.

**Next requirement:** Obtain each RGB dataset and verify its images, labels,
annotations, sample counts and class distribution.

## 5. Current availability summary

| Modality | Dataset | Current finding |
|---|---|---|
| VNIR | Wheat Septoria | Available and investigated |
| SWIR | Wheat Septoria | Metadata only; raw data unconfirmed |
| RGB | NWRD Wheat Rust | Not found |
| RGB | CCMT Tomato | Not found |
| RGB | Rice Sheath Blight | Not found |

## 6. Scientific and project considerations

1. Do not combine modalities until their sample identities and acquisition
   conditions are understood.
2. Do not assume that VNIR and SWIR metadata proves that both raw modalities
   are available.
3. Investigate biological replication and possible pot-level confounding.
4. Avoid pixel-level random train/test splitting because pixels from the same
   leaf or scan may be highly correlated.
5. Begin model development only after dataset readiness and experimental
   design have been assessed.

## 7. Next actions

- Complete VNIR biological replication investigation.
- Investigate scan and disease-treatment confounding.
- Obtain and audit raw SWIR data.
- Obtain and audit the three required RGB datasets.
- Define a leakage-resistant experimental design before model training.
