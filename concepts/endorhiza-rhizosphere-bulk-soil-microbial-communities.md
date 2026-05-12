---
title: Endorhiza Rhizosphere and Bulk Soil Microbial Community Differentiation
source: understanding-cultivar-specificity-cannabis-microbiome.md
topics: microbiology, plant-microbe interactions, rhizosphere ecology, endophytes
created: 2026-05-11
---

# Endorhiza, Rhizosphere, and Bulk Soil Microbial Community Differentiation

## Overview

Plant root systems create three distinct microbial habitats: the **bulk soil** (soil not directly influenced by roots), the **rhizosphere** (soil immediately influenced by root exudates and activity), and the **endorhiza** or endosphere (the interior of the root tissue itself). Each of these compartments supports a progressively more specialized microbial community, with the greatest community shift occurring during the transition from rhizosphere to endorhiza. This compartmentalization was systematically characterized in Cannabis by Winston et al. (2014) using 16S rRNA gene sequencing across five cultivars.

## The Three Compartments

### Bulk Soil

Bulk soil represents the background microbial community determined primarily by [[cannabinoid-microbiome-correlation-confounded-edaphic-factors]] such as pH, nitrogen, carbon, salinity, water content, and soil texture. It serves as the source pool from which rhizosphere and endorhiza communities are drawn. Bulk soil communities are the most diverse of the three compartments and show the strongest differentiation between soil types. In the Cannabis study, bulk soil communities clustered significantly differently from other sample types in both unweighted (ADONIS: R² = 0.14, p = 0.001) and weighted (ADONIS: R² = 0.29, p = 0.004) UniFrac analyses.

The bulk soil harbors the full range of soil-adapted bacteria, including abundant Acidobacteria, which are characteristic of oligotrophic soil environments. The microbial diversity here reflects the complex physical and chemical properties of the soil matrix and the long-term ecological processes that have shaped the community.

### Rhizosphere

The rhizosphere is the narrow zone of soil directly influenced by root secretions, including exudates, mucilage, and lysates. This nutrient-rich environment selects for bacteria capable of rapid growth on labile carbon sources, creating a community that is distinct from bulk soil but retains substantial overlap. In the Cannabis study, rhizosphere samples showed mixed results for differentiation from other sample types—in the first experiment, rhizosphere samples were not significantly different from other categories (unweighted: ADONIS R² = 0.07, p = 0.07), though in the second experiment with greater edaphic variation, they did differentiate (unweighted: R² = 0.05, p = 0.04).

The rhizosphere effect—the enrichment of specific microbial taxa near roots relative to bulk soil—is driven by rhizodeposition, the release of organic compounds from roots. These compounds include sugars, amino acids, organic acids, [[plant-defense-mechanisms]] that serve as carbon and energy sources for heterotrophic bacteria. The rhizosphere community represents the first filtering step as soil microbes respond to the chemical environment created by the plant.

### Endorhiza (Endosphere)

The endorhiza comprises bacteria that have colonized the interior of root tissues, either between cells (apoplastic colonization) or within cells (symplastic colonization). This is the most selective microbial habitat, supporting the lowest diversity but the most specialized community. Endorhiza communities are shaped by plant immune responses, nutrient availability within root tissues, and specific plant-microbe signaling interactions.

In the Cannabis study, endorhiza samples formed the most distinct cluster in both unweighted (ADONIS: R² = 0.26, p = 0.001) and weighted (ADONIS: R² = 0.59, p = 0.001) analyses, and were the only compartment where cultivar-specific differences were statistically significant. The endorhiza community is enriched in Proteobacteria and Actinobacteria and depleted in Acidobacteria relative to both the rhizosphere and bulk soil.

## Alpha Diversity Gradient

A consistent pattern across all experiments was the progressive reduction in microbial diversity from bulk soil to endorhiza:

| Compartment | Chao1 (Exp 2) | SD |
|---|---|---|
| Bulk soil | 4947 | 717 |
| Rhizosphere | 4525 | 542 |
| Endorhiza | 3321 | 420 |

The same gradient was recovered in the first experiment despite much shallower sequencing depth:
- Bulk soil: chao1 = 2010.7 (SD = 146.2)
- Rhizosphere: chao1 = 1837.2 (SD = 114.0)
- Endorhiza: chao1 = 916.1 (SD = 161.7)

An interesting finding was that while bulk soil and rhizosphere diversity differed significantly between the two soil types tested (Mo-Bio and Orange County), endorhiza diversity was not significantly different between soils. This suggests that once bacteria successfully colonize root tissues, host plant factors constrain community diversity more strongly than the soil of origin.

## Beta-Diversity Distance Patterns

The degree of community similarity between compartments was quantified using pairwise beta-diversity distances:

- **Rhizosphere vs. Bulk soil**: Significantly lower distances than other comparisons (both analyses, p < 0.001), indicating these communities are most similar to each other.
- **Endorhiza vs. Rhizosphere**: Higher distances reflecting the major community shift at the root tissue boundary.
- **Endorhiza vs. Bulk soil**: Similarly high distances to endorhiza-rhizosphere comparisons.

Critically, the difference between rhizosphere-endorhiza distances and bulk soil-endorhiza distances was not statistically significant (unweighted: t = -2.10, p = 0.109; weighted: t = -2.23, p = 0.078). This provides only partial support for the intermediate filtering role of the rhizosphere, suggesting that the most dramatic community restructuring occurs directly at the root tissue boundary rather than in the surrounding soil.

## Core Endorhiza Community

Despite cultivar-specific differences in relative abundance, all Cannabis endorhiza samples shared a conserved core community. The prevalent members included:

- **Pseudomonas** (Gammaproteobacteria): Well-known plant growth-promoting bacteria and biocontrol agents.
- **Cellvibrio** (Gammaproteobacteria): Aerobic cellulolytic bacteria. Their presence as core community members in the first experiment was later attributed to post-harvest root decay, as their abundance dropped from 16.9% to 0.095% when comparing post-harvest to pre-harvest samples.
- **Oxalobacteraceae** (Betaproteobacteria): Known root colonizers found in many plant species.
- **Xanthomonadaceae** (Gammaproteobacteria): A widespread family of plant-associated bacteria.
- **Actinomycetales** (Actinobacteria): Common endophytes known for producing antibiotics and growth-promoting compounds.
- **Sphingobacteriales** (Bacteroidetes): Associated with plant root environments.

With the exception of Cellvibrio, all prevalent core community members are well-established [[endorhiza-endophytic-bacteria]], primarily within Gammaproteobacteria and Alphaproteobacteria, consistent with observations from other plant systems including poplar and Arabidopsis.

## Functional Roles of Compartment-Specific Communities

### Bulk Soil Functions

The bulk soil community drives nutrient cycling, organic matter decomposition, and soil structure maintenance. Microbial processes here determine the availability of nitrogen, phosphorus, and other essential nutrients that ultimately become accessible to plants through the rhizosphere.

### Rhizosphere Functions

[[lowenfels-rhizosphere-bacteria-plant-interaction]] provide direct benefits to plants including nitrogen fixation, phosphate solubilization, production of phytohormones (auxins, gibberellins, cytokinins), siderophore production for iron acquisition, and suppression of soil-borne pathogens through antibiotic production and competitive exclusion. The dynamic nature of rhizosphere communities responds to seasonal changes, diel temperature fluctuations, water content, pH, CO₂ concentration, and O₂ levels. These communities are highly responsive to the physiological state of the plant and shift predictably across growth stages, making the rhizosphere a temporally variable yet deterministic microbial environment.

### Endorhiza Functions

Endorhiza bacteria support plant growth and suppress diseases by providing phytohormones, low molecular weight compounds, and enzymes involved in regulating growth and metabolism. They also assist host plants in tolerating phytotoxic effects of environmental toxicants, including heavy metals and organic pollutants. Endorhiza communities tend to be more plant-specific and are shaped by compounds or proteins produced by their host. Both endophytes and epiphytes may play roles in localized terroir for crop plants, contributing to the unique chemical profiles associated with specific growing regions—much as microbial terroir influences wine characteristics.

## Sampling Considerations

The Cannabis study highlighted how sampling timing can dramatically affect observed communities. First-experiment samples taken eight weeks post-harvest showed evidence of root decay, with Cellvibrio—a known cellulolytic bacterium—comprising 16.9% of the endosphere community compared to only 0.095% in pre-harvest samples from the second experiment. This decay signature diminished the detectable rhizosphere effect and reduced alpha diversity in the first experiment's endosphere (chao1 = 916.1) compared to actively growing plants (chao1 = 3321–3325). The lesson is clear: for accurate characterization of plant-associated microbiomes, samples should be taken from actively growing plants rather than post-harvest, and the growth stage of the plant must be carefully documented and controlled.

## Methodological Approach

The [[winston-cannabis-microbiome-study-design]] employed Illumina sequencing of the V4 region of the 16S rRNA gene to analyze 69 total samples across two experiments. DNA was extracted using the PowerSoil DNA Isolation Kit with a modification of heating the extraction at 65°C for 10 minutes prior to the initial vortex step. The 291 bp V4 region was amplified using Earth Microbiome Project standard protocols with 515F and 806R Golay-barcoded primers.

Bioinformatic analysis was performed in QIIME 1.7.0, with quality filtering of raw Illumina data, OTU-picking against the Greengenes database (both closed and open reference methods), sequence alignment with PyNAST, phylogenetic tree construction with FastTree, and taxonomic assignment using the RDP classifier. Samples were rarified to 3,000 sequences (first experiment) or 45,000 sequences (second experiment) to enable fair comparison.

Statistical analyses included ADONIS (permutational MANOVA), ANOSIM, ANOVA, redundancy analysis (RDA), Mantel tests for correlation between community structure and environmental variables, and BEST analysis for identifying the optimal subset of environmental predictors. Multiple testing correction was applied using the false discovery rate (FDR) method.

## Relevance to Cannabis Agriculture

Understanding the differentiation between these three microbial compartments has direct implications for Cannabis cultivation. The bulk soil serves as the reservoir from which beneficial microbes are drawn, making soil health [[soil-mineral-management-and-amendment-strategies]] foundational to building a supportive microbiome. Rhizosphere management through companion planting, organic amendments, and controlled irrigation can enhance the density and diversity of beneficial microbes near root surfaces. Targeted endophyte inoculation—introducing beneficial bacteria directly into root tissues—represents a promising but technically challenging approach for improving plant fitness, suppressing pathogens, or augmenting cannabinoid production.

## The Rhizosphere as a Dynamic Interface

The rhizosphere is not a static environment but a highly dynamic interface that changes as the plant develops. Root exudation patterns shift with growth stage, leading to predictable changes in microbial community composition over time. Young seedlings produce different exudate profiles than flowering plants, and the microbial communities respond accordingly. This temporal dynamism was evident in the Cannabis study, where pre-harvest and post-harvest sampling revealed dramatically different community compositions even within the same cultivar. Understanding these temporal dynamics is essential for developing microbiome management strategies that align with the plant's natural developmental rhythms rather than working against them.

## Practical Applications

These principles can be applied in permaculture design, sustainable agriculture, and ecological restoration projects. Practitioners integrate these approaches to build resilient food production systems and healthy soil ecosystems.

## Key Considerations

When applying these concepts, several factors warrant attention: environmental conditions, regional climate variations, available resources, and long-term sustainability goals. Success depends on careful observation and adaptive management based on feedback from the system.

## See Also

- [[rhizosphere-bulk-soil-microbial-comparison]]
- [[cannabis-rhizosphere-bulk-soil-similarity-endorhiza-divergence]]
- [[cannabis-rhizosphere-bulk-soil-microbial-comparison]]
- [[cannabis-alpha-diversity-gradient-bulk-soil-rhizosphere-endorhiza]]
- [[beta-diversity-distances-bulk-soil-rhizosphere-cannabis-endorhiza]]

## See Also

- [[two-tier-selection-model-plant-microbiome-assembly]]
- [[edaphic-factors-soil-microbial-community-structure]]
- cannabis cultivar specificity microbiome

## References

- Winston ME et al. (2014) Understanding Cultivar-Specificity and Soil Determinants of the Cannabis Microbiome. PLoS ONE 9(6): e99641.
- Bulgarelli D et al. (2012) Revealing structure and assembly cues for Arabidopsis root-inhabiting bacterial microbiota. Nature 488: 91–95.
- Mendes R et al. (2011) Deciphering the rhizosphere microbiome for disease-suppressive bacteria. Science 332: 1097–1100.
