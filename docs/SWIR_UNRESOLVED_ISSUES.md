# SWIR Unresolved Issues
## TerraSpectra – 16 November 2026

| ID | Issue | Current finding | Evidence / next action |
|---|---|---|---|
| U01 | Exact scan filename convention | Not established by the two metadata CSVs alone | Review the existing filename list and matching table. |
| U02 | Independent review of 96/96 result | Filename list and matching table were not included in this upload | Obtain both existing evidence files; do not repeat the matching. |
| U03 | Calendar acquisition dates | Metadata gives days post-inoculation (dpi), not calendar dates or clock times | Consult original acquisition log / experimental protocol. |
| U04 | Missing dpi points | Listed dates omit 1, 2, 3 and 9 dpi | Confirm whether no acquisitions were planned or whether these dates are absent for another reason. |
| U05 | Technical missing value | One NA at pot 23, 10 dpi, G side | Seek acquisition/technical log for the cause. |
| U06 | Inoculum concentration notation | Supplied note says `1.106 spores/mL` | Check original protocol or paper; do not reinterpret notation without evidence. |
| U07 | Confidence assessment protocol | Level 1 high and level 2 low confidence, based on visual symptoms | Obtain the visual scoring protocol if available. |
| U08 | Experimental unit / biological replication | Pot and leaf records are not necessarily independent replicates | Review full experimental design and repeated-measure protocol. |
| U09 | Acquisition settings | Exact instrument settings and calendar acquisition details are not in these two CSVs | Consult instrument metadata, acquisition log or associated methods paper. |
| U10 | Leaf-to-file mapping | Metadata has Pot/Side/Leaf but exact file-level linkage not shown here | Validate against existing scan filename list and mapping table. |

## Resolved / verified during this investigation

- The uploaded `SWIR_data.csv` MD5 matches the official repository's published checksum.
- The uploaded `Data_description.csv` MD5 matches the official repository's published checksum.
- Official DOI and Etalab Open License 2.0 were confirmed on the repository record.

## Confirmed interpretations (not unresolved)

- G = left side of the pot.
- D = right side of the pot.
- Infected / Non-infected is stored in Treatment, not in D/G.
- Confidence level 1 = high; 2 = low.
- Empty SWIR count-table cells mean no HSI acquisition due to sampling.
- `NA` means missing data due to technical malfunction.
