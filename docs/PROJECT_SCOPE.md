# TerraSpectra
## Project Scope

### 1. Project Overview

TerraSpectra is a crop disease detection and spectral analysis system that uses real-world RGB crop images and laboratory-collected hyperspectral data.

The project aims to identify visible crop disease symptoms from field images and investigate spectral changes associated with disease development using hyperspectral wheat measurements.

The project will use separate processing and modelling pipelines for RGB and hyperspectral datasets. Any attempt to combine these modalities will require scientific justification and compatibility assessment.

### 2. Project Objectives

- Develop machine learning models for crop disease classification using verified RGB field-image datasets.
- Investigate disease-associated spectral differences using laboratory-collected wheat hyperspectral data.
- Explore whether suitable temporal measurements support the investigation of early disease-related spectral changes.
- Perform appropriate data preprocessing and exploratory data analysis.
- Evaluate models using suitable classification metrics and leakage-resistant validation.
- Develop an interactive dashboard to present predictions and analysis results.
- Document dataset characteristics, experimental limitations and model performance.

### 3. Proposed Crop Selection

1. Wheat – Field disease detection and hyperspectral Septoria analysis.
2. Tomato – Field image-based disease classification.
3. Rice – Field image-based disease classification.

Final dataset selection and disease classes will be confirmed after verifying data availability, original sources, labels, licences and data quality.

### 4. Data Modalities

**RGB Images:**

Real-world crop photographs collected under agricultural conditions. These will be investigated for visible disease classification. Disease-region segmentation will be considered only if suitable annotations and sufficient time are available.

**Hyperspectral Images:**

Laboratory-collected wheat hyperspectral measurements in VNIR and SWIR ranges. These will be investigated for spectral differences associated with healthy and inoculated plants.

VNIR and SWIR datasets will be assessed separately before any integration. Differences in sensor characteristics, spectral ranges, acquisition conditions and experimental design must be considered.

RGB and hyperspectral data will initially be processed through separate pipelines because they have different data structures and characteristics.

### 5. Proposed Technology Stack

- Programming Language: Python 3.12
- Data Processing: NumPy and Pandas
- Image Processing: OpenCV
- Hyperspectral Processing: Spectral Python
- Machine Learning: Scikit-learn
- Deep Learning: PyTorch
- Dashboard: Streamlit
- Version Control: Git and GitHub

### 6. Expected Deliverables

- Verified and documented datasets with source and licence information where available.
- Dataset inventory, preprocessing assessment and exploratory analysis.
- RGB-based crop disease classification models, subject to dataset suitability.
- Wheat hyperspectral analysis and classification, subject to sufficient independent biological samples and reliable labels.
- Model evaluation results using appropriate validation strategies.
- Interactive Streamlit dashboard presenting supported predictions and analysis.
- Project documentation, limitations and final presentation.

### 7. Project Limitations

- Laboratory hyperspectral data may not directly represent real-world farm conditions.
- RGB and hyperspectral datasets will be processed separately unless compatibility and scientific justification for integration are established.
- Pixels and image patches from the same biological sample must not be treated as independent biological samples.
- Validation must account for the experimental grouping structure to reduce data leakage.
- Early disease detection will remain exploratory until suitable temporal measurements and reliable disease labels support it.
- The project will not claim farm-scale disease forecasting or future disease prediction without sufficient temporal evidence and appropriate validation.
- Final crop selection, model complexity and deliverables depend on dataset verification, data quality and the one-month development timeline.

### 8. Project Duration

Start Date: 10 November 2026

End Date: 10 December 2026

Project Duration: One Month

### 9. Team Structure

The project is currently coordinated by a three-member team:

- Hiba: VNIR investigation, coordination and integration.
- Member 2: SWIR investigation.
- Member 3: RGB dataset investigation.

Responsibilities may be adjusted after dataset verification and project planning.

### 10. Current Status

The revised project scope is under review. Dataset source verification and initial investigations are in progress. Final dataset selection, experimental design and model development are pending verification of the available data.
