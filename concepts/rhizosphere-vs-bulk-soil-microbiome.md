---
title: Rhizosphere vs Bulk Soil Microbiome in Cannabis
source: understanding-cultivar-specificity-cannabis-microbiome.md
tags: [microbiome, cannabis, rhizosphere, soil-science]
created: 2026-05-09
---

# Rhizosphere vs Bulk Soil Microbiome in Cannabis

Understanding how [[edaphic-factors-microbial-communities]] differ across the root-soil continuum
is essential for characterizing plant-microbiome interactions. The Winston et
al. (2014) study systematically compared [[cannabis-endorhiza-bacterial-communities]] across three
sample types — bulk soil, rhizosphere soil, and endorhiza (root interior) —
in Cannabis plants, revealing consistent patterns of community differentiation
that have implications for both basic plant ecology and agricultural practice.

## The Three Sample Types Defined

The study examined [[soil-edaphic-factors-microbial-communities]] from three distinct compartments
along the root-soil interface. Bulk soil refers to soil collected at a
distance from the plant root (10 cm from the stem at 20 cm depth), representing
the background soil [[cannabis-cultivar-microbial-community-effects]] unaffected by direct root influence.
Rhizosphere soil is the soil that remains adhered to the roots after removal
from the ground, representing the zone of direct plant-microbe interaction
shaped by [[query-what-are-root-exudates-and-how-do-they-shape-soil-life]] rhizodeposition. The endorhiza is the root
interior itself, where bacteria have colonized plant tissues and form intimate
associations with root cells.

## Experimental Design and Sample Collection

The study was conducted in two experiments. The first experiment collected
bulk soil, rhizosphere, and endorhiza samples from nine Cannabis plants of
three strains (Burmese, BooKoo Kush, and Sour Diesel) in Vista, California,
totaling 27 samples. The second experiment collected samples from six plants
of two strains ([[white-widow-cannabis]] and Maui Wowie) from two locations (Vista and
Orange County, California), with triplicate samples from each plant for both
rhizosphere and endorhiza, plus bulk soil samples, totaling 42 samples.

A critical design feature was the use of triplicate samples from each plant,
including pseudoreplicates taken from different roots on the same plant. This
replication strategy allowed the researchers to distinguish between
plant-level and within-plant variation in microbial communities. All samples
were processed using Illumina 16S rRNA gene sequencing of the V4 region,
following the Earth Microbiome Project's standard pipeline.

## Alpha Diversity: Highest in Bulk Soil, Lowest in Endorhiza

One of the most consistent findings across both experiments was the pattern
of alpha diversity across sample types. Bacterial diversity was highest in
bulk soil, showed a slight reduction in the rhizosphere, and then declined
dramatically in the endorhiza. In the second experiment, the Chao1 diversity
index demonstrated this pattern clearly: bulk soil had a mean Chao1 of 4947
(SD = 717), rhizosphere had a mean of 4525 (SD = 542), and endorhiza had a
mean of just 3321 (SD = 420).

The slight reduction from bulk soil to rhizosphere likely reflects the
selective pressure of root exudates, which favor certain microbial groups
while disadvantaging others. The much more dramatic reduction from rhizosphere
to endorhiza reflects the additional barrier of plant cell walls and the
immune responses that further filter which bacteria can successfully colonize
root tissues. Notably, diversity differences between soil types were
significant for bulk soil and rhizosphere but not for endorhiza, suggesting
that the selective bottleneck of root colonization converges endorhiza
communities toward similar diversity levels regardless of starting soil.

The first experiment, with shallower sequencing, recovered the same pattern:
Chao1 was highest in bulk soil (mean = 2010.7, SD = 146.2), slightly lower
in the rhizosphere (mean = 1837.2, SD = 114.0), and lowest in the endorhiza
(mean = 916.1, SD = 161.7). The lower absolute values reflect the reduced
sequencing depth but the relative pattern was identical.

## Beta Diversity: Rhizosphere More Similar to Bulk Soil

Beta diversity analyses revealed that rhizosphere communities are more similar
to bulk soil communities than to [[cannabis-rhizosphere-endorhiza-communities]]. Using both weighted
and [[weighted-vs-unweighted-unifrac-cannabis-strain-microbiome]] distances, beta distances between rhizosphere and bulk
soil were significantly lower than distances between rhizosphere and endorhiza
(unweighted: t = 24.59, p < 0.001; weighted: t = 211.82, p < 0.001). Similarly,
distances between rhizosphere and bulk soil were significantly lower than
distances between bulk soil and endorhiza (unweighted: t = 25.15, p < 0.001;
weighted: t = 211.56, p < 0.001).

However, distances between rhizosphere and endorhiza were not significantly
different from distances between bulk soil and endorhiza for either unweighted
(t = 22.10, p = 0.109) or weighted (t = 22.23, p = 0.078) analyses. This
suggests that the differentiation between rhizosphere and bulk soil is subtle
compared to the large compositional shift that occurs between soil
compartments and the root interior.

## OTU Abundance Correlations Between Sample Types

The relationship between sample types was further quantified by examining
correlations in OTU abundances. Mean abundances of the 51 OTUs that
significantly differentiated sample types were highly correlated between bulk
soil and rhizosphere (Pearson's rho = 0.92), indicating that the general
relative abundance patterns of these discriminating taxa are largely preserved
when moving from bulk soil to the rhizosphere.

The correlation was substantially lower between rhizosphere and Cannabis
endorhiza (Pearson's rho = 0.63), and even lower between bulk soil and
endorhiza (Pearson's rho = 0.42). This declining correlation gradient — from
0.92 to 0.63 to 0.42 — quantitatively captures the progressive
transformation of microbial communities as they move from bulk soil through
the rhizosphere and into the root interior.

## The 51 OTUs Differentiating Sample Types

Fifty-one OTUs were found to significantly differentiate between sample types
(bulk soil, rhizosphere, and endorhiza). Of these, 17 OTUs increased in
abundance within the [[alpha-diversity-gradient-bulk-soil-cannabis-endorhiza]] relative to the rhizosphere. These 17
enriched OTUs were predominantly Proteobacteria, including several from the
Rhizobiales order, consistent with the known copiotrophic and endophytic
tendencies of this group.

The most significant individual OTU difference between sample types was the
dramatic decrease in Acidobacteria from the order iii1-15 in endorhiza
samples, with a Bonferroni-corrected ANOVA p-value of 1.12e-7. This finding
supports the two-tier [[cultivar-cannabis-microbiome-two-tier-selection-model]]'s prediction that oligotrophic
Acidobacteria should be depleted in the nutrient-rich root interior
environment.

## ADONIS Results: Endorhiza Most Distinct

ADONIS permutation tests confirmed that endorhiza communities were the most
distinct sample type. In the pooled analysis across both experiments, endorhiza
samples showed the strongest differentiation from other sample types
(unweighted ADONIS: R² = 0.069, p = 0.001; weighted ADONIS: R² = 0.215, p =
0.001). Rhizosphere samples showed weaker but still significant differentiation
in some tests, while bulk soil samples showed the least distinct clustering.
These results are consistent with the view that the root interior represents
the most strongly filtered microbial niche, while the rhizosphere represents
an intermediate zone where soil and plant influences overlap.

## Implications for Agricultural Practice

These findings have practical implications for [[arbuscular-mycorrhizal-fungi-cannabis-cultivation]]. The
strong influence of soil type on all compartments means that soil management
practices (amendments, composting, irrigation) will affect the entire
root-associated microbiome. The dramatic diversity reduction in the endorhiza
suggests that only a relatively small subset of soil microbes successfully
colonize root tissues, making the identification and promotion of beneficial
endorhiza organisms a promising strategy for improving plant fitness.

## References

- Winston ME, et al. (2014) Understanding Cultivar-Specificity and Soil
  Determinants of the [[cannabis-microbiome-cultivar-specificity]]. PLoS ONE 9(6): e99641.
- Bulgarelli D, Schlaeppi K, Spaepen S, et al. (2013) Structure and Functions
  of the Bacterial Microbiota of Plants. Annu Rev Plant Biol.
