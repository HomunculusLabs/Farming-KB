---
title: Fungal Biodiversity Data Analysis
created: 2026-04-16
updated: 2026-04-16
type: concept
tags: [[mycology]], fungi]
sources:
  - "raw/papers/unknown-biodiversity-of-fungi.md"
---
# fungal-biodiversity-forest-floor data presents unique challenges due to the cryptic nature of fungi, episodic fruiting, methodological dependencies, and the difficulty of defining fungal individuals. This page covers quantitative approaches for assessing growing gourmet global, drawn from Chapter 5 of "Biodiversity of Fungi" (Zak and Willig).

## Types of Biodiversity Data

### [[fungal-species-estimation-methods-total-diversity]] Composition

The most fundamental data from fungal surveys: lists of species present at each site, with associated metadata on abundance, substratum, habitat, and collection method.

### Abundance Measures

- **Presence/absence**: Binary record of species occurrence
- **Frequency**: Proportion of samples or plots in which a species occurs
- **Biomass**: [[stamets-forest-mycelial-biomass-topsoil-douglas-fir]] (difficult to measure for most fungi)
- **Sporocarp counts**: Number [[bloomfield-asterophora-and-mycoparasites-of-fruiting-bodies]] (standard for macrofungi)
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

## Practical Applications

The principles and techniques discussed here have wide-ranging applications
across multiple disciplines and contexts. Practitioners and researchers
continue to explore new ways to integrate these concepts into modern practice,
adapting traditional knowledge to contemporary challenges and opportunities.

## Key Considerations

Several important factors influence the effectiveness and outcomes described
in this topic. Understanding these considerations helps practitioners make
informed decisions and avoid common pitfalls. Environmental conditions,
timing, and material selection all play critical roles.

## Historical Context

The historical development of this subject reflects centuries of accumulated
knowledge and practical experience. From traditional methods passed down
through generations to modern scientific approaches, the evolution continues
to inform current best practices and research directions.

## Common Challenges

Practitioners frequently encounter several challenges when working with
these concepts. Climate variability, resource limitations, and knowledge
gaps can all affect outcomes. Addressing these challenges requires patience,
observation, and a willingness to adapt approaches based on results.

## See Also
- [[dom]]
- [[det]]
- [[fungal-biodiversity-power-analysis-statistical-design-zak-willig]]
- [[lichen-biodiversity-sampling-protocols-data-analysis]]
- [[fungal-biodiversity-built-environments-indoor-mycobiome]]
