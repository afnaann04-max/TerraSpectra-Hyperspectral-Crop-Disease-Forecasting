# VNIR Feature Selection Review

## Dataset
- Original spectral bands: 216
- Metadata columns: 4
- Candidate wavelength region: 730-810 nm
- Candidate bands: 30

## Findings
- The largest exploratory infected/non-infected mean differences
  occurred mainly around 739-755 nm.
- Seven pairs within the candidate region had absolute correlation
  of at least 0.98.
- Correlation indicates potential redundancy, not proof that a
  feature is unnecessary.

## Selection decisions
1. Retain all 216 original spectral bands as the baseline.
2. Retain the 30 bands from 730-810 nm as an exploratory candidate subset.
3. Flag highly correlated neighbouring bands for later testing.
4. Keep leaf-level statistical features separate from pixel-level features.
5. Keep intensity-based spectral indices exploratory.
6. Do not permanently remove features before leakage-safe model validation.

## Limitations
- The comparison includes only 6 infected and 4 non-infected leaves.
- Raw sensor intensity is not calibrated reflectance.
- Genotype, scan and experimental conditions may influence observed differences.
- Candidate wavelengths are not validated disease biomarkers.

## Validation
- Original 216 spectral bands confirmed.
- Candidate feature count confirmed: 30.
- Highly correlated candidate pairs confirmed: 7.
- No original spectral bands removed.
