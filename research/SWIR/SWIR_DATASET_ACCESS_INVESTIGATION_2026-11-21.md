# SWIR Dataset Access Investigation

**Date:** 21 November 2026
**Member:** Fahma (Member 2)
**Branch:** Fahma
**Previous access report:** SWIR_ACCESS_FOLLOWUP_2026-11-20.md
**Previous commit:** a537079

## 1. Objective

Identify the official SWIR dataset holder and access route, establish the public availability of the original archive, and determine whether technical verification can proceed.

No previous local searches or historical scan verification were repeated.

## 2. Official dataset source — independently verified

- Dataset: Early detection of septoria infection on wheat leaves using hyperspectral imaging data.
- DOI: 10.57745/WVP0FJ
- Repository: Recherche Data Gouv.
- Depositor and repository point of contact: Lorraine Latchoumane.
- Associated institution: INRAE.
- Repository file access: Public.
- Licence: Etalab Open License 2.0.
- Publication date: 15 November 2024.

Official dataset:
https://entrepot.recherche.data.gouv.fr/dataset.xhtml?persistentId=doi:10.57745/WVP0FJ

## 3. Original archive availability — independently verified

The official repository file listing includes:

- Filename: 20210311.zip
- Repository path: Data/SWIR/20210311.zip
- Listed size: 4.3 GB
- Access status: Public
- Publication date: 15 November 2024
- Listed MD5: 7ad4e3b5a9a14704af51191269d2e019

The public repository listing establishes an official access route for this archive.

Important limitation: The archive was not downloaded or inspected during this investigation. Its internal contents have not been verified.

## 4. Dataset contact and responsible institution

The repository identifies Lorraine Latchoumane (INRAE) as the dataset point of contact and depositor.

The 2025 associated data article lists the corresponding author's email:

lorraine.latchoumane@inrae.fr

Article:
https://pmc.ncbi.nlm.nih.gov/articles/PMC11919375/

The repository also provides a Contact Owner option.

This identifies the official dataset contact and institutional route. It does not establish who currently holds the project's downloaded copy.

## 5. Supporting-file availability

| Resource | Current finding |
|---|---|
| Original 20210311.zip | Publicly listed by official repository |
| Internal .hyspex files | Not inspected; unconfirmed |
| Matching .hdr files | Not inspected; unconfirmed |
| Dark-current references | Unconfirmed |
| White-reference files | Unconfirmed |
| Instrument acquisition records | Unconfirmed |
| Original filename-to-pot/side mapping | Historical mapping evidence exists, but separate original mapping file availability is unconfirmed |

The repository landing-page listing does not independently establish the presence of all calibration and acquisition files inside the archive.

## 6. Project-team contact status

Hiba was previously contacted to identify the project archive holder and supporting files.

As reported by the member, no response had been received as of 20 November 2026, 18:36 IST.

Hiba's status as the original archive holder remains unconfirmed.

Direct email contact: The member reports sending an email to lorraine.latchoumane@inrae.fr on 21 November 2026, requesting confirmation of the original archive contents, calibration references, acquisition records and sample mapping documentation.

Response status: Awaiting a response at the time of this report update.

## 7. Technical verification status

No original archive was downloaded or inspected.

The following checks remain pending:

- Actual .hdr metadata inspection.
- Spectral wavelengths and band count.
- Raw image dimensions.
- Data type, byte order and binary layout.
- No-data and ignore values.
- Basic raw-data quality checks.
- Calibration-reference correspondence.
- Acquisition-setting consistency.

Published instrument specifications must not be substituted for actual header values.

## 8. Restrictions observed

- No repeated local archive searches.
- No repeated 96/96 scan verification.
- No archive redownload.
- No modification of raw data.
- No preprocessing or calibration transformations.
- No normalization or feature engineering.
- No model training.
- No SWIR/VNIR/RGB merging.

## 9. Remaining blockers and next actions

1. Await the response to the email sent to Lorraine Latchoumane on 21 November 2026. If necessary, follow up through the repository Contact Owner option.
2. Ask for confirmation of the archive contents and availability of .hyspex and matching .hdr files.
3. Ask specifically whether dark-current, white-reference and instrument acquisition records are included or separately available.
4. Ask whether an original filename-to-pot/side mapping file exists.
5. Obtain confirmation of the project's working-copy holder from Hiba or the project team.
6. Once files are made available, perform read-only technical verification.

## 10. Readiness decision

**Official archive access route: Identified.**

**Project working-copy holder: Not identified.**

**Internal archive contents and calibration references: Not verified.**

**Technical verification: Pending access to and inspection of the original files.**

Preprocessing remains on hold.
