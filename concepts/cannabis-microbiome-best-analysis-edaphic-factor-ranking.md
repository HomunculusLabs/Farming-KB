---
title: "BEST Analysis and Edaphic Factor Ranking in Cannabis Microbiome Studies"
source: understanding-cultivar-specificity-cannabis-microbiome.md
topics: [microbiome, cannabis, edaphic-factors, bioenv, statistical-methods, community-ecology]
created: 2026-05-09
---

# BEST Analysis and Edaphic Factor Ranking in Cannabis Microbiome Studies

## Overview

BEST (Best Subset of Environmental Variables with Maximum Rank Correlation with Community Dissimilarities) analysis, implemented as `vegan::bioenv` in R, is a multivariate statistical method used to identify which combination of environmental variables best explains variation in community composition. In the Winston et al. (2014) Cannabis microbiome study, BEST analysis was employed alongside Mantel tests to determine the hierarchical importance of edaphic factors in structuring microbial communities across bulk soil, rhizosphere, and endorhiza compartments of Cannabis plants.

The study examined five Cannabis cultivars (Sour Diesel, Bookoo Kush, Burmese, White Widow, and Maui Wowie) across multiple soil types, providing one of the first comprehensive assessments of how soil chemistry shapes the microbial communities associated with this commercially and medicinally important crop. The BEST analysis complemented the permutational multivariate ANOVA (ADONIS) and UniFrac-based community comparisons by quantifying the relative contributions of individual soil properties.

## Edaphic Factor Hierarchy

Both weighted and unweighted UniFrac analyses identified the same ranking of edaphic factors by their correlation with community beta-diversity. All tested factors showed significant correlations (p = 0.001), but their relative importance differed substantially:

| Rank | Edaphic Factor | Weighted (r-stat) | Unweighted (r-stat) | Interpretation |
|------|---------------|-------------------|---------------------|----------------|
| 1    | Nitrogen      | 0.465             | 0.630               | Primary driver of community membership and structure |
| 2    | Salinity      | 0.437             | 0.620               | Strong ionic/osmotic filtering effect |
| 3    | Carbon        | 0.330             | 0.512               | Organic matter as energy and carbon source |
| 4    | Water Content | 0.281             | 0.466               | Moisture-driven metabolic activity |
| 5    | pH            | 0.221             | 0.292               | Acid-base selection, weakest of tested factors |

### Nitrogen Dominance

Nitrogen emerged as the single most important edaphic variable for structuring microbial communities in the Cannabis root zone. This finding aligns with ecological theory predicting that nitrogen availability is a primary limiting nutrient in most terrestrial ecosystems and therefore acts as a strong selective filter on microbial populations. In the Cannabis microbiome context, nitrogen likely influences:

- The balance between copiotrophic (fast-growing, N-rich) and oligotrophic (slow-growing, N-poor) bacterial taxa
- The relative abundance of nitrogen-fixing bacteria such as Rhizobiales, which were prominent in the endorhiza
- Root exudate composition, as nitrogen status modulates the types and quantities of organic compounds released by roots
- Competition dynamics between bacterial taxa with differing nitrogen utilization strategies

The stronger correlation of nitrogen with unweighted UniFrac (r = 0.630) compared to weighted UniFrac (r = 0.465) suggests that nitrogen availability primarily determines which taxa are present or absent, rather than their relative abundances. This is consistent with nitrogen acting as a threshold filter: below certain concentrations, specific taxa cannot persist; above them, they can colonize and establish populations.

The total nitrogen values in the study ranged from 0.26% (Orange County bulk soil) to 1.51% (Sour Diesel bulk soil), representing a nearly six-fold variation. This wide range provided sufficient gradient for detecting nitrogen effects. In the second experiment, the two soil types showed dramatic nitrogen differences: Mo-Bio soil contained approximately 1.0-1.5% total N while Orange County soil contained only 0.53%, and this difference was the primary driver of PC1 separation in the unweighted analysis (32.06% variance explained).

### Salinity as Secondary Driver

Salinity ranked second in importance, which is notable because the study soils were not extreme saline environments. The soil salinity values ranged from 1.73 to 7.44, representing mild to moderate conditions. Even within this range, salinity significantly structured communities, suggesting that Cannabis microbiomes are sensitive to ionic strength and osmotic potential. Salinity likely affects microbial communities through:

- Direct osmotic stress on bacterial cells, favoring halotolerant taxa
- Modulation of water availability and nutrient diffusion rates
- Alteration of root membrane permeability and exudation patterns
- Changes in soil aggregation and pore structure
- Interactions with other soil chemical properties through ion exchange processes

The salinity values showed a particularly striking difference between the two soils in the second experiment: Mo-Bio soil had salinity values of 5.12-7.44 while Orange County soil was only 1.73. This five-fold difference in salinity likely contributed to the strong soil-type clustering observed in the PCoA plots.

### The Carbon and Water Content Axis

Total organic carbon and water content showed intermediate effects. Carbon availability determines the energy landscape for heterotrophic microbes, while water content governs diffusion rates of both nutrients and signaling molecules. Together with nitrogen, these three variables formed the optimal BEST subset (rho = 0.632), suggesting they capture largely independent dimensions of soil variability.

The total organic carbon values ranged dramatically from 3.02% to 20.0%, with the Orange County soil being an outlier at 20% organic carbon compared to 3.02-5.00% for the Mo-Bio soils. Water content ranged from 0.101 to 0.371, with the Orange County soil again being the outlier at 0.371. This co-variation between carbon and water content in the Orange County soil complicates the interpretation of their individual effects, as high organic matter soils typically retain more water.

### pH: The Weakest but Still Significant Factor

Surprisingly, pH showed the weakest correlation with community structure despite being widely cited as a primary driver of soil microbial communities in the broader literature (Fierer and Jackson 2006). This may reflect the narrow pH range in the study soils (6.63 to 6.94), which varied by less than 0.4 units. Within such a restricted range, pH effects may be subtle compared to the much larger variation in nitrogen (0.26 to 1.51% total N) and carbon (3.02 to 20.0% total organic C).

All study soils were slightly acidic, falling within the range generally considered optimal for both Cannabis cultivation and soil microbial activity. Had the study included strongly acidic (below 5.5) or alkaline (above 7.5) soils, pH would likely have emerged as a more important factor.

## BEST Analysis Methodology

The BEST analysis works through the following procedure:
1. A community distance matrix is computed (UniFrac distances in this study)
2. Environmental distance matrices are computed for each subset of edaphic variables using Euclidean distance
3. Spearman rank correlation is calculated between the community distance matrix and each environmental distance matrix
4. All possible subsets of environmental variables are tested
5. The subset with maximum rank correlation is selected as optimal
6. Permutation tests assess statistical significance

The method was implemented in the QIIME bioinformatics pipeline via the `compare_distance_matrices.py` script, which interfaces with R's `vegan::bioenv` function. The original method was developed by Clarke and Ainsworth (1993) for marine benthic community analysis and has since been widely adopted in microbial ecology.

### Advantages of BEST Over Alternative Approaches

BEST analysis offers several advantages over methods like redundancy analysis (RDA) or canonical correspondence analysis (CCA):
- It does not assume linear relationships between environmental variables and community composition
- It uses rank correlations, making it robust to outliers and non-normal distributions
- It identifies optimal variable subsets, enabling parsimonious models
- It handles collinearity among environmental variables naturally through subset selection

### Interpretation of the Optimal Three-Variable Model

The finding that only three of five tested variables (N, C, Water) formed the optimal subset means that salinity and pH, while individually significant, were redundant in the presence of the other three variables. This suggests that salinity and pH effects on community structure are largely mediated through their influence on nitrogen availability, carbon dynamics, or water relations. Alternatively, salinity and pH may be correlated with one or more of the three optimal variables in these soils, making their independent contribution marginal.

The Spearman rho of 0.632 for the optimal three-variable model indicates that these edaphic factors explain a substantial portion of community variation, but a significant proportion (approximately 37% of rank-ordered variation) remains unexplained. This unexplained variation likely reflects the influence of plant genotype (cultivar effects), unmeasured soil properties (micronutrients, clay mineralogy), biological interactions (predation, competition), and stochastic processes.

## Comparison with Mantel Tests

Mantel tests confirmed that all individual edaphic factors were significantly correlated with community beta-diversity (p = 0.001 for all factors). The Mantel test ranking was consistent with BEST analysis, providing convergent evidence for the edaphic hierarchy. Both weighted and unweighted UniFrac Mantel tests were performed, and the consistency between these approaches — which differ in their treatment of abundance versus presence/absence — strengthens confidence in the findings.

The weighted Mantel tests showed lower correlation coefficients than unweighted tests for all factors. This pattern suggests that edaphic factors have a stronger influence on which taxa are present (composition) than on their relative proportions (structure), consistent with niche-filtering models of community assembly. Under niche filtering, environmental conditions determine the pool of taxa capable of surviving at a site, but within that pool, interspecific interactions and stochastic processes determine relative abundances.

## Implications for Cannabis Cultivation

### Soil Amendment Priorities

The edaphic factor hierarchy directly informs cultivation practices. Since nitrogen is the primary driver of microbial community structure, nitrogen management should be the top priority when attempting to manipulate the Cannabis microbiome through soil amendments. The strong effect of nitrogen on THC concentration, however, confounds simple causal interpretations — higher nitrogen soils in the study also produced plants with higher THC, making it difficult to disentangle microbiome effects from direct nutritional effects on cannabinoid biosynthesis.

### Practical Soil Testing Protocol

For growers seeking to understand or manage their Cannabis microbiome, comprehensive soil testing should prioritize measuring total nitrogen, salinity (EC), total organic carbon, water-holding capacity, and pH. These five parameters capture the vast majority of edaphic influence on microbial community structure based on the BEST analysis results.

### Limitations for Cultivation Application

These findings are based on field-grown plants in California sandy loam soils. Indoor cultivation systems with soilless media, hydroponics, or peat-based substrates may show entirely different factor hierarchies, as the edaphic context is fundamentally different.

## Limitations and Future Directions

The study used only two distinct soil types in the second experiment and minimal edaphic variation in the first experiment, limiting the generalizability of the factor rankings. All soils were sandy loams, and the hierarchy may differ substantially in clay-dominated, silt-dominated, or highly organic soils. Correlation does not establish causation, and edaphic factors may serve as proxies for other unmeasured variables such as micronutrient availability, microbial predator populations, or organic matter quality. Future studies should include a broader range of soil types and employ experimental manipulation of individual edaphic factors to establish causal relationships.

## Cross-References

- [[cannabis-microbiome-two-tier-selection]]
- [[edaphic-factors-structuring-cannabis-microbiome]]
- [[two-tier-selection-model]]
- [[cannabis-endorhiza-microbiome]]
- [[cannabinoid-concentration-endorhiza-microbiome-correlation-cannabis]]
- [[16s-rrna-sequencing-microbiome-analysis]]
