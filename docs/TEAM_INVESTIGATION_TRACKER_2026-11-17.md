# TerraSpectra Team Investigation Tracker

**Date:** 26 November 2026

**Project stage:** Evidence consolidation, experimental-design review and dataset suitability assessment

## 1. Team responsibilities

| Member | Responsibility | Assigned datasets |
|---|---|---|
| Hiba | VNIR investigation, coordination and integration | Wheat Septoria VNIR |
| Member 2 | SWIR investigation | Wheat Septoria SWIR |
| Member 3 | RGB investigation | NWRD Wheat Rust, CCMT Tomato, Rice Sheath Blight |

## 2. Existing dataset availability

Current known dataset status based on investigation evidence reviewed up to 26 November 2026:

| Dataset | Existing local and investigation status |
|---|---|
| Wheat Septoria VNIR | Four local ENVI headers verified: 1,370 lines, 1,024 samples and 216 bands, with wavelength units in nm and ignore value 4095. Calibration provenance, processing reproducibility and biological sample tracking remain unresolved. |
| Wheat Septoria SWIR | Official archive downloaded outside the repository and MD5 verified. Read-only inventory confirmed 96 HYSPEX files, 96 matching headers, 96 JPGs and 259 CSVs; all 96 raw/header pairs checked. Calibration references, annotation meaning and biological sample mapping remain unresolved. |
| NWRD Wheat Rust | Archive downloaded and MD5 checksum verified by Member 3. Inventory reports 100 JPG images and 100 PNG masks, with 100 filename-level image-mask pairs. Dataset image and mask reuse permissions remain unresolved. |
| CCMT Tomato | Inventory reports 5,805 raw images, 21,723 Train images and 5,445 Test images (27,168 augmented images, versus 27,178 in the publication). SHA-256 and CRC32 independently confirm 4,084 unique shared contents and 4,085 matching Train-Test file pairs. The supplied Test partition is not suitable as an independent test set until lineage, label inconsistency and leakage-safe splitting are resolved. |
| Rice Sheath Blight | Archive-level inventory completed. Six folder-based severity classes contain 1,609 images in total, matching the README count. Individual image-label correctness, exact severity boundaries and biological sample grouping remain unresolved. |

**Important status clarification:**

- Public availability, archive download, archive-level inventory and technical readiness are separate verification stages.
- Filename-level image-mask pairing does not establish visual mask correctness.
- Exact-content SHA-256 and CRC32 matches establish file-content overlap, not by themselves biological sample identity, original-to-augmented lineage or biological independence.
- Dataset availability does not mean that a dataset is approved for preprocessing or model training.
- Original raw data must remain unchanged. Different modalities and RGB datasets must remain separate until their individual suitability and experimental designs are approved.

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
| VNIR investigation | Selected-scan header verification and suitability documentation completed; calibration provenance and biological tracking remain unresolved |
| VNIR calibration provenance | Investigated; calibration application and reproducibility remain unverified |
| SWIR source and public archive access-route verification | Completed; official source and public archive listing identified |
| SWIR historical 96/96 scan matching | Historical result documented; original standalone filename-to-pot/side mapping remains unconfirmed |
| SWIR instrument specifications and metadata review | All 96 raw/header pairs and common technical configuration verified; calibration references, annotation meaning and biological mapping remain unresolved |
| SWIR final investigation report | Submitted and reviewed by Hiba |
| SWIR Git handover | Latest archive investigation report verified on `origin/Fahma`, commit `0652ddb` |
| SWIR archive location | Downloaded by Member 2 and retained outside the project repository for read-only investigation |
| SWIR original raw-file technical verification | Archive inventory and all 96 raw/header pairs verified; calibration references and biological/annotation provenance remain unresolved |
| Rice Sheath Blight source and archive inventory | Completed; 1,609 images counted across six severity folders |
| Rice Sheath Blight label correctness and biological grouping | Unresolved; individual images not visually checked and plant-level lineage unknown |
| NWRD source and archive verification | Completed; downloaded archive MD5 checksum matched expected value |
| NWRD archive inventory and image-mask pairing | Completed at filename level; 100 image-mask pairs reported |
| NWRD visual mask validation | Pending; visual alignment and mask quality not checked |
| NWRD dataset image and mask reuse licence | Unresolved; explicit asset permission required |
| NWRD train/validation/test split | Archive contains 90/10 train/test folders; paper and README split descriptions require clarification |
| NWRD Git handover | Updated report verified on `origin/Afnan`, commit `b19989c` |
| CCMT Tomato archive inventory | Updated; 5,805 raw, 21,723 train and 5,445 test images |
| CCMT publication count discrepancy | Unresolved; augmented-image difference 10 and raw-image difference 370 |
| CCMT Train-Test overlap | SHA-256 and CRC32 independently confirm 4,084 unique shared contents and 4,085 matching file pairs; independent evaluation split not established |
| CCMT original-to-augmented lineage | Unresolved; near-duplicate and source-independent split analysis pending |
| Cross-dataset suitability assessment | Updated; dataset-specific limitations and experimental-design constraints documented |
| Consolidated experimental design | Framework previously committed; latest 26 November updates remain local and uncommitted; final dataset approval remains pending |
| Preprocessing, feature engineering and model training | Not approved or started |

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

## 5I. Daily progress update — 23 November 2026

### Hiba — Evidence review and project coordination

- Reviewed Member 2's updated SWIR dataset-access investigation.
- Retrieved and reviewed Member 3's updated RGB investigation reports from the remote `Afnan` branch.
- Reviewed the latest evidence concerning CCMT Tomato, Rice Sheath Blight and NWRD Wheat Rust.
- Updated the central tracker to reflect the latest verified dataset availability, archive inventory and technical-readiness status.
- Reviewed the cross-dataset suitability findings and consolidated experimental-design constraints.
- No preprocessing, feature engineering, model training or modality fusion was started.

### Member 2 — SWIR Wheat Septoria

- Official dataset source identified in Recherche Data Gouv.
- DOI: `10.57745/WVP0FJ`.
- Public archive listing: `Data/SWIR/20210311.zip`, approximately 4.3 GB.
- The project working-copy holder and local archive availability remain unconfirmed.
- Original `.hyspex` files, matching `.hdr` files, dark-current files, white-reference files and acquisition records remain unverified.
- Historical 96/96 pot-side scan matching remains documented; the original standalone filename-to-pot/side mapping file has not been confirmed.
- Fahma documented a contact attempt to Lorraine Latchoumane on 21 November; a response was pending in the submitted report.
- No archive download, raw-data modification, calibration, preprocessing or model training was verified.

**Status:** Exploratory investigation only. Technical verification and preprocessing remain on hold until the original archive and supporting files are accessible.

### Member 3 — RGB investigation

#### A. CCMT Tomato

- Updated archive inventory: 5,805 Raw Tomato images, 21,723 Train images and 5,445 Test images, totalling 27,168 augmented images.
- The publication reports 27,178 augmented images, leaving a difference of 10 images.
- The publication reports 5,435 raw images, compared with 5,805 in the current archive inventory, leaving a difference of 370 images.
- CRC32 comparisons reported 4,263 unique Raw–Train matching values, 1,363 Raw–Test matching values and 4,084 unique Train–Test matching values.
- A total of 1,241 unique CRC32 values were reported as common to Raw, Train and Test.
- Raw–Train matching entries were reported as 4,264, associated with 4,263 unique matching CRC32 values.
- CRC32 findings indicate checksum matches; they do not independently establish biological sample identity or complete image lineage.
- Original-to-augmented image relationships, near-duplicate status and source-image-independent splitting remain unresolved.

**Status:** Existing Train/Test splits are not accepted as independent evaluation sets. A defensible leakage-control strategy is required before modelling.

#### B. Rice Sheath Blight

- Archive: `SBSeverity.zip`.
- Six folder-based severity classes were identified.
- Image counts: Stage-1 157, Stage-2 326, Stage-3 410, Stage-4 355, Stage-5 263 and Stage-6 98.
- Total inventory: 1,609 images, matching the README count.
- README descriptions refer to lesion progression, lesion height relative to plant height, colour intensity and lesion density.
- No separate annotation file was identified in the reported archive metadata scan.
- Individual image-label correctness has not been visually verified.
- Exact severity boundaries, repeated-plant lineage and duplicate or near-duplicate status remain unresolved.
- The reported verification did not include image extraction or visual inspection.

**Status:** Potential candidate for a separate RGB severity-estimation track, conditional on label validation, biological grouping and leakage assessment.

#### C. NWRD Wheat Rust

- Downloaded archive: `NWRD.zip`, reported size 608,898,312 bytes.
- Expected MD5: `7b9193efebe1ed8c60b10c9f05d11e14`.
- Actual MD5 matched the expected checksum.
- Archive inventory: 90 Train JPG images and 90 Train PNG masks; 10 Test JPG images and 10 Test PNG masks.
- All 100 image files had filename-level matching masks.
- No Train/Test filename overlap was reported.
- No separate validation folder was found in the inspected archive.
- Visual mask alignment, mask pixel values, image quality and visual duplicates remain unchecked.
- The paper and GitHub README report differing split descriptions; the reason for the discrepancy remains unresolved.
- The GitHub repository's MIT licence does not establish reuse permission for the dataset images and masks.
- Explicit dataset asset reuse permission remains unresolved; author contact had not been initiated in the reported update.

**Status:** Potential binary-segmentation candidate, but dataset asset permissions and visual quality checks must be resolved before project reuse.

### RGB Git handover

Member 3 reported the following commits as pushed to `origin/Afnan`:

- `2595f65` — `docs: document tomato published count discrepancy`
- `21e4323` — `docs: document tomato lineage and leakage findings`
- `e210139` — `docs: verify rice sheath blight archive labels and counts`
- `b19989c` — `docs: document NWRD dataset licence uncertainty`

The updated investigation reports were retrieved and reviewed by Hiba.

### Team evidence-review outcome — 23 November

- **VNIR:** Exploratory investigation completed for selected scans; calibration provenance and biological sample tracking limitations remain.
- **SWIR:** Public archive source identified; original archive contents and supporting calibration files remain unverified.
- **CCMT Tomato:** Archive inventory updated; checksum overlap and image-lineage concerns prevent acceptance of the existing split as independent evaluation data.
- **Rice Sheath Blight:** Six folder-based severity stages and the total image count verified; individual label correctness and biological grouping remain unresolved.
- **NWRD Wheat Rust:** Archive checksum and filename-level image-mask pairing verified; visual mask validation and dataset asset reuse permission remain unresolved.
- No dataset has received final approval for model training.
- Preprocessing, feature engineering, model training and multimodal fusion remain on hold.
- Forecasting claims must remain limited to what the available data and approved experimental design can scientifically support.

## 5J. Daily progress update — 26 November 2026

### Hiba — VNIR and project coordination

- Completed additional technical verification of four local VNIR ENVI headers.
- Confirmed 1,370 lines, 1,024 samples, 216 bands, wavelength units in nm and ignore value 4095 across the inspected headers.
- Documented the distinction between processed spectral-intensity data and verified calibrated reflectance.
- Created `VNIR_PROGRESS_REPORT_2026-11-25.md`.
- Updated the consolidated experimental design with the latest SWIR and CCMT findings.
- VNIR documentation commit `471252e` was pushed to `origin/Hiba`.
- The current consolidated experimental-design changes are still local and uncommitted.

### Member 2 — SWIR Wheat Septoria

- Downloaded the official SWIR archive outside the repository.
- Verified the local MD5 against the published checksum.
- Inspected the archive read-only without extraction or modification.
- Inventory: 96 `.hyspex` files, 96 matching `.hdr` files, 96 JPG files and 259 CSV files.
- Checked all 96 raw/header pairs; no missing matching headers or binary-size mismatches were reported.
- Verified 256 spectral bands and a wavelength range of 964.181280–2494.388419 nm across the inspected headers.
- Documented the common 420 × 320 × 256 configuration, unsigned 16-bit data, little-endian byte order and BIL interleave.
- Inspected 922,064 CSV rows containing two numeric values per row.
- Calibration-reference correspondence, CSV annotation semantics, biological sample mapping and the `18_D` folder-placement irregularity remain unresolved.
- Updated report committed and pushed to `origin/Fahma` in commit `0652ddb`.

### Member 3 — RGB

**CCMT Tomato**

- Completed reproducible Train–Test exact-content comparison using SHA-256 and CRC32.
- Both methods returned 4,084 unique shared content values.
- 4,084 Test entries have at least one Train match.
- The comparison identified 4,085 matching Train–Test file pairs and 1,361 unmatched Test entries.
- One shared content occurs in two Train entries with different class labels, requiring label-consistency investigation.
- The archive contains 5,805 raw images, 21,723 Train images and 5,445 Test images.
- The augmented archive total is 27,168, compared with 27,178 reported in the publication.
- Original-to-augmented lineage, near-duplicates and biological sample identity remain unresolved.
- The supplied Test partition is not accepted as an independent evaluation set at this stage.
- Verification report and supporting evidence pushed to `origin/Afnan` in commit `830254a`.

**Rice Sheath Blight**

- Rice documentation correction submitted and pushed in commit `36029b2`.
- Exact severity definitions, individual image-label correctness and biological grouping remain subject to verification.

### Team status at the end of 26 November

- VNIR: Selected-scan technical investigation documented; calibration provenance and biological tracking remain unresolved.
- SWIR: Archive and header inventory technically verified; calibration and sample-provenance questions remain unresolved.
- CCMT: Exact-content Train–Test overlap verified; independent evaluation split not established.
- Rice: Documentation updated; label and biological-grouping validation remain outstanding.
- NWRD: Reuse permission, visual mask validation and split questions remain outstanding.
- No dataset has final approval for preprocessing or model training.
- No preprocessing, feature engineering, model training or modality fusion was started.

## 5K. Daily progress update — 27 November 2026

### Hiba
- Reviewed the latest RGB investigation evidence and completed the README update locally.
- Reviewed Fahma's revised SWIR investigation report and identified minor final corrections.
- Continued updating the central investigation tracker and consolidated experimental design.
- No preprocessing, feature engineering, model training or multimodal fusion was performed or approved.

### Member 2 — Fahma
- Completed the SWIR archive, header, metadata and coordinate investigation.
- Revised the SWIR investigation report following Hiba's review.
- Minor wording and path corrections remain before final report acceptance.
- The revised report was committed on Fahma's branch; no central-document modification was made.

### Member 3 — Afnan
- Completed the current RGB investigation review queue.
- CCMT, Rice and NWRD findings are available for central documentation.
- No repeat investigation is currently required; targeted clarification may be requested if necessary.

### End-of-day assessment
- VNIR: Exploratory evidence documented; biological tracking and calibration questions remain.
- SWIR: Archive inventory and scan-to-pot-side mapping verified; calibration and visual annotation mapping remain unresolved.
- CCMT: Exact Train-Test overlap and raw-to-augmented lineage investigated; label conflicts and publication-count discrepancies remain unresolved.
- Rice: Duplicate-content findings documented; severity-label and biological grouping questions remain.
- NWRD: Image-mask pairing and dimension checks completed; licence and annotation questions remain.
- No dataset has received final experimental-design approval.

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

## 7. Pending work after 27 November review

### SWIR
- Fahma to complete the minor wording and path corrections in the revised report.
- Preserve the distinction between coordinate-range validation and visual annotation verification.
- Preserve the distinction between scan-to-pot-side correspondence and independent biological samples.
- Keep the complete list of 20 missing coordinate CSV identifiers.
- Provide the corrected report and a standard diff against the actual repository file.
- Hiba must review the corrected report and diff before Git integration.

### RGB
- No repeat investigation is currently required from Afnan.
- Preserve the CCMT Train-Test overlap, raw-to-augmented lineage and cross-class label-conflict findings.
- Preserve the Rice duplicate-content and severity-label limitations.
- Preserve the NWRD image-mask dimension, duplicate-image and licensing limitations.
- Request targeted clarification only if needed during central-document review.

### VNIR
- Retain the existing follow-up items in Section 8.
- Do not treat exploratory candidate bands as validated biomarkers.
- Do not assume raw intensity values are calibrated reflectance.
- Biological tracking and independent sample grouping remain unresolved.

### Hiba coordination
- Complete the central tracker and consolidated experimental design updates.
- Review Fahma's corrected report before integration.
- Keep RGB, VNIR and SWIR investigations separate.
- Do not approve preprocessing, modelling, forecasting or multimodal fusion without the required evidence and explicit design approval.
- Inspect all changed files and diffs before any commit or push.
## 8. VNIR follow-up items

- Verify whether reflectance calibration was applied to the local VNIR data.
- Obtain or reconstruct a reproducible NPZ processing pipeline.
- Confirm the number of plants per pot and the true experimental unit from authoritative records.
- Investigate physical leaf tracking across dates.
- Establish which metadata pots have usable VNIR image files.
- Design group-aware validation only after experimental units and dataset suitability are established.

## 9. Current follow-up assignments — 27 November 2026

### Hiba
- Complete the central tracker and consolidated experimental design updates.
- Review the corrected SWIR report and its standard Git diff.
- Maintain scientific safeguards and review all changes before integration.

### Member 2 — Fahma
- Complete the minor corrections to the SWIR investigation report.
- Return the corrected report and standard diff for review.
- Do not commit, push, merge or modify central project documents before approval.

### Member 3 — Afnan
- No new investigation assignment at present.
- Remain available for targeted clarification of existing RGB evidence if requested.
- Do not repeat completed investigations or modify central documents without approval.
## 10. Overall project assessment

The project remains in the evidence-consolidation and experimental-design review stage.

- **VNIR:** Technical header information has been verified. Exploratory spectral findings are documented, but calibration status, biological tracking and independent sample grouping remain unresolved.
- **SWIR:** Archive integrity, raw/header inventory and all 96 scan-to-pot-side metadata matches have been verified. These matches do not establish 96 independent biological samples. Twenty metadata leaf records lack coordinate CSVs. Calibration and visual annotation mapping remain unresolved.
- **CCMT Tomato:** Exact Train-Test content overlap is substantial: 4,084 unique shared hashes and 4,085 matching file pairs. Approximately 75% of Test entries have an exact Train match. Raw-to-augmented lineage and two cross-class label-conflict groups have also been documented. The supplied Test split is not suitable as an independent evaluation set.
- **Rice Sheath Blight:** Six severity stages are represented, but duplicate-content groups, cross-stage conflicts and unresolved severity standards limit immediate modelling readiness.
- **NWRD Wheat Rust:** Image-mask pairing has been checked. One image-mask dimension mismatch and one duplicate-image pair with differing masks require attention. Dataset reuse permission and annotation semantics remain unresolved.

### Scientific decision

No dataset is approved for unrestricted modelling at this stage. Conditional exploratory work may be considered only after the relevant dataset-specific limitations and experimental-design requirements are addressed.

Preprocessing, feature engineering, model training, forecasting and multimodal fusion remain unapproved.

Forecasting requires identifiable biological units, genuine temporal observations, a defined prediction target and a future holdout. Multimodal fusion requires demonstrated correspondence between biological samples and compatible observations across modalities. These conditions have not yet been established.

The project must continue to prioritize evidence quality, reproducibility, biological sample independence, leakage prevention and transparent reporting over premature model development.

## 11. Progress update - 28 November 2026

### Hiba - central documentation
- Reviewed the latest RGB dataset suitability assessment and supplementary findings from Afnan.
- Reviewed Fahma's SWIR report corrections and confirmed that the correction commit is included in the latest `origin/Fahma` branch history.
- Updated the consolidated experimental design with a conditional boundary for read-only descriptive analysis of SWIR dark-current-corrected intensity values. Results must be labelled as uncalibrated intensity; reflectance interpretation and further processing remain unapproved.
- Added the visual inspection result for both Rice cross-stage duplicate groups. The images appeared identical despite different severity-stage labels.
- Added the NWRD aggregate mask-pixel distribution: approximately 99.43% black and 0.57% white. Foreground semantics remain unverified.
- Added Afnan's supplementary CCMT dHash findings: 550 candidate Train-Test pairs at distance <= 8, including 238 cross-class candidates. These are similarity candidates, not confirmed identical photographs, and are kept separate from the earlier dHash analysis.
- Experimental-design changes passed `git diff --check`. The tracker update, formatting and Git review are complete.

### Fahma - SWIR
- The SWIR wording and path corrections are included in the latest `origin/Fahma` branch history.
- Archive and header inventory findings remain documented.
- Calibration/reference correspondence, visual annotation mapping, 20 missing coordinate CSVs, biological grouping and the `18_D` folder-placement issue remain unresolved.
- No preprocessing, calibration transformation, feature extraction, modelling or forecasting is approved.

### Afnan - RGB
- Supplementary RGB findings are available and have been incorporated into the central experimental-design document.
- No repeat investigation is assigned.
- Existing unresolved CCMT lineage and label conflicts, Rice severity standards and biological grouping, and NWRD annotation semantics and reuse permission remain open.

### Overall position
- Central documentation integration, formatting and full Git diff review are complete.
- No dataset is approved for unrestricted modelling.
- No preprocessing, feature engineering, model training, forecasting or multimodal fusion is approved.
- No commit or push has been made.
