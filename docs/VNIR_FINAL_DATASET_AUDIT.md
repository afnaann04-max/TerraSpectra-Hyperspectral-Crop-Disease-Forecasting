# VNIR Final Dataset Audit

Date: 13 November 2026

## 1. Dataset Structure

- Total pixel samples: 272,912
- Total columns: 220
- Metadata columns: 4 (Scan_ID, Leaf_ID, X, Y)
- Spectral bands: 216
- Scans: 4
- Unique leaves: 10

## 2. Pixel Identity Validation

- Duplicate rows: 0
- Duplicate pixel identities: 0
- Unique pixel identities: 272,912
- Leaves linked to multiple scans: 0
- Pixel identity validation: PASS

## 3. Missing Values

- Total missing spectral values: 7,559
- Missing values remain in some wavelength bands.
- Missing values were not removed or filled during this audit.

## 4. Disease Treatment Label Validation

Original dataset metadata was matched using pot number, side and leaf number.

| Scan | Pot | Genotype | Treatment | Leaves |
|---|---:|---|---|---:|
| 01_D | 1 | EPO_68 | Infected | 3 |
| 04_D | 4 | EPO_68 | Non-infected | 2 |
| 07_D | 7 | EPO_67 | Infected | 3 |
| 10_D | 10 | EPO_67 | Non-infected | 2 |

- Matched leaves: 10
- Unmatched leaves: 0
- Infected leaves: 6
- Non-infected leaves: 4
- All matched leaves have confidence level 1.

Treatment labels are assigned at the plant/leaf level based on the original metadata. They are not independent pixel-level diagnoses.

## 5. Important Metadata Interpretation

- D represents the right side of the pot.
- G represents the left side of the pot.
- D does not mean diseased.
- Infected plants were inoculated with Zymoseptoria tritici.
- Non-infected plants received the water/Tween mixture.

## 6. Audit Conclusion

The combined VNIR dataset has consistent pixel identities and all ten leaf samples successfully match the original treatment metadata.

The dataset is suitable for continuing feature preparation, subject to handling remaining missing spectral values and designing validation splits that keep related pixels and leaves together.

No changes were made to the original combined dataset during this audit.

## 7. Limitations

- Only four selected scans and ten leaves are included.
- Treatment classes are imbalanced at the leaf level (6 infected, 4 non-infected).
- Pixel samples from the same leaf are not independent observations.
- Results from this selected subset should not be treated as proof of generalization to new plants or experimental conditions.
