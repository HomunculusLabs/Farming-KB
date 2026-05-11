---
title: Mycelial Growth Modeling Heterogeneous Environments
aliases: [fungal growth modeling, mycelial continuum model, discrete hyphal network model, fungal [[gadd-mathematical-modelling-fungal-mycelia]]
tags: [mycology, mathematical-modeling, mycelium, fungal-ecology, simulation]
sources:
  - geoffrey-gadd-sarah-c-watkinson-paul-s-dyer-fungi-in-the-environment.md
---

# Mycelial Growth Modeling in Heterogeneous Environments

## Overview

[[davidson-mathematical-modeling-fungal-mycelia]] of fungal mycelial growth provides powerful tools for understanding how filamentous fungi explore, colonize, and exploit heterogeneous environments such as soil. Fungi in nature rarely encounter uniform conditions; instead, they navigate complex spatial mosaics of nutrients, moisture, pH, and physical structure. Modeling approaches developed by researchers including Davidson, Boswell, Gadd, and Ritz combine continuum and discrete frameworks to simulate mycelial form and function, yielding insights into colony expansion, [[dighton-fungal-nutrient-translocation-element-redistribution]], [[gadd-mycelial-network-resilience-graph-theory]], and environmental acidification that complement and extend experimental observations.

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
- **Passive translocation** (diffusion) was associated with exploitation ([[growing-gourmet-mushrooms-species-sequencing-substrate-utilization]] at established locations)

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

The dual representation solves a critical problem. In a pure cell-based model, two adjacent but parallel hyphae would automatically be treated as connected, allowing transfer of materials between them. In reality, parallel hyphae are NOT connected unless an anastomosis (fusion) point forms between them. The bond-based approach explicitly models connections, accurately representing the [[mycelial-cord-network-topology-graph-theory-bebber]] and internal substrate redistribution.

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
