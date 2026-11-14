
# TerraSpectra – Dataset Inventory Checklist

## 1. Purpose

This document tracks the availability, structure, metadata,
labels and preprocessing status of the datasets required
for the TerraSpectra project.

The purpose is to verify dataset readiness before
machine-learning development.

## 2. Dataset Inventory

| Dataset | Modality | Crop | Disease |
|---|---|---|---|
| VNIR | Hyperspectral | Wheat | Septoria |
| SWIR | Hyperspectral | Wheat | Septoria |
| NWRD | RGB | Wheat | Wheat Rust |
| CCMT | RGB | Tomato | Multiple classes |
| Rice Sheath Blight | RGB | Rice | Sheath Blight |

## 3. Verification Checklist

For each dataset, verify the following:

- [ ] Dataset source and download link recorded
- [ ] Raw files available
- [ ] File formats identified
- [ ] Dataset dimensions checked
- [ ] Metadata inspected
- [ ] Disease labels verified
- [ ] Class distribution examined
- [ ] Missing or invalid data investigated
- [ ] Sample identities checked
- [ ] Preprocessing requirements documented

## 4. Dataset-Specific Status

### 4.1 VNIR – Wheat Hyperspectral

Previously completed:
- Four selected scans investigated.
- Ten leaf annotation files examined.
- Baseline and candidate feature datasets compared.
- Coordinate alignment verified.
- Missing-value behaviour investigated.

Pending:
- [ ] Confirm raw and processed data availability.
- [ ] Verify biological sample independence.
- [ ] Investigate scan-treatment confounding.
- [ ] Review calibration and normalization requirements.

### 4.2 SWIR – Wheat Hyperspectral

- [ ] Confirm dataset download.
- [ ] Identify raw file formats.
- [ ] Inspect metadata and annotations.
- [ ] Verify sample identities.
- [ ] Assess data quality.

### 4.3 NWRD – Wheat RGB

- [ ] Confirm dataset availability.
- [ ] Inspect image formats and dimensions.
- [ ] Verify disease categories.
- [ ] Check image quality.
- [ ] Examine class distribution.

### 4.4 CCMT – Tomato RGB

- [ ] Confirm dataset availability.
- [ ] Inspect image formats and dimensions.
- [ ] Verify disease categories.
- [ ] Check image quality.
- [ ] Examine class distribution.

### 4.5 Rice Sheath Blight – RGB

- [ ] Confirm dataset availability.
- [ ] Inspect image formats and dimensions.
- [ ] Verify disease annotations.
- [ ] Check image quality.
- [ ] Examine class distribution.

## 5. Dataset Compatibility Considerations

VNIR, SWIR and RGB data have different measurement
characteristics.

Before attempting integration, investigate:

- Crop and disease compatibility.
- Sample identity and biological relationships.
- Acquisition conditions.
- Label consistency.
- Availability of paired observations.

Separate preprocessing and modelling pipelines should
be maintained unless compatibility is established.

## 6. Inventory Summary

| Dataset | Availability | Verification |
|---|---|---|
| VNIR | Previously investigated | Further checks pending |
| SWIR | To be confirmed | Pending |
| NWRD | To be confirmed | Pending |
| CCMT | To be confirmed | Pending |
| Rice Sheath Blight | To be confirmed | Pending |

Note: "To be confirmed" does not mean the dataset is
unavailable. The responsible team member must verify it.

## 7. Completion Criteria

The inventory will be considered complete when:

1. All five dataset components have been checked.
2. Raw data and metadata availability are documented.
3. Labels and sample identities are verified.
4. Data-quality concerns are recorded.
5. Dataset-specific preprocessing requirements are identified.

## 8. Current Status

Status: Dataset inventory checklist prepared.

Actual dataset verification is still in progress.
No model-training readiness is claimed at this stage.
