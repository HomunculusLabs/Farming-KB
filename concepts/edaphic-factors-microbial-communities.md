---
title: Edaphic [[edaphic-factors-structuring-cannabis-microbiome]] [[soil-edaphic-factors-microbial-communities]] in Cannabis
source: understanding-cultivar-specificity-cannabis-microbiome.md
tags: [microbiome, cannabis, rhizosphere, soil-science]
created: 2026-05-09
---

# Edaphic Factors Structuring Microbial Communities in Cannabis

Edaphic factors — the physicochemical properties of soil — are among the most
important determinants of microbial [[core-endorhiza-bacterial-community-composition-cannabis]] in terrestrial
ecosystems. The Winston et al. (2014) study systematically evaluated the
relative importance of key edaphic variables in structuring bulk soil,
rhizosphere, and endorhiza microbial communities associated with Cannabis
plants, using both Mantel tests and BEST (Best Subset of Environmental
Variables) analysis to quantify their contributions.

## Overview of Edaphic Factors Tested

Five edaphic factors were measured and analyzed for their effects on microbial
[[edaphic-determinants-cannabis-microbiome-community-structure]] across both experiments: total nitrogen concentration,
salinity, total organic carbon, water content, and pH. These factors were
measured for all bulk soil samples and used in Mantel tests to understand
their effects on structuring microbial communities across all sample types.
Soil texture was also characterized, with all soils classified as sandy loam.

## Nitrogen: The Strongest Predictor

Nitrogen was consistently the strongest edaphic predictor of microbial
community beta-diversity across both weighted and unweighted analyses. In the
weighted UniFrac analysis, nitrogen had the highest Mantel correlation
(r-stat = 0.465, p = 0.001). In the unweighted analysis, the effect was even
stronger (r-stat = 0.630, p = 0.001). This primacy of nitrogen is consistent
with the fundamental role of nitrogen as a limiting nutrient for microbial
growth in most soil environments. [[nitrogen-availability-in-legumes]] directly influences
microbial metabolic potential, growth rates, and competitive dynamics, making
it a master variable that shapes [[edaphic-factors-microbial-community-structure]] across all soil
compartments.

## Salinity: The Second Strongest Factor

Salinity was the second most important edaphic factor, with Mantel
correlations of r-stat = 0.437 (weighted, p = 0.001) and r-stat = 0.620
(unweighted, p = 0.001). Soil salinity affects microbial communities through
osmotic stress, which can inhibit the growth of salt-sensitive organisms while
selecting for halotolerant species. The two soil types in the second experiment
showed notable differences in salinity: the MB (Mo-Bio) soil had salinity
values ranging from 5.12 to 7.44, while the OC (Orange County) soil had a
salinity of just 1.73. This large difference in salinity between soils
contributed to the strong soil-type signal observed in the PCoA analyses.

## Carbon and Water Content

Total organic carbon was the third most important factor, with Mantel
correlations of r-stat = 0.330 (weighted, p = 0.001) and r-stat = 0.512
(unweighted, p = 0.001). Organic carbon serves as the primary energy source
for heterotrophic soil microbes, and its concentration directly influences
microbial biomass and [[mycorrhizal-effects-on-plant-community-composition]]. The two soil types showed
dramatic differences in organic carbon: MB soil had total organic C values of
3.02 to 5.00, while OC soil had a total organic C of 20.0 — roughly four to
six times higher. This substantial difference likely contributed to the strong
soil-type differentiation observed in the study.

Water content was the fourth most important factor, with Mantel correlations
of r-stat = 0.281 (weighted, p = 0.001) and r-stat = 0.466 (unweighted,
p = 0.001). Soil water content influences microbial activity by affecting
nutrient diffusion, oxygen availability, and osmotic conditions. The OC soil
had substantially higher water content (0.371) compared to MB soil (0.101 to
0.178), consistent with its higher organic matter content.

## pH: Important but Weakest of the Five

pH was the fifth and weakest of the five edaphic factors tested, though it
remained highly significant (r-stat = 0.221, weighted, p = 0.001; r-stat =
0.292, unweighted, p = 0.001). This finding is noteworthy because pH has
often been cited as the single most important edaphic factor structuring soil
microbial communities in other studies. The relatively lower importance of pH
in the Cannabis study may reflect the narrow pH range across the sampled
soils (6.63 to 6.94), which limited the variation available for detecting
pH effects.

## Mantel Test Results: All Factors Significant

For both weighted and [[weighted-vs-unweighted-unifrac-cannabis-strain-microbiome]] distances (with all samples pooled
in the analysis), all five edaphic factors tested were significantly
correlated with community beta-diversity (p = 0.001 for all factors). This
comprehensive significance underscores that microbial communities in the
Cannabis root zone are shaped by a combination of soil physicochemical
variables rather than any single dominant factor. The relative ranking of
importance (N > salinity > C > water > pH) was consistent between weighted
and unweighted analyses, lending confidence to the robustness of these
findings.

## Soil Texture: Sandy Loam Classification

All soils in the study were classified as sandy loam, with sand content
ranging from 62.0% to 66.0%, silt from 16.0% to 17.7%, and clay from 17.7%
to 20.7%. Despite this shared classification, there were significant
differences in clay content and other edaphic factors between the two soil
types used in the second experiment. The sandy loam texture across all sites
suggests that the [[cannabis-cultivar-microbial-community-effects]] differences observed were driven more
by chemical factors (nitrogen, carbon, salinity) than by physical soil
structure.

## Differences Between MB and OC Soil Types

The two soil types in the second experiment exhibited significant
physicochemical differences. MB (Mo-Bio) soil had higher salinity (5.12 to
7.44 vs 1.73), higher total nitrogen (0.26 to 1.51 vs 0.53), lower organic
carbon (3.02 to 5.00 vs 20.0), and lower water content (0.101 to 0.178 vs
0.371) compared to OC (Orange County) soil. pH values were similar between
soil types (6.63 to 6.94 for MB vs 6.77 for OC). These differences were
sufficient to produce highly significant clustering of microbial communities
by soil type in PCoA analyses (unweighted ADONIS: R² = 0.196, p = 0.001;
weighted ADONIS: R² = 0.323, p = 0.001).

## BEST Analysis: Optimal Combination of Factors

The BEST (Best Subset of Environmental Variables with Maximum Rank Correlation
with Community Dissimilarities) analysis was used to identify the combination
of edaphic factors that optimally explained variance in community data. This
analysis, implemented via the vegan::bioenv function in R, determined that
three factors — nitrogen, carbon, and water content — optimally explained the
variance in community composition, achieving a correlation of rho = 0.632.
This finding suggests that while all five factors are individually
significant, the combination of [[ph-and-nutrient-availability-garden-soils]] (N, C) and moisture
conditions captures the primary abiotic drivers of microbial community
structure in these Cannabis-associated soils.

## Implications for Cannabis Cultivation

These results have direct implications for Cannabis cultivation practices.
Soil [[weed-management-strategies]] that optimize nitrogen availability, maintain
appropriate salinity levels, and ensure adequate organic carbon and water
content can be expected to favor beneficial microbial communities. The strong
soil-type effect on all sample types — including the endorhiza — means that
soil selection and amendment practices will influence not only the soil
microbiome but also the microbes that colonize root tissues.

## References

- Winston ME, et al. (2014) Understanding Cultivar-Specificity and Soil
  Determinants of the [[cannabis-microbiome-cultivar-specificity]]. PLoS ONE 9(6): e99641.
- Oksanen J, et al. (2013) vegan: Community Ecology Package. R package.
