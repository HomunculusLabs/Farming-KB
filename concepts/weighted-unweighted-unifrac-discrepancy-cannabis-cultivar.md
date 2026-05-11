---
title: "Weighted Unweighted Unifrac Discrepancy Cannabis Cultivar"
created: 2026-05-11
tags: [cannabis, microbiome, unifrac, beta-diversity, cultivar-specificity, community-structure, weighted-analysis, unweighted-analysis]
source: raw/papers/understanding-cultivar-specificity-cannabis-microbiome.md
---

# Weighted vs Unweighted UniFrac Discrepancy in Cannabis Cultivar Studies

## Overview

The Winston et al. (2014) [[winston-cannabis-microbiome-study-design]] revealed a
striking discrepancy between weighted and unweighted UniFrac distance
metrics when assessing cultivar effects on [[cannabis-rhizosphere-microbial-communities]].
Specifically, **strain-level differentiation was detectable only with
weighted UniFrac** when examining OTU presence/absence patterns, while
[[unifrac-weighted-unweighted-analysis-cannabis-microbiome]] found zero significant OTU differences between
strains. This finding has important implications for how microbiome
studies should be designed and analyzed when investigating host
genotype effects.

## Understanding the Two Metrics

**Unweighted UniFrac** measures community similarity based solely on
the phylogenetic distances of OTUs that are present or absent
(qualitative composition). It treats all observed lineages equally
regardless of their abundance, making it sensitive to rare taxa
and compositional shifts.

**Weighted UniFrac** incorporates both phylogenetic distance and
relative abundance of each lineage (quantitative composition). It
is more sensitive to changes in dominant taxa and community
structure even when the overall species pool remains similar.

## The Strain Effect Discrepancy

In the second experiment (White Widow vs Maui Wowie, two soil
types), the analysis produced a clear pattern:

### Unweighted Analysis (Composition)

- Soil type: 657 significant OTUs (p < 0.05, FDR-corrected)
- Sample type (endorhiza/rhizosphere/bulk): 11 significant OTUs
- Strain: **0 significant OTUs**

Despite finding zero strain-specific OTUs, unweighted UniFrac
beta-diversity still showed significant strain clustering in
endorhiza (ADONIS R² = 0.10, p = 0.001) and all samples pooled
(ADONIS R² = 0.178, p = 0.001). This paradox occurs because
unweighted UniFrac captures phylogenetic shifts even when
individual OTUs don't reach significance after multiple-testing
correction.

### Weighted Analysis (Abundance)

- Soil type: 690 significant OTUs
- Sample type: 51 significant OTUs
- Strain: **71 significant OTUs**

Weighted UniFrac beta-diversity showed much stronger strain
effects: endorhiza (ADONIS R² = 0.26, p = 0.001), rhizosphere
(R² = 0.13, p = 0.001), and pooled samples (R² = 0.301, p = 0.001).

## Interpreting the Discrepancy

The absence of significant unweighted OTU differences between
strains means that Cannabis cultivars share essentially the same
species pool of root-associated bacteria. The 71 significant
weighted OTU differences indicate that cultivars differ in the
relative abundances of these shared taxa, not in which taxa are
present.

This is consistent with the two-tier selection model:

1. Soil type determines which bacteria are available (composition)
2. Host genotype fine-tunes their relative abundances (structure)

The same Proteobacterial orders appear across all cultivars —
Pseudomonadales, Burkholderiales, Sphingomonadales, Rhizobiales —
but their proportional representation shifts based on the host
strain. Methylophilus dominates Bookoo Kush but is absent from
Sour Diesel, while [[sphingomonas-wittichii-cannabis-endorhiza-strain-specificity]] characterizes Maui Wowie.

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

- [[cannabis-microbiome-two-tier-selection]] — Selection model
- [[edaphic-factors-structuring-cannabis-microbiome]] — Soil effects
- [[beta-diversity-distances-bulk-soil-rhizosphere-cannabis-endorhiza]]
- cannabis endorhiza strain specificity post harvest persistence
