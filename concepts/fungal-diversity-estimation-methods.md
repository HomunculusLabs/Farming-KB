---
title: Fungal Diversity Estimation Methods
created: 2026-04-16
updated: 2026-04-16
type: concept
tags: [mycology, fungi]
sources: []
---
# Fungal Diversity Estimation Methods

Estimating fungal species richness and diversity from field samples requires specialized quantitative methods. Because most fungal species cannot be directly counted and complete inventories are rarely achievable, researchers rely on statistical approaches to estimate total diversity from partial sampling.

## The Challenge of Estimating Fungal Diversity

Fungal diversity estimation presents unique difficulties:
- Many fungi are known only from environmental DNA and cannot be cultured
- Sporocarp production is seasonal and ephemeral, causing underestimation
- Detectability varies enormously among species and habitats
- Sampling effort is limited by time, cost, and taxonomic expertise
- Species accumulation curves often fail to reach asymptotes, indicating incomplete sampling

## Species Richness Concepts

Three distinct concepts of species richness must be distinguished when estimating fungal diversity:
- **Numerical species richness**: the number of species in a sample standardized by the number of individuals or isolates
- **Species density**: the number of species in a sample standardized by area, volume, or weight of the sampling unit
- **Total species richness**: the cumulative number of species in a series of samples from a habitat or substratum

The first two are measured without error (assuming complete enumeration of taxa in the sample), whereas total species richness must be estimated from a series of samples and is always an underestimate.

## Collector's Curves and Species-Effort Relationships

Collector's curves (also called species-accumulation curves) plot cumulative species richness against sampling effort. Three mathematical models describe how richness increases with effort:
- **Logistic model**: S reaches a plateau (asymptote), providing an accurate estimate of total richness for a bounded domain
- **Power model**: S increases monotonically without plateau (S = CA^z)
- **Exponential model**: S increases monotonically (S = C + z ln A)

The logistic model is most appropriate for geographically bounded areas with random sampling, whereas power and exponential models better describe sampling across heterogeneous landscapes.

## Rarefaction

Rarefaction is a quantitative method that facilitates comparison of species richness among areas or habitats based on a standardized sample size. When samples differ in the number of individuals or isolates, rarefaction calculates the expected number of species for a standardized sample of n individuals:

E(S) = sum of [1 - (N-Ni choose n) / (N choose n)]

where E(S) is the expected species richness, n is the standardized sample size (usually the smallest available), N is the total number of individuals, and Ni is the number of individuals in species i. Polishook and colleagues (1996) used rarefaction to determine the expected number of fungal species from decaying leaves in a Puerto Rican rain forest.

## Diversity Indices

### Shannon Index (H')

The most widely used diversity index in community ecology. H' measures the average uncertainty in predicting the identity of a randomly chosen individual. Values typically range from 1.5 to 3.5 and rarely exceed 4.5. The Shannon index exhibits a normal distribution across replicate samples, facilitating parametric statistical comparisons.

### Simpson's Index (D)

A dominance measure strongly influenced by the most common species. The reciprocal form (1/D) is usually presented to ensure the index increases with increasing diversity. Significant differences can be tested using parametric or nonparametric analyses.

### Fisher's Log-Series Alpha

An index with good discriminant ability and low sensitivity to sample size. However, it is unaffected by the actual distribution of individuals among species (evenness), assuming a log-series distribution. Two communities with the same N and S but different evenness will have the same alpha value.

### Hill's Numbers (N0, N1, N2)

Perhaps the easiest to interpret ecologically, with units of effective number of species:
- N0 = total species count regardless of abundance
- N1 = e^H' (effective number of abundant species)
- N2 = 1/D (effective number of very abundant species)

## Jackknifing for Confidence Limits

The jackknife technique improves accuracy of diversity estimates and provides confidence limits. It involves recalculating overall diversity while disregarding data from each of n constituent samples, creating jackknifed pseudovalues. Confidence limits should not be calculated for datasets with fewer than 15 samples.

## Species-Area Relationships

The relationship between species number and area sampled is fundamental to fungal biogeography. The Arrhenius power law (S = CA^z) and Gleason exponential model (S = C + z ln A) are widely used. The slope parameter z typically ranges from 0.2 to 0.35 for fungi, and is influenced by habitat heterogeneity, dispersal ability, and spatial aggregation of species.

## Recommendations for Fungal Diversity Studies

Zak and Willig (2004) recommend that future research always include an explicit definition of scale and the attribute of richness being evaluated. The effects of environmental variation on species density and numerical species richness are scale-dependent, making standardized protocols essential for meaningful comparisons.

## Related Topics

- [[fungal-monitoring-long-term-studies]]
- [[fungal-metagenomics]]
- [[fungal-community-assembly]]
- [[culturing-culture-independent-fungi]]
- [[fungal-biodiversity-sampling-design]]

## References

- Biodiversity of Fungi (2004), Chapter 5: Fungal Biodiversity Patterns
- Colwell, R.K. and Coddington, J.A. 1994. Estimating terrestrial biodiversity
- Magurran, A.E. 1988. Ecological Diversity and Its Measurement
- Ludwig, J.A. and Reynolds, J.F. 1988. Statistical Ecology
- [[fungal-species-richness-and-diversity-indices]]
- [[fungal-species-estimation-methods-total-diversity]]
- [[arbuscular-mycorrhizal-fungal-diversity-patterns-distribution]]
