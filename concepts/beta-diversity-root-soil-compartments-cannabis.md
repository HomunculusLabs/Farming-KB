---
title: Beta-Diversity Patterns Across Root-Soil Compartments
created: 2026-04-28
tags: [microbiome, beta-diversity, soil-science, cannabis]
date: 2026-04-28
updated: 2026-04-28
sources:
  - /Users/t3rpz/wiki/raw/papers/understanding-cultivar-specificity-cannabis-microbiome.md
type: concept
---

# Beta-Diversity Patterns Across Root-Soil Compartments

## Overview

Beta-diversity measures compositional dissimilarity between microbial
communities. In Winston et al. (2014), both weighted and [[weighted-vs-unweighted-unifrac-cannabis-strain-microbiome]]
metrics revealed that soil type dominates [[core-endorhiza-bacterial-community-composition-cannabis]] while
cultivar primarily affects abundance structure. These patterns provide
critical evidence for the
[[cannabis-cultivar-microbiome-specificity]]), confirming compartment-
specific [[cannabis-cultivar-effects-soil-microbiome]].

## Experiment 2: Two Cultivars, Two Soil Types

The second experiment grew [[soil-heritability-otu-sharing-white-widow-cross-soil-cannabis-endorhiza]] and [[maui-wowie]] across two distinct
soils, providing a more rigorous test of the two-tier model.

### Unweighted UniFrac

All three factors showed significant effects on community beta-diversity:

- **Soil type**: ADONIS R2 = 0.32, p = 0.001 (strongest)
- **Sample type**: ADONIS R2 = 0.12, p = 0.005
- **Strain**: ADONIS R2 = 0.10, p = 0.008

Individual compartment comparisons: endorhiza (R2 = 0.10, p = 0.001) and
rhizosphere (R2 = 0.05, p = 0.04) were significant, but bulk soil was not
(R2 = 0.04, p = 0.12).

### Weighted UniFrac

Weighted analysis produced much stronger strain effects, consistent with
cultivar operating on abundance rather than presence/absence:

- **Soil type**: ADONIS R2 = 0.21, p = 0.001
- **Sample type**: ADONIS R2 = 0.27, p = 0.001
- **Strain**: ADONIS R2 = 0.27, p = 0.001

Strain became equally important as sample type, and rhizosphere clustering
was now significant (R2 = 0.13, p = 0.001). Bulk soil remained borderline
(R2 = 0.06, p = 0.054).

## Pooled Analysis: Both Experiments

Combining experiments confirmed robustness of all three factors:

- Soil type: ADONIS R2 = 0.196 (unweighted), R2 = 0.323 (weighted)
- Sample type: ADONIS R2 = 0.086 (unweighted), R2 = 0.229 (weighted)
- Strain: ADONIS R2 = 0.178 (unweighted), R2 = 0.301 (weighted)
- All p = 0.001

In the pooled weighted analysis, strain (R2 = 0.301) nearly matched soil
type (R2 = 0.323), demonstrating that cultivar genotype is almost as
important as soil chemistry for [[edaphic-determinants-cannabis-microbiome-community-structure]].

## Inter-Compartment Distance Comparisons

Pairwise beta-diversity distances revealed clear community similarity
hierarchies for both unweighted and weighted analyses:

- Rhizosphere-endorhiza distances significantly lower than bulk
  soil-endorhiza distances (unweighted: t = 24.59, p < 0.001;
  weighted: t = 211.82, p < 0.001)
- Rhizosphere-bulk soil distances significantly lower than bulk
  soil-endorhiza distances (unweighted: t = 25.15, p < 0.001;
  weighted: t = 211.56, p < 0.001)
- Rhizosphere-endorhiza distances not significantly different from bulk
  soil-endorhiza distances (unweighted: t = -2.10, p = 0.109;
  weighted: t = -2.23, p = 0.078)

This confirms bulk soil and rhizosphere are more similar to each other
than either is to the endorhiza. However, the non-significant difference
between rhizosphere-endorhiza and bulk soil-endorhiza distances provides
mixed support for the first step of the two-tier model.

## OTU Abundance Correlation Across Compartments

Mean abundance of the 51 OTUs differentiating sample types showed
progressive decorrelation from soil to root:
