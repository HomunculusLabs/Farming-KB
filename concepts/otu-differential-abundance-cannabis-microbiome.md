---
title: OTU Differential Abundance in Cannabis Microbiome
created: 2026-04-28
tags: [microbiome, bioinformatics, cannabis, statistics]
date: 2026-04-28
updated: 2026-04-28
sources:
  - /Users/t3rpz/wiki/raw/papers/understanding-cultivar-specificity-cannabis-microbiome.md
type: concept
---

# OTU Differential Abundance in Cannabis Microbiome

## Overview

Winston et al. (2014) performed differential abundance analysis on
individual OTUs (Operational Taxonomic Units) to identify bacterial taxa
significantly different between soil types, sample compartments, and
Cannabis cultivars. Two complementary approaches were used: unweighted
analysis (G-test for presence/absence) and weighted analysis (ANOVA for
abundance), both with FDR multiple test correction. The results revealed
a striking asymmetry: soil type drives both composition and abundance,
while cultivar affects only abundance.

## Summary of Significant OTUs

The overall pattern of significant OTU differences (Table 2 of the paper)
clearly illustrates the hierarchical importance of factors:

| Factor       | Weighted (ANOVA) | Unweighted (G-test) |
|-------------|------------------|---------------------|
| Soil type   | 690              | 657                 |
| Sample type | 51               | 11                  |
| Strain      | 71               | 0                   |

Soil type produces roughly 10x more significant OTU differences than
either sample type or strain. The complete absence of unweighted strain
differences (zero OTUs) versus 71 weighted differences is the most
important finding: cultivars modulate microbial abundance but do not
determine which taxa can colonize roots.

## Soil Type Effects on OTU Composition

Soil type was the dominant factor at the OTU level, with 690 OTUs showing
significant abundance differences and 657 showing significant
presence/absence differences. This overwhelming soil effect underpins the
first tier of the [[cultivar-cannabis-microbiome-two-tier-selection-model]]: the local soil microbiota serves as the source
pool from which rhizosphere and endorhiza communities are drawn.

The two soil types in the second experiment (Mo-Bio and Orange County)
differed dramatically in edaphic properties including nitrogen (0.26% vs
0.53%), carbon (3.02% vs 20.0%), salinity (5.12 vs 1.73), and water
content (0.113 vs 0.371), explaining the massive OTU differentiation.

## Sample Type Effects: The 51 Discriminating OTUs

Fifty-one OTUs significantly differentiated between endorhiza, rhizosphere,
and bulk soil compartments (weighted ANOVA). Of these, 17 OTUs increased
in abundance within the Cannabis endorhiza relative to the rhizosphere,
and these were predominantly Proteobacteria from the Rhizobiales order.

### Acidobacteria iii1-15: The Strongest Sample Type Signal

The single most significant OTU abundance difference between sample types
was the dramatic decrease in Acidobacteria from the order iii1-15 in
endorhiza samples (Bonferroni-corrected ANOVA: p = 1.12e-7). This
This oligotrophic, acidophilic group dominates bulk soils but is largely
excluded from the nutrient-rich root interior, consistent with the
understanding that Acidobacteria are poor competitors in carbon-rich
environments.

### Enrichment Patterns in the Endorhiza

The 17 OTUs enriched in the endorhiza were primarily fast-growing,
copiotrophic bacteria adapted to the high-carbon root environment:

- Multiple Proteobacteria from Rhizobiales (known root colonizers)
- Members of Pseudomonadales (plant growth-promoting endophytes)
- Members of Burkholderiales and Sphingomonadales
- Actinobacteria (bioactive compound producers)

This pattern supports the general ecological principle that root
environments favor copiotrophic over oligotrophic strategies.

## Strain Effects: 71 Abundance-Only Differences

Seventy-one OTUs showed significant abundance differences between Cannabis
strains (weighted ANOVA), but zero OTUs differed in presence/absence
(unweighted G-test). This fundamental asymmetry reveals that cultivar
genotype acts as a modulator of relative abundance rather than a gatekeeper
of microbial presence.

### Composition of Strain-Differentiating OTUs

The 71 strain-differentiating OTUs were mostly Proteobacteria:

- **Pseudomonadales**: Including Pseudomonas species, core endorhiza
  members whose abundance varies by cultivar
- **Burkholderiales**: Versatile bacteria with diverse metabolic
  capabilities
- **Sphingomonadales**: Including Sphingomonas wittichii, prevalent in
  Maui Wowie
- **Rhizobiales**: Nitrogen-fixing bacteria whose enrichment varies by
  host genotype

Beyond Proteobacteria, Bacteroidetes orders also contributed:

- **Sphingobacteriales**: Root-associated bacteria in several plant systems
- **Flavobacteriales**: Known for polysaccharide degradation

### Key Biomarker OTUs

Two OTUs emerged as particularly important strain-specific biomarkers:

**Methylophilus** (Bookoo Kush marker): Comprising 13% of the Bookoo Kush
endorhiza community, only 0.13% in Burmese, and entirely absent from Sour
Diesel (FDR: p = 0.012). This methylotrophic bacterium likely responds to
differences in root exudate profiles between cultivars.

Sphingomonas wittichii (Maui Wowie marker): Prevalent in Maui Wowie
in experiment 2. This species metabolizes phenazine-1-carboxylic acid and
has been implicated in increased soil survival, suggesting a functional
role in this cultivar's root microbiome.

## OTU Sharing Between Endorhiza and Soil

The soil origin of endorhiza microbes was tested through OTU sharing
analysis. White Widow was grown in two soils, and roots shared
significantly more OTUs with their own soil (n = 45, mean = 2934) than
with the different soil (n = 45, mean = 2162; t = -10.05, p = 1.209e-15),
confirming soil as the primary microbial source pool.

## Implications for the Two-Tier Model

The OTU-level analysis provides quantitative support for the two-tier
selection model at the individual taxon level. The 657 presence/absence
differences driven by soil versus zero for strain demonstrates that tier 1
(soil filtering) determines community membership, while tier 2 (host
selection) fine-tunes relative abundances. The 17 endorhiza-enriched OTUs
represent the conserved core surviving both filtering steps, while the 71
strain-specific shifts reflect genotype-dependent modulation.

## See Also

- [[beta-diversity-root-soil-compartments-cannabis]] for community-level
  patterns
- [[proteobacteria-dominance-cannabis-endorhiza]] for Proteobacteria
  details
- [[rhizosphere-microbiome-selection-model]] for the assembly framework
- [[cannabis-cultivar-microbiome-specificity]] for cultivar effects
