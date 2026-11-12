# TerraSpectra – Hyperspectral Dataset Research

## 1. Introduction

Dataset research is an important stage of the TerraSpectra project. Before developing Machine Learning models, it is necessary to understand the source, structure, characteristics and limitations of the selected dataset.

The primary dataset proposed for this project is the Wheat Septoria Hyperspectral Dataset, published through Recherche Data Gouv.

The dataset contains hyperspectral observations of healthy and infected durum wheat leaves. It provides spectral information captured using Visible and Near-Infrared (VNIR) and Short-Wave Infrared (SWIR) imaging systems.

The dataset will be investigated to understand its suitability for early disease detection and disease progression analysis.

## 2. Dataset Information

**Dataset Title:** Early detection of septoria infection on wheat leaves using hyperspectral imaging data.

**Dataset Author:** Lorraine Latchoumane (INRAE).

**Publication Year:** 2024.

**Dataset Version:** Version 1.0.

**Official Repository:** Recherche Data Gouv.

**DOI:** https://doi.org/10.57745/WVP0FJ

**Associated Research Article:** Early detection of Zymoseptoria tritici infection on wheat leaves using hyperspectral imaging data.

**Article DOI:** https://doi.org/10.1016/j.dib.2025.111404

**License:** Etalab Open Licence 2.0, compatible with CC-BY 2.0.

## 3. Dataset Description

The dataset contains hyperspectral images of healthy wheat leaves and leaves infected with the fungal pathogen Zymoseptoria tritici, responsible for Septoria tritici blotch (STB).

The experiment was conducted using two durum wheat genotypes under controlled conditions.

Hyperspectral observations were collected over multiple dates to study disease development and identify spectral and spatial differences associated with infection.

The dataset is particularly relevant to TerraSpectra because it provides observations covering the period before inoculation and the subsequent development of infection.

## 4. Dataset Characteristics

| Property | Description |
|---|---|
| Crop | Durum wheat |
| Disease | Septoria tritici blotch |
| Pathogen | Zymoseptoria tritici |
| Wheat genotypes | 2 |
| Observation dates | 18 |
| Observation period | One day before inoculation to 20 days after |
| Healthy samples | Included |
| Infected samples | Included |
| Spectral imaging | VNIR and SWIR |
| VNIR images | 1,175 |
| SWIR images | 1,175 |
| Leaves measured | 3,326 per spectral range |
| Data type | Hyperspectral images and annotations |
| Image format | ENVI |
| Licence | Etalab Open Licence 2.0 |

The image and leaf counts represent the dataset's reported observations. They should not be interpreted as independent training examples without checking repeated measurements and sample relationships.

## 5. Disease Information

The dataset focuses on Septoria tritici blotch, a fungal disease affecting wheat.

The disease is caused by the pathogen Zymoseptoria tritici.

The dataset includes infected and non-infected wheat leaf observations. These observations can be used to investigate spectral differences associated with infection.

For TerraSpectra, the initial classification objective will be to distinguish healthy and infected wheat samples.

The temporal observations may also support research into changes in disease signatures over time.

## 6. Hyperspectral Imaging Types

The dataset uses two different hyperspectral imaging systems.

### 6.1 VNIR – Visible and Near-Infrared

VNIR captures spectral information in the visible and near-infrared wavelength regions.

It provides spectral information that can be investigated to identify differences between healthy and infected wheat leaves.

### 6.2 SWIR – Short-Wave Infrared

SWIR captures spectral information in the short-wave infrared region.

This provides another source of spectral information that may help identify changes associated with plant health and disease.

### 6.3 Combined Analysis

The availability of both VNIR and SWIR observations provides an opportunity to investigate the differences between the two spectral ranges.

However, combining both datasets will require checking wavelength calibration, image alignment, sample correspondence and compatible metadata.

## 7. Observation Timeline

One important characteristic of the selected dataset is its temporal structure.

Hyperspectral images were collected on 18 observation dates.

The observation period extends from one day before inoculation to 20 days after inoculation.

This makes the dataset useful for studying how spectral patterns change during the development of infection.

Potential research activities include:

- Comparing healthy and infected spectral signatures.
- Investigating spectral changes across observation dates.
- Studying differences between wheat genotypes.
- Identifying observation periods associated with early infection signatures.
- Exploring disease progression patterns.

The actual dates, sample identifiers and label definitions will be examined through the original annotation files.

## 8. Dataset File Structure

According to the associated research publication, the dataset is organized into two main sections.

### 8.1 Data Annotation

The Data annotation directory contains three CSV files:

| File | Purpose |
|---|---|
| Data_description.csv | General dataset description |
| VNIR_data.csv | VNIR sample and leaf information |
| SWIR_data.csv | SWIR sample and leaf information |

These files will be inspected to understand the metadata, image references, sample information and available annotations.

### 8.2 Hyperspectral Data

The Data directory contains two main spectral folders:

- VNIR
- SWIR

Each spectral folder contains compressed ZIP archives corresponding to the acquisition dates.

The archive names use the YYYYMMDD date format.

The compressed folders contain hyperspectral images organized into subfolders associated with plant pot numbers and measured sides.

The original hyperspectral images are stored in ENVI format.

## 9. Image Data Distribution

The published dataset description reports the following distribution:

| Spectral range | Treatment | Images | Leaves |
|---|---|---:|---:|
| VNIR | Infected | 588 | 1,652 |
| VNIR | Non-infected | 587 | 1,674 |
| VNIR | Total | 1,175 | 3,326 |
| SWIR | Infected | 588 | 1,652 |
| SWIR | Non-infected | 587 | 1,674 |
| SWIR | Total | 1,175 | 3,326 |

The reported counts will be checked against the annotation CSV files during dataset validation.

## 10. Dataset Licence and Accessibility

The dataset is available through the Recherche Data Gouv repository.

The listed licence is Etalab Open Licence 2.0, compatible with CC-BY 2.0.

The repository provides public access to dataset files.

However, the complete dataset is large and should not be downloaded without first examining the available file sizes and selecting the files required for initial experimentation.

The annotation CSV files are comparatively small and will be examined before downloading the larger hyperspectral image archives.

Proper attribution to the original dataset authors will be maintained in project documentation and final reports.

## 11. Suitability for TerraSpectra

The selected dataset is relevant to the project for the following reasons:

1. It contains actual hyperspectral imaging observations.
2. It includes healthy and infected wheat samples.
3. It covers two durum wheat genotypes.
4. It provides VNIR and SWIR observations.
5. It contains multiple observation dates.
6. It provides information about disease development after inoculation.
7. It can support hyperspectral image analysis and classification experiments.

The dataset provides a suitable starting point for wheat-specific disease identification and early infection research.

Its temporal observations may also support carefully designed disease progression experiments.

## 12. Dataset Limitations and Considerations

The following limitations must be considered before model development:

### 12.1 Single Crop

The dataset focuses on durum wheat and does not provide multiple crop species.

Therefore, the initial system will focus on wheat-specific disease identification rather than multi-crop disease classification.

### 12.2 Single Disease

The dataset focuses on Septoria tritici blotch.

It does not provide a comprehensive collection of different wheat diseases.

### 12.3 Controlled Experimental Conditions

The observations were collected under controlled experimental conditions.

Performance on field-collected images and different environmental conditions cannot be assumed.

### 12.4 Large Dataset Size

The hyperspectral image archives are large.

Selective downloading, storage planning and computational resource assessment will be necessary.

### 12.5 Repeated Observations

The dataset contains observations across multiple dates.

Related measurements from the same leaf or experimental unit must be handled carefully when dividing data into training, validation and testing sets.

### 12.6 Forecasting Limitations

The dataset supports disease monitoring and investigation of infection-related spectral changes.

However, classification of existing infection and prediction of future disease occurrence are different tasks.

A forecasting model will require a clearly defined prediction target, suitable temporal features and independent evaluation.

The project will not claim future disease forecasting without experimental evidence.

## 13. Planned Dataset Validation Activities

Before beginning model development, the following activities will be performed:

1. Access the official dataset repository.
2. Download and inspect the annotation CSV files.
3. Understand the columns and metadata.
4. Verify image references and sample identifiers.
5. Examine observation dates.
6. Check infected and non-infected sample distributions.
7. Inspect available VNIR and SWIR files.
8. Verify image dimensions and spectral information.
9. Identify missing or invalid observations.
10. Assess storage and processing requirements.

## 14. Planned Applications in TerraSpectra

After successful dataset validation and preprocessing, the dataset may be used for:

- Hyperspectral image visualization.
- Healthy and infected sample comparison.
- Spectral signature analysis.
- Feature extraction.
- Dimensionality reduction.
- Disease classification.
- Temporal disease progression analysis.
- Machine Learning model evaluation.

The final experiments will depend on the actual dataset structure and the information available in its annotations.

## 15. References

1. Latchoumane, L. (2024). Early detection of septoria infection on wheat leaves using hyperspectral imaging data. Recherche Data Gouv.

   https://doi.org/10.57745/WVP0FJ

2. Latchoumane, L. et al. (2025). Early detection of Zymoseptoria tritici infection on wheat leaves using hyperspectral imaging data. Data in Brief, 59, 111404.

   https://doi.org/10.1016/j.dib.2025.111404

3. Dataset repository:

   https://entrepot.recherche.data.gouv.fr/dataset.xhtml?persistentId=doi%3A10.57745%2FWVP0FJ

---

**Project:** TerraSpectra – Hyperspectral Crop Disease Forecasting  
**Organization:** Infotact Solutions  
**Domain:** Data Science and Machine Learning  
**Documentation:** Dataset Research  
**Status:** Initial dataset research completed; actual metadata and file validation pending.