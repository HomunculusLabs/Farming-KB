---
title: Nitrogen Salinity Carbon Edaphic Microbial Structuring Cannabis
tags: [microbiome, cannabis, edaphic-factors, nitrogen, salinity, soil-chemistry, microbial-ecology]
related: [cannabis-microbiome-best-analysis-edaphic-factor-ranking, cannabis-microbiome-two-tier-selection, cannabis-endorhiza-microbiome]
source: [winston-cannabis-microbiome-study-design]
created: 2026-05-10
---

# Nitrogen, Salinity, and Carbon as Primary Edaphic Drivers of Cannabis Microbial Community Structure

## Overview

In the landmark Winston et al. (2014) study of the [[cannabis-microbiome-agricultural-implications-and-future-directions]], edaphic (soil) factors were shown to be the dominant determinants of microbial community structure across all sample types — bulk soil, rhizosphere, and endorhiza. Among the five edaphic variables tested (nitrogen, salinity, total organic carbon, water content, and pH), a clear hierarchical ranking emerged that has implications for [[arbuscular-mycorrhizal-fungi-cannabis-cultivation]] and microbial management.

## The Five Edaphic Factors Tested

The study measured five [[soil-physicochemical-properties-cannabis-microbiome-assembly-winston]] across five distinct soil types used in two experiments:

1. **Total nitrogen concentration** — ranged from 0.26% to 1.51%
2. **Salinity (electrical conductivity)** — ranged from 1.73 to 7.44 dS/m
3. **Total organic carbon** — ranged from 3.02% to 20.0%
4. **Water content** — ranged from 0.101 to 0.371
5. **pH** — ranged from 6.63 to 6.94 (narrow range, all slightly acidic)

The soil types were all classified as sandy loam, with varying proportions of sand (62–66%), silt (16–18%), and clay (17–21%).

## Weighted UniFrac Analysis: Abundance-Weighted Community Structure

Using weighted UniFrac distances (which account for both phylogenetic relatedness and relative abundance of taxa), the Mantel tests revealed the following correlation strengths with community beta-diversity:

| Rank | Factor | Correlation (r-stat) | p-value |
|------|--------|---------------------|---------|
| 1 | Nitrogen | 0.465 | 0.001 |
| 2 | Salinity | 0.437 | 0.001 |
| 3 | Total Organic Carbon | 0.330 | 0.001 |
| 4 | Water Content | 0.281 | 0.001 |
| 5 | pH | 0.221 | 0.001 |

All factors were statistically significant, but nitrogen showed approximately twice the explanatory power of pH in structuring communities when accounting for taxon abundance.

## Unweighted UniFrac Analysis: Presence-Absence Community Composition

Using unweighted UniFrac distances (which measure only phylogenetic distances based on presence or absence of taxa, ignoring abundance), the ranking remained the same but correlations were uniformly stronger:

| Rank | Factor | Correlation (r-stat) | p-value |
|------|--------|---------------------|---------|
| 1 | Nitrogen | 0.630 | 0.001 |
| 2 | Salinity | 0.620 | 0.001 |
| 3 | Total Organic Carbon | 0.512 | 0.001 |
| 4 | Water Content | 0.466 | 0.001 |
| 5 | pH | 0.221 | 0.001 |

The stronger correlations in [[unifrac-weighted-unweighted-analysis-cannabis-microbiome]] indicate that these edaphic factors are particularly important in determining which taxa are present at all, rather than merely adjusting their relative proportions.

## Why Nitrogen Leads: Ecological Interpretation

### Nitrogen as the Limiting Nutrient
Nitrogen's dominant role aligns with ecological theory. In most terrestrial ecosystems, nitrogen is the primary limiting nutrient for microbial growth. Soil [[nitrogen-availability-in-legumes]] directly determines which bacterial taxa can survive and reproduce, as different taxa have different [[fungal-bacterial-predators-nitrogen-acquisition-soil-ecology]] strategies:

- **Nitrogen fixers** (e.g., Rhizobiales, found enriched in Cannabis endorhiza) can thrive in low-N environments by converting atmospheric N₂
- **Copiotrophic bacteria** (e.g., Proteobacteria, which increased in the endorhiza) flourish in nitrogen-rich zones
- **Oligotrophic Acidobacteria** (which dramatically decreased in endorhiza) prefer nutrient-poor conditions

### Salinity as an Osmotic Filter
Salinity acts as a physiological filter, selecting for halotolerant or halophilic taxa while excluding salt-sensitive organisms. The study soils ranged from relatively low (1.73 dS/m in Orange County soil) to moderate salinity (7.44 dS/m in Bookoo Kush soil), a range sufficient to drive significant community differentiation.

### Carbon as an Energy Source
Total organic carbon determines the energy available for heterotrophic microbial metabolism. The Orange County soil had dramatically higher organic carbon (20.0%) compared to Mo-Bio soils (3.0–5.0%), representing a major nutritional difference that structured communities independently of nitrogen.

## Implications for Cannabis Cultivation

### Soil Amendment Priority
If cultivators seek to influence the soil microbiome to benefit their plants, the [[cannabis-microbiome-best-analysis-edaphic-factor-ranking]] suggests:

1. **[[stamets-compost-supplements-nitrogen-management]]** should be the first priority — both the form (ammonium vs. nitrate) and total amount significantly reshape [[cannabis-rhizosphere-microbial-communities]]
2. **Salinity control** is the second most important lever — excessive mineral salt accumulation from [[teaming-with-nutrients-natural-vs-synthetic-fertilizers]] can shift communities away from beneficial taxa
3. **Organic matter (carbon)** additions should be strategic — high-carbon amendments like compost selectively enrich different communities than low-carbon mineral soils
4. **Water content** matters but is secondary — consistent moisture is more important than total water content
5. **pH adjustment** had the weakest effect within the near-neutral range tested, though extreme pH shifts would likely have larger effects

### The Cultivar-Edaphic Interaction
The study found that while soil properties dominated overall community composition, within the endorhiza specifically, cultivar identity became the dominant factor structuring community abundance. This means that even in identical soil, different Cannabis strains will recruit different endophytic communities — but the pool of available microbes from which they recruit is still primarily determined by edaphic conditions.

This has practical implications: to optimize the [[cannabinoid-concentration-endorhiza-microbiome-correlation-cannabis]] for a specific cultivar, growers should first ensure appropriate soil chemistry (especially nitrogen levels) to cultivate the right pool of potential endophytes, and then allow the plant's genotype to select its preferred partners.

## Methodological Notes

The edaphic factor analysis was performed using the BEST (Best Subset of Environmental Variables with Maximum Rank Correlation with Community Dissimilarities) procedure in QIIME, which implements the `bioenv` function from the R vegan package. This multivariate approach tests all possible subsets of environmental variables to find the combination that best explains community distances.

The Mantel tests correlating individual edaphic factors with UniFrac community distances provide complementary information — while BEST identifies optimal variable combinations, Mantel tests reveal the independent contribution of each factor.
