# TerraSpectra – Hyperspectral Crop Disease Forecasting

## 1. Project Overview

**Project Name:** TerraSpectra – Hyperspectral Crop Disease Forecasting  
**Organization:** Infotact Solutions  
**Internship Domain:** Data Science and Machine Learning  
**Specialization:** Computer Vision  
**Project Duration:** 1 Month  
**Start Date:** 10 November 2026  
**End Date:** 10 December 2026  
**Team Size:** 4 Members

TerraSpectra is an AI-powered agricultural intelligence project that aims to identify early signs of crop disease using hyperspectral imaging and Machine Learning.

Unlike conventional RGB images, hyperspectral images capture information across multiple wavelengths of light. These spectral measurements can reveal changes in plant properties that may not be visible to the human eye.

The project will investigate spectral patterns associated with healthy and infected wheat leaves and develop machine learning models for disease identification and early disease progression analysis.

## 2. Problem Statement

Crop diseases can negatively affect agricultural productivity and crop quality. Conventional visual inspection may fail to identify early infection when symptoms are not yet clearly visible.

Hyperspectral imaging provides an opportunity to analyse plant reflectance across multiple wavelengths. Machine Learning techniques can use these spectral patterns to distinguish healthy and infected plant samples.

**Main problem:**

How can hyperspectral imaging and Machine Learning be used to identify early signs of crop disease and analyse disease progression?

## 3. Project Objectives

1. Understand hyperspectral imaging and its applications in agriculture.
2. Collect and study a suitable hyperspectral crop disease dataset.
3. Preprocess and analyse hyperspectral data.
4. Identify spectral differences between healthy and infected samples.
5. Extract relevant spectral features.
6. Develop and compare Machine Learning and Deep Learning models.
7. Evaluate model performance using appropriate metrics.
8. Develop an interactive dashboard to demonstrate model predictions.
9. Document the complete methodology, results and findings.

## 4. Selected Dataset

**Proposed Primary Dataset:** Wheat Septoria Hyperspectral Dataset.

**Official Source:** https://doi.org/10.57745/WVP0FJ

The dataset contains hyperspectral observations of durum wheat leaves associated with Septoria tritici blotch disease.

### Dataset Characteristics

| Property | Details |
|---|---|
| Crop | Durum wheat |
| Disease | Septoria tritici blotch |
| Plant genotypes | 2 |
| Leaf samples | 3,326 |
| Observation dates | 18 |
| Observation period | One day before inoculation to 20 days after |
| Healthy samples | Included |
| Infected samples | Included |
| Imaging types | VNIR and SWIR |
| VNIR images | 1,175 |
| SWIR images | 1,175 |
| Licence | Etalab Open Licence 2.0 |

*Dataset statistics are based on the proposed dataset description and will be checked against the original metadata before implementation.*

### 4.1 VNIR Imaging

VNIR stands for Visible and Near-Infrared.

It captures spectral information from visible light and the near-infrared region. These measurements may help identify changes associated with plant health and disease.

### 4.2 SWIR Imaging

SWIR stands for Short-Wave Infrared.

It captures information from a different infrared wavelength region and may provide additional information about plant characteristics.

### 4.3 Dataset Validation

Before model development, the team will:

- Inspect the original dataset structure.
- Review metadata and available annotations.
- Verify image dimensions and spectral bands.
- Understand the healthy and infected labels.
- Examine observation dates and sample relationships.
- Check missing or invalid measurements.
- Determine the computational requirements.
- Identify suitable preprocessing methods.

**Dataset status:** Selected as the primary candidate, pending actual data validation.

## 5. Proposed Technology Stack

| Technology | Purpose |
|---|---|
| Python | Main programming language |
| NumPy | Numerical computations |
| Pandas | Dataset handling |
| Matplotlib | Data visualisation |
| Seaborn | Statistical visualisation |
| Spectral Python | Hyperspectral image processing |
| Rasterio | Raster data handling, if required |
| Scikit-learn | Machine Learning |
| PyTorch | Deep Learning |
| PCA | Spectral dimensionality reduction |
| FastAPI | Backend API |
| Streamlit | Interactive dashboard |
| Git and GitHub | Version control and collaboration |
| VS Code | Development environment |
| Google Colab | Optional cloud-based model training |

## 6. Proposed Machine Learning Models

The following models will be considered:

### 6.1 Random Forest
A traditional Machine Learning model that can classify healthy and infected samples using extracted spectral features.

### 6.2 Support Vector Machine (SVM)
A classification algorithm suitable for analysing high-dimensional spectral data.

### 6.3 3D Convolutional Neural Network (3D-CNN)
A Deep Learning approach that can learn spatial and spectral features from hyperspectral image data, provided the available image structure supports it.

### 6.4 Vision Transformer
An advanced architecture that may be explored if the dataset size, available computational resources and project timeline permit.

The final model will be selected based on experimental results rather than algorithm complexity.

## 7. Proposed Project Workflow

The planned system will follow these stages:

1. Dataset collection and verification.
2. Hyperspectral image loading.
3. Data preprocessing and normalization.
4. Exploratory Data Analysis.
5. Spectral signature analysis.
6. Feature extraction and dimensionality reduction.
7. Machine Learning model development.
8. Model training and validation.
9. Performance evaluation and model comparison.
10. Final model selection.
11. Dashboard development and integration.
12. Final testing and documentation.

## 8. Model Evaluation

The developed models will be evaluated using suitable classification metrics:

- Accuracy
- Precision
- Recall
- F1-score
- Confusion matrix

Additional evaluation will consider class imbalance, data leakage and validation across observation dates or independent samples.

The evaluation strategy will ensure that related observations from the same leaf or experimental unit do not unintentionally appear in both training and test sets.

## 9. Proposed System Architecture

**Input Layer:** Hyperspectral wheat images and associated metadata.

**Preprocessing Layer:** Image loading, cleaning, normalization and spectral preparation.

**Analysis Layer:** Exploratory analysis, spectral signatures and feature extraction.

**Model Layer:** Trained Machine Learning or Deep Learning classification models.

**Evaluation Layer:** Model comparison and performance assessment.

**Application Layer:** Interactive Streamlit dashboard with FastAPI integration if required.

**Output Layer:** Predicted disease status, model confidence and relevant spectral analysis.

## 10. Proposed Dashboard Features

The TerraSpectra dashboard may include:

- Project introduction and overview.
- Dataset summary.
- Hyperspectral image visualization.
- Spectral signature comparison.
- Healthy versus infected classification.
- Disease prediction results.
- Model performance metrics.
- Confusion matrix.
- Disease progression analysis across observation dates.

The final dashboard features will depend on the validated dataset and trained model capabilities.

## 11. Team Structure

The project consists of four members.

| Member | Proposed Responsibility |
|---|---|
| Fahma | Dataset research, preprocessing and project documentation |
| Afnan | Dataset handling and data pipeline |
| Hiba | Dashboard and frontend development |
| Midlaj | Machine Learning model development and evaluation |

These are initial proposed responsibilities and can be adjusted through team discussion.

All members are expected to understand the overall project and contribute to integration and testing.

## 12. Project Timeline

| Period | Planned Activities |
|---|---|
| Week 1 | Project planning, repository setup, dataset verification and EDA |
| Week 2 | Data preprocessing, spectral analysis and feature extraction |
| Week 3 | Machine Learning development, model comparison and evaluation |
| Week 4 | Dashboard integration, testing, documentation and final presentation |

**Official Project Period:** 10 November 2026 – 10 December 2026.

## 13. Expected Deliverables

1. Complete GitHub source code.
2. Dataset research and documentation.
3. Hyperspectral preprocessing pipeline.
4. Exploratory Data Analysis.
5. Spectral feature analysis.
6. Trained Machine Learning models.
7. Model evaluation results.
8. Interactive dashboard.
9. Project documentation.
10. Final project report.
11. Presentation.
12. Final project demonstration, if applicable.

## 14. Scientific Scope and Limitations

The selected dataset focuses on controlled hyperspectral observations of durum wheat leaves affected by Septoria tritici blotch.

It does not automatically provide multi-crop coverage, satellite imagery, GPS-based farm mapping or large-scale agricultural field observations.

Therefore, the initial project will focus on wheat-specific disease identification and analysis of disease progression over time.

Although early disease detection is a primary objective, actual prediction of future disease occurrence must be supported by an appropriate temporal modelling strategy and independent evaluation.

The project will not claim validated three-week-ahead farm disease forecasting unless the available data and experiments support that capability.

## 15. Version Control and Collaboration

GitHub will be used as the central platform for team collaboration.

The team will follow these practices:

- Each member works on an assigned individual branch.
- Members commit and push their own contributions.
- The main branch will be protected from premature changes.
- Changes will be reviewed before integration.
- Project documentation will be maintained throughout development.
- Progress will be recorded regularly.

## 16. Project Status

| Activity | Status |
|---|---|
| Official assignment received | Completed |
| Project objective understood | Completed |
| GitHub repository created | Completed |
| Repository connected to Project Progress | Completed |
| Project overview prepared | In progress |
| Dataset selected | Pending data validation |
| Repository structure audit | Pending |
| Dataset acquisition | Pending |
| Data preprocessing | Pending |
| EDA | Pending |
| Model development | Pending |
| Dashboard development | Pending |
| Final documentation and presentation | Pending |

## 17. Conclusion

TerraSpectra aims to explore the use of hyperspectral imaging and Machine Learning for agricultural disease identification.

By analysing spectral information from healthy and infected wheat leaves, the project will investigate how AI-based approaches can support early disease detection and disease progression analysis.

The team will follow a structured Data Science workflow, validate the dataset, develop suitable models, evaluate their performance and deliver an interactive demonstration within the one-month project period.

**Project:** TerraSpectra – Hyperspectral Crop Disease Forecasting  
**Organization:** Infotact Solutions  
**Domain:** Data Science and Machine Learning