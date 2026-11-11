
# Hyperspectral Dataset Metadata Analysis

## 1. Introduction

This document describes the initial metadata investigation
of the Wheat Septoria Hyperspectral Dataset.

The dataset is used to study spectral changes associated
with Septoria tritici blotch infection in durum wheat.

## 2. Dataset Overview

- Crop: Durum wheat
- Disease: Septoria tritici blotch
- Genotypes: EPO_67 and EPO_68
- Treatments: Inoculated and non-inoculated
- Observation period: Approximately -1 to 20 days
  post-inoculation
- Spectral ranges: VNIR and SWIR

## 3. Metadata Files

Three metadata CSV files have been identified:

1. Data_description.csv
2. VNIR_data.csv
3. SWIR_data.csv

### Data_description.csv

Purpose:
To understand the dataset description and experimental
information.

### VNIR_data.csv

Purpose:
To investigate metadata associated with Visible and
Near-Infrared acquisitions.

### SWIR_data.csv

Purpose:
To investigate metadata associated with Short-Wave
Infrared acquisitions.

## 4. Important Metadata Information

The metadata investigation identifies information
related to:

- Plant identification
- Leaf identification
- Wheat genotype
- Treatment information
- Acquisition dates
- Confidence information

Exact column names, data types and missing-value counts
must be confirmed by inspecting the original CSV files.

## 5. Research Objectives

The metadata analysis will help us:

1. Understand the experimental structure.
2. Identify healthy and inoculated samples.
3. Study observations across different dates.
4. Understand the relationship between metadata and
   hyperspectral acquisitions.
5. Prepare for spectral data preprocessing.

## 6. Pending Verification

- Inspect all metadata column names.
- Check missing values and duplicate records.
- Verify sample identification consistency.
- Map metadata records to raw hyperspectral files.
- Confirm the actual file formats.
- Inspect image dimensions and spectral bands.
- Identify a manageable subset for initial experiments.

## 7. Important Limitations

The metadata CSV files are not the actual hyperspectral
measurements.

The raw VNIR and SWIR image files must be inspected
before beginning spectral preprocessing.

## 8. Conclusion

The initial metadata investigation provides a foundation
for understanding the wheat hyperspectral dataset.

Further validation of raw image files and metadata
mapping is required before model development.
