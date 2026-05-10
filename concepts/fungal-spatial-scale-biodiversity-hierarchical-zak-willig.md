# Spatial Scale of Fungal Biodiversity

## Overview

Whittaker (1977) first recognized that ecological diversity is scale-dependent and hierarchical in nature. For mycologists, this creates unique challenges because fungi operate across spatial scales ranging from micrometers (individual hyphal tips) to entire landscapes (mycelial networks spanning hectares). Understanding spatial scale is essential for designing sampling protocols, interpreting biodiversity data, and comparing results across studies.

## The Hierarchical Nature of Diversity

### Point Diversity

The most fundamental level: the diversity at a single, precisely defined location at a single point in time. For fungi, this could be a single soil core, a leaf litter sample, or a piece of wood. Point diversity captures only the microhabitat conditions at that specific location.

### Alpha Diversity

Also called within-habitat diversity. Alpha diversity is the diversity within a single, relatively homogeneous habitat type. It is influenced by local environmental conditions, resource availability, and competitive interactions. Alpha diversity forms the baseline against which larger-scale patterns are measured.

### Beta Diversity

The change in species composition between habitats or along environmental gradients. Beta diversity quantifies how much species turnover occurs as one moves across space. It is by far the most commonly used metric of differentiation diversity for examining compositional changes along gradients.

### Gamma Diversity

The total diversity across an entire landscape or region, encompassing all habitat types within it. Gamma diversity is conceptually related to alpha and beta diversity through the relationship:
```
Gamma = Alpha × Beta (approximately)
```
More precisely, gamma diversity reflects the cumulative species pool across all habitats in a region.

### Delta and Epsilon Diversity

Delta diversity describes the change in species composition between geographic regions (biogeographic scale), while epsilon diversity addresses broad biogeographic patterns across continents or major climatic zones. These scales are rarely addressed in individual mycological studies due to the logistical demands of multi-regional sampling.

## Scale-Dependent Challenges for Mycologists

### The Fungal Unit Problem

Fungi present a fundamental challenge to biodiversity measurement because their body plan differs from most organisms:
- Most fungi consist of indeterminate mycelial networks rather than discrete individuals
- A single mycelium can occupy microenvironments to macroenvironments simultaneously
- Distant segments remain interconnected, facilitating intercellular communication
- Sporocarps on a forest floor may represent multiple ramets of a single genet or ramets from multiple genets
- Only molecular or isozymic analyses can untangle genetic structure of fungal populations

### Genet vs. Ramet

For clonal organisms like fungi:
- A **genet** is a unique genetic individual
- A **ramet** is a physiologically independent module belonging to a genet
- The number of countable units (ramets) is not the same as the number of genets
- Without genetic analysis, diversity estimates based on sporocarp counts may dramatically over- or underestimate true genetic diversity

### Operational Definitions

Because the concept of "individual" is ambiguous for fungi, each investigator must establish a clearly stated operational definition of the unit to be counted. This definition will differ depending on the taxonomic or ecological group:
- For macrofungi: one sporocarp = one operational unit (common but problematic)
- For microfungi from soil plates: one colony = one operational unit
- For molecular surveys: one OTU or ASV = one operational unit

## Sampling Design and Spatial Scale

### Plot Size and Shape

The choice of sampling plot dimensions directly affects measured diversity:
- Too small: rare species are missed, underestimating true diversity
- Too large: habitat heterogeneity within the plot confounds measurements
- The investigator should have a priori knowledge of appropriate plot dimensions
- Plot shape matters: elongated plots may cross habitat boundaries, increasing apparent beta diversity

### Scale Dependence of Patterns

Evidence from Kolasa and Pickett (1991), Waide et al. (1999), and Gross et al. (2000) demonstrates that ecological patterns and processes are scale-dependent. This means:
- Patterns observed at one spatial scale may not exist at another
- Mechanisms driving diversity may differ across scales
- Caution is required when comparing studies using different plot sizes
- The spatial scale of data collection should relate to the spatial scales of causative mechanisms

### Inference Space

Every study has defined spatial and temporal limits within which inferences are valid:
- Phenology of focal species constrains when sampling can occur
- Results from a tropical forest may not transfer to temperate systems
- The inference space should be explicitly stated and respected when drawing conclusions

## Nested Sampling Designs

A powerful approach to addressing scale-dependency is nested or hierarchical sampling, where multiple spatial scales are captured within a single study design:
- **Level 1 (finest)**: Individual substrate samples (e.g., single leaves, soil cores)
- **Level 2**: Plots containing multiple samples from the same microhabitat
- **Level 3**: Sites containing multiple plots across a habitat gradient
- **Level 4 (coarsest)**: Regions containing multiple sites across a landscape

This hierarchical structure allows researchers to partition diversity into components attributable to different spatial scales using methods such as additive partitioning of diversity (Lande 1996). The approach reveals whether most variation in fungal community composition occurs within microhabitats, among habitats within sites, or among sites across the landscape.

### Additive Partitioning

Additive diversity partitioning decomposes total gamma diversity into additive alpha and beta components at each spatial scale:
```
γ = α1 + β1 + β2 + β3 + ...
```
Where α1 is average within-sample diversity and each β component represents the diversity added by moving to the next broader spatial scale. This approach, recommended by Crist et al. (2003) and Veech et al. (2002), allows direct comparison of the relative contributions of different spatial scales to overall diversity.

## Practical Guidelines for Mycologists

1. **Define the spatial scale explicitly**: State plot size, shape, number, and arrangement before sampling begins
2. **Match scale to question**: Large-scale questions require large-scale sampling; fine-scale mechanisms require fine-scale plots
3. **Standardize across sites**: When comparing sites, use identical plot dimensions and sampling intensity
4. **Consider the fungal unit**: Acknowledge whether operational units represent genets, ramets, or something else
5. **Use molecular verification when possible**: Genetic data resolves ambiguities that morphology cannot
6. **Report all spatial metadata**: GPS coordinates, elevation, habitat type, substrate, and microhabitat conditions
7. **Address multiple scales**: Where feasible, include nested sampling designs that capture diversity across multiple spatial scales simultaneously
8. **Beware of pseudoreplication**: Samples from the same mycelial individual are not independent replicates
9. **Account for temporal variation**: Seasonal fruiting patterns mean that single-timepoint surveys capture only a fraction of true diversity

## See Also

- [[fungal-biodiversity-power-analysis-statistical-design-zak-willig]]

- [[fungal-beta-diversity-similarity-indices-zak-willig]]
- [[fungal-species-abundance-distributions-diversity-indices]]
- [[biodiversity-fungi-soil-fungal-communities]]
- [[fungal-biodiversity-data-analysis]]
- [[fungal-biodiversity-species-estimation]]
