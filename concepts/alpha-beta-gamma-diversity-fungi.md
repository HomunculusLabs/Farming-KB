---
title: Alpha Beta Gamma Diversity in Fungal Communities
created: 2026-04-16
updated: 2026-04-16
type: concept
tags: [mycology, fungi]
sources: [/Users/t3rpz/wiki/raw/papers/unknown-biodiversity-of-fungi.md]
---
# Alpha Beta Gamma Diversity in Fungal Communities

Diversity in fungal communities operates at multiple spatial scales. Whittaker (1977) was the first to formalize the hierarchical, scale-dependent nature of ecological diversity, defining alpha, beta, and gamma diversity as complementary components that together describe the full diversity of a landscape.

## Hierarchical Diversity Concepts

### Point Diversity
The primary level of diversity, reflecting the species composition at a particular micro-location (a single leaf, a small soil core, or a specific microhabitat). Point diversity represents the finest spatial resolution and is influenced by microenvironmental conditions.

### Alpha Diversity
Alpha diversity, sometimes called within-habitat diversity, describes the diversity within a single, relatively homogeneous habitat or sampling unit. For fungal studies, alpha diversity typically refers to:
- The number of fungal species in a single plot, soil sample, or host individual
- The diversity of a single substrate type (e.g., leaf litter, dung, wood)
- Species richness, Shannon diversity, or Simpson diversity calculated within a defined sampling unit

Alpha diversity in fungal communities is influenced by:
- Resource heterogeneity within the habitat
- Competition among fungal species
- Host plant identity (for plant-associated fungi)
- Microclimatic conditions (moisture, temperature, pH)

### Beta Diversity
Beta diversity measures the degree of species turnover or change in species composition between habitats, sites, or along environmental gradients. It quantifies how different two or more communities are from each other. Beta diversity is by far the most commonly used metric of differentiation diversity for examining species turnover along gradients.

Beta diversity can be measured using presence-absence (binary) data or abundance data. Common binary measures include:
- **Whittaker's beta** (bw = S/a - 1): the total species count divided by average sample diversity minus one; fulfills most criteria for an effective index with fewest restrictions
- **Cody's beta** (bc = [g(H) + l(H)]/2): based on species gained and lost along a transect
- **Wilson-Shmida beta** (bT = [g(H) + l(H)]/2a): an acceptable alternative to Whittaker's measure

A disadvantage of binary beta diversity indices is that all species contribute equally regardless of abundance. The Bray-Curtis dissimilarity index uses abundance data and is recommended when quantitative data are available.

### Gamma Diversity
Gamma diversity is the total species richness across an entire landscape, region, or set of habitats. It represents the cumulative diversity at the broadest spatial scale studied and incorporates both within-habitat (alpha) and between-habitat (beta) components.

The relationship among diversity components is: gamma diversity = alpha diversity + beta diversity (additive model) or gamma = alpha x beta (multiplicative model).

## Similarity and Dissimilarity Indices

In addition to beta diversity, similarity coefficients quantify differences in species composition among sites. Widely used indices include:
- **Sorensen's Index** (SI = 2j/(a+b)): recommended by Magurran (1988) for binary data comparisons
- **Jaccard's Index** (JI = j/(a+b-j)): proportion of shared species to total species
- **Bray-Curtis Index**: metric dissimilarity using abundance data; a modification of the Sorensen Index
- **Morisita-Horn Index**: useful for quantitative comparisons when sample sizes differ

Tulloss (1997) reviewed 15 similarity indices and found most unsatisfactory, proposing a Tripartite Similarity Index (T = U x S x R) that is sensitive to the size of each species list being compared.

## Applications to Fungal Studies

### Ectomycorrhizal Communities
Alpha diversity of ECM fungi varies with host tree species, stand age, and soil conditions. Beta diversity is often high along elevation gradients and between different host tree species, reflecting host specificity and environmental filtering. See [[arbuscular-mycorrhizal-fungal-diversity]] for comparison with AMF diversity patterns.

### Endophyte Communities
Alpha diversity of foliar [[endophytic-fungi]] varies with host species, leaf age, and canopy position. Beta diversity between tropical and temperate regions can be high, reflecting different host floras and climatic conditions.

### Soil Fungal Communities
Soil fungal alpha diversity varies with soil type, depth, and vegetation cover. Beta diversity along environmental gradients (moisture, pH, disturbance) reflects niche differentiation among fungal taxa. Gamma diversity at the landscape scale integrates diverse microhabitats.

### Coprophilous Fungi
Beta diversity between tropical and temperate [[coprophilous-fungi]] communities is significant, with latitudinal turnover in species composition. Richardson (2001) showed that although the number of taxa per sample does not decrease significantly with latitude, the individual taxa are different.

## Scale-Dependent Patterns

Zak and Willig (2004) emphasized that ecological effects on species density and numerical species richness are scale-dependent. The importance of different causal mechanisms varies with the spatial scale of observation:
- Fine scales: biotic interactions (competition, parasitism) dominate
- Intermediate scales: environmental heterogeneity and resource distribution
- Broad scales: climate, geography, and evolutionary history

Studies should explicitly define the scale of observation and the attribute of diversity being measured to allow meaningful comparisons across studies.

## Related Topics

- [[fungal-diversity-estimation-methods]]
- [[fungal-community-assembly]]
- [[fungal-biodiversity-sampling-design]]
- [[fungal-endemism-biogeography]]
- [[fungal-monitoring-long-term-studies]]

## References

- Biodiversity of Fungi (2004), Chapter 5: Fungal Biodiversity Patterns
- Whittaker, R.H. 1977. Evolution of species diversity in land communities
- Magurran, A.E. 1988. Ecological Diversity and Its Measurement
- Tulloss, R.E. 1997. Assessment of similarity indices
- [[fungal-species-richness-and-diversity-indices]]
- [[fungal-species-estimation-methods-total-diversity]]
- [[fungal-beta-diversity-species-turnover]]
