---
title: Rhizosphere-Endorhiza Beta-Distance Comparison in cultivar-cannabis-microbiome-two-tier-selection-model
created: 2026-05-08
tags: [microbiology, cannabis, microbiome, beta-diversity, rhizosphere, endorhiza, bulk-soil, community-ecology, unifrac]
date: 2026-05-08
---

# Rhizosphere-Endorhiza Beta-Distance Comparison in Cannabis Microbiome

## Overview

A key finding from the characterization of the Cannabis [[two-tier-selection-model-plant-microbiome]]
(Winston et al., 2014) was the systematic comparison of beta-diversity
distances between three compartments — bulk soil, rhizosphere, and
endorhiza. This comparison reveals how microbial communities shift
along the soil-to-root continuum and tests predictions of the two-tier
[[two-tier-selection-model-plant-microbiome]].

## The Soil-to-Root Continuum

The three compartments represent progressively more intimate plant-microbe
associations:

1. **Bulk soil**: The surrounding soil not directly influenced by roots
2. **Rhizosphere**: Soil adhering to roots, modified by [[mycorrhizal-root-exudates-pathogen-interactions]]
3. **Endorhiza**: Bacteria that have colonized root tissue (endophytes)

Each transition involves selective pressures that reshape the microbial
community. The question is how much change occurs at each step.

## Key Distance Comparison Results

Using both unweighted and weighted UniFrac distances, the study compared
beta-diversity between all pairwise compartment combinations:

### Rhizosphere vs. Bulk Soil: Most Similar
Beta distances between rhizosphere and bulk soil communities were
significantly lower than distances between rhizosphere and endorhiza
communities for both unweighted (t = 24.59, p < 0.001) and weighted
(t = 211.82, p < 0.001) analyses.

This confirms that the rhizosphere represents a relatively modest shift
from the bulk soil community — primarily driven by the enrichment of
organisms that can metabolize root exudates, but retaining most of the
soil's original taxonomic composition.

### Bulk Soil vs. Endorhiza: Most Different
Distances between bulk soil and endorhiza communities were significantly
greater than distances between bulk soil and rhizosphere communities for
both unweighted (t = 25.15, p < 0.001) and weighted (t = 211.56,
p < 0.001) analyses.

The endorhiza community is the most distinct, having undergone the
strongest selective filtering as bacteria must overcome physical root
barriers, plant immune responses, and compete for niche space within
root tissue.

### Rhizosphere vs. Endorhiza: Intermediate
Notably, distances between rhizosphere and endorhiza communities were
not significantly different from distances between bulk soil and
endorhiza communities for either unweighted (t = -2.10, p = 0.109)
or weighted (t = -2.23, p = 0.078) analyses.

This non-significant result is telling: the leap from rhizosphere to
endorhiza is essentially as large as the leap from bulk soil to
endorhiza. The rhizosphere is a transitional zone that does not
substantially pre-select for endorhiza colonization. Rather, the
major filtering step occurs at the root tissue boundary itself.

## Implications for the Two-Tier Model

These distance patterns support a modified understanding of the two-tier
selection model:

- **Tier 1 (Soil → Rhizosphere)**: Moderate community shift driven by
  [[soil-edaphic-factors-microbial-communities]] and root exudation. Community membership is largely
  preserved; abundances shift toward copiotrophic organisms.

- **Tier 2 (Rhizosphere → Endorhiza)**: Dramatic community shift driven
  by plant immune selection and host genotype. This is the step where
  cultivar-specificity emerges most strongly.

The non-significant difference between rhizosphere-to-endorhiza and
bulk-soil-to-endorhiza distances suggests that the rhizosphere does not
serve as a strong pre-filter. Endorhiza colonists are drawn from the
full soil species pool, not preferentially from rhizosphere-enriched
taxa.

## Correlation Analysis Between Compartments

Mean OTU abundances showed a gradient of decreasing correlation as
distance from bulk soil increased:
- Bulk soil ↔ Rhizosphere: Pearson's rho = 0.92
- Rhizosphere ↔ Endorhiza: Pearson's rho = 0.63
- Bulk soil ↔ Endorhiza: Pearson's rho = 0.42

The steep drop from 0.92 to 0.63 between rhizosphere and endorhiza
corroborates the beta-distance findings: the most transformative step in
community assembly occurs at the root tissue boundary.

## Phylum-Level Shifts

The transition from rhizosphere to endorhiza was characterized by:
- **Dramatic reduction** in Acidobacteria (order iii1-15 was the most
  significantly depleted OTU, Bonferroni-corrected ANOVA: p = 1.12e-7)
- **Increase** in Proteobacteria (especially Rhizobiales)
- **Increase** in Actinomycetales

Acidobacteria are typically oligotrophic soil bacteria adapted to low-
nutrient conditions. Their exclusion from the endorhiza reflects the
shift from a nutrient-poor soil environment to the relatively carbon-rich
root interior.

## Agricultural Implications

For [[query-how-does-no-till-cannabis-cultivation-work]], these findings suggest that:
- Soil management primarily affects the rhizosphere and indirectly
  influences endorhiza composition through the available species pool
- Direct endorhiza manipulation (e.g., through inoculants) would need
  to overcome the strong selection at the root tissue boundary
- The rhizosphere is not a reliable predictor of endorhiza composition

## See Also

- [[two-tier-selection-model-plant-microbiome]]
- [[cannabis-endorhiza-microbiome]]
- [[acidobacteria-decline-rhizosphere-endorhiza-transition]]
- [[alpha-beta-diversity-cannabis-root-microbiomes]]
- [[cannabis-root-microbiome]]

## Source

- Winston ME, Hampton-Marcell J, Zarraonaindia I, et al. Understanding
  Cultivar-Specificity and Soil Determinants of the Cannabis Microbiome.
  *PLoS ONE* 9(6): e99641, 2014.
