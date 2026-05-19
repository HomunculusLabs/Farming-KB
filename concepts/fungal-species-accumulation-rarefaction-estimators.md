---
title: "Fungal Species Accumulation Rarefaction Estimators"
tags:
  - concept
---

## Fungal Species Accumulation Curves and Rarefaction Estimators

## Overview

Species accumulation curves (also called collector's curves) and rarefaction are fundamental quantitative tools in [[mycorrhizal-fungi-fruit-trees]] intermittently and many species are cryptic, achieving a complete inventory requires understanding the relationship between sampling effort and species discovery.

## The Species Accumulation Curve

A species accumulation curve plots the cumulative number of unique species detected against increasing sampling effort, where effort can be measured as the number of samples, the number of individual specimens collected, or the area or volume of substrata examined.

### Mathematical Models

Three mathematical relationships describe how cumulative species richness (S) increases with effort (A):

1. **Power function** (Arrhenius 1921): S = CA^z — species increase monotonically without plateau. Most appropriate for heterogeneous landscapes where increased effort captures additional habitat heterogeneity.

2. **Exponential function** (Gleason 1922, 1925): S = C + z ln A — also increases monotonically. Suitable for landscapes with diverse microhabitats.

3. **Logistic function** (Archibold 1949): S = B/(C + A)^-z — predicts that S eventually reaches a plateau (asymptote), which represents the true species richness of the sampled domain. Most appropriate for geographically bounded areas with random sampling.

All three are members of the same family of curves (He and Legendre 1996). The logistic model is most useful for fungal surveys because it predicts when sampling has been sufficient.

### Practical Implications for Fungal Surveys

The effort required to reach asymptotic values is specific to particular substrata, habitats, and biomes. For macrofungi, up to 8–12 years of sampling may be required to approach an asymptote at a single site. This extreme requirement reflects:

- Many species fruit only 1 year out of 4 or more
- Maximum richness occurs during brief periods that differ among years
- Only 5–20% of ectomycorrhizal species may fruit in 2 consecutive years
- In a 21-year Swiss study, species richness estimators never stabilized

Comparisons of species richness at effort levels below the asymptote can lead to spurious conclusions about differences between sites.

## Types of Species Richness

Three distinct measures must be distinguished:

1. **Numerical species richness**: Number of species in a sample where the number of individuals (isolates) has been standardized.

2. **Species density**: Number of species in a sample where the area, volume, or weight of the sampling unit has been standardized.

3. **Total species richness**: Cumulative number of species based on a series of samples from a habitat or substratum. This is always an estimate.

The first two are measured without error (assuming complete enumeration), but their relationship to environmental variables is scale-dependent — the effect of environmental variation may not be the same for samples that differ in area, volume, or number of individuals.

## Rarefaction

Rarefaction is a quantitative method that facilitates comparison of species richness among areas or habitats as if they were based on a standardized sample size. When sample sizes are not equal (as is common in fungal surveys), rarefaction allows meaningful cross-site comparisons.

### The Rarefaction Formula

The expected number of species in a rarified sample of n individuals from a total collection of N individuals is:

E(S) = Σ[1 - (C(N-Ni,n) / C(N,n))]

Where:
- E(S) is the expected number of species in the rarified sample
- n is the standardized sample size (usually the smallest sample available)
- N is the total number of isolates recorded across all samples
- Ni is the number of isolates in the ith species
- C represents the combinatorial function (factorials)

### Applications

Polishook and colleagues (1996) used rarefaction to determine the expected number of fungi from decaying leaves in a Puerto Rican rain forest. The method is particularly valuable when sampling effort differs markedly between sites — a common situation in mycological inventories.

## Species Richness Indices

Several indices attempt to estimate total richness independent of sample number:

- **Margalef index** (1958): Assumes S = kn^0.5, where k is a constant
- **Menhinick index** (1964): Similar proportional assumption

Both make specific assumptions about the relationship between species number (S) and total individuals (n) that may not hold for [[beta-diversity-root-soil-compartments-cannabis]]**: Species turnover between habitats or along environmental gradients
- **[[alpha-beta-diversity-cannabis-root-microbiomes]] (turnover rate). For lichens in Pacific Northwest forests, cyanolichens, alectorioid lichens, and green-alga foliose lichens respond differently to canopy position, forest age, tree density, and habitat heterogeneity, demonstrating the importance of partitioning data by functional or morphological groups.

## Recommendations for Fungal Surveys

1. Always generate species accumulation curves to determine whether sampling effort has been sufficient
2. Use rarefaction when comparing sites with unequal sample sizes
3. Apply non-parametric richness estimators (Chao1, ACE, jackknife) to estimate total richness
4. Report multiple [[dom]]
- [[lichens]]
- [[mycology]]
## Practical Applications
The principles discussed here have direct applications in agricultural systems, ecological restoration, and sustainable resource management.
Practitioners have demonstrated successful implementation across diverse climates and soil conditions.
Adaptation to local conditions and careful observation remain central to effective application.
Field trials provide essential data for validating theoretical approaches and refining methodologies.

## Research Directions
Current research explores the intersections between traditional knowledge and modern scientific understanding.
Comparative studies across different bioregions provide valuable insights into generalizable principles.
Long-term monitoring and documentation continue to build the evidence base for these approaches.
Collaborative research networks facilitate knowledge exchange and accelerate innovation.
Peer-reviewed publications and practitioner reports contribute complementary perspectives.

## Key Considerations
Context-specific implementation requires attention to local ecology, climate patterns, and community needs.
Integration with existing systems often yields better results than complete replacement strategies.
Monitoring and adaptive management are essential for long-term success and continuous improvement.

## Integration Strategies
Successful implementation often draws on multiple complementary approaches working in concert.
Scale-appropriate solutions range from backyard gardens to broadacre agricultural systems.
Knowledge sharing between practitioners accelerates collective learning and refinement of methods.
Regional networks and demonstration sites play crucial roles in technology transfer.

## Implementation Notes
Start with small-scale trials before expanding to larger operations.
Maintain detailed records of conditions, inputs, and outcomes for iterative refinement.
Regular review and adjustment of strategies based on observed results ensures continuous improvement.
## Practical Considerations
Successful implementation requires attention to detail and adaptation to local conditions.
Field experience and systematic observation remain the most reliable guides for practitioners.
Documentation of results enables continuous improvement and knowledge sharing.

## Future Directions
Emerging research continues to validate and refine traditional approaches.
Integration with modern technology offers new possibilities for monitoring and optimization.
Collaborative networks facilitate rapid dissemination of innovations and best practices.
