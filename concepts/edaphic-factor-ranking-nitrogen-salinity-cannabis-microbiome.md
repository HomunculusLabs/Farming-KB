---
title: Edaphic Factor Ranking in cultivar-cannabis-microbiome-two-tier-selection-model Assembly via BEST Analysis
created: 2026-05-08
tags: [microbiology, cannabis, microbiome, edaphic-factors, soil-science, nitrogen, salinity, BEST-analysis, community-ecology]
date: 2026-05-08
---

# Edaphic Factor Ranking in Cannabis Microbiome Assembly via BEST Analysis

## Overview

The physical and chemical properties of soil — collectively called edaphic
factors — are primary drivers of [[edaphic-factors-microbial-community-structure]] structure. In the
Cannabis microbiome study (Winston et al., 2014), a Best Subset of
Environmental Variables with Maximum (Rank) Correlation (BEST) analysis
was employed to determine which [[soil-edaphic-factors-microbial-communities]] most strongly influence
[[core-endorhiza-bacterial-community-composition-cannabis]] across bulk soil, rhizosphere, and endorhiza
compartments.

## Edaphic Factors Measured

The study quantified five soil physicochemical properties for each sample:
- **Total Nitrogen** (N)
- **Total Organic Carbon** (C)
- **pH**
- **Salinity**
- **Water content**

Soil texture was also characterized as sandy loam across all sites, with
variation in clay and silt proportions. Two soil types showed significant
edaphic differences: Mo-Bio soil (higher salinity, lower organic carbon)
and Orange County soil (lower salinity, much higher organic carbon at
20.0% vs. ~3-5%).

## Mantel Test Results: All Factors Significant

For both weighted and [[weighted-vs-unweighted-unifrac-cannabis-strain-microbiome]] distances (all samples pooled),
every edaphic factor tested was significantly correlated with community
beta-diversity (p = 0.001 for all). However, the strength of correlation
varied substantially between factors.

## Weighted Analysis Ranking

In the weighted (abundance-sensitive) analysis, edaphic factors ranked
by correlation strength with community dissimilarity:

| Rank | Factor          | R-statistic | p-value |
|------|-----------------|-------------|---------|
| 1    | Nitrogen        | 0.465       | 0.001   |
| 2    | Salinity        | 0.437       | 0.001   |
| 3    | Carbon          | 0.330       | 0.001   |
| 4    | Water content   | 0.281       | 0.001   |
| 5    | pH              | 0.221       | 0.001   |

## Unweighted Analysis Ranking

The unweighted (presence/absence) analysis showed the same ordering but
with stronger overall correlations:

| Rank | Factor          | R-statistic | p-value |
|------|-----------------|-------------|---------|
| 1    | Nitrogen        | 0.630       | 0.001   |
| 2    | Salinity        | 0.620       | 0.001   |
| 3    | Carbon          | 0.512       | 0.001   |
| 4    | Water content   | 0.466       | 0.001   |
| 5    | pH              | 0.221       | 0.001   |

The stronger correlations in the unweighted analysis suggest that edaphic
factors have an even greater effect on which taxa are present than on
their relative abundances. In other words, nitrogen and salinity levels
determine whether a taxon can survive in a given soil, while the actual
proportions are more influenced by plant-driven factors.

## Nitrogen as the Dominant Edaphic Factor

Nitrogen emerged as the single most important edaphic factor in both
analyses. This is consistent with nitrogen's role as the primary
limiting nutrient for microbial growth in most terrestrial ecosystems.
Total nitrogen concentration constrains the size of the microbial
biomass that a soil can support and selects for organisms with
compatible nitrogen metabolism strategies.

The Mo-Bio soil had total nitrogen of 0.26-1.51%, while the Orange
County soil had 0.53% nitrogen but dramatically higher organic carbon
(20.0%). Despite lower nitrogen, the high-carbon Orange County soil
supported a distinct microbial community, reflecting the interplay
between carbon availability and nitrogen limitation.

## Salinity as the Second Factor

Salinity ranked second in both analyses, which is notable given that
soil salinity directly affects microbial osmotic balance. High salinity
creates a physiological barrier that excludes salt-sensitive taxa while
selecting for halotolerant organisms. The Mo-Bio soil had salinity
readings of 5.12-7.44 compared to 1.73 for the Orange County soil,
representing a substantial difference that contributed to community
differentiation.

## Carbon and Water Content

Organic carbon content ranked third and water content fourth. Carbon
is the primary energy source for heterotrophic soil bacteria, while
water content affects oxygen diffusion, [[cervantes-nutrient-mobility-deficiency-diagnosis]], and
microbial activity. The dramatic difference in organic carbon between
soil types (3-5% vs. 20%) likely drove much of the community
differentiation beyond what nitrogen alone explains.

## pH: Weakest but Still Significant

pH ranked last among the five factors tested, though it remained
statistically significant (r = 0.221, p = 0.001). This is somewhat
surprising given that pH is often cited as the strongest edaphic
predictor of soil microbial community composition in the broader
literature. The relatively narrow pH range across samples (6.63-6.94)
may have limited the ability to detect stronger pH effects, as all
soils were mildly acidic.

## Interaction with Plant Strain Effects

THC levels were significantly correlated with endorhiza community structure
(Mantel r = 0.863, p = 0.001), but THC was also correlated with edaphic
variables because one soil type produced higher-THC plants. This confounding
means microbiome-cannabinoid associations cannot be cleanly separated from
soil chemistry without controlled experiments.

## Implications for Cannabis Cultivation

For growers, the edaphic factor rankings suggest a priority order for
soil management:
1. **Nitrogen management** has the largest effect on the available
   microbial community
2. **Salinity control** (through irrigation practices) is the second
   most important lever
3. **Organic matter** (carbon) amendments should target adequate levels
   rather than maximizing content
4. **Water management** and **pH adjustment** fine-tune the community
   but have smaller effects within normal ranges
