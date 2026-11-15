
# TerraSpectra – Tomato RGB Dataset Assessment

## 1. Dataset Overview

**Dataset Name:** Dataset for Crop Pest and Disease Detection  
**Source:** Mendeley Data  
**Published:** 27 April 2023  
**Version:** 1  
**DOI:** 10.17632/bwh3zbpkpv.1  
**License:** CC BY 4.0

This dataset contains RGB images collected from local farms in Ghana for crop pest and disease detection.

## 2. Dataset Composition

The dataset covers four crops:

- Cashew
- Cassava
- Maize
- Tomato

According to the dataset description:

| Dataset Type | Number of Images |
|---|---:|
| Raw images | 24,881 |
| Augmented images | 102,976 |
| Raw tomato images | 5,435 |
| Augmented tomato images | 27,178 |

The complete dataset download size is approximately 7.86 GB.

## 3. Tomato Disease Classes

The Tomato dataset contains five classes:

1. Healthy
2. Leaf blight
3. Leaf curl
4. Septoria leaf spot
5. Verticillium wilt

These classes can support a multi-class tomato disease classification task.

## 4. Folder Structure

The Mendeley repository displays two main folders:

- Raw Data
- CCMT Dataset-Augmented

The augmented Tomato folder contains:

- train_set
- test_set

The training and testing folders contain class-wise subfolders.

## 5. Image Characteristics

- Image format: JPG
- Image dimensions vary.
- Reported dimensions include 400 × 400, 487 × 1080, 1080 × 518, 3024 × 4032 and 4032 × 3024 pixels.
- Images were captured under different backgrounds and illumination conditions.

## 6. Relevance to TerraSpectra

This dataset is a potential source for the Tomato RGB image classification pipeline.

It provides healthy and disease-affected tomato images across five classes.

It can be evaluated for training and testing a tomato disease classification model.

## 7. Limitations and Checks Required

Before using this dataset, the following checks are required:

- Download and inspect the selected Tomato images.
- Verify the number of images in each class.
- Check image quality and corrupted files.
- Identify duplicate or near-duplicate images.
- Inspect the existing training and testing split.
- Check for possible data leakage between training and testing sets.
- Confirm whether the raw or augmented dataset will be used.

The dataset description alone does not confirm that the existing split is free from data leakage.

## 8. Current Status

**Status:** Initial dataset assessment completed using the published Mendeley dataset description and folder structure.

Image-level inspection, preprocessing and model development are pending.

## 9. Dataset Reference

Mensah Kwabena, P., et al. (2023). Dataset for Crop Pest and Disease Detection. Mendeley Data, Version 1.

https://doi.org/10.17632/bwh3zbpkpv.1
