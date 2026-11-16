# SWIR Updated File Inventory
## TerraSpectra – 16 November 2026

**Scope:** Files supplied for today's metadata investigation. This is not an inventory of files inside the 4.6 GB archive.

| File | Supplied / repository name | Type / content | Inspection status |
|---|---|---|---|
| SWIR metadata table | SWIR_data.csv (uploaded as `SWIR_data.csv.xls`) | Semicolon-delimited text CSV; 48 pot rows; 18 dpi time points; G/D leaf counts | Inspected; MD5 matches repository (`12dc1a89b7f0d648948750247ef488a3`) |
| Leaf sample description | Data_description.csv (uploaded as `Data_description.csv.xls`) | Semicolon-delimited text CSV; 279 leaf-level records; six metadata fields plus notes | Inspected; MD5 matches repository (`2efd148e433016da14a3209e6db575df`) |
| Existing scan filename list | Not supplied in this upload | Expected 96 scan filenames | Pending receipt |
| Existing 96-scan matching table | Not supplied in this upload | Existing scan-to-expected-scan mapping evidence | Pending receipt |
| SWIR archive | `20210311.zip` | Existing team archive; no new download performed | Not inspected in this task; do not download again |

## Metadata inspection summary

### SWIR_data.csv
- 48 pot records, IDs 01–48.
- 24 EPO_67 and 24 EPO_68.
- 24 Infected and 24 Non-infected.
- 18 dpi time points: -1, 0, 4–8, 10–20.
- 552 empty measurement cells, defined by the source as no HSI acquisition due to sampling.
- One `NA`: pot 23, EPO_67, Non-infected, 10 dpi, G side.
- Sum of numeric leaf-count cells across all dates/sides: 3,326.

### Data_description.csv
- 279 leaf-level records.
- 48 pot IDs.
- Both G and D sides represented for every pot.
- No duplicate Pot/Side/Leaf key found.
- Genotype and Treatment agree with SWIR_data.csv at pot level.
- Confidence: 246 level-1 records and 33 level-2 records.
- 39 pots have six records; 9 pots have five.

## File-format note

Although the uploads have `.csv.xls` suffixes, the contents are semicolon-delimited text, not Excel workbooks. They were read as Windows-1252 (cp1252) encoded CSV text. Original uploads were not modified.

## Inventory limitations

This is not the archive's internal file inventory. The 96-scan filename list and matching table were not included in the current upload, so the prior 96/96 result remains team-reported and pending evidence review.


## Official provenance

- DOI: https://doi.org/10.57745/WVP0FJ
- Repository: https://entrepot.recherche.data.gouv.fr/dataset.xhtml?persistentId=doi:10.57745/WVP0FJ
- Licence: Etalab Open License 2.0, compatible with CC-BY 2.0.
- The two uploaded metadata files' MD5 checksums exactly match the repository-published checksums.
