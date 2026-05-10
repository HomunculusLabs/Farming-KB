# Species-Abundance Distributions and Diversity Indices for Fungal Communities

## Overview

Species diversity indices compress complex community data into single values for comparison between sites. However, they discard important information about how individuals are distributed among species. Species-abundance distributions, in contrast, use all available data to characterize community structure and organization. This approach, advocated by May (1975, 1981), Southwood (1978), and Magurran (1988), provides the most complete assessment of fungal community diversity.

## The Limitation of Diversity Indices

Diversity indices combine two distinct components:
1. **Species richness**: The number of species present
2. **Evenness**: How equitably individuals are distributed among species

The evenness component is calculated as:
```
e = Diversity observed / Diversity maximum
```
Where Dmax assumes each taxon has 1/S of total abundance.

The problem: compressing community data to a single value conveys little about the underlying structure. Two communities with identical diversity indices can have radically different species compositions and abundance patterns.

## The Four Major Species-Abundance Models

### 1. Geometric Series

The geometric series model describes communities where a few dominant species account for most individuals:
- The most abundant species takes a proportion k of available resources
- The second most abundant takes k of the remainder, and so on
- This produces a steep rank-abundance curve
- Ecological interpretation: communities in harsh or disturbed environments where only a few species can tolerate conditions
- In mycology: typical of polluted or heavily disturbed fungal communities

### 2. Logarithmic (Log) Series

Fisher et al. (1943) first recognized that plotting species number against relative abundance produces a characteristic pattern:
- The log-series parameter alpha serves as a diversity index
- Taylor (1978) strongly supported its use due to good discriminant ability
- It is less affected by common species abundance than Shannon or Simpson indices
- Disadvantage: assumes a specific distribution and is unaffected by evenness
- Two communities with the same N and S but different evenness will have identical alpha values

### 3. Broken-Stick Model

The broken-stick model represents a theoretical equilibrium where resources are divided randomly among species:
- Produces a moderate rank-abundance curve, more even than geometric but less than lognormal
- Rarely observed in nature but serves as a useful null hypothesis
- In mycology: represents an idealized community with no strong competitive hierarchy

### 4. Lognormal Distribution

Preston (1948) showed that species-abundance distributions often follow lognormal functions:
- Most species are of intermediate abundance, with few very rare and few very common species
- The canonical lognormal has a specific relationship between total individuals (N), number of species (S), and the modal octave
- Represents species-rich, stable communities with complex niche partitioning
- In mycology: typical of mature forest floor fungal communities with diverse niches

### Ecological Interpretation of Each Model

| Model | Species Pattern | Typical Environment | Fungal Example |
|-------|----------------|-------------------|----------------|
| Geometric | Few dominant species | Harsh, disturbed | Post-fire fungal community |
| Log series | Many rare species | Species-rich, variable | Tropical leaf litter fungi |
| Broken-stick | Even distribution | Theoretical equilibrium | Rare in fungal studies |
| Lognormal | Bell curve of abundances | Stable, mature | Old-growth forest floor |

## Fitting Models to Fungal Data

### Methodological Considerations

When fitting species-abundance distributions to fungal data:
- Taxonomic units must be consistently applied
- Isolates obtained from litter or soil should not be combined into a single morphospecies group
- Both morphological and molecular identification should be used when possible
- Sample size affects which distribution best fits the data

### Statistical Testing

Goodness-of-fit tests compare observed distributions to each model:
- Chi-square tests for categorical abundance classes
- Kolmogorov-Smirnov tests for continuous distributions
- Likelihood ratio tests compare model fits
- Expected values for each model can be compared using the G-test (Sokal and Rohlf 1995)

### Challenges Specific to Fungi

- Fruiting body surveys underestimate rare species that are not fruiting during the survey period
- Culture-based methods introduce bias toward fast-growing species
- Molecular methods detect unculturable species but may overrepresent certain taxa due to primer bias
- Combining methods provides the most complete picture but complicates distribution fitting

## Common Diversity Indices and Their Properties

### Shannon Index (H')

Widely used but sensitive to sample size:
- Combines richness and evenness into a single value
- Units are "bits per individual" (log base 2) or "nats per individual" (natural log)
- Overweights rare species relative to their ecological importance

### Simpson Index (D or λ)

Measures the probability that two randomly selected individuals belong to different species:
- Less sensitive to sample size than Shannon
- Overweights common species
- The complement (1 - D) or reciprocal (1/D) are often used for easier interpretation

### Berger-Parker Index

The proportional importance of the most abundant species:
- Simple to calculate and interpret
- Independent of species richness but influenced by sample size
- Useful as a quick dominance indicator

### Hill's Numbers (N0, N1, N2)

Ludwig and Reynolds (1988) recommended these as the most ecologically interpretable:
- **N0**: Species richness (count of all species)
- **N1**: Number of abundant species (exponential of Shannon index)
- **N2**: Number of very abundant species (reciprocal of Simpson index)
- Units are "number of species," making results intuitively meaningful
- The relationship N0 ≥ N1 ≥ N2 always holds

### McIntosh Index

Reflects the Euclidean distance of the sample from the origin in species-abundance space:
- Easy to calculate but strongly influenced by sample size
- Less commonly used in mycological studies

## Jackknife Estimation

For estimating confidence intervals around diversity indices:
- Pseudovalue approach creates n jackknifed values from n samples
- Each pseudovalue: VPi = (nV) - [(n - 1)(VJi)]
- Mean of pseudovalues is the best diversity estimate
- Confidence limits use the t-distribution with n-1 degrees of freedom
- Minimum 15 samples recommended; small datasets may overestimate diversity

Magurran (1988) urged caution with jackknifed Shannon and Simpson estimates, as the technique can produce ecologically absurd results.

## See Also

- [[fungal-beta-diversity-similarity-indices-zak-willig]]
- [[fungal-species-richness-and-diversity-indices]]
- [[fungal-biodiversity-species-estimation]]
- [[biodiversity-fungal-biodiversity-estimation-methods]]
- [[fungal-biodiversity-data-analysis]]
