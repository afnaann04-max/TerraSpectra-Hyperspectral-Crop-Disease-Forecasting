# SWIR Progress Report — 16 November 2026

## 1. Work completed

Member 2 completed the assigned SWIR metadata investigation and submitted four documentation files:

- `SWIR_INVESTIGATION_REPORT_UPDATED.md`
- `SWIR_METADATA_COLUMN_EXPLANATION.md`
- `SWIR_UPDATED_FILE_INVENTORY.md`
- `SWIR_UNRESOLVED_ISSUES.md`

The submitted documents were reviewed for consistency and coverage.

## 2. Dataset source and integrity

- Dataset: Early detection of septoria infection on wheat leaves using hyperspectral imaging data
- Repository: Recherche Data Gouv
- DOI: https://doi.org/10.57745/WVP0FJ
- Version: 1.0
- Licence reported in the repository record: Etalab Open License 2.0, compatible with CC-BY 2.0

Member 2 reports that the MD5 checksums of both supplied metadata files exactly match the repository-published checksums:

- `SWIR_data.csv`: `12dc1a89b7f0d648948750247ef488a3`
- `Data_description.csv`: `2efd148e433016da14a3209e6db575df`

This checksum result applies to the two metadata CSV files only. It does not verify the large SWIR archive or the team's 96-scan mapping.

## 3. Verified metadata findings reported by Member 2

### `SWIR_data.csv`

- 48 pot records, IDs 01–48.
- Two genotypes: EPO_67 and EPO_68, with 24 pots each.
- Two treatment groups: Infected and Non-infected, with 24 pots each.
- 18 listed acquisition time points: -1, 0, 4–8 and 10–20 dpi.
- G represents the left side of the pot; D represents the right side.
- 552 empty measurement cells are defined by the source as no HSI acquisition due to sampling.
- One `NA` is recorded at pot 23, EPO_67, Non-infected, 10 dpi, G side; the source defines `NA` as missing data due to technical malfunction.
- The sum of numeric leaf-count entries across all dates and sides is 3,326. This is not established as 3,326 unique individual leaves.

### `Data_description.csv`

- 279 leaf-level records across 48 pots.
- Both G and D sides are represented for every pot.
- 279 unique Pot/Side/Leaf combinations; no duplicate key was found.
- Genotype and treatment agree with `SWIR_data.csv` at pot level.
- Confidence levels: 246 level-1 records and 33 level-2 records.
- 39 pots have six records; nine pots have five.

## 4. Existing 96-scan verification

The project previously recorded a result of 96/96 expected pot-side scans matched. However, the separate filename list and matching table were not found in the earlier project-folder search and were not included in Member 2's submission.

Therefore, the 96/96 result remains **previously team-reported; supporting evidence not independently reviewed**. Do not repeat the matching or download the archive again solely to recreate missing documentation.

## 5. Outstanding questions

The submitted unresolved-issues list identifies the following items for future evidence review:

- Exact scan filename convention and leaf-to-file mapping.
- Independent review of the existing 96/96 scan-matching evidence.
- Calendar acquisition dates, clock times and instrument settings.
- Reason for the unlisted dpi 1, 2, 3 and 9 time points.
- Cause of the technical `NA` at pot 23, 10 dpi, G side.
- Original notation of the inoculum concentration, transcribed as `1.106 spores/mL`.
- Visual confidence-scoring protocol.
- Experimental unit, biological replication and repeated-measure structure.

These points remain unresolved; no assumptions have been substituted for missing evidence.

## 6. Work restrictions followed

- The existing SWIR archive was not downloaded again or modified.
- The 96-scan matching was not repeated.
- No preprocessing or model training was performed.
- Original metadata files were not modified.

## 7. Current assessment

**Member 2's assigned metadata investigation: Completed for 16 November 2026.**

**Metadata review: Completed from the four submitted documentation files.**

**96/96 scan evidence review: Pending supporting filename list and matching table.**

The SWIR metadata investigation is documented, while the separate scan-mapping evidence and experimental-protocol questions remain open.
