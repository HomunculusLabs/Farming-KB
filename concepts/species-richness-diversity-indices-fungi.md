---
title: Species Richness and Diversity Indices for Fungal Communities
source: unknown-biodiversity-of-fungi.md
type: concept
---

## Species Richness and Diversity Indices for Fungal Communities

Quantifying fungal biodiversity requires robust statistical frameworks that account for sampling effort, species abundance distributions, and the inherent challenges of detecting cryptic or rare taxa. This page covers the major approaches to measuring and comparing species richness and diversity in fungal communities.

## Collector"s Curves and Species-Effort Relationships

As sampling effort increases, the cumulative number of species recorded initially rises steeply, then gradually approaches an asymptote. This relationship — the collector's curve — is fundamental to estimating true richness and assessing sampling completeness.

Three mathematical models describe species-effort relationships, all belonging to the same curve family (He and Legendre 1996):

- **Logistic model** (Archibold 1949): S = B/(C + A)^−z — predicts an asymptotic plateau, providing the most accurate estimate of true species richness.
- **Power model** (Arrhenius 1921): S = CA^z — species richness increases monotonically without plateau, appropriate for heterogeneous landscapes where new species continue to appear.
- **Exponential model** (Gleason 1922): S = C + z ln A — also increases monotonically, suitable for heterogeneous sampling contexts.

The choice of model reflects the scale-dependence of ecological patterns. In homogeneous fungal communities, the logistic model's asymptote reliably estimates total richness. In spatially or temporally heterogeneous environments, the power and exponential models better capture the ongoing accumulation of species.

## Three Kinds of Species Richness

Species richness is not a single metric but a family of related concepts (Hurlbert 1971; Kempton 1979; Brown 1995; Rosenzweig 1995):

1. **Numerical species richness**: The species count when biomass or number of individuals is standardized across samples. Useful for comparing communities of similar productivity.

2. **Species density**: The species count when area, volume, or weight is standardized. This is the most common form reported in ecological studies of fungi, as it controls for substrate quantity.

3. **Total species richness**: The cumulative count derived from a series of samples, typically estimated through extrapolation rather than direct observation. This represents the asymptotic richness that full sampling would reveal.

Distinguishing among these forms is critical for valid comparisons, since conflating them can produce misleading conclusions about community structure.

## Rarefaction

When comparing fungal communities from areas or habitats sampled with unequal effort, raw species counts are biased toward better-sampled sites. **Rarefaction** (Magurran 1988) standardizes richness to a common sample size by calculating the expected number of species in a random subsample.

The rarefaction formula is:

**E(S) = Σ [1 − (N − Nᵢ choose n) / (N choose n)]**

where n is the rarified (standardized) sample size, N is the total number of isolates across all species, and Nᵢ is the number of isolates belonging to species i. The combinatorial terms use factorials.

Rarefaction produces a curve showing expected species count as a function of sample size. Communities can be compared by evaluating richness at the same n value, typically the smallest sample size among the datasets being compared.

## Diversity Indices

Diversity indices integrate species richness with information about relative abundances (evenness), producing a single value that captures multiple dimensions of community structure.

### Simpson's Index (λ or D)

Introduced by Simpson (1949), this is a dominance measure heavily influenced by the most common species. It ranges from 0 (infinite diversity) to 1 (single species dominates). The unbiased estimator corrects for finite sample sizes. The reciprocal form (1/D) is widely used so that higher values indicate greater diversity.

### Shannon Index (H')

Based on information theory, H' = −Σ pᵢ ln pᵢ measures the average uncertainty in predicting the species identity of a randomly chosen individual. It equals 0 when a single species is present and reaches its maximum when all species are equally abundant. Typical values range from 1.5 to 3.5, rarely exceeding 4.5. A key advantage: H' is approximately normally distributed across replicate samples, enabling parametric statistical comparisons.

### McIntosh Index (U)

Defined as U = √(Σ pᵢ²), the McIntosh index offers good discrimination among communities with moderate sensitivity to sample size. It is less commonly used than Shannon or Simpson but provides complementary information.

### Berger-Parker Index (d)

The ratio d = Nₘₐₓ / N, where Nₘₐₓ is the number of individuals in the most abundant species and N is total individuals. This is a simple dominance index with poor discriminatory power for complex communities.

### Hill Numbers

Hill numbers provide a unified framework that relates common diversity indices to a single parameter q (the "order") controlling sensitivity to rare species:

- **N₁** = e^H" (the exponential of Shannon's index) — weights all species by their frequency
- **N₂** = 1/D (the reciprocal of Simpson's index) — disproportionately weights common species

Higher q values give more weight to abundant species. Hill numbers are in units of "effective number of species," making them intuitively interpretable.

### Fisher's Log-Series Alpha (α)

A parameter derived from fitting a log-series distribution to the species abundance data. Alpha is widely used in mycological studies as a diversity measure relatively insensitive to sample size.

### Brillouin Index (H_B)

Designed for non-random, complete enumeration of a collection. It is generally not recommended for fungal diversity studies, where sampling is inherently incomplete and random.

## Evenness Indices

Evenness quantifies how uniformly individuals are distributed among species, independent of richness:

- **Shannon evenness**: E = H' / ln S — ranges from 0 to 1
- **Hill evenness**: E = N₂ / N₁ — ratio of Simpson's to Shannon's effective numbers
- **McIntosh's evenness**: derived from the McIntosh diversity index relative to its maximum

## Jackknifing for Index Accuracy

Jackknifing (Zahl 1977) is a resampling technique that improves the accuracy of diversity index estimates without requiring assumptions about underlying species abundance distributions. By iteratively omitting subsets of the data and recalculating the index, jackknifing produces bias-corrected estimates and confidence limits — particularly valuable for Simpson's and Shannon's indices applied to fungal community data with limited replication.

## Choosing Among Indices

Selecting the appropriate diversity index depends on the research question and the characteristics of the fungal community being studied. A comparison of key indices based on their ability to discriminate among sites and sensitivity to sample size (Magurran 1988):

| Index | Site Discrimination | Sample Size Sensitivity |
|-------|-------------------|------------------------|
| Shannon (H') | Moderate | Moderate |
| Simpson (D) | Moderate | Low |
| McIntosh (U) | Good | Moderate |
| McIntosh (D) | Poor | Moderate |
| Berger-Parker (d) | Poor | Low |
| Fisher's α | Good | Low |

The McIntosh U index and Fisher's log-series alpha provide the best site discrimination with low to moderate sample size sensitivity, making them attractive choices for mycological studies where sample sizes may be constrained by culturing and identification bottlenecks. The Shannon and Simpson indices remain the most widely used, offering a balance of interpretability, statistical tractability, and ecological meaning.

## Scale-Dependence and Fungal Diversity

A critical consideration when applying these indices to fungal communities is that the effects of environmental variation on species density and numerical species richness are **scale-dependent** — the importance of different causal mechanisms depends on the spatial scale at which data are collected (Waide et al. 1999; Gross et al. 2000). Most ecological studies of fungi cover species densities as a consequence of sampling design, although this is rarely stated explicitly. Future research should always include an explicit definition of scale as well as the attribute of richness being evaluated, ensuring that diversity comparisons are made at ecologically meaningful and methodologically consistent scales.

## References

- Andrews, J.H. 1991. Comparative ecology of microorganisms and macroorganisms.
- Archibold, O.W. 1949. Species-area relationships in plant communities.
- Arrhenius, O. 1921. Species and area.
- Brillouin, L. 1956. *Science and Information Theory*.
- Colwell, R.K. & Coddington, J.A. 1994. Estimating terrestrial biodiversity through extrapolation.
- Gleason, H.A. 1922. On the relation between species and area.
- He, F. & Legendre, P. 1996. On species-area relations.
- Hurlbert, S.H. 1971. The nonconcept of species diversity.
- Kempton, R.A. 1979. Structure of species abundance and measurement of diversity.
- Ludwig, J.A. & Reynolds, J.F. 1988. *Statistical Ecology*.
- Magurran, A.E. 1988. *Ecological Diversity and Its Measurement*.
- May, R.M. 1975. Patterns of species abundance and diversity.
- Polishook, J.D. et al. 1996. Fungal diversity in decaying leaves from Puerto Rico.
- Rosenzweig, M.L. 1995. *Species Diversity in Space and Time*.
- Shannon, C.E. & Weaver, W. 1949. *The Mathematical Theory of Communication*.
- Simpson, E.H. 1949. Measurement of diversity.
- Zahl, S. 1977. Jackknifing an index of diversity.

## See Also

- [[mycology]]
- [[mycorrhiza]]
- [[basidiomycota]]
- [[ascomycota]]
- [[kingdom-fungi]]
