# Fungal Beta Diversity and Similarity Indices: Measuring Species Turnover

## Overview

Beta diversity quantifies the degree of species turnover between sites or along environmental gradients. In mycology, beta diversity measures are essential for comparing fungal communities across habitats, assessing the impact of environmental gradients, and evaluating the effectiveness of conservation strategies. The foundational work by Whittaker (1977) and subsequent refinements by Zak and Willig in *Biodiversity of Fungi* provide the framework for these analyses.

## Defining Beta Diversity

### Whittaker's Framework

R.H. Whittaker (1977) proposed a multi-scale diversity framework:
- **Alpha diversity**: Species richness within a single, homogeneous habitat
- **Beta diversity**: The degree of species turnover between different habitats or along environmental gradients
- **Gamma diversity**: The total species richness across all habitats in a landscape
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

**Bray-Curtis** (modification of Sørensen):
```
BCI = 2W / (a + b)
```
Where W = sum of lower abundances of shared species. Frequencies of occurrence can substitute for abundances.

**Morisita-Horn**:
```
CMH = 2Σ(ani·bni) / [(da + db)(aN·bN)]
```
Where aN, bN are total individuals in each site; ani, bni are individuals of species i; da, db are calculated dominance measures.

**Renkonen Index**:
```
P12 = Σmin(p1i, p2i)
```
Where p1i, p2i are proportional representations of species i in each site.

### Critical Limitations

Magurran (1988) reported that binary similarity indices generally give misleading results, indicating higher similarity than actually exists. Tulloss (1997) reviewed 15 similarity indices and found all unsatisfactory due to insensitivity to the relative sizes of species lists being compared.

## Tulloss's Tripartite Similarity Index

Standard similarity indices fail to account for differences in species list sizes and proportional representation. Tulloss (1997) proposed the Tripartite Similarity Index:
```
T = U × S × R
```

Where U, S, and R are cost functions addressing each of the three insensitivities:

- **U** (size disparity): Reduces similarity when species list sizes differ greatly
- **S** (shared-species proportion): Accounts for the proportion of shared species relative to the smaller list
- **R** (representation balance): Ensures sensitivity to how well each list represents its community

## Application to Mycology

The Tripartite Index is particularly relevant for fungal community studies where sampling effort often varies between sites, rare species detection is uneven, and standard indices may overstate similarity between incompletely sampled assemblages.

## Practical Considerations for Fungal Studies

### Recommended Approach

1. Use abundance-based indices (Bray-Curtis, Morisita-Horn) when abundance data are available
2. Apply the Tripartite Index for presence-absence data to avoid overestimating similarity
3. Report multiple indices to allow comparison across studies
4. Clearly document sampling methods, as index values are not comparable across different sampling protocols

## See Also

- [[fungal-biodiversity-species-estimation]]
- [[fungal-beta-diversity-species-turnover]]
- [[fungal-species-richness-and-diversity-indices]]
- [[biodiversity-fungal-biodiversity-estimation-methods]]
- [[biodiversity-fungi-soil-fungal-communities]]
