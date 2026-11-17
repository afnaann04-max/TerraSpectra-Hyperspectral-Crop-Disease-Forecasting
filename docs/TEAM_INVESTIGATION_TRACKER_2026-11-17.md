# TerraSpectra Team Investigation Tracker

**Date:** 17 November 2026
**Project stage:** Dataset investigation, evidence verification and suitability assessment

## 1. Team responsibilities

| Member | Responsibility | Assigned datasets |
|---|---|---|
| Hiba | VNIR investigation, coordination and integration | Wheat Septoria VNIR |
| Member 2 | SWIR investigation | Wheat Septoria SWIR |
| Member 3 | RGB investigation | NWRD Wheat Rust, CCMT Tomato, Rice Sheath Blight |

## 2. Existing dataset availability

Current known dataset status based on previous investigations:

| Dataset | Existing local status |
|---|---|
| Wheat Septoria VNIR | Available; selected scans investigated and suitability assessed |
| Wheat Septoria SWIR | Official archive previously downloaded; historical 96/96 expected pot-side scan matches documented |
| NWRD Wheat Rust | Not located in previously searched project folders; source investigation pending |
| CCMT Tomato | Not located in previously searched project folders; source investigation pending |
| Rice Sheath Blight | Initial source and severity-label investigation completed; archive contents not yet fully verified |

Not located in searched project folders does not mean publicly unavailable. External source and access verification must be documented separately.

## 3. Team responsibilities and investigation requirements

### Member 2 — SWIR Wheat Septoria

- Verify and document the original dataset source and download details.
- Check licence and usage conditions.
- Review the existing 96/96 expected pot-side scan matching evidence without repeating the matching process.
- Investigate SWIR camera and instrument specifications.
- Review spectral range and available acquisition settings.
- Investigate missing time points and technical NA information.
- Record unresolved metadata and experimental-design questions.

### Member 3 — RGB datasets

Investigate each dataset separately:

1. NWRD Wheat Rust
2. CCMT Tomato
3. Rice Sheath Blight

For each dataset:

- Verify the original source.
- Check access and availability.
- Verify licence information, if available.
- Inspect the folder structure when files are available.
- Prepare an initial file inventory.
- Verify image labels and annotation information.
- Record unknowns and evidence sources.

### Hiba — Coordination and VNIR

- Conduct VNIR dataset investigation and suitability assessment.
- Review Member 2 and Member 3 submissions.
- Collect source and access evidence.
- Track blockers and unresolved questions.
- Maintain the central project documentation.
- Assess dataset suitability and experimental-design limitations.
- Keep different modalities separate until compatibility is established.

## 4. Required evidence from team members

Each member must provide, where available:

- Original dataset source or download link.
- Access or download confirmation.
- Licence information.
- Folder structure.
- File names, formats and verified counts.
- Metadata and annotation information.
- Errors and unresolved issues.
- Supporting references and evidence.
- Initial or updated investigation report.

Claims must be distinguished as verified findings, previously documented results, team-reported information or unresolved questions.

## 5. Current progress status

| Work item | Status |
|---|---|
| VNIR investigation | Completed for the selected available scans; suitability assessment documented |
| VNIR calibration provenance | Investigated; application of reflectance calibration to local NPZ files remains unverified |
| SWIR source verification | Completed and documented |
| SWIR historical 96/96 scan matching | Previously documented; original standalone filename list and matching table not preserved separately |
| SWIR instrument and metadata investigation | Completed and documented; some acquisition settings remain unresolved |
| SWIR final investigation report | Submitted and reviewed by Hiba |
| SWIR Git handover | Completed; commit `09e134e` pushed to `Fahma` |
| SWIR documentation files pushed | Five files confirmed by Member 2 |
| RGB Rice Sheath Blight initial source investigation | Completed |
| Rice Sheath Blight severity-label investigation | Completed with remaining annotation questions |
| NWRD Wheat Rust investigation | Latest submission status requires confirmation |
| CCMT Tomato investigation | Pending further source verification |

Statuses will be updated only after reviewing actual evidence.

## 5A. Daily progress update — 15 November 2026

### Hiba — VNIR

- Completed the day's VNIR data-quality and calibration assessment documentation.
- Recorded missing-value and spectral-gap findings.
- Documented the 30 validation comparisons across 10 VNIR files and three CSV references.
- Created `VNIR_PROGRESS_REPORT_2026-11-15.md`.
- Calibration provenance, full-dataset class counts and biological replication remained unresolved.
- Documentation committed and pushed to GitHub in commit `77602be`.

### Member 2 — SWIR

- Completed the initial investigation task.
- Submitted investigation files for review.
- Evidence review and further SWIR validation remained pending.

### Member 3 — RGB

- Completed the initial source investigation of the Rice Sheath Blight candidate dataset.
- Identified the Mendeley Data record: DOI `10.17632/489spnkhp5.1`.
- Recorded the reported 1,609 original JPG images, six severity levels and CC BY 4.0 licence.
- Documented dataset characteristics, preliminary suitability and unresolved questions.
- Dataset retained as a candidate; final selection was not approved.
- Created `RGB_PROGRESS_REPORT_2026-11-15.md`.

**Unresolved Rice dataset questions:**

- Exact names, codes and definitions of the six severity levels.
- Annotation file format and image-to-label mapping.
- Whether original and augmented images are stored separately.
- Internal archive structure and class-wise image counts.

## 5B. Original assignments — 16 November 2026

The assignments below were issued before the day's investigation reviews.

- Hiba: Review submitted team evidence and document verified findings.
- Member 2: Continue SWIR investigation and address evidence gaps.
- Member 3: Verify Rice Sheath Blight severity labels and annotation details.

Completion and current status are recorded in Section 5C.

## 5C. Daily progress update — 16 November 2026

### Hiba — VNIR and coordination

- Reviewed Member 2's updated SWIR investigation submission and all four supporting documents.
- Reviewed Member 3's Rice Sheath Blight severity-label verification report.
- Created the RGB and SWIR daily progress reports.
- Updated the central team investigation tracker.
- Existing VNIR findings remained documented in the previous progress reports.

### Member 2 — SWIR Wheat Septoria

- Completed the assigned metadata investigation and submitted four updated documents.
- Verified that the MD5 checksums of both supplied metadata CSV files matched the official repository checksums.
- Confirmed the reported DOI and Etalab Open License 2.0 information.
- Documented 48 pots, 279 leaf-level metadata records, 18 reported time points and metadata limitations.
- The separate 96-scan filename list and matching table were not supplied for independent review.
- Acquisition settings, exact filename convention, biological replication and other experimental details remained unresolved.
- No archive re-download, preprocessing or model training was performed.

### Member 3 — RGB Rice Sheath Blight

- Completed the severity-label verification task.
- Official dataset description reports six progressive severity levels and image-level severity annotation.
- Exact class names, codes, definitions, scoring boundaries and annotation-file mapping remained unverified.
- The dataset remained a candidate, not an approved final dataset.
- Member 3 committed and pushed the revised report to the Afnan branch in commit `192d033`.

## 5D. Daily progress update — 17 November 2026

### Hiba — VNIR

- Investigated local VNIR reflectance-calibration provenance. Application of reflectance calibration to the processed NPZ files remains unverified.
- Inspected four VNIR headers, all recording an ignore value of 4095. The inspected SWIR header records 16383; these are treated as modality-specific observations for the inspected files.
- Compared 10 original and corrected VNIR NPZ file pairs. Raw spectra, original invalid masks and coordinates were preserved; cleaned spectra and missing-value information changed.
- Identified 723 raw values matching the VNIR header ignore value of 4095 across the compared files.
- Searched the repository for the original NPZ generation/correction scripts; none were found. Complete processing reproducibility remains unresolved.
- Reviewed the VNIR sampling metadata: 48 unique pot records, 18 time points, 48 pots recorded from -1 to 7 DPI and 36 pots from 8 to 20 DPI.
- Documented unequal sampling, missing individual plant identity information and unconfirmed physical leaf tracking.
- Confirmed that the selected processed subset contains four scans, four pots, 10 leaves and 272,912 pixel records across 216 bands.
- Created `VNIR_FINAL_SUITABILITY_ASSESSMENT_2026-11-17.md`.
- Created `VNIR_PROGRESS_REPORT_2026-11-17.md`.
- Corrected the sampling coverage statement in `VNIR_PROGRESS_REPORT_2026-11-14.md`.
- No final model training or forecasting claim was made.
- Committed and pushed the VNIR documentation to the `Hiba` branch.

**VNIR Git details:**

- Branch: `Hiba`
- Commit ID: `6e1854c`
- Commit message: `docs: complete VNIR investigation assessment for Nov 17`
- Push confirmed successfully.

### Member 2 — SWIR Wheat Septoria

**Investigation and documentation status: Completed.**

- Consolidated the SWIR investigation findings into the final report.
- Reviewed the historical 96/96 pot-side scan verification. The result is previously documented/team-reported and was not independently re-audited during this investigation.
- Documented that the original standalone filename list and pot-side matching table were not preserved separately.
- Documented the SWIR dataset source, DOI, licence and archive information.
- Reviewed the SWIR instrument specifications, spectral range and available acquisition details.
- Documented the 48-pot metadata, 279 leaf-level records, 18 DPI values and missing observations.
- Documented the distinction between empty metadata cells and the explicit technical NA entry.
- Recorded unresolved acquisition settings, technical questions and evidence limitations.
- Submitted four investigation documents for review.
- Hiba reviewed the four submitted documents.

**Git handover: Completed.**

- Approved SWIR documentation committed and pushed successfully.
- Branch: `Fahma`
- Commit ID: `09e134e`
- Commit message: `Complete SWIR dataset investigation and documentation`
- Five updated SWIR documentation files pushed.
- Member 2 confirmed that all five files are available in the GitHub repository under the `Fahma` branch.
- No further SWIR investigation was performed on 17 November.

**Planned next task — 18 November:**

SWIR data-readiness and preprocessing-feasibility assessment. No preprocessing or model training is authorized yet.

### Member 3 — RGB

- Latest 17 November submission status requires confirmation.
- Do not mark additional RGB investigation tasks complete without reviewing the submitted evidence.

## 6. Scientific and repository rules

- Preserve original raw data.
- Keep SWIR and each RGB dataset separate during investigation.
- Do not merge modalities without scientific justification.
- Do not begin final model training before experimental-design review.
- Do not claim forecasting capability without suitable temporal evidence.
- Document commands, findings, errors and decisions.
- Do not commit or push changes without project lead approval.
- Do not treat pixels, patches or leaves from the same biological sample as independent observations.
- Use group-aware validation based on the correct biological experimental unit.
- Distinguish verified findings from historical reports, assumptions and unknowns.

## 7. Pending work after 17 November review

### SWIR — Member 2

- Investigate remaining acquisition settings and technical uncertainties when supporting evidence becomes available.
- Assess SWIR data readiness and propose a preprocessing workflow without modifying raw data.
- Identify which data-quality checks can be performed reliably and which require additional information.

### RGB — Member 3

- Review the latest NWRD Wheat Rust investigation submission when received.
- Continue CCMT Tomato source and access verification.
- Resolve remaining Rice Sheath Blight annotation questions when additional evidence becomes available.

### VNIR — Hiba

- Continue only the unresolved follow-up investigations recorded in Section 8.
- Avoid repeating completed VNIR checks.

### Project coordination — Hiba

- Maintain the central investigation tracker.
- Review team submissions and supporting evidence.
- Keep RGB, VNIR and SWIR assessments separate until compatibility is established.
- Decide dataset suitability before approving preprocessing or model development.

## 8. VNIR follow-up items

- Verify whether reflectance calibration was applied to the local VNIR data.
- Obtain or reconstruct a reproducible NPZ processing pipeline.
- Confirm the number of plants per pot and the true experimental unit from authoritative records.
- Investigate physical leaf tracking across dates.
- Establish which metadata pots have usable VNIR image files.
- Design group-aware validation only after experimental units and dataset suitability are established.

## 9. Plan for 18 November 2026

| Person | Assignment |
|---|---|
| Hiba | Review team progress, coordinate dataset-readiness decisions and maintain the central tracker. |
| Member 2 | Complete SWIR data-readiness and preprocessing-feasibility assessment. |
| Member 3 | Continue the next RGB dataset investigation based on the latest verified status and assigned priorities. |

## 10. Overall project assessment

**Current stage:** Dataset investigation, evidence verification and feasibility assessment.

**Progress:** Meaningful investigation and documentation have been completed across VNIR and SWIR, with RGB source and label investigations underway.

**Main strengths:**

- Dataset evidence and limitations are being documented.
- Raw data is being preserved.
- Modality-specific investigations are being kept separate.
- Scientific limitations involving biological replication, metadata and temporal tracking are being considered before modelling.

**Main risks:**

- VNIR calibration provenance and processing reproducibility remain unresolved.
- SWIR acquisition settings and some technical metadata remain unresolved.
- RGB archive contents, annotation mappings and additional dataset sources require further verification.
- Dataset compatibility and reliable temporal labels have not been established.

**Next milestone:** Complete the initial source and suitability assessment of all candidate datasets, establish the experimental units and determine which datasets can genuinely support the intended research objectives.

**Final note:** Documentation completion does not equal scientific validation. The next priority is to establish whether the available data can support a defensible disease-detection, severity-assessment or forecasting study before moving into preprocessing and model development.
