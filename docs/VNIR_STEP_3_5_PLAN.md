\# VNIR Step 3.5 – Final Feature Dataset Preparation



\## 1. Objective



The objective of Step 3.5 is to prepare and validate the VNIR spectral features for future machine learning experiments.



This stage will build on the exploratory analysis documented in `VNIR\_FEATURE\_EXTRACTION.md`. No classification or forecasting performance is claimed at this stage.



\## 2. Planned Activities



\### 2.1 Final Dataset Inspection

\- Locate and verify the existing VNIR feature datasets.

\- Confirm the number of samples, features and metadata columns.

\- Check column names, data types and duplicate records.

\- Verify that the 216 spectral bands are represented correctly.



\### 2.2 Missing-Value Analysis

\- Identify columns and samples containing missing values.

\- Examine the extent and distribution of missing values.

\- Select an appropriate missing-value handling strategy based on the data.

\- Document any rows or features excluded during preparation.



\### 2.3 Feature Distribution and Outlier Analysis

\- Examine the distributions of spectral features.

\- Identify unusual values and potential outliers.

\- Distinguish genuine spectral variation from possible measurement errors.

\- Avoid removing observations without a scientific justification.



\### 2.4 Feature Redundancy Investigation

\- Review the highly correlated spectral bands identified in the earlier analysis.

\- Investigate potential redundancy among features.

\- Consider dimensionality reduction or feature selection where appropriate.

\- Retain relevant spectral information for further experiments.



\### 2.5 Feature Selection

\- Evaluate suitable feature-selection approaches.

\- Consider spectral relevance, correlation and model-based selection.

\- Perform feature selection only within the training data during model validation to prevent data leakage.



\### 2.6 Final Dataset Validation

\- Verify the final dataset dimensions and data types.

\- Check for remaining missing or non-finite values.

\- Confirm that metadata and spectral features are correctly separated.

\- Document the final preparation decisions.



\## 3. Scientific Considerations



\- The available VNIR measurements are treated as raw intensity unless calibration to reflectance is verified.

\- Pixels from the same leaf or scan may be correlated.

\- Future model evaluation should use appropriate group-based splitting to reduce data leakage.

\- The limited number of scans and leaf profiles must be considered when interpreting results.

\- Any disease classification or early-detection claims must be supported by suitable labels and independent validation.



\## 4. Expected Deliverables



The following are planned outputs, not yet completed results:



\- Validated VNIR feature dataset.

\- Missing-value and data-quality summary.

\- Feature distribution and outlier analysis.

\- Feature redundancy investigation.

\- Feature-selection report.

\- Final dataset validation summary.



Actual filenames and results will be recorded after the source datasets are located and the analysis is performed.



\## 5. Current Status



\*\*Status: Planned – Pending source dataset verification.\*\*



The exploratory VNIR feature extraction steps 3.1–3.4 are documented in `VNIR\_FEATURE\_EXTRACTION.md`. Step 3.5 will begin after the original processed datasets are located and verified.



No new measurements, feature-selection results or model-performance values are introduced in this document.

