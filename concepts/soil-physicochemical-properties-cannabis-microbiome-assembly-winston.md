---
title: Soil Physicochemical Properties Cannabis Microbiome Assembly Winston
source: understanding-cultivar-specificity-cannabis-microbiome.md
source_author: "Winston et al. (2014)"
topics: [soil-science, cannabis-microbiome, edaphic-factors, microbiome-assembly, plant-microbe-interactions]
created: 2026-05-10
---

# Soil Physicochemical Properties and Their Role in Cannabis Microbiome Assembly

## Overview

Soil physicochemical properties are the primary determinant of microbial [[core-endorhiza-bacterial-community-composition-cannabis]] across all sample types in the [[cannabis-root-microbiome]]. The study by Winston et al. (2014), published in PLOS ONE, demonstrated that [[cannabinoid-microbiome-correlation-confounded-edaphic-factors]] exert the strongest influence on both the presence and abundance of microbial taxa, surpassing the effects of plant cultivar and sample type. Understanding these soil parameters is essential for predicting and managing the Cannabis microbiome in agricultural settings, particularly for a crop with significant medicinal and economic value whose [[fungal-elicitors-enhanced-secondary-metabolite-production]] may be influenced by microbial partners.

This finding aligns with broader plant microbiome literature showing that soil type is consistently the dominant factor shaping rhizosphere and [[cannabis-rhizosphere-endorhiza-communities]] across diverse plant species, though the Cannabis study was notable for being the first to characterize these relationships in this commercially and medicinally important crop.

The study analyzed 69 samples total across two experiments, including bulk soil, rhizosphere soil, and endorhiza (root interior) samples from five Cannabis cultivars grown in California soils. Soil parameters were measured at Fruit Growers Laboratory in Santa Paula, California, using standard agricultural testing protocols. The five parameters measured — pH, salinity, total nitrogen, total organic carbon, and water content — were each individually and collectively correlated with [[edaphic-factors-microbial-community-structure]] using Mantel tests and BEST analysis within the QIIME 1.7.0 [[qiime-bioinformatics-pipeline-16s-rrna-microbiome]].

## Key Soil Parameters Measured

The study characterized five soil types across two experiments, measuring the following physicochemical properties at Fruit Growers Laboratory (Santa Paula, CA):

- **pH**: Ranging from 6.63 to 6.94 across all samples — a relatively narrow acidic-to-neutral range
- **Salinity**: Measured as electrical conductivity (EC), ranging from 1.73 to 7.44 dS/m
- **Total Nitrogen**: Ranging from 0.26% to 1.51% — reflecting different levels of organic matter decomposition and fertilization
- **Total Organic Carbon**: Ranging from 3.02% to 20.0% — the most variable parameter between soil types
- **Water Content**: Ranging from 0.101 to 0.371 g/g — reflecting moisture retention capacity
- **Physical Composition**: Sand (62–66%), silt (16–18%), clay (17–21%), all classified as sandy loam

## Edaphic Factor Ranking by Correlation Strength

When all edaphic variables were tested for their correlation with community beta-diversity using both weighted and [[weighted-vs-unweighted-unifrac-cannabis-strain-microbiome]] distances, a clear hierarchy emerged. All samples from both experiments were pooled in the analysis.

### Weighted UniFrac Analysis
1. **Nitrogen** (r-stat: 0.465, p = 0.001) — the single strongest predictor of [[edaphic-determinants-cannabis-microbiome-community-structure]]
2. **Salinity** (r-stat: 0.437, p = 0.001)
3. **Total Organic Carbon** (r-stat: 0.330, p = 0.001)
4. **Water Content** (r-stat: 0.281, p = 0.001)
5. **pH** (r-stat: 0.221, p = 0.001)

### Unweighted UniFrac Analysis
The unweighted analysis, which captures presence/absence patterns rather than abundance, showed the same ranking but with stronger correlation coefficients:

1. **Nitrogen** (r-stat: 0.630, p = 0.001)
2. **Salinity** (r-stat: 0.620, p = 0.001)
3. **Carbon** (r-stat: 0.512, p = 0.001)
4. **Water Content** (r-stat: 0.466, p = 0.001)
5. **pH** (r-stat: 0.292, p = 0.001)

The consistently stronger correlations in the unweighted analysis suggest that edaphic factors primarily determine which taxa are present or absent, rather than their relative abundances. This is a critical distinction for understanding the two-tier selection model: the first tier (soil → rhizosphere) is primarily a composition filter, while the second tier (rhizosphere → endorhiza) is primarily an abundance filter driven by host genotype.

## BEST Analysis and Optimal Predictor Subset

A Best Subset of Environmental Variables with Maximum (Rank) Correlation (BEST) analysis, implemented through QIIME's vegan::bioenv function, determined that the variance in community data was optimally explained by just three edaphic factors: **Nitrogen, Carbon, and Water Content** (rho = 0.632). This is notable because salinity and pH, while individually correlated with community structure, are partially redundant with the combination of nitrogen, carbon, and moisture. In practical terms, a grower monitoring these three parameters would capture the majority of edaphic influence on the microbiome.

## Soil Type Dominance in OTU Composition

The number of significant OTUs differing between soil types dwarfed all other comparisons, underscoring the primacy of edaphic factors:

- **Soil type**: 690 OTUs (weighted), 657 OTUs (unweighted)
- **Strain (cultivar)**: 71 OTUs (weighted), 0 OTUs (unweighted)
- **Sample type** (bulk soil, rhizosphere, endorhiza): 51 OTUs (weighted), 11 OTUs (unweighted)

The complete absence of unweighted cultivar differences indicates that all Cannabis cultivars tested share the same pool of potentially colonizing taxa — they differ only in how abundantly they host them within the endorhiza. This finding has important practical implications: inoculant selection can be guided by soil type rather than cultivar, since the available taxa are determined edaphically.

## Two Distinct Soil Environments Compared

### Mo-Bio (MB) Soil Series

The first experiment used a single composted soil (MB.1) with consistent physicochemical properties across three cultivars. The second experiment introduced MB.2 soil, which had lower organic carbon and nitrogen but similar texture. MB soils were characterized by higher salinity (5.12–7.44 dS/m) and lower organic carbon (3.02–5.00%) compared to Orange County soil. Three sub-types of MB.1 soil were identified based on the cultivar grown in them (B = Burmese, SD = Sour Diesel, BK = Bookoo Kush), though these showed minimal edaphic variation.

### Orange County (OC) Soil

The second experiment included a dramatically different soil type with much higher organic carbon (20.0%), moderate nitrogen (0.53%), and very low salinity (1.73 dS/m). This soil produced a microbial community structure that was significantly different from MB-grown plants. The OC soil's high organic carbon content likely supported a different base microbial community, providing the strong edaphic variation needed to properly test the two-tier selection model with its prediction of soil-determined rhizosphere composition.

## Interaction with Cultivar Effects and Cannabinoid Confounds

The dramatic differences in soil chemistry between MB and OC soils in the second experiment created a confounding factor for cannabinoid analysis. Plants from the OC soil had higher THC composition and concentration, but THC variables were also significantly correlated with soil edaphic variables (p = 0.001). This made it impossible to disassociate any association between microbiota and THC from soil physicochemical effects.

The authors acknowledged this limitation and noted that while significant differences between strains were found for unweighted community structure (r-stat: 0.863, p = 0.001), the higher THC composition and concentration in plants from one of the soil types meant that any association between microbiota and THC could not be separated from soil physicochemical variables. This underscores a general challenge in plant-microbiome research: the difficulty of disentangling host genotype effects from environmental effects when the host's secondary metabolism is itself environmentally responsive.

Future studies should decouple cannabinoid variation from edaphic variation through controlled experiments, such as growing the same cultivar across a gradient of soil types with matched cannabinoid profiles, or using isogenic lines that differ only in their cannabinoid production capacity.

## Sandy Loam Consistency Across Sites

Despite significant differences in chemical properties, all soils shared a similar physical composition classified as sandy loam (62–66% sand, 16–18% silt, 17–21% clay). This texture classification was consistent across both experiments and both locations (Vista and Orange County, California). The consistency in physical composition while chemical properties varied suggests that within this textural class, chemical properties are the dominant drivers of microbiome differentiation. The practical implication for [[arbuscular-mycorrhizal-fungi-cannabis-cultivation]] is that soil texture alone provides limited predictive value for microbiome outcomes — chemical management is the key variable. Sandy loam's well-drained nature and moderate water-holding capacity may represent an optimal texture class for Cannabis root microbiome development, though comparative studies across textures are needed to confirm this hypothesis.

## Alpha Diversity Differences Between Soils

The second experiment revealed significant alpha diversity differences between soil types. MB bulk soil had higher observed species and chao1 diversity (chao1: m = 5597; s = 89) compared to OC bulk soil (chao1: m = 4296; s = 85). This pattern extended to the rhizosphere (MB: chao1 m = 4859 vs OC: chao1 m = 3913). However, endorhiza diversity converged between soil types (MB: chao1 m = 3325 vs OC: chao1 m = 3311), suggesting that host plant selection on the endophytic community overrides soil-driven diversity differences at the root interior.
