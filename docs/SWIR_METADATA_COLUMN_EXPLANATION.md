# SWIR Metadata Column Explanation
## TerraSpectra â€“ 16 November 2026

## 1. `SWIR_data.csv`

**Purpose:** Number of leaves collected per pot and per date using SWIR hyperspectral imaging.

The table contains three fixed pot-level fields followed by 18 acquisition time points. Each time point has two side-specific count fields: G and D.

| Column / field | Explanation |
|---|---|
| Pot [2] | Pot identifier, 01â€“48. |
| Genotype [3] | Durum wheat genotype: EPO_67 or EPO_68. |
| Treatment [4] | Infected or Non-infected, as defined by the inoculation protocol note. |
| G at each dpi | Number of leaves recorded from the left side of the pot at that dpi. |
| D at each dpi | Number of leaves recorded from the right side of the pot at that dpi. |
| 1, 2 or 3 | Number of leaves recorded for that pot/side/time point. |
| Empty cell | No HSI acquisition due to sampling, according to the table note. |
| NA | Missing data due to a technical malfunction, according to the table note. |

**DPI columns:** -1, 0, 4, 5, 6, 7, 8, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20.

**Side definitions:** G = left side; D = right side.

## 2. `Data_description.csv`

**Purpose:** Identification of wheat leaf samples and their infection status.

| Column | Explanation |
|---|---|
| Pot [1] | Pot identifier, 1â€“48. |
| Side [2] | G (left) or D (right) side of the pot. |
| Leaf [3] | Leaf number on that pot side. Documentation states 1â€“3 leaves per pot side were imaged by HSI for each pot. |
| Genotype [4] | EPO_67 or EPO_68. |
| Treatment [5] | Infected or Non-infected. |
| Confidence level [6] | Visual symptom assessment: 1 = high confidence; 2 = low confidence. |

The supplied export has an additional blank field and an eighth field containing explanatory notes. These are not extra sample-level variables.

## 3. Documented experimental definitions

- G means the left side of the pot.
- D means the right side of the pot.
- EPO_67 and EPO_68 are two durum wheat genotypes associated in the note with the David et al. (2014) EPO population reference (DOI: 10.1007/s11032-014-0179-z).
- Infected plants were inoculated with *Zymoseptoria tritici* strain P1a in distilled water/Tween 20 mixture.
- Non-infected plants received distilled water/Tween 20 mixture only.
- Confidence level 1 means high confidence and 2 means low confidence, based on visual symptom evaluation.

The concentration is transcribed as `1.106 spores/mL` from the supplied file. Its intended notation is not inferred here.

## 4. Inspection checks

- 48 distinct pot IDs in each metadata table.
- 24 EPO_67 and 24 EPO_68 pots in the SWIR pot-level table.
- 24 Infected and 24 Non-infected pots in the SWIR pot-level table.
- 279 leaf-level records in `Data_description.csv`.
- Both G and D sides are represented for all 48 pots.
- 279 unique Pot/Side/Leaf combinations; no duplicate key found.
- Genotype and Treatment agree between the two files for every pot.
- Confidence levels: 246 records at level 1 and 33 at level 2.
- Nine pots have five leaf-level records; 39 pots have six.

## 5. Important interpretation caution

These CSVs provide metadata and counts. They do not, by themselves, establish the exact SWIR filename syntax or prove that each leaf record maps one-to-one to an individual file. The team's filename list and matching table are required for that review.


## 6. Source and file integrity

Official dataset DOI: https://doi.org/10.57745/WVP0FJ\
Licence: Etalab Open License 2.0, compatible with CC-BY 2.0.

The uploaded `SWIR_data.csv` MD5 is `12dc1a89b7f0d648948750247ef488a3`, matching the repository-published checksum. The uploaded `Data_description.csv` MD5 is `2efd148e433016da14a3209e6db575df`, also matching the repository-published checksum. Thus, both supplied metadata files match the repository versions byte-for-byte.
