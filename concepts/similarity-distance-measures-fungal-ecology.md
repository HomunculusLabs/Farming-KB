---
title: Similarity and Distance Measures in Fungal Community Ecology
source: unknown-biodiversity-of-fungi.md
type: concept
---

# Similarity and Distance Measures in Fungal Community Ecology

[[distance-coefficients-fungal-community-comparison|Similarity and distance coefficients]] are fundamental tools in [[fungal-diversity-fire-ecology|fungal community ecology]]
for comparing species assemblages across samples, sites, or environmental gradients.
They reduce complex multivariate data into pairwise indices used as input for
**ordination**, **[[cluster-analysis-fungal-biodiversity-classification]]**, and hypothesis testing. The choice depends on
whether data are binary (presence–absence) or quantitative (abundance-based).

## Overview and Purpose

When mycologists collect fungal inventories, metabarcoding data, or culture-based
isolates, they need objective measures to ask: *How similar are the fungal
communities at site A and site B?* Similarity ranges from 0 to 1; distance is the
complement.

These pairwise matrices are used to:
- **Cluster** sites into groups with similar assemblages (UPGMA, Ward's method)
- **Ordinate** samples along reduced-dimension axes (NMDS, PCoA)
- **Test hypotheses** about environmental drivers (PERMANOVA, Mantel tests)
- **Track temporal changes** across seasons or successional stages

---

## Binary (Presence–Absence) Similarity Coefficients

Binary coefficients operate on species-by-sample matrices coded as 1 (present) or 0
(absent). For two samples *j* and *k*:

| Symbol | Meaning |
|--------|---------|
| **a** | Species present in **both** samples |
| **b** | Species present only in sample j |
| **c** | Species present only in sample k |
| **d** | Species absent from both samples |

### Jaccard Coefficient

One of the most widely used indices in [[fungal-ecology]]:

$$C_J = \frac{a}{a + b + c}$$

Considers only shared and unique species, ignoring joint absences (*d*). Values range
from 0 to 1. Appropriate when the total species pool is unknown.

### Sørensen Coefficient

Gives more weight to shared species than Jaccard:

$$C_S = \frac{2a}{2a + b + c}$$

Values are consistently higher than Jaccard for the same data. Preferred by many mycologists
because its emphasis on co-occurrence aligns with ecological intuition.

### Ochiai Coefficient

The geometric mean of the proportions of shared species in each sample:

$$C_O = \frac{a}{\sqrt{(a + b)(a + c)}}$$

Ranges from 0 to 1; equivalent to cosine similarity of two binary vectors.
Useful when sample sizes differ substantially.

### Simple Matching Coefficient

$$C_{SM} = \frac{a + d}{a + b + c + d}$$

Includes joint absences as agreement, inflating similarity when the species pool is
large and most species are rare. Generally **not recommended** unless the
total pool is comprehensively known.

---

## Quantitative (Abundance-Based) Measures
When abundance data are available — colony-forming units, sequence read counts, or
basidiocarp counts — quantitative coefficients incorporate magnitude
of differences.

### Percent Similarity (Renkonen Index)

Sums the minimum abundance across all shared species:

$$PS_{jk} = \sum_{i=1}^{S} \min(X_{ij},\, X_{ik})$$

where $X_{ij}$ is the abundance of species *i* in sample *j*. When expressed as
proportions, ranges from 0 to 1. Widely used for comparing dominance structures.

### Euclidean Distance

Treats each sample as a point in *S*-dimensional species space:

$$D_E = \sqrt{\sum_{i=1}^{S} (X_{ij} - X_{ik})^2}$$

Sensitive to species with large abundances; best with standardized data.

### Cosine Similarity

Measures the angle between two species-abundance vectors:

$$\text{ccos}_{jk} = \sum_{i=1}^{S}(X_{ij} \times X_{ik}) - \sum(X_{ij})\sum(X_{ik})$$

After normalization, ranges from −1 to +1. Less sensitive to total abundance
differences than Euclidean distance.

### Geodesic Distance (GDD)

$$\text{GDD}_{jk} = \arccos(\text{cosine similarity}_{jk})$$

Values range from 0 (identical) to approximately 1.57 (π/2; maximally dissimilar).
Provides a well-bounded metric distance useful for ordination and clustering.

### [[bray-curtis-dissimilarity|Bray–Curtis Dissimilarity]]

Among the most widely used [[quantitative-indices-fungal-diversity|quantitative indices]] in fungal ecology. Bounded 0 to 1, it
gives less weight to dominant species than Euclidean distance and handles
heterogeneous, zero-inflated datasets typical of fungal studies well.

---

## Choosing Between Binary and Quantitative Measures
| Consideration | Binary Measures | Quantitative Measures |
|---|---|---|
| **Data type** | Presence–absence (e.g., checklists) | Abundance (e.g., reads, CFU) |
| **Ecological focus** | Which species occur | How abundant each species is |
| **Noise sensitivity** | Robust to uneven effort | Sensitive to sampling depth |
| **Recommended** | Jaccard, Sørensen | Bray–Curtis, Percent Similarity, GDD |

Many studies compute **both** to disentangle compositional turnover from dominance
changes. A site pair may share most species (high Jaccard) but differ in dominance
(low Percent Similarity), revealing replacement vs. nestedness patterns.

---

## Applications in Fungal Ecology
- **Ordination** (NMDS, PCoA) of assemblages across [[soil-ph]], host species, or land use
- **[[cluster-analysis-fungal-biodiversity-classification]]** to identify community types (tropical vs. temperate)
- **Temporal comparisons** of seasonal succession in ectomycorrhizal communities
- **Biogeographic analyses** comparing fungal floras across continents or islands

## See Also

- Ordination methods in fungal ecology
- [[cluster-analysis-fungal-biodiversity-classification|Cluster analysis]] of community data
- DNA metabarcoding and sequence-based fungal surveys
- [[alpha-beta-gamma-diversity-fungi|Alpha]] and [[alpha-beta-gamma-diversity-fungi|beta diversity]]
