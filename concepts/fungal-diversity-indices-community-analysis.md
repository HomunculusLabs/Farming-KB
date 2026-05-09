---
title: Fungal Diversity Indices and Community Analysis
created: 2026-04-21
updated: 2026-04-21
type: concept
tags: [[mycology, fungi]
sources: [/Users/t3rpz/wiki/raw/papers/unknown-biodiversity-of-fungi.md]
---

# Fungal Diversity Indices and Community Analysis

Quantifying fungal diversity requires appropriate ecological indices that account for both the number of species present (richness) and their relative abundances (evenness). The choice of index affects conclusions about community structure and comparisons between sites.

## Species Richness (S)

The simplest measure — total number of species in a sample or area. However, S depends strongly on sampling effort: more samples generally yield more species. Species accumulation curves plot S against effort (number of samples, individuals counted); ideally they reach an asymptote representing the true species richness of the community.

### Limitations of S
- Strongly dependent on collection effort
- Limited value for comparing communities sampled with different effort
- Effort required to reach asymptote varies by taxon, substratum, habitat, and biome
- Comparisons at non-asymptotic effort levels can be misleading

## Rarefaction

Rarefaction standardizes species richness by estimating the expected number of species for a given number of individuals or samples. Uses the hypergeometric distribution:

E(S) = sum [1 - C(N-ni, n) / C(N, n)]

where N = total individuals, ni = individuals in species i, n = standardized sample size. Rarefaction curves allow fair comparison of species richness among communities sampled with different effort.

## Diversity Indices

Diversity combines species richness and evenness into a single number.

### Simpson's Index (D)
- D = sum(ni(ni-1)) / N(N-1)
- Ranges 0-1; influenced strongly by dominant species
- Reciprocal form (1/D) more commonly used (increases with diversity)
- Appropriate for finite ecological units
- Low sensitivity to sample size

### Shannon Index (H')
- H' = -sum(pi ln pi)
- Based on information theory; most widely used in community ecology
- Measures uncertainty in predicting identity of a randomly chosen individual
- H' = 0 only if single species; maximum when all species equally abundant
- Usually ranges 1.5-3.5; rarely exceeds 4.5
- Exhibits normal distribution across replicate samples — facilitates parametric statistics
- Moderate sensitivity to sample size

### Fisher's Log-Series Alpha
- Alpha parameter of the log-series species-abundance relationship
- Good discriminant ability among sites
- Low sensitivity to sample size
- Less affected by common species than Shannon or Simpson
- Disadvantage: assumes log-series distribution; unaffected by actual evenness

### Other Indices
- **McIntosh's U:** Easy to calculate; good discriminant ability; moderate sample-size sensitivity
- **Berger-Parker d:** Reflects proportional importance of most abundant species; low discriminant ability
- **Hill's N1 and N2:** N1 = exp(H'), N2 = 1/D — unified framework

## Evenness Indices

Evenness measures how equally individuals are distributed among species:

- **Shannon evenness:** E = H' / ln(S)
- **Hill evenness:** E = N2/N1
- **McIntosh evenness:** E = (N-U) / (N - sqrt(NS))

## Jackknifing for Confidence Limits

Jackknifing improves accuracy of diversity estimates and provides confidence intervals:

1. Recalculate diversity while disregarding data from each of n samples
2. Convert each jackknifed estimate to a pseudovalue: VPi = nV - (n-1)VJi
3. Mean of pseudovalues = best diversity estimate
4. Confidence limits: mean +/- t(alpha) * (SD of VPi / sqrt(n))

Requirements: n >= 15 samples; no confidence intervals for smaller datasets.

## Choosing an Index

| Index | Discriminant Ability | Sample Size Sensitivity |
|-------|---------------------|------------------------|
| Shannon | Moderate | Moderate |
| Simpson | Moderate | Low |
| McIntosh U | Good | Moderate |
| Berger-Parker | Poor | Low |
| Fisher alpha | Good | Low |

## Practical Considerations

- Always report sample size along with diversity indices
- Use multiple indices to characterize communities fully
- Report both richness and evenness separately in addition to composite indices
- Use rarefaction when comparing differently-sampled communities
- For fungal communities, culture-based methods may underestimate rare species
- Molecular methods (clone libraries, high-throughput sequencing) reveal higher diversity than cultivation alone

## See Also

- [[fungal-community-ecology]]
- [[soil-fungal-isolation-techniques]]
- [[fungal-species-estimates-taxonomy]]
- [[arbuscular-mycorrhizal-fungal-diversity-patterns-distribution]]
