---
title: Two-Tier Selection Model
tags: [microbiome, plant-microbe-interaction, rhizosphere, soil-ecology, endophyte, selection]
source: understanding-cultivar-specificity-cannabis-microbiome.md
created: 2026-05-09
---

# Two-Tier Selection Model

## Overview

The two-tier selection model (also called the two-step selection model) describes how
plant root-associated [[cannabis-endorhiza-bacterial-communities]] are assembled through two sequential
filtering stages. First, edaphic (soil) factors determine the composition of the local
soil microbiota, which becomes the source pool for the first community shift into the
nutrient-rich environment of the rhizosphere. Second, migration from the rhizosphere
into plant tissues is governed by plant genotype-dependent selection of the endorhiza
(endophytic) environment. This model was developed through work by Bulgarelli et al.
(2013) and others, and has been validated in Cannabis by Winston et al. (2014).

## Tier 1: Soil-Type Selection

The first tier of selection is driven by soil properties. [[edaphic-factors-cannabis-endorhiza-microbiome-assembly]] — including
soil pH, nitrogen content, salinity, total organic carbon, water content, and soil
texture — are the primary determinants of which bacterial taxa are present in the bulk
soil community. These abiotic factors create the foundational microbial pool from which
all root-associated communities are drawn.

In the Cannabis microbiome study, soil type was overwhelmingly the strongest predictor
of microbial [[core-endorhiza-bacterial-community-composition-cannabis]] across all samples. For [[weighted-vs-unweighted-unifrac-cannabis-strain-microbiome]] analysis
(presence/absence), soil type showed the largest effect on OTU differences, with 657
significant OTUs differing between soil types. Soil type also dominated PC1 in
principal coordinate analysis, explaining 32.06% of variance in the unweighted
analysis of the second experiment.

The relative importance of edaphic factors, ranked by their correlation with community
beta-diversity:

1. **Nitrogen** — strongest effect (weighted r-stat: 0.465; unweighted r-stat: 0.630)
2. **Salinity** — second strongest (weighted: 0.437; unweighted: 0.620)
3. **Total organic carbon** — (weighted: 0.330; unweighted: 0.512)
4. **Water content** — (weighted: 0.281; unweighted: 0.466)
5. **pH** — weakest but still significant (weighted: 0.221; unweighted: 0.292)

A BEST analysis showed that the variance in community data is optimally explained by
three edaphic factors: nitrogen, carbon, and water (rho = 0.632).

## Tier 2: Host Genotype Selection

The second tier of selection occurs when bacteria migrate from the rhizosphere into
the root tissue (endorhiza). At this stage, host genotype — the specific plant
cultivar — becomes the dominant factor shaping community structure. While soil type
determines which taxa are available (presence/absence), the host plant determines
which taxa thrive and at what abundance (community structure).

In the Cannabis study, strain (cultivar) showed a larger effect than sample type for
weighted OTU differences (71 significant OTUs), but notably showed zero significant
unweighted OTU differences between strains. This means that cultivar selection acts
primarily on community abundance rather than composition — the same taxa tend to be
present across cultivars, but their relative abundances differ. This was reflected in
PCoA analysis where strain dominated PC1 (34.51%) in the weighted analysis of the
second experiment.

## Key Predictions of the Model

The two-tier selection model generates several testable predictions about microbial
community patterns across sample types:

### Prediction 1: Taxonomic Shifts

There should be predictable changes in phylum-level abundance from bulk soil through
rhizosphere to endorhiza. Specifically, Acidobacteria should dramatically decrease
and Proteobacteria should increase in the endorhiza. This was confirmed — the most
significant OTU difference between sample types was the decrease in Acidobacteria
(order iii1-15) in endorhiza samples (Bonferroni-corrected ANOVA: p = 1.12e-7).

### Prediction 2: Progressive Decorrelation

OTU abundance correlations should decrease with each transition: bulk soil to
rhizosphere (high correlation), rhizosphere to endorhiza (moderate), and bulk soil
to endorhiza (lowest). This was confirmed — Pearson's rho decreased from 0.92
(bulk soil vs rhizosphere) to 0.63 (rhizosphere vs endorhiza) to 0.42 (bulk soil
vs endorhiza).

### Prediction 3: Soil Origin of Endophytes

[[cannabis-rhizosphere-endorhiza-communities]] should share more OTUs with their own native soil than with a
foreign soil, confirming that endophytes are recruited from the local soil pool. This
was confirmed — White Widow grown in two soils shared significantly more OTUs with
their own soil (mean = 2934) than with the foreign soil (mean = 2162).

### Prediction 4: Alpha Diversity Decline

Alpha diversity should decrease progressively from bulk soil (highest) through
rhizosphere to endorhiza (lowest), reflecting the sequential filtering at each tier.
This was confirmed — chao1 diversity decreased from 4947 (bulk soil) to 4525
(rhizosphere) to 3321 (endorhiza).

## Partial Validation and Open Questions

While many predictions were supported, some aspects of the model were not fully
validated in the Cannabis study. The prediction that rhizosphere and endorhiza
communities should be more similar to each other than either is to bulk soil was
partially supported — rhizosphere-bulk soil distances were significantly lower than
rhizosphere-endorhiza distances, but rhizosphere-endorhiza distances were not
significantly different from bulk soil-endorhiza distances.

Additionally, results from the first experiment (post-harvest sampling) did not show
cultivar effects on the rhizosphere, which the model would predict. This discrepancy
was attributed to root decay processes occurring 8 weeks after harvest, which may
have diminished the rhizosphere signal.

## Implications for Agriculture

The two-tier selection model has practical implications for Cannabis cultivation:
- Soil management directly affects the microbial pool available for root colonization
- Cultivar selection shapes the endorhiza community, potentially influencing plant
  health and metabolite production
- Inoculation strategies should consider both the native soil microbiome and the
  target cultivar's selection preferences
- Future work could develop cultivar-specific [[microbial-inoculants-and-biological-soil-amendments]] optimized for
  plant fitness, disease suppression, or metabolite augmentation

## See Also

- [[cannabis-endorhiza-microbiome]]
- [[cannabis-rhizosphere-bacterial-communities]]
- rhizosphere effect
