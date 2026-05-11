# Fungal Beta Diversity and Similarity Indices: Measuring Species Turnover

## Overview

Beta diversity quantifies the degree of species turnover between sites or along [[fungal-adaptations-environmental-gradients]]. In mycology, beta diversity measures are essential for comparing [[biodiversity-fungi-soil-fungal-communities]] across habitats, assessing the impact of environmental gradients, and evaluating the effectiveness of [[endangered-fungi-and-conservation-strategies]]. The foundational work by Whittaker (1977) and subsequent refinements by Zak and Willig in *[[biodiversity-of-fungi-biodiversity-patterns-ecosystems]]* provide the framework for these analyses.

## Defining Beta Diversity

### Whittaker's Framework

R.H. Whittaker (1977) proposed a multi-scale diversity framework:
- **[[alpha-diversity-gradient-bulk-soil-cannabis-endorhiza]]**: Species richness within a single, homogeneous habitat
- **Beta diversity**: The degree of species turnover between different habitats or along environmental gradients
- **[[alpha-beta-gamma-diversity-fungi]]**: The total species richness across all habitats in a landscape
- **Delta diversity**: Geographic turnover of species across regional boundaries
- **Epsilon diversity**: The total diversity of a geographic region

The relationship is expressed as: gamma diversity = alpha diversity × beta diversity. Alternatively, beta diversity can be conceptualized as the extent to which species composition changes as one moves between sites along a gradient.

### Interpretation

When two sites share few species, beta diversity is high. When they share many species, beta diversity is low.

## Binary Beta Diversity Indices

Six commonly used metrics employ presence-absence data (Table 5.4 in Zak & Willig):

### Whittaker's Measure

```
bw = (S/a) - 1
```
Where S is total species (gamma diversity) and a is average species richness per site (alpha diversity). Whittaker's measure fulfills most criteria for an effective index and has fewest restrictions among binary measures.

### Cody's Measure

```
bc = [g(H) + l(H)] / 2
```
Where g(H) is species gained along a transect and l(H) is species lost. This index explicitly tracks gains and losses.

### Wilson and Shmida's Measure

```
bT = [g(H) + l(H)] / 2a
```
Similar to Cody's but standardized by alpha diversity.

### Routledge's Measures

Three indices use different mathematical approaches:
- **br**: Based on species pair overlap counts
- **bI**: Based on information theory
- **bE**: Exponential form of bI

### Limitations of Binary Indices

All binary indices share a critical disadvantage: species contribute equally regardless of abundance. This can produce misleading results in fungal studies where abundance varies enormously.

## Resemblance Functions: Similarity Indices

### Overview

Similarity, distance, and dissimilarity coefficients provide an alternative approach to quantifying beta diversity. Approximately 20 similarity indices exist in the ecological literature, differing in how they weight shared occurrences versus shared absences.

### The Four Major Binary Similarity Indices

**Dice Index**:
```
DI = 2j / (2j + a + b)
```

**Jaccard Index**:
```
JI = j / (a + b - j)
```

**Ochiai Index**:
```
OI = j / √[(j + a)(j + b)]
```

**Sørensen Index**:
```
SI = 2j / (a + b)
```

Where j = species in common between two sites, a = species in site A only, b = species in site B only.

### Metric (Abundance-Based) Indices
