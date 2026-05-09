---
title: "Post-Harvest vs Pre-Harvest Sampling Effects on Cannabis Endorhiza Microbiome Characterization"
source: understanding-cultivar-specificity-cannabis-microbiome.md
topics: [microbiome, cannabis, sampling-methodology, root-decay, endorhiza, experimental-design, cellvibrio]
created: 2026-05-09
---

# Post-Harvest vs Pre-Harvest Sampling Effects on Cannabis Endorhiza Microbiome Characterization

## Overview

The Winston et al. (2014) Cannabis microbiome study inadvertently demonstrated that the timing of root sampling — specifically whether samples are collected before or after harvest — can dramatically alter the observed microbial community composition of the endorhiza. The study's two experiments used different sampling protocols: the first experiment sampled roots eight weeks post-harvest, while the second sampled two weeks before harvest. The resulting differences between experiments provide important methodological insights for anyone studying or managing plant-associated microbial communities.

This comparison is valuable because few plant microbiome studies have directly examined how post-mortem tissue decomposition affects endophyte community profiles. The findings have implications for archaeological and paleomicrobiological studies as well as for modern agricultural research where post-harvest root sampling may be logistically convenient but scientifically problematic.

## The Two Experiments

### Experiment 1: Post-Harvest Sampling

- Three cultivars: Burmese, Bookoo Kush, Sour Diesel
- Nine plants total, sampled from Vista, California in November 2011
- Root samples collected eight weeks after bud and foliage harvest
- Bulk soil sampled at 10 cm from stem, 20 cm depth
- 27 total samples (endorhiza, rhizosphere, bulk soil per plant)
- DNA extracted using MO BIO PowerSoil kit with 65°C heating modification
- Sequenced on Illumina MiSeq, rarified to 3,000 sequences per sample
- Minimal edaphic variation between the three bulk soil samples

### Experiment 2: Pre-Harvest Sampling

- Two cultivars: White Widow, Maui Wowie
- Six plants total, from two locations (Vista and Orange County, CA)
- Root samples collected two weeks before harvest (actively flowering plants)
- 42 total samples (triplicate endorhiza, rhizosphere, and bulk soil per plant)
- Sequenced on Illumina MiSeq, rarified to 45,000 sequences per sample
- Cannabinoid data also collected from buds
- Significant edaphic variation between the two soil types

## Cellvibrio: The Decay Signal

The most striking difference between the two experiments was the relative abundance of the aerobic cellulolytic bacterium *Cellvibrio* within the endorhiza. This genus, known for its ability to degrade plant cell wall cellulose, was present at dramatically different levels:

| Sample Type | Experiment 1 (Post-Harvest) | Experiment 2 (Pre-Harvest) |
|-------------|---------------------------|---------------------------|
| Cellvibrio mean abundance | 16.9% (SD = 13.0%) | 0.095% (SD = 2.7%) |
| Sample size (N) | 9 | 18 |

This 178-fold difference strongly suggests that *Cellvibrio* was not a member of the living endorhiza community but rather a colonizer of decaying root tissue. In the post-harvest samples, senescing and decomposing root tissue provided abundant cellulose substrate, allowing *Cellvibrio* to proliferate dramatically. In the pre-harvest samples from actively growing plants, *Cellvibrio* was essentially absent from the endorhiza, consistent with living root tissue being resistant to cellulolytic colonization.

### Cellvibrio as a Post-Mortem Colonizer

*Cellvibrio* species are known for their cellulase enzymes and are commonly isolated from decomposing plant material, soil, and freshwater environments. They are Gram-negative bacteria within the Pseudomonadaceae family, and their ability to degrade crystalline cellulose makes them important decomposers in terrestrial ecosystems. The presence of *Cellvibrio* at 16.9% mean abundance in post-harvest roots — making it one of the dominant taxa — indicates that root decay was well advanced by eight weeks post-harvest.

Despite the confounding effect of root decay, the post-harvest experiment still detected significant cultivar-specificity in the endorhiza (weighted ADONIS R² = 0.59, p = 0.004; unweighted R² = 0.39, p = 0.003). This is remarkable because the cultivar-specific metabolites that presumably drive endophyte selection would no longer be actively produced by a dead or senescing plant. The persistence of cultivar-specific microbial signatures even without active host influence suggests that some endophyte communities are remarkably stable after host death, or that the decay process itself proceeds differently depending on the residual biochemical environment of different cultivar roots.

The high standard deviation of Cellvibrio abundance in the post-harvest samples (13.0%) relative to the mean (16.9%) indicates substantial plant-to-plant variation in the extent of decay colonization. This variation may reflect differences in root tissue quality, microenvironmental conditions, or the timing of initial decomposer colonization among individual plants.

## Alpha Diversity Differences

The post-harvest experiment showed dramatically lower alpha diversity in the endorhiza compared to the pre-harvest experiment:

| Metric | Exp. 1 Post-Harvest | Exp. 2 Pre-Harvest (MB Soil) | Exp. 2 Pre-Harvest (OC Soil) |
|--------|--------------------|---------------------------|---------------------------|
| Chao1 (mean) | 916.1 (SD = 161.7) | 3325 (SD = 517) | 3311 (SD = 112) |
| Observed species (mean) | Lower | Higher | Higher |

The endorhiza from the post-harvest experiment had roughly 3.6-fold lower species richness than pre-harvest samples. Even after pooling and rarifying both experiments to the same sequencing depth (3,000 sequences), the post-harvest endorhiza diversity remained greatly reduced. This dramatic diversity collapse is consistent with root senescence and decay, where the loss of plant immune function and metabolic activity leads to a microbial community dominated by a few opportunistic decomposers rather than the diverse consortium maintained by a living host.

### Bulk Soil and Rhizosphere Were Less Affected

Interestingly, the alpha diversity differences between experiments were less pronounced for bulk soil and rhizosphere samples. The bulk soil in Experiment 1 had intermediate diversity (chao1 = 2010.7) relative to the Experiment 2 soils (MB: 2319.1, OC: 2004.8). The rhizosphere showed a similar intermediate pattern. This differential impact — severe diversity loss in endorhiza but not in soil — further supports the interpretation that the diversity collapse was driven by root decay rather than by inherent differences between experiments or soils.

## Rhizosphere Signal Attenuation

The post-harvest experiment failed to detect significant cultivar effects in the rhizosphere (ADONIS R² = 0.07, p = 0.07 for unweighted; R² = 0.09, p = 0.10 for weighted), while the pre-harvest experiment did detect significant cultivar effects in the rhizosphere (ADONIS R² = 0.05, p = 0.04 for unweighted). This difference likely reflects the progressive decay of the rhizosphere effect after plant death:

- In living plants, root exudates maintain a distinct rhizosphere community that reflects the host genotype
- After harvest, exudation ceases and the rhizosphere gradually reverts to bulk soil community composition
- By eight weeks post-harvest, the rhizosphere signal had attenuated beyond statistical detection

This finding has important implications for field studies of plant microbiomes: sampling must occur during active plant growth to detect meaningful rhizosphere effects. Post-harvest sampling may still detect endorhiza cultivar-specificity (as this study showed), but rhizosphere patterns are likely lost or severely attenuated.

## Cultivar-Specificity Persistence Despite Decay

Perhaps the most intriguing finding from the comparison of these two experiments is that cultivar-specificity was detectable in the endorhiza even in the post-harvest samples. This persistence suggests several possible mechanisms:

1. **Physical protection**: Endophytes may be physically protected within root cortical tissues or vascular bundles, shielded from external colonization by decomposers
2. **Residual host chemistry**: Even after plant death, residual secondary metabolites, lectins, or cell wall composition differences may continue to filter microbial colonizers
3. **Established biofilms**: Mature endophyte biofilms may resist displacement by opportunistic decomposers
4. **Priority effects**: Early colonizers may resist invasion by later-arriving decomposer taxa through competitive exclusion

The fact that cultivar-specificity was stronger in weighted analysis (abundance-based) than unweighted analysis in the pre-harvest experiment, but both weighted and unweighted analyses detected it, suggests that cultivar effects operate on both community membership and community structure.

## Methodological Recommendations

Based on the differences between these two experiments, several best practices emerge for Cannabis microbiome research:

1. **Sample before or at harvest**, not after. Post-harvest sampling introduces confounding decay dynamics that obscure the native endorhiza community.
2. **Surface-sterilize root samples** thoroughly, especially if there is any possibility of partial tissue degradation. The alcohol and sterile water rinse protocol used in this study was appropriate but may be insufficient for compromised tissue.
3. **Report the time elapsed since harvest** when post-harvest sampling is unavoidable, as this is a critical variable affecting community composition.
4. **Consider Cellvibrio abundance as a quality control metric**. High Cellvibrio in endorhiza samples may indicate tissue decay and compromised data quality.
5. **Use root health assessments** such as tissue integrity scoring, electrolyte leakage measurement, or visual inspection to document sample condition.
6. **Include positive controls for decay** such as known-age decomposing root samples to distinguish decay-associated from living endorhiza taxa.

## Broader Implications

The contrast between these two experiments illustrates a fundamental challenge in plant microbiome studies: the plant is a dynamic organism, and its associated microbial communities change dramatically across developmental stages and after death. For Cannabis specifically, where the plant undergoes dramatic physiological changes during flowering and senescence, time-series sampling across the growth cycle would be far more informative than single time-point studies.

The persistence of cultivar-specificity in post-harvest roots, despite the loss of rhizosphere effects and the dramatic shift in community composition toward decay-associated taxa, suggests that some endophyte-host associations are remarkably durable. Understanding the mechanisms behind this persistence — whether it reflects physical protection within root tissues, metabolic cross-feeding, or other stabilizing interactions — could inform strategies for establishing beneficial microbial associations in agricultural settings.

## Cross-References

- [[cellvibrio-root-decay-indicator-cannabis-endorhiza]]
- [[cannabis-microbiome-experimental-design]]
- [[cannabis-endorhiza-microbiome]]
- [[cultivar-specificity-persistence-post-harvest-cannabis-endorhiza]]
- [[alpha-diversity-gradient-bulk-soil-cannabis-endorhiza]]
- [[cannabis-microbiome-two-tier-selection]]
