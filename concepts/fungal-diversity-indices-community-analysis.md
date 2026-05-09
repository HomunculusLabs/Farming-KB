---
title: Fungal fungal diversity indices community analysis and rhizosphere-fungal-community-analysis-rrna-rdna
created: 2026-04-21
updated: 2026-04-21
type: concept
tags: [mycology, ecology, biodiversity, statistics]
sources: [/Users/t3rpz/wiki/raw/papers/unknown-biodiversity-of-fungi.md]
---
# Fungal Diversity Indices and Community Analysis

Quantifying fungal diversity requires appropriate
ecological indices that account for both the number of
species present (richness) and their relative abundances
(evenness). The choice of index affects conclusions
about community structure and comparisons between sites.

## Species Richness (S)

The simplest measure is total number of species in a
sample or area. However, S depends strongly on sampling
effort: more samples generally yield more species.

Species accumulation curves plot S against effort
(number of samples or individuals counted); ideally
they reach an asymptote representing the true species
richness of the community being studied.

### Limitations of S

Strongly dependent on collection effort and limited
value for comparing communities sampled with different
intensity. The effort required to reach asymptote
varies by taxon, substratum, habitat, and biome.
Comparisons at non-asymptotic effort levels can be
misleading.

## Rarefaction

Rarefaction standardizes species richness by estimating
the expected number of species for a given number of
individuals or samples. Uses the hypergeometric
distribution to compute the expected count. Rarefaction
curves allow fair comparison of species richness among
communities sampled with different effort.

Modern implementations use interpolation and
extrapolation methods from the iNEXT package in R,
which extends rarefaction to predict diversity at
sample sizes larger than the original data.

## Alpha Diversity Indices

### Simpson Index (D)

D = sum of ni(ni-1) divided by N(N-1). Ranges 0 to 1;
influenced strongly by dominant species. The reciprocal
form (1/D) is more commonly used and increases with
diversity. Appropriate for finite ecological units
with low sensitivity to sample size.

### Shannon Index

H = minus sum of pi times ln(pi). Based on information
theory; the most widely used index in community
ecology. Measures uncertainty in predicting the
identity of a randomly chosen individual.

H equals 0 only if a single species is present;
maximum when all species are equally abundant. Usually
ranges 1.5 to 3.5; rarely exceeds 4.5. The Shannon
index exhibits approximately normal distribution
across replicate samples, facilitating parametric
statistical testing.

### Fisher Log-Series Alpha

The alpha parameter of the log-series species-abundance
relationship provides good discriminant ability among
sites with low sensitivity to sample size. Less affected
by common species than Shannon or Simpson. A limitation
is that it assumes log-series distribution regardless
of actual community structure.

### Other Indices

McIntosh U is easy to calculate with good discriminant
ability and moderate sample-size sensitivity. Berger-
Parker d reflects the proportional importance of the
most abundant species but has poor discriminant ability.
Hill numbers provide a unified framework expressing
diversity in effective number of species units. N1
equals exp of H, and N2 equals 1/D.

## Evenness Indices

Evenness measures how equally individuals are distributed
among species. Shannon evenness is E = H / ln(S).
Hill evenness is E = N2 / N1. McIntosh evenness is
E = (N-U) divided by (N minus sqrt of NS). Low evenness
indicates dominance by one or a few species.

## Beta Diversity and Species Turnover

While alpha diversity describes within-habitat
diversity, beta diversity measures compositional change
between habitats or along environmental gradients. For
[[biodiversity-of-fungi-soil-fungal-communities-agriculture]], beta diversity is often high due to
the strong influence of substrate specificity and
microclimate on [[core-endorhiza-bacterial-community-composition-cannabis]].

Common beta diversity measures include Sorensen index
(based on presence-absence) and Bray-Curtis
dissimilarity (based on abundance). Partitioning beta
diversity into nestedness and turnover components
helps distinguish between species loss and species
replacement processes.

## Ordination Methods

Ordination techniques visualize and analyze community
composition patterns across multiple samples. Principal
Coordinates Analysis and Non-metric Multidimensional
Scaling (NMDS) are widely used for [[air-pollution-fungal-community-responses]]
data derived from sequencing studies.

NMDS is particularly popular because it makes no
assumptions about data distribution and can accommodate
non-linear species responses. Permutational multivariate
analysis of variance (PERMANOVA) tests for significant
differences among predefined groups of samples.

## Jackknifing for Confidence Limits

Jackknifing improves accuracy of diversity estimates
and provides confidence intervals. The procedure
involves recalculating diversity while disregarding
data from each of n samples, converting each jackknifed
estimate to a pseudovalue, and computing the mean and
confidence limits from the pseudovalues.

Requirements include at least 15 samples. Bootstrap
methods provide an alternative approach for generating
## See Also

- [[fungal-community-assembly]]
- [[fungal-species-accumulation-rarefaction-estimators]]
- [[fungal-species-estimates-taxonomy]]
- [[fungal-biodiversity-measurement-methods]]
- [[fungal-species-richness-and-diversity-indices]]
