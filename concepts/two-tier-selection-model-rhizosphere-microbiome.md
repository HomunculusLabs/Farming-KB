---
title: Two-Tier Selection Model of the Rhizosphere Microbiome
slug: two-tier-selection-model-rhizosphere-microbiome
tags: [microbiology, rhizosphere, plant-microbe-interactions, soil-science, cannabis]
related: [endorhiza-endophyte-bacteria-plant-roots, cultivar-specificity-microbiome-plant-genotype]
source: [[endorhiza-microbiome-cannabis-cultivar-specificity]]
---

# Two-Tier Selection Model of the Rhizosphere Microbiome

The two-tier selection model is the prevailing framework for understanding how microbial communities assemble in and around plant roots. First articulated by Bulgarelli et al. (2012, 2013) and supported by work from Berg and Smalla (2009), the model proposes that root-associated microbiomes are assembled in two sequential filtering steps, each governed by different selective pressures. This model has been validated across numerous plant systems, including Arabidopsis, barley, poplar, and Cannabis sativa.

## The Two Selection Tiers

### Tier 1: Soil-Driven Filtering (Bulk Soil to Rhizosphere)

The first tier is driven by edaphic (soil) factors. Bulk soil contains the largest and most diverse pool of microorganisms, and its composition is shaped by physical and chemical properties:

- **Soil pH** — often the single strongest predictor of soil [[edaphic-factors-microbial-community-structure]] across geographic scales, affecting nutrient availability and enzyme activity
- **Nitrogen content** — total nitrogen concentration strongly correlates with beta-diversity of all root-associated communities, as nitrogen availability shapes the metabolic capacity of resident microbes
- **Salinity** — electrical conductivity and ionic composition of soil water influence osmotic stress on microbial populations
- **Organic carbon** — total organic carbon provides the primary energy source for heterotrophic soil microbes, driving community composition
- **Water content** — soil moisture affects oxygen availability, diffusion of soluble compounds, and microbial metabolic rates
- **Soil texture** — the ratio of sand, silt, and clay influences water retention, nutrient availability, pore space connectivity, and microbial habitat structure

When plant roots exude compounds into the surrounding soil — a process called rhizodeposition — the local environment shifts dramatically. Root exudates include sugars, amino acids, organic acids, mucilage, phenolics, [[plant-defense-chemistry-and-secondary-metabolites]] that create a nutrient-rich zone compared to bulk soil. This enrichment selects for microbes capable of utilizing these specific carbon sources, causing a community shift from the diverse bulk soil community toward a more specialized rhizosphere community.

In the Cannabis microbiome study (Winston et al., 2014), soil type was the dominant factor explaining community variation across all sample types. Principal coordinate analysis (PCoA) showed that soil type accounted for 32% of [[weighted-vs-unweighted-unifrac-cannabis-strain-microbiome]] variation (PC1 = 32.06%), making it the most important determinant of which microbes were present in any given sample.

### Tier 2: Host Genotype-Driven Selection (Rhizosphere to Endorhiza)

The second tier is driven by the plant itself. After soil-derived microbes colonize the rhizosphere, a subset migrates into the root interior — the endorhiza or endosphere. The plant exerts strong selective pressure on which microbes successfully establish as endophytes through several mechanisms:

- **Root architecture** — physical structure, tissue properties, and intercellular spaces that facilitate or impede microbial entry and colonization
- **Immune responses** — innate plant immunity (PTI and ETI pathways) recognizes and restricts microbial colonization to compatible taxa
- **Root exudate chemistry** — specific metabolites and signaling compounds that selectively promote or inhibit certain taxa beyond the general enrichment of the rhizosphere
- **Host proteins** — lectins and other root surface proteins that mediate specific microbe-host recognition, acting as gatekeepers for root entry
- **Secondary metabolites** — compounds such as cannabinoids in Cannabis, glucosinolates in Brassica, or alkaloids in other plants that may directly shape microbial communities

This second tier is genotype-dependent, meaning different cultivars or species of the same plant will select different endophytic communities even when grown in identical soil. In the Cannabis study, strain (cultivar) explained 27% of weighted UniFrac variation in the pooled analysis — nearly as much as soil type (32%). Crucially, strain effects were significant for weighted analysis (abundance-based) but not unweighted analysis (presence/absence-based), meaning cultivar selection primarily modulates the relative abundance of endophytes rather than determining which taxa can enter the root.

## Evidence from the Cannabis Microbiome Study

### Shared OTUs Support the Soil-Origin Hypothesis

A key prediction of the two-tier model is that endorhiza microbes are ultimately soil-derived. This was tested by comparing OTU overlap between endorhiza communities and their own soil versus a different soil in which the same cultivar was grown.

White Widow plants grown in two different soils (Mo-Bio and Orange County) shared significantly more OTUs with the soil they were actually grown in (mean = 2934 shared OTUs) than with the foreign soil (mean = 2162 shared OTUs), a highly significant difference (t = -10.05, p = 1.209e-15). This confirms that endophytes are recruited from the local soil pool rather than being vertically transmitted or randomly assembled.

### Community Similarity Patterns

Beta-diversity comparisons showed that rhizosphere and bulk soil communities were significantly more similar to each other than either was to the endorhiza, for both weighted and unweighted analyses.

Unweighted beta-distances between rhizosphere and bulk soil (t = 24.59, p < 0.001) and between bulk soil and endorhiza (t = 25.15, p < 0.001) were both highly significant. However, distances between rhizosphere and endorhiza were not significantly different from distances between bulk soil and endorhiza (unweighted: t = -2.10, p = 0.109; weighted: t = -2.23, p = 0.078), providing only partial support for the discrete-step nature of the model.

### Alpha Diversity Declines Along the Gradient

Species richness followed the expected pattern of progressive filtering:

- Highest in bulk soil (chao1 = 4947, SD = 717)
- Intermediate in the rhizosphere (chao1 = 4525, SD = 542)
- Lowest in the endorhiza (chao1 = 3321, SD = 420)

This progressive reduction in diversity reflects the increasing selectivity at each tier, as fewer organisms possess the traits needed to thrive in each more specialized niche. Notably, while bulk soil and rhizosphere diversity differed significantly between the two soil types tested (Mo-Bio vs Orange County), endorhiza diversity did not differ between soils — suggesting that host plant selection creates a convergence point.

### Edaphic Factor Rankings

BEST analysis identified nitrogen, carbon, and water content as the three [[cannabinoid-microbiome-correlation-confounded-edaphic-factors]] that optimally explained community variation (rho = 0.632). The ranked importance across all pooled samples was:

1. Nitrogen (r = 0.465 weighted, 0.630 unweighted)
2. Salinity (r = 0.437 weighted, 0.620 unweighted)
3. Carbon (r = 0.330 weighted, 0.512 unweighted)
4. Water content (r = 0.281 weighted, 0.466 unweighted)
5. pH (r = 0.221 weighted, 0.292 unweighted)

All edaphic factors were significantly correlated with community beta-diversity (p = 0.001 for all), confirming the primacy of soil chemistry in structuring root-associated microbiomes.

## Taxonomic Shifts Across Tiers

The transition from bulk soil to endorhiza is characterized by predictable taxonomic shifts at the phylum level:

- **Acidobacteria** dramatically decrease in abundance within the endorhiza. The most significant OTU shift between sample types was a decrease in Acidobacteria order iii1-15 (Bonferroni-corrected p = 1.12e-7), consistent with their oligotrophic lifestyle being maladapted to the carbon-rich root interior.
- **Proteobacteria** increase substantially, particularly orders within Gammaproteobacteria and Alphaproteobacteria, which are well-adapted to nutrient-rich environments and commonly found as endophytes.
- **Actinobacteria** increase in the endorhiza, reflecting their ability to survive in root tissues and produce antibiotics that may help them compete for niche space.
- Of the 51 OTUs significantly different between sample types, the 17 enriched in the endorhiza were predominantly Proteobacteria, including several from the Rhizobiales order.

## The Core Endorhiza Community

Despite cultivar-specific differences in abundance, all Cannabis plants shared a core endorhiza community consisting of:
