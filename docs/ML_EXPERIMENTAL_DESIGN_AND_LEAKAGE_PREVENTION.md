\# TerraSpectra — ML Experimental Design and Data Leakage Prevention



\## 1. Purpose



This document proposes an experimental design for developing and evaluating machine learning models in the TerraSpectra crop disease research project.



The objective is to establish a reliable evaluation procedure for VNIR, SWIR and RGB datasets while reducing data leakage, overfitting and misleading performance estimates.



This document describes recommended procedures. It does not claim that model training or evaluation has already been completed.



\## 2. Why Experimental Design Matters



Hyperspectral and image datasets may contain multiple observations from the same leaf, plant or acquisition session.



For example, a hyperspectral scan can contain thousands of pixel-level observations. These pixels are not necessarily independent biological samples.



If pixels from the same leaf appear in both training and testing sets, a model may learn leaf-specific characteristics rather than general disease patterns.



This can produce overly optimistic evaluation results.



Therefore, the split strategy must consider the biological and acquisition structure of the dataset.



\## 3. Define the Independent Sample Unit



Before model development, identify the independent experimental unit.



Potential levels include:



\- Pixel

\- Leaf

\- Plant

\- Pot

\- Acquisition session

\- Experimental batch



The correct unit depends on how the data was collected and how disease labels were assigned.



\### Required investigation



\- Identify how many plants were measured.

\- Determine how many leaves belong to each plant.

\- Identify which leaves belong to the same pot.

\- Determine whether multiple scans belong to the same physical sample.

\- Identify repeated measurements and acquisition sessions.

\- Confirm whether disease labels are assigned at pixel, leaf or plant level.



\*\*Decision:\*\* The independent sample unit must be established from experimental metadata before finalizing data splitting.



\## 4. Group-Aware Data Splitting



Where multiple observations belong to the same biological sample, use group-aware splitting.



Recommended conceptual structure:



| Dataset partition | Purpose |

|---|---|

| Training set | Model fitting |

| Validation set | Model selection and hyperparameter tuning |

| Test set | Final independent performance evaluation |



\### Recommended rules



1\. Keep observations from the same independent biological unit within one partition.

2\. Avoid placing pixels from the same leaf in different partitions.

3\. Avoid placing repeated scans of the same plant across different partitions.

4\. Preserve class representation where the available sample size permits.

5\. Use a fixed random seed for reproducibility.

6\. Document group identifiers and split assignments.

7\. Do not repeatedly tune a model using the final test set.



Possible approaches include:



\- GroupShuffleSplit

\- StratifiedGroupKFold

\- GroupKFold



The selected method must match the dataset's group structure and class distribution.



If there are too few independent groups for a reliable split, report this limitation instead of presenting an unreliable test score.



\## 5. Prevent Data Leakage During Preprocessing



All learned preprocessing operations must be fitted using training data only.



Examples include:



\- Missing-value imputation

\- Feature scaling

\- Feature selection

\- Dimensionality reduction

\- Normalization based on estimated dataset statistics



\### Recommended workflow



1\. Identify independent sample groups.

2\. Create training, validation and test partitions.

3\. Fit preprocessing transformations on training data.

4\. Apply the fitted transformations to validation and test data.

5\. Perform feature selection without using test labels.

6\. Tune model parameters using training and validation data.

7\. Evaluate the selected model once on the independent test set.



Where possible, use Scikit-learn pipelines to keep preprocessing and model fitting together.



\## 6. Missing Values and Invalid Spectral Measurements



Hyperspectral datasets may contain:



\- Missing values

\- Invalid measurements

\- Saturated values

\- Sensor-related noise

\- Unreliable spectral bands



Before training:



\- Identify invalid values and their causes.

\- Document missing-value patterns.

\- Determine whether affected samples or features should be excluded.

\- Evaluate whether imputation is scientifically justified.

\- Fit statistical imputation parameters on training data only.

\- Preserve the distinction between original missing values and imputed values.

\- Avoid filling long missing spectral regions without scientific justification.



The preprocessing strategy must be documented for each dataset separately.



\## 7. Class Imbalance



Unequal class distribution can affect model training and evaluation.



Recommended checks:



\- Count independent samples in each disease class.

\- Examine class distribution at the correct biological level.

\- Compare class distribution across training, validation and test partitions.

\- Avoid relying on accuracy alone.

\- Consider class weighting when justified.

\- Consider resampling only within training data.



Synthetic oversampling must not be applied before the train/test split.



\## 8. Model Development Strategy



Potential baseline models include:



\- Logistic Regression

\- Random Forest

\- Support Vector Machine

\- XGBoost or LightGBM



Potential deep learning approaches include:



\- One-dimensional CNN for suitable spectral inputs.

\- Two-dimensional CNN for suitable images or hyperspectral cubes.



Model selection should depend on:



\- Number of independent samples.

\- Number of features or spectral bands.

\- Data quality.

\- Class distribution.

\- Computational requirements.

\- Scientific objective.



Start with simple baseline models before considering complex architectures.



\## 9. Evaluation Metrics



Use multiple metrics to understand model performance.



| Metric | Purpose |

|---|---|

| Accuracy | Overall proportion of correct predictions |

| Balanced accuracy | Average recall across classes |

| Precision | Reliability of positive predictions |

| Recall | Ability to identify positive samples |

| F1-score | Balance between precision and recall |

| Confusion matrix | Distribution of correct and incorrect predictions |

| ROC-AUC | Ranking performance across classification thresholds |

| PR-AUC | Precision-recall performance, particularly useful with class imbalance |



Metric selection should reflect the disease-detection objective and available sample sizes.



Report the unit of evaluation clearly, such as pixel-level, leaf-level or plant-level.



\## 10. VNIR-Specific Considerations



The currently investigated VNIR dataset contains:



\- 4 scans.

\- 10 leaves.

\- 6 infected leaves.

\- 4 non-infected leaves.

\- 216 spectral bands in the combined dataset.



Important limitations:



1\. The number of independent plants is not yet established.

2\. Possible scan-treatment confounding requires further investigation.

3\. The small number of leaves limits reliable generalization claims.

4\. Pixel-level observations must not be treated as independent biological samples.

5\. The selected 30-band candidate dataset should not be assumed superior without comparative evaluation.



These limitations must be considered before model training.



\## 11. Cross-Dataset Experimental Design



VNIR, SWIR and RGB datasets should initially be investigated independently.



Before combining them, verify:



\- Crop species.

\- Disease categories.

\- Sample identities.

\- Label definitions.

\- Acquisition conditions.

\- Experimental design.

\- Compatibility of sample units.



Combining unrelated datasets does not automatically create a valid multimodal training dataset.



Separate dataset-specific baselines may be more appropriate when sample identity or acquisition conditions cannot be aligned.



\## 12. Reproducibility



For each experiment, record:



\- Dataset version and source.

\- Preprocessing steps.

\- Feature selection method.

\- Independent sample unit.

\- Grouping strategy.

\- Train/validation/test split.

\- Random seed.

\- Model parameters.

\- Evaluation metrics.

\- Software and library versions.

\- Results and limitations.



Store experiment configurations and results in a consistent project structure.



\## 13. Model Training Readiness Checklist



\- \[ ] Dataset source and licence verified.

\- \[ ] Dataset structure and labels checked.

\- \[ ] Independent biological sample unit established.

\- \[ ] Group relationships identified.

\- \[ ] Scan and treatment confounding investigated.

\- \[ ] Missing-value strategy finalized.

\- \[ ] Preprocessing methodology documented.

\- \[ ] Group-aware splitting strategy selected.

\- \[ ] Leakage prevention reviewed.

\- \[ ] Evaluation metrics defined.

\- \[ ] Baseline experiment plan prepared.

\- \[ ] Remaining limitations documented.



\## 14. Final Note



This document establishes a proposed experimental methodology for TerraSpectra.



The project should proceed to model development only when the relevant dataset quality, sample independence, experimental design and leakage-prevention requirements have been adequately investigated.



A high model score alone is not sufficient evidence of reliable crop disease detection or forecasting.
