# Species-Abundance Distributions and Diversity Indices for Fungal Communities

## Overview

Species diversity indices compress complex community data into single values for comparison between sites. However, they discard important information about how individuals are distributed among species. Species-abundance distributions, in contrast, use all available data to characterize [[monitoring-and-assessment-of-fungal-bioremediation]] community diversity.

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
- In mycology: typical of mature [[biodiversity-fungal-molecular-identification-dna-barcoding]] should be used when possible
- Sample size affects which distribution best fits the data

### Statistical Testing

Goodness-of-fit tests compare observed distributions to each model:
- Chi-square tests for categorical abundance classes
- Kolmogorov-Smirnov tests for continuous distributions
- Likelihood ratio tests compare model fits
- Expected values for each model can be compared using the G-test (Sokal and Rohlf 1995)

### Challenges Specific to Fungi

- [[biodiversity-of-fungi-pcr-molecular-methods-fungal-diversity]] detect unculturable species but may overrepresent certain taxa due to primer bias
- Combining methods provides the most complete picture but complicates distribution fitting

## Common Diversity Indices and Their Properties

## Practical Applications

The principles and techniques discussed here have wide-ranging applications
across multiple disciplines and contexts. Practitioners and researchers
continue to explore new ways to integrate these concepts into modern practice,
adapting traditional knowledge to contemporary challenges and opportunities.

## Key Considerations

Several important factors influence the effectiveness and outcomes described
in this topic. Understanding these considerations helps practitioners make
informed decisions and avoid common pitfalls. Environmental conditions,
timing, and material selection all play critical roles.

## Historical Context

The historical development of this subject reflects centuries of accumulated
knowledge and practical experience. From traditional methods passed down
through generations to modern scientific approaches, the evolution continues
to inform current best practices and research directions.

## Common Challenges

Practitioners frequently encounter several challenges when working with
these concepts. Climate variability, resource limitations, and knowledge
gaps can all affect outcomes. Addressing these challenges requires patience,
observation, and a willingness to adapt approaches based on results.

## See Also
- [[det]]
- [[biodiversity-fungal-species-abundance-diversity]]
- [[fungal-species-richness-and-diversity-indices]]
