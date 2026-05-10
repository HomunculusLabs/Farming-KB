---
title: [[gadd-mathematical-modelling-fungal-mycelia]] of Fungal Mycelia Form and Function
source: geoffrey-gadd-sarah-c-watkinson-paul-s-dyer-fungi-in-the-environment.md
author: Fordyce A. Davidson
topics:
  - mycology
  - mathematical-modelling
  - mycelial-networks
  - fungal-morphology
  - computational-biology
---

# Mathematical Modelling of Fungal Mycelia

## Overview

In Chapter 4 of *Fungi in the Environment*, Fordyce A. Davidson presents mathematical modelling approaches to understanding the form and function of fungal mycelia. The chapter explores how computational models can capture the complex growth patterns, nutrient transport, and adaptive responses of mycelial networks that are difficult or impossible to study through observation alone.

## Why Model Fungal Mycelia?

### The Complexity Problem

Fungal mycelia present extraordinary modelling challenges:

- **Non-linear growth**: Hyphal extension rates vary with local nutrient conditions, not as simple linear functions
- **Network topology**: Mycelia form complex branching networks that continuously reconfigure
- **Multi-scale processes**: Relevant phenomena span from sub-cellular (vacuolar transport) to colony-level (meter-scale foraging) scales
- **Emergent behavior**: Colony-level patterns arise from local interactions between individual hyphae, not from central coordination
- **Environmental coupling**: Growth, branching, and regression respond to heterogeneous and changing environments

### What Models Can Reveal

Mathematical models allow researchers to:

1. Test hypotheses about mechanisms underlying observed mycelial patterns
2. Predict mycelial behavior under conditions not yet observed experimentally
3. Identify which parameters most strongly influence network architecture
4. Explore the relationship between local growth rules and global network function
5. Understand how nutrient translocation constrains or enables [[mycelial-foraging-strategies-nutrient-translocation]]

## Fractal Geometry in Mycelial Description

### Mass Fractal vs. Surface Fractal Systems

Davidson builds on the fractal analysis framework described by Boddy and colleagues. Mycelia can be classified by their fractal dimension (D), which describes space-filling characteristics:

- **Mass fractal mycelia** (D_M): Have gaps in their interiors. Characterized by well-defined, rapidly extending cords forming open, long-range foraging networks. Species include *[[phanerochaete-velutina]]*, *[[bloomfield-stinkhorns-phallus-impudicus-osmotic-fruiting]]*, and *Resinicium bicolor*. These are long-range foragers suited to discovering large, sparsely distributed resources.

- **Surface fractal mycelia** (D_S < D_M): Completely plane-filled except at boundaries. Characterized by diffuse, slowly extending search fronts. Species include *[[hypholoma-fasciculare]]* and *[[stropharia-caerulea]]*. These short-range foragers search areas intensively and succeed with abundant, homogeneous resources.

### Box-Counting Method

The standard method for determining fractal dimensions of mycelia:

- Overlay grids of decreasing box sizes on mycelial images
- Count boxes containing mycelial material at each scale
- Plot log(box count) vs. log(box size)
- The slope of the linear region gives the fractal dimension

This method allows quantitative comparison between species, developmental stages, and environmental conditions.

### Temporal Changes in Fractal Dimension

Mycelial systems are not static. Davidson notes that fractal dimension changes with time:

- Systems tend to become more open (lower D) as they mature
- Even initially surface-fractal mycelia become increasingly mass-fractal over months
- Regression of minor cords leaves persistent thick-cord networks behind foraging fronts
- This regression redistributes biomass and nutrients to support further exploration

## Modelling Approaches

### Continuum Models

Continuum models treat the mycelium as a continuous density field rather than tracking individual hyphae:

- **Reaction-diffusion equations**: Describe how biomass density changes over time as a function of local growth, branching, and death rates
- **Nutrient transport equations**: Model diffusion and active translocation of resources through the network
- These models are computationally efficient but lose information about network connectivity

### Network Models

Network (graph-theoretic) models represent the mycelium as a set of nodes (branch points) connected by edges (hyphal segments):

- Each edge has properties: length, diameter, conductance, biomass
- Transport follows physical laws (Poiseuille flow for cytoplasmic streaming)
- Growth occurs at tip nodes, governed by local nutrient gradients

Network models preserve connectivity information crucial for understanding nutrient redistribution but are computationally demanding for large systems.

### Individual-Based Models

The most detailed approach simulates individual hyphae:

- Each hyphal tip extends at a rate determined by local conditions
- Branching angles and frequencies follow species-specific rules
- Septal pores regulate inter-compartment flow
- Vacuolar dynamics within individual hyphae can be modelled

These models capture the most biological detail but are computationally expensive, limiting simulation time and system size.

## Key Modelling Insights

A central finding from modelling work is that complex mycelial patterns emerge from simple local rules:

- No global coordination mechanism is needed to produce efficient foraging networks
- Local sensing of nutrients and neighbors, combined with growth and branching responses, is sufficient
- The observed "intelligence" of mycelial networks is an emergent property

### Trade-offs in Foraging Strategies

Models reveal fundamental trade-offs:

- **Exploration vs. exploitation**: Resources invested in extending search fronts are not available for exploiting found resources
- **Persistence vs. flexibility**: Maintaining connections to old resources constrains reallocation to new ones
- **Speed vs. thoroughness**: Rapid extension covers more ground but samples each location less intensively

### The Role of Cord Formation

Cord formation (hyphal aggregation into high-conductivity channels) is modelled as a response to nutrient gradients:

- Cords form along paths of net nutrient flow, reinforcing successful transport routes
- This positive feedback creates preferred pathways that become self-reinforcing
- Models show cord formation dramatically increases the efficiency of long-distance translocation
- The threshold conditions for cord initiation are a key parameter determining network architecture

## Challenges and Limitations

### Parameter Estimation

The major modelling challenge is obtaining accurate parameter values:

- Hyphal extension rates vary with temperature, nutrients, and species
- Branching probabilities are context-dependent
- Transport coefficients within hyphae are difficult to measure in vivo
- Most models require simplifying assumptions

### Validation

Comparing model predictions to experiments is difficult:

- 2D models cannot fully capture 3D soil environments
- Laboratory microcosms differ from natural field conditions
- Some model outputs (internal nutrient distributions) are not directly measurable
## See Also

- [[mycelial-network-nutrient-dynamics]]
- [[gadd-mycelial-network-dynamics]]
- [[fungal-mycelial-foraging-heterogeneous-environments]]
