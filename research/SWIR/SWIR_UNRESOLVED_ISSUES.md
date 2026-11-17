

\# SWIR Unresolved Issues and Technical Limitations



\*\*Project:\*\* TerraSpectra – Hyperspectral Crop Disease Forecasting  

\*\*Dataset:\*\* Early detection of septoria infection on wheat leaves using hyperspectral imaging data  

\*\*DOI:\*\* 10.57745/WVP0FJ  

\*\*Updated:\*\* 17 November 2026



\## 1. Archive verification limitations



\- Historical filename-based verification documented 96 expected scans, 96 actual scans, 96 unique identities, zero duplicates, zero missing scans and zero unexpected or unmatched identities.

\- The original filename list and pot-side matching table were not preserved as separate files.

\- The historical results are referenced from earlier dataset assessment documentation and have not been independently rerun.

\- Local archive checksum, ZIP integrity and duplicate checks have not been independently verified in this update.



\## 2. Acquisition details requiring confirmation



The 2025 research paper identifies the SWIR camera as HySpex SWIR-384 and reports the following study-specific specifications:



\- Spectral range: 964–2494 nm

\- Spectral channels: 256

\- Image resolution: 420 × 320 pixels

\- Acquisition mode: Pushbroom

\- Camera-to-leaf distance: 21.5 cm

\- Lens focal distance: 30 cm

\- Pixel dimensions: 217 × 217 µm



The following acquisition parameters were not established from the reviewed study methods:



\- Exact integration time

\- Exact frame period

\- Scan speed

\- Whether all acquisition sessions used identical instrument settings



These details require confirmation from the authors, original instrument configuration files or additional technical documentation.



\## 3. Acquisition dates and missing observations



\- Metadata records 18 acquisition time points in days post inoculation (dpi): -1, 0, 4–8 and 10–20.

\- Calendar dates and clock times for every acquisition are not established by the reviewed metadata.

\- No acquisitions were reported at 1, 2 and 3 dpi because plants were bagged to maintain high humidity and promote infection.

\- The 9 dpi acquisition was affected by technical problems, according to the paper.

\- One explicit `NA` occurs in `SWIR\_data.csv`: pot 23, EPO\_67, Non-infected, 10 dpi, G side. The metadata identifies a technical malfunction but does not specify its exact cause.

\- The 10 dpi missing value must not be assumed to be related to the separate 9 dpi technical interruption.



\## 4. Metadata interpretation limitations



\- Empty measurement cells indicate no HSI acquisition for the corresponding pot, date and side.

\- `NA` indicates missing data due to technical malfunction.

\- The confidence-level field uses 1 for high confidence and 2 for low confidence, based on visual symptoms.

\- The inoculum concentration is printed as `1.106 spores/mL` in the metadata notes. Its intended notation should not be reinterpreted without confirmation from the study protocol.

\- The sum of numeric leaf-count entries is 3,326; this is not necessarily a count of 3,326 unique leaves.

\- The metadata does not establish the exact cause of every empty cell.



\## 5. Dataset scope and completeness



\- The official repository reports 40 files, while the reviewed repository listing exposes only a portion of them.

\- The reviewed inventory is not a complete archive-internal file listing.

\- The `20210311.zip` archive is one date-named SWIR archive and should not be assumed to represent every acquisition date.

\- Additional date-named archives were identified in the research investigation, but the reviewed list is not confirmed to be exhaustive.



\## 6. Recommended follow-up



1\. Recover the original scan filename list and pot-side mapping table if reproducible audit evidence is required.

2\. Confirm exact instrument acquisition settings from original technical records or the dataset authors.

3\. Seek a complete acquisition-date mapping if calendar dates are needed.

4\. Clarify the printed inoculum concentration notation using the original protocol.

5\. Confirm whether additional repository files or archives are required before designing the final modelling dataset.



\## 7. Scope restrictions for this investigation



\- No new archive download is required for this update.

\- Historical scan matching will not be repeated.

\- Raw hyperspectral data must remain unchanged.

\- No preprocessing, model training or disease prediction claims are made by this investigation.



\*\*Related report:\*\* `SWIR\_FINAL\_INVESTIGATION\_REPORT\_2026-11-17.md`  

\*\*Related inventory:\*\* `SWIR\_INITIAL\_FILE\_INVENTORY.md`



