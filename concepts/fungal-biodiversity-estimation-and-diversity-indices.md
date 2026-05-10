---
title: Fungal Biodiversity Estimation and Diversity Indices
source: Biodiversity of Fungi (Mueller, Bills & Foster, 2004)
tags: [mycology, biodiversity, ecology, statistics, fungal-survey]
created: 2026-05-10
---

# Fungal Biodiversity Estimation and Diversity Indices

## Overview

Fungal biodiversity estimation represents one of the most formidable challenges in
mycology and ecology. Current evidence suggests that only 5-10% of the estimated
1.5 million fungal species on Earth have been formally described and named.
Quantifying fungal diversity demands sophisticated statistical approaches that
account for sampling effort, habitat heterogeneity, and the cryptic, often
microscopic nature of most fungal life forms.

Unlike plants or animals, fungi cannot be trapped, fogged, or collected en masse
in any standardized way. They may produce visible fruiting bodies only at
intervals of many years, and those structures may persist for only a few hours
before decomposing. Other fungi are perennial, such as lichen-forming species
and many polypores, and can be found at any time of year. Still others live
hidden inside plant tissues or arthropod bodies, detectable only through
microscopic examination or molecular methods.

## The Scale of Undiscovered Diversity

The foreword to *Biodiversity of Fungi* notes that at least 74,000 and possibly
as many as 120,000 fungal species have been described to date. David
Hawksworth's 1991 estimate of 1.5 million total species has been widely cited
and generally accepted as a working hypothesis.

Evidence accumulated since that time, especially from studies on tropical plants
and critical molecular investigations, suggests this figure may actually be too
low. We may know at most only about 5% of the fungal species on Earth.

No single site on the planet has been comprehensively surveyed for fungi. In
temperate areas, researchers expect approximately six times as many fungi as
native plants to occur at a site. A comprehensive survey of 200 hectares by
multiple specialists over more than 25 years can yield 2,500 to 3,000 species.

## Species Richness: The Foundation

Species richness is the most widely used parameter for evaluating fungal
biodiversity. It is deceptively simple in concept but complex in practice,
defined as an enumeration of the species associated with a particular sample,
area, habitat, or substratum.

Three distinct kinds of species richness are recognized in the ecological
literature:

**Numerical species richness** is a straightforward count of species present in
a sample. It is measured without error assuming the sample is sufficiently
small and isolation and identification techniques are adequate.

**Species density** expresses the number of species per unit area, volume, or
biomass. Most ecological studies of fungi actually cover species densities as a
consequence of sampling design, though this aspect is rarely stated explicitly.

**Total species richness** is estimated from a series of samples and represents
the asymptotic total for a defined domain. It is the most informative but most
difficult measure to obtain.

## Species-Effort Relationships

The relationship between species richness and sampling effort (A) follows one
of three mathematical models that have been championed in the literature.

In the **Power model** (S = CA^z, Arrhenius 1921) and the **Exponential model**
(S = C + z ln A, Gleason 1922), S increases monotonically with effort. These
models apply when heterogeneous landscapes are sampled and increases in effort
reveal new habitat types within the samples.

The **Logistic model** (S = B/(C + A)^-z, Archibold 1949) predicts that S
eventually reaches a plateau or asymptote. The value of S at this asymptote is
the most accurate estimate of true species richness for a geographically
circumscribed domain.

All three relations are members of the same family of curves (He and Legendre
1996) and figure prominently in island biogeography and conservation biology
theory. The effort required to attain asymptotic values is likely specific to
particular substrata, habitats, or biomes.

## Rarefaction: Standardizing for Sample Size

Rarefaction is a quantitative method that facilitates comparison of species
richness among areas or habitats as if they were based on a standardized sample
size.

The expected number of species in a rarified sample of n individuals is
calculated using combinatorial formulas that account for the abundance of each
species. The approach requires equal sample sizes for direct counts, but when
this is not possible, rarefaction provides a mathematically rigorous
alternative.

This technique was applied by Polishook and colleagues (1996) to compare fungal
diversity from decaying leaves in a Puerto Rican rain forest, demonstrating its
practical utility for tropical mycological surveys.

## Simpson's Diversity Index

Proposed by Simpson in 1949, this was the first diversity index used in
ecology. The index varies from 0 to 1 and is strongly influenced by the
abundance of the most common species, making it a dominance measure.

The original form was restricted to completely enumerated ecological units. For
field sampling of fungi, where complete enumeration is impossible, Simpson
developed an unbiased estimator D based on a sample of N individuals.

Significant differences between Simpson indices can be tested using parametric
analyses such as analysis of variance or regression, or their nonparametric
counterparts. The reciprocal form (1/D) is usually presented, ensuring that the
index increases with increasing diversity.

## Shannon Diversity Index

The Shannon Index (H') is currently the most popular diversity index in
community ecology. Derived from information theory, H' measures the average
degree of uncertainty in predicting the specific identity of an individual
chosen at random from a collection of S species and N individuals.

It has two critical properties. First, H' equals zero if and only if the
sample includes a single species. Second, H' reaches its maximum only when
all species are equally abundant.

Values typically range between 1.5 and 3.5 and rarely exceed 4.5. May (1975)
calculated that a value exceeding 5.0 would require approximately 10^5 species.
When determined for replicate samples of the same ecological unit, H' exhibits
a normal distribution, facilitating parametric statistical evaluation.

## Additional Diversity Measures

**McIntosh's diversity index (U)** reflects the Euclidean distance of the
sample point from the origin of an S-dimensional hypervolume. While easy to
calculate, it is influenced strongly by sample size, limiting its usefulness.

**The Berger-Parker index (d)** reflects the proportional importance of the
most abundant species and is independent of species count, making it a simple
dominance indicator.

**Fisher's log-series alpha** has good discriminant ability and low sensitivity
to sample size, making it particularly useful for fungal community studies,
though it assumes a log-series distribution of individuals among species.

**Hill's diversity numbers (N0, N1, N2)** are perhaps the most ecologically
intuitive indices. Their units are expressed as numbers of species, and they
measure the effective number of species in a community.

## See Also
