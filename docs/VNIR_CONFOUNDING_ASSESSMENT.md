# VNIR Confounding Assessment

## 1. Selected scan structure

The available selected VNIR raw dataset contains four scan folders:

| Scan | Pot | Genotype | Treatment | Acquisition time |
|---|---|---|---|---|
| 01_D | 01 | EPO_68 | Infected | 08:31:43 |
| 04_D | 04 | EPO_68 | Non-infected | 09:33:49 |
| 07_D | 07 | EPO_67 | Infected | 08:44:24 |
| 10_D | 10 | EPO_67 | Non-infected | 09:42:12 |

All scans were acquired on 11 March 2021.

## 2. Acquisition consistency

The four headers report identical:
- Image dimensions: 1370 lines x 1024 samples
- Spectral bands: 216
- Integration time: 6500
- Frame period: 6600
- Interleave: BIL
- Wavelength range: approximately 411.36–993.17 nm

## 3. Potential confounding

Both infected scans were acquired earlier than both non-infected scans.

Although the recorded technical settings are identical, acquisition-time effects such as illumination changes, instrument drift or environmental variation cannot be ruled out.

There is also only one pot/scan for each genotype-treatment combination. Treatment effects therefore cannot be reliably separated from individual pot and scan effects using this selected subset.

## 4. Implications for machine learning

- Pixels from the same scan or leaf must not be treated as independent biological samples.
- Random pixel-level train/test splitting would cause data leakage.
- Evaluation should use independent biological groups wherever sufficient data becomes available.
- The four-scan subset is suitable for exploratory analysis and preprocessing validation, not strong evidence of generalizable disease-classification performance.
- Additional independent pots and acquisition information are needed for reliable validation.

## 5. Conclusion

The selected VNIR scans have consistent recorded header settings, but low biological replication and aligned acquisition-time ordering between treatment groups create important limitations.

These limitations must be considered before model training and performance claims.
