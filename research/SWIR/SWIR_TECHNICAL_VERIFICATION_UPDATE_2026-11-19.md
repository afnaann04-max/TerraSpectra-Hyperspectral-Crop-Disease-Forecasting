# SWIR Technical Verification and Preprocessing Readiness Update



**Project:** TerraSpectra – Hyperspectral Crop Disease Forecasting

**Date:** 19 November 2026

**Branch:** Fahma

**Previous readiness assessment:** `SWIR_DATA_READINESS_ASSESSMENT_2026-11-18.md`

**Previous commit:** `dd5e954`



---



## 1. Objective



Continue the SWIR investigation by resolving original-data access, preparing technical verification and refining the preprocessing-readiness decision.



This update builds on the 18 November assessment. Previously completed metadata investigation and historical 96/96 scan verification are not repeated.



## 2. Original SWIR Data Access Status



As of 19 November 2026, confirmation from the teammate regarding the location and availability of the original SWIR files has not been received.



The following resources remain unconfirmed or unavailable for this investigation:



| Required resource | Current status |

|---|---|

| Original `20210311.zip` archive | Not located in previously searched local folders |

| Extracted `.hyspex` files | Not located in previously searched local folders |

| Matching `.hdr` files | Not located in previously searched local folders |

| Dark-current calibration files | Availability unconfirmed |

| White-reference calibration files | Availability unconfirmed |

| Original instrument acquisition records | Availability unconfirmed |

| Detailed filename-to-pot/side mapping evidence | Not separately available |



**Access blocker:** The person currently holding the original downloaded archive and associated calibration files has not yet been identified.



**Required action:** Obtain confirmation from the project teammate or dataset holder about the storage location and access arrangements.



No archive was downloaded again.



## 3. Technical Verification Status



Actual header and raw-data inspection cannot proceed until the original files are available.



| Verification item | Status |

|---|---|

| Wavelength values and spectral band count | Blocked – headers unavailable |

| Image dimensions | Blocked – headers unavailable |

| Data type | Blocked – headers unavailable |

| Byte order | Blocked – headers unavailable |

| Binary layout and data offset | Blocked – headers unavailable |

| Ignore/no-data values | Blocked – headers unavailable |

| Invalid and non-finite raw measurements | Not tested |

| Saturation and unusual values | Not tested |

| Acquisition settings | Not verified against actual headers |

| Calibration information | Calibration files unavailable or unconfirmed |

| Consistency across scans | Not verified |



The published instrument specifications recorded in the previous assessment remain reference information only. They must not be substituted for actual per-file header values.



## 4. Technical Verification Plan



When the original files become available, perform the following read-only checks:



### 4.1 Header inspection



- Identify all available header files.

- Extract the wavelength list and spectral band count.

- Record image dimensions and number of bands.

- Identify data type, byte order, interleave format and header offset.

- Record ignore/no-data values.

- Compare relevant fields across available scans.



### 4.2 Raw-data quality checks



- Check whether raw values can be interpreted using the documented binary layout.

- Identify NaN and infinite values, if applicable to the data representation.

- Check for saturation and unexpected numeric ranges.

- Examine potential invalid or ignored pixels.

- Record scan-specific inconsistencies.

- Preserve original files without modification.



### 4.3 Calibration review



- Identify dark-current reference information.

- Identify white-reference or Spectralon reference information.

- Confirm the documented calibration procedure.

- Establish whether reference files correspond to the relevant acquisition sessions.



No calibration or reflectance transformation should be applied until the required reference information and procedure are confirmed.



## 5. Proposed Preprocessing Workflow



The following workflow is a preparation plan, not an executed pipeline.



| Stage | Planned action | Current decision |

|---|---|---|

| 1 | Preserve original files and record file inventory | Can be performed after access |

| 2 | Parse and validate headers | Waiting for `.hdr` files |

| 3 | Confirm binary layout and read-only data interpretation | Waiting for header information |

| 4 | Validate wavelengths and spectral dimensions | Waiting for headers |

| 5 | Inspect invalid values and scan quality | Waiting for raw data |

| 6 | Review dark-current and white-reference information | Waiting for calibration files |

| 7 | Apply documented reflectance calibration | Requires confirmed calibration procedure |

| 8 | Identify unreliable spectral bands | Requires spectral quality evidence |

| 9 | Decide on justified smoothing or normalization | Requires data inspection and approval |

| 10 | Handle missing observations | Requires confirmed missing-data strategy |

| 11 | Validate and document processed outputs | After approved preprocessing |



### 5.1 Steps that can be prepared now



- Define the file-inventory format.

- Prepare a header-validation checklist.

- Define the quality-control measurements to record.

- Document the expected preprocessing stages.

- Identify required calibration information.

- Prepare a reproducibility and logging structure.



### 5.2 Steps that must wait



- Reading actual binary image values.

- Selecting or removing spectral bands.

- Applying dark-current correction.

- Computing reflectance.

- Applying normalization or smoothing.

- Interpolating missing observations.

- Generating analysis-ready SWIR data.



These operations require actual data inspection, confirmed technical information and appropriate team approval.



## 6. Existing Evidence Retained



The following previous findings remain valid as documented historical evidence:



- Official dataset DOI: `10.57745/WVP0FJ`.

- Historical scan verification: 96 expected and 96 matched scans.

- Historical duplicate and missing scan counts: zero.

- Previously documented metadata structure: 48 pots, two genotypes, two treatments and 18 time points.

- Previously published instrument specifications are recorded in the 18 November assessment.



These checks were not repeated on 19 November.



## 7. Remaining Blockers for the Central Tracker



| Blocker | Required information | Responsible party |

|---|---|---|

| Original archive access | Archive location or access permission | To be identified by project teammate |

| Raw SWIR files | Original `.hyspex` files | Dataset holder |

| Header information | Matching `.hdr` files | Dataset holder |

| Calibration references | Dark-current and white-reference files | Dataset holder |

| Instrument settings | Acquisition protocol and settings | Dataset holder or experiment documentation |

| Scan mapping evidence | Original filename-to-pot/side mapping | Original investigator or previous verification records |



The responsible individuals are not yet confirmed.



## 8. Final Readiness Decision



**Current decision: Not ready for SWIR preprocessing execution.**



The project has sufficient previous documentation to prepare a preprocessing plan. However, raw-file access, header-level validation and calibration confirmation remain outstanding.



Technical verification and preprocessing readiness must be reassessed once the original files are accessible.



The next project milestone is obtaining the original SWIR files and calibration references, followed by read-only technical validation.



## 9. Work Restrictions



During this update:



- No archive was downloaded again.

- No historical scan matching was repeated.

- No raw data was modified.

- No preprocessing was executed.

- No VNIR or RGB data was merged.

- No machine-learning model was trained.

- No unsupported acquisition values were assumed.



**Report status:** Technical verification preparation completed; original-data access remains blocked.
