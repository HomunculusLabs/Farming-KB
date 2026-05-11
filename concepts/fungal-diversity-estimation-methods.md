---
title: Fungal Diversity Estimation Methods
created: 2026-04-16
updated: 2026-04-16
type: concept
tags: [[mycology]], fungi]
sources: []
---

# Fungal Diversity Estimation Methods
Estimating fungal species richness and diversity from field samples requires
specialized quantitative methods. Because most fungal species cannot be directly
counted and complete inventories are rarely achievable, researchers rely on
statistical approaches to estimate [[fungal-species-estimation-methods-total-diversity]] from partial sampling.

## The Challenge of Estimating Fungal Diversity

Fungal diversity estimation presents unique difficulties:
- Many fungi are known only from [[environmental-dna-fungal-discovery]] and cannot be cultured
- Sporocarp production is seasonal and ephemeral, causing underestimation
- Detectability varies enormously among species and habitats
- Sampling effort is limited by time, cost, and taxonomic expertise
- Species accumulation curves often fail to reach asymptotes, indicating
  incomplete sampling

## Species Richness Concepts

Three distinct concepts of species richness must be distinguished when
estimating fungal diversity:

- **Numerical species richness**: the number of species in a sample
  standardized by the number of individuals or isolates
- **Species density**: the number of species in a sample standardized by
  area, volume, or weight of the sampling unit
- **Total species richness**: the cumulative number of species in a series
  of samples from a habitat or substratum
The first two are measured without error (assuming complete enumeration of taxa
in the sample), whereas total species richness must be estimated from a series
of samples and is always an underestimate.

## Collector's Curves and Species-Effort Relationships

Collector's curves (also called species-accumulation curves) plot cumulative
species richness against sampling effort. Three mathematical models describe
how richness increases with effort:

- **Logistic model**: S reaches a plateau (asymptote), providing an accurate
  estimate of total richness for a bounded domain
- **Power model**: S increases monotonically without plateau (S = CA^z)
- **Exponential model**: S increases monotonically (S = C + z ln A)

The logistic model is most appropriate for geographically bounded areas with
random sampling, whereas power and exponential models better describe sampling
across heterogeneous landscapes.

## Rarefaction

Rarefaction is a quantitative method that facilitates comparison of species
richness among areas or habitats based on a standardized sample size. When
samples differ in the number of individuals or isolates, rarefaction calculates
the expected number of species for a standardized sample of n individuals:
E(S) = sum of [1 - (N-Ni choose n) / (N choose n)]
where E(S) is the expected species richness, n is the standardized sample size
(usually the smallest available), N is the total number of individuals, and Ni
is the number of individuals in species i.
Polishook and colleagues (1996) used rarefaction to determine the expected
number of fungal species from decaying leaves in a Puerto Rican [[stamets-mycorrhizal-decline-europe-acid-rain-forest-health]].

## Diversity Indices

### Shannon Index (H')

The most widely used diversity index in community ecology. H' measures the
average uncertainty in predicting the identity of a randomly chosen individual.
Values typically range from 1.5 to 3.5 and rarely exceed 4.5. The Shannon
index exhibits a normal distribution across replicate samples, facilitating
parametric statistical comparisons. See [[fungal-species-richness-and-diversity-indices]]
for detailed methodology.

### Simpson's Index (D)

A dominance measure strongly influenced by the most common species. The
reciprocal form (1/D) is usually presented to ensure the index increases with
increasing diversity. Significant differences can be tested using parametric
or nonparametric analyses.

### Fisher's Log-Series Alpha

An index with good discriminant ability and low sensitivity to sample size.
However, it is unaffected by the actual distribution of individuals among
