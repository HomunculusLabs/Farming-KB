---
title: Quantitative Indices of Fungal Biodiversity
source: unknown-biodiversity-of-fungi.md
type: concept
---

# Quantitative Indices of Fungal Biodiversity

Quantitative indices provide the mathematical foundation for comparing fungal biodiversity across habitats, spatial scales, and sampling regimes. Because fungal communities are extraordinarily diverse and often dominated by a few abundant taxa with many rare species, choosing appropriate indices and understanding their properties is critical for robust ecological inference.

## Species Richness: Three Measures

Species richness — the count of species present — is the most intuitive measure of biodiversity, but the term encompasses distinct concepts:

**Numerical Species Richness (S)** is simply the raw count of species observed in a sample or census. It makes no adjustment for sampling effort and is therefore highly sensitive to the number of individuals or substrate units examined. Comparisons of S across studies are only meaningful when effort is equivalent.

**Species Density (S/A)** expresses richness per unit of sampling effort, area, or substrate (e.g., species per soil core, species per gram of litter). This standardization permits comparison across studies that differ in total effort but sample comparable microhabitats. It is the most widely used richness measure in mycological surveys.

**Total Species Richness** estimates the asymptotic number of species in a community as sampling approaches completeness. It is inferred by extrapolating species-accumulation curves or fitting parametric models to sample data. Total richness is valuable for conservation assessments but carries substantial estimation uncertainty when communities contain many rare species — a near-universal condition in fungal assemblages.

## Species-Effort Relationships

Three mathematical models commonly describe the relationship between observed species richness (S) and accumulated sampling effort (A):

| Model | Equation | Shape | Appropriate When |
|-------|----------|-------|------------------|
| **Power** | S = CA^z | Decelerating, no asymptote | Sampling a small fraction of a large, heterogeneous landscape; z typically 0.1–0.4 |
| **Exponential** | S = C + z ln A | Decelerating, no asymptote | Similar to power but fits communities where new species accumulate logarithmically with effort |
| **Logistic** | S = B / (C + A)^−z | Sigmoidal with upper asymptote | Sampling nears community completeness; asymptote B estimates total richness |

The power model (also called the species-area relationship or Arrhenius equation) is the most widely applied in mycology. Its exponent z reflects the spatial turnover of species: higher z values indicate stronger compositional change with scale. The logistic model is preferred when the goal is estimating total species richness, as its asymptote provides a direct estimate.

## Rarefaction Analysis

Rarefaction standardizes species richness to a common sample size, allowing fair comparison among communities sampled with unequal effort. The classic rarefaction formula for individuals-based sampling is:

**E(S_n) = Σ (1 − C(N − n_i, n) / C(N, n))** for i = 1 to S

where E(S_n) is the expected number of species in a random subsample of n individuals, N is total individuals, n_i is the count of species i, S is total species, and C denotes the binomial coefficient.

Rarefaction curves plot E(S_n) against n; steep initial slopes indicate uneven communities dominated by few species, while gradual slopes indicate more equitable distributions. Rarefaction is most informative when subsample sizes do not fall below roughly 50% of the smallest sample total. In fungal studies, where individual counts are often impractical, sample-based (incidence-based) rarefaction using presence-absence across sampling units is more commonly applied.

## Simpson's Diversity Index

Simpson's index measures the probability that two randomly chosen individuals belong to different species. Two formulations exist:

**λ = Σ p_i²** (complete enumeration / infinite population)

**D = Σ [n_i(n_i − 1)] / [N(N − 1)]** (finite sampling correction)

where p_i is the proportional abundance of species i, n_i is the count of species i, and N is total individuals. Lambda ranges from 0 to 1; higher values indicate lower diversity (greater dominance). Because this is counterintuitive, many authors report **1 − λ** or **1/D**, which increase with diversity. Simpson's index is strongly weighted toward the most abundant species and is relatively insensitive to rare taxa — an advantage when rare species are poorly sampled, but a limitation when the goal is capturing full community structure.

## Shannon Index (H′)

The Shannon index derives from information theory and measures the uncertainty (in bits) associated with predicting the species identity of a randomly chosen individual:

**H′ = −Σ p_i ln p_i**

Key properties:
- H′ = 0 when a single species monopolizes the community.
- H′ increases with both species richness and evenness.
- Typical values for fungal communities range from **1.5 to 3.5**, with higher values in species-rich, equitable tropical assemblages.
- H′ is moderately sensitive to rare species, more so than Simpson's index but less than species richness itself.

The Shannon index is the most widely reported diversity measure in mycological studies. Its information-theoretic foundation allows it to be decomposed into alpha (within-habitat) and beta (between-habitat) components, facilitating hierarchical analyses of fungal diversity across spatial scales.

## McIntosh Diversity Index

McIntosh's index treats the community as a point in S-dimensional space defined by species abundances:

**U = √(Σ n_i²)** (the Euclidean distance from the origin)

**D_Mc = (N − U) / (N − √N)** (diversity index, 0 to 1)

where n_i is the abundance of species i and N is total abundance. McIntosh's index has an elegant geometric interpretation: communities with even abundances lie closer to the surface of the hypersphere, yielding higher diversity values. It performs well in simulation studies and is correlated with both Shannon and Simpson indices, but sees less routine use in mycology.

## Berger-Parker Dominance Index

The Berger-Parker index is the simplest dominance measure:

**d = N_max / N**

where N_max is the abundance of the most dominant species. It ranges from near 0 (no dominance) to 1 (complete monoculture). Its simplicity is both a strength (easy to interpret, no assumptions about the full species abundance distribution) and a weakness (ignores all species except the dominant one). In fungal studies, it is useful for tracking the impact of disturbance or environmental gradients that shift community dominance.

## Fisher's Log-Series Alpha (α)

Fisher's α is derived from fitting a log-series distribution to species abundance data:

**S = α ln(1 + N/α)**

where S is species count and N is total individuals. The parameter α is a diversity index independent of sample size for log-series-distributed communities. Fisher's α is particularly sensitive to the number of rare species and performs well when the community follows a log-series distribution — a common pattern in species-rich fungal assemblages. It is less appropriate when a few species strongly dominate.

## Hill's Diversity Numbers

Hill (1973) unified diversity indices into a single parametric family:

| Order | Formula | Equivalence |
|-------|---------|-------------|
| N₀ = S | Σ p_i⁰ (p_i > 0) | Species richness |
| N₁ = exp(H′) | exp(−Σ p_i ln p_i) | Exponential Shannon |
| N₂ = 1/D | 1 / Σ p_i² | Inverse Simpson |

The order a determines sensitivity to rare species: N₀ weights all species equally, N₂ is dominated by common species, and N₁ is intermediate. Because all N_a share the same units (effective number of species), they are directly comparable. N₂ is recommended as the best single index of diversity for most purposes because of its strong statistical properties and ecological interpretability.

## Evenness Indices

Evenness quantifies how equally abundances are distributed among species:

- **Shannon Evenness (J′) = H′ / ln S** — ranges 0 to 1; compares observed H′ to the maximum possible for the observed richness.
- **Hill Evenness (E_{a,b}) = (N_a − 1) / (N_b − 1)** — typically E_{1,0} or E_{2,0}; compares diversity orders directly.
- **McIntosh Evenness = (N − U) / (N − N/√S)** — analogous to J′ using the McIntosh framework.

Evenness is ecologically meaningful in fungal communities because it distinguishes between species-poor communities with equitable distributions and species-rich communities dominated by a few taxa.

## Jackknifing for Confidence Limits

Because most diversity indices are biased estimators (especially with small samples), jackknifing provides a nonparametric method for estimating bias and constructing confidence intervals. The first-order jackknife deletes one sampling unit at a time, recalculates the index, and averages the pseudovalues:

**θ̂_JK = nθ̂ − (n − 1)(1/n) Σ θ̂_{(i)}**

Higher-order jackknives and bootstrapping offer improved accuracy for complex indices like Fisher's α. Confidence intervals from jackknifing are essential for statistically rigorous comparisons of fungal diversity among treatments or habitats.

## Scale-Dependence of Diversity Patterns

All diversity indices are scale-dependent. Species richness increases with spatial extent (positive species-area relationship). Evenness may increase or decrease with scale depending on whether environmental heterogeneity generates novel species assemblages or mixes already-dominant taxa. Simpson's index (N₂) is the least scale-sensitive of the common indices, while species richness and Shannon index are more strongly affected. Consequently, comparisons across studies must account for differences in both grain (individual sample unit size) and extent (total area sampled).

## Recommendations for Mycological Studies

1. **Always report species richness (S) and sample size (N or number of sampling units)** — these are the fundamental data from which all indices derive.
2. **Use Hill's N₂ (inverse Simpson) as the primary diversity index** — it has the best statistical behavior, is interpretable as effective number of species, and is relatively robust to sampling variation.
3. **Report Shannon H′ for comparability with the existing literature** — it remains the most widely cited index in mycology.
4. **Apply rarefaction** when comparing communities sampled with unequal effort.
5. **Use Fisher's α** when the community is species-rich and log-series-distributed, as is typical for many fungal assemblages.
6. **Construct confidence intervals via jackknifing or bootstrapping** rather than relying on point estimates alone.
7. **Pair diversity indices with evenness measures** (e.g., J′ or Hill evenness) to disentangle the contributions of richness and equitability.
8. **Report Berger-Parker dominance** alongside composite indices to highlight the influence of the most abundant taxa.

## See Also

- [[mycology]]
- [[mycorrhiza]]
- [[basidiomycota]]
- [[ascomycota]]
- [[kingdom-fungi]]
