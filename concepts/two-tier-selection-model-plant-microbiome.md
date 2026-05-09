---
title: Two-Tier Selection Model for Plant Microbiome Assembly
slug: two-tier-selection-model-plant-microbiome
source: understanding-cultivar-specificity-cannabis-microbiome.md
tags: [microbiome, rhizosphere, endorhiza, plant-microbe-interactions, soil-ecology]
created: 2026-05-08
---

# Two-Tier Selection Model for Plant Microbiome Assembly

## Overview

The two-tier selection model describes how microbial communities
associated with plant roots are assembled through two sequential
filtering steps. Community composition across sample types is
determined mainly by soil type (Tier 1), while community structure
within endorhiza samples is determined mainly by host cultivar
(Tier 2). The model was notably validated in Cannabis spp. by
Winston et al. (2014).

## Tier 1: Soil-to-Rhizosphere Selection

The first tier is driven by edaphic (soil) factors. The bulk soil
microbial community serves as the reservoir from which rhizosphere
colonizers are drawn. Key soil properties driving this filter:

- **Soil pH**: One of the strongest predictors of community
  composition. In the Cannabis study, soils ranged from pH 6.63
  to 6.94 (slightly acidic range).
- **Nitrogen content**: The single strongest edaphic factor
  (Mantel r-stat: 0.465 for weighted UniFrac).
- **Salinity**: Significant influence on community structure
  (r-stat: 0.437). Study soils ranged from 1.73 to 7.44.
- **Total organic carbon**: Carbon shapes the metabolic landscape
  (r-stat: 0.330). Soils ranged from 3.02% to 20.0% TOC.
- **Water content**: Affects O2 availability, nutrient diffusion,
  and microbial mobility (r-stat: 0.281).
- **Soil texture**: Sand (62-66%), silt (16-18%), clay (17-21%);
  all classified as sandy loam.

When all Cannabis experiment samples were pooled, soil type
accounted for R² = 0.196 (unweighted) and R² = 0.323 (weighted)
of community variation. Soil type also produced 690 weighted and
657 unweighted significant OTU differences — far exceeding sample
type (51/11) and strain (71/0).

## Tier 2: Rhizosphere-to-Endorhiza Selection

The second tier is driven by host genotype (cultivar). Once microbes
pass through the edaphic filter into the nutrient-rich rhizosphere,
the plant exerts selection on which taxa colonize internal root
tissues (endorhiza) through several mechanisms:

- **Root exudates**: Genotype-dependent mixtures of sugars, amino
  acids, organic acids, phenolics, and secondary metabolites
  selectively promote or inhibit specific microbial taxa.
- **Root cell wall composition**: Structural properties (pectin,
  cellulose, lignin ratios) influence bacterial attachment and
  penetration efficiency.
- **Immune responses**: Pattern recognition receptors detect MAMPs,
  permitting commensals while restricting pathogens.
- **Secondary metabolites**: Cannabis cannabinoids and terpenes may
  shape endorhiza communities. Cannabinoid concentration correlated
  with endorhiza structure (Mantel r-stat: 0.863, p = 0.001),
  though confounded by soil-cannabinoid correlations.

## Evidence from Cannabis Microbiome Experiments

### Experiment 1 (Minimal Edaphic Variation)

Three cultivars (Burmese, BooKoo Kush, Sour Diesel) were grown in
similar soils in Vista, CA. Endorhiza showed significant cultivar-
specificity: weighted UniFrac ADONIS R² = 0.59, p = 0.004;
unweighted R² = 0.39, p = 0.003. Rhizosphere and bulk soil did
not differ significantly by strain.

The genus Methylophilus explained significant cultivar-level
differentiation (FDR: p = 0.012), comprising 13% of the Bookoo
Kush endorhiza community, 0.13% in Burmese, and was absent from
Sour Diesel entirely.

### Experiment 2 (Significant Edaphic Variation)

Two cultivars (White Widow, Maui Wowie) in two distinct soils
(Vista vs Orange County, CA) with substantial differences in
organic carbon (3.02% vs 20.0%), salinity (5.12 vs 1.73), and
nitrogen content.

Both soil type (R² = 0.21, p = 0.001) and strain (R² = 0.27,
p = 0.001) significantly structured endorhiza communities,
confirming both tiers operate simultaneously and additively.

### Shared OTU Analysis

The model predicts endorhiza share more OTUs with their own soil
than with a different soil. White Widow grown in two soils confirmed
this: endorhiza shared more OTUs with their own soil (mean = 2934)
than the alternative (mean = 2162; t = 210.05, p = 1.209e-15).

## Predicted Taxonomic Shifts

Transitioning from bulk soil through rhizosphere to endorhiza:

- **Acidobacteria**: Dramatically reduced in endorhiza. Order iii1-15
  showed the largest decrease (Bonferroni ANOVA: p = 1.12e-7).
  Adapted to oligotrophic conditions, they decline in the
  carbon-rich root environment.
- **Proteobacteria**: Enriched in endorhiza. Orders Rhizobiales,
  Pseudomonadales, Burkholderiales, and Sphingomonadales showed
  significant inter-strain abundance differences.
- **Actinobacteria**: Increased in endorhiza relative to bulk soil,
  consistent with known endophytic roles.
- **Bacteroidetes**: Sphingobacteriales and Flavobacteriales
  contributed to strain-level differences, suggesting sensitivity
  to host genotype cues.

## Alpha Diversity Gradient

Diversity peaks in bulk soil, decreases slightly in rhizosphere,
and collapses in endorhiza. Chao1 estimates: bulk soil (m = 4947,
s = 717), rhizosphere (m = 4525, s = 542), endorhiza (m = 3321,
s = 420). The rhizosphere-to-endorhiza transition shows the
steepest diversity loss, reflecting the combined selective pressure
of both tiers.

## Agricultural Implications

- **Soil management**: Amendments, composting, and rotation shape
  the microbial pool from which beneficial colonizers are drawn.
- **Cultivar selection**: Breeding could target genotypes that
  promote beneficial partnerships for nutrient uptake and disease
  resistance.
- **Inoculant design**: Products must be compatible with both the
  soil environment (Tier 1) and host selective pressures (Tier 2)
  to establish persistent endorhiza populations.

## See Also

- [[soil-edaphic-factors-microbial-communities]]
- [[cannabinoid-concentration-endorhiza-microbiome-correlation-cannabis]]

## See Also

- [[cultivar-cannabis-microbiome-two-tier-selection-model]]
