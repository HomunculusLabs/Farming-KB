---
title: Mycelial Growth Modeling in Heterogeneous Environments
aliases: [fungal growth modeling, mycelial continuum model, discrete hyphal network model, fungal [[gadd-mathematical-modelling-fungal-mycelia]]
tags: [mycology, mathematical-modeling, mycelium, fungal-ecology, simulation]
sources:
  - geoffrey-gadd-sarah-c-watkinson-paul-s-dyer-fungi-in-the-environment.md
---

# Mycelial Growth Modeling in Heterogeneous Environments

## Overview

Mathematical modeling of fungal mycelial growth provides powerful tools for understanding how filamentous fungi explore, colonize, and exploit heterogeneous environments such as soil. Fungi in nature rarely encounter uniform conditions; instead, they navigate complex spatial mosaics of nutrients, moisture, pH, and physical structure. Modeling approaches developed by researchers including Davidson, Boswell, Gadd, and Ritz combine continuum and discrete frameworks to simulate mycelial form and function, yielding insights into colony expansion, nutrient translocation, network resilience, and environmental acidification that complement and extend experimental observations.

## Why Model Fungal Growth?

Mathematical models of fungal growth serve several important purposes:

1. **Testing hypotheses** about the functional significance of mycelial traits (e.g., translocation, anastomosis, branching patterns)
2. **Predicting behavior** in conditions difficult or expensive to replicate experimentally
3. **Quantifying** relationships between environmental variables and growth parameters (e.g., fractal dimension as a function of substrate concentration)
4. **Integrating** multiple processes (growth, nutrient uptake, translocation, acidification) into a unified framework
5. **Guiding applications** in biocontrol, bioremediation, and environmental biogeochemistry

## The Continuum Model

### Foundation

The continuum approach treats the mycelium as a density field rather than tracking individual hyphae. It is most appropriate when growth is dense and the network can be approximated as a continuous medium. The model is built on partial differential equations describing:

- **Tip extension**: New biomass is produced at hyphal tips as they extend into uncolonized space
- **Substrate uptake**: External nutrients are absorbed by the fungal biomass
- **Internal translocation**: Substrate is moved within the mycelium from regions of surplus to regions of demand, through both active transport and passive diffusion
- **Acidification**: [[arbuscule-isolation-metabolic-activity-assays]] releases acids that lower the pH of the surrounding environment

### Active vs. Passive Translocation

A key finding from the modeling work concerns the roles of active and passive (diffusive) translocation. Conventionally:

- **Active translocation** was thought to be associated primarily with exploration (outgrowth into new territory)
- **Passive translocation** (diffusion) was associated with exploitation (substrate utilization at established locations)

The modeling results suggest the reverse: active translocation is crucially involved in the initial exploitative phase when a hypha first contacts a new resource, carrying internal substrate to hyphal tips to provide the "energy" needed to drive active uptake. Diffusive translocation, by contrast, serves primarily as a short-range exploratory mechanism, distributing signals and metabolites locally to coordinate nearby growth.

### Parameterization

The continuum model is calibrated and tested against experimental data from systems including:

- *Rhizoctonia solani* growing on agar
- Tessellated agar droplet arrays (hexagonal arrays of nutrient-amended and unamended droplets)
- Soil microcosms with defined pore structures

Quantitative features such as colony radial expansion rate, biomass distribution, and environmental acidification are used to validate model predictions.

## The Discrete (Hybrid) Model

### Motivation

When growth is sparse — when individual hyphae can be resolved and the network has not yet filled space — a continuum approach is less relevant. In these conditions, a discrete model that tracks individual hyphae is more appropriate. The challenge lies in deriving meaningful growth rules and parameterizing them.

### The Hybrid Approach

The hybrid model developed by Davidson and colleagues is derived directly from the continuum model, providing a principled link between the two frameworks:

- **Space** is modeled as an array of hexagonal cells, with the mycelium defined on the embedded triangular lattice
- **Time** advances in discrete steps, with movement probabilities derived from the finite-difference discretization of the continuum equations
- **Dual representation**: "Cell" models track individual particles (hyphal tips, substrate), while "bond" models track connections between cells (active/inactive hyphae, anastomosis points)

### Why Both Cell and Bond Models?

The dual representation solves a critical problem. In a pure cell-based model, two adjacent but parallel hyphae would automatically be treated as connected, allowing transfer of materials between them. In reality, parallel hyphae are NOT connected unless an anastomosis (fusion) point forms between them. The bond-based approach explicitly models connections, accurately representing the network topology and internal substrate redistribution.

### Key Processes Modeled

The discrete model captures several important biological processes:

- **Hyphal tip extension and branching**: Tips advance into uncolonized space and branch probabilistically
- **Anastomosis**: When two hyphae meet, they can fuse, creating a connected network that allows translocation
- **Hyphal inactivation and reactivation**: Old hyphae can become inactive (cease growth) and potentially reactivate if conditions improve
- **Substrate uptake and translocation**: External substrate is absorbed and moved through the network
- **Network resilience**: The model can simulate damage (removal of nodes or edges) to study network robustness

## Modeling Growth in Soil

### Soil as a Heterogeneous Environment

Soils exhibit multiple types of heterogeneity that affect fungal growth:

- **Structural**: Soil particles create a complex pore space; water films coat particle surfaces while larger pores are air-filled
- **Nutritional**: Nutrients are concentrated in water films and associated with organic matter, creating patchy distributions
- **Temporal**: Moisture content, temperature, [[ph-and-nutrient-availability-garden-soils]] change over time

### The Water Film Model

In non-saturated soils, water films of varying thickness coat soil particle surfaces. These films are the primary habitat for fungal hyphae because they provide both moisture and dissolved nutrients. Key features:

- Nutrients diffuse within the water film but do not cross the air-water interface (surface tension prevents it)
- Hyphae grow primarily within and along these films
- The thickness and connectivity of water films determine the effective growth habitat

### Model Predictions for Soil Growth

The hybrid model, adapted for soil-like pore structures, predicts:

1. **Early growth** is confined to the water film region, where nutrients are accessible
2. **Explorer tips** emerge from the water film and extend across air-filled pore spaces, locating new substrate resources
3. **Surface tension** of the water film plays a significant role: reducing surface tension in the model results in greater biomass distribution in pore space and faster overall expansion
4. **Fractal dimension** of the growth habitat correlates with biomass distribution — more connected pore spaces support more extensive colonization

### Validation

The model soil is constructed by randomly removing hexagonal blocks from the growth domain, creating connected or fragmented pore spaces with defined fractal dimensions. These artificial structures can be compared with real soil thin sections, enabling quantitative validation of model predictions against experimental observations of fungal growth in soils.

## Biological Control and Bioremediation Applications

The modeling framework has direct relevance to applied mycology:

- **Biocontrol agents**: Certain fungi suppress plant pathogens through competition, antibiosis, or parasitism. Models can predict how these agents colonize root systems and soil, optimizing application strategies
- **Bioremediation**: Fungi that transform toxic metals or degrade pollutants operate in heterogeneous contaminated environments. Models can predict colonization patterns, remediation rates, and the effects of environmental variables on process efficiency
- **Nutrient cycling**: As key decomposers and nutrient recyclers in soil food webs, fungal activity patterns influence carbon and nitrogen dynamics at the ecosystem scale

## Network Resilience

The discrete model enables study of [[gadd-mycelial-network-resilience-graph-theory]] by simulating the removal of individual nodes or links:

- **Random damage** (e.g., random physical disruption) versus **targeted damage** (e.g., grazing by soil invertebrates that preferentially consume certain regions)
- Self-organizing spatial networks may have advantages over random networks in the cost, consistency, and efficacy of reconnection after damage
- The average degree of connectivity (number of connections per node) stabilizes around 3.5 in mature *[[phanerochaete-velutina]]* networks after initial exploratory growth

## Limitations and Future Directions

Current limitations of mycelial growth modeling include:

- Lack of clear anatomical description of how transport pathways map onto individual hyphae in corded systems
- Difficulty quantitatively comparing results from notionally replicate experiments due to the immense plasticity of mycelial networks
- The challenge of spanning all relevant length scales — from sub-cellular nutrient transport to colony-level resource distribution
- Limited incorporation of biotic interactions (competition, predation, symbiosis) into growth models

Despite these challenges, the combination of continuum and discrete modeling approaches provides a powerful framework for understanding fungal ecology and for applying fungi to solve environmental problems.

## See Also

- [[fungal-mycelial-networks-nutrient-translocation]] — experimental observations of nutrient movement
- [[fungal-vacuolar-system-nutrient-translocation]] — intracellular transport mechanisms
- [[fungal-mycelial-foraging-heterogeneous-environments]] — [[root-foraging-behavior]] in patchy resources
- [[fungal-contributions-soil-structure]] — how fungi physically modify soil structure
