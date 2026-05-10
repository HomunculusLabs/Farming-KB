---
title: [[arbuscular-mycorrhizal-fungal-diversity]] [[biodiversity-fungal-biodiversity-estimation-methods]]
created: 2026-04-16
updated: 2026-04-16
type: concept
tags: [mycology, fungi]
sources: []
---

# Fungal Diversity Estimation Methods
Estimating fungal species richness and diversity from field samples requires
specialized quantitative methods. Because most fungal species cannot be directly
counted and complete inventories are rarely achievable, researchers rely on
statistical approaches to estimate total diversity from partial sampling.

## The Challenge of Estimating Fungal Diversity

Fungal diversity estimation presents unique difficulties:
- Many fungi are known only from environmental DNA and cannot be cultured
- Sporocarp production is seasonal and ephemeral, causing underestimation
- Detectability varies enormously among species and habitats
- Sampling effort is limited by time, cost, and taxonomic expertise
- Species accumulation curves often fail to reach asymptotes, indicating
  incomplete sampling

## Species Richness Concepts

Three distinct concepts of species richness must be distinguished when
estimating fungal diversity:

- **Numerical species richness**: the number of species in a sample
  standardized by the number of individuals or isolates
- **Species density**: the number of species in a sample standardized by
  area, volume, or weight of the sampling unit
- **Total species richness**: the cumulative number of species in a series
  of samples from a habitat or substratum
The first two are measured without error (assuming complete enumeration of taxa
in the sample), whereas total species richness must be estimated from a series
of samples and is always an underestimate.

## Collector's Curves and Species-Effort Relationships

Collector's curves (also called species-accumulation curves) plot cumulative
species richness against sampling effort. Three mathematical models describe
how richness increases with effort:

- **Logistic model**: S reaches a plateau (asymptote), providing an accurate
  estimate of total richness for a bounded domain
- **Power model**: S increases monotonically without plateau (S = CA^z)
- **Exponential model**: S increases monotonically (S = C + z ln A)

The logistic model is most appropriate for geographically bounded areas with
random sampling, whereas power and exponential models better describe sampling
across heterogeneous landscapes.

## Rarefaction

Rarefaction is a quantitative method that facilitates comparison of species
richness among areas or habitats based on a standardized sample size. When
samples differ in the number of individuals or isolates, rarefaction calculates
the expected number of species for a standardized sample of n individuals:
E(S) = sum of [1 - (N-Ni choose n) / (N choose n)]
where E(S) is the expected species richness, n is the standardized sample size
(usually the smallest available), N is the total number of individuals, and Ni
is the number of individuals in species i.
Polishook and colleagues (1996) used rarefaction to determine the expected
number of fungal species from decaying leaves in a Puerto Rican rain forest.

## Diversity Indices

### Shannon Index (H')

The most widely used diversity index in community ecology. H' measures the
average uncertainty in predicting the identity of a randomly chosen individual.
Values typically range from 1.5 to 3.5 and rarely exceed 4.5. The Shannon
index exhibits a normal distribution across replicate samples, facilitating
parametric statistical comparisons. See [[fungal-species-richness-and-diversity-indices]]
for detailed methodology.

### Simpson's Index (D)

A dominance measure strongly influenced by the most common species. The
reciprocal form (1/D) is usually presented to ensure the index increases with
increasing diversity. Significant differences can be tested using parametric
or nonparametric analyses.

### Fisher's Log-Series Alpha

An index with good discriminant ability and low sensitivity to sample size.
However, it is unaffected by the actual distribution of individuals among
species (evenness), assuming a log-series distribution. Two communities with
the same N and S but different evenness will have the same alpha value.

### Hill's Numbers (N0, N1, N2)

Perhaps the easiest to interpret ecologically, with units of effective number
of species:
- N0 = total species count regardless of abundance
- N1 = e^H' (effective number of abundant species)
- N2 = 1/D (effective number of very abundant species)

## Jackknifing for Confidence Limits

The jackknife technique improves accuracy of [[fungal-diversity-estimates]] and provides
confidence limits. It involves recalculating overall diversity while
disregarding data from each of n constituent samples, creating jackknifed
pseudovalues. Confidence limits should not be calculated for datasets with
fewer than 15 samples.

## Species-Area Relationships

The relationship between species number and area sampled is fundamental to
[[fungal-biogeography]]. The Arrhenius power law (S = CA^z) and Gleason
exponential model (S = C + z ln A) are widely used. The slope parameter z
typically ranges from 0.2 to 0.35 for fungi, and is influenced by habitat
heterogeneity, dispersal ability, and spatial aggregation of species.

## Emerging Technologies

### Metabarcoding and High-Throughput Sequencing

The application of high-throughput sequencing to fungal diversity estimation
has fundamentally changed the field. [[environmental-dna-metabarcoding-fungi]]
using the ITS (Internal Transcribed Spacer) region as a barcode allows
detection of thousands of fungal taxa from a single soil sample. This
technology has revealed that traditional fruiting body surveys capture only
a small fraction of the total [[air-pollution-fungal-community-responses]] present in any given habitat.

### Bioinformatics Pipelines

Modern fungal diversity studies rely on sophisticated bioinformatics
pipelines to process raw sequencing data into actionable diversity estimates.
Common workflows include DADA2 or UNOISE for denoising sequences into exact
amplicon sequence variants (ASVs), followed by taxonomic assignment using
reference databases such as UNITE or SILVA. These pipelines have largely
replaced earlier OTU clustering approaches, offering higher resolution and
reproducibility.

### Machine Learning Approaches

Machine learning algorithms are increasingly applied to fungal diversity data
for species distribution modeling, habitat suitability prediction, and
automated classification of environmental sequences. Random forests, gradient
boosted trees, and neural networks can integrate environmental variables with
fungal occurrence data to predict [[arbuscular-mycorrhizal-fungal-diversity-patterns-distribution]] across unsampled
landscapes.
## See Also

- [[fungal-species-estimation-methods-total-diversity]]
