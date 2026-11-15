# TerraSpectra Team Investigation Tracker

**Date:** 15 November 2026
**Project stage:** Dataset source verification and initial investigation

## 1. Team responsibilities

| Member | Responsibility | Assigned datasets |
|---|---|---|
| Hiba | VNIR investigation, coordination and integration | Wheat Septoria VNIR |
| Member 2 | SWIR investigation | Wheat Septoria SWIR |
| Member 3 | RGB investigation | NWRD Wheat Rust, CCMT Tomato, Rice Sheath Blight |

## 2. Existing dataset availability

Current verified local status as of 15 November 2026:

| Dataset | Existing local status |
|---|---|
| Wheat Septoria VNIR | Available; selected scans investigated |
| Wheat Septoria SWIR | Official archive downloaded; 96/96 expected scans matched; further validation pending |
| NWRD Wheat Rust | Not located in searched project folders |
| CCMT Tomato | Not located in searched project folders |
| Rice Sheath Blight | Not located in searched project folders |

Not located does not mean publicly unavailable. External source and access verification are pending.

## 3. Today's investigation assignments

### Member 2 — SWIR Wheat Septoria

- Verify and document the original dataset source and download details.
- Check licence and usage conditions, if available.
- Validate the downloaded archive and its file inventory.
- Document the 96/96 expected pot-side scan matches.
- Record unresolved issues, including metadata and acquisition details.

### Member 3 — RGB datasets

Investigate each dataset separately:

1. NWRD Wheat Rust
2. CCMT Tomato
3. Rice Sheath Blight

For each dataset:

- Verify the original source.
- Check access and availability.
- Verify licence information, if available.
- Inspect the folder structure.
- Prepare an initial file inventory.

### Hiba — Coordination

- Coordinate both investigations.
- Collect source and access evidence.
- Review the submitted inventories.
- Track blockers and unresolved questions.
- Maintain the central project documentation.

## 4. Required evidence from team members

Each member must provide:

- Original dataset source or download link.
- Access or download confirmation.
- Licence information, if available.
- Folder structure.
- File names, formats and verified counts.
- Errors and unresolved issues.
- Initial investigation report.

## 5. Current progress status

| Work item | Status |
|---|---|
| VNIR investigation | Completed for selected available scans |
| SWIR source verification | Source identified; evidence review pending |
| SWIR raw-data access | Archive downloaded; 96/96 expected scans matched |
| RGB source verification | Initial Rice source identified; NWRD and CCMT verification pending |
| RGB dataset access | Rice archive not downloaded; other datasets awaiting confirmation |
| Initial SWIR inventory | Scan matching completed; further validation pending |
| Initial RGB investigation | Rice Sheath Blight initial source investigation completed |
| NWRD and CCMT inventories | Pending |

Statuses will be updated only after reviewing actual evidence.

## 5A. Daily progress update — 15 November 2026

### Hiba — VNIR

- Completed today's VNIR data-quality and calibration assessment documentation.
- Recorded missing-value and spectral-gap findings.
- Documented the 30 validation comparisons across 10 VNIR files and three CSV references.
- Created `VNIR_PROGRESS_REPORT_2026-11-15.md`.
- Calibration provenance, full-dataset class counts and biological replication remain unresolved.
- Documentation committed and pushed to GitHub in commit `77602be`.

### Member 2 — SWIR

- Today's initial investigation task completed.
- Submitted investigation files for review.
- Evidence review and further SWIR validation remain pending.

### Member 3 — RGB

- Completed today's initial source investigation of the Rice Sheath Blight candidate dataset.
- Identified the Mendeley Data record: DOI `10.17632/489spnkhp5.1`.
- Recorded the reported 1,609 original JPG images, six severity levels and CC BY 4.0 licence.
- Documented dataset characteristics, preliminary suitability and unresolved questions.
- Dataset retained as a candidate; final selection is not approved.
- Created `RGB_PROGRESS_REPORT_2026-11-15.md`.

**Unresolved Rice dataset questions:**

- Exact names, codes and definitions of the six severity levels.
- Annotation file format and image-to-label mapping.
- Whether original and augmented images are stored separately.
- Internal archive structure and class-wise image counts.

## 5B. Next tasks — 16 November 2026

### Hiba

- Review Member 2's submitted SWIR investigation files.
- Identify missing evidence and corrections.
- Document verified SWIR findings.
- Continue outstanding VNIR investigation only where necessary.
- Avoid repeating completed VNIR checks.

### Member 2 — SWIR

- Continue SWIR investigation based on the evidence review.
- Address identified gaps in source verification, metadata and acquisition information.
- Submit supporting evidence and an updated investigation report.

### Member 3 — RGB

**Primary task: Rice Sheath Blight severity-label verification.**

- Verify the exact six severity class names or numerical codes.
- Identify the definitions and criteria for each severity level.
- Verify image-level annotation availability.
- Identify the annotation format and image-to-label mapping.
- Provide supporting evidence from the official dataset record and associated research documentation.

**Expected output:**

- Severity class reference table.
- Annotation information.
- Source links and supporting evidence.
- List of unresolved questions.

Do not download the 4.06 GB archive or begin preprocessing until the team approves the next step.

NWRD Wheat Rust and CCMT Tomato investigations remain pending.

## 6. Scientific and repository rules

- Preserve original raw data.
- Keep SWIR and each RGB dataset separate during investigation.
- Do not merge modalities without scientific justification.
- Do not begin final model training before experimental design review.
- Do not claim forecasting capability without suitable temporal evidence.
- Document commands, findings, errors and decisions.
- Do not commit or push changes without project lead approval.

## 7. Next review

- Review Member 2's SWIR evidence.
- Review Member 3's Rice severity-label investigation.
- Check progress on NWRD Wheat Rust and CCMT Tomato.
- Update dataset suitability and investigation status based on verified evidence.
- Assign the next tasks based on the actual findings.