# TerraSpectra Team Investigation Tracker

**Date:** 21 November 2026

**Project stage:** Evidence consolidation, experimental-design review and dataset suitability assessment

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
| Wheat Septoria SWIR | Official archive publicly listed in Recherche Data Gouv; historical 96/96 expected pot-side scan matches documented. Current project-copy holder and archive contents remain unconfirmed; original raw-file technical verification is pending |
| NWRD Wheat Rust | Official source investigated; archive not downloaded; archive contents not independently verified |
| CCMT Tomato | Available archive investigated; archive-level counts documented; discrepancy and leakage questions remain unresolved |
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
| SWIR source and public archive access-route verification | Completed and documented; archive listing verified, but archive contents not inspected |
| SWIR historical 96/96 scan matching | Previously documented; original standalone filename list and matching table not preserved separately |
| SWIR instrument specifications and published metadata review | Documented; original raw headers, calibration references and acquisition records remain unverified |
| SWIR final investigation report | Submitted and reviewed by Hiba |
| SWIR Git handover | Completed; commit `09e134e` pushed to `Fahma` |
| SWIR documentation files pushed | Five files confirmed by Member 2 |
| SWIR project working-copy holder | Unconfirmed |
| SWIR original raw-file technical verification | Pending access to and inspection of original files |
| RGB Rice Sheath Blight initial source investigation | Completed |
| Rice Sheath Blight severity-label investigation | Completed with remaining annotation questions |
| NWRD Wheat Rust initial source verification | Completed; report reviewed |
| NWRD dataset licence | Unresolved; author clarification required |
| NWRD archive inventory and image-mask pairing | Not independently verified; archive not downloaded |
| NWRD train/validation/test split | Zenodo/GitHub discrepancy unresolved |
| NWRD Git handover | Completed; commit `20c1031` pushed to `Afnan` |
| CCMT Tomato investigation | Archive-level investigation completed; discrepancy and leakage verification remain pending |

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

**NWRD Wheat Rust initial source verification: Completed.**

- Investigated the NUST Wheat Rust Disease Dataset (NWRD).
- Submitted `docs/NWRD_WHEAT_RUST_SOURCE_VERIFICATION.md`.
- Official source: https://zenodo.org/records/21672928
- DOI: `10.5281/zenodo.21672928`.
- The official description reports 100 RGB field images and corresponding binary segmentation masks. Actual archive contents have not been independently inspected.
- Dataset licence remains unresolved. Zenodo identifies copyright information, but a specific dataset reuse licence has not been established.
- Archive was not downloaded; actual image counts, mask counts and image-mask pairing remain unverified.
- Zenodo describes an 80/10/10 split, while the GitHub README describes 90% train and validation combined and 10% test. This discrepancy remains unresolved.
- Dataset remains a candidate and is not approved for modelling.

**NWRD Git handover: Completed.**

- Branch: `Afnan`
- Commit ID: `20c1031`
- Commit message: `docs: add NWRD wheat rust source verification`
- Push and branch synchronisation confirmed by Member 3.

**Remaining RGB work:**

- Continue CCMT Tomato source investigation.
- Seek NWRD licence clarification.
- Investigate the dataset split discrepancy.
- Verify archive contents when inspection is authorized.
- Continue Rice Sheath Blight annotation questions where further evidence is available.

## 5E. Daily progress update — 18 November 2026

### Hiba — Cross-dataset assessment and coordination

- Completed the cross-dataset suitability assessment and experimental-design recommendations.
- Reviewed the SWIR data-readiness and preprocessing-feasibility assessment submitted by Member 2.
- Retrieved and reviewed the SWIR readiness report from the Fahma branch.
- Verified Fahma's Git commit: `dd5e954` (`Add SWIR data readiness assessment`).
- Historical 96/96 scan verification remains documented; the standalone filename-to-pot/side mapping table is unavailable.
- Recorded that original SWIR `.hyspex`, `.hdr` and calibration/reference files are not locally accessible to Fahma.
- Confirmed that preprocessing has not been executed and raw data has not been modified.

**Fahma — SWIR Git handover:**

- Branch: `Fahma`
- Commit: `dd5e954`
- File: `research/SWIR/SWIR_DATA_READINESS_ASSESSMENT_2026-11-18.md`
- Commit and push verified on `origin/Fahma`.
- Report retrieved into Hiba's working branch and reviewed.

**SWIR readiness decision:**

- Initial data-readiness and preprocessing-feasibility assessment: Completed.
- Preprocessing workflow: Proposed, not executed.
- Raw-file/header validation: Blocked pending access to original raw files and calibration references.
- Remaining questions include wavelength arrays, binary layout, ignore values, acquisition settings, calibration details and raw-value quality.
- Historical scan mapping evidence remains a limitation.

## 5F. Daily progress update — 19 November 2026

### Hiba — Cross-dataset assessment and integration

- Reviewed Member 3's three updated RGB investigation reports:
  - `docs/NWRD_FOLLOW_UP_VERIFICATION.md`
  - `docs/RICE_SHEATH_BLIGHT_SEVERITY_LABEL_VERIFICATION.md`
  - `docs/TOMATO_DATASET_SOURCE_VERIFICATION.md`
- Retrieved the three reports from Afnan's branch into the Hiba working branch.
- Updated `docs/CROSS_DATASET_SUITABILITY_ASSESSMENT_2026-11-18.md` with the latest RGB and SWIR evidence.
- Recorded the CCMT public-record CC BY 4.0 licence and remaining archive-verification requirements.
- Recorded the NWRD licence, archive and train/validation/test split uncertainties.
- Recorded the Rice Sheath Blight CC BY 4.0 public-record finding and unresolved severity-label details.
- Reviewed Sections 2.4 and 2.5 and confirmed their headings are unique.
- Ran `git diff --check`; no whitespace errors remain.
- The assessment has 122 insertions and 47 deletions. It remains modified but unstaged.
- The three RGB reports are staged locally but have not been committed or pushed.

### Member 3 — RGB investigation

**NWRD Wheat Rust — Follow-up verification completed.**

- Reviewed the official Zenodo and GitHub source information.
- Documented the reported 100 images and binary segmentation masks.
- Recorded the unresolved dataset reuse licence.
- Documented the discrepancy between the paper's 80/10/10 split and the GitHub README's 90% train-plus-validation and 10% test description.
- Archive integrity, actual image/mask counts and image-mask pairing remain unverified.

**CCMT Tomato — Public-source investigation completed.**

- Reviewed the official Mendeley Data record and associated publication.
- Recorded 5,435 reported raw tomato images, 27,178 augmented tomato images and five tomato classes.
- Recorded the CC BY 4.0 licence listed on the public dataset record.
- Archive contents, image-to-label mapping, duplicates, augmentation relationships and biological sample grouping remain unverified.

**Rice Sheath Blight — Follow-up verification completed.**

- Reviewed the official Mendeley Data record.
- Recorded the public-record CC BY 4.0 licence.
- Exact six class names, definitions, severity boundaries and image-to-label mapping remain unresolved.
- Repeated observation periods do not establish longitudinal tracking of the same plants or leaves.
- Archive contents have not been independently inspected.

**RGB Git handover:**

- Three updated reports were retrieved into the Hiba working branch.
- The files are staged locally but have not yet been committed or pushed by Hiba.

### Member 2 — SWIR Wheat Septoria

- SWIR data-readiness and preprocessing-feasibility assessment remains completed and reviewed.
- Preprocessing workflow is proposed only; it has not been executed.
- Original raw headers and calibration/reference files remain unavailable for local validation.
- Wavelength arrays, binary layout, acquisition settings and calibration provenance remain unresolved.

## 5G. Current evidence-based progress status — 19 November 2026

| Work item | Current status |
|---|---|
| VNIR investigation and suitability assessment | Completed for investigated data; documented limitations remain |
| SWIR source and metadata investigation | Completed; technical metadata gaps remain |
| SWIR data-readiness assessment | Completed and reviewed |
| NWRD initial source verification | Completed |
| NWRD follow-up verification | Completed; licence, archive and split questions unresolved |
| CCMT public-source investigation | Completed; archive-level verification pending |
| Rice Sheath Blight severity-label follow-up | Completed; exact class definitions and annotation mapping unresolved |
| Cross-dataset suitability assessment | Updated; final team review pending |
| RGB report retrieval into Hiba branch | Completed; three reports staged, not committed |
| Tracker update | 19 November update added |
| Preprocessing and model training | Not approved or started |

## 5H. Daily progress update — 21 November 2026

### Hiba — Experimental design and coordination

- Consolidated the cross-dataset experimental design framework.
- Updated the cross-dataset suitability assessment using the available VNIR, SWIR and RGB evidence.
- Reviewed Member 2's SWIR dataset access investigation report.
- Verified the report's Git commit and file on the remote Fahma branch.
- Updated the central investigation tracker with the latest SWIR access findings.
- No preprocessing, feature engineering or model training was started.

**Git handover — Hiba:**

- Branch: `Hiba`
- Commit: `423f3e4`
- File: `docs/CONSOLIDATED_EXPERIMENTAL_DESIGN_2026-11-21.md`
- Commit: `ed899b5`
- File: `docs/CROSS_DATASET_SUITABILITY_ASSESSMENT_2026-11-18.md`
- Both commits were pushed successfully.

### Member 2 — SWIR Wheat Septoria

**SWIR dataset access investigation: Completed and reviewed.**

- Identified Recherche Data Gouv as the official repository.
- Verified dataset DOI `10.57745/WVP0FJ`.
- Identified Lorraine Latchoumane (INRAE) as the depositor and repository contact.
- Confirmed that the official repository publicly lists `Data/SWIR/20210311.zip`, with a listed size of 4.3 GB.
- Recorded the repository's Etalab Open License 2.0.
- The archive was not downloaded or inspected during this investigation.
- The project working-copy holder remains unconfirmed.
- Availability of original `.hyspex`, matching `.hdr`, dark-current, white-reference and acquisition-record files remains unconfirmed.
- Historical 96/96 expected pot-side scan matching remains documented; the separate original filename-to-pot/side mapping file has not been confirmed.
- Fahma reported emailing Lorraine Latchoumane on 21 November to request clarification about archive contents and supporting files. A response was pending when the report was written.
- No preprocessing, calibration, raw-data modification, feature engineering or model training was performed.

**SWIR Git handover:**

- Branch: `Fahma`
- Commit: `0bc2880`
- Commit message: `Document SWIR dataset access investigation`
- File: `research/SWIR/SWIR_DATASET_ACCESS_INVESTIGATION_2026-11-21.md`
- Remote branch and commit verified by Hiba.
- Report reviewed by Hiba.

**SWIR readiness decision:**

- Official repository and archive access route: Identified.
- Project working-copy holder: Unconfirmed.
- Internal archive contents and supporting calibration files: Not verified.
- Original raw-file technical verification: Pending access and inspection.
- Preprocessing remains on hold.

### Member 3 — RGB

- 21 November RGB investigation update: Awaiting submission and review.
- Existing CCMT Tomato, Rice Sheath Blight and NWRD Wheat Rust evidence remains subject to the unresolved questions documented in the earlier investigation records.
- No new RGB preprocessing or model training is authorized.

### Team status at the end of 21 November

- Hiba's experimental-design framework: Committed and pushed.
- Fahma's SWIR access investigation: Submitted, reviewed and verified on the remote branch.
- Afnan's 21 November RGB update: Pending review.
- Dataset-specific technical readiness and final experimental approval remain outstanding.

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

## 7. Pending work after 21 November review

### SWIR — Member 2

- Await the response to Fahma's 21 November email to Lorraine Latchoumane.
- Confirm who holds the project's original SWIR archive.
- Establish whether the original `.hyspex`, matching `.hdr`, dark-current, white-reference and acquisition records are available.
- Confirm whether an original filename-to-pot/side mapping file exists.
- Once the files are available, perform read-only raw-file and header verification.
- Keep preprocessing and calibration on hold until technical verification and experimental-design approval.

### RGB — Member 3

- Continue CCMT Tomato source and licence verification.
- Investigate the 20-image difference between the available archive count and publication-reported augmented count.
- Investigate original-to-augmented image relationships and possible train/test leakage.
- Obtain clarification of the NWRD dataset licence.
- Resolve the NWRD Zenodo/GitHub train/validation/test split discrepancy.
- Verify NWRD image counts and image-mask pairing when archive inspection is authorized.
- Continue Rice Sheath Blight annotation verification, particularly exact severity class definitions and image-to-label mapping.
- Submit the 21 November RGB investigation update for review.

### VNIR — Hiba

- Verify whether reflectance calibration was applied to the local VNIR data.
- Obtain or reconstruct a reproducible NPZ processing pipeline.
- Confirm the number of plants per pot and the true experimental unit from authoritative records.
- Investigate physical leaf tracking across dates.
- Establish which metadata pots have usable VNIR image files.
- Design group-aware validation only after experimental units and dataset suitability are established.

### Project coordination — Hiba

- Maintain the central investigation tracker.
- Review team submissions and supporting evidence.
- Keep RGB, VNIR and SWIR assessments separate until compatibility is established.
- Finalize dataset suitability and experimental-design decisions before approving preprocessing or model development.

## 8. VNIR follow-up items

- Verify whether reflectance calibration was applied to the local VNIR data.
- Obtain or reconstruct a reproducible NPZ processing pipeline.
- Confirm the number of plants per pot and the true experimental unit from authoritative records.
- Investigate physical leaf tracking across dates.
- Establish which metadata pots have usable VNIR image files.
- Design group-aware validation only after experimental units and dataset suitability are established.

## 9. Plan for 22 November 2026

| Person | Assignment |
|---|---|
| Hiba | Review Afnan's RGB update, maintain the central tracker and continue experimental-design integration. |
| Member 2 | Await the SWIR contact response and identify the project archive holder; no repeated searches or preprocessing. |
| Member 3 | Submit the RGB evidence update and document unresolved CCMT, Rice and NWRD questions. |

## 10. Overall project assessment

**Current stage:** Evidence consolidation, experimental-design review and dataset suitability assessment.

**Progress:** Investigation and documentation have been completed across the selected VNIR and SWIR evidence. Initial source and follow-up investigations have been completed for Rice Sheath Blight and NWRD. CCMT archive-level investigation has also advanced, while important RGB verification questions remain unresolved.

**Main strengths:**

- Dataset evidence and limitations are being documented.
- Raw data is being preserved.
- Modality-specific investigations are being kept separate.
- Scientific limitations involving biological replication, metadata and temporal tracking are being considered before modelling.
- Experimental-design requirements and approval gates are documented.

**Main risks:**

- VNIR calibration provenance and processing reproducibility remain unresolved.
- SWIR original raw-file access, calibration references and acquisition records remain unverified.
- NWRD licence, archive contents, image-mask pairing and split discrepancy require further verification.
- Rice Sheath Blight annotation mappings and CCMT Tomato augmentation/leakage questions require further verification.
- Dataset compatibility and reliable temporal labels have not been established.

**Next milestone:** Complete the remaining evidence review, freeze candidate datasets and research objectives, and approve a defensible experimental design before preprocessing begins.

**Final note:** Documentation completion does not equal scientific validation. The next priority is to establish whether the available data can support a defensible disease-detection, severity-assessment or forecasting study before moving into preprocessing and model development.