# VNIR Progress Report — 25 November 2026

## 1. Work completed
- Rechecked the four VNIR ENVI headers found under the repository data directory.
- Verified four VNIR headers: 01_D, 04_D, 07_D and 10_D.
- All four specify `data ignore value = 4095`.
- Confirmed consistent dimensions across the four headers: 1370 lines, 1024 samples and 216 spectral bands.
- Confirmed wavelength units are nanometres (nm).

## 2. Ignore-value clarification
- The value 4095 is consistently specified in all four inspected VNIR headers.
- The value 16383 was recorded in an inspected SWIR header.
- These are modality-specific observations, not a contradiction within the inspected VNIR headers.
- This finding is limited to the four available VNIR headers inspected.

## 3. Remaining limitations
- Calibration and reflectance-processing provenance remain unverified.
- The original NPZ generation and correction scripts have not been located.
- Biological sample identity and acquisition-time confounding remain unresolved.
- The available ten-leaf subset does not establish sufficient independent biological replication for reliable predictive claims.

## 4. Current conclusion
The VNIR ignore-value discrepancy is resolved for the four inspected headers. The data remain suitable for carefully qualified exploratory spectral analysis only. This verification does not establish calibrated reflectance, complete processing reproducibility, reliable disease classification or forecasting.

## 5. Next actions
1. Obtain or verify the original VNIR processing and calibration records.
2. Confirm biological sample identities and experimental units.
3. Preserve the existing raw data and corrected-data provenance.
4. Incorporate this finding into the consolidated experimental design.
