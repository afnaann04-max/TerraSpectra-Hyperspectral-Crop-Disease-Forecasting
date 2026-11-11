
# TerraSpectra
## Project Scope

### 1. Project Overview

TerraSpectra is a crop disease detection and early spectral stress analysis system that uses real-world RGB crop images and laboratory hyperspectral data.

The project aims to identify visible crop disease symptoms from field images and investigate spectral changes associated with disease development using hyperspectral measurements.

### 2. Project Objectives

- Develop machine learning models for crop disease classification using real-world field images.
- Investigate early disease-related spectral changes using hyperspectral wheat data.
- Perform data preprocessing and exploratory data analysis.
- Evaluate models using appropriate classification metrics.
- Develop an interactive dashboard to display predictions and analysis results.

### 3. Proposed Crop Selection

1. Wheat – Field disease detection and hyperspectral Septoria analysis.
2. Tomato – Field image-based disease classification.
3. Rice – Field image-based disease classification.

The final datasets and disease classes will be confirmed after verifying data availability, labels and licences.

### 4. Data Modalities

**RGB Images:**
Real-world crop photographs collected under natural agricultural conditions. These will be used for visible disease classification and, where suitable annotations are available, disease-region segmentation.

**Hyperspectral Images:**
Laboratory-collected wheat hyperspectral measurements in VNIR and SWIR ranges. These will be used to analyse spectral differences between healthy and inoculated plants.

The RGB and hyperspectral data will be processed through separate pipelines because they have different data structures and characteristics.

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

- Verified and documented datasets.
- Data preprocessing and exploratory analysis.
- RGB-based crop disease detection models.
- Wheat hyperspectral analysis and classification model.
- Model evaluation results.
- Interactive Streamlit dashboard.
- Project documentation and final presentation.

### 7. Project Limitations

- Laboratory hyperspectral data does not directly represent real-world farm conditions.
- RGB and hyperspectral datasets will be processed separately.
- The project will not claim farm-scale disease forecasting or advance prediction without sufficient supporting evidence.
- Final crop selection and model scope depend on dataset verification and the one-month development timeline.

### 8. Project Duration

Start Date: 10 November 2026

End Date: 10 December 2026

Project Duration: One Month

### 9. Current Status

Project scope proposed to the four-member team. Dataset verification and final approval are pending.
