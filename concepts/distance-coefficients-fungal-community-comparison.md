---
title: "Distance and Dissimilarity Coefficients for Fungal Community Comparison"
source: "unknown-biodiversity-of-fungi.md, Chunks 20-21"
type: "concept"
---

# Distance and Dissimilarity Coefficients for Fungal Community Comparison

Distance (dissimilarity) coefficients quantify how different two fungal communities are
based on species composition and abundance. The choice of coefficient directly
influences ordination results, [[cluster-analysis-fungal-biodiversity-classification]], and ecological conclusions. This page
reviews the major coefficients used in [[fungal-ecology]] and recommendations for use.

## Matrix-Based Calculation Approach

All distance coefficients operate on a community data matrix where **sites (samples)
form columns** and **species form rows**. Each cell $x_{ij}$ contains the abundance of
species $i$ at site $j$. A pairwise distance matrix is computed by comparing every
column to every other, producing a symmetric dissimilarity matrix for downstream
multivariate analyses (clustering, ordination).

## [[similarity-distance-measures-fungal-ecology|Relationship Between Similarity]] and Distance

Similarity and distance are complementary measures. For communities $j$ and $k$:

$$\text{Distance} = 1 - \text{Similarity}$$

Some indices express similarity on a 0–1 scale, while others use 0–100 (percentage
scale), giving $\text{PD} = 100 - \text{SI}$. Note which convention a coefficient uses
before interpreting results.

## Euclidean Distance Coefficients

Euclidean distances measure straight-line distance between sites in species space.
They are geometrically intuitive but share a key weakness: sensitivity to double-zero
coincidences (joint absences), which are ecologically meaningless.

### Euclidean Distance (ED)

$$\text{ED}_{jk} = \sqrt{\sum_{i=1}^{p}(x_{ij} - x_{ik})^2}$$

ED treats each species as an independent axis and is sensitive to total abundance
differences and double zeros.

### Squared Euclidean Distance (SED)

$$\text{SED}_{jk} = \sum_{i=1}^{p}(x_{ij} - x_{ik})^2$$

SED omits the square root, giving greater weight to large differences. Mathematically
simpler but less interpretable in ecological terms.

### Mean Euclidean Distance (MED)

$$\text{MED}_{jk} = \sqrt{\frac{1}{p}\sum_{i=1}^{p}(x_{ij} - x_{ik})^2}$$

MED normalizes by species count, producing a scale independent of [[species-richness-diversity-indices-fungi]].

### Mean Absolute Distance (MAD)

$$\text{MAD}_{jk} = \frac{1}{p}\sum_{i=1}^{p}|x_{ij} - x_{ik}|$$

MAD uses absolute differences (Manhattan metric averaged over species), making it more
robust to outlier species with very large abundances.

## [[bray-curtis-dissimilarity|Bray-Curtis]] Dissimilarity Index

Bray-Curtis (percent difference, PD) is among the most widely used [[fungal-ecological-operational-groups-biodiversity-inventory]]
coefficients:

$$\text{PD}_{jk} = \frac{\sum_{i=1}^{p}|x_{ij} - x_{ik}|}{\sum_{i=1}^{p}(x_{ij} + x_{ik})}$$

Expressed via similarity index (SI): $\text{PD} = 100 - \text{SI}$ or $\text{PD} = 1
- \text{SI}$, depending on scale. Bray-Curtis ranges from 0 (identical) to 1
(completely dissimilar), ignores double zeros, and handles differing site totals well.

## Relative Euclidean Distance Coefficients

The RE group corrects standard Euclidean sensitivity to total abundance differences.

### Relative Euclidean Distance (RED)

RED rescales each site vector to unit length before computing Euclidean distance,
removing sample-size influence and comparing relative composition.

### Relative Absolute Distance (RAD)

RAD similarly rescales site vectors but uses the absolute-difference (Manhattan)
framework, focusing on compositional differences rather than total abundance.

## Cord Distance

Cord distance derives from the cosine of the angle between site vectors:

$$\text{CRD}_{jk} = 2(1 - \cos_{jk})$$

where $\cos_{jk}$ is the cosine coefficient. Ranges from 0 (identical) to 2
(completely dissimilar with standardized data). Insensitive to double zeros and site
totals, making it well suited for ecological community data.

## Geodesic Distance

Geodesic distance is the arc length on the unit hypersphere between standardized
site vectors:

$$\text{GDD}_{jk} = \arccos(\cos_{jk})$$

GDD ranges from 0 (identical) to $\pi/2$ (maximally dissimilar). It provides a direct
angular measure of compositional difference and is monotonically related to cord
distance.

## Metric vs. Nonmetric Coefficients

A coefficient is **metric** if it satisfies: (1) non-negativity ($d_{jk} \geq 0$,
zero only when $j = k$), (2) symmetry ($d_{jk} = d_{kj}$), and (3) the triangle
inequality ($d_{jl} \leq d_{jk} + d_{kl}$). All coefficients here are symmetric and
non-negative, but some fail the triangle inequality. Metric distances are required for
PCoA; nonmetric distances may require NMDS.

## Suitability Recommendations (Ludwig and Reynolds, 1988)

Ludwig and Reynolds (1988) provided key guidance for community ecology:

- **Avoid standard Euclidean distances** (ED, SED, MED, MAD) for biodiversity data.
  Sensitivity to double zeros and total abundance produces misleading results.
- **The RE group (RED, RAD) performs well** — they correct for sample-size effects
  and handle abundance data effectively.
- **Cord distance is the best overall** coefficient for fungal communities. It ignores
  double zeros, is independent of site totals, and satisfies metric properties.
- **Bray-Curtis is an excellent alternative** — widely adopted, intuitive, and
  comparable to cord distance, though it may violate the triangle inequality.

## When to Use Each Metric

| Coefficient | Best Use Case | Caution |
|---|---|---|
| **ED / SED** | Rarely appropriate for ecology | Double zeros, total abundance sensitivity |
| **MED / MAD** | General dissimilarity (non-ecological) | Same issues as ED |
| **Bray-Curtis** | Abundance-based community data | Triangle inequality may fail |
| **RED / RAD** | Standardized compositional comparison | Requires careful data preparation |
| **Cord distance** | Default choice for fungal communities | Standardize input for full benefit |
| **Geodesic distance** | Angular compositional difference | Fewer software implementations |

## Summary

Cord distance and Bray-Curtis dissimilarity are the recommended first choices for
fungal community comparison, with the Relative Euclidean group as strong alternatives.
Standard Euclidean distances should be avoided for [[fungal-biodiversity]] studies. The data
matrix convention of sites as columns and species as rows is universal across all
these coefficients.
