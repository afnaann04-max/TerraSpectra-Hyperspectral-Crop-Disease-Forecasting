# RGB Progress Report — 15 November 2026

## 1. Work completed

Member 3 completed the initial source investigation of the candidate Rice Sheath Blight dataset.

### Dataset information

- **Dataset:** Colour-Mix Augmentation Dataset for Rice Sheath Blight Severity Estimation
- **Source:** Mendeley Data
- **Contributor:** Sonu Varghese K
- **DOI:** 10.17632/489spnkhp5.1
- **Version:** 1
- **Publication date:** 29 December 2025
- **Licence:** CC BY 4.0
- **Archive:** SBSeverity.zip
- **Reported archive size:** 4.06 GB
- **Reported original images:** 1,609 JPG images
- **Reported severity levels:** Six

Official source: https://data.mendeley.com/datasets/489spnkhp5/1

## 2. Published dataset characteristics

According to the Mendeley dataset description:

- Images were collected under natural field conditions.
- Collection location: Kottekkad, Kuttur, Thrissur, Kerala, India.
- Rice variety: Jyotsna.
- Camera: iPhone 6s, 12 MP.
- Blurred and duplicate images were reportedly removed.
- Images were reviewed by a domain expert.
- Each image is described as annotated into one of six progressive disease severity levels.

The published severity assessment considers lesion extent, lesion height progression along the sheath and symptom colour intensity.

## 3. Initial assessment

Positive aspects:
- Relevant to rice sheath blight severity estimation.
- Uses field-collected RGB images.
- Includes six reported severity levels.
- Published under CC BY 4.0.
- Collected in natural field conditions.

Unresolved questions:
- Exact names or numerical codes of the six severity levels.
- Precise severity boundaries and definitions.
- Annotation file format and image-to-label mapping.
- Internal archive structure and file counts.
- Class-wise image distribution.
- Whether the downloadable archive contains only original images or also generated augmentation outputs.

The dataset description identifies 1,609 original images and describes augmentation experiments. The actual downloadable archive contents have not been inspected, so its internal composition remains unverified.

## 4. Current recommendation

**Potentially Suitable — Pending Verification**

Keep this dataset as an RGB candidate. Do not treat it as the final approved dataset yet.

No archive download, preprocessing, class counting or model training has been performed.

## 5. Next investigation task — 16 November 2026

Member 3 will investigate:

1. Exact severity class names, codes and definitions.
2. The criteria used to distinguish severity levels.
3. Image-level annotation availability and format.
4. Whether individual images can be mapped to their severity labels.
5. Supporting evidence from the official dataset record and associated research documentation.

Expected output:
- Severity class reference table.
- Annotation information.
- Supporting source evidence.
- List of unresolved questions.

Archive inspection and image-level analysis will be assigned separately after this verification.

## 6. Status

- Initial source investigation: Completed.
- Candidate dataset selection: Pending.
- Severity class verification: Pending.
- Annotation verification: Pending.
- Archive inspection: Not started.
- Class distribution analysis: Not started.
- Duplicate and leakage assessment: Not started.
- Model development: Not started.