---
title: Fungal Beta Diversity and Species Turnover Analysis
created: 2026-04-21
updated: 2026-04-21
type: concept
tags: [[mycology, fungi]
sources: []
---

# Fungal Beta Diversity and Species Turnover Analysis

Beta diversity quantifies the degree of change in species composition between sites, habitats, or along environmental gradients. It is a critical concept for understanding how fungal communities are organized across landscapes.

## Whittaker's Hierarchical Diversity

Whittaker (1977) recognized that ecological diversity is scale-dependent:

- **Point diversity:** Diversity at a single location
- **Alpha diversity:** Within-habitat diversity (multiple samples within the same habitat type)
- **Beta diversity:** Between-habitat component — species turnover along gradients
- **Gamma diversity:** Total diversity of a site (multiple habitat types)
- **Delta diversity:** Between-landscape changes in species composition
- **Epsilon diversity:** Diversity of a large biogeographic region (e.g., a biome)

### Example: Fungi on Decaying Leaves
- Point diversity: fungal species on a single leaf
- Alpha diversity: fungi across multiple leaves of the same tree species
- Beta diversity: differences in fungal communities between leaf types in the same forest
- Gamma diversity: fungi across several forested locations
- Epsilon diversity: fungal species composition across all deciduous forests of eastern North America

## Species Abundance Distribution Models

Four models describe how species abundances are distributed within communities, from most to least equitable:

### 1. Geometric Series (Niche Preemption)
- Most successful species preempts a proportion of the total resource
- Next species claims the same proportion of the remainder
- Highest dominance, lowest evenness
- Typical of species-poor habitats or stress-tolerant communities
- Arises when species arrive regularly into unsaturated habitats

### 2. Log-Series
- A few species dominant; many rare species
- Related to the geometric model
- Typical of root-surface fungal assemblages
- May indicate nonequilibrial conditions
- Characteristic of Puerto Rican rainforest litter microfungi

### 3. Lognormal Distribution
- Multiple interacting factors control species abundances
- Most species of intermediate abundance
- Characteristic of species-rich habitats
- Lussenhop (1981): lognormal best described Wisconsin forest soil and rhizosphere fungi
- Warning: mixing samples from many microhabitats can artificially create lognormal distributions

### 4. Broken-Stick Model
- Most equitable distribution of abundances
- Species equally divide available resources
- Rare in nature; represents maximum evenness

## Beta Diversity Indices (Binary Data)

| Index | Formula Basis | Best Use |
|-------|--------------|----------|
| Whittaker (bw) | S/a - 1 | Most recommended; fewest restrictions |
| Wilson-Shmida (bt) | [g(H)+l(H)]/2a | Acceptable alternative |
| Cody (bc) | [g(H)+l(H)]/2 | Species gain/loss along transects |
| Routledge (br) | S2/(2r+S) - 1 | Emphasizes species overlap |

Where S = total species, a = average sample diversity, g(H) = species gained, l(H) = species lost.

### Limitations
- All species contribute equally regardless of abundance
- Binary data indices may overestimate similarity compared to abundance-based measures
- Sorensen's Index recommended when only binary data available

## Cluster Analysis for Fungal Communities

Cluster analysis represents patterns of species composition among sites as a dendrogram:

1. **Input:** Dissimilarity/similarity matrix derived from species composition data
2. **Method:** UPGMA (unweighted pair group method with arithmetic averages) most commonly used
3. **Output:** Dendrogram showing hierarchical grouping of sites by species similarity
4. **Validation:** Cophenetic correlation coefficient quantifies how well the dendrogram represents multidimensional relationships

### Resemblance Functions
Similarity, distance, and dissimilarity coefficients quantify relationships between samples:
- **Sorensen's coefficient:** Based on shared species; commonly used
- **Jaccard's coefficient:** Similar to Sorensen but different formula
- **Bray-Curtis:** Uses abundance data; most widely used distance measure
- **Euclidean distance:** Simple geometric distance; sensitive to sample size
- **Chord distance:** Normalized Euclidean distance; reduces sample-size effects
- **Canberra metric:** Gives more weight to rare species

### Important Considerations
- The pattern detected is only as reliable as the input data
- Results affected strongly by the resemblance function chosen
- Cluster analysis compresses multidimensional relationships into one dimension — information is lost
- Choice of sites, species included, and resemblance function should be considered carefully

## Power Analysis in Fungal Diversity Studies

Power analysis helps distinguish between:
1. No real biological differences exist
2. Sample sizes too small to detect real differences

### Key Factors Affecting Power
- Sample size (larger = more power)
- Magnitude of effect (larger differences = more power)
- Sample variance (lower = more power)
- Alpha level (higher = more power, but more Type I errors)
- Statistical test used (parametric > nonparametric when assumptions met)

### When to Use
- **Before study:** Determine optimal sample sizes and resource allocation
- **After study:** Interpret biological meaning of nonsignificant results

Software available: nQuery Advisor, PASS, SPSS, and others.

## See Also

- [[fungal-species-richness-and-diversity-indices]]
- [[fungal-biodiversity-forest-floor]]
- [[biodiversity-of-fungi-soil-fungal-communities-agriculture]]
- [[alpha-beta-gamma-diversity-fungi]]
