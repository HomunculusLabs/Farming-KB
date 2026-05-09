---
title: Fungal Species fungal species richness and diversity indices Indices
created: 2026-04-21
updated: 2026-04-21
type: concept
tags: [mycology, fungi]
sources: []
---
# Fungal Species Richness and Diversity Indices
Assessing patterns of [[biodiversity-fungal-biodiversity-estimation-methods]] requires analytical approaches
grounded in current methodologies of sampling design that account for
effects of scale on patterns of biodiversity. The parameters that define
a community and that are important for assessing biodiversity include
species composition, types and intensities of interspecific interactions,
and dynamics of those attributes over time and space.
## The Fungal Unit Problem
Most fungi consist of filaments (hyphae) forming mycelia capable of
essentially unlimited growth. This indeterminate body structure differs
significantly from most animals and plants, making the definition of an
"individual" problematic. Sporocarps of one basidiomycete species on a
forest floor can represent multiple ramets of a single genet or ramets
from multiple genets. Only molecular or isozymic analyses can untangle
genetic structure. A clearly stated operational definition of "individual"
relevant to the taxon of interest must be provided to facilitate
unambiguous comparisons among ecosystems.
## Species Richness
Three kinds of species richness can be distinguished:
1. **Numerical species richness:** Enumeration of species in a
   particular sample
2. **Species density:** Species per unit area, volume, weight, biomass,
   or number of individuals
3. **Total species richness:** Cumulative unique species from a series
   of samples
### Species-Effort Relationships
Three mathematical models predict how richness increases with sampling
effort:
- **Power model:** S = CA^z (Arrhenius 1921) — monotonically increasing
- **Exponential model:** S = C + z ln A (Gleason 1922, 1925) —
  monotonically increasing
- **Logistic model:** S = B/(C + A)^-z (Archibold 1949) — reaches
  asymptote
The logistic relation predicts that S eventually reaches a plateau,
providing an accurate estimate of true species richness. For
macrofungi, up to 8-12 years of sampling may be required to approach an
asymptote.
### Rarefaction
Rarefaction facilitates comparison of species richness among areas as
if they were based on a standardized sample size:
E(S) = Sum[1 - (C(N-Ni,n))/C(N,n)]
where E(S) is expected species in a rarified sample, n is the
standardized sample size, N is total isolates, and Ni is isolates per
species.
## Common Diversity Indices
### Simpson's Index
- Infinite populations: lambda = Sum(pi^2)
- Finite populations: D = Sum[ni(ni-1)] / [N(N-1)]
- Reciprocal form (1/D) increases with diversity
### Shannon Index
H' = -Sum[pi ln(pi)]
where pi is proportional abundance of each species. The most widely
used diversity index.
### Berger-Parker Index
d = Nmax/N where Nmax is the number of isolates in the most abundant
species. Reciprocal form most commonly used.
### Hill Numbers
- N1 = e^H' (based on Shannon)
- N2 = 1/D (based on Simpson)
### Evenness
Shannon evenness: E = H'/ln(S)
## Beta Diversity
Beta diversity measures species turnover among sites. Six commonly used
metrics use presence-absence data:
- **Whittaker:** bw = (S/a) - 1 — fulfills most criteria
- **Wilson and Shmida:** bT = [g(H) + l(H)]/2a — acceptable
- **Cody:** bc = [g(H) + l(H)]/2
- **Routledge measures:** br, bI, bE
## Resemblance Functions
Similarity indices quantify differences in species composition among
sites:
- **Dice:** DI = 2j/(2j + a + b)
- **Jaccard:** JI = j/(a + b - j)
- **Sorensen:** SI = 2j/(a + b) — recommended for binary data
- **Bray-Curtis:** Uses abundance data, recommended as dissimilarity
## Cluster Analysis
Cluster analysis groups objects into subgroups more similar to each
other than to objects in other subgroups. The unweighted pair group
method using arithmetic averages (UPGMA) provides a good starting
point. The cophenetic correlation coefficient quantifies how well the
dendrogram represents the multidimensional relationship among sites.
## Ordination Methods
Ordination techniques arrange sampling units in a low-dimensional space
to reveal patterns in [[core-endorhiza-bacterial-community-composition-cannabis]]. Principal Coordinates
Analysis (PCoA) and Non-metric Multidimensional Scaling (NMDS) are
widely used for fungal community data. NMDS is particularly popular
because it accommodates non-linear species responses and various
distance or dissimilarity measures. The stress value indicates goodness
of fit, with values below 0.2 generally considered acceptable for
ecological interpretation of fungal [[edaphic-determinants-cannabis-microbiome-community-structure]].
## Power Analysis
Power analysis is crucial for [[cannabis-microbiome-experimental-design]], helping to evaluate
relationships among sample sizes, effect magnitudes, variance,
significance levels, and statistical power. It is particularly
important for interpreting nonsignificant results in fungal biodiversity
studies.
## Metabarcoding and Molecular Diversity
The advent of high-throughput DNA sequencing has transformed fungal
[[ingham-soil-food-web-diversity-assessment-dna-molecular-methods]]. Environmental DNA metabarcoding using ITS primers
reveals cryptic diversity invisible to traditional fruiting body
surveys. However, molecular methods introduce new challenges including
primer bias, copy number variation, and the inability to distinguish
viable from dead biomass. Integrating morphological and molecular
approaches provides the most comprehensive [[monitoring-and-assessment-of-fungal-bioremediation]]
community diversity.
## Related
- [[biodiversity-fungal-species-abundance-diversity]]
- [[fungal-diversity-indices-community-analysis]]
- [[fungal-beta-diversity-species-turnover]]
