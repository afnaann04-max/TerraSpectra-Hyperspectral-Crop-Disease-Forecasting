# TerraSpectra Team Investigation Tracker

**Date:** 23 November 2026

**Project stage:** Evidence consolidation, experimental-design review and dataset suitability assessment

## 1. Team responsibilities

| Member | Responsibility | Assigned datasets |
|---|---|---|
| Hiba | VNIR investigation, coordination and integration | Wheat Septoria VNIR |
| Member 2 | SWIR investigation | Wheat Septoria SWIR |
| Member 3 | RGB investigation | NWRD Wheat Rust, CCMT Tomato, Rice Sheath Blight |

## 2. Existing dataset availability

Current known dataset status based on investigation evidence reviewed up to 23 November 2026:

| Dataset | Existing local and investigation status |
|---|---|
| Wheat Septoria VNIR | Available in the project; selected raw scans and suitability limitations investigated. Calibration provenance and biological sample tracking limitations remain. |
| Wheat Septoria SWIR | Official archive publicly listed in Recherche Data Gouv (DOI: `10.57745/WVP0FJ`). Historical 96/96 expected pot-side scan matches documented. Project working-copy holder, original archive contents, raw headers and calibration-file availability remain unconfirmed. |
| NWRD Wheat Rust | Archive downloaded and MD5 checksum verified by Member 3. Inventory reports 100 JPG images and 100 PNG masks, with 100 filename-level image-mask pairs. Dataset image and mask reuse permissions remain unresolved. |
| CCMT Tomato | Available archive investigated. Inventory reports 5,805 raw images, 21,723 train images and 5,445 test images (27,168 total augmented images). Publication count discrepancies and substantial Train-Test CRC32 overlap require leakage investigation. |
| Rice Sheath Blight | Archive-level inventory completed. Six folder-based severity classes contain 1,609 images in total, matching the README count. Individual image-label correctness, exact severity boundaries and biological sample grouping remain unresolved. |

**Important status clarification:**

- Public availability, archive download, archive-level inventory and technical readiness are separate verification stages.
- Filename-level image-mask pairing does not establish visual mask correctness.
- CRC32 overlap is evidence of matching checksum values, not by itself proof of biological sample identity or complete image lineage.
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
| VNIR investigation | Completed for selected available scans; exploratory suitability assessment documented |
| VNIR calibration provenance | Investigated; calibration application and reproducibility remain unverified |
| SWIR source and public archive access-route verification | Completed; official source and public archive listing identified |
| SWIR historical 96/96 scan matching | Historical result documented; original standalone filename-to-pot/side mapping remains unconfirmed |
| SWIR instrument specifications and metadata review | Published specifications documented; original raw headers, calibration references and acquisition records remain unverified |
| SWIR final investigation report | Submitted and reviewed by Hiba |
| SWIR Git handover | Latest investigation report verified on `origin/Fahma`, commit `0bc2880` |
| SWIR project working-copy holder | Unconfirmed |
| SWIR original raw-file technical verification | Pending access to archive and supporting files |
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
| CCMT Train-Test overlap | 4,084 unique matching CRC32 values reported; independent evaluation split not established |
| CCMT original-to-augmented lineage | Unresolved; near-duplicate and source-independent split analysis pending |
| Cross-dataset suitability assessment | Updated; dataset-specific limitations and experimental-design constraints documented |
| Consolidated experimental design | Completed and pushed; final dataset approval remains pending |
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

## 7. Pending work after 23 November review

### SWIR — Member 2

- Follow up on the response to Fahma's 21 November email to Lorraine Latchoumane.
- Confirm who holds the project's original SWIR archive and whether the public archive can be accessed by the team.
- Establish whether the original `.hyspex`, matching `.hdr`, dark-current, white-reference and acquisition records are available.
- Confirm whether the original filename-to-pot/side mapping file exists.
- Once the files are accessible, perform read-only archive, raw-file and header verification.
- Keep calibration, preprocessing and modelling on hold until technical verification and experimental-design approval.

### RGB — Member 3

**CCMT Tomato**
- Investigate the 10-image difference between the archive inventory and publication-reported augmented-image count.
- Investigate the 370-image difference between the archive raw-image inventory and publication-reported raw-image count.
- Continue original-to-augmented lineage and near-duplicate investigation.
- Establish whether a defensible source-image-independent evaluation split can be created.
- Keep existing Train/Test split independence unconfirmed.

**Rice Sheath Blight**
- Obtain exact severity-stage definitions and clarify the image-to-label mapping.
- Visually inspect representative images from all six severity folders when authorized.
- Investigate repeated-plant lineage, biological grouping and duplicate or near-duplicate images.

**NWRD Wheat Rust**
- Obtain explicit clarification of dataset image and mask reuse permissions.
- Resolve the paper and README train/validation/test split discrepancy.
- Perform visual image-mask alignment and mask-content checks when authorized.
- Investigate image quality and possible duplicate or near-duplicate images.

### VNIR — Hiba

- Verify whether reflectance calibration was applied to the local VNIR data.
- Obtain or reconstruct a reproducible NPZ processing pipeline.
- Confirm the number of plants per pot and the true experimental unit from authoritative records.
- Investigate physical leaf tracking across dates.
- Establish which metadata pots have usable VNIR image files.
- Design group-aware validation only after experimental units and dataset suitability are established.

### Project coordination — Hiba

- Maintain the central investigation tracker and update it only from reviewed evidence.
- Review new team submissions and supporting evidence.
- Maintain the cross-dataset suitability assessment and consolidated experimental design.
- Keep RGB, VNIR and SWIR assessments separate until scientific and technical compatibility is established.
- Identify candidate datasets and research objectives that can be supported by the available evidence.
- Obtain explicit experimental-design approval before preprocessing or model development.
## 8. VNIR follow-up items

- Verify whether reflectance calibration was applied to the local VNIR data.
- Obtain or reconstruct a reproducible NPZ processing pipeline.
- Confirm the number of plants per pot and the true experimental unit from authoritative records.
- Investigate physical leaf tracking across dates.
- Establish which metadata pots have usable VNIR image files.
- Design group-aware validation only after experimental units and dataset suitability are established.

## 9. Plan for 24 November 2026

| Person | Assignment |
|---|---|
| Hiba | Review the updated tracker, continue cross-dataset suitability and experimental-design integration, and identify the evidence required for final dataset selection. |
| Member 2 | Follow up on SWIR archive access and contact response; confirm the original archive holder and supporting calibration-file availability. |
| Member 3 | Continue resolving CCMT image-count and lineage questions, Rice severity-label and biological-grouping questions, and NWRD asset permissions and visual mask-validation requirements. |

**Team priority:** Resolve the remaining dataset-access, licensing, annotation, biological-grouping and leakage questions before approving preprocessing or model development.

## 10. Overall project assessment

**Current stage:** Evidence consolidation, dataset suitability assessment and experimental-design approval.

**Progress:** Investigation and documentation have advanced across VNIR, SWIR and the three RGB candidates. The latest review has improved archive inventory verification, documented important dataset limitations and clarified the remaining technical and scientific approval requirements.

**Main strengths:**

- Dataset sources, archive inventories and evidence limitations are being documented.
- Raw data preservation and read-only investigation principles are maintained.
- RGB, VNIR and SWIR investigations remain separate.
- Biological replication, metadata quality, temporal tracking and potential data leakage are considered before modelling.
- Cross-dataset suitability and experimental-design requirements are documented.
- A consolidated experimental-design framework is available for review.

**Main risks and unresolved issues:**

- **VNIR:** Calibration provenance, reproducible processing and biological sample tracking remain unresolved.
- **SWIR:** Original archive access, raw headers, calibration references and acquisition records remain unverified.
- **CCMT Tomato:** Publication/archive image-count discrepancies, image lineage and Train-Test checksum overlap prevent acceptance of the existing split as independent evaluation data.
- **Rice Sheath Blight:** Exact severity definitions, individual image-label correctness and biological grouping remain unresolved.
- **NWRD Wheat Rust:** Explicit dataset asset reuse permission, visual mask validation and split-description discrepancies remain unresolved.
- Cross-dataset compatibility and reliable temporal labels have not been established.
- The available evidence does not yet justify a unified multimodal forecasting claim.

**Next milestone:** Resolve the highest-priority evidence gaps, select scientifically defensible candidate datasets and research objectives, and obtain approval of the experimental design before preprocessing begins.

**Final note:** Documentation and archive-level verification do not equal scientific validation or modelling readiness. The project must establish whether each candidate dataset can support a defensible disease-detection, severity-estimation or forecasting objective before model development.
