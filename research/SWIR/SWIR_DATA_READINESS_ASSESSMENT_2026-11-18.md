\# SWIR Data Readiness and Preprocessing Feasibility Assessment



\*\*Project:\*\* TerraSpectra â€“ Hyperspectral Crop Disease Forecasting

\*\*Investigation date:\*\* 18 November 2026

\*\*Dataset:\*\* Early detection of septoria infection on wheat leaves using hyperspectral imaging data

\*\*Source:\*\* Recherche Data Gouv

\*\*DOI:\*\* 10.57745/WVP0FJ

\*\*Investigation scope:\*\* SWIR data readiness and preprocessing feasibility



\---



\## 1. Objective



Assess whether the existing SWIR dataset has sufficient documented structure, metadata and technical information to support a reliable preprocessing workflow.



This investigation is limited to reviewing existing documentation and available evidence. It does not include downloading the archive again, modifying raw data, repeating the historical scan-matching exercise, executing preprocessing or training machine-learning models.



\## 2. Dataset Inventory and Existing Evidence



The official repository inventory previously documented the following SWIR-related files:



| File | Repository location | Published size | Existing evidence |

|---|---|---:|---|

| 20210311.zip | Data/SWIR | 4.3 GB | Official listing verified; historical scan verification documented |

| SWIR\_data.csv | Data annotation | 5.5 KB | Metadata contents previously reviewed |

| Data\_description.csv | Data annotation | 9.2 KB | Metadata contents previously reviewed |



Official dataset DOI: https://doi.org/10.57745/WVP0FJ



Official archive MD5 reference:



`7ad4e3b5a9a14704af51191269d2e019`



The checksum is a repository reference only. Local checksum verification and ZIP integrity testing were not performed during this investigation.



\### 2.1 Historical scan verification



Previously documented results:



\- Expected scans: 96

\- Actual scans: 96

\- Unique scan identities: 96

\- Duplicate identities: 0

\- Missing scans: 0

\- Unexpected or unmatched identities: 0



A folder anomaly was previously recorded: `18\_D.hyspex` was stored inside the `18\_G` folder, although its filename was correct.



These are historical findings. The verification was not repeated on 18 November.



\## 3. Metadata Readiness



The earlier metadata review documented:



\- 48 pot records.

\- Two genotypes: `EPO\_67` and `EPO\_68`.

\- Two treatments: infected and non-infected.

\- 18 acquisition time points, from -1 to 20 days post-inoculation.

\- G and D represent the two pot sides.

\- Numeric cells represent leaf counts.

\- Empty cells indicate no hyperspectral acquisition.

\- An explicit `NA` was recorded for pot 23 at 10 dpi on the G side.

\- The leaf-level description contains 279 records.

\- Confidence levels include 246 level-1 records and 33 level-2 records.



The metadata review also identified that the CSV files do not provide all instrument acquisition settings or exact calendar acquisition dates.



\*\*Limitation:\*\* The original CSV files were not located in the local folders searched on 18 November. These findings are based on the earlier metadata investigation and existing documentation, not a fresh local CSV inspection.



\## 4. Raw SWIR File and Header Inspection



The local project folder and searched user directories did not contain the original `.hyspex` files or identifiable SWIR header files.



The `.hdr` files encountered during the search belonged to installed Astropy package test data and were not treated as SWIR dataset headers.



Consequently, the following checks could not be performed:



| Technical property | Status |

|---|---|

| Per-file wavelength arrays | Not verified |

| Spectral band count from actual headers | Not verified |

| Raw image dimensions | Not verified locally |

| Data type and byte order | Not verified |

| Header offsets and binary layout | Not verified |

| Ignore/no-data values | Not verified |

| Per-file acquisition settings | Not verified |

| Header consistency across scans | Not verified |

| Invalid, non-finite or out-of-range raw values | Not tested |



\### 4.1 Published instrument information



The associated 2025 research paper reports the following SWIR instrument information:



\- Camera: HySpex SWIR-384.

\- Manufacturer: Norsk Elektro Optikk (NEO).

\- Acquisition type: Pushbroom.

\- Study spectral range: 964â€“2494 nm.

\- Reported spectral samples: 256.

\- Image resolution: 420 Ã— 320 pixels.

\- Camera-to-leaf distance: 21.5 cm.

\- Lens focal distance: 30 cm.

\- Pixel dimensions: 217 Ã— 217 Âµm.



These are published study specifications, not values independently extracted from the actual local headers.



The paper does not establish all per-scan acquisition parameters needed for reproducible preprocessing. Exact integration time, frame period and scan speed remain unverified in this investigation.



\## 5. Data Quality Considerations



The following issues should be considered before preprocessing:



1\. \*\*Missing observations:\*\* Empty metadata cells represent unavailable acquisitions and should not automatically be treated as zero-valued measurements.

2\. \*\*Explicit missing-value marker:\*\* The previously identified `NA` entry requires preservation and interpretation.

3\. \*\*Confidence levels:\*\* The two confidence categories should be retained as metadata and not silently discarded.

4\. \*\*Folder inconsistency:\*\* The historical `18\_D.hyspex` placement anomaly should be documented and checked if the original archive is available.

5\. \*\*Acquisition differences:\*\* Header-level consistency across scans has not been established.

6\. \*\*Invalid raw values:\*\* NaN, infinity, saturation and instrument-specific ignore values have not been checked because raw files were unavailable.

7\. \*\*Spectral quality:\*\* No local assessment of noisy bands, detector artefacts or scan-specific spectral abnormalities was possible.



No unverified quality issue is being reported as an observed defect.



\## 6. Proposed SWIR Preprocessing Workflow



\*\*This is a proposed workflow only. It has not been executed.\*\*



| Stage | Proposed check or operation | Rationale |

|---|---|---|

| 1. File inventory | Record filenames, sizes and checksums | Establish traceability |

| 2. Header parsing | Extract dimensions, bands, data type, byte order and wavelength information | Confirm binary interpretation |

| 3. Header validation | Compare technical fields across scans | Identify acquisition inconsistencies |

| 4. Raw-value validation | Check non-finite values, ignore values, saturation and invalid ranges | Detect corrupted or unusable measurements |

| 5. Wavelength validation | Verify wavelength ordering, range and band count | Ensure spectral-axis correctness |

| 6. Calibration review | Confirm dark-current and reference-panel information | Avoid incorrect reflectance calculations |

| 7. Reflectance processing | Apply the documented calibration procedure once acquisition details are confirmed | Produce physically interpretable measurements |

| 8. Spectral quality assessment | Identify noisy or unreliable bands using evidence and instrument documentation | Avoid arbitrary band removal |

| 9. Spatial quality assessment | Examine scan dimensions and spatial artefacts | Identify unusable image regions |

| 10. Missing-data handling | Preserve missingness and document any justified handling method | Prevent false observations |

| 11. Output validation | Record processing parameters and verify output dimensions and values | Ensure reproducibility |



No interpolation, normalization, smoothing, band removal or other transformation should be selected until the raw header information and calibration requirements are confirmed.



\## 7. Unresolved Technical Questions



The following information is still required:



\- Access to the original SWIR raw files and corresponding headers.

\- Confirmation of the exact binary format and data layout.

\- Per-file wavelength information and spectral band count.

\- Instrument ignore/no-data values and their interpretation.

\- Integration time, frame period and scan speed, where available.

\- Dark-current and reference-panel files or documented calibration procedure.

\- Confirmation of whether acquisition settings changed between scans.

\- Original detailed scan filename and pot-side mapping evidence, if reproducible audit evidence is required.



\## 8. Readiness Assessment



| Area | Assessment |

|---|---|

| Official dataset identification | Previously verified |

| Metadata structure | Previously reviewed |

| Historical scan matching | Documented |

| Published instrument specifications | Available from research paper |

| Local raw-file availability | Not established |

| Header-level technical validation | Blocked |

| Raw-value quality assessment | Pending |

| Preprocessing design | Proposed |

| Preprocessing execution | Not started |



\*\*Overall assessment: Conditionally ready for preprocessing planning, but not ready for preprocessing execution.\*\*



The existing documentation provides a useful understanding of the dataset, its experimental design and its metadata. However, actual raw SWIR files and headers must be available before technical validation and preprocessing can be performed reliably.



\## 9. Investigation Limitations and Restrictions



During this investigation:



\- The SWIR archive was not downloaded again.

\- The historical 96/96 scan verification was not repeated.

\- Raw data was not modified.

\- No preprocessing was executed.

\- No VNIR or RGB data was merged.

\- No machine-learning model was trained.

\- No acquisition settings were invented or assumed.

\- No Git commit or push was performed.



\## 10. Recommendation



Retain the existing SWIR investigation findings and obtain access to the original raw SWIR files and headers before proceeding with technical validation.



Once those files are available, perform header inspection and raw-value quality checks first. Only after confirming the binary layout, wavelengths, missing-value conventions and calibration requirements should the proposed preprocessing workflow be finalized and executed.



\*\*Report status:\*\* Initial readiness assessment â€“ evidence and limitations documented.
