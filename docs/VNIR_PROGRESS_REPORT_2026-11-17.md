# VNIR Progress Report — 17 November 2026

## 1. Work completed

Today's work focused on calibration provenance, ignore-value verification, processed NPZ comparison, biological sampling metadata, and final VNIR suitability assessment.

## 2. Calibration provenance

- Searched the local repository for calibration-related scripts, references, and files.
- No local processing script or reference data was found that independently demonstrates reflectance calibration of the processed VNIR NPZ files.
- Although the research methodology may describe calibration procedures, their application to the local processed files has not been verified.
- The current data should therefore be described as processed spectral intensity data, not confirmed calibrated reflectance.

## 3. Ignore-value investigation

- Inspected four VNIR ENVI headers. All four recorded an ignore value of 4095.
- The inspected SWIR header recorded an ignore value of 16383.
- These observations support treating the values as modality-specific for the inspected files.
- The findings do not establish that every VNIR or SWIR header uses the same value.

## 4. Processed NPZ comparison

- Compared 10 original and corrected VNIR NPZ file pairs.
- Raw spectra, original invalid masks, and pixel coordinates were unchanged across the compared pairs.
- Cleaned spectra and remaining-missing information changed in all 10 corrected files.
- The corrected files also contain additional masks identifying header ignore values and corrected invalid values.
- A total of 723 raw values matching the VNIR header ignore value of 4095 were identified in the 10-file subset.
- The comparison supports preservation of raw measurements and coordinates during the correction.
- The original NPZ generation/correction script was not found in the repository. Complete processing reproducibility is therefore not established.

## 5. Biological sampling metadata

The VNIR sampling metadata was parsed and checked.

- 48 unique pot records were identified.
- The metadata contains 24 EPO_67 and 24 EPO_68 pots.
- It records 24 infected and 24 non-infected pots, with 12 pots in each genotype-treatment combination.
- Sampling metadata covers 18 time points from -1 to 20 days post inoculation (DPI).
- 48 pots are recorded from -1 to 7 DPI; 36 pots are recorded from 8 to 20 DPI.
- Leaf counts vary by date and pot side.
- No D-side leaf acquisitions are recorded at 18–20 DPI.
- The metadata does not establish the number of individual plants per pot or confirm the identity of individual plants.
- It identifies sampling information such as pot, side, and leaf number, but does not establish that the same physical leaf was tracked across dates.
- The 48 metadata pot records do not prove that all 48 pots have usable VNIR image files in the local processed subset.

## 6. Selected processed VNIR subset and limitations

The currently investigated processed subset contains:

- 4 scans and 4 pots.
- 10 leaves.
- 272,912 pixel records.
- 216 spectral bands.

Important limitations:

- Pixels and leaves from the same scan or pot are not independent biological replicates.
- The selected subset contains one pot for each genotype-treatment combination.
- Treatment is confounded with scan identity in this selected subset.
- Group-aware validation is required; random pixel-level splitting would risk data leakage.
- The selected subset does not establish reliable disease classification, early detection, severity prediction, or forecasting performance.

## 7. Final suitability assessment

Created `docs/VNIR_FINAL_SUITABILITY_ASSESSMENT_2026-11-17.md`.

The assessment concludes that the available VNIR subset is suitable for exploratory spectral analysis and carefully qualified descriptive comparisons. It is not yet demonstrated to be suitable for reliable disease classification, early detection, severity prediction, or forecasting.

The assessment also records unresolved calibration provenance, incomplete processing reproducibility, limited biological replication evidence, and experimental-design limitations.

## 8. Previous report correction

Updated `docs/VNIR_PROGRESS_REPORT_2026-11-14.md` to correct the earlier sampling-coverage statement.

The corrected statement reflects 48 pots from -1 to 7 DPI and 36 pots from 8 to 20 DPI, across 18 sampling time points.

## 9. Pending work

1. Obtain or reconstruct a reproducible VNIR NPZ processing pipeline, while preserving the original files.
2. Verify whether reflectance calibration was applied to the local VNIR data.
3. Confirm the number of plants per pot and the true experimental unit from authoritative experimental records.
4. Investigate whether physical leaves can be tracked across sampling dates.
5. Establish which metadata pots have usable raw and processed VNIR image files.
6. Review the full team's modality findings before deciding whether any data fusion is scientifically justified.
7. Design group-aware validation only after the experimental units and dataset suitability are established.

## 10. Current conclusion

The VNIR investigation has made progress in data-quality verification, metadata interpretation, and documenting limitations. The work supports exploratory analysis, but important provenance and experimental-design questions remain unresolved. No final predictive model or forecasting claim is made at this stage.
