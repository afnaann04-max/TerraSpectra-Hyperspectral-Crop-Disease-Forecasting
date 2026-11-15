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
| RGB source verification | Awaiting evidence |
| RGB dataset access | Awaiting confirmation |
| Initial SWIR inventory | Scan matching completed; further validation pending |
| Initial RGB inventories | Pending |

Statuses will be updated only after reviewing actual evidence.

## 5A. Daily progress update - 15 November 2026

### Hiba - VNIR
- Completed today's VNIR data-quality and calibration assessment documentation.
- Recorded missing-value and spectral-gap findings.
- Documented the 30 validation comparisons across 10 VNIR files and three CSV references.
- Created `VNIR_PROGRESS_REPORT_2026-11-15.md`.
- Calibration provenance, full-dataset class counts and biological replication remain unresolved.

### Member 2 - SWIR
- Today's initial investigation task completed.
- Submitted investigation files for review.
- Evidence review and further SWIR validation remain pending.

### Member 3 - RGB
- Today's assigned investigation task remains pending.
- No completion status is claimed until evidence is submitted and reviewed.

## 6. Scientific and repository rules

- Preserve original raw data.
- Keep SWIR and each RGB dataset separate during investigation.
- Do not merge modalities without a scientific justification.
- Do not begin final model training before experimental design review.
- Do not claim forecasting capability without suitable temporal evidence.
- Document commands, findings, errors and decisions.
- Do not commit or push changes without project lead approval.

## 7. Next review

Review both members' submitted evidence before assigning the next investigation phase.
