# Rice Sheath Blight – Severity Label Verification Report

**Project:** TerraSpectra – RGB Dataset Investigation  
**Team Member:** Member 3  
**Date:** 16 November 2026

## 1. Dataset Identification

- **Dataset:** Colour-Mix Augmentation Dataset for Rice Sheath Blight Severity Estimation
- **Source:** Mendeley Data
- **DOI:** 10.17632/489spnkhp5.1
- **Dataset URL:** https://data.mendeley.com/datasets/489spnkhp5/1
- **Reported original images:** 1,609 JPG images
- **Reported severity classes:** Six
- **Download status:** Not downloaded
- **Dataset status:** Candidate only; not finally approved

## 2. Severity Class Investigation

The official Mendeley description confirms that every image is annotated into one of six progressive disease severity levels.

However, the exact names, numerical codes and definitions of the six classes are not provided in the publicly accessible description.

| Class number | Exact class name/code | Severity definition |
|---|---|---|
| 1 | Not disclosed | Not disclosed |
| 2 | Not disclosed | Not disclosed |
| 3 | Not disclosed | Not disclosed |
| 4 | Not disclosed | Not disclosed |
| 5 | Not disclosed | Not disclosed |
| 6 | Not disclosed | Not disclosed |

No class names or severity boundaries have been assumed or invented.

## 3. Documented Severity Assessment Criteria

According to the official dataset description, visual severity assessment considers:

- Lesion extent.
- Lesion height progression along the sheath.
- Symptom colour intensity.
- Lesion density and spatial spread.

The images were reviewed by a domain expert from the Department of Plant Pathology, College of Agriculture, Padannakkad, Kasargod.

The description mentions visual scoring using a standard evaluation scale but does not identify the exact scale or provide its numerical scoring criteria.

## 4. Severity Measurement Method

| Measurement | Verification status |
|---|---|
| Lesion extent | Mentioned |
| Lesion height progression | Mentioned |
| Symptom colour intensity | Mentioned |
| Lesion density and spatial spread | Mentioned |
| Percentage of affected sheath | Not explicitly specified |
| Lesion area percentage | Not explicitly specified |
| Relative lesion height (RLH) | Not confirmed |
| Exact severity thresholds | Not disclosed |

Other rice sheath blight studies use standard evaluation systems and relative lesion height. However, the use of a particular system in this dataset cannot be assumed without explicit documentation.

## 5. Annotation Investigation

- Image-level severity annotation is reported in the Mendeley description.
- An annotation file is not identified in the public documentation.
- CSV, Excel, JSON or text annotation formats are not specified.
- Folder-based class labels are not verified.
- The mapping between individual image filenames and severity labels cannot currently be independently confirmed.
- Segmentation masks, bounding boxes and pixel-level annotations are not documented in the accessible description.

The NLM catalogue also lists no associated publication data and no supplementary data for this dataset.

## 6. Research Paper Investigation

The official Mendeley dataset description and available catalogue information were examined.

An accessible associated research paper containing the exact six class definitions could not be located.

A related research listing by the contributor was found, but its full text was not accessible for verification. Therefore, it has not been used as evidence for the six severity labels.

## 7. Unresolved Questions

1. What are the exact names or numerical codes of the six severity classes?
2. What is the definition of each severity class?
3. Which standard disease severity evaluation scale was used?
4. Are the classes based on relative lesion height, percentage of affected sheath, lesion area or a combination of visual criteria?
5. Are numerical severity scores available for each image?
6. Is there a separate CSV, Excel, JSON or text annotation file?
7. Are severity labels encoded in image filenames or folder names?
8. Can every original image be mapped to its corresponding severity label?
9. Is there a research paper or supplementary document containing the full scoring rubric?

## 8. Conclusion

**Verification Status: PARTIALLY VERIFIED**

The official Mendeley dataset description confirms that:
- The dataset reports six progressive disease severity levels.
- Image-level severity annotation is reported for the images.
- Severity assessment considers lesion extent, lesion height progression, symptom colour intensity, lesion density and spatial spread.

However, the following information remains unverified:
- Exact names or numerical codes of the six severity classes.
- Severity definitions and class boundaries.
- The specific scoring scale used.
- The annotation file and its format.
- The actual mapping between individual image files and their corresponding severity labels.

A related ResearchGate publication was identified, but it has not been established as direct supporting documentation for this specific dataset's six-class annotation scheme.

The standard 0–9 rice sheath blight severity scale must not be assumed to apply to this dataset.

The dataset remains a candidate and should not receive final approval until the missing severity-label and annotation information is clarified.

**Restrictions followed:**
- The 4.06 GB archive was not downloaded.
- No image preprocessing was performed.
- No image analysis or model training was started.
- No final dataset approval was made.

## 9. Sources

1. Official Mendeley Data record: https://data.mendeley.com/datasets/489spnkhp5/1
2. NLM Dataset Catalogue: https://datasetcatalog.nlm.nih.gov/dataset?q=0001394886
3. Related contributor research listing: https://www.researchgate.net/publication/403426363_Context-Aware_Explanation_Drift_Detection_CA-EDD_For_Plant_Disease_Severity_Estimation
4. Example of separate rice sheath blight severity assessment research: https://pmc.ncbi.nlm.nih.gov/articles/PMC10642295/

**End of report.**