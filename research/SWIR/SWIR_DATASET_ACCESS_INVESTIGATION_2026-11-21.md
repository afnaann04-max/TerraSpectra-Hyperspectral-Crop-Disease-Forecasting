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
