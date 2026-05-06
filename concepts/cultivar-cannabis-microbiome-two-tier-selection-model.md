---
title: "Two-Tier Selection Model for Cannabis Root Microbiome"
created: 2026-04-28
tags: [cannabis-microbiome, rhizosphere, plant-microbe-interactions, soil-ecology, endorhiza]
date: 2026-04-25
updated: 2026-04-25
sources: [raw/papers/understanding-cultivar-specificity-cannabis-microbiome.md]
type: concept
---

# Two-Tier Selection Model for Cannabis Root Microbiome

## Overview

This landmark study by Winston et al. (2014) provides the first description of the
endorhiza, rhizosphere, and bulk soil-associated microbiome of five distinct Cannabis
cultivars. The research supports a two-tier selection model where soil type determines
community composition across sample types while host cultivar determines community
structure within endorhiza samples. For related work, see [[cannabis-microbiome-research]]
and [[cannabis-root-microbiome]] pages.

## Study Design

Two experiments were conducted:

**Experiment 1:** Bulk soil, rhizosphere, and endorhiza samples from nine plants of
three Cannabis strains (Burmese, BooKoo Kush, Sour Diesel) in Vista, California.
Samples taken eight weeks post-harvest. 27 total samples.

**Experiment 2:** Two strains (White Widow, Maui Wowie) grown in two different soil
types with significant edaphic variation. Samples taken two weeks pre-harvest from
organically grown plants in Vista and Orange County, California. 42 total samples.

Total: 69 samples analyzed via Illumina 16S rRNA sequencing of the V4 region.

## The Two-Tier Selection Model

A growing body of research unites rhizosphere and plant tissue colonization under
a two-tier selection model:

### Tier 1: Soil Determination of Community Composition
Edaphic factors determine the structure of the local soil microbiota, which
becomes the source for the first bacterial community shift into the nutrient-rich
rhizosphere environment. Soil type is the main determinant of which microbial
species are present (OTU presence/absence). The [[comparison-soil-food-web-vs-bacterial-vs-fungal-soil]] is the
foundation of this first tier.

### Tier 2: Host Genotype-Dependent Selection
Migration from rhizosphere into plant tissues (endorhiza) is based on plant
genotype-dependent selection. The host cultivar controls community structure
(relative abundance) more than composition. Different strains growing in the same
soil develop distinct endorhiza communities.

## Key Findings

### Soil Type Has Strongest Overall Effect

Soil type had the strongest influence over significant OTU differences, with 690
weighted and 657 unweighted significant OTUs. This confirms that soil is the
primary determinant of microbial community composition across all sample types.

### Strain Affects Abundance, Not Presence

Strain showed a larger effect than sample type for weighted OTU differences (71
significant OTUs) but zero significant unweighted OTU differences between strains.
This means Cannabis cultivar influences which bacteria are abundant in the
endorhiza, but not fundamentally which bacteria are present.

### Edaphic Factor Ranking

For structuring microbial communities, edaphic factors ranked by importance:

**Weighted analysis:** Nitrogen (r=0.465) > Salinity (r=0.437) > Carbon (r=0.330)
> Water content (r=0.281) > pH (r=0.221)

**Unweighted analysis:** Nitrogen (r=0.630) > Salinity (r=0.620) > Carbon (r=0.512)
> Water content (r=0.466) > pH (r=0.292)

BEST analysis showed nitrogen, carbon, and water optimally explain community
variance (rho = 0.632). All factors were significant at p = 0.001.

### Community Shifts from Soil to Root

The two-tier model predicts specific phylum-level changes:
- Dramatic **reduction in Acidobacteria** within the endorhiza
- **Increase in Proteobacteria and Actinobacteria** relative to rhizosphere
- Most significant decrease: Acidobacteria order iii1-15 (p = 1.12e-7)
- Of 17 OTUs increasing in the endorhiza, most were Proteobacteria from
  the Rhizobiales order

### OTU Sharing Between Endorhiza and Soil

White Widow was grown in two different soils, testing whether endorhiza
communities share more OTUs with their own soil than with foreign soil. Results:
- Shared OTUs with own soil: mean = 2934
- Shared OTUs with different soil: mean = 2162
- Difference highly significant (t = -10.05, p = 1.209e-15)

This validates the hypothesis that endophytic microbes are inherited and
selected from surrounding soil.

### Alpha Diversity Patterns

Alpha diversity peaks in bulk soil and declines through transitions to
rhizosphere and endorhiza: bulk soil chao1 (4947-5597) > rhizosphere
(3913-4859) > endorhiza (3321-3325). Despite greater sequencing depth in
Experiment 2, endorhiza diversity was similar between soil types, suggesting
strong cultivar-level filtering regardless of starting soil community.

### Beta Diversity Relationships

Rhizosphere-bulk soil distances were significantly lower than rhizosphere-
endorhiza distances. This provides limited evidence for the first tier but
strong evidence for cultivar-driven endorhiza structuring.

## Cultivar-Specific Endorhiza Communities

### Core Endorhiza Community

All endorhiza samples maintained a core community of: Pseudomonas, Cellvibrio,
Oxalobacteraceae, Xanthomonadaceae, Actinomycetales, and Sphingobacteriales.
With the exception of Cellvibrio, all are well-known endophytic bacteria
primarily within Gammaproteobacteria and Alphaproteobacteria.

### Strain-Specific Differences

- Methylophilus comprised 13% of BooKoo Kush endorhiza, 0.13% of Burmese,
  and was absent in Sour Diesel (FDR: p = 0.012)
- Sphingomonas wittichii was prevalent in Maui Wowie, a species known to
  metabolize phenazine-1-carboxylic acid and increase soil survival
- Most strain differences were in Proteobacteria orders: Pseudomonadales,
  Burkholderiales, Sphingomonadales, and Rhizobiales
- Bacteroidetes (Sphingobacteriales, Flavobacteriales) also contributed

## Root Decay Consideration

Experiment 1 samples were taken 8 weeks post-harvest. The cellulytic bacterium
Cellvibrio was found at 16.9% abundance (vs. 0.095% in pre-harvest Experiment 2),
indicating early root decay. Sampling timing significantly affects microbiome
characterization; post-harvest samples may not represent active growing communities.

## Cannabinoid-Microbiome Correlation

Cannabinoid concentration correlated significantly with endorhiza structure
(r-stat: 0.863, p = 0.001). However, THC was also correlated to soil variables,
making it difficult to disassociate microbiome-cannabinoid associations from
soil chemistry effects. For more on cannabinoid biosynthesis, see [[modern-farm-lab-and-cannabinoid-terpene-biosynthesis]].

## See Also

- [[understanding-cultivar-two-tier-selection-model-cannabis-microbiome]]
