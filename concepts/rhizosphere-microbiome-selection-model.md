---
title: Rhizosphere Microbiome Selection Model
created: 2026-04-28
tags: [microbiome, soil-science, plant-biology]
date: 2026-04-28
updated: 2026-04-28
sources:
  - /Users/t3rpz/wiki/raw/papers/understanding-cultivar-specificity-cannabis-microbiome.md
type: concept
---

# Rhizosphere Microbiome Selection Model

## Overview

The two-tier selection model (also called the two-step selection model) describes
how plant root microbiomes are assembled through a hierarchical filtering process.
The model posits that soil [[soil-edaphic-factors-microbial-communities]] first determine the pool of available
microbes in the rhizosphere, and then host plant genotype selects from that pool
to shape the [[proteobacteria-dominance-cannabis-endorhiza-community]]. This model was proposed based on studies in
Arabidopsis, poplar, and other plant systems (Bulgarelli et al., 2013; Garbeva
et al., 2004; Berg and Smalla, 2009) and has been tested in Cannabis by Winston
et al. (2014).

## Tier 1: Soil Determination of Rhizosphere Communities

Under the first tier of the model, [[cannabinoid-microbiome-correlation-confounded-edaphic-factors]] (soil chemistry and physics)
determine the structure of the local soil microbiota. These soil microbes become
the source community for the first [[core-endorhiza-bacterial-community-composition-cannabis]] shift into the nutrient
rich environment of the rhizosphere. Rhizodeposition, the release of carbon
compounds from plant roots, enriches certain soil bacteria near the root surface.

In the Winston et al. Cannabis study, soil type was the strongest determinant of
[[edaphic-factors-microbial-community-structure]] composition across all samples. In the pooled analysis:

- Soil type: ADONIS R2 = 0.196 (unweighted), R2 = 0.323 (weighted), p = 0.001
- Sample type: ADONIS R2 = 0.086 (unweighted), R2 = 0.229 (weighted), p = 0.001
- Strain: ADONIS R2 = 0.178 (unweighted), R2 = 0.301 (weighted), p = 0.001

Soil type produced 657 significant OTU differences (unweighted), compared to
only 51 for sample type and 0 for strain in presence/absence comparisons.

## Tier 2: Host Genotype Selection of Endorhiza Communities

The second tier involves migration from the rhizosphere into plant tissues,
based on plant genotype dependent selection of the endorhiza environment.
Endorhiza communities tend to be more plant-specific than rhizosphere
communities, shaped by compounds or proteins produced by the host plant.

In Cannabis, strain level differences were observed only in the endorhiza:

- Experiment 1 endorhiza by strain: ADONIS R2 = 0.59 (weighted), p = 0.004
- Experiment 1 endorhiza by strain: ADONIS R2 = 0.39 (unweighted), p = 0.003
- Rhizosphere showed no significant [[weighted-unifrac-strain-clustering-cannabis-endorhiza-community-structure]] in experiment 1

The model predicts that rhizosphere and endorhiza microbiota should be
soil-derived. This was tested by comparing shared OTUs between endorhiza and
their own soil versus a different soil. White Widow grown in two soils shared
significantly more OTUs with its own soil (mean = 2934) than with the other
soil (mean = 2162), t = -10.05, p = 1.209e-15.

## Predicted Phylum-Level Shifts

The two-tier model predicts several broad changes in phylum-level taxon
abundance as microbes shift from bulk soil through rhizosphere to endorhiza:

- **Acidobacteria**: Dramatic reduction within the endosphere. The most
  significant [[cannabis-microbiome-otu-abundance-vs-presence-cannabis-strains]] difference between sample types was the decrease
  in Acidobacteria from order iii1-15 in endorhiza samples (Bonferroni-
  corrected ANOVA: p = 1.12e-7).
- **Proteobacteria**: Increase in abundance within the endorhiza. Of 17 OTUs
  that increased from rhizosphere to endorhiza, most were Proteobacteria,
  including several from the Rhizobiales order.
- **Actinobacteria**: Increase in the endorhiza relative to bulk soil and
  rhizosphere.

## Evidence from the PCoA Analysis

Principal coordinate analysis from the second experiment provided strong visual
support for the model:

1. PC1 (32.06% variance) in [[unifrac-weighted-unweighted-analysis-cannabis-microbiome]] was dominated by soil type,
   confirming soil as the primary determinant of which microbes are present.
2. PC2 (11.34% variance) showed the community shift from bulk soil (negative
   values) through rhizosphere (intermediate) to endorhiza (positive values).
3. PC1 (34.51% variance) in weighted analysis was dominated by strain,
   suggesting that host genotype controls [[edaphic-determinants-cannabis-microbiome-community-structure]] (abundance) more
   than composition.

## Correlation Patterns Across Compartments
