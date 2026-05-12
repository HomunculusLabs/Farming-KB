---
title: Cannabis Microbiome Otu Abundance Vs Presence Cannabis Strains
source: "understanding-cultivar-specificity-cannabis-microbiome.md"
tags: [cannabis, microbiome, otu, strain-specificity, soil-type, alpha-diversity, rhizosphere]
created: 2026-05-08
---

# OTU Abundance vs Presence-Absence in Cannabis Microbiome Structuring

## Overview

A critical finding from the Winston et al. (2014) study of Cannabis microbiomes
is that plant strain (cultivar) and soil type exert their influence through
fundamentally different mechanisms. Soil type primarily determines which
microbial taxa are *present or absent* ([[core-endorhiza-bacterial-community-composition-cannabis]]), while Cannabis
cultivar primarily shapes the *relative abundances* of those taxa within the
endorhiza. This distinction has important implications for understanding how
plant-microbe partnerships form and how they might be manipulated in
agricultural practice.

## The Two-Tier Selection Model Context

The two-tier selection model posits that bulk soil [[cannabis-rhizosphere-microbial-communities]] are
first filtered by rhizodeposition into the rhizosphere, and then further
selected by host genotype-dependent mechanisms as bacteria colonize root
tissues (the endorhiza). The study's results partially support this model but
reveal that the second tier operates mainly through abundance modulation rather
than presence/absence filtering.

## Evidence from Unweighted vs Weighted Analyses

### Unweighted UniFrac (Presence/Absence)

When analyzing community differences using unweighted UniFrac distances, which
emphasize taxonomic presence or absence regardless of abundance:

- **Soil type** produced **657** significant OTU differences
- **Sample type** (bulk soil, rhizosphere, endorhiza) produced **11**
  significant OTU differences
- **Strain** (cultivar) produced **0** significant OTU differences

This is a striking result: despite growing five different Cannabis cultivars,
no individual bacterial taxon was significantly present in one strain and
absent from another when only presence/absence was considered.

### Weighted UniFrac (Abundance-Weighted)

When abundance was factored in using weighted UniFrac distances and ANOVA:

- **Soil type** produced **690** significant OTU differences
- **Sample type** produced **51** significant OTU differences
- **Strain** produced **71** significant OTU differences

The appearance of 71 strain-dependent OTUs in the weighted analysis, contrasted
with zero in the [[unifrac-weighted-unweighted-analysis-cannabis-microbiome]], demonstrates that [[cannabis-cultivar-effects-soil-microbiome]] are
almost entirely mediated through changes in relative abundance of shared taxa,
not through selective inclusion or exclusion of specific bacteria.

## PCoA Axis Interpretation

The principal coordinate analysis (PCoA) of the second experiment reinforces
this interpretation:

- In the **unweighted analysis**, PC1 (32.06% variance) was dominated by soil
  type variation, confirming soil as the primary determinant of microbial
  presence/absence patterns.
- In the **weighted analysis**, PC1 (34.51% variance) was dominated by strain
  variation, showing that once bacteria are present, cultivar genotype drives
  their relative abundances.

## Taxonomic Composition of Strain-Specific Differences

The 71 OTUs showing significant abundance differences between strains were
predominantly **Proteobacteria**, spanning several key orders:

- **Pseudomonadales**: Well-known plant growth-promoting rhizobacteria
- **Burkholderiales**: Includes species with biocontrol and nitrogen-fixing
  capabilities
- **Sphingomonadales**: Notably *[[sphingomonas-wittichii-cannabis-endorhiza-strain-specificity]]*, which was prevalent
  in [[sour-diesel]] endorhiza

This difference was statistically significant even after FDR correction
(p = 0.012), making Methylophilus a potential biomarker for strain-specific
endorhiza [[fungal-community-profiling-rock-mineral-surfaces-gadd]].

## Soil Type Dominance in OTU Presence/Absence

The 657 OTUs differing between soil types (unweighted) vastly outnumbered all
other factors combined. Edaphic variables measured included:

## Practical Applications

The principles and techniques discussed here have wide-ranging applications
across multiple disciplines and contexts. Practitioners and researchers
continue to explore new ways to integrate these concepts into modern practice,
adapting traditional knowledge to contemporary challenges and opportunities.

## Key Considerations

Several important factors influence the effectiveness and outcomes described
in this topic. Understanding these considerations helps practitioners make
informed decisions and avoid common pitfalls. Environmental conditions,
timing, and material selection all play critical roles.

## Historical Context

The historical development of this subject reflects centuries of accumulated
knowledge and practical experience. From traditional methods passed down
through generations to modern scientific approaches, the evolution continues
to inform current best practices and research directions.

## Common Challenges

Practitioners frequently encounter several challenges when working with
these concepts. Climate variability, resource limitations, and knowledge
gaps can all affect outcomes. Addressing these challenges requires patience,
observation, and a willingness to adapt approaches based on results.

## See Also
- [[strain-otu-presence-absence-vs-abundance-cannabis-microbiome]]
- [[otu-abundance-vs-presence-absence-cannabis-strain-microbiome]]
- [[dom]]
- [[det]]
- [[otu-differential-abundance-cannabis-microbiome]]
