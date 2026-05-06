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
communities. In Winston et al. (2014), both weighted and unweighted UniFrac
metrics revealed that soil type dominates community composition while
cultivar primarily affects abundance structure. These patterns provide
critical evidence for the
[[cultivar-cannabis-microbiome-two-tier-selection-model]].

## Experiment 1: Three Cultivars, One Soil

The first experiment compared endorhiza, rhizosphere, and bulk soil from
Burmese, Bookoo Kush, and Sour Diesel grown in the same soil.

### Compartment Clustering (Unweighted UniFrac)

- **Endorhiza**: ADONIS R2 = 0.26, p = 0.001 (significantly distinct)
- **Bulk soil**: ADONIS R2 = 0.14, p = 0.001 (significantly distinct)
- **Rhizosphere**: ADONIS R2 = 0.07, p = 0.07 (not significant)

Weighted UniFrac produced stronger effects: endorhiza R2 = 0.59, bulk
soil R2 = 0.29 (both p = 0.001), but rhizosphere remained non-significant
(R2 = 0.09, p = 0.10).

### Strain-Level Clustering

Division of all communities by strain was not significant (weighted:
R2 = 0.11, p = 0.25; unweighted: R2 = 0.11, p = 0.15). However,
endorhiza-only strain differences were highly significant (see
[[cannabis-cultivar-microbiome-specificity]]), confirming compartment-
specific cultivar effects.

## Experiment 2: Two Cultivars, Two Soil Types

The second experiment grew White Widow and Maui Wowie across two distinct
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
important as soil chemistry for community structure.

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

- Bulk soil vs rhizosphere: Pearson's rho = 0.92
- Rhizosphere vs endorhiza: Pearson's rho = 0.63
- Bulk soil vs endorhiza: Pearson's rho = 0.42

The high soil-rhizosphere correlation (0.92) indicates minimal community
restructuring at the rhizosphere, while the sharp drop to 0.63 reflects
strong host filtering during root colonization.

## PCoA Key Findings

Principal coordinate analysis from experiment 2 confirmed the beta-
diversity patterns visually:

- Unweighted PC1 (32.06% variance): Dominated by soil type
- Unweighted PC2 (11.34%): Sample type differentiation
- Weighted PC1 (34.51%): Dominated by strain
- Weighted PC2 (25.41%): Additional sample type structure

The shift from soil-dominated (unweighted) to strain-dominated (weighted)
PC1 encapsulates the core finding: soil determines composition while
cultivar determines abundance structure.

## See Also

- [[rhizosphere-microbiome-selection-model]] for the theoretical framework
- [[cannabis-cultivar-microbiome-specificity]] for cultivar-level effects
- [[soil-edaphic-factors-microbial-communities]] for soil drivers
- [[microbial-alpha-diversity-soil-plant-gradient]] for diversity patterns
- [[otu-differential-abundance-cannabis-microbiome]] for OTU-level analysis
