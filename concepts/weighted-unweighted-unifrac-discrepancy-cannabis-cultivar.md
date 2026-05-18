---
title: "Weighted Unweighted Unifrac Discrepancy Cannabis Cultivar"
created: 2026-05-11
tags: [cannabis, microbiome, unifrac, beta-diversity, cultivar-specificity, community-structure, weighted-analysis, unweighted-analysis]
source: raw/papers/understanding-cultivar-specificity-cannabis-microbiome.md
---

# Weighted vs Unweighted UniFrac Discrepancy in Cannabis Cultivar Studies

## Overview

The Winston et al. (2014) [[cannabis-rhizosphere-microbial-communities]].
Specifically, **strain-level differentiation was detectable only with
weighted UniFrac** when examining OTU presence/absence patterns, while
[[sphingomonas-wittichii-cannabis-endorhiza-strain-specificity]] characterizes Maui Wowie.

## The PC1 Axis Flip

Perhaps the most dramatic illustration of this discrepancy appears
in the principal coordinate analysis of the second experiment:

- **Unweighted PC1 (32.06% variance)**: Dominated by soil type,
  not strain. Communities cluster primarily by which soil they
  came from, with strain effects secondary.

- **Weighted PC1 (34.51% variance)**: Dominated by strain,
  not soil type. Communities cluster primarily by cultivar,
  with soil effects pushed to secondary axes.

This axis flip demonstrates that the most powerful structuring
force depends entirely on whether you measure who is there
(unweighted) or how much of each is there (weighted). Soil
determines composition; genotype determines abundance.

## The Rhizosphere as Intermediate Zone

The rhizosphere showed an interesting intermediate pattern. In
Experiment 2, rhizosphere communities were significantly
different between strains using weighted UniFrac (ADONIS
R² = 0.13, p = 0.001) but showed only marginal significance
with unweighted (R² = 0.05, p = 0.04). This positions the
rhizosphere between bulk soil (soil-dominated) and endorhiza
(genotype-dominated) in terms of how cultivar effects manifest.

In Experiment 1 (post-harvest), rhizosphere strain effects
were absent entirely, consistent with the cessation of root
exudation eliminating the genotype-mediated selection pressure
that shapes abundance patterns in living root zones.

## Implications for Microbiome Research Design

### Choose Metrics Based on Question

Researchers studying host genotype effects should prioritize
weighted distance metrics, as cultivar effects manifest primarily
through abundance modulation rather than species sorting. Studies
using only unweighted analyses may falsely conclude that host
genotype has no effect on the microbiome.

### Sample Depth Matters

Weighted analyses require deeper sequencing to accurately estimate
relative abundances. The second experiment's deeper sequencing
(45,000 sequences per sample vs 3,000 in Experiment 1) provided
the statistical power needed to detect the 71 significant strain
OTUs. Shallow sequencing may miss abundance-driven effects.

### Multiple Testing Correction is Conservative

The zero significant unweighted OTUs between strains reflects the
stringency of FDR correction across hundreds of OTUs. While no
single OTU reaches significance, the aggregate phylogenetic signal
(strain clustering in PCoA) remains strong, suggesting that
multivariate approaches capture signals lost in per-OTU testing.

## See Also

- [[edaphic-factors-structuring-cannabis-microbiome]] — Soil effects
- [[beta-diversity-distances-bulk-soil-rhizosphere-cannabis-endorhiza]]
- cannabis endorhiza strain specificity post harvest persistence
## Benefits and Limitations

Weighted Unweighted Unifrac Discrepancy Cannabis Cultivar offers several advantages in practice, including adaptability to
different conditions and compatibility with related approaches. However,
limitations exist depending on context, scale, and available resources.
Understanding both helps practitioners set realistic expectations and plan
appropriate strategies for implementation.

## Related Methods and Approaches

Several complementary approaches exist alongside weighted unweighted unifrac discrepancy cannabis cultivar, each
offering unique advantages for specific situations. Comparative evaluation
of these methods helps identify the most suitable option given available
resources, environmental constraints, and desired outcomes. Combining
multiple approaches often yields synergistic benefits.
