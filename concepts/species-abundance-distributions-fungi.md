---
title: Species Abundance Distributions Fungi
source: unknown-biodiversity-of-fungi.md
type: concept
---

# Species Abundance Distributions in Fungal Communities

Species abundance distributions (SADs) describe how individuals are partitioned among species within a fungal community. They are fundamental to understanding [[fungal-biodiversity]], [[acidifying-pollutants-mycorrhizal-community-structure]], and the ecological processes shaping assemblages across habitats ranging from forest soils to leaf surfaces.

## Diversity Indices

Quantifying fungal diversity requires robust indices that capture both [[species-richness-diversity-indices-fungi]] and the relative abundances of species. Several major indices are employed in mycological studies, each with distinct strengths and limitations.

### Berger-Parker Index

The Berger-Parker index (*d*) expresses dominance as the proportion of individuals belonging to the single most abundant species in a sample:

> *d* = N_max / N

where N_max is the number of individuals in the most abundant species and N is the total number of individuals. Its primary advantage is simplicity and intuitive interpretability. However, it is highly sensitive to changes in the dominant species and ignores the contributions of all other species, making it a coarse measure of community structure.

### Fisher's Log-Series Alpha (α)

Fisher's α is derived from fitting a log-series distribution to species abundance data. It is a widely used richness estimator that is largely independent of sample size, making it valuable for comparing fungal communities sampled with unequal effort. Fisher's α weights rare species heavily, which is advantageous in hyperdiverse [[fungal-biodiversity]] assemblages where many species occur as singletons or doubletons. Its limitation is that it assumes a specific underlying distribution (log-series) and may not perform well in communities where common species dominate.

### Hill's Diversity Numbers

Hill (1973) proposed a unified framework of diversity numbers that encompasses several traditional indices as special cases. The three most commonly used are:

| Index | Definition | Sensitivity |
|-------|-----------|-------------|
| **N0** | Species richness (S) | Sensitive to rare species |
| **N1** | Exponential of Shannon index (e^H′) | Gives weight to all species proportionally to their abundance |
| **N2** | Inverse of Simpson's index (1/λ) | Weighted heavily toward dominant species |

N0, N1, and N2 form a spectrum from rarity-weighted to dominance-weighted diversity. Plotting these together provides a profile of the community that reveals how diversity changes with the weighting of rare versus common species. A community where N0 >> N2 indicates high evenness, while N0 ≈ N2 signals strong dominance by a few species.

## Evenness Measures

Evenness quantifies how equally individuals are distributed among species. It is commonly expressed as:

> **e = Diversity_observed / Diversity_max**

where Diversity_max is the diversity that would be achieved if all species were equally abundant (i.e., the maximum value for the given index at the observed species richness). Evenness ranges from 0 (complete dominance by one species) to 1 (perfect evenness). Different diversity indices yield different evenness values, so the choice of parent index matters. Evenness complements richness by revealing whether high species counts are driven by many co-dominant species or by a long tail of rare taxa.

## Jackknifing for Confidence Intervals

Diversity indices are point estimates subject to sampling variation. **Jackknifing** is a resampling technique used to estimate bias and construct confidence intervals for diversity indices without assuming a specific distribution. The procedure works by iteratively removing one sample (or observation) from the dataset, recalculating the index on the reduced dataset, and aggregating these pseudoreplicate values. The variance across pseudoreplicates provides an estimate of the standard error, from which confidence intervals are derived. Jackknifing is particularly valuable in [[fungal-ecology]] because it accommodates the typically non-normal, skewed abundance distributions found in fungal datasets.

## Species Abundance Distribution Models

Several theoretical models describe how species abundances are arranged within communities. Fitting these models to fungal data reveals underlying ecological processes.

### Geometric Series

In the geometric series (niche-preemption) model, the most abundant species preempts a proportion *k* of a limiting resource, the next most abundant preempts the same proportion *k* of the remainder, and so on. This produces a steep rank-abundance curve where a few species dominate and many species are rare. It is characteristic of **species-poor, environmentally stressed, or early-successional communities**.

### Log-Series Distribution

The log-series predicts that the number of species represented by *n* individuals follows a harmonic series. Most species are represented by a single individual, with progressively fewer species at higher abundance classes. Fisher's α serves as the diversity parameter. This distribution fits **highly diverse communities with many rare species**, such as tropical fungal assemblages.

### Lognormal Distribution

The lognormal model assumes that the log-transformed abundances of species follow a normal (Gaussian) distribution. It produces a bell-shaped curve in logarithmic abundance classes, with a modal abundance class and symmetric tails of rarer and more common species. The lognormal is characteristic of **species-rich, mature, stable communities** where many niche axes regulate species abundances.

### Broken-Stick Model

The broken-stick (MacArthur) model divides a fixed total resource randomly among *S* species, yielding a relatively even distribution. It is considered a null model representing minimum niche differentiation. Communities fitting the broken-stick model show **high evenness and strong competitive equilibrium** among species.

## Rank-Abundance Plots

Rank-abundance (Whittaker) plots display species ranked from most to least abundant on the x-axis, with their relative or absolute abundance on the y-axis (often log-scaled). The shape of the curve immediately reveals the underlying distribution model: steep slopes indicate geometric or log-series distributions (dominance-driven), while shallow, convex curves indicate lognormal or broken-stick distributions (evenness-driven). These plots are a powerful visual tool for comparing fungal communities across habitats or treatments.

## Ecological Characteristics of Distribution Models

| Model | Ecological Context | Typical Habitat Examples |
|-------|-------------------|------------------------|
| Geometric series | Species-poor, stressed, or disturbed environments | Rhizoplane fungi on single plant roots |
| Log-series | Very diverse, many rare species | Phylloplane fungi on leaf surfaces; diverse tropical soil fungi |
| Lognormal | Species-rich, stable, mature communities | Forest soil fungal communities; [[biodiversity-of-fungi-leaf-litter-microfungi-survey-methods]] in late decomposition |
| Broken-stick | Competitive equilibrium, high evenness | Rarely observed in full in natural fungal communities |

## Fungal Ecology Examples

Empirical studies of fungal communities reveal patterns consistent with these models:

- **Rhizoplane fungi** — Communities on root surfaces are often dominated by one or two fast-colonizing species (e.g., *Fusarium*, *Mucor*), fitting geometric or log-series distributions. The rhizoplane is a spatially constrained, resource-limited habitat favoring dominance.

- **Phylloplane fungi** — Leaf surface communities can be highly diverse, with many transient species represented by few propagules. These communities frequently fit log-series or lognormal distributions depending on leaf age, host plant, and seasonal conditions.

- **Forest soil fungi** — Mature forest soils harbor extraordinarily diverse fungal assemblages including mycorrhizal, saprotrophic, and pathogenic guilds. These communities often follow lognormal distributions, reflecting the stable, multi-dimensional niche structure of the soil environment.

- **Leaf litter microfungi** — Successional changes in litter decomposer communities shift distributions from geometric (early colonization by opportunists) toward lognormal (later stages with complex guild structure), illustrating how SADs change with community maturation.

## Spatial Scales of Biodiversity

Whittaker (1972) defined a hierarchical framework for biodiversity at different spatial scales:

| Scale | Definition | Fungal Relevance |
|-------|-----------|-----------------|
| **Point diversity** | Species richness at a single microsite or sample point | OTUs in a single soil core or leaf disk |
| **Alpha (α) diversity** | Diversity within a single habitat or community | Fungal diversity within a forest stand or a single leaf type |
| **Beta (β) diversity** | Turnover of species between habitats or along gradients | Species replacement between rhizoplane and bulk soil, or between leaf litter layers |
| **Gamma (γ) diversity** | Total diversity across a landscape encompassing multiple habitats | Fungal diversity across an entire forest or watershed |
| **Epsilon (ε) diversity** | Regional diversity across broad biogeographic domains | Continental-scale fungal diversity patterns |

Alpha and gamma diversity are related through beta diversity: γ = ᾱ × β, where ᾱ is mean alpha diversity across habitats. This relationship highlights that regional fungal diversity arises from both local richness and species turnover among habitats.

## Differentiation Diversity

Differentiation diversity describes the extent to which species composition differs across spatial or ecological units:

- **Pattern diversity** — Turnover of species between samples within the same habitat; measured at a fine spatial grain. It captures microhabitat heterogeneity, such as differences between adjacent soil cores or individual leaves on the same tree.

- **Beta diversity** — Species turnover between distinct habitats or along [[fungal-adaptations-environmental-gradients]]. In fungal ecology, beta diversity between root-associated and soil communities is typically high due to host selection and niche specialization.

- **Delta (δ) diversity** — Turnover between major geographic regions or landscape units. It captures biogeographic and climatic controls on fungal [[core-endorhiza-bacterial-community-composition-cannabis]] at broad scales.

## Beta Diversity Metrics

Multiple [[quantitative-indices-fungal-diversity]] exist for assessing beta diversity, each emphasizing different aspects of compositional change:

- **Whittaker's β** = (S / ᾱ) − 1, where S is total species in the combined sites and ᾱ is mean [[species-richness-diversity-indices-fungi]] per site. This simple ratio captures additive species turnover and is a cornerstone of [[quantitative-indices-fungal-diversity]] in ecology.

- **Jaccard and Sørensen dissimilarity** — Coefficient-based measures of pairwise compositional similarity, widely used in fungal [[yeast-isolation-community-ecology]] studies employing sequencing data.

- **Bray-Curtis dissimilarity** — Accounts for relative abundances (not just presence/absence), making it sensitive to changes in dominant fungal taxa across samples. A widely used [[similarity-distance-measures-fungal-ecology]] in community ecology.

- **Additive and multiplicative partitioning** — Frameworks that decompose gamma diversity into within- and between-habitat components, allowing ecologists to quantify the relative contributions of alpha and beta diversity to regional fungal richness.

The choice of beta diversity metric influences ecological interpretation, and no single measure is universally optimal. Researchers are encouraged to use multiple complementary metrics and to consider the grain, extent, and environmental context of their sampling design.
