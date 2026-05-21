---
title: Evenness Indices and Species-Abundance Distribution Models in Fungal Ecology
source: unknown-biodiversity-of-fungi.md (Chunk 19)
type: concept
---

## Evenness Indices and Species-Abundance Distribution Models in Fungal Ecology

## Overview

While species richness (the number of species present) provides a basic measure of fungal community diversity, it fails to capture how individuals are distributed among those species. Two communities may contain the same number of species yet differ profoundly in their ecological structure: one may be dominated by a few abundant taxa, while another may exhibit a more equitable distribution of individuals across species. **Evenness** and **species-abundance distribution models** address this limitation by quantifying and describing the pattern of species dominance and rarity within fungal assemblages.

## Evenness Indices

Evenness measures the degree to which individuals are evenly distributed among species. The simplest formulation expresses evenness as the ratio of observed diversity to maximum possible diversity:

```
e = Diversity_obs / Diversity_max
```

When all species are equally abundant, evenness approaches 1.0; when one species dominates the community, evenness approaches 0. Values between 0 and 1 allow comparison of community structure independent of species richness. Evenness is most commonly calculated using the Shannon diversity index as the numerator, with the denominator being the maximum Shannon value achievable when all species are equally represented (i.e., H_max = ln S, where S is species richness). Pielou"s evenness index (J') is the most widely used form:

```
J' = H' / H_max = H' / ln S
```

However, evenness based on the Shannon index is sensitive to species richness, which has prompted alternative approaches such as those based on Simpson's index. The Simpson-based evenness (E_1/D = D/D_max) is less affected by richness but more heavily weights dominant species, providing a complementary perspective on community structure.

## Hill's Diversity Numbers

Ludwig and Reynolds recommended the use of **Hill's diversity numbers** (N0, N1, N2) as a unified framework for diversity measurement. These provide a family of diversity measures that differ in their sensitivity to rare versus common species:

- **N0** (Hill number of order 0): Equivalent to species richness S. All species are weighted equally regardless of abundance. This is the most basic diversity measure, sensitive only to species presence.
- **N1** (Hill number of order 1): Equivalent to the exponential of Shannon's entropy, e^H'. Represents the number of "common" or "typical" species in the community. Sensitive to both richness and evenness.
- **N2** (Hill number of order 2): Equivalent to 1/Simpson"s concentration index. Represents the number of "very abundant" or "dominant" species. Weighted heavily toward the most common taxa.

Hill's numbers have the advantage of being expressed in effective species units, making them directly comparable across orders. The ratio N2/N1 or N1/N0 can serve as an evenness measure, avoiding some of the biases inherent in ratio-based evenness indices. The relationship N2 ≤ N1 ≤ N0 always holds, with equality only when all species are equally abundant.

## Species-Abundance Distributions

Rather than reducing community structure to a single diversity or evenness index, species-abundance distribution (SAD) models describe the full pattern of how many species are represented by how many individuals. These models serve as powerful alternatives to single-value diversity indices because they encode information about both richness and evenness simultaneously. They also provide insight into the underlying ecological processes shaping community assembly. Four main models are recognized in [[fungal-ecology]]:

### 1. Geometric Series (Niche Preemption Model)

In the geometric series, each species preempts a constant proportion (k) of the remaining niche space. The most abundant species claims the largest fraction, the second most abundant claims k of the remainder, and so on. This produces a steep rank-abundance curve with few dominant species and many rare ones. It is characteristic of species-poor, environmentally stressed, or early successional communities where strong competitive hierarchies exist.

### 2. Logarithmic Series

Fisher's logarithmic series predicts the number of species expected to be represented by 1, 2, 3, ... n individuals. It is described by the parameter α (alpha), which is **independent of sample size** and serves as a robust diversity index in its own right. Fisher's α increases with both richness and evenness, making it one of the most widely used single-value diversity measures in mycological studies. The log series is characteristic of species-rich communities with many rare species and fits well in [[fungal-foraging-strategies-heterogeneous-environments]] or large, well-mixed species pools.

### 3. Lognormal Distribution

The lognormal distribution arises when the log-transformed abundances of species follow a normal (Gaussian) curve. It is characteristic of mature, stable, species-rich communities where many interacting factors regulate species abundances. Most fungal communities in undisturbed ecosystems are expected to follow lognormal distributions. The distribution is described by parameters related to its mean and variance on the log scale, and the canonical lognormal (where variance is a function of the total number of individuals) is particularly relevant for ecological communities.

### 4. Broken-Stick (MacArthur) Model

The broken-stick model assumes that resources are divided randomly among species, akin to breaking a stick at random points. It predicts the most even distribution of abundances among the four models and is characteristic of species-rich, ecologically stable, and highly competitive communities where niche overlap is minimal. Few fungal communities conform strictly to the broken-stick model, making it useful primarily as a theoretical endpoint against which observed communities can be compared.

## Rank-Abundance Plots

A **rank-abundance plot** (also called a dominance-diversity curve) provides a visual representation of species-abundance patterns. Species are ranked from most to least abundant on the x-axis, and their relative importance is plotted on the y-axis using a logarithmic scale:

```
Pi = (ni / N) × 100
```

Where Pi is the relative importance (percentage) of species i, ni is the number of individuals (or a proxy such as biomass, colony-forming units, or molecular operational taxonomic unit counts) of species i, and N is the total number of individuals in the community. The shape of the resulting curve identifies which SAD model best describes the community: steep slopes indicate geometric or log-series distributions, while shallower slopes approaching a plateau suggest lognormal or broken-stick distributions. Rank-abundance plots are particularly useful for comparing communities visually before formal statistical fitting.

## Ecological Interpretation (Model Characteristics)

Each SAD model carries distinct ecological implications, summarized as follows:

| Model | Community Type | Evenness | Richness | Disturbance Regime |
|-------|---------------|----------|----------|-------------------|
| Geometric series | Stressed, early successional | Low | Low | High disturbance or harsh conditions |
| Logarithmic series | Heterogeneous, species-rich | Low–moderate | Moderate–high | Variable, often disturbed |
| Lognormal | Mature, stable, complex | Moderate–high | High | Low disturbance, equilibrium |
| Broken-stick | Highly competitive, stable | High | High | Very low disturbance, niche-packed |

Communities occupying harsh or recently disturbed habitats (e.g., heavily polluted soils, newly colonized substrates) tend toward geometric or log-series distributions. In contrast, fungal communities in late-successional or undisturbed forests typically approach lognormal distributions, reflecting the equilibrium of many interacting species. The progression from geometric → log-series → lognormal → broken-stick along gradients of increasing habitat stability and niche complexity is a recurring pattern in fungal ecology.

## Examples from Fungal Studies

Empirical applications of SAD models in [[mycology]] illustrate their diagnostic value:

- **Zak (1988)** studied root-surface fungi and found that fungal assemblages on root surfaces of different plant species often followed lognormal distributions, suggesting mature and stable host-fungal associations. Differences in distribution parameters among host species reflected variation in root exudate chemistry and microhabitat conditions.
- **Lussenhop (1981)** examined fungal communities in forest soils and reported patterns consistent with log-series or lognormal distributions depending on soil depth and horizon. Surface organic layers with greater resource heterogeneity supported more species-rich assemblages with lognormal patterns, while deeper mineral [[soil-horizons]] showed simpler geometric or log-series structures.
- **Polishook (1996)** investigated endophytic and leaf-litter fungi in Puerto Rican forests and documented distinct species-abundance patterns across successional gradients. Early-successional leaf litter hosted fungal communities fitting geometric series models, while mature forest canopy and litter communities approached lognormal distributions, consistent with increasing niche complexity and competitive equilibrium over time.

These studies collectively demonstrate that SAD models can discriminate among fungal communities differing in successional status, substrate quality, and environmental conditions — information that would be lost or obscured by relying solely on species richness or a single diversity index.

## Statistical Methods: Fitting and Testing Distributions

Fitting SAD models to observed fungal community data requires formal goodness-of-fit testing:

- **Chi-square (χ²) tests** compare observed and expected frequencies of species in each abundance class. The community data are binned into abundance categories, expected frequencies under each model are calculated, and the χ² statistic is computed. Significant departures indicate poor fit. Adequate expected cell counts (generally ≥ 5) are required for valid inference.
- **G-tests (log-likelihood ratio tests)** provide a preferred alternative to χ² tests, particularly when expected frequencies are small. The G statistic is based on the ratio of observed to expected likelihoods and follows a χ² distribution under the null hypothesis. Williams' correction can be applied to improve the approximation.

Model selection among competing SAD models should consider both statistical fit and ecological plausibility. Akaike's Information Criterion (AIC) and related approaches can supplement traditional goodness-of-fit tests when comparing non-nested models.

## Confidence Intervals and Estimation Precision

**Jackknife estimation** provides a resampling-based method for constructing confidence intervals around diversity indices (including Fisher's α, Shannon's H', and Simpson's D). By systematically omitting one sample or observation at a time and recalculating the index, the jackknife estimates bias and variance. This approach is particularly valuable in fungal ecology, where sampling intensity and spatial heterogeneity can substantially affect diversity estimates. Jackknife-derived confidence intervals allow researchers to assess whether observed differences between communities are statistically meaningful or artifacts of sampling variability. Bootstrap resampling offers a related alternative that may be preferable for indices with complex sampling distributions.

## Limitations and Cautions

Several important caveats attend the use of evenness indices and SAD models in fungal ecology:

- **Magurran (1988)** cautioned that evenness indices are sensitive to sample size and species richness. Comparison of evenness between communities with very different richness values can be misleading because the denominator (maximum diversity) is itself a function of richness.
- **Taylor (1978)** demonstrated that species-abundance distributions are heavily influenced by sampling effort and spatial scale. Aggregation of individuals (patchiness), which is characteristic of many fungal taxa, violates the assumptions of randomness underlying several SAD models and can distort apparent distribution shapes.
- **Sampling completeness** is a critical concern: undersampled fungal communities may appear to follow geometric or log-series distributions simply because rare species have not been detected, when in reality the community may be lognormal.
- **Molecular vs. morphological data**: Modern [[biodiversity-fungal-molecular-identification-dna-barcoding]] (e.g., high-throughput sequencing) reveals far greater species richness than culture-based methods, shifting observed distributions toward lognormal patterns and increasing estimates of evenness. Comparisons across studies using different [[forensic-identification-methods-psilocybin-mushrooms-tlc-gc-hplc]] must account for this bias.
- **Choice of abundance measure**: Whether abundance is measured as colony-forming units, hyphal length, DNA sequence read counts, or biomass can profoundly affect the perceived distribution shape and derived diversity estimates.

## Practical Recommendations for Mycologists

When applying these methods in fungal ecology, the following workflow is recommended: (1) characterize species-abundance patterns using rank-abundance plots as an initial exploratory step; (2) compute Hill's diversity numbers N0, N1, and N2 to capture richness-to-dominance gradients in interpretable units; (3) fit the four candidate SAD models and evaluate goodness-of-fit using G-tests with Williams' correction; (4) construct jackknife confidence intervals for all diversity estimates to quantify sampling uncertainty; and (5) interpret distribution shapes in light of known [[fungal-adaptations-environmental-gradients]] and successional context. This [[solomon-insects-and-diseases-integrated-approach]] leverages the strengths of both single-value indices and full distributional models while maintaining awareness of their limitations.

## Summary

Evenness indices and species-abundance distribution models provide complementary tools for characterizing [[mineralogical-controls-fungal-community-structure]] beyond simple species counts. While single-value indices like evenness, Shannon's H', Simpson's D, and Fisher's α offer convenient summary statistics, SAD models encode richer ecological information about dominance hierarchies, niche partitioning, and successional status. Hill's diversity numbers (N0, N1, N2) offer a unified and interpretable framework for comparing communities. Rigorous application requires adequate sampling, appropriate goodness-of-fit testing, jackknife confidence intervals, and careful attention to the ecological assumptions underlying each model.
