# TerraSpectra — SWIR Dataset Investigation
## Final Investigation Report — 17 November 2026

**Project:** TerraSpectra — Hyperspectral Crop Disease Forecasting
**Dataset:** Early detection of septoria infection on wheat leaves using hyperspectral imaging data
**DOI:** 10.57745/WVP0FJ
**Status:** Investigation documentation updated; team review and Git approval pending.

---

## 1. Executive Summary

The SWIR dataset source, metadata and related research paper have been reviewed.

The team confirmed that filename-based scan verification was already completed during the earlier investigation using the downloaded `20210311.zip` archive and 48 pot records in `SWIR_data.csv`.

The earlier command output recorded:

- 96 expected scans and 96 actual scans.
- 96 unique scan identities.
- 0 duplicates.
- 0 missing scans.
- 0 unexpected or unmatched identities.

One folder-placement anomaly was identified: `18_D.hyspex` was stored inside the `18_G` folder, although the filename itself was correct.

The original filename list and pot-side matching table were not preserved as separate files. The verification results were recorded in the earlier dataset assessment documentation.

This report uses the previously documented results. Scan matching was not repeated, and the archive was not downloaded again.

## 2. Official Dataset Information

- Dataset: Early detection of septoria infection on wheat leaves using hyperspectral imaging data.
- Author: Lorraine Latchoumane (INRAE).
- Repository: Recherche Data Gouv.
- DOI: 10.57745/WVP0FJ.
- Version: 1.0.
- Publication date: 15 November 2024.
- Licence: Etalab Open License 2.0.
- SWIR archive: `20210311.zip`.
- Published archive size: 4.3 GB.
- Official MD5: `7ad4e3b5a9a14704af51191269d2e019`.

Official repository:
https://entrepot.recherche.data.gouv.fr/dataset.xhtml?persistentId=doi:10.57745/WVP0FJ

DOI:
https://doi.org/10.57745/WVP0FJ

## 3. Historical SWIR Scan Verification

The teammate confirmed that the earlier filename-based verification used the downloaded archive and the 48 pot records in `SWIR_data.csv`.

| Verification | Previously documented result |
|---|---:|
| Expected scans | 96 |
| Actual scans | 96 |
| Unique scan identities | 96 |
| Duplicates | 0 |
| Missing scans | 0 |
| Unexpected/unmatched identities | 0 |

### Folder-placement anomaly

`18_D.hyspex` was stored inside the `18_G` folder, although its filename was correct.

### Evidence limitation

The original filename list and pot-side matching table were not saved as separate files.

The results were recorded in the earlier dataset assessment documentation.

Therefore:

- The 96/96 result is a previously completed and documented team verification.
- The separate filename list is not preserved.
- The separate pot-side matching table is not preserved.
- This report does not claim that those original evidence files are available.
- No repeat scan matching or archive download was performed for this update.

## 4. Metadata Findings

### 4.1 SWIR_data.csv

The metadata contains 48 pot-level records and 39 columns.

Important fields:

- Pot ID
- Genotype
- Treatment
- 18 acquisition dates
- G and D side-specific leaf counts

Genotypes:
- EPO_67
- EPO_68

Treatments:
- Infected
- Non-infected

There are 24 pots per genotype and 24 pots per treatment.

The 18 listed DPI values are:

`-1, 0, 4, 5, 6, 7, 8, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20`

Side meanings:
- G = left side of pot.
- D = right side of pot.

Other findings:

- Numeric values 1, 2 and 3 represent leaf counts.
- Empty cells indicate no HSI acquisition due to sampling.
- `NA` indicates missing data due to technical malfunction.
- 552 empty measurement cells.
- One explicit `NA`.
- The explicit NA occurs at pot 23, EPO_67, Non-infected, 10 DPI, G side.
- Sum of numeric leaf-count entries is 3,326. This is not necessarily the number of unique leaves.

### 4.2 Data_description.csv

The table contains 279 leaf-level records.

Important fields:

- Pot
- Side
- Leaf
- Genotype
- Treatment
- Confidence level

Findings:

- Both sides are represented for all 48 pots.
- No duplicate Pot-Side-Leaf keys were found.
- Nine pots have five records; 39 pots have six records.
- Genotype and treatment agree between the two metadata tables.
- Confidence level 1 = high confidence.
- Confidence level 2 = low confidence.
- 246 records have confidence level 1.
- 33 records have confidence level 2.

### 4.3 Experimental description

- Durum wheat with two genotypes.
- Infected plants were inoculated with *Zymoseptoria tritici* strain P1a in water/Tween 20.
- Non-infected controls received water/Tween 20 only.
- The metadata prints the inoculum concentration as `1.106 spores/mL`. Its notation requires confirmation from the experimental protocol before interpretation.

## 5. SWIR Instrument Specifications

According to the 2025 research paper:

| Parameter | Study-specific specification |
|---|---|
| Camera | HySpex SWIR-384 |
| Manufacturer | Norsk Elektro Optikk (NEO) |
| Acquisition mode | Pushbroom |
| Spectral range | 964–2494 nm |
| Spectral channels | 256 |
| Image dimensions | 420 × 320 pixels |
| Camera-to-leaf distance | 21.5 cm |
| Lens focal distance | 30 cm |
| Pixel dimensions | 217 × 217 µm |
| Reference panel | Certified SRS99 Spectralon |

The paper also describes dark-current measurement and reflectance calculation.

The study-specific value of 256 spectral channels should be used rather than a generic manufacturer specification.

Exact integration time, frame period and scan speed were not established from the inspected study methods.

## 6. Missing DPI Observations

The experiment was conducted in 2021, with acquisitions on 18 dates from -1 to 20 DPI.

### 1, 2 and 3 DPI

No acquisition was performed because plants were bagged to maintain high humidity and promote infection.

### 9 DPI

Acquisition was skipped due to technical problems.

### 10 DPI — Technical NA

The metadata records:

- Pot: 23
- Genotype: EPO_67
- Treatment: Non-infected
- DPI: 10
- Side: G
- Status: NA

The metadata identifies this as a technical malfunction, but the exact cause is unknown.

There is no evidence linking this individual 10 DPI NA to the separate 9 DPI interruption.

### General sample reduction

The paper mentions leaf sampling for biomolecular analyses, natural senescence, mechanical injuries and technical errors as general reasons for sample reduction.

These reasons should not be assigned to every individual empty cell without supporting evidence.

## 7. Unresolved Technical Questions

1. What exact SWIR integration time was used?
2. What were the frame period and scan speed?
3. What caused the technical malfunction at pot 23, G side, 10 DPI?
4. What is the specific reason for every individual empty metadata cell?
5. What is the complete calendar-date mapping for all 18 DPI acquisition dates?
6. What is the correct interpretation of the printed inoculum concentration `1.106 spores/mL`?
7. Can the original 96-scan filename list and pot-side matching table be recovered from earlier working records?
8. Are the original archive checksum and ZIP integrity results available in the earlier assessment documentation?

These questions require additional protocol, acquisition-log or historical documentation evidence.

## 8. Evidence Status

| Item | Status |
|---|---|
| Official dataset source | Verified |
| Metadata review | Completed |
| Study-specific camera specifications | Reported in research paper |
| Missing 1–3 DPI explanation | Documented |
| Missing 9 DPI explanation | Documented |
| Pot 23, 10 DPI NA | Recorded; exact cause unknown |
| Historical 96/96 verification | Previously completed and documented |
| Separate filename list | Not preserved |
| Separate pot-side matching table | Not preserved |
| 18_D.hyspex folder anomaly | Previously identified |
| Exact integration time and scan speed | Unresolved |

## 9. Recommended Next Actions

1. Retain this report in `research/SWIR`.
2. Keep the earlier dataset assessment as the reference for historical scan-verification results.
3. Recover original evidence files only if they are available in earlier working records.
4. Consult experimental protocols or acquisition logs to resolve technical questions.
5. Review all documentation changes before Git staging.
6. Obtain approval before committing and pushing.

No scan matching or archive download should be repeated solely for this documentation update.

## 10. Supporting References

1. Recherche Data Gouv dataset:
https://entrepot.recherche.data.gouv.fr/dataset.xhtml?persistentId=doi:10.57745/WVP0FJ

2. Dataset DOI:
https://doi.org/10.57745/WVP0FJ

3. Latchoumane et al. (2025), Data in Brief 59, 111404:
https://doi.org/10.1016/j.dib.2025.111404

4. Full-text research paper:
https://pmc.ncbi.nlm.nih.gov/articles/PMC11919375/

5. HySpex SWIR-384 manufacturer page:
https://www.hyspex.com/hyspex-products/hyspex-classic/hyspex-swir-384

## 11. File and Git Handover

New report filename:

`SWIR_FINAL_INVESTIGATION_REPORT_2026-11-17.md`

Other relevant existing files:

- `SWIR_INITIAL_FILE_INVENTORY.md`
- `SWIR_INVESTIGATION_REPORT.md`
- `SWIR_METADATA_COLUMN_EXPLANATION.md`
- `SWIR_UNRESOLVED_ISSUES.md`

Only files actually changed and saved should be reported as updated.

Git commit ID: Pending review, approval and push.

Do not invent a commit ID or claim that changes have been pushed before the actual Git operation.

---

**Final status — 17 November 2026:** The SWIR investigation findings, historical 96/96 verification, evidence limitation, instrument specifications, missing DPI observations, technical NA finding, unresolved questions and source references have been consolidated. Team review and Git approval/push remain pending.