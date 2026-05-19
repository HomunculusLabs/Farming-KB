---
title: Fungal Biodiversity Assessment Methods
source: unknown-biodiversity-of-fungi.md
type: concept
---

# Fungal Biodiversity Assessment Methods

Assessing [[fungal-biodiversity]] presents unique challenges that distinguish mycology from plant and animal ecology. Fungi exhibit growth forms and body plans that resist straightforward enumeration. This page covers core conceptual and methodological issues in fungal biodiversity assessment.

## The Fungal Unit Problem

The most fundamental challenge in fungal biodiversity is defining **what constitutes an individual**. Unlike animals and plants, fungi do not have a determinate body plan. Their [[fungal-mycelial-networks-nutrient-translocation]] can grow indefinitely, fragment, and fuse in complex ways.

This ambiguity creates the **fungal unit problem**: researchers must decide what counts as one organism before they can count organisms at all.

### Numerical, Genetic, and Ecological Individuals

Three primary definitions are used:

- **Numerical individual**: Each physically separated structure counts as one. Each fruiting body is one individual. Intuitive but ecologically misleading, since many fruiting bodies may arise from the same mycelium.
- **Genetic individual (genet)**: Defined by shared genotype — all mycelium and fruiting bodies with identical DNA. Biologically meaningful but requires molecular tools.
- **Ecological individual**: Defined by functional role and resource use. Context-dependent and harder to standardize.

## Ramets vs Genets

- **Genet**: The entire genetically uniform mycelium, regardless of how many physically separated structures it produces.
- **Ramet**: A physically discrete module (e.g., a single fruiting body) produced by a genet.

A single genet may produce hundreds of ramets across a forest floor. Counting ramets inflates apparent abundance, while counting genets may underrepresent ecological presence.

## Indeterminate vs Determinate Body Plans

Animals and plants have **determinate body plans** — they grow to a characteristic size and form. Fungi have **indeterminate body plans**. Their mycelium can expand, contract, fragment, and re-fuse without clear boundaries.

This indeterminacy makes it difficult to:

- Define where one fungus ends and another begins
- Determine the age or size of an individual
- Apply standard census methods from plant or animal ecology

## Frequency of Occurrence

**Frequency of occurrence** measures how commonly a species is found across sampling units. The formula is:

> F = (n / N) × 100

Where **F** = frequency (%), **n** = number of sampling units where the species is present, and **N** = total number of sampling units examined.

**Relative frequency** expresses a species' occurrence relative to all species combined:

> RF = (F_i / ΣF) × 100

This is useful for comparing dominance structure across different sites or habitats.

## Sampling Design

### Plot Size

Choosing an appropriate **plot size** is critical. Plots that are too small miss rare species; plots that are too large increase effort without proportional gains.

- **Small plots** (1–4 m²): targeted studies of specific substrates
- **Medium plots** (10–100 m²): common in community-level surveys
- **Large plots** (100–1000 m²): landscape-scale assessments

### Plot Shape: Circular vs Rectangular

- **Circular plots** minimize edge effects for a given area. Preferred when distance-based measurements from a center point are convenient.
- **Rectangular plots** (quadrats) are easier to establish in the field and align with transect-based sampling. May introduce directional bias along edges.

### Scale Dependence

Fungal diversity measures are strongly **scale-dependent**. Species richness typically increases with sampled area.

- Alpha diversity (local) may differ dramatically from gamma diversity (regional)
- Rare species are more likely detected at larger spatial scales
- [[core-endorhiza-bacterial-community-composition-cannabis]] shifts with scale due to habitat heterogeneity

## Collection Effort Curves

**Collection effort curves** (species accumulation curves) plot cumulative species richness against sampling effort. They are fundamental tools for evaluating whether a survey has adequately sampled the fungal community.

### Common Models

1. **Power model**: S = a · E^b
   - Simple and flexible, but lacks a true asymptote
   - Often fits empirical data well at low-to-moderate effort

2. **Exponential model**: S = S_max · (1 − e^(−kE))
   - Approaches an asymptote smoothly
   - Assumes constant rate of new species discovery per unit effort

3. **Logistic model**: S = S_max / (1 + e^(−k(E−E₀)))
   - Sigmoidal shape with an inflection point
   - Useful when initial discovery is slow, accelerates, then decelerates

Where **S** = cumulative species count, **E** = sampling effort, **S_max** = asymptotic richness, and **a, b, k, E₀** = fitted parameters.

### Asymptote and Sample Size Determination

The **asymptote** estimates total species richness. Reaching it indicates additional sampling yields diminishing returns. Determining adequate **sample size** involves:

1. Plotting the observed accumulation curve
2. Fitting an appropriate model (power, exponential, or logistic)
3. Estimating the proportion of total richness captured
4. Identifying the effort level at which the curve flattens

A common rule of thumb: sampling is sufficient when **90–95% of estimated total richness** has been observed.

## Community-Level Parameters

### Species Composition

**Species composition** describes the identity and relative abundance of all species. Two communities may have identical richness but completely different composition. **Jaccard** and **Sørensen** indices quantify compositional similarity.

### Functional Correlates

Fungi play diverse **[[hemenway-mulch-makers-and-plant-functional-roles]]**: decomposers, mycorrhizal partners, pathogens, and endophytes. Key parameters include guild structure, enzyme repertoire, and [[functional-redundancy]].

### Genetic Correlates

**[[biodiversity-fungal-genetic-diversity]]** provides insight into evolutionary potential and population history. High diversity suggests stable populations; low diversity may indicate bottlenecks or clonal reproduction.

### Interspecific Interactions

Fungi interact through **competition**, **antagonism**, and **facilitation**. Commonly assessed interactions include competitive exclusion among wood-decay fungi, antibiotic production, and [[arbuscular-mycorrhizal-network-visualization-anastomosis]] sharing.

### Dynamics

Fungal communities are **temporally dynamic**. [[macrofungal-fruiting-phenology-climate-variability]] varies widely, weather events trigger mass fruiting, and long-term monitoring is needed to capture temporal turnover.

## Operational Definitions and Their Importance

Researchers must adopt explicit **operational definitions** of what constitutes an individual. An operational definition should specify:

1. Whether individuals are defined by fruiting bodies, genets, or another criterion
2. How genetic individuals are identified (if applicable)
3. How partially connected mycelia are treated
4. How sterile morphotypes are handled

Without clear operational definitions, biodiversity estimates are **not comparable** across studies.

## Standard Error and Variability Among Species

[[fungal-biodiversity-estimates]] carry substantial **uncertainty**. Key sources of variability include temporal (seasonal fruiting), spatial (patchy distribution), observer differences, and methodological choices (plot size, shape, number).

The **standard error** decreases with increasing sample size and replication. It can be estimated via analytical approaches, resampling methods (bootstrap/jackknife), or parametric confidence intervals from fitted models. Reporting standard errors is **essential best practice**.

Different species exhibit vastly different **detectability**. Common, conspicuous species are reliably recorded; rare or microscopic species are under-sampled. This **heterogeneous detectability** biases raw species counts. **Rarefaction** and estimators like **Chao1** and **ACE** attempt to correct for this, but rely on assumptions that may not hold for all fungal communities.
