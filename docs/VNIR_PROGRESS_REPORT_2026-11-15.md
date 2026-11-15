# VNIR Progress Report - 15 November 2026

## 1. Work completed
- Reviewed the existing VNIR dataset assessment and progress documentation.
- Documented missing values in the combined, baseline and candidate datasets.
- Documented the treatment of ignore values and short spectral gaps in the corrected NPZ.
- Recorded the results of 30 validation comparisons across 10 VNIR files and three CSV references.
- Added calibration and reflectance-provenance limitations to the dataset assessment.

## 2. Important findings and limitations
- Radiometric calibration procedures and reference measurements remain unverified.
- The current analysis uses recorded spectral intensity values, not confirmed calibrated reflectance.
- Acquisition-time differences may confound infected and control comparisons.
- Biological replication remains limited. The available pot records do not establish the number of individual plants.
- The four selected scans represent only one pot per genotype-treatment combination.
- Full-dataset class balance has not yet been established.

## 3. Current status
The available structural and numerical checks have passed. The VNIR dataset still requires further assessment before model development. The current findings are exploratory and should not be presented as validated classification performance.

## 4. Remaining work
- Verify calibration and reflectance-processing provenance.
- Establish full-dataset class counts using verified metadata.
- Continue assessing biological replication and group-aware validation.
- Avoid model training until dataset suitability and experimental design are established.
