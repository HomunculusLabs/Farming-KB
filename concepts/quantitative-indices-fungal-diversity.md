---
title: Quantitative Indices Fungal Diversity
source: unknown-biodiversity-of-fungi.md
type: concept
---

# Quantitative Indices of Fungal Diversity

Quantifying fungal diversity requires selecting appropriate indices that capture different aspects of community complexity. Diversity is a multidimensional concept comprising two distinct attributes:

- **[[species-richness-diversity-indices-fungi]]**: the number of species present in a community
- **Species evenness**: the equitability of [[species-abundance-distribution]] within that community

This page covers the major diversity and evenness indices used in [[fungal-ecology]], their mathematical properties, and guidelines for their application.

## Species Richness Measures

Three kinds of species richness can be distinguished, each serving different analytical purposes:

**Numerical species richness** is the number of species in a sample where biomass or the number of individuals has been standardized.

- This is a direct count with no estimation error
- Assumes the sample is sufficiently small for complete enumeration
- Assumes isolation and identification techniques are fully developed

**Species density** is the number of species in a sample where the area, volume, or weight of the sampling unit has been standardized.

- Most [[mycorrhiza-bioassays-ecological-studies]] of fungi actually measure species density
- This is rarely stated explicitly in published studies
- Effects of environmental variation on species density are scale-dependent

**Total species richness (S)** is the cumulative number of unique species across a series of samples from a habitat or substratum.

- This is an estimated value, not a direct count
- The magnitude of S depends on sample size, number, and dispersion
- Limited resources often prevent collecting enough samples to reach asymptotic values

Two well-known richness indices exist but have limitations:

- **Margalef index** (1958): assumes S = kN^0.5, which may not hold
- **Menhinick index** (1964): makes the same assumption about S and N

Because these assumptions often fail, the utility of both indices is limited.

## Rarefaction

When sample sizes are unequal, **rarefaction** provides a robust method for comparing species richness.

The expected number of species in a standardized sample of n individuals is:

```
E(S) = Σ [1 - (N-Ni choose n) / (N choose n)]
```

Where:

- **E(S)** is the expected number of species in the rarified sample
- **n** is the standardized sample size (usually the smallest available)
- **N** is the total number of isolates across all samples
- **Ni** is the number of isolates belonging to species i

The combinatorial term is calculated as:

```
(N choose n) = N! / [n!(N-n)!]
```

Rarefaction allows comparison of species richness among areas or habitats as if they were based on equal sample sizes.

- It facilitates fair comparison across different sampling efforts
- It has been used for fungal [[microfungal-litter-diversity-studies]] (e.g., Polishook et al. 1996)
- It assumes collector's curves are coincident or nonintersecting

## Simpson's Diversity Index

Simpson (1949) proposed the first diversity index used in ecology. It is fundamentally a **dominance measure** because it is strongly influenced by the abundance of the most common species.

The original form applies to completely enumerated ecological units:

```
λ = Σ pi²
```

Where pi is the proportion of individuals in the ith species.

For sampled (finite) ecological units, Simpson developed an unbiased estimator:

```
D = Σ [ni(ni - 1)] / [N(N - 1)]
```

Where ni is the number of individuals of species i and N is the total.

Key characteristics of Simpson's index:

- Ranges from 0 to 1 in the original form
- The reciprocal form (1/D) is most commonly used
- 1/D increases with increasing diversity
- Has **moderate** ability to discriminate among sites
- Has **low** sensitivity to sample size
- Can be tested with parametric (ANOVA) or nonparametric statistics

## Shannon Diversity Index

The Shannon Index (H′) is currently the most popular diversity index in [[yeast-isolation-community-ecology]].

Based on information theory, it measures the average degree of uncertainty in predicting the identity of an individual chosen at random:

```
H′ = -Σ pi · ln(pi)
```

Where pi (ni/N) is the proportional abundance of the ith species and ln is the natural logarithm.

Important properties of H′:

- **H′ = 0** if and only if the sample includes only a single species
- H′ reaches its **maximum** when all species are equally abundant
- Typical values range from **1.5 to 3.5**
- Values rarely exceed **4.5**
- A value exceeding 5.0 would require approximately 10^5 species (May 1975)

Statistical advantages:

- For replicate samples, H′ exhibits a **normal distribution**
- This facilitates parametric statistical comparisons of means and variances
- It has **moderate** discriminatory ability among sites
- It has **moderate** sensitivity to sample size

The index has sometimes incorrectly been referred to as the Shannon-Weaver index (Krebs 1989).

## Additional Diversity Indices

Several other indices complement Simpson and Shannon:

**McIntosh's diversity index (U)**:

```
U = √(Σpi²)
```

- Easy to calculate
- Reflects Euclidean distance from the origin in S-dimensional space
- The dominance form D = (N - U)/(N - √N) is independent of N
- Has **good** discriminatory ability and **moderate** sample size sensitivity

**Berger-Parker index (d)**:

```
d = Nmax / N
