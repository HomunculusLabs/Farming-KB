---
title: "OTU Abundance vs Presence-Absence in cultivar-cannabis-microbiome-two-tier-selection-model Structuring"
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

The two-tier selection model posits that bulk soil microbial communities are
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
with zero in the unweighted analysis, demonstrates that [[cannabis-cultivar-effects-soil-microbiome]] are
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
- **Sphingomonadales**: Notably *Sphingomonas wittichii*, which was prevalent
  in [[sour-diesel]] endorhiza

This difference was statistically significant even after FDR correction
(p = 0.012), making Methylophilus a potential biomarker for strain-specific
endorhiza community profiling.

## Soil Type Dominance in OTU Presence/Absence

The 657 OTUs differing between soil types (unweighted) vastly outnumbered all
other factors combined. Edaphic variables measured included:

- **Nitrogen content** (strongest correlate, r = 0.630 unweighted)
- **Salinity** (r = 0.620 unweighted)
- **Total organic carbon** (r = 0.512 unweighted)
- **Water content** (r = 0.466 unweighted)
- **pH** (r = 0.292 unweighted)

A BEST analysis found that the optimal combination of Nitrogen, Carbon, and
Water content explained community variance with rho = 0.632.

## Implications for Agricultural Practice

### Bioinoculant Development

Since cultivar selects mainly from the available soil pool, the composition of
the growing medium is the primary lever for introducing beneficial microbes.
Strain-specific enrichment can then be achieved by ensuring the right taxa are
present in the soil, knowing the plant will adjust their relative abundances.

### Soil Selection for Cultivation

The dramatic dominance of soil type in determining microbial composition
suggests that matching soil properties to desired microbial profiles is more
important than [[blesching-cannabis-strain-selection-receptor-targeting]] for establishing beneficial microbiomes.

### Synthetic Communities (SynComs)

The finding that cultivars share most of their endorhiza OTUs (differing only
in abundance) means that a single synthetic [[edaphic-factors-microbial-community-structure]] could serve
multiple cultivars, with the plant naturally adjusting population ratios.

## Limitations and Considerations

- The study analyzed only [[cultivar-endorhiza-bacterial-communities-cannabis]] via 16S rRNA; fungal and
  archaeal communities may show different patterns
- Sample sizes were relatively small (6-9 plants per experiment)
- The first experiment sampled post-harvest, potentially confounding results
  with root decay dynamics
- Pseudoreplication within plants may have inflated strain effect estimates
## See Also

- [[cannabis-root-bound-symptoms-and-management]]
- [[blesching-cannabis-fever-temperature-regulation]]
- [[query-how-to-identify-and-treat-bud-rot-on-cannabis]]
