---
title: Cannabis Rhizosphere Bulk Soil Microbial Comparison
source: understanding-cultivar-specificity-cannabis-microbiome.md
extracted: 2026-05-10
type: concept
tags: [cannabis, microbiome, rhizosphere, bulk-soil, beta-diversity, unifrac, community-structure]
---

# Cannabis Rhizosphere and Bulk Soil Microbial Community Comparison

## Overview

A fundamental question in plant [[cannabis-microbiome-research]] is how microbial
communities change across the root-soil continuum. In cannabis, the transition
from bulk soil through the rhizosphere to the endorhiza reveals a progressive
filtering of microbial diversity, driven by [[cannabinoid-microbiome-correlation-confounded-edaphic-factors]] at the soil level
and host genotype selection at the root tissue level. Beta-diversity analyses
using both weighted and [[weighted-vs-unweighted-unifrac-cannabis-strain-microbiome]] distances demonstrate that rhizosphere
and bulk soil communities are more similar to each other than either is to
the [[cannabinoid-concentration-endorhiza-microbiome-correlation-cannabis]].

## Beta-Diversity Patterns

### Experiment 1: Three Cultivars, Single Soil Type

In the first experiment using Burmese, Bookoo Kush, and Sour Diesel grown in
similar soils with minimal edaphic variation:

- **Endorhiza** samples clustered significantly apart from all other sample
  types using both unweighted (ADONIS: R2 = 0.26, p = 0.001) and weighted
  UniFrac (ADONIS: R2 = 0.59, p = 0.001).
- **Bulk soil** samples also showed significant distinct clustering
  (unweighted ADONIS: R2 = 0.14, p = 0.001; weighted ADONIS: R2 = 0.29,
  p = 0.004).
- **Rhizosphere** samples did NOT cluster significantly from other types
  (unweighted ADONIS: R2 = 0.07, p = 0.07; weighted ADONIS: R2 = 0.09,
  p = 0.10).

This pattern indicates that in a uniform soil, the rhizosphere acts as a
transitional zone between bulk soil and root interior, without developing a
distinct community identity separate from its source soil.

### Experiment 2: Two Cultivars, Two Soil Types

The second experiment with White Widow and Maui Wowie grown in two
significantly different soil types (Mo-Bio and Orange County soils) revealed
stronger differentiation:

- **Endorhiza** remained the most distinct sample type (unweighted ADONIS:
  R2 = 0.10, p = 0.001; weighted ADONIS: R2 = 0.26, p = 0.001).
- **Rhizosphere** now showed significant clustering from other types
  (unweighted ADONIS: R2 = 0.05, p = 0.04; weighted ADONIS: R2 = 0.13,
  p = 0.001).
- **Bulk soil** showed mixed results (weighted ADONIS: R2 = 0.06, p = 0.054),
  suggesting that with greater edaphic variation, the bulk soil community
  becomes less distinct from the transitional rhizosphere.

### Pooled Analysis

When experiments were pooled together, all three factors -- soil type, sample
type, and strain -- showed highly significant effects on [[edaphic-determinants-cannabis-microbiome-community-structure]].
Soil type remained the dominant factor for overall composition (weighted
ADONIS: R2 = 0.323, p = 0.001), while strain had the strongest effect on
OTU abundances within sample types (weighted ADONIS: R2 = 0.301, p = 0.001).

## Distance Comparisons

Pairwise beta-diversity distances between sample types confirmed that
rhizosphere and bulk soil communities are significantly more similar to each
other than either is to the endorhiza:

- Rhizosphere-bulk soil distances were significantly lower than rhizosphere-
  endorhiza distances for both unweighted (t = 24.59, p < 0.001) and
  weighted analyses (t = 211.82, p < 0.001).
- Rhizosphere-bulk soil distances were significantly lower than bulk soil-
  endorhiza distances for both unweighted (t = 25.15, p < 0.001) and
  weighted analyses (t = 211.56, p < 0.001).
- Rhizosphere-endorhiza distances were NOT significantly different from
  bulk soil-endorhiza distances (unweighted: t = 22.10, p = 0.109; weighted:
  t = 22.23, p = 0.078).

This last finding is particularly important: the endorhiza community is
equally distant from both the rhizosphere and bulk soil, suggesting that the
transition from soil environments into root tissue represents a major
ecological boundary with strong selective filtering, regardless of whether
the source community has already been modified by rhizodeposition.

## OTU Sharing Between Compartments

The soil origin of endorhiza microbes was confirmed by analyzing OTU sharing
