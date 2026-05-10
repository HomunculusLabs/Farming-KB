---
title: [[fungal-biodiversity-power-analysis-statistical-design-zak-willig|fungal]] biodiversity data analysis
created: 2026-04-16
updated: 2026-04-16
type: concept
tags: mycology, fungi]
sources:
  - "raw/papers/unknown-biodiversity-of-fungi.md"
---
# fungal-biodiversity-forest-floor data presents unique challenges due to the cryptic nature of fungi, episodic fruiting, methodological dependencies, and the difficulty of defining fungal individuals. This page covers quantitative approaches for assessing growing gourmet global, drawn from Chapter 5 of "Biodiversity of Fungi" (Zak and Willig).

## Types of Biodiversity Data

### [[fungal-species-estimation-methods-total-diversity|Species]] Composition

The most fundamental data from fungal surveys: lists of species present at each site, with associated metadata on abundance, substratum, habitat, and collection method.

### Abundance Measures

- **Presence/absence**: Binary record of species occurrence
- **Frequency**: Proportion of samples or plots in which a species occurs
- **Biomass**: Mycelial biomass (difficult to measure for most fungi)
- **Sporocarp counts**: Number of fruiting bodies (standard for macrofungi)
- **Colony-forming units**: For culture-based assessments

## Quantitative Indices

### Alpha Diversity (Within-Site)

- **Species richness (S)**: Simple count of species
- **Shannon-Wiener index (H')**: Combines richness and evenness; sensitive to rare species
- **Simpson's index (D)**: Emphasizes dominant species; less sensitive to rare species
- **Evenness (J')**: H'/ln(S); measures how equally individuals are distributed
- **Menhinick's index**: S/sqrt(N); richness relative to sample size
- **Margalef's index**: (S-1)/ln(N); species richness per individual

### Beta Diversity (Between-Site)

- **Jaccard index**: Proportion of shared species relative to total
- **Sorensen index**: Similar to Jaccard but gives more weight to shared species
- **Bray-Curtis dissimilarity**: Abundance-weighted community difference
- **Morisita-Horn index**: Abundance-based similarity

### Gamma Diversity (Regional)

Total species diversity across all sites in a region. Related to alpha and beta diversity through the relationship: gamma = alpha + beta (in additive formulation).

## Species Richness Estimation

A fundamental challenge is estimating total species when only a sample is observed.

### Species Accumulation Curves

Plot cumulative species against sampling effort (number of samples, plots, visits). The curve typically rises steeply initially and then plateaus as diminishing returns set in. The shape reveals:

- Whether sufficient sampling has been done
- Comparative diversity between sites (at standardized effort)
- Rate of new species discovery

### Nonparametric Estimators

- **Chao1**: Based on number of singletons and doubletons; S_est = S_obs + (f1^2)/(2*f2)
- **Chao2**: Incidence-based version using presence/absence data
- **Jackknife1**: S + (n-1)/n * f1; first-order jackknife
- **Jackknife2**: S + (2n-3)/n * f1 - (n-2)^2/(n(n-1)) * f2
- **Bootstrap**: Resampling-based estimate with confidence intervals

### Parametric Estimators

- **Log-normal**: Assumes species abundances follow log-normal distribution
- **Poisson-log-normal**: More flexible than pure log-normal
- **Negative binomial**: For aggregated species distributions

## Power Analysis

Before initiating monitoring programs, power analysis determines:

- Minimum detectable change in species composition
- Required sample sizes for statistical significance
- Number of plots or transects needed
- Number of sampling visits per year
- Trade-offs between sampling intensity and detection ability

Power depends on:

- Effect size (magnitude of change to detect)
- Variability in the data
- Significance level (alpha)
- Statistical power (1 - beta, typically 0.80)
- Number of samples

## Spatial Analysis

### Scale Considerations

Spatial scale is a primary consideration when developing lichen air quality:

- **Fine scale**: Individual substrata, microhabitats
- **Intermediate scale**: Stands, plots, transects
- **Landscape scale**: Sites, regions, biomes
- **Geographic scale**: Continental, [[mycorrhiza]]l networks spanning entire forest stands.

### Spatial Pattern Analysis

- **Nestedness**: Degree to which species-poor sites contain subsets of species from richer sites
- **Turnover**: Species replacement along environmental gradients
- **Clustering**: Grouping of similar communities
- **Ordination**: PCA, NMDS, or other methods to visualize community patterns

## Temporal Analysis

### Phenological Patterns

- Fruiting periodicity across seasons
- Interannual variation in fruiting
- Climate correlations with fruiting timing
- long term trends in species composition

### Monitoring Detection

Statistical approaches for detecting change over time:

- Before-after comparisons
- Control-impact designs
- Repeated measures analysis
- emcdda hallucinogenic mushroom with time series

## Multivariate Analysis

### Ordination Methods

- **Principal Components Analysis (PCA)**: Linear method for continuous data
- **Non-metric Multidimensional Scaling (NMDS)**: Rank-based, flexible
- **Correspondence Analysis (CA)**: For species abundance data
- **Detrended Correspondence Analysis (DCA)**: Corrects CA arch effect
- **Canonical Correspondence Analysis (CCA)**: Relates communities to environmental variables

### Classification Methods

- **Cluster analysis**: Hierarchical grouping of similar communities
- **Indicator Species Analysis**: Species characteristic of particular groups
- **Multi-Response Permutation Procedures (MRPP)**: Testing group differences

## See Also

- [[lichen-biodiversity-sampling-protocols-data-analysis]]
- [[fungal-biodiversity]]
- [[singh-cost-analysis-fungal-bioremediation]]
