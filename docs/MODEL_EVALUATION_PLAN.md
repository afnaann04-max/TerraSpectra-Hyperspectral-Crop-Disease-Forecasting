
# TerraSpectra – Model Evaluation Plan

## 1. Introduction

This document defines the proposed evaluation strategy for
the TerraSpectra crop disease detection system.

The project uses two independent data modalities:

1. RGB field images.
2. Laboratory wheat hyperspectral data.

Separate models will be developed and evaluated for each
data modality.

## 2. RGB Image Classification Pipeline

### Objective

Classify crop images into healthy and disease-related
categories while preserving crop-specific disease labels.

### Proposed Models

- Convolutional Neural Network (CNN)
- MobileNetV2
- ResNet50

The models will be selected based on dataset size,
computational requirements and experimental results.

### Evaluation Metrics

- Accuracy
- Precision
- Recall
- F1-score
- Confusion Matrix

## 3. Hyperspectral Classification Pipeline

### Objective

Analyse spectral information to identify patterns
associated with healthy and infected wheat samples.

### Proposed Models

- Random Forest
- Support Vector Machine (SVM)
- 3D-CNN, subject to data availability and feasibility

### Evaluation Metrics

- Accuracy
- Precision
- Recall
- F1-score
- Confusion Matrix

Spectral feature analysis and dimensionality reduction
may also be explored.

## 4. Data Splitting Strategy

The datasets will be divided into:

- Training set: 70%
- Validation set: 15%
- Testing set: 15%

Splitting must be performed carefully to prevent data
leakage.

For hyperspectral data, samples from the same plant or
leaf should not appear across training and testing sets
where this could lead to leakage.

For RGB data, duplicate or near-duplicate images should
also be considered during splitting.

## 5. Model Comparison

Models will be compared using consistent evaluation
metrics and appropriate test datasets.

The comparison will consider:

- Classification performance
- Generalisation ability
- Training time
- Computational requirements
- Class imbalance

The best model will be selected based on overall
performance rather than accuracy alone.

## 6. Important Considerations

1. RGB and hyperspectral datasets will use separate
   processing pipelines.
2. Different crop diseases will retain their original
   labels.
3. No unsupported performance claims will be made.
4. Evaluation results will be documented after actual
   model training.
5. Early disease forecasting claims require temporal
   validation and sufficient experimental evidence.

## 7. Expected Outcome

This evaluation plan will provide a structured approach
for comparing machine learning models in TerraSpectra.

It will help identify suitable models for crop disease
classification and hyperspectral spectral analysis.

## 8. Current Status

Status: Evaluation strategy documented.

Model training and performance evaluation are pending
dataset verification and preprocessing.
