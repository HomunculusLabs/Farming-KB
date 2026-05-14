---
title: Two-Tier Selection Model for Plant Microbiome Assembly
source: understanding-cultivar-specificity-cannabis-microbiome.md
topics: microbiology, plant-microbe interactions, rhizosphere, Cannabis
created: 2026-05-11
---

# Two-Tier Selection Model for Plant Microbiome Assembly

## Overview

The two-tier selection model is a theoretical framework describing how [[cannabis-rhizosphere-microbial-communities]] associated with plant roots are assembled through a sequential filtering process. The model posits that root-associated microbiota are structured in two distinct stages: first by **edaphic (soil) factors** that determine the pool of available microorganisms, and second by **host genotype-dependent selection** that fine-tunes the community within plant tissues.

This model was empirically validated through studies of the Cannabis microbiome by Winston et al. (2014), published in PLOS ONE. The study represented the first comprehensive description of the endorhiza, rhizosphere, and bulk soil-associated microbiome of five distinct Cannabis cultivars, providing a uniquely controlled test of the model through systematic variation of both soil type and plant genotype.

The model emerged from earlier observations that plant-associated microbial communities are not random assemblages but are shaped by deterministic processes operating at different scales. Prior work by Bulgarelli et al. (2013) and Garbeva et al. (2004) had suggested a two-step process of root colonization, but the Cannabis study provided some of the clearest evidence by sampling across multiple compartments with controlled variation.

## The Two Selection Stages

### Tier 1: Soil-Driven Community Filtering

The first tier of selection occurs at the level of the bulk soil. [[cannabinoid-microbiome-correlation-confounded-edaphic-factors]]—including soil pH, nitrogen content, salinity, total organic carbon, water content, and soil texture—exert the strongest influence on determining which microbial taxa are present in the local environment. These factors structure the soil microbial community that serves as the source pool for subsequent colonization of the rhizosphere and plant interior.

In the [[edaphic-factors-microbial-community-structure]]:

- **Nitrogen** (strongest effect, r-stat: 0.465–0.630 depending on analysis)
- **Salinity** (r-stat: 0.437–0.620)
- **Total organic carbon** (r-stat: 0.330–0.512)
- **Water content** (r-stat: 0.281–0.466)
- **pH** (r-stat: 0.221–0.292)

A BEST (Best Subset of Environmental Variables) analysis determined that the optimal combination of edaphic variables explaining community variance was nitrogen, carbon, and water content (rho = 0.632). All tested edaphic factors showed significant correlations with community beta-diversity (p = 0.001 for all factors), underscoring the overwhelming importance of soil chemistry.

### Tier 2: Host Genotype-Dependent Selection

The second tier occurs when microorganisms transition from the rhizosphere into the plant's endorhiza (root interior). At this stage, host plant genotype—specifically the cultivar—becomes the primary determinant of microbial community structure, particularly in terms of relative abundance rather than mere presence or absence.

In the Cannabis study, strain-level differences were only statistically significant within the endorhiza. The [[cannabis-weighted-unifrac-strain-abundance-vs-presence-absence]] analysis showed that Cannabis strain was the main determinant of PC1 (34.51%) for all samples in the second experiment. Notably, there were zero significant unweighted OTU differences between cultivars, yet 71 OTUs showed significant weighted differences, confirming that cultivar selection modulates relative abundances without fundamentally changing which taxa can colonize.

The molecular basis for genotype-dependent selection likely involves plant-produced compounds including root exudates, lectins, and defense metabolites. Cannabis produces numerous secondary metabolic compounds including cannabinoids, and the observation of strong cultivar-specificity in its endorhiza suggests these specialized metabolites may directly influence microbial community assembly.

## Expected Community Shifts

The two-tier model predicts specific directional changes in phylum-level taxon abundance as microorganisms move from bulk soil through the rhizosphere and into the endorhiza:

### Acidobacteria Decrease

This phylum, abundant in bulk soils, is dramatically reduced in the endorhiza. The most significant OTU abundance difference between sample types was the decrease in Acidobacteria from order iii1-15 in endorhiza samples (Bonferroni-corrected ANOVA: p = 1.12e-7). Acidobacteria are generally adapted to oligotrophic conditions and may be outcompeted in the carbon-rich root interior environment.

### Proteobacteria Increase

Multiple Proteobacterial orders increase in the endorhiza: Rhizobiales, Burkholderiales, Sphingomonadales, and Pseudomonadales. Of 51 OTUs significantly differentiating between sample types, 17 that increased in the endorhiza were predominantly Proteobacteria, including several from the Rhizobiales order.

### Actinobacteria Increase

Actinobacteria also become more prevalent in the endorhiza, consistent with their known roles as endophytic colonizers in many plant systems.

### Conserved Core Community

Despite cultivar-specific differences, all endorhiza samples maintained a core community of Pseudomonas, Cellvibrio, Oxalobacteraceae, Xanthomonadaceae, Actinomycetales, and Sphingobacteriales. These well-known [[endorhiza-endophytic-bacteria]], primarily within Gammaproteobacteria and Alphaproteobacteria, appear to represent a stable plant-associated consortium found across all Cannabis cultivars tested.

## Evidence from the Cannabis Microbiome

### Shared OTU Analysis

A key prediction is that [[cannabis-rhizosphere-endorhiza-communities]] share more OTUs with their own soil than with a different soil. Using White Widow plants grown in two distinct soil types, the shared OTUs between endorhiza and their own soil (mean = 2934) was significantly greater than shared OTUs with the foreign soil (mean = 2162; t = -10.05, p = 1.209e-15).

### Alpha Diversity Patterns

The model predicts progressive diversity reduction from bulk soil to endorhiza. Chao1 metrics confirmed this:

- Bulk soil: mean = 4947 (SD = 717)
- Rhizosphere: mean = 4525 (SD = 542)
- Endorhiza: mean = 3321 (SD = 420)

While diversity differed between soil types in bulk soil and rhizosphere, endorhiza diversity was not significantly different between soils, suggesting host selection overrides soil-driven patterns once microbes enter root tissues.

### Beta-Diversity Distance Patterns

Distances between rhizosphere and bulk soil communities were significantly lower than distances between rhizosphere and endorhiza communities (unweighted: t = 24.59, p < 0.001; weighted: t = 211.82, p < 0.001). The greatest community restructuring occurs during the transition into the endorhiza, supporting the second tier as the more selective step.

### OTU Abundance vs. Presence/Absence

A critical finding was that soil type showed the strongest influence over both weighted (690 significant OTUs) and unweighted (657 significant OTUs) differences. Strain showed a moderate effect on weighted differences (71 significant OTUs) but zero significant unweighted differences, confirming that cultivar selection acts on abundance rather than composition.

## Cultivar-Specific Microbial Signatures

Distinct cultivars harbored characteristic microbial populations, demonstrating the practical reality of genotype-dependent selection. In the first experiment, Methylophilus comprised 13% of the endorhiza community in Bookoo Kush but only 0.13% in Burmese and was entirely absent in Sour Diesel (FDR: p = 0.012). This striking difference in a single genus accounted for a significant portion of the beta-diversity between cultivars and illustrates how a cultivar's internal chemistry can dramatically favor or disfavor specific bacterial taxa.

In the second experiment, [[arabidopsis-thaliana]], poplar, potato, and maize have all demonstrated that soil type is the primary determinant of rhizosphere community composition, while host genotype exerts stronger selection within root tissues. However, Cannabis presents a particularly interesting model organism because of its extensive [[arbuscular-mycorrhizal-fungi]]—in mediating bacterial community assembly deserves further investigation. Future work should focus on elucidating the role of cultivar on rhizosphere dynamics, identifying which aspects of host genotype produce the observed community structures, and developing targeted microbial inoculants that work synergistically with specific Cannabis cultivars.

## See Also

- [[edaphic-factors-soil-microbial-community-structure]]
- cannabis [[cultivar-specificity-microbiome]]
- rhizosphere effect root exudate microbe interactions
- plant microbiome alpha diversity gradients

## References

- Winston ME et al. (2014) Understanding Cultivar-Specificity and Soil Determinants of the Cannabis Microbiome. PLoS ONE 9(6): e99641.
- Bulgarelli D et al. (2013) Structure and Functions of the Bacterial Microbiota of Plants. Annu Rev Plant Biol.
- Garbeva P et al. (2004) Microbial diversity in soil: selection microbial populations by plant and soil type. Ann Rev Phytopathol.
