---
title: Two-Tier Selection Model Plant Microbiome
created: 2026-05-09
tags: [microbiome, plant-microbe-interactions, rhizosphere, endorhiza, soil-ecology]
date: 2026-05-09
aliases: [Two Tier Selection Model, Root [[cannabis-two-tier-microbiome-selection]], Edaphic Plant Microbiome]
---

# Two-Tier Selection Model of the Plant Microbiome

The two-tier selection model describes how microbial communities associated with plant
roots are assembled through two sequential filtering processes. First, soil edaphic
properties determine which microorganisms are available to colonize the rhizosphere.
Second, the plant's genotype selectively filters which of those rhizosphere microbes
are permitted to colonize internal root tissues (the endorhiza). This model was
formalized through studies of the Cannabis microbiome by Winston et al. (2014) and
builds on earlier work by Bulgarelli et al. (2013) and Lundberg et al. (2012).

## The Model: Two Sequential Filters

### Tier 1: Soil Determines the Available Pool

Edaphic (soil) factors act as the primary filter on microbial [[core-endorhiza-bacterial-community-composition-cannabis]].
The local soil environment — including pH, nitrogen content, salinity, carbon content,
water content, and texture — selects for a characteristic microbial community. This
soil-derived community serves as the source pool from which root-associated microbes
are recruited. The key predictions of this tier:

- Bulk soil and rhizosphere communities should be more similar to each other than
  to [[cannabis-rhizosphere-endorhiza-communities]]
- Microbial composition should differ significantly between soil types, regardless
  of the plant species or cultivar growing in them
- [[edaphic-factors-cannabis-endorhiza-microbiome-assembly]] should be the strongest predictor of community-level differences

Evidence from the Cannabis microbiome study strongly supports these predictions:
soil type explained the largest portion of OTU (operational taxonomic unit) variation,
with 690 significant OTUs differing between soil types compared to only 51 between
sample types and 71 between cultivar strains.

### Tier 2: Plant Genotype Selects the Endorhiza

Once the soil has defined the available microbial pool, the plant exerts a second,
genotype-dependent filter on which microbes colonize internal root tissues. The
endorhiza (root interior) community is shaped by:

- Root exudate composition, which varies by plant species and cultivar
- Root immune responses that selectively permit or exclude specific microbial taxa
- Physical and chemical barriers at the root-soil interface

Key predictions of this tier:

- Endorhiza communities should show cultivar-specific differences even when the
  same soil type is used
- Endorhiza communities should share more OTUs with their own soil than with a
  different soil in which the same cultivar is grown
- [[edaphic-determinants-cannabis-microbiome-community-structure]] (relative abundances) within the endorhiza should be driven
  primarily by cultivar identity rather than soil type

The Cannabis study confirmed that endorhiza communities showed significant cultivar
specificity (ADONIS R² = 0.59, p = 0.004 for weighted UniFrac) and that White Widow
plants shared significantly more OTUs with their own soil than with the soil used for
other White Widow plants (mean 2934 vs 2162 shared OTUs).

## Predicted Phylum-Level Shifts

The two-tier model predicts specific changes in taxonomic composition as microbes
transition from soil to rhizosphere to endorhiza:

| Transition | Acidobacteria | Proteobacteria | Actinobacteria |
|---|---|---|---|
| Bulk soil → Rhizosphere | Slight decrease | Slight increase | Stable |
| Rhizosphere → Endorhiza | Dramatic decrease | Dramatic increase | Increase |

The dramatic reduction in Acidobacteria within the endorhiza is a hallmark prediction
of the model. Acidobacteria are typically oligotrophic soil bacteria adapted to low-
nutrient conditions. The nutrient-rich environment of the rhizosphere and endorhiza
favors copiotrophic Proteobacteria and Actinobacteria instead.

In the Cannabis study, the most significant OTU difference between sample types was
the decrease in Acidobacteria from the order iii1-15 in endorhiza samples
(Bonferroni-corrected ANOVA: p = 1.12e-7). Of the 51 OTUs that significantly increased
in the endorhiza, 17 were predominantly Proteobacteria, including several from the
Rhizobiales order — well-known plant-associated endophytes.

## OTU Presence vs. Abundance

An important distinction emerged from the data: while soil type strongly influenced
both OTU presence/absence (unweighted analysis: 657 significant OTUs) and OTU
abundance (weighted analysis: 690 significant OTUs), cultivar strain only affected
abundance patterns (71 significant weighted OTUs, 0 significant unweighted OTUs).

This means that cultivar selection acts primarily on the relative proportions of
microbes that successfully colonize the endorhiza, rather than determining which taxa
are present or absent. The cultivar "tunes" the community composition from within
the soil-defined pool rather than imposing an entirely different membership.

## Edaphic Factor Ranking

The Cannabis study identified a clear hierarchy of edaphic factors influencing
microbial community structure, consistent across both weighted and unweighted analyses:

1. **Nitrogen** — strongest predictor (weighted r = 0.465, unweighted r = 0.630)
2. **Salinity** — second strongest (weighted r = 0.437, unweighted r = 0.620)
3. **Total organic carbon** — third (weighted r = 0.330, unweighted r = 0.512)
4. **Water content** — fourth (weighted r = 0.281, unweighted r = 0.466)
5. **pH** — fifth (weighted r = 0.221, unweighted r = 0.292)

All factors were highly significant (p = 0.001). Nitrogen content's dominance
is consistent with its role as the primary limiting nutrient for microbial growth
in most soil environments.

## Implications for Agriculture

The two-tier selection model has practical implications for managing plant-microbiome
interactions in cultivation:

1. **Soil management is foundational:** Because soil type is the primary determinant
   of the available microbial pool, soil amendments, composting, and crop rotation
   have the largest impact on the root-associated microbiome
2. **Breeding for microbiome traits is possible:** Since cultivar identity shapes
   [[proteobacteria-dominance-cannabis-endorhiza-community]] structure, breeding programs could select for cultivars that
   recruit beneficial microbial assemblages
3. **Inoculant success depends on soil compatibility:** Probiotic soil inoculants
   must be compatible with the existing soil microbial community, which serves as
   the primary filter for root colonization
4. **Terroir effects are real:** The combination of soil-defined microbial pools and
   cultivar-specific selection creates unique, location-dependent microbiome profiles
   that may influence crop quality — analogous to terroir effects in viticulture

## Limitations

- The model is primarily supported by bacterial 16S rRNA studies; fungal community
  assembly may follow different rules
- The relative strength of each tier may vary across plant species and growth stages
- Temporal dynamics (seasonal changes, plant developmental stage) are not captured
- The model does not fully account for host immune system complexity

## See Also

- [[cannabis-endorhiza-microbiome]]
- [[cannabis-rhizosphere-microbial-communities]]
- [[edaphic-factors-microbial-community-structure]]
