---
title: Two-Tier Selection Model
tags:
  - microbiology
  - rhizosphere
  - plant-microbiome
  - cannabis
  - ecology
  - endophytes
date: 2026-04-28
updated: 2026-04-28
sources:
  - understanding-cultivar-specificity-cannabis-microbiome.md
---

# Two-Tier Selection Model

The Two-Tier Selection Model describes how microbial communities
associated with plant roots are structured through two sequential
filtering processes: first by soil characteristics at the rhizosphere
level, and second by host genotype at the endorhiza (root interior)
level. The model was validated in the context of Cannabis microbiome
research by Winston et al. (2014), providing the first comprehensive
characterization of the endorhiza, rhizosphere, and bulk
soil-associated microbiome of multiple Cannabis cultivars.

## Model Overview

The two-tier selection model posits a hierarchical process of root
colonization driven by two distinct selection pressures:

### Tier 1: Soil-Driven Rhizosphere Selection

Edaphic (soil) factors — including pH, nitrogen, carbon, salinity,
and water content — determine the structure of the local bulk soil
microbiota. These soil communities serve as the source pool for the
first major community shift into the nutrient-rich environment of
the rhizosphere. The rhizosphere is the narrow zone of soil directly
influenced by root secretions and associated soil microorganisms.

In the Cannabis microbiome study, soil type was the overwhelmingly
dominant factor determining community composition. Principal
coordinate analysis (PCoA) showed soil type accounted for 32% of
variance on PC1 in unweighted analysis. All edaphic factors tested
were significantly correlated with community beta-diversity
(p = 0.001).

### Tier 2: Host Genotype-Driven Endorhiza Selection

Following rhizosphere colonization, migration into plant tissues is
governed by host genotype-dependent selection. The endorhiza
experiences a second filtering event driven by plant-specific
compounds, proteins, and immune responses. This results in
endorhiza communities that are significantly more host-specific
than rhizosphere communities.

For Cannabis, strain-level differences were only observed within
endorhiza samples. In weighted UniFrac analysis, Cannabis strain
accounted for 27% of variance in community structure
(ADONIS: R2 = 0.27, p = 0.001), but no significant strain-level
OTU differences were found in unweighted analysis — indicating that
strain affects community abundance rather than presence or absence
of taxa.

## Key Predictions of the Model

The model generates several testable predictions about changes in
microbial community structure across the soil-to-root gradient:

1. **Decrease in Acidobacteria**: Dramatic reduction in Acidobacteria
   within the endosphere relative to rhizosphere and bulk soil. The
   most significant OTU difference was Acidobacteria order iii1-15
   in endorhiza samples (Bonferroni-corrected ANOVA: p = 1.12e-7).

2. **Increase in Proteobacteria and Actinobacteria**: These phyla
   increase in relative abundance from bulk soil through rhizosphere
   to endorhiza. Of 51 significantly differentiating OTUs, 17 that
   increased in the Cannabis endorhiza were predominantly
   Proteobacteria, including several from the Rhizobiales order.

3. **Soil-Derived Endorhiza Communities**: Endorhiza communities
   share more OTUs with their own surrounding soil than with foreign
   soils. White Widow grown in two different soils shared
   significantly more OTUs with their own soil (mean = 2934) than
   with the other soil (mean = 2162; p = 1.209e-15).

4. **Cultivar-Specific Core Communities**: Each cultivar maintains a
   core endorhiza community. The Cannabis core included *Pseudomonas*,
   *Cellvibrio*, *Oxalobacteraceae*, *Xanthomonadaceae*,
   *Actinomycetales*, and *Sphingobacteriales*.

## Evidence from Two Cannabis Experiments

**First Experiment** (Sour Diesel, Bookoo Kush, Burmese): Illumina
16S rRNA V4 sequencing of 27 samples from Vista, California (November
2011). Endorhiza clustered significantly by strain (weighted ADONIS:
R2 = 0.59, p = 0.004). *Methylophilus* comprised 13% of Bookoo Kush
endorhiza, 0.13% in Burmese, absent in Sour Diesel.

**Second Experiment** (White Widow, Maui Wowie, two soil types):
42 samples from Vista and Orange County (August 2012).
*Sphingomonas wittichii* was significantly more prevalent in Maui
Wowie endorhiza — a species known to metabolize phenazine-1-carboxylic
acid and increase soil survival.

## Alpha Diversity Gradient

The study documented a clear gradient in microbial diversity from
bulk soil through rhizosphere to endorhiza:

- **Bulk soil**: Highest alpha diversity (chao1: m = 4947)
- **Rhizosphere**: Slightly reduced (chao1: m = 4525)
- **Endorhiza**: Dramatically reduced (chao1: m = 3321)

This funneling is consistent with sequential niche filtering.
Despite differences between soil types in bulk soil and rhizosphere
diversity, endorhiza alpha diversity converged, supporting
genotype-driven second tier selection.

## Beta Diversity and Community Distances

Rhizosphere and bulk soil microbiomes are more similar to each other
than to endorhiza (unweighted: t = 24.59, p < 0.001; weighted:
t = 211.82, p < 0.001). OTU abundance correlations decreased along
the gradient: bulk soil to rhizosphere (rho: 0.92), rhizosphere to
endorhiza (rho: 0.63), bulk soil to endorhiza (rho: 0.42).

## Root Decay and Cannabinoid Correlation

The first experiment sampled roots eight weeks post-harvest;
*Cellvibrio* abundance was 16.9% versus 0.095% in growing plants,
indicating root decomposition confounded rhizosphere signals.
Cannabinoid concentrations correlated with endorhiza structure
(Mantel: r = 0.863, p = 0.001), but THC also correlated with
edaphic variables. BEST analysis identified nitrogen, carbon, and
water as optimal explanatory factors (rho = 0.632).

## Related Concepts

- [[Cannabis Microbiome]] for the full scope of microbial
  associations with Cannabis
- [[Endorhiza]] for the biology of root-colonizing bacteria
- [[Rhizosphere Ecology]] for broader root-zone microbial dynamics
- [[Edaphic Factors]] for soil properties shaping microbial
  communities
- [[Cultivar Specificity]] for genetic influences on plant-microbe
  interactions

## See Also

- [[decomposition]]
- [[pseudomonas]]
- [[rhizosphere-ecology]]
