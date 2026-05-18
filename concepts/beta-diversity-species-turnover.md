---
title: Beta Diversity and Species Turnover Metrics
source: unknown-biodiversity-of-fungi.md
type: concept
---

# Beta Diversity and Species Turnover Metrics

## Overview

**Beta diversity** (β-diversity) is a measure of **differentiation diversity** — the degree to which species composition differs between two or more sites, communities, or habitats. Unlike alpha diversity, which quantifies species richness within a single site, beta diversity captures the variation in species identity across space (or time). It is a central concept in community ecology, biogeography, and [[fungal-conservation-biology]], providing insight into how ecological processes such as dispersal, environmental filtering, and competition shape the distribution of biodiversity.

In mycology, beta diversity is especially valuable for understanding how fungal communities change across soil types, host plants, elevation gradients, and disturbance regimes. Because many fungi are habitat specialists with narrow ecological niches, turnover in fungal assemblages can be pronounced even across relatively short distances.

## Whittaker's Framework of Diversity Levels

The concept of beta diversity was formally introduced by **R. H. Whittaker** (1960, 1972) as part of a hierarchical framework distinguishing three scales of diversity:

### 1. Alpha (α) Diversity

The species richness of a local community or homogeneous habitat patch — the number of species co-occurring within a single sampling unit.

### 2. Beta (β) Diversity

The change (or turnover) in species composition between different sites or along [[fungal-adaptations-environmental-gradients]]. Beta diversity measures the extent to which species replace one another across space. It reflects both the **pattern diversity** within a landscape (heterogeneity at the within-habitat scale) and the broader **differentiation** between distinct habitat types.

### 3. Gamma (γ) Diversity

The total species richness across an entire landscape or region, encompassing all the alpha diversity units within it. Gamma diversity is related to alpha and beta by the classic multiplicative relationship:

> **γ = ᾱ × β**

where ᾱ is the mean alpha diversity across sites and β is the average beta diversity.

### Whittaker's Three Sub-Levels of Differentiation

Within his broader scheme, Whittaker further subdivided differentiation diversity into:

- **Pattern diversity**: Variation in species composition among microhabitats within a single community (fine-scale heterogeneity, e.g., variation among different decaying log stages within a forest stand).
- **Beta diversity**: Species turnover between different communities or along an environmental gradient (e.g., changes in fungal species from lowland to montane forest).
- **Delta (δ) diversity**: Broad-scale turnover among different landscape types or biogeographic regions (e.g., differences between temperate and tropical fungal floras).

## Species Turnover Along Ecological Gradients

Species turnover — the replacement of some species by others as one moves across space or environmental conditions — is the fundamental process underlying beta diversity. Key mechanisms driving turnover include:

- **Environmental gradients**: Changes in temperature, moisture, pH, or [[nutrient-availability]] select for different species. Fungal fruiting patterns, for instance, often shift predictably along elevation and precipitation gradients.
- **Spatial distance and [[fungal-dispersal-limitation-biogeographic-barriers]]**: Even in environmentally homogeneous areas, communities may differ due to limited [[spore-dispersal]] and historical contingency.
- **Biotic interactions**: Competition, host specificity, and mutualisms (e.g., [[plants-without-mycorrhizal-associations]]) can cause sharp species turnover across host plant boundaries.
- **Disturbance and succession**: Post-fire, post-harvest, or post-flood successional gradients often show strong fungal species turnover as pioneer species are replaced by late-successional taxa.

## Beta Diversity Metrics Using Presence-Absence Data

A wide range of [[fungal-biodiversity-quantitative-indices]] have been developed to measure beta diversity from **presence-absence** (incidence) data. Six of the most commonly used metrics are summarized below. Each takes as input a species-by-site matrix recording which species are present in each sample, and each provides a different perspective on how communities differ.

### 1. Whittaker's Beta (β_w)

**Formula:**

> β_w = S / ᾱ − 1

where **S** is the total number of species recorded across all sites combined, and **ᾱ** is the average number of species per site.

**Interpretation:** This is the simplest and most widely used beta diversity index. It expresses the ratio of total (gamma) richness to average local (alpha) richness. Values close to 0 indicate that most species are shared among sites (low turnover); higher values indicate greater dissimilarity. In fungal surveys, β_w is useful for a first-pass comparison of turnover among habitat types, though it is sensitive to the number of sites sampled.

### 2. Cody's Beta (β_c)

**Formula:**

> β_c = (g + l) / 2

where **g** is the number of species gained and **l** is the number of species lost between two sites (or between consecutive sites along a gradient).

**Interpretation:** Cody's index measures turnover as the average number of species that are replaced (i.e., gained in one site and lost in another). It is particularly well suited for **gradient studies** and transect-based sampling where the direction of change matters. In [[fungal-ecology]], β_c can reveal sharp compositional breaks along [[soil-ph]] or host tree transitions.

### 3. Routledge's Beta (β_R)

**Formula:**

> β_R = (S² / (2r + S)) − 1

where **S** is the total species richness across all sites and **r** is the number of species pairs with overlapping (shared) occurrences among sites.

**Interpretation:** This metric directly incorporates the degree of **species overlap** between sites. When many species co-occur across sites, r is large and β_R approaches zero. When few species are shared, β_R increases. It provides an intuitive measure of how much the communities "overlap" in composition.

### 4. Routledge's Modified Beta (β_I)

**Formula:**

> β_I = log(S) − log(ᾱ) − log(ᾱ / S) / log(S)

**Interpretation:** A modified version of Routledge's original index, β_I was designed to capture **gain and loss along transects** in a way that is less sensitive to variation in species richness among sites. It is useful when comparing turnover across datasets that differ in sampling intensity or local richness.

### 5. Wilson and Shmida's Beta (β_T)

**Formula:**

> β_T = (g + l) / (2ᾱ)

where **g** and **l** are species gained and lost, and **ᾱ** is the mean alpha diversity.

**Interpretation:** This metric **combines additive and multiplicative approaches** to beta diversity. The numerator (g + l) captures absolute turnover, while dividing by 2ᾱ standardizes the index relative to local species richness. Values range from 0 (complete compositional identity) to 1 (no species shared). It is one of the most balanced and widely recommended metrics for ecological studies.

### 6. Routledge's Reciprocal Beta (β_E)

**Formula:**

> β_E = exp(H) − 1

where **H** is the Shannon information (entropy) calculated from the proportion of species found in each site.

**Interpretation:** Also called the "complement of evenness," β_E reflects how evenly species are distributed across sites. If all species occur at every site, β_E = 0. If each species is restricted to a single site, β_E reaches its maximum. This index is conceptually related to the Shannon diversity index and is particularly useful when researchers want to quantify how species are partitioned across a landscape.

## Comparative Summary

| Metric | Basis | Sensitive to | Typical Use |
|--------|-------|-------------|-------------|
| β_w (Whittaker) | S / ᾱ ratio | Total vs. average richness | General turnover comparison |
| β_c (Cody) | Gains + losses | Species replacement rate | Gradient and transect studies |
| β_R (Routledge) | Species overlap | Shared species pairs | Overlap-focused analysis |
| β_I (Routledge mod.) | Gain/loss, transect | Sampling intensity differences | Standardized transect comparisons |
| β_T (Wilson–Shmida) | Additive × multiplicative | Richness-standardized turnover | Balanced ecological studies |
| β_E (Routledge reciprocal) | Shannon evenness | Species distribution evenness | Landscape-level partitioning |

## Ecological Interpretation and Considerations

All six metrics address a fundamental question: **how many species are shared versus unique between sites?** However, they differ in how they weight various components of compositional change:

- **Richness-dependent metrics** (β_w, β_R, β_E) are influenced by the total number of species in the dataset and may conflate turnover with differences in local richness.
- **Incidence-based metrics** (β_c, β_T) focus specifically on which species are gained or lost, making them more directly interpretable as measures of turnover.
- **Standardized metrics** (β_T, β_I) attempt to control for variation in alpha diversity, allowing more meaningful comparisons across studies.

### Applications in Fungal Ecology

Beta diversity metrics are widely applied in fungal community studies to address questions such as:

- How does the composition of **mycorrhizal fungal communities** change along elevation gradients?
- What is the rate of **saprotrophic species turnover** across different stages of wood decay?
- How does **soil fungal beta diversity** respond to agricultural intensification or land-use change?
- Are fungal communities in **distinct habitat types** (e.g., forest vs. grassland) more differentiated than plant communities in the same areas?

## See Also

- **Alpha diversity** — species richness within a single community
- **Gamma diversity** — total species richness across a landscape
- **Incidence-based compositional dissimilarity** — related pairwise measures (Jaccard, Sørensen)
- **[[fungal-functional-diversity-communities]]** — turnover in functional traits rather than species identities
