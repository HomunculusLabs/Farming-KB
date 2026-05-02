---
title: Fungal Mycelial Modeling
created: 2026-04-14
updated: 2026-04-14
type: concept
tags: [mycology, fungi]
sources: []
---
# Fungal Mycelial Modeling

## Overview

Mathematical modelling provides a powerful complement to experimental approaches for understanding fungal mycelial growth and function. The filamentous, network-forming nature of fungi, their capacity for nutrient translocation, and their growth across spatially heterogeneous environments create systems of such complexity that experimental investigation alone is often insufficient. Models range in scale from subcellular processes (vacuolar transport) through individual hyphal dynamics to colony-level biomass distribution and network topology. As Turing (1952) articulated, a mathematical model is "a simplification and an idealisation" — the art lies in achieving a meaningful balance between biological realism and tractability.

## The Scale Problem

The fundamental challenge in modelling fungal growth is the choice of scale. Historically, modelling efforts have split into two camps:

- **Mycelium-level models** using variables such as biomass yield, which generally ignore spatial properties (e.g., Paustian & Schnürer, 1987; Lamour et al., 2000).
- **Hyphal-level models** focused on tip growth, branching, and anastomosis, which often neglect temporal effects (e.g., Prosser & Trinci, 1979; Heath, 1990; Regalado et al., 1997).

The ultimate goal is multi-scale modelling that transfers information from individual gene action through hyphal physiology to large-scale mycelial growth and function. Recent hybrid approaches are beginning to bridge this gap.

## Continuum (Differential Equation) Models

Continuum models represent the mycelium as a spatial distribution of densities and are best suited for dense mycelial growth such as that observed in Petri dishes or on solid substrates. They typically take the form of systems of **nonlinear partial differential equations** representing the interaction of fungal biomass with a growth-limiting substrate.

### The Boswell–Davidson Model

A comprehensive continuum model was developed by Boswell, Jacobs, Davidson, Gadd, and Ritz, based on the saprotroph *Rhizoctonia solani*. The model tracks five state variables:

1. **Active hyphae** — involved in translocation of internal metabolites
2. **Inactive hyphae** — not involved in translocation or growth (moribund)
3. **Hyphal tips** — sites of growth and extension
4. **Internal substrate** — carbon-based metabolites within the fungus
5. **External substrate** — carbon source in the environment

The model equations describe:

- **Tip extension:** Tips move in approximately straight lines with small random fluctuations; rate depends on internal substrate status.
- **Branching:** Proportional to internal substrate concentration, reflecting the role of turgor pressure and tip vesicle accumulation.
- **Nutrient uptake:** Active transport depending on both external substrate concentration and internal energy status, proportional to hyphal membrane surface area.
- **Active translocation:** Metabolically driven movement of internal substrate toward hyphal tips (the major energy sinks).
- **Passive translocation:** Diffusive redistribution of internal substrate.
- **Hyphal inactivation and reactivation:** Dynamic cycling between active and inactive states.

### Key Predictions from Continuum Modelling

- **Temperature effects captured by a single parameter:** Applying the Q₁₀ rule (reaction rate approximately halves per 10 K decrease) to tip velocity alone generated radial growth predictions at 15°C that closely matched experimental data from calibration at 30°C.
- **Diffusion suffices in uniform conditions:** When active translocation was disabled, radial growth rate and biomass distributions were largely unaffected in uniform, substrate-rich conditions. The model predicts that *R. solani* relies on diffusion (not active translocation) for internal metabolite redistribution in resource-rich habitats.
- **Active translocation is crucial in heterogeneous environments:** Reducing active translocation rates decreased substrate uptake on newly colonized resource droplets, because less internal substrate reached hyphal tips and less energy was available for active uptake. This reverses the traditional assumption that active translocation serves exploration while diffusion serves exploitation — modelling suggests active translocation is crucially involved in the initial exploitative phase.
- **Acidification prediction:** By modelling acid production as proportional to internal substrate concentration (since acidity arises from proton efflux and organic acid excretion during carbon metabolism), model pH profiles accurately replicated experimental measurements.

## Discrete (Individual-Based) Models

When growth is sparse — as in nutrient-poor conditions or structurally heterogeneous environments like soils — continuum approaches are less appropriate. Discrete models identify individual hyphae and typically take the form of computer simulations.

### Limitations of Traditional Discrete Models

Early discrete models (Hutchinson et al., 1980; Bell, 1986; Kotov & Reshetnikov, 1990; Ermentrout & Edelstein-Keshet, 1993) used non-mechanistic rules to generate tip extension and branching. While they produced images nearly indistinguishable from real fungi in uniform conditions, they suffered from:

- Need for complete recalibration when modelling the same species in different environments or different species
- Inability to test hypotheses about growth dynamics and function when underlying mechanisms were not modelled
- Neglect of anastomosis and translocation due to computational constraints

### Hybrid Cellular Automaton Model

A novel hybrid approach (Boswell et al., 2006) derives discrete growth rules directly from the calibrated continuum model, overcoming key limitations:

- **Spatial representation:** Space is modelled as an array of hexagonal cells with the mycelium defined on the embedded triangular lattice.
- **Dual representation:** 'Cell' models track internal/external substrate and hyphal tips (presence/absence at each site), while 'bond' models track active/inactive hyphae (connections between adjacent cells). This distinction is critical: adjacent parallel hyphae are not automatically connected — connections occur only at anastomosis points.
- **Derivation from continuum model:** Transition probabilities are derived from the finite-difference discretization of the continuum equations, providing a meaningful mechanistic link between classical continuum and discrete approaches.
- **Explicit inclusion of anastomosis and translocation:** These crucial processes for heterogeneous environments are directly modelled.
- **Parameter consistency:** Parameter values in the discrete model are exactly those from the calibrated continuum model — no re-parameterization is needed.

The hybrid model replicates qualitative features of mycelial growth in uniform conditions and produces consistent fractal dimensions. Relations between substrate concentration and fractal dimension have been established.

## Fractal Geometry in Mycelial Description

Fractal geometry provides quantitative tools for describing mycelial patterns that cannot be captured by Euclidean measures:

- **Mass fractal dimension (D_M):** Describes space-filling when there are gaps in the interior (D ranges from 1 = linear to 2 = plane-filling in 2D).
- **Surface/border fractal dimension (D_S):** Describes boundary complexity.
- **Box-counting method:** The most common technique for determining fractal dimensions of mycelia, yielding D_BM and D_BS.

Different foraging strategies produce characteristic fractal signatures:
- Long-range foragers (mass fractal): D_M > D_S, with well-defined open corded networks
- Short-range foragers (surface fractal): D_S < D_M, with diffuse, plane-filling colonies

Temporal changes in fractal dimension reflect developmental shifts: systems become more open (lower D) over time as fine hyphae and minor cords regress, leaving persistent corded networks.

## Network Analysis

Mycelial networks can be represented as graphs with nodes (branch points, junctions, anastomoses, resource bases) connected by links (persistent cords). Network measures include:

- **Node degree distribution:** Tips have degree 1; branch points typically degree 3; resource nodes may have many links (hub-like).
- **Minimum path length and network diameter:** Measures of transport efficiency.
- **Clustering coefficient (transitivity):** Probability that two nodes connected to a third are also connected.
- **Alpha, beta, and gamma indices:** Connectivity measures from physical geography.
- **Resilience:** How network properties change as nodes or links are removed — critical for understanding tolerance to grazing and physical damage.

Model networks (Delaunay triangulation, relative neighbourhood graph, minimum spanning tree) provide reference points for comparison. Fungal networks show intermediate connectivity — more connected than minimum spanning trees but less than Delaunay triangulations — reflecting a balance between transport efficiency and construction/maintenance costs.

## Modelling Growth in Structured Media (Soils)

Soils exhibit spatiotemporal, nutritional, and structural heterogeneity. Structural heterogeneity arises from particle arrangement and pore space, while nutritional heterogeneity is modulated by water distribution in non-saturated soils (nutrients confined to water films by surface tension).

Artificial porous media can be constructed by randomly removing hexagonal blocks from the growth domain. Model predictions for soil-like environments show:

- **Early growth confined to water films:** External substrate is taken up for tip extension within the film region.
- **Bridging of air-filled pores:** A small number of tips emerge from the water film and rapidly cross pore spaces to locate new substrate resources.
- **Surface tension effects:** Reduced surface tension leads to greater biomass distribution in pore space and faster overall expansion.
- **Fractal dimension comparisons:** The fractal dimension of model pore spaces can be computed and compared with real soil systems.

## Applications and Future Directions

Mathematical modelling of fungal mycelia has practical implications for:

- **Biocontrol:** Predicting how biological control agents deploy in spatially heterogeneous environments
- **Bioremediation:** Understanding functional consequences of fungi growing in contaminated soils with patchy pollutant distributions
- **Nutrient cycling:** Quantifying acidification, solubilization, and nutrient redistribution by mycelial networks
- **Multi-scale integration:** Connecting gene-level regulation through hyphal physiology to ecosystem-level processes

Combining modelling with experimental data yields more detailed qualitative and quantitative results than either approach alone. The hybrid cellular automaton approach, in particular, provides a framework for bridging scales — from individual hyphal behaviour to network-level function — that was previously intractable.

## See Also

- [[mycelium-composites-materials]] — Structure and biology of mycelial networks
- [[fungal-growth-dynamics]] — Experimental observations of fungal growth patterns
- [[fungal-enzymatic-capabilities]] — Enzyme production and substrate utilization
- soil biology fundamentals — Soil as a growth medium for mycelial fungi
- [[saprotrophic-fungi]] — The primary functional group studied in mycelial models

## Related

- [[fungal-chromogens-and-color-change]]
- [[fungal-carbon-substrate-utilization-efficiency]]
- [[biodiversity-of-fungi-biomass-carbon-soil-structure]]
- [[fungal-mycelial-foraging-resource-heterogeneity]]
