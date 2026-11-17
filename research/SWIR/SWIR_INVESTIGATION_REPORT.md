# SWIR Investigation Report
## TerraSpectra – Hyperspectral Crop Disease Forecasting

**Date:** 15 November 2026  
**Investigation role:** Member 2 – SWIR Dataset Verification  
**Dataset:** Early detection of septoria infection on wheat leaves using hyperspectral imaging data

### 1. Investigation objective

The objective is to independently investigate the official SWIR dataset source, DOI, licence, metadata and acquisition details, and review the team's existing archive and 96-scan verification evidence.

The dataset has already been downloaded by the team. No additional download was performed for this investigation.

### 2. Official source verification

| Field | Finding |
|---|---|
| Dataset title | Early detection of septoria infection on wheat leaves using hyperspectral imaging data |
| Author | Lorraine Latchoumane (INRAE) |
| Repository | Recherche Data Gouv |
| DOI | 10.57745/WVP0FJ |
| Version | 1.0 |
| Publication date | 15 November 2024 |
| Dataset access | Public |

**Official source:**  
https://entrepot.recherche.data.gouv.fr/dataset.xhtml?persistentId=doi:10.57745/WVP0FJ

**DOI:**  
https://doi.org/10.57745/WVP0FJ

**Verification status:** Verified against the official repository record.

### 3. Licence and usage conditions

The official repository identifies the dataset licence as:

**Etalab Open License 2.0**, compatible with CC-BY 2.0.

The repository also asks users to provide appropriate credit through the dataset citation.

For project documentation and any future publication, the team should retain the dataset title, author, DOI and licence information.

**Verification status:** Licence name and repository attribution guidance verified. The team should consult the actual licence text before applying it to redistributed or modified materials.

### 4. Existing SWIR archive

The repository lists the following file:

| Field | Official repository information |
|---|---|
| Filename | 20210311.zip |
| Repository folder | Data/SWIR |
| Format | ZIP archive |
| Published size | 4.3 GB |
| Access | Public |
| Published MD5 | 7ad4e3b5a9a14704af51191269d2e019 |
| Publication date | 15 November 2024 |

The team has reported that it already downloaded this archive and found all 96 expected pot-side scans.

However, the archive is currently understood to be on another team member's laptop. I have not independently accessed the local archive or repeated its file checks.

The reported local size is approximately 4.60 GB, while the repository displays 4.3 GB. This difference needs clarification using the exact local file size in bytes and the repository's displayed units.

**Verification status:**
- Official archive listing: Verified.
- Repository checksum: Verified from the listing.
- Local archive integrity: Pending independent confirmation.
- Reported 96/96 scan match: Previously reported by the team; evidence review pending.

### 5. Dataset description and experimental details

The official repository describes a hyperspectral imaging dataset containing:

- Healthy wheat leaves.
- Leaves infected with *Zymoseptoria tritici*, the fungus responsible for Septoria tritici blotch.
- Two durum wheat genotypes.
- Controlled experimental conditions.
- Two spectral imaging systems: VNIR and SWIR.
- Eighteen acquisition dates, ranging from one day before inoculation to twenty days after inoculation.
- A total of 1,175 images for each wavelength range, providing information on 3,326 leaves measured throughout the experiment.

These are dataset-level details. They do not establish the exact number of independent plants, pots or biological replicates represented by the 96 scans.

### 6. Metadata investigation

The official repository lists two relevant documentation files:

| Filename | Repository description | Published size |
|---|---|---:|
| SWIR_data.csv | SWIR data annotation | 5.5 KB |
| Data_description.csv | Data annotation/documentation | 9.2 KB |

The actual contents of these two CSV files have not yet been independently inspected in this investigation.

The following metadata questions therefore remain open:

1. What does each pot ID represent?
2. What is the exact meaning of D and G in the scan naming convention?
3. How are individual scans linked to pots, leaves and experimental conditions?
4. Are acquisition dates explicitly recorded for every scan?
5. Are genotype, infection status and inoculation information available for each scan?
6. Are repeated measurements from the same pot or plant identifiable?
7. Are the scan naming conventions explained in the documentation?

These questions must be answered from the actual metadata files or original experimental documentation. No naming interpretation should be assumed without evidence.

### 7. Existing 96-scan verification

The team has reported that 96 out of 96 expected pot-side scans were found and matched.

This investigation does not claim to have independently reproduced that result.

To complete the evidence review, the following existing materials are required:

- The expected 96-scan filename list.
- The actual archive filename listing or inventory.
- The scan-to-pot matching table.
- The method used to identify expected scans.
- The missing-file and duplicate-file check results.

The review should confirm that all expected filenames are present, no unexpected duplicates exist, and the mapping is consistent with the metadata.

A scan count alone does not establish 96 independent biological samples.

### 8. Unresolved issues

| Issue | Current status | Evidence needed |
|---|---|---|
| Local archive integrity | Pending | Local MD5 and ZIP integrity result |
| Archive size difference | Unresolved | Exact local size in bytes |
| 96 expected scan matches | Previously reported | Filename list and matching table |
| Missing or duplicate scans | Pending independent review | Inventory and check output |
| Pot ID interpretation | Unresolved | Metadata CSV and documentation |
| D/G naming convention | Unresolved | Naming explanation or original documentation |
| Scan-level acquisition dates | Unresolved | SWIR metadata |
| Genotype and infection labels | Unresolved | Metadata-to-scan mapping |
| Biological replication | Unresolved | Experimental design documentation |

### 9. Initial findings

The official dataset source, DOI, publication details, licence and archive listing have been verified from the repository.

The repository describes a controlled wheat Septoria experiment with two durum wheat genotypes, healthy and infected leaves, two spectral ranges and eighteen acquisition dates.

The team's reported 96/96 scan verification has not been independently reproduced because the archive and its verification evidence are on another team member's laptop.

The most important next step is to inspect the existing `SWIR_data.csv`, `Data_description.csv`, scan filename inventory and matching table. This will help establish the relationship between scan names, pot IDs, acquisition dates and experimental information.

### 10. Conclusion

The official SWIR dataset source and licence have been identified and documented. The repository also provides a published archive checksum that can be compared with the team's existing archive without downloading it again.

The investigation remains partially complete. Independent confirmation of the local archive, 96-scan matching, metadata interpretation and scan-level acquisition details requires access to the team's existing evidence.

No raw files were modified, no additional archive was downloaded, and no model training or preprocessing was performed.

---

**Prepared by:** Member 2  
**Project:** TerraSpectra – Hyperspectral Crop Disease Forecasting