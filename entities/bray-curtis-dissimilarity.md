---
title: Bray-Curtis Dissimilarity
source: unknown-biodiversity-of-fungi.md
type: entity
---

## Description

The Bray-Curtis dissimilarity index is a quantitative ecological metric used to measure the compositional dissimilarity between two sites or samples based on species abundance data. Originally developed by Bray and Curtis in 1957 as a modification of the Sorensen index, it is one of the most widely used distance measures in community ecology and multivariate analysis of [[fungal-biodiversity]].

## Classification

- **Category**: Ecological distance metric
- **Data type**: Quantitative (abundance-based) or binary (presence-absence)
- **Related indices**: Sorensen index, Jaccard index, Morisita-Horn index
- **Application domain**: Community ecology, fungal biodiversity assessment, multivariate statistics

## Historical Context (Bray & Curtis 1957)

The Bray-Curtis dissimilarity was introduced by J. Roger Bray and John T. Curtis in their seminal 1957 paper "An Ordination of the Upland Forest Communities of Southern Wisconsin," published in *Ecological Monographs*. Their work was motivated by the need for a quantitative, abundance-weighted measure that could be applied to vegetation survey data for ordination and [[cluster-analysis-fungal-biodiversity-classification|cluster analysis]]. The index was conceived as a modification of the Sorensen (1948) coefficient of community, extending it from binary presence-absence data to incorporate species abundance information. Bray and Curtis demonstrated the index as part of their pioneering approach to vegetation ordination, showing that ecological communities could be arranged along continua rather than classified into discrete types — a paradigm shift in plant ecology that later influenced mycological community analysis.

## Mathematical Formula

The Bray-Curtis dissimilarity between two samples *i* and *j* is defined as:

$$BC_{ij} = \frac{\sum_{k=1}^{S} |x_{ik} - x_{jk}|}{\sum_{k=1}^{S} (x_{ik} + x_{jk})}$$

Where:
- $x_{ik}$ is the abundance of species *k* in sample *i*
- $x_{jk}$ is the abundance of species *k* in sample *j*
- *S* is the total number of species across both samples

An equivalent formulation commonly used in practice:

$$BC_{ij} = 1 - \frac{2W}{A + B}$$

Where:
- $W = \sum_{k} \min(x_{ik}, x_{jk})$, the sum of the lesser abundances for each shared species
- $A = \sum_{k} x_{ik}$, the total abundance in sample *i*
- $B = \sum_{k} x_{jk}$, the total abundance in sample *j*

The Bray-Curtis percentage dissimilarity (PD) is expressed as $PD = 100 \times BC_{ij}$, while the Bray-Curtis similarity index is $SI = 100 - PD$.

## Properties and Characteristics

- **Range**: The index yields values from 0 (identical community composition and abundance) to 1 (completely dissimilar, no shared species)
- **Semi-metric**: Bray-Curtis is a semi-metric distance; it does not satisfy the triangle inequality, meaning that the distance from A to B plus the distance from B to C may be less than the distance from A to C
- **Abundance-weighted**: Unlike binary [[similarity-distance-measures-fungal-ecology|similarity measures]], Bray-Curtis incorporates quantitative abundance data, making it sensitive to shifts in dominant species
- **Compositional sensitivity**: Emphasizes changes in the most abundant species, which often drive ecological patterns
- **Normalization-free**: The denominator automatically normalizes for total sample abundance, reducing the influence of sample size differences
- **Robustness**: Relatively robust to moderate levels of sampling noise, though sensitive to undersampling of rare species
- **Units**: Dimensionless — the ratio structure eliminates the effect of absolute abundance scales
- **Monotonicity**: A monotonic transformation of the Sorensen index when applied to binary data, reducing to Sorensen dissimilarity in the presence-absence case

## Applications in Mycological Research

Bray-Curtis dissimilarity has become a standard tool in mycological community ecology. Key applications include:

- **Substrate comparison**: Quantifying fungal community differences across [[composting]] stages, [[substrate-preparation]] methods, and organic matter types
- **Soil fungal diversity**: Comparing [[soil-horizons]] and soil microhabitat fungal assemblages using culture-independent (molecular) and culture-dependent datasets
- **Successional studies**: Tracking changes in fungal community composition across temporal gradients, including [[mycorrhizae-plant-succession-regulation|successional stages]] in deadwood decomposition and forest stand development
- **Geographic comparisons**: Assessing [[alpha-beta-gamma-diversity-fungi|beta diversity]] among geographically separated fungal communities in different forest types, elevational gradients, or biomes
- **Mycorrhizal ecology**: Comparing arbuscular mycorrhizal (AMF) and ectomycorrhizal fungal communities across host plant species and soil conditions
- **Disturbance assessment**: Evaluating the impact of fire, logging, pollution, or land-use change on fungal community structure
- **[[accessible-mushroom-cultivation-for-disabilities]]**: Monitoring community shifts during substrate colonization, identifying contaminant organisms, and optimizing growing conditions
- **Metagenomic studies**: Applied to high-throughput sequencing (HTS) amplicon data (e.g., ITS, 18S) for beta diversity estimation in environmental samples

## Comparison with Other Distance Measures

| Measure | Data Type | Metric? | Abundance-weighted? | Notes |
|---------|-----------|---------|---------------------|-------|
| **Bray-Curtis** | Quantitative | Semi-metric | Yes | Emphasizes dominant species; widely recommended |
| Jaccard | Binary | Metric | No | Presence-absence only; ignores abundance |
| Sorensen | Binary | Semi-metric | No | Closely related to Bray-Curtis; binary equivalent |
| Morisita-Horn | Quantitative | Metric | Yes | Less sensitive to sample size; emphasizes dominant species |
| Euclidean | Quantitative | Metric | Yes | Sensitive to total abundance; not composition-focused |
| Chi-squared | Quantitative | Metric | Yes | Emphasizes rare species; suitable for correspondence analysis |
| [[distance-coefficients-fungal-community-comparison|Gower]] | Mixed | Metric | Partial | Handles mixed data types; flexible weighting |

Ludwig and Reynolds (1988) recommended Bray-Curtis over relative Euclidean distance for ecological analyses because it better captures compositional differences independent of total sample abundance. Faith et al. (1987) found Bray-Curtis to be among the best-performing distance measures for recovering ecological gradients.

## Limitations

- **Semi-metric nature**: Because Bray-Curtis does not satisfy the triangle inequality, it is technically unsuitable for methods that assume Euclidean geometry (e.g., principal components analysis on the distance matrix itself). Workarounds include Principal Coordinates Analysis (PCoA) with appropriate corrections.
- **Dominant species bias**: The abundance-weighting disproportionately reflects changes in the most abundant taxa, potentially obscuring turnover among rare species that may be ecologically significant.
- **Sample completeness sensitivity**: As with all abundance-based indices, undersampling can inflate dissimilarity estimates, particularly in hyperdiverse fungal communities where rare species constitute a large fraction of diversity.
- **Zero-inflation**: In sparse datasets common to fungal metabarcoding, many zero-zero matches (species absent from both samples) do not contribute to the index, which can distort comparisons among depauperate samples.
- **Non-Euclidean embeddability**: Distance matrices built from Bray-Curtis may produce negative eigenvalues in PCoA, requiring square-root transformation or use of modified distances for proper ordination.
- **Transformation dependence**: Results can be sensitive to whether raw abundances, log-transformed, or presence-absence data are used, requiring careful preprocessing decisions.

## Relationship to Cluster Analysis

Bray-Curtis dissimilarity is extensively used as the distance input for hierarchical [[cluster-analysis-fungal-biodiversity-classification|cluster analysis]] of fungal communities. Common clustering algorithms paired with Bray-Curtis include:

- **UPGMA** (Unweighted Pair Group Method with Arithmetic Mean): The most common agglomerative method for ecological dendrograms
- **Ward's method**: Minimizes within-cluster variance; requires metric distances (a square-root transformation of Bray-Curtis is sometimes applied)
- **Single/complete linkage**: Useful for identifying outliers or compact clusters in community data
- **k-means clustering**: Requires Euclidean distances; a square-root or Wisconsin double-standardization of Bray-Curtis may be applied first

The resulting dendrograms reveal groupings of similar fungal communities, which can then be related to environmental gradients, [[whittaker-beta-diversity|Whittaker beta diversity]] patterns, or experimental treatments. When combined with SIMPROF (similarity profile) tests, Bray-Curtis cluster analysis provides statistically rigorous community classification.

## Key Facts

- Calculated as PD = 100 - SI, where SI = (2W / (a + b)) × 100
- W is the sum of lower abundances of shared species; a and b are total abundances at each site
- Can be rescaled from 0 to 1 by subtracting the similarity index from 1
- Values range from 0 (identical composition) to 1 (completely dissimilar)
- Recommended by Ludwig and Reynolds (1988) as an alternative to relative Euclidean distance measures
- Incorporates abundance information rather than just presence-absence, unlike binary indices
- Suitable for cluster analysis and ordination as a metric coefficient
- Reduces to the Sorensen index when applied to binary (presence-absence) data

## Relevance to Cultivation and Mycology

The Bray-Curtis index is directly applicable to comparing fungal communities across different cultivation substrates, environmental conditions, or geographic locations. In [[accessible-mushroom-cultivation-for-disabilities]], it can quantify how similar or different fungal communities are between substrate preparations, [[composting]] stages, or growing environments. For mycological biodiversity surveys, the index provides a robust measure for comparing species composition and abundance across forest types, [[soil-horizons]], or successional stages. Its use with quantitative data makes it superior to binary indices for detecting subtle community shifts.

## See Also

- [[cluster-analysis-fungal-biodiversity-classification]]
- [[distance-coefficients-fungal-community-comparison]]
- [[similarity-distance-measures-fungal-ecology]]
- [[whittaker-beta-diversity]]
- [[alpha-beta-gamma-diversity-fungi]]
- [[fungal-biodiversity]]
- [[species-abundance-distribution]]
