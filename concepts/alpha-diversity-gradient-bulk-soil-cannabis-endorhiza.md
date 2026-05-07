---
title: Alpha Diversity Gradient from Bulk Soil to Cannabis Endorhiza
tags:
  - cannabis
  - microbiome
  - alpha-diversity
  - endorhiza
  - rhizosphere
  - bulk-soil
  - chao1
  - microbial-ecology
date: 2026-04-28
updated: 2026-04-28
sources:
  - raw/papers/understanding-cultivar-specificity-cannabis-microbiome.md
---

# Alpha Diversity Gradient from Bulk Soil to Cannabis Endorhiza

## Overview

A consistent finding across the cannabis microbiome literature is that [[alpha diversity]] follows a declining gradient from [[bulk soil]] through the rhizosphere to the [[cannabis-endorhiza-microbiome]]. This pattern was demonstrated in the Winston et al. (2014) study using both observed species counts and the chao1 diversity index.

The gradient mirrors patterns observed in many other plant species including Arabidopsis, Populus, and potato. It reflects the progressive filtering of the soil microbial community as organisms transition from the open soil environment into increasingly selective root-associated compartments.

## Quantified Diversity Values

### Second Experiment (Pre-Harvest Sampling)

Plants were sampled two weeks prior to harvest in the second experiment. The chao1 values showed a clear progressive decline:

- **Bulk soil**: chao1 mean of 4,947 (SD = 717)
- **Rhizosphere**: chao1 mean of 4,525 (SD = 542)
- **Endorhiza**: chao1 mean of 3,321 (SD = 420)

The bulk soil to rhizosphere transition showed a slight reduction of approximately 422 chao1-estimated species (about 8.5%). The rhizosphere to endorhiza transition produced a dramatic reduction of approximately 1,204 species (about 26.6%).

### First Experiment (Post-Harvest Sampling)

The same pattern was recovered in the first experiment despite much shallower sequencing depth:

- **Bulk soil**: chao1 mean of 2,010.7 (SD = 146.2)
- **Rhizosphere**: chao1 mean of 1,837.2 (SD = 114.0)
- **Endorhiza**: chao1 mean of 916.1 (SD = 161.7)

The proportional reduction from bulk soil to endorhiza was approximately 54% in this experiment, substantially larger than the 33% observed in the second experiment. The larger reduction is attributable to post-harvest [[root decay]] processes that further reduced endorhiza diversity beyond the normal plant-driven filtering.

## Mechanisms Driving the Gradient

### Bulk Soil as the Microbial Reservoir

[[alpha-diversity-gradient-bulk-soil-cannabis-endorhiza]] represents the most diverse microbial environment because it is subject to the fewest selective pressures. Soil microbial communities are shaped primarily by [[edaphic factors]] including pH, nitrogen, carbon content, salinity, and water content.

Within these constraints, a wide range of organisms with different metabolic strategies can coexist. The high diversity reflects the heterogeneous nature of soil as a habitat, with diverse microenvironments supporting different lifestyles from oligotrophic Acidobacteria to copiotrophic Proteobacteria.

The bulk soil serves as the reservoir from which rhizosphere and endorhiza communities are drawn. All organisms found in the root compartments must first exist in the soil, establishing the fundamental constraint on community assembly described by the first tier of the [[two-tier selection model]].

### Rhizosphere as a Semi-Permeable Filter

The transition from bulk soil to rhizosphere involves the first major selective filter. Rhizodeposition including root exudates, mucilage, border cells, and dead cell material creates a nutrient-rich environment that favors certain microbial groups over others.

However, this enrichment effect is relatively modest in terms of diversity loss. The modest reduction suggests the rhizosphere is a relatively permissive environment where most soil organisms can persist at some level, even if their relative abundances shift.

This is consistent with the finding that rhizosphere communities were not significantly different from other sample types in the unweighted analysis of the first experiment (ADONIS: R-squared = 0.07, p = 0.07). Presence/absence patterns are largely preserved during the soil-to-rhizosphere transition.

The rhizosphere acts as a semi-permeable filter that enriches for copiotrophic organisms while reducing but not eliminating oligotrophic taxa. Many organisms that decline in the rhizosphere are not excluded entirely but merely reduced in abundance.

### Endorhiza as the Strongest Selective Bottleneck

The most dramatic diversity reduction occurs during the transition from rhizosphere to [[cannabis-endorhiza-microbiome]]. Entry into root tissues requires organisms to overcome physical barriers including the Casparian strip and cell walls.

They must also navigate plant immune responses including pattern-triggered and effector-triggered immunity. Additionally, they must compete for space within the root cortical intercellular spaces.

This second selective step, described in the [[two-tier selection model]], is driven primarily by host genotype and produces the most pronounced diversity decline. Only organisms with specific adaptations for endophytic life persist within the endorhiza.

These adaptations include the ability to colonize intercellular spaces, tolerate plant defense compounds such as phytoalexins and reactive oxygen species, form mutualistic signaling relationships with the host, and compete effectively in the nutrient-rich but biologically challenging root interior.

The loss of approximately 27% of rhizosphere species during this transition represents a substantial culling event. It fundamentally reshapes community composition, producing the cultivar-specific patterns observed in the endorhiza.

## Soil Type Effects on Alpha Diversity

While the diversity gradient was consistent across soil types, there were significant differences in absolute diversity between the two soil types tested:

- **Mo-Bio soil**: bulk soil chao1 = 5,597, rhizosphere chao1 = 4,859
- **Orange County soil**: bulk soil chao1 = 4,296, rhizosphere chao1 = 3,913

However, endorhiza diversity was not significantly different between soil types (Mo-Bio chao1: 3,325 vs. Orange County chao1: 3,311). This convergence supports the [[two-tier selection model]].

Despite different starting diversities in the soil reservoir, the host plant applies consistent selective pressure producing similar end-point diversity within root tissues regardless of soil origin. The Mo-Bio soil had a larger pool of organisms, but the endorhiza bottleneck produced equivalent diversity.

## Post-Harvest Diversity Reduction and Cellvibrio

The first experiment was conducted eight weeks post-harvest, producing substantially lower endorhiza diversity (chao1: 916.1 vs. approximately 3,300 in the second experiment). The post-harvest samples showed high abundances of Cellvibrio.

Cellvibrio comprised 16.9% of the endorhiza community (SD = 13.0%) in post-harvest samples compared to only 0.095% (SD = 2.7%) in actively growing plants. This enrichment serves as a useful biomarker for distinguishing living from decaying root microbiome samples.

The dramatic difference between experiments underscores that sampling timing is critical for accurately characterizing the functional endorhiza community. Post-harvest samples capture decomposition communities rather than the mutualistic endophytes present during active growth.

## Relationship to Beta Diversity Patterns

The alpha diversity gradient parallels [[beta diversity]] patterns observed in the same study. Rhizosphere and bulk soil communities were more similar to each other than either was to endorhiza communities.

Beta distances between rhizosphere and bulk soil were significantly lower than rhizosphere-to-endorhiza distances for both unweighted (t = 24.59, p less than 0.001) and weighted (t = 211.82, p less than 0.001) analyses.

The alpha diversity reduction at the rhizosphere-to-endorhiza boundary reflects the same selective processes that drive the beta diversity differentiation between compartments.

## Implications for Microbial Terroir

The alpha diversity gradient has implications for understanding [[microbial terroir]] in cannabis. While the soil determines the available pool of organisms with varying diversity levels, the plant genotype acts as the final arbiter.

The endorhiza bottleneck produces convergent diversity regardless of soil origin. This means that cultivar-specific microbial communities could contribute to consistent product characteristics even when plants are grown in different soils, because the selective filtering is genotype-dependent rather than soil-dependent.

## See Also

- [[microbial-alpha-diversity-soil-plant-gradient]]
- [[edaphic-factors-cannabis-endorhiza-microbiome-assembly]]

- [[two-tier selection model]]
- [[beta diversity root soil compartments cannabis]]
- [[cannabis endorhiza microbiome]]
- [[edaphic determinants of cannabis microbiome community structure]]
- [[chao1 diversity index]]
- [[cellvibrio-and-root-decay-microbiome]]
- [[core endorhiza bacterial community composition in cannabis]]
- [[acidobacteria-decline-rhizosphere-endorhiza-transition]]
