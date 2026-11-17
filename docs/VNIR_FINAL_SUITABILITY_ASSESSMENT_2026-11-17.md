# VNIR Final Suitability Assessment
Date: 17 November 2026
Project: TerraSpectra - Hyperspectral Crop Disease Forecasting

## 1. Overall conclusion

The available VNIR data are suitable for exploratory spectral analysis and carefully qualified descriptive comparisons. The currently processed VNIR subset has not been demonstrated to support reliable independent disease classification, early disease detection, or disease forecasting.

This assessment distinguishes the broader experimental sampling metadata from the smaller VNIR subset currently processed in the repository.

## 2. Dataset and sampling structure

The VNIR sampling metadata contains 48 unique pot records:
- 24 EPO_67 and 24 EPO_68 pots.
- 24 infected and 24 non-infected pots.
- 12 pots in each genotype-treatment combination.
- 18 sampling time points from -1 to 20 days post-inoculation.

Sampling coverage is unequal:
- 48 pots are recorded from -1 through 7 DPI.
- 36 pots are recorded from 8 through 20 DPI.
- Leaf counts vary by date and pot side.
- No D-side leaf acquisitions are recorded at 18, 19 and 20 DPI.

The metadata identifies pot, side and leaf number. It does not establish that the same physical leaf was tracked across dates.

The local metadata does not establish the number of individual plants per pot. Individual plant identities have not been mapped to the processed VNIR records. The number and identity of independent experimental units represented in the selected VNIR subset therefore require further verification.

## 3. Current processed VNIR subset

The current validated subset contains:
- Four scans.
- Four selected pots.
- Ten leaves.
- 272,912 pixel records.
- 216 spectral bands in the baseline dataset.

Pixels and leaves from the same scan or pot must not be treated as independent biological replicates.

The selected scans have one pot per genotype-treatment combination. Treatment is therefore confounded with scan identity in this subset. A reliable independent treatment-effect evaluation cannot be established from these four groups alone.

The existence of 48 pots in the broader sampling metadata does not establish that usable VNIR image data for all 48 pots are present in the repository.

## 4. Data quality and ignore values

Four inspected VNIR headers specify an ignore value of 4095. An inspected SWIR header specifies 16383. These are modality-specific observations and should not be treated as a same-modality contradiction.

Ten original and corrected NPZ file pairs were compared:
- Raw spectra were unchanged.
- Pixel coordinates were unchanged.
- Original invalid masks were unchanged.
- Cleaned spectra and missing-value information changed.
- The corrected files include additional header-ignore and corrected-invalid masks.

The numerical comparisons support the integrity of the correction, but do not independently establish the complete original processing history.

## 5. Processing provenance

No Python scripts, notebooks, PowerShell scripts or R scripts were found in the repository search that could reproduce the NPZ generation or correction process.

The documented cleaning decisions and numerical audit results are available, but the original generation script and complete execution environment remain unverified.

The corrected NPZ data should not be described as fully reproducible until the processing implementation and its dependencies are available.

## 6. Calibration provenance

The original research publication describes a reflectance calculation using a Spectralon reference and dark-current measurements.

However:
- No calibration implementation was found in the searched local source and script directories.
- No calibration-named files or directories were found under the data directory.
- The local NPZ processing has not been shown to apply the publication's reflectance calculation.

Therefore, the processed VNIR spectra must currently be described as processed spectral-intensity data. Their status as calibrated reflectance is unverified.

## 7. Suitability by research objective

### Exploratory spectral analysis
Suitable, provided missing values, ignore values and acquisition conditions are handled transparently.

### Descriptive comparisons
Possible with clear limitations. Results from the four-scan subset must not be interpreted as independent biological treatment effects.

### Disease classification
Not validated. The selected subset has too few independent scan/pot groups and treatment is confounded with scan identity.

### Early disease detection
Not established. A reliable early-detection claim requires appropriate time-resolved observations, verified labels and independent validation.

### Disease severity prediction
Not established by the current evidence. Severity labels and their relationship to the processed VNIR observations require verification.

### Disease forecasting
Not currently supported. Forecasting requires verified temporal linkage, future outcomes, appropriate independent experimental units and leakage-safe validation.

## 8. Recommendations

1. Preserve raw VNIR data and retain the 216-band baseline.
2. Keep the 30-band candidate as an exploratory feature subset; it has not been proven superior to the baseline.
3. Obtain the original NPZ generation and correction scripts, if available.
4. Verify calibration reference measurements and processing history before describing data as reflectance.
5. Confirm plant identity, plants per pot and the experimental unit used for treatment assignment.
6. Confirm whether individual leaves can be tracked across dates.
7. Establish which of the 48 metadata pot records have corresponding usable VNIR image files.
8. Use group-aware validation based on the true experimental unit. Do not randomly split pixels from the same biological sample across training and testing.
9. Do not claim disease forecasting or early detection until temporal and independent validation requirements are met.

## 9. Final assessment

The VNIR investigation has established useful evidence about the dataset structure, spectral data quality, sampling coverage and limitations.

The available subset is suitable for exploratory analysis, but it is not yet validated for reliable disease classification, early detection or forecasting.

Unresolved calibration and processing provenance, acquisition-time confounding, and incomplete plant and leaf identity mapping must be addressed before stronger scientific claims are made.
