
# SWIR Initial File Inventory

**Source:** Recherche Data Gouv  
**DOI:** 10.57745/WVP0FJ  
**Inventory type:** Official repository-level inventory  
**Original inventory date:** 15 November 2026  
**Updated:** 17 November 2026

| File | Repository location | Format | Published size | Status |
|---|---|---|---:|---|
| 20210311.zip | Data/SWIR | ZIP | 4.3 GB | Official listing verified; historical 96-scan filename verification documented |
| SWIR_data.csv | Data annotation | CSV | 5.5 KB | Official listing and metadata contents reviewed |
| Data_description.csv | Data annotation | CSV | 9.2 KB | Official listing and metadata contents reviewed |
| VNIR_data.csv | Data annotation | CSV | 5.5 KB | Official listing verified; not part of SWIR archive verification |

### Archive checksum reference

`20210311.zip`

Official MD5:

`7ad4e3b5a9a14704af51191269d2e019`

The repository lists the archive size as 4.3 GB. The local archive checksum and ZIP integrity have not been independently verified in this update.

### Historical 96-scan verification

Filename-based verification was previously completed using the downloaded `20210311.zip` archive and the 48 pot records in `SWIR_data.csv`.

Previously documented results:

- Expected scans: 96
- Actual scans: 96
- Unique scan identities: 96
- Duplicate identities: 0
- Missing scans: 0
- Unexpected or unmatched identities: 0

**Folder anomaly:** `18_D.hyspex` was stored inside the `18_G` folder, although its filename was correct.

**Evidence limitation:** The original filename list and pot-side matching table were not preserved as separate files. The verification results are recorded in the earlier dataset assessment documentation. These historical results are referenced here and have not been independently rerun.

### Inventory limitations

- The repository reports 40 files in total, but the currently reviewed listing exposes only a portion of them.
- This is not a complete archive-internal filename inventory.
- The two SWIR metadata CSV files have been reviewed, including their columns, pot records, genotype, treatment, acquisition dates and missing-value conventions.
- The historical 96-scan verification is documented, but its original detailed filename and mapping evidence files are not separately available.
- Local archive checksum, ZIP integrity and duplicate checks have not been independently verified in this update.
- Exact acquisition calendar dates and some instrument acquisition settings are not available in the reviewed metadata files.

**Next evidence required:** If a fully reproducible scan audit is required, recover the original filename list and pot-side mapping table from the earlier dataset assessment records. Do not repeat the archive download or scan matching for the current investigation.
