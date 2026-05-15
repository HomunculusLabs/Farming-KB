---
title: Fungal Biodiversity Indices
source: unknown-biodiversity-of-fungi.md
type: concept
---

# Fungal Biodiversity Indices

Quantifying fungal biodiversity requires robust indices that capture different dimensions of community structure. This page covers the major richness, diversity, and evenness indices used in fungal ecology, their mathematical foundations, and practical considerations for their application.

## Species Richness

Species richness is the most widely used parameter for evaluating fungal biodiversity, but it is deceptively nuanced. Three distinct kinds of species richness are recognized:

1. **Numerical species richness** — the number of species in a sample where the number of individuals has been standardized.
2. **Species density** — the number of species where the area, volume, or weight of the sampling unit has been standardized. Most ecological studies of fungi actually measure species density, though this is rarely stated explicitly.
3. **Total species richness** — the cumulative number of species based on a series of samples from a habitat or substratum.

Numerical species richness and species density are measured without error (assuming complete enumeration), whereas total species richness must be estimated from a series of samples. A critical caveat is that the effects of environmental variation on species density and numerical richness are **scale-dependent** — the importance of different causal mechanisms depends on the spatial scale at which data are collected.

## Species-Effort Curves

The relationship between cumulative species richness (S) and sampling effort (A — number, area, or volume of samples) has been modeled by three mathematical functions, all members of the same family of curves:

- **Power model** (Arrhenius 1921): S = CA^z — richness increases monotonically with effort; most appropriate for heterogeneous landscapes where increased effort captures additional habitat heterogeneity.
- **Exponential model** (Gleason 1922, 1925): S = C + z·ln(A) — also monotonically increasing; prominent in island biogeography and conservation biology.
- **Logistic model** (Archibold 1949): S = B/(C + A)^-z — unlike the other two, predicts that S eventually reaches a plateau (asymptote). The value at the asymptote is an accurate estimate of true species richness. Most appropriate when the domain is geographically circumscribed and random sampling occurs within its borders.

Comparisons of species richness at effort levels not associated with the asymptote can lead to **spurious conclusions**. The effort required to reach asymptotic values is specific to particular substrata, habitats, or biomes.

## Rarefaction

When sample sizes are unequal, **rarefaction** facilitates comparison of species richness among areas or habitats as if they were based on a standardized sample size. The expected number of species in a rarified sample of n individuals is:

```
E(S) = Σ [1 - ((N - Ni) choose n) / (N choose n)]
```

Where E(S) is the expected species count, n is the standardized (rarified) sample size (usually the smallest sample available), N is the total number of isolates recorded, and Ni is the number of isolates of the ith species. The combinatorial term uses factorials: (N choose n) = N! / [n!(N−n)!]. Rarefaction assumes that collector's curves for treatments are coincident or nonintersecting.

## Diversity Indices

Diversity comprises two distinct attributes: **species richness** and **species evenness** (the equitability of abundance distribution among species).

### Simpson's Index

The first diversity index used in ecology (Simpson 1949). It varies from 0 to 1 and is a **dominance measure** strongly influenced by the most common species:

- **λ** (lambda) = Σpi² — for infinitely large ecological units, where pi is the proportional abundance of the ith species.
- **D** = Σ[ni(ni−1)] / [N(N−1)] — unbiased estimator for finite ecological units, where ni is individuals of species i and N is total individuals. The reciprocal form (1/D) is typically presented so the index increases with diversity.

### Shannon Index (H')

Currently the most popular index in community ecology, derived from information theory. H' = −Σpi·ln(pi), where pi = ni/N. It measures the average degree of uncertainty in predicting the identity of a randomly chosen individual. Key properties:

- H' = 0 if and only if the sample includes a single species
- H' reaches its maximum only when all species are equally abundant
- Typical magnitude: 1.5–3.5; rarely exceeds 4.5; exceeding 5.0 would require ~10⁵ species
- Replicate samples of the same unit exhibit a **normal distribution**, facilitating parametric statistics (ANOVA, regression)

### Other Diversity Indices

| Index | Formula/Description | Key Characteristic |
|-------|-------------------|--------------------|
| **McIntosh U** | U = √(Σpi²) | Easy to calculate, reflects dominance |
| **McIntosh D** | D = (N−U)/(N−√N) | Independent of N |
| **Berger-Parker d** | d = Nmax/N | Nmax = individuals in most abundant species; reciprocal most commonly used |
| **Fisher's α** | α = N(1−x)/x | Log-series parameter; solved iteratively |
| **Hill N1** | N1 = e^H' | Hill's diversity number based on Shannon |
| **Hill N2** | N2 = 1/D | Hill's diversity number based on Simpson |
| **Brillouin HB** | Complete enumeration | Not recommended for fungal studies — restricted conditions, cannot use biomass/cover data |

## Evenness Indices

Evenness measures how equally individuals are distributed among species:

- **Shannon evenness**: E = H' / ln(S)
- **Hill evenness**: E = N2 / N1 (ratio of Simpson to Shannon diversity numbers)
- **McIntosh evenness**: E = (N − U) / (N − N√S)

## Practical Considerations

### Index Selection

| Index | Discrimination Among Sites | Sensitivity to Sample Size |
|-------|---------------------------|---------------------------|
| Shannon | Moderate | Moderate |
| Simpson | Moderate | Low |
| McIntosh (U) | Good | Moderate |
| McIntosh (D) | Poor | Moderate |
| Berger-Parker | Poor | Low |
| Fisher's α | Good | Low |

### Jackknifing

The **jackknife technique** (Zahl 1977) can improve the accuracy of any diversity index by generating pseudovalues for confidence limits. It makes no assumptions about the underlying distribution and allows hypothesis testing. This is particularly valuable when sample sizes are small or when comparing diversity across habitats with different sampling intensities.

### Recommendations for Fungal Studies

1. Always include an **explicit definition of scale** and the attribute of richness being evaluated
2. Use **collector's curves** to determine adequate sampling effort before comparing richness
3. The Shannon index is recommended as a primary diversity measure due to its statistical properties and normal distribution in replicates
4. **Rarefaction** should be used when sample sizes are unequal
5. **Jackknifing** provides confidence intervals for hypothesis testing
6. Be cautious comparing species richness at effort levels below the asymptote of the species-effort curve

## References

- Andrews JH. 1991. Comparative ecology of microorganisms and macroorganisms. Springer.
- Arrhenius O. 1921. Species and area. J Ecol 9:95–99.
- Gleason HA. 1922. On the relation between species and area. Ecology 3:158–162.
- Ludwig JA, Reynolds JF. 1988. Statistical Ecology. Wiley.
- Magurran AE. 1988. Ecological Diversity and its Measurement. Princeton Univ Press.
- Simpson EH. 1949. Measurement of diversity. Nature 163:688.
- Zak JC, Willig MR. Fungal biodiversity patterns. In: Biodiversity of Fungi.

## See Also

- [[mycology]]
- [[mycorrhiza]]
- [[basidiomycota]]
- [[ascomycota]]
- [[kingdom-fungi]]
