# SWIR Dataset Access Investigation

**Date:** 21 November 2026
**Member:** Fahma (Member 2)
**Branch:** Fahma
**Previous access report:** SWIR\_ACCESS\_FOLLOWUP\_2026-11-20.md
**Previous commit:** a537079

## 1\. Objective

Identify the official SWIR dataset holder and access route, establish the public availability of the original archive, and determine whether technical verification can proceed.

No previous local searches or historical scan verification were repeated.

## 2\. Official dataset source — independently verified

* Dataset: Early detection of septoria infection on wheat leaves using hyperspectral imaging data.
* DOI: 10.57745/WVP0FJ
* Repository: Recherche Data Gouv.
* Depositor and repository point of contact: Lorraine Latchoumane.
* Associated institution: INRAE.
* Repository file access: Public.
* Licence: Etalab Open License 2.0.
* Publication date: 15 November 2024.

Official dataset:
https://entrepot.recherche.data.gouv.fr/dataset.xhtml?persistentId=doi:10.57745/WVP0FJ

## 3\. Original archive availability — independently verified

The official repository file listing includes:

* Filename: 20210311.zip
* Repository path: Data/SWIR/20210311.zip
* Listed size: 4.3 GB
* Access status: Public
* Publication date: 15 November 2024
* Listed MD5: 7ad4e3b5a9a14704af51191269d2e019

The public repository listing establishes an official access route for this archive.

Important limitation: The archive was not downloaded or inspected during this investigation. Its internal contents have not been verified.

## 4\. Dataset contact and responsible institution

The repository identifies Lorraine Latchoumane (INRAE) as the dataset point of contact and depositor.

The 2025 associated data article lists the corresponding author's email:

lorraine.latchoumane@inrae.fr

Article:
https://pmc.ncbi.nlm.nih.gov/articles/PMC11919375/

The repository also provides a Contact Owner option.

This identifies the official dataset contact and institutional route. It does not establish who currently holds the project's downloaded copy.

## 5\. Supporting-file availability

|Resource|Current finding|
|-|-|
|Original 20210311.zip|Publicly listed by official repository|
|Internal .hyspex files|Not inspected; unconfirmed|
|Matching .hdr files|Not inspected; unconfirmed|
|Dark-current references|Unconfirmed|
|White-reference files|Unconfirmed|
|Instrument acquisition records|Unconfirmed|
|Original filename-to-pot/side mapping|Historical mapping evidence exists, but separate original mapping file availability is unconfirmed|

The repository landing-page listing does not independently establish the presence of all calibration and acquisition files inside the archive.

## 6\. Project-team contact status

Hiba was previously contacted to identify the project archive holder and supporting files.

As reported by the member, no response had been received as of 20 November 2026, 18:36 IST.

Hiba's status as the original archive holder remains unconfirmed.

Direct email contact: The member reports sending an email to lorraine.latchoumane@inrae.fr on 21 November 2026, requesting confirmation of the original archive contents, calibration references, acquisition records and sample mapping documentation.

Response status: Awaiting a response at the time of this report update.

## 7\. Technical verification status

No original archive was downloaded or inspected.

The following checks remain pending:

* Actual .hdr metadata inspection.
* Spectral wavelengths and band count.
* Raw image dimensions.
* Data type, byte order and binary layout.
* No-data and ignore values.
* Basic raw-data quality checks.
* Calibration-reference correspondence.
* Acquisition-setting consistency.

Published instrument specifications must not be substituted for actual header values.

## 8\. Restrictions observed

* No repeated local archive searches.
* No repeated 96/96 scan verification.
* No archive redownload.
* No modification of raw data.
* No preprocessing or calibration transformations.
* No normalization or feature engineering.
* No model training.
* No SWIR/VNIR/RGB merging.

## 9\. Remaining blockers and next actions

1. Await the response to the email sent to Lorraine Latchoumane on 21 November 2026. If necessary, follow up through the repository Contact Owner option.
2. Ask for confirmation of the archive contents and availability of .hyspex and matching .hdr files.
3. Ask specifically whether dark-current, white-reference and instrument acquisition records are included or separately available.
4. Ask whether an original filename-to-pot/side mapping file exists.
5. Obtain confirmation of the project's working-copy holder from Hiba or the project team.
6. Once files are made available, perform read-only technical verification.

## 10\. Readiness decision

**Official archive access route: Identified.**

**Project working-copy holder: Not identified.**

**Internal archive contents and calibration references: Not verified.**

**Technical verification: Pending access to and inspection of the original files.**

Preprocessing remains on hold.





\---

## 24 November 2026 - Final Access Investigation and Readiness Update

### 1. Official archive access

The official Recherche Data Gouv dataset record was identified.

- Dataset: Early detection of septoria infection on wheat leaves using hyperspectral imaging data
- DOI: https://doi.org/10.57745/WVP0FJ
- Repository: https://entrepot.recherche.data.gouv.fr/dataset.xhtml?persistentId=doi:10.57745/WVP0FJ
- Archive: `20210311.zip`
- Published location: `Data/SWIR`
- Published size: 4.3 GB
- Published MD5: `7ad4e3b5a9a14704af51191269d2e019`
- Access status: Publicly listed.

The public listing confirms an official access route. The archive has not been downloaded, its checksum has not been verified locally, and its internal contents have not been inspected.

### 2. Storage assessment

A PowerShell check on 24 November 2026 reported:

- Available drive: `C:`
- Free space: 172.93 GB
- Storage directory: `C:\TerraSpectra_SWIR\raw\`
- Directory creation: Successful.

The directory is outside the Git repository. Available capacity appears sufficient for the published 4.3 GB archive, but the extracted size and additional storage requirements remain unknown.

**Download status:** Not downloaded. Team approval is required before downloading.

### 3. Supporting-file availability

| Component | Evidence and status |
|---|---|
| `20210311.zip` | Publicly listed; not downloaded or inspected locally |
| Original `.hyspex` files | Internal archive contents unverified |
| Corresponding `.hdr` files | Internal archive contents unverified |
| Dark-current measurements | Internal archive contents unverified |
| White-reference measurements | Internal archive contents unverified |
| Acquisition settings and records | Some instrument details described in the associated paper; original records unverified |
| Sample, pot and side mapping | Public metadata CSVs previously examined; correspondence with original raw files not reverified |

Previously examined metadata and the historical 96/96 filename-to-pot-side matching result are documented in earlier reports. They do not substitute for inspecting the original archive.

### 4. Technical verification checklist

| Verification item | Required evidence | Status |
|---|---|---|
| Spectral wavelength range | Original header or acquisition metadata | Pending |
| Number of spectral bands | Original header and data dimensions | Pending |
| Image dimensions | Header and binary-file consistency | Pending |
| Data type | Header declaration | Pending |
| Byte order | Header declaration and binary interpretation | Pending |
| Binary layout/interleave | Header declaration and file consistency | Pending |
| No-data values | Header and data-quality inspection | Pending |
| Data quality | Read-only inspection of original files | Pending |
| Dark-current correspondence | Matching calibration files and acquisition records | Pending |
| White-reference correspondence | Matching reference files and acquisition records | Pending |
| Acquisition settings | Original instrument records or headers | Pending |
| Sample/pot/side correspondence | Original sample mapping and metadata | Pending |

No technical values have been inferred or marked as verified without original-file evidence.

### 5. Final SWIR recommendation

**Recommendation: 2 - Partially suitable, with clearly documented limitations.**

Evidence:

- An official public dataset record and archive access route have been identified.
- The archive's published size and checksum are documented.
- Supporting metadata CSVs were previously examined.
- Historical filename-to-pot-side matching results are documented.
- C: drive capacity and a separate storage directory have been checked.

Limitations:

- The original archive has not been downloaded or inspected.
- The presence and correspondence of `.hyspex`, `.hdr`, dark-current and white-reference files remain unverified.
- Original acquisition settings and raw-file technical properties have not been verified.
- The extracted archive size is unknown.
- Team approval for downloading has not yet been confirmed.

This recommendation does not certify that SWIR data is ready for preprocessing or model development.

### 6. Remaining actions

1. Obtain team approval before downloading the official archive.
2. Download it to `C:\TerraSpectra_SWIR\raw\` only after approval.
3. Verify the downloaded archive against the published MD5 checksum.
4. Inspect archive contents without modifying original data.
5. Verify raw files, headers and calibration references.
6. Complete the technical checklist using actual file evidence.
7. Update the recommendation if new evidence changes the assessment.

### 7. Work restrictions and completion status

- No raw data was modified.
- No SWIR preprocessing or calibration was performed.
- No feature extraction or model training was performed.
- No archive download was initiated.
- The investigation proceeded without waiting for the depositor's email response.

**Status as of 24 November 2026:** Public access route identified, storage location prepared, and technical readiness limitations documented. Original archive inspection remains pending team approval and data access.

### 8. 25 November 2026 — Official Archive Download and Technical Inventory

#### Archive integrity
- Archive: `20210311.zip`
- Location: `C:\TerraSpectra_SWIR\raw\20210311.zip`
- Downloaded: 25 November 2026
- Size: 4,600,920,431 bytes
- Published MD5: `7ad4e3b5a9a14704af51191269d2e019`
- Local MD5: `7AD4E3B5A9A14704AF51191269D2E019`
- Result: checksum matched.

The archive was inspected read-only without extraction or modification.

#### Archive inventory
- 547 files, 97 folders
- 96 `.hyspex` files and 96 matching `.hdr` files
- 96 `.jpg` files
- 259 `.csv` files
- All files are under `20210311`.

#### Technical verification
All 96 raw/header pairs were checked. No missing matching headers or binary size mismatches were found.

All 96 headers contain 256 wavelength entries, with range 964.181280–2494.388419 nm.

Common configuration:
- 420 lines × 320 samples × 256 bands
- ENVI data type 12 (unsigned 16-bit integer)
- Byte order 0 (little-endian)
- Interleave BIL
- Wavelength units nm
- Data ignore value 16383
- Header offset 1,974,272 bytes

Representative header `01_D.hdr` reports acquisition date 2021-03-11 and start time 08:53:43. Descriptive fields include integration time 12000, frame period 17400, `CalibAvailable = 1`, and 200 background frames. Field units and meanings have not been independently confirmed.

#### CSV structure
The 259 CSVs are distributed across 96 scan folders:
- 70 folders have 3 CSVs
- 23 folders have 2 CSVs
- 3 folders have 1 CSV

All 259 CSVs were structurally checked:
- 922,064 total rows
- Exactly 2 numeric values per row
- No blank or non-numeric rows
- Column 1 range: 114–321
- Column 2 range: 1–307

The CSVs appear to contain coordinate-like annotation pairs; their exact meaning and coordinate convention remain unconfirmed.

#### Limitations and updated assessment
A filename/path search found no separately named dark, white, reference, calibration, acquisition, mapping, metadata, or sample files. This does not rule out information embedded in headers, CSV contents, or external documentation.

The `18_D.hdr` and `18_D.hyspex` files are stored under the `18_G` folder; both are present and size-consistent.

The archive checksum and all 96 raw/header pairs are verified. The dataset is suitable for continued technical research and documentation, but calibration-reference availability, acquisition/sample mapping, annotation semantics, and the folder-placement irregularity require clarification.

No extraction, preprocessing, calibration, feature extraction, or model training was performed.

---

## 26 November 2026 – Read-Only Archive and Annotation Verification

### 1. Wavelength verification across all headers

A read-only script inspected all 96 `.hdr` files in the official archive.

- Headers inspected: 96
- Headers with 256 wavelength entries: 96
- Headers without wavelength lists: 0
- Wavelength range shared by all headers: 964.181280–2494.388419 nm

This confirms that all inspected headers contain a consistent 256-entry wavelength list and the same wavelength range.

### 2. Filename/path search for supporting files

The complete archive filename/path list was searched for terms related to:

`dark`, `white`, `reference`, `calib`, `background`, `acquisition`, `mapping`, `sample`, `metadata`, `annotation`, `readme`, and `wavelength`.

No filename/path matches were found for these terms.

This is a filename/path search only. It does not establish that supporting information is absent from file contents, header fields, or external documentation. Separate dark-current, white-reference, acquisition, or mapping files have not been identified by this search.

### 3. CSV content inspection

Two representative CSVs were read directly from the ZIP without extraction:

- `20210311/01_D/01_D_leaf1.csv`
- `20210311/01_G/01_G_leaf1.csv`

Each contained two numeric values per row. The first rows were coordinate-like pairs. The exact official meaning and order of the CSV columns remain unconfirmed.

### 4. CSV coordinate-range and structural checks

All 259 CSV files were inspected read-only.

- Total rows: 922,064
- Rows per CSV: 1,857–5,010
- Invalid/non-numeric rows: 0
- Duplicate coordinate rows within individual CSV files: 0
- Column 1 range: 114–321
- Column 2 range: 1–307

The verified raw image dimensions are 420 lines × 320 samples.

Two possible coordinate interpretations were tested against these dimensions:

| Assumed coordinate order | Rows outside image bounds |
|---|---:|
| Column 1 = sample, column 2 = line | 37 |
| Column 1 = line, column 2 = sample | 0 |

All 37 rows outside bounds under the first interpretation occur in:

`20210311/24_G/24_G_leaf3.csv`

The first-column values in those rows are:
- 320: 29 rows
- 321: 8 rows

The results strongly support the inferred coordinate order **(line, sample)**. This remains an inference from coordinate ranges, not an officially confirmed annotation convention. No CSV values were changed.

### 5. `18_D` folder-placement irregularity

The following files are present under `20210311/18_G/`:

- `18_D.hdr`
- `18_D.hyspex`
- `18_D.jpg`

The three `18_D` leaf CSV files are present under `20210311/18_D/`.

This is documented as a folder-placement inconsistency. The raw file and matching header are present and were included in the 96/96 structural verification; no missing scan is inferred from the folder placement alone.

### 6. Calibration and biological mapping limitations

The representative header contains `CalibAvailable = 1` and `Number of background = 200`. These header fields do not independently establish the presence or correspondence of separate dark-current and white-reference files, nor do they prove that the raw data are calibrated reflectance.

The following remain unresolved:

- Whether dark-current and white-reference measurements are included or separately available.
- How the CSV coordinate columns are officially defined.
- How each acquisition maps to leaf, plant, pot, side, and biological sample.
- Whether the `18_D` folder placement reflects an original archive organization issue or a packaging mistake.

### 7. Updated SWIR readiness assessment

**Archive integrity and technical structure: verified.**

**Spectral metadata consistency across 96 headers: verified.**

**CSV structural integrity and coordinate-range evidence: verified.**

**Calibration-reference correspondence, official annotation semantics, and biological sample mapping: unresolved.**

The dataset is suitable for continued technical investigation and documentation. It is not yet approved for preprocessing, calibration, feature extraction, or model training. The coordinate order should be described as inferred until confirmed by documentation or visual annotation validation.

No archive extraction, raw-data modification, preprocessing, calibration transformation, feature engineering, or model training was performed during this update.

---

## 8. Investigation addendum - 27 November 2026

This addendum supersedes earlier unresolved statements where new evidence is available. The original report content is retained for investigation history.

### 8.1 Verified findings

**Coordinate and annotation investigation**
- The associated publication documents CSV coordinates as: column 1 = vertical line coordinate; column 2 = horizontal sample coordinate.
- Expected dimensions for the inspected archive are 420 lines and 320 samples.
- Rechecking `24_G_leaf3.csv` under this documented order found 0 out-of-range rows.
- The previously reported 37 unusual rows resulted from checking the coordinate columns in reverse order. They are not confirmed anomalies.

**Biological sample mapping**
- Official `Data_description.csv` contains 279 valid leaf records across 48 pot IDs and 96 pot-side groups.
- The metadata contains genotypes EPO_67 and EPO_68 and treatments Infected and Non-infected.
- All 96 unique scan IDs match the 96 official pot-side groups; no unmatched scan IDs or metadata pot-side pairs were found.
- Genotype and treatment are consistent within all 96 pot-side groups.
- No duplicate pot-side/leaf identifiers were found.
- The scan ID identifies pot and side; the official metadata supplies leaf number, genotype, treatment and confidence level.

**Leaf-coordinate CSV comparison**
- 279 unique biological leaf IDs were found in the metadata.
- 259 unique leaf-coordinate CSV IDs were found in the archive.
- 20 metadata leaf IDs have no matching coordinate CSV.
- 0 coordinate CSV IDs lack a metadata match.
- The affected pot-side scans exist. The sampling table contains recorded counts for these pot-sides, but its date-level aggregate counts do not identify the specific missing leaf CSVs or explain their absence.

Missing coordinate CSV IDs:
`04_D_leaf2`, `04_G_leaf3`, `10_D_leaf1`, `13_D_leaf2`, `13_D_leaf3`, `21_G_leaf3`, `24_D_leaf3`, `25_G_leaf2`, `26_D_leaf3`, `27_D_leaf1`, `28_G_leaf2`, `32_D_leaf3`, `32_G_leaf2`, `32_G_leaf3`, `33_D_leaf1`, `35_D_leaf2`, `45_D_leaf2`, `46_G_leaf2`, `47_D_leaf2`, `47_G_leaf1`.

**Structural placement**
- `18_D.hdr`, `18_D.hyspex` and `18_D.jpg` are stored under `20210311/18_G/`.
- The three `18_D` leaf CSVs are stored under `20210311/18_D/`.
- The `18_D` scan and matching header are present and were included in the 96/96 structural verification.
- This is a confirmed folder-placement inconsistency; it does not indicate a missing scan. The original archive was not modified.

**Calibration evidence**
- A filename search found 0 archive paths containing the searched calibration/reference keywords.
- The inspected header contains `CalibAvailable = 1`, `Number of background = 200`, and `Integration time = 12000`.
- These header fields do not prove that the archived cubes are calibrated reflectance or establish reference-file correspondence.
- The publication describes a reflectance-calibration method using a certified Spectralon SRS99 reference and dark-current measurements. The availability and correspondence of the required reference measurements for this exact archive remain unverified.

### 8.2 Inferred findings

- Pot-side scan IDs can be used to associate scans with pot and side, with the official metadata providing biological labels.
- Leaf-level coordinate extraction is incomplete for the 20 metadata-listed leaf IDs without coordinate CSVs.
- Folder-based matching alone is unsafe for pot 18 because the `18_D` scan files are stored under `18_G`; filename-based matching must account for this exception.

These are evidence-based interpretations, not proof of the cause of missing coordinate files or the folder-placement inconsistency.

### 8.3 Unresolved findings

- Whether the required dark-current and white-reference measurements are included in another file, embedded in the acquisition data, or available separately.
- Whether the archived `.hyspex` cubes have already undergone any reflectance calibration.
- Why the 20 metadata-listed leaf coordinate CSVs are absent.
- Why the `18_D` scan files are placed under the `18_G` folder.
- Whether the dataset is suitable for the team's intended forecasting task, considering its acquisition timeline, biological replication and target definition.

### 8.4 Missing leaf-coordinate CSV inventory

The comparison reported:

- **279 unique leaf IDs** in the official metadata.
- **259 unique leaf-coordinate CSV IDs** in the archive.
- **20 metadata leaf IDs** without a matching coordinate CSV.
- **0 coordinate CSV IDs** without a metadata match.

The 20 missing coordinate-file IDs are:

`04_D_leaf2`, `04_G_leaf3`, `10_D_leaf1`, `13_D_leaf2`, `13_D_leaf3`, `21_G_leaf3`, `24_D_leaf3`, `25_G_leaf2`, `26_D_leaf3`, `27_D_leaf1`, `28_G_leaf2`, `32_D_leaf3`, `32_G_leaf2`, `32_G_leaf3`, `33_D_leaf1`, `35_D_leaf2`, `45_D_leaf2`, `46_G_leaf2`, `47_D_leaf2`, `47_G_leaf1`.

These are **missing leaf-coordinate CSV files**, not evidence that the corresponding hyperspectral scans are missing. The pot-side scans for the affected IDs were found. `SWIR_data.csv` contains date-level aggregate counts for pot-sides, but those totals do not identify the specific absent leaf CSVs or explain why they are absent.

The reported comparison used the metadata leaf identifiers constructed from pot, side and leaf fields and compared them with the leaf IDs parsed from archive CSV filenames. A dedicated comparison script or saved machine-readable inventory was not located in the repository search. The counts and full missing-ID list above are retained as the available investigation evidence; independent script-based reproduction remains a gap.

### 8.5 Pot 18 folder-placement inconsistency

The archive paths show:

- `20210311/18_G/18_D.hdr`
- `20210311/18_G/18_D.hyspex`
- `20210311/18_G/18_D.jpg`
- The three `18_D` leaf-coordinate CSVs are under `20210311/18_D/`.

The `18_D` scan and matching header are present and were included in the 96/96 structural verification. This is a confirmed folder-placement inconsistency; it does not indicate a missing scan. The original archive was not modified. The reason for the placement remains unknown.

### 8.6 Calibration evidence and limitations

The publication describes reflectance calibration using sample intensity \(I\), dark intensity \(I_d\), and reference intensity \(I_0\), with a certified Spectralon SRS99 reference and dark-current measurements. It also describes the `.hyspex` signal as dark-current-corrected intensity.

That publication describes the method; it does **not** establish that the required reference measurements are available for, or correctly correspond to, this exact downloaded archive. The investigation's filename/path search found no separately named calibration/reference files among the searched terms. A filename search cannot rule out information embedded in data/header contents or separately supplied outside the archive.

The inspected header's `CalibAvailable = 1`, `Number of background = 200`, and `Integration time = 12000` fields are not sufficient proof that the archived cubes are calibrated reflectance, nor do they establish reference-file identity, acquisition correspondence, or calibration provenance. Calibration provenance therefore remains unresolved.

### 8.7 Final suitability recommendation

**Suitable for continued work**
- Metadata investigation and review.
- Coordinate and annotation review.
- Scan-to-pot-side mapping.
- Planning exploratory analysis.

**Potentially suitable, subject to explicit limitations**
- Read-only, descriptive exploratory analysis of the archive's **dark-current-corrected intensity values**, if the analysis is clearly labeled as uncalibrated intensity and does not interpret values as reflectance. This is a conditional option, not a declaration that calibration is complete or that the dataset supports the project's forecasting objective.

**Not yet approved**
- Reflectance-based spectral interpretation without verified calibration provenance.
- Calibration transformations.
- Preprocessing and feature extraction.
- Model training and forecasting.

Evidence supporting this cautious decision includes the verified archive checksum and raw/header structure, consistent header wavelength entries, documented coordinate convention, coordinate-range results, and scan-to-pot-side metadata matches. Limitations include unresolved reference-measurement correspondence, no independent visual annotation validation, 20 missing coordinate CSVs, unresolved biological replication/grouping, the pot 18 path inconsistency, and no demonstrated forecasting target/validation design. The dataset should not be forced into a forecasting objective if the acquisition timeline and biological design do not support it.

### 8.8 Supporting evidence references and gaps

| Finding | Available source/path | Evidence status |
|---|---|---|
| Coordinate convention | Publication, Sections 3 and 4.3; DOI above | Publication-documented |
| Coordinate range check | Archive `C:\TerraSpectra_SWIR\raw\20210311.zip`; member `20210311/24_G/24_G_leaf3.csv`; archive-wide CSV checks summarized above | Historical check result reported; dedicated script/output not located |
| 96/96 scan-to-pot-side match | `C:\Users\MUHAMMED ADINAN\Downloads\Data_description.csv`; archive scan IDs | Historical comparison result reported; dedicated script/output not located |
| 279 vs 259 and missing 20 IDs | `Data_description.csv`; ZIP CSV member paths; list in Section 8.4 | Historical comparison result and complete list retained; dedicated script/output not located |
| Pot 18 path placement | ZIP members listed in Section 8.5 | Archive path inventory |
| Calibration investigation | Publication Sections 4.1 and 4.3; representative member `20210311/01_D/01_D.hdr`; archive filename/path search | Method is publication-documented; archive reference correspondence unresolved |
| Sampling-count context | `C:\Users\MUHAMMED ADINAN\Downloads\SWIR_data.csv` | Aggregate counts only; does not identify individual missing coordinate files |

The local archive was previously reported as checksum-matched to the repository's published MD5 and inspected read-only. No raw data were modified. A repository search for likely `*SWIR*.py`, `*SWIR*.ps1`, `*coordinate*.py`, and `*metadata*.py` files returned no output, and the `research\SWIR` listing showed reports rather than a dedicated validation script. This report therefore identifies the evidence that is available and explicitly records the missing reproducibility artifacts instead of inventing script names or paths.

### 8.9 Final quality and status check

- Historical investigation sections retained.
- Verified, inferred and unresolved findings separated.
- Numerical counts and the full missing-ID list retained.
- Publication title, authors, year, journal, article number, DOI and relevant sections included.
- Today's readiness wording was refined to distinguish dark-current-corrected intensity from verified reflectance.
- The earlier `git diff --check` completed without whitespace errors; it must be rerun after adding these sections.
- UTF-8 text was used when saving the earlier wording update; verify encoding and formatting again after this full revision.
- No new raw-data or archive changes made.
- No calibration, preprocessing, feature extraction, or model training performed.

**Status:** Revised report content prepared for review. No commit, push, merge, or central project-document update has been made.
