# SWIR Investigation Report
## TerraSpectra â€“ Hyperspectral Crop Disease Forecasting

**Investigation date:** 16 November 2026\
**Role:** Member 2 â€“ SWIR metadata investigation\
**Scope:** Inspection of the two supplied metadata CSV files and assessment of available verification evidence.\
**Archive handling:** The SWIR archive was not downloaded or modified.

## 1. Objective

Inspect `SWIR_data.csv` and `Data_description.csv`; explain their fields; establish the documented meaning of pot, side, genotype, treatment, leaf and confidence level; review acquisition timing and experimental annotations; and identify what remains unverified.

## 1.1 Files inspected and parsing notes

The two supplied files were named `SWIR_data.csv.xls` and `Data_description.csv.xls` on upload. Their contents are semicolon-delimited text CSV files, not Excel workbooks. They were readable using Windows-1252 (cp1252) text encoding.

- `SWIR_data.csv`: 48 pot records, 39 columns including the three fixed metadata columns and 36 date/side measurement columns.
- `Data_description.csv`: 279 leaf-level records. The six data fields are followed by an empty column and a documentation-notes column.

The original uploaded files were not modified.

## 2. Official source and provenance

**Dataset:** Early detection of septoria infection on wheat leaves using hyperspectral imaging data\
**Author:** LATCHOUMANE, Lorraine (INRAE)\
**Repository:** Recherche Data Gouv\
**DOI:** https://doi.org/10.57745/WVP0FJ\
**Version:** 1.0\
**Publication date:** 15 November 2024\
**Licence:** Etalab Open License 2.0, compatible with CC-BY 2.0.

Official dataset page: https://entrepot.recherche.data.gouv.fr/dataset.xhtml?persistentId=doi:10.57745/WVP0FJ

The repository describes healthy and *Zymoseptoria tritici*-infected leaves from two durum wheat genotypes, imaged with VNIR and SWIR cameras on 18 dates from one day before inoculation to 20 days after inoculation. It reports 1,175 images per wavelength range and information on 3,326 leaves measured throughout the experiment. The repository requests appropriate credit using the dataset citation.

### 2.1 Checksum verification of the two supplied metadata files

The repository publishes these MD5 checksums, and the uploaded files were hashed locally:

| Metadata file | Repository MD5 | Uploaded-file MD5 | Result |
|---|---|---|---|
| `SWIR_data.csv` | `12dc1a89b7f0d648948750247ef488a3` | `12dc1a89b7f0d648948750247ef488a3` | Exact match |
| `Data_description.csv` | `2efd148e433016da14a3209e6db575df` | `2efd148e433016da14a3209e6db575df` | Exact match |

This confirms that the two uploaded metadata files are byte-for-byte identical to the versions represented by the repository's published MD5 values. It does not verify the large SWIR archive or the 96-scan mapping.

## 3. Metadata column explanation

### 3.1 `SWIR_data.csv`

The table title is: â€œNumber of leaves collected per pot and per date using short-wave infrared (SWIR) hyperspectral imaging (HSI).â€

| Field / column group | Meaning supported by the file |
|---|---|
| `Pot [2]` | Pot identifier. The table contains pot IDs 01â€“48. The note says the number of pots varies from 01 to 48 according to the date. |
| `Genotype [3]` | Durum wheat genotype: `EPO_67` or `EPO_68`. |
| `Treatment [4]` | `Infected` or `Non-infected`, defined by the inoculation procedure in note [4]. |
| Date columns (`-1`, `0`, `4`, `5`, `6`, `7`, `8`, `10`, `11`, `12`, `13`, `14`, `15`, `16`, `17`, `18`, `19`, `20` dpi) | For each date, two columns record the number of leaves collected/imaged from the pot sides `G` and `D`. |
| Numeric values `1`, `2`, `3` | Number of leaves recorded for that pot, side and acquisition date. |
| Empty cells | The table explicitly says empty cells indicate no HSI acquisition due to sampling. They must not automatically be treated as technical failures. |
| `NA` | The table explicitly says `NA` indicates missing data due to a technical malfunction. |

There are 18 listed acquisition time points, expressed as days post-inoculation (dpi): **-1, 0, 4â€“8, and 10â€“20**. The table does not list dpi 1, 2, 3 or 9.

### 3.2 `Data_description.csv`

The table title is: â€œIdentification of wheat leaf samples and their infection status.â€

| Column | Meaning supported by the file |
|---|---|
| `Pot [1]` | Pot identifier, represented as an unpadded integer (1â€“48). |
| `Side [2]` | Pot side: `G` or `D`. |
| `Leaf [3]` | Leaf number within that pot side; the documentation says 1 to 3 wheat leaves per pot side were imaged by HSI for each pot. |
| `Genotype [4]` | `EPO_67` or `EPO_68`. |
| `Treatment [5]` | `Infected` or `Non-infected`. |
| `Confidence level [6]` | Visual symptom-based infection confidence: `1` means high confidence; `2` means low confidence. |

The seventh field is blank. The eighth field contains explanatory notes in the supplied CSV export; it is not a sample-level metadata variable.

## 4. Pot, side, genotype and infection relationships

### 4.1 Documented relationship

`Data_description.csv` explicitly associates each leaf record with a pot, side, leaf number, genotype, treatment and confidence level.

The documentation defines:
- `G` = left side of the pot.
- `D` = right side of the pot.

The same left/right definition is repeated in the notes of both supplied files. Therefore **D and G identify pot sides, not disease classes, genotypes or treatments**.

The `SWIR_data.csv` table uses the same pot, genotype and treatment concepts, and has G/D columns for each dpi.

### 4.2 Checks performed on the supplied metadata

- `SWIR_data.csv` contains 48 distinct pot IDs, 01â€“48.
- The SWIR table has 24 `EPO_68` pots and 24 `EPO_67` pots.
- The SWIR table has 24 `Infected` pots and 24 `Non-infected` pots.
- `Data_description.csv` contains 279 leaf-level records across 48 pots.
- All 48 pot IDs in the leaf table are represented.
- Each pot has records for both sides (`G` and `D`).
- Each pot has 5 or 6 leaf records; nine pots have five records and the remaining 39 have six.
- No duplicate `(Pot, Side, Leaf)` keys were found in the supplied `Data_description.csv`.
- For every pot, the genotype and treatment in the leaf table agree with the corresponding pot-level genotype and treatment in `SWIR_data.csv`.

These checks establish internal consistency between the two supplied metadata tables. They do **not** independently validate image filenames because the filename list and matching table were not supplied in this upload.

### 4.3 Relationship to scan filenames

The metadata provides the components needed to describe a sample: pot ID, side (D/G), leaf number, genotype and treatment. However, the actual SWIR scan filename convention cannot be confirmed from these two tables alone. The exact filename pattern and the filename-to-metadata mapping must be checked against the team's existing filename list and matching table.

## 5. Meaning of D and G

The meaning is explicitly documented in the supplied metadata notes:

- `G`: left side of the pot.
- `D`: right side of the pot.

This is a **verified documentation finding**. Do not interpret D as diseased or G as healthy; infection status is represented separately by the `Treatment` field.

## 6. Acquisition dates and experimental details

### 6.1 Acquisition timing

`SWIR_data.csv` labels acquisition dates as `Date (dpi)`, and note [1] states that the dates are days post-inoculation. The 18 recorded time points are:

`-1, 0, 4, 5, 6, 7, 8, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20`

Thus, the table supports a relative experimental timeline from one day before inoculation through 20 days post-inoculation. It does **not** provide calendar dates or clock times for individual acquisitions.

### 6.2 Experimental details in the supplied metadata

- The plants are durum wheat (`Triticum turgidum subsp. durum`).
- The two genotypes are `EPO_67` and `EPO_68`.
- The notes link these genotypes to the Evolutionary Pre-breeding pOpulation (EPO) and cite David et al. (2014), DOI `10.1007/s11032-014-0179-z`.
- `Infected` plants were inoculated with *Zymoseptoria tritici* strain P1a dissolved in a distilled water/Tween 20 mixture. The file prints the concentration as `1.106 spores/mL`; this notation should be preserved as written until checked against the original experimental paper/protocol. Do not silently reinterpret it as a power-of-ten concentration.
- `Non-infected` plants received distilled water/Tween 20 mixture only.
- The number of pots represented varies by date, as stated in the table note.
- The table distinguishes empty cells (no HSI acquisition due to sampling) from `NA` (technical malfunction).

### 6.3 Quantitative checks from the supplied tables

- The SWIR table has 48 pot rows and 18 dpi time points, with separate G and D entries at each time point.
- It contains 552 empty measurement cells and one explicit `NA`.
- The one `NA` is recorded for pot 23, genotype `EPO_67`, treatment `Non-infected`, at 10 dpi on side `G`.
- Summing the numeric leaf-count entries across all pot Ã— date Ã— side cells gives **3,326**. This is a sum of leaf-count entries across time points and sides; it should not be described as 3,326 unique individual leaves without further identity-level evidence.
- The leaf-level description table contains 279 records: 246 with confidence level 1 and 33 with confidence level 2.

## 7. Existing 96-scan verification evidence

The team previously reported that all 96 expected pot-side scans were found and matched. The current upload contains only the two metadata CSV files. The following two requested evidence files are **not present in this conversation upload**:

1. Existing 96-scan filename list.
2. Existing 96-scan matching table.

Therefore, this investigation has not re-run the matching and cannot independently review the reported 96/96 result, its expected-scan definition, duplicate check or unmatched-file check.

The reported result should remain labelled **team-reported / evidence review pending** until the filename list and matching table are supplied. No additional archive download is needed.

## 8. Inconsistencies, limitations and unresolved questions

1. **Filename convention:** The exact filename pattern and its encoding of pot, side, leaf, genotype, treatment and/or date are not established by the two metadata CSVs alone.
2. **96-scan evidence:** The filename list and matching table were not included in the current upload, so the existing 96/96 verification cannot yet be reviewed.
3. **Calendar acquisition dates:** The SWIR table provides dpi values, not actual calendar dates or acquisition timestamps.
4. **DPI gaps:** The listed time points omit dpi 1, 2, 3 and 9. The supplied file does not explain these gaps beyond its general statement that empty cells indicate no HSI acquisition due to sampling.
5. **Technical missingness:** One `NA` is explicitly present at pot 23, 10 dpi, G side. The technical cause is not described in this table.
6. **Treatment concentration notation:** The source text states `1.106 spores/mL`. Its intended mathematical notation needs confirmation from the original protocol or paper.
7. **Leaf-level confidence:** Confidence level is based on visual evaluation of symptoms, with 1 high and 2 low. The supplied table does not provide the underlying visual assessment protocol.
8. **Biological replication:** Pot and leaf records are not automatically independent biological replicates. The experimental unit and repeated-measure structure should be confirmed from the full experimental protocol.
9. **Calendar-level acquisition schedule and sensor details:** Exact calendar dates, acquisition times, instrument settings and other acquisition conditions are not contained in the two supplied CSV tables.

## 9. Conclusion

The two supplied metadata files were successfully inspected. The documentation confirms that G is the left pot side and D is the right pot side. The files link pot IDs to genotype and treatment, and the leaf-level table adds side, leaf number and confidence level.

The two metadata tables are internally consistent for pot-level genotype and treatment. The SWIR count table records 18 dpi time points from -1 to 20 dpi, with one explicit technical-missing `NA` at pot 23 / 10 dpi / G side and empty cells defined as no acquisition due to sampling.

The exact filename convention and the team's existing 96/96 verification remain pending review because the filename list and matching table were not included with the two CSV uploads. No archive was downloaded, no matching was repeated, and no raw metadata file was changed.

**Prepared by:** Member 2\
**Project:** TerraSpectra â€“ Hyperspectral Crop Disease Forecasting
