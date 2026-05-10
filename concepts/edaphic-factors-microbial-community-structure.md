---
title: [[cannabinoid-microbiome-correlation-confounded-edaphic-factors]] and [[cannabis-cultivar-microbial-community-effects]] Structure
created: 2026-05-09
tags: [soil-science, microbiome, edaphic-factors, rhizosphere, cannabis]
date: 2026-05-09
updated: 2026-05-09
sources:
  - /Users/t3rpz/wiki/raw/papers/understanding-cultivar-specificity-cannabis-microbiome.md
type: concept
---

# Edaphic Factors and Microbial Community Structure

## Overview

Edaphic factors — the physical, chemical, and biological properties of soil
— are the primary determinants of microbial [[core-endorhiza-bacterial-community-composition-cannabis]] in the
plant root zone. Winston et al. (2014) demonstrated that in Cannabis, soil
properties overwhelmingly determine which bacterial taxa are available for
root colonization, while plant cultivar subsequently shapes the relative
abundances of those taxa within the endorhiza.

## Soil Physicochemical Properties Studied

The Cannabis microbiome study measured five key edaphic variables across
five soil types from two experiments:

| Soil ID | pH | Salinity | Total N (%) | Total Organic C (%) | Water Content |
|---------|-----|----------|-------------|---------------------|---------------|
| MB.1.B | 6.94 | 7.15 | 1.41 | 5.00 | 0.164 |
| MB.1.SD | 6.80 | 7.10 | 1.51 | 4.32 | 0.178 |
| MB.1.BK | 6.82 | 7.44 | 1.30 | 3.31 | 0.101 |
| MB.2 | 6.63 | 5.12 | 0.26 | 3.02 | 0.113 |
| OC.2 | 6.77 | 1.73 | 0.53 | 20.0 | 0.371 |

All soils were classified as sandy loam with similar physical composition
(~64% sand, ~17% silt, ~19% clay), but showed dramatic differences in
chemical properties. The Orange County soil (OC.2) had notably higher total
organic carbon (20.0% vs. 3-5%) and water content (0.371 vs. 0.10-0.18%).

## Relative Importance of Edaphic Factors

Mantel tests revealed a clear hierarchy of edaphic influence on community
beta-diversity:

### Weighted UniFrac Analysis (abundance-sensitive):

1. **Nitrogen** — strongest effect (r-stat: 0.465, p = 0.001)
2. **Salinity** — second strongest (r-stat: 0.437, p = 0.001)
3. **Total Organic Carbon** — moderate effect (r-stat: 0.330, p = 0.001)
4. **Water Content** — moderate effect (r-stat: 0.281, p = 0.001)
5. **pH** — weakest but significant (r-stat: 0.221, p = 0.001)

### Unweighted UniFrac Analysis (presence/absence-sensitive):

1. **Nitrogen** — strongest effect (r-stat: 0.630, p = 0.001)
2. **Salinity** — second strongest (r-stat: 0.620, p = 0.001)
3. **Total Organic Carbon** — (r-stat: 0.512, p = 0.001)
4. **Water Content** — (r-stat: 0.466, p = 0.001)
5. **pH** — (r-stat: 0.221, p = 0.001)

The relative ranking is identical between weighted and unweighted analyses,
with nitrogen and salinity consistently being the dominant factors. The
stronger correlations in unweighted analyses suggest these factors primarily
determine which organisms can survive in a given soil, while their effects
on abundance are somewhat moderated by other factors.

## Nitrogen as the Dominant Edaphic Factor

[[nitrogen-availability-in-legumes]] emerged as the single most important edaphic variable
structuring [[cannabis-rhizosphere-microbial-communities]]. This is biologically logical because:

- Nitrogen is a limiting nutrient for most soil microorganisms
- Nitrogen availability directly influences microbial growth rates and
  competitive dynamics
- Different bacterial groups have varying nitrogen utilization strategies
  (ammonifiers, nitrifiers, nitrogen fixers)
- Nitrogen levels affect root exudate composition, indirectly shaping
  the rhizosphere environment

The dramatic nitrogen difference between MB.2 (0.26%) and other soils
(1.30-1.51%) likely drove substantial community shifts in experiment 2.

## Salinity as the Second Most Important Factor

Soil salinity is a well-known determinant of microbial community structure.
High salinity creates osmotic stress that:

- Selects for halotolerant bacterial taxa
- Reduces overall microbial diversity
- Shifts community composition toward Proteobacteria, which tend to be more
  salt-tolerant than Acidobacteria
- Alters competitive interactions by stressing salt-sensitive populations

The large salinity difference between OC.2 (1.73) and MB soils (5.12-7.44)
contributed to significant community separation between soil types.

## Edaphic vs. Biotic Factors

When all factors were considered together, the hierarchy of influence on
microbial community structure was:

1. **Soil type** (edaphic) — dominant for both composition and structure
2. **Cultivar/strain** (biotic) — significant for endorhiza structure only
3. **Sample type** (compartment) — structures communities by proximity
   to root

Soil type produced 690 significant weighted OTU differences, compared to
71 for strain and 51 for sample type. This ~10:1 ratio underscores the
primacy of edaphic conditions in determining the available microbial pool.

## Soil Texture Considerations

All soils in the study were sandy loam, which limited the ability to assess
the effect of soil physical structure. In other systems, soil texture has
been shown to significantly influence microbial communities through:

- Water-holding capacity affecting microbial habitat connectivity
- Particle surface area determining attachment sites
- Pore size distribution influencing oxygen availability and microbial
  predation by protozoa

The controlled texture in this study allowed cleaner isolation of chemical
edaphic effects.

## BEST Analysis for Factor Optimization

The Best Subset of Environmental Variables with Maximum (Rank) Correlation
with Community Dissimilarities (BEST) analysis was used to identify the
optimal combination of edaphic factors for explaining community variation.
This multivariate approach confirmed that the five measured factors
collectively provided strong predictive power for community structure.

## Implications for Cannabis Cultivation

- **Soil testing**: Measuring nitrogen, salinity, carbon, and pH predicts
  the microbial foundation available to plants
- **Soil amendments**: Targeted amendments can shift the microbial pool
  toward beneficial compositions
- **Irrigation**: Water content influences community structure,
  indirectly affecting root [[edaphic-factors-cannabis-endorhiza-microbiome-assembly]]
- **Site selection**: Strong edaphic effects mean growing location
  constrains microbiome possibilities for any cultivar

## See Also

- [[cannabis-endorhiza-microbiome-structure]]
- [[two-tier-selection-model-plant-microbiome]]
- [[cultivar-specific-root-microbial-communities]]
- [[16s-rrna-sequencing-microbiome-analysis]]
