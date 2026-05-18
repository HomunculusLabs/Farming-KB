---
title: Fungal Biodiversity Patterns Sampling Indices
source: unknown-biodiversity-of-fungi.md
type: concept
---

# Fungal Biodiversity Patterns and Quantitative Assessment

Assessing fungal biodiversity requires specialized quantitative approaches that account for the unique biology of fungi — particularly their mycelial growth form and clonal life histories. This page covers the conceptual and methodological foundations for measuring fungal diversity, from defining the basic unit of enumeration through community-level indices.

## The Fungal Unit Problem

Most fungi (excluding yeasts and some zoosporic taxa) consist of filaments (hyphae) that grow by apical extension, forming a network called the **mycelium**. Once established, mycelia are capable of essentially unlimited growth and persistence. This **indeterminate body plan** differs fundamentally from the determinate body plans of most animals and many plants, creating a core challenge: how do we define and count a fungal "individual"?

### Three Perspectives on Individuality (Andrews 1991)

The term *individual* can be used in a numerical, genetic, or ecological context depending on the organism and question of interest:

- **Numerical perspective**: An individual is a countable unit of a species (e.g., a mushroom, or a colony on an agar plate). Cooke and Rayner (1984) defined individuals as discrete, functionally independent units, but the level of cellular aggregation fulfilling that criterion for fungi is not clear. Isolates of a single species from disjunct leaf fragments may represent one mycelium or several.
- **Genetic perspective**: An individual is a single cell or collection of cells exhibiting the same genotype — a **genet** (sensu Kays and Harper 1974). For clonal organisms capable of asexual growth, the countable units are **ramets** (Harper 1977). A ramet, although a member of a specific genet, is capable of essentially independent growth.
- **Ecological perspective**: Functional independence within a community context, which may differ from both numerical and genetic definitions.

For animals, the numerical and genetic definitions typically coincide (e.g., a squirrel is one individual by both criteria). For fungi, the number of discrete, countable units is *not* the same as the number of genets. Sporocarps on a forest floor can represent multiple ramets of a single genet or ramets from multiple genets. Only **molecular or isozymic analyses** of sporocarps can untangle the genetic structure of such a population and enable biodiversity quantification comparable to that for animals and plants. Because this approach is not generally practical, a clearly stated **operational definition of "individual"** — relevant to the taxon of interest — must be provided to facilitate unambiguous comparisons among ecosystems.

## Frequency of Occurrence

The simplest metric for characterizing fungal communities is **frequency of occurrence**, calculated as:

```
Frequency (%) = (sample units with species / total sample units examined) × 100
```

For example, if 50 1-mm² particles of organic soil matter are plated onto agar, the maximum frequency for any species is 100%. Note that the sum of frequencies for all species can exceed 100% when multiple species occur in the same sample unit.

### Relative and Standardized Frequency

**Relative frequency** standardizes frequencies so they sum to 100%:

```
Relative Frequency (%) = (number of isolates for each species / total number of isolates) × 100
```

Dividing each species' frequency by the sum of all frequencies yields a **standardized frequency**, a straightforward normalization useful when comparing across communities with different total counts. Investigators should report mean frequency and standard error for each species when sampling is replicated.

## Sampling Design: Plot Size and Shape

The choice of sampling plot size and shape significantly influences estimates of [[fungal-diversity-and-ecosystem-function]] density. Plot dimensions should balance practicality, a priori knowledge of the system, and the need to capture relevant spatial heterogeneity.

### Circular vs. Rectangular Quadrats

- **Circular plots** are delineated easily with a center pole and radius line, and they minimize edge effects that can bias density estimates.
- **Rectangular quadrats** provide more accurate estimates of species composition than circular or square plots of equal area (Krebs 1989). They are especially suited for assessing [[fungal-adaptations-environmental-gradients]] when the long axis is oriented parallel to the underlying gradient (Cox 1996). Rectangular quadrats are more effective at detecting **habitat heterogeneity** and accurately estimating the patchy distribution of organisms, since a long quadrat potentially crosses more habitat patches than a circular plot of the same area.

## Collector's Curves and Species-Effort Relationships

A **collector's curve** (species accumulation curve) plots cumulative species richness against sampling effort (number of samples, area, or volume). The total number of species increases with effort but eventually reaches a **plateau (asymptote)** if the domain is geographically circumscribed and sampling is random. The effort required to reach the plateau depends on environmental heterogeneity and the dispersion patterns and [[macrofungal-fruiting-phenology-climate-variability]] of the focal taxa.

### Three Species-Effort Models

All three models below are members of the same family of curves (He and Legendre 1996):

1. **Power model** (Arrhenius 1921): `S = CA^z` — Species richness increases monotonically with effort; no asymptote predicted. Most appropriate for heterogeneous landscapes where increased effort captures new habitat types.
2. **Exponential model** (Gleason 1922, 1925): `S = C + z ln A` — Also monotonically increasing without asymptote. Figures prominently in island biogeography and [[fungal-conservation-biology]].
3. **Logistic model** (Archibold 1949): `S = B/(C + A)^-z` — Predicts that S eventually reaches an **asymptote**, the value of which is an accurate estimate of the **true species richness** of the domain of interest. Most appropriate for geographically circumscribed domains with random sampling.

Comparing species richness at effort levels below the asymptote can lead to spurious conclusions.

## Three Kinds of Species Richness

| Type | Definition | Error |
|------|-----------|-------|
| **Numerical species richness** | Number of species in a sample where biomass or number of individuals is standardized | None (with complete enumeration) |
| **Species density** | Number of species in a sample where area, volume, or weight is standardized | None (with complete enumeration) |
| **Total species richness** | Cumulative number of species from a series of samples; estimated, not directly measured | Must be estimated (e.g., via asymptotic models) |

The effects of environmental variation on species density and numerical species richness are **scale-dependent** — the effect may not be the same for samples differing in area, volume, weight, biomass, or number of individuals (Waide et al. 1999; Gross et al. 2000). This scale-dependence occurs because different causal mechanisms operate at different spatial scales. Future research should always include an explicit definition of scale and the attribute of richness being evaluated.

## Rarefaction Analysis

When sample sizes are unequal, **rarefaction** (Magurran 1988) allows comparison of species richness as if all samples were based on a standardized number of individuals. The expected number of species in a rarified sample of *n* individuals is:

```
E(S) = Σ [1 - ((N - Ni choose n) / (N choose n))]
```

Where:
- **E(S)** = expected number of species in the rarified sample
- **n** = standardized (rarified) sample size (usually the smallest available sample)
- **N** = total number of isolates (individuals) across all samples
- **Ni** = number of isolates belonging to the *i*th species

Rarefaction has been used to determine the expected number of fungal species from decaying leaves in Puerto Rican rain forests (Polishook et al. 1996).

## Diversity Indices

Diversity comprises two attributes: **species richness** and **species evenness**. Multiple indices capture different aspects of [[acidifying-pollutants-mycorrhizal-community-structure]]:

### Simpson's Index (D)

A **dominance measure** ranging from 0 to 1, influenced strongly by the abundance of the most common species. For finite ecological units:

```
D = Σ ni(ni - 1) / N(N - 1)
```

Where *ni* is the number of individuals in species *i* and *N* is the total. The reciprocal (1/D) is usually presented so the index increases with diversity. Simpson's D has low sensitivity to sample size (Table 5.2).

### Shannon Index (H′)

Derived from **information theory** (Shannon and Weaver 1949), H′ measures the average uncertainty in predicting the identity of a randomly chosen individual:

```
H′ = -Σ pi ln pi
```

Where *pi* = *ni*/*N* (proportional abundance). H′ = 0 if only one species is present and reaches its maximum when all species are equally abundant. Values typically range from 1.5 to 3.5 and rarely exceed 4.5 (Margalef 1972). H′ is normally distributed across replicate samples, facilitating parametric statistical comparisons.

### Additional Indices

| Index | Formula | Characteristics |
|-------|---------|----------------|
| **McIntosh U** | U = √(Σ pi²) | Euclidean distance from origin in S-dimensional hypervolume; sensitive to sample size |
| **Berger-Parker d** | d = Nmax / N | Proportional importance of most abundant species; independent of S, low sample-size sensitivity |
| **Fisher's log-series α** | α = N(1-x)/x | Good discriminant ability, low sample-size sensitivity; unaffected by evenness (assumes log-series distribution) |
| **Hill's N1** | N1 = e^H′ | Effective number of abundant species (numbers of species) |
| **Hill's N2** | N2 = 1/D | Effective number of very abundant species |

## Evenness Indices

Evenness quantifies how equally individuals are distributed among species:

- **Shannon evenness**: `E = H′ / ln(S)` — where S is species richness
- **Hill evenness**: `E = N2 / N1` — ratio of Simpson to Shannon diversity
- **McIntosh's evenness**: `E = (N - U) / (N - √(N/S))` — where N is total isolates, U is McIntosh diversity

## Jackknifing for Confidence Limits

**Jackknifing** (Zahl 1977) improves accuracy and provides confidence limits for any diversity index. The method recalculates overall diversity while systematically disregarding each of *n* constituent samples, producing *n* jackknifed values (*VJi*). Each is converted to a **pseudovalue**:

```
VPi = (n × V) - [(n - 1) × VJi]
```

Where *n* is the number of samples and *V* is the diversity index based on all samples. The mean of pseudovalues is the best diversity estimate. Confidence limits are:
## See Also

- [[mycology]]
- [[spore]]
- [[estimating-fungal-diversity-living-plants]]
- [[microfungal-inventory-sampling-culture-protocols]]
