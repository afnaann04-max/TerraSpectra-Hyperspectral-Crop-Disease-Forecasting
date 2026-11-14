# VNIR Experimental Design and Limitations Assessment

**Project:** TerraSpectra – Hyperspectral Crop Disease Forecasting
**Assessment date:** 14 November 2026
**Dataset:** Wheat Septoria – VNIR
**Status:** Experimental design investigation completed for the four selected scans

---

## 1. Purpose

This assessment investigates whether the selected VNIR dataset provides a sufficiently reliable experimental basis for machine-learning development.

The investigation focuses on:

- Biological sample independence and replication.
- Pot, genotype and treatment consistency.
- Association between scan identity and treatment.
- Recorded acquisition settings.
- Potential data leakage and evaluation limitations.

The conclusions apply to the four selected VNIR scans and should not automatically be generalized to the complete original experiment.

## 2. Selected Dataset Overview

The current selected VNIR feature dataset contains:

| Item | Count |
|---|---:|
| Raw selected scans | 4 |
| Selected pots | 4 |
| Annotated leaves | 10 |
| Infected leaves | 6 |
| Non-infected leaves | 4 |
| Pixel observations | 272,912 |
| Spectral bands in baseline dataset | 216 |
| Candidate spectral bands | 30 |

The four selected scans are:

| Scan ID | Pot | Genotype | Treatment | Selected leaves |
|---|---:|---|---|---:|
| 01_D | 1 | EPO_68 | Infected | 3 |
| 04_D | 4 | EPO_68 | Non-infected | 2 |
| 07_D | 7 | EPO_67 | Infected | 3 |
| 10_D | 10 | EPO_67 | Non-infected | 2 |

The original metadata lists three leaves for each selected pot's D side. However, only ten leaves are represented in the selected feature dataset.

## 3. Biological Independence and Replication

### 3.1 Metadata findings

The original `Data_description.csv` metadata identifies samples using pot, side, leaf, genotype, treatment and confidence level.

The metadata explains that:

- D represents the right side of a pot.
- G represents the left side of a pot.
- Between one and three wheat leaves per pot side were imaged.
- Infected plants were inoculated with *Zymoseptoria tritici* strain P1a.
- Non-infected plants received the water/Tween control.
- Confidence level 1 represents high confidence; level 2 represents low confidence.

All selected pot records were checked using the Windows-1252 (cp1252) encoding.

### 3.2 Mapping validation

The selected pot mapping was checked against the original metadata.

Results:

- All four selected pots were found.
- All four expected genotype-treatment mappings passed.
- No selected pot had multiple genotypes.
- No selected pot had multiple treatments.
- No selected pot had multiple confidence levels.
- All selected metadata records had confidence level 1.

The mapping and label consistency checks passed.

### 3.3 Biological replication limitation

Four distinct pot identifiers are present in the selected subset:

- Two infected pots.
- Two non-infected pots.
- One pot for each genotype-treatment combination.

However, the available metadata does not establish:

- Whether each pot contained exactly one biological plant or multiple plants.
- Whether treatment assignment was randomized.
- Whether additional independent experimental replicates are available outside the selected scans.
- Whether the four selected pots represent independent biological experimental units.

The number of independent biological plants represented by the four selected pots is currently unknown. Therefore, distinct pot identifiers alone are not sufficient to prove biological independence.

Pixels and leaves are nested observations, not independent treatment replicates.

**Conclusion:** The selected subset has limited biological replication. More independent pots and scans are needed to support robust generalization.

## 4. Scan-Treatment Association

The candidate feature dataset was inspected using Scan_ID, Leaf_ID, Treatment and Genotype.

### 4.1 Scan-level findings

| Scan ID | Pixel count | Leaf count | Treatment | Genotype |
|---|---:|---:|---|---|
| 01_D | 67,639 | 3 | Infected | EPO_68 |
| 04_D | 44,618 | 2 | Non-infected | EPO_68 |
| 07_D | 91,972 | 3 | Infected | EPO_67 |
| 10_D | 68,683 | 2 | Non-infected | EPO_67 |

Every selected scan contains exactly one treatment and one genotype.

No scan contains both infected and non-infected observations.

### 4.2 Confounding risk

Treatment is perfectly associated with scan identity in the selected subset.

This creates a serious experimental-design concern.

A machine-learning model might learn scan-specific or pot-specific spectral differences instead of disease-related patterns.

The genotype-treatment combinations are:

- EPO_68: one infected pot and one non-infected pot.
- EPO_67: one infected pot and one non-infected pot.

However, there is only one selected pot for each combination. This does not provide sufficient independent replication to separate treatment effects reliably from pot- and scan-specific variation.

## 5. Acquisition Header Comparison

All four original ENVI header files were located and inspected recursively under:

`data/raw/VNIR/20210311/`

The recorded acquisition parameters were compared.

| Parameter | 01_D | 04_D | 07_D | 10_D |
|---|---:|---:|---:|---:|
| Integration time | 6500 | 6500 | 6500 | 6500 |
| Binning | 2 | 2 | 2 | 2 |
| Camera temperature (recorded value) | 0 | 0 | 0 | 0 |
| Lines | 1370 | 1370 | 1370 | 1370 |
| Bands | 216 | 216 | 216 | 216 |
| Samples | 1024 | 1024 | 1024 | 1024 |
| Acquisition date | 2021-03-11 | 2021-03-11 | 2021-03-11 | 2021-03-11 |
| Data type | 12 | 12 | 12 | 12 |
| Interleave | BIL | BIL | BIL | BIL |
| Byte order | 0 | 0 | 0 | 0 |

Recorded acquisition start times:

| Scan | Start time |
|---|---|
| 01_D | 08:31:43 |
| 07_D | 08:44:24 |
| 04_D | 09:33:49 |
| 10_D | 09:42:12 |

The wavelength range is approximately 411.360–993.172 nm for all four scans.

### 5.1 Interpretation

No differences were found in the acquisition parameters recorded in the inspected headers.

This is a positive finding, but it does not prove that every acquisition condition was identical.

The headers do not establish whether illumination, sample positioning, environmental conditions or other unrecorded factors were consistent.

Therefore, the possibility of scan-specific effects cannot be eliminated.

## 6. Machine-Learning Evaluation Risks

### 6.1 Pixel-level data leakage

The dataset contains 272,912 pixel observations, but these pixels come from only ten leaves and four selected pots/scans.

A random pixel-level train/test split could place pixels from the same leaf and scan in both training and testing sets.

This could produce overly optimistic performance estimates.

### 6.2 Group-aware validation

The split strategy must respect the biological hierarchy.

Potential grouping levels include:

- Pot.
- Plant, once its relationship to pots is established.
- Leaf.
- Scan.

The correct experimental unit must be confirmed from the original experimental design.

Grouping by scan or pot is more appropriate than treating every pixel as an independent sample. However, only four selected groups are available, with one group for each genotype-treatment combination.

Consequently, this subset is insufficient to establish a reliable, balanced independent holdout evaluation across all genotype-treatment combinations. Group-aware validation remains the appropriate principle, but the available four groups severely limit what can be evaluated.

### 6.3 Recommended evaluation precautions

- Do not use a random pixel-level split as the primary validation strategy.
- Keep related pixels and leaves together within the appropriate biological group.
- Perform imputation, feature selection and scaling using training data only.
- Report the number of independent biological groups, not just pixel counts.
- Evaluate at leaf or plant level where appropriate.
- Clearly report the limitations of any preliminary model results.

## 7. Impact on Project Scope

The current selected VNIR labels identify infected and non-infected samples.

They do not establish repeated observations over time or future disease outcomes.

Therefore:

- Disease classification is supported as the current modelling objective.
- Early detection requires suitable pre-symptomatic observations and ground truth.
- True disease forecasting requires repeated temporal observations and future outcome labels.

The project should not claim validated forecasting unless suitable temporal data are obtained.

## 8. Recommended Actions

1. Confirm the number of biological plants represented by each pot.
2. Obtain the original experimental design and treatment-randomization information.
3. Ask the data provider or team whether additional independent pots and scans are available.
4. Seek additional infected and non-infected replicates for both genotypes.
5. Investigate any available acquisition and environmental metadata.
6. Establish a group-aware validation strategy before model development.
7. Keep the baseline 216-band and candidate 30-band datasets available for later controlled experiments.
8. Treat the current results as exploratory until independent validation is possible.

## 9. Final Assessment

The selected VNIR data passed the previously completed structural, identity, label and data-quality validation checks.

The present investigation also confirmed that all four selected scans have consistent recorded acquisition settings and that their pot, genotype and treatment mappings are internally consistent.

However, the subset has only four selected pots, ten leaves and one pot per genotype-treatment combination. Treatment is perfectly associated with scan identity.

These limitations create a substantial risk of scan-specific learning and overly optimistic model evaluation.

The data can support carefully labelled exploratory analysis and preliminary model development, but reliable generalization to independent plants has not yet been demonstrated.

Additional independent biological replicates and a verified experimental design are needed before making strong claims about generalization to unseen plants.

---

**Assessment status:** VNIR experimental-design investigation completed for the selected four-scan subset. Additional experimental information and independent samples remain necessary.
