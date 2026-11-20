# SWIR Original Data Access Follow-up

**Date:** 20 November 2026
**Member:** Fahma (Member 2)
**Branch:** Fahma
**Previous technical update:** `SWIR_TECHNICAL_VERIFICATION_UPDATE_2026-11-19.md`
**Previous commit:** `7e3caa8`

## 1. Objective

Follow up on access to the original SWIR dataset and supporting technical files so that read-only technical verification can proceed.

This report records the access status as of 20 November 2026. It does not repeat the completed dataset investigation or historical scan verification.

## 2. Contact status

- **Contact:** Hiba (project team member).
- **Purpose:** Identify who currently holds the original SWIR archive and determine how access can be provided.
- **Requested information:** Original `20210311.zip` archive, `.hyspex` files, matching `.hdr` files, dark-current references, white-reference calibration files, instrument acquisition records, and original filename-to-pot/side mapping information.
- **Response status:** No reply received as of 20 November 2026, 18:36 IST.
- **Dataset ownership:** Hiba's status as the original dataset holder has not been confirmed.

The contact status above is based on the member's reported communication. No archive location or access permission has been confirmed.

## 3. Original data and supporting-file access

| Resource | Status |
|---|---|
| Original `20210311.zip` archive | Access not confirmed |
| Original `.hyspex` files | Availability not confirmed |
| Matching `.hdr` files | Availability not confirmed |
| Dark-current references | Availability not confirmed |
| White-reference calibration files | Availability not confirmed |
| Instrument acquisition records | Availability not confirmed |
| Original filename-to-pot/side mapping | Availability not confirmed |

No new file access or technical evidence was obtained during this follow-up.

## 4. Technical verification status

Actual technical verification remains blocked because the original files have not been made available.

The following checks therefore remain pending:

- Header wavelength and band information.
- Image dimensions.
- Data type, byte order, and binary layout.
- No-data or ignore values.
- Basic raw-data quality checks.
- Calibration-reference availability and correspondence to scans.
- Acquisition-setting consistency across scans.

Published instrument specifications are not treated as verified values from the original headers.

## 5. Work completed and restrictions

- Follow-up communication with Hiba was reported; no response had been received by the reporting time.
- Existing investigation reports were retained.
- Historical 96/96 scan verification was not repeated.
- Previous local searches were not repeated.
- The original archive was not downloaded again.
- No raw data was modified.
- No preprocessing, calibration transformation, normalization, or model training was performed.
- No SWIR, VNIR, or RGB data was merged.

## 6. Remaining blockers

1. The person currently holding the original SWIR archive is still unidentified.
2. The location and access method for `20210311.zip` are unconfirmed.
3. Availability of the original scan files and supporting calibration records is unconfirmed.
4. Header-level and raw-data technical verification cannot begin without access to the original files.

## 7. Next action

Await Hiba's response. If she does not hold the archive, request the name of the responsible dataset holder or project contact.

Once access is provided, perform the assigned read-only technical checks while preserving all original files.

## 8. Readiness decision

**Status: Not ready for technical verification or preprocessing execution.**

The access blocker remains unresolved as of 20 November 2026. Preprocessing must remain on hold until the original data, relevant headers, and required calibration information are available and verified.
