---
title: Species-Abundance Distribution
source: unknown-biodiversity-of-fungi.md
type: entity
---

## Description

A species-abundance distribution (SAD) is a mathematical and graphical representation of how individuals are distributed among species within an ecological community. When the number of species and their relative abundances are plotted, characteristic patterns emerge that provide insights into ecological processes. Four main models describe these distributions: geometric series, logarithmic series, lognormal distribution, and broken-stick model.

## Classification

- **Category**: Ecological concept / analytical framework
- **Subtypes**: Geometric series, log-series, lognormal distribution, broken-stick model
- **Data requirement**: Species abundance counts within a defined ecological unit
- **Historical origin**: Fisher et al. (1943), Preston (1948)

## Historical Development

The study of species-abundance distributions began with R.A. Fisher"s seminal 1943 paper introducing the logarithmic series model to describe moth trap data. Fisher, Corbet, and Williams observed that most species in a sample were represented by few individuals while a small number of species were very abundant, and they formalized this pattern mathematically using the parameter α (alpha), now known as [[fishers-log-series-alpha]].

In 1948, Frank Preston proposed the lognormal distribution as an alternative, arguing that species abundances in large, diverse communities tend to follow a bell-shaped curve when plotted on a logarithmic scale. Preston introduced the concept of "octaves" — doubling abundance classes — and noted the "veil line" effect where sampling incompleteness truncates the full distribution.

Motomura (1932) had earlier described the geometric series (also called the niche preemption model) in lake communities, though this work gained broader recognition through Whittaker"s studies of plant communities in the 1960s and 1970s. Whittaker also popularized rank-abundance (Whittaker) plots as a standard graphical tool, and his framework of [[whittaker-beta-diversity]] is conceptually linked to SAD analysis.

The broken-stick model was formalized by MacArthur (1957) as a null model assuming random niche division. May (1975, 1981) and Southwood (1978) later advocated SADs as the most rigorous foundation for examining species diversity, arguing that single-number indices inevitably lose important information about community structure.

## Theoretical Models

### Geometric Series (Niche Preemption Model)

The geometric series model, also called Motomura's model, assumes that the dominant species preempts a proportion *k* of the total resources, the second-most dominant species preempts the same proportion *k* of the remaining resources, and so on. This produces a rank-abundance curve that is steep and linear on a log scale.

- **Ecological interpretation**: Strong niche preemption by competitively dominant species
- **Typical habitats**: Species-poor, harsh, or frequently disturbed environments
- **Key parameter**: *k* (niche preemption coefficient, typically 0.3–0.7)
- **Characteristics**: Few common species, many rare species, steep dominance hierarchy

### Logarithmic Series (Log-Series)

Fisher's log-series model describes communities where a few factors control species dominance and propagules arrive at random. The distribution predicts that the number of species with *n* individuals follows a declining series.

- **Ecological interpretation**: Nonequilibrial communities with random colonization
- **Typical habitats**: Early successional stages, recently disturbed sites, island communities
- **Key parameter**: α (Fisher's alpha) — a diversity index relatively insensitive to sample size
- **Characteristics**: Large number of rare species, predictable species-total relationship
- **See also**: [[fishers-log-series-alpha]]

### Lognormal Distribution

Preston's lognormal model emerges when many independent factors influence species abundances. When species are tallied into octave classes (doubling abundance intervals), the distribution approximates a bell curve. It is considered the most common SAD in nature for large, diverse communities.

- **Ecological interpretation**: Many interacting niche factors in equilibrial communities
- **Typical habitats**: Mature forests, species-rich tropical communities, well-established soil ecosystems
- **Key parameters**: Mean and standard deviation of log abundances; the "canonical" form predicts a fixed relationship between these
- **Characteristics**: Symmetric distribution on log scale; Preston"s "canonical lognormal" predicts S/A ratio patterns
- **Truncation effect**: The "veil line" — undersampled rare species are hidden behind a sampling veil

### Broken-Stick Model

MacArthur's broken-stick model treats niche space as a stick broken randomly into *S* pieces, where *S* is the number of species. Each segment represents a species' share of total resources.

- **Ecological interpretation**: Random, simultaneous niche division with no competitive hierarchy
- **Typical habitats**: Stable environments with long-lived organisms and saturated communities
- **Key assumption**: All species are ecologically equivalent
- **Characteristics**: Most equitable distribution of all four models; serves as a null hypothesis
- **Limitation**: Rarely fits empirical data well, making it useful primarily as a theoretical benchmark

## Mathematical Framework

### Geometric Series

$$n_i = N C_k k (1 - k)^{i-1}$$

where *n_i* is the abundance of the *i*-th most abundant species, *N* is total individuals, *k* is the niche preemption fraction, and *C_k* is a normalization constant.

### Log-Series

The number of species with *n* individuals:

$$S_n = \frac{\alpha x^n}{n}$$

where α is Fisher's alpha and *x* is a parameter (0 < *x* < 1) related to total abundance by *N = αx/(1 - x)*. The total number of species is:

$$S = -\alpha \ln(1 - x)$$

### Lognormal Distribution

$$S(R) = S_0 \exp\left(-\frac{(R - R_0)^2}{2\sigma^2}\right)$$

where *S(R)* is the number of species in the *R*-th octave, *S_0* is the number of species in the modal octave, *R_0* is the modal octave, and σ is the standard deviation of the lognormal curve.

### Broken-Stick

The expected abundance of the *i*-th most abundant species:

$$n_i = \frac{N}{S} \sum_{j=i}^{S} \frac{1}{j}$$

where *N* is total individuals and *S* is total species.

### Goodness-of-Fit Testing

Model fit is typically assessed using Chi-square tests or G-tests (log-likelihood ratio tests) following Sokal and Rohlf (1995). Rank-abundance (Whittaker) plots provide visual comparison — plotting log abundance against species rank.

## Applications in Mycology

Species-abundance distributions have been extensively applied to fungal community ecology, where they provide insights that single-number diversity indices cannot:

- **Soil fungal communities**: Lussenhop (1981) demonstrated that lognormal distributions characterize mature forest soil fungal communities, reflecting the many interacting niche dimensions in complex soil environments. This contrasts with stressed or disturbed soils where distributions shift toward geometric or log-series patterns.

- **Rhizoplane fungal assemblages**: Zak (1988, 1992) found that geometric and log-series models best described rhizoplane fungal communities on root surfaces, consistent with strong niche preemption by competitive colonizers and nonequilibrial conditions.

- **Substrate ecology in cultivation**: In mushroom cultivation, SADs can reveal whether substrate microbial communities are dominated by few species (suggesting contamination risk or ecological instability) or are diverse and balanced (suggesting mature, stable communities resistant to weed molds and competitors).

- **Mycorrhizal communities**: SAD analysis helps assess mycorrhizal diversity and colonization patterns, distinguishing between heavily dominated communities (geometric) and more equitable partnerships (approaching broken-stick).

- **Airborne spore communities**: Fungal spore trapping data often fit log-series distributions, reflecting the stochastic arrival of propagules from diverse sources.

- **Wood decay succession**: The progression from geometric → log-series → lognormal models can track successional stages in decomposing wood, as pioneer decomposers give way to more diverse, equilibrial communities.

## Relationship to Other Diversity Metrics

Species-abundance distributions are considered the most information-rich approach to characterizing community diversity. Their relationship to other metrics includes:

- **[[fishers-log-series-alpha]]**: The α parameter from the log-series is itself a widely used diversity index. It is relatively insensitive to sample size, making it robust for comparing communities sampled with different intensities.

- **[[species-richness-diversity-indices-fungi]]**: SADs contain richness information (total species count) as one component but add critical information about how individuals are distributed among those species. Richness alone cannot distinguish between a community dominated by one species and one where all species are equally abundant.

- **[[whittaker-beta-diversity]]**: While SADs characterize within-community (alpha) diversity, beta diversity measures turnover between communities. Whittaker himself connected these concepts by noting that SAD shape influences beta diversity calculations.

- **[[bray-curtis-dissimilarity]]**: Bray-Curtis dissimilarity uses species abundance data to compare communities. The shape of SADs in each community directly influences Bray-Curtis values — communities with similar SAD shapes will have lower dissimilarity.

- **[[alpha-beta-gamma-diversity-fungi]]**: SADs operate at the alpha (within-community) level. The aggregation of multiple SADs across habitats connects to gamma diversity, while differences between them relate to beta diversity.

- **[[fungal-diversity-indices-community-analysis]]**: Common indices like Shannon-Wiener (H') and Simpson's (D) are essentially summaries of the SAD. Shannon's index is maximized when the SAD is perfectly even (broken-stick), while Simpson's index is more sensitive to dominant species (the left tail of the SAD).

- **Evenness indices**: Pielou's J and other evenness measures quantify the shape of the SAD relative to a perfectly even distribution.

- **Rarefaction**: SADs provide the underlying distribution from which rarefaction curves are derived. A community with a lognormal SAD will produce a different rarefaction curve than one with a geometric SAD, even at identical richness.

## Key Facts

- First recognized by Fisher and colleagues (1943) who observed characteristic abundance patterns
- Four main models form a progression from few dominant species (geometric) to equitable distribution (broken-stick)
- Geometric series: dominant species preempts resources; typical of species-poor or stressed habitats
- Log-series: few factors control dominance; propagules arrive randomly; nonequilibrial communities
- Lognormal: many interacting factors; characteristic of large, diverse, equilibrial communities
- Broken-stick: random division of resources; associated with stable populations and long life cycles
- May (1975, 1981) and Southwood (1978) advocated these as the only sound basis for examining species diversity
- Goodness-of-fit tested using Chi-square or G-test (Sokal and Rohlf 1995)
