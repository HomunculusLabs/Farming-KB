---
title: Mathematical Modelling Fungal Mycelia Davidson
source: geoffrey-gadd-sarah-c-watkinson-paul-s-dyer-fungi-in-the-environment
tags: [fungal-modelling, mycelial-growth, Rhizoctonia-solani, cellular-automaton, translocation, biomass-distribution]
---

# Mathematical Modelling of Fungal Mycelia

## Overview

Mathematical modelling of [[brassinosteroid-fungal-growth-promotion]] faces the fundamental challenge of
scale. Models must address specific biological questions at appropriate
spatial and temporal scales, with the ultimate goal of constructing multi-
scale models that transfer information from individual gene action through
to the growth and function of large-scale mycelia. Davidson and colleagues
have developed a framework connecting physiology at the hyphal level to
growth and function at the mycelial level, encompassing both continuum and
discrete approaches calibrated against the soil-borne saprotroph
[[gadd-mathematical-modelling-rhizoctonia-solani-mycelial-growth]].

Earlier approaches either focused on the mycelium using variables such as
biomass yield while ignoring spatial properties, or focused on hyphal-level
growth such as tip extension and branching while neglecting temporal
dynamics. The new framework overcomes these limitations by addressing
spatio-temporal properties across scales, using a continuum formulation for
dense growth and a hybrid cellular automaton for sparse growth in
[[fungal-mycelial-foraging-heterogeneous-environments]] such as soils.

## Model Variables and Structure

The mycelium is modelled using five interacting variables: active hyphae
(involved in translocation of internal metabolites), inactive hyphae
(moribund hyphae not involved in translocation or growth), hyphal tips,
internal substrate (nutrients within the fungus), and external substrate
(nutrients free in the environment). A single generic limiting element,
assumed to be carbon, drives the model. Active hyphae change through new
hyphae from tips and reactivation of inactive hyphae. Hyphal tips change
through movement, branching proportional to internal substrate, and
anastomosis. Internal substrate changes through translocation, uptake,
and expenditure on maintenance and growth. External substrate changes
through diffusion and fungal uptake.

## Tip Growth, Branching and Translocation

Hyphal tips tend to move in straight lines with small random directional
fluctuations arising from new wall material incorporation at the tip. Tip
growth rate depends on internal substrate status. Branching is proportional
to internal substrate concentration, consistent with the established
relationship between branching and [[bloomfield-turgor-pressure-and-hyphal-invasion]] or vesicle build-up.
[[aact-microbial-foliar-nutrient-uptake-co2-stomata-ingham]] depends on both external and internal substrate
concentrations and on hyphal biomass representing membrane surface area.

The model includes both active, metabolically driven translocation and
passive diffusive translocation. Active translocation depletes energy
reserves and moves internal substrate towards hyphal tips as the major
growth sinks. A key finding is that when active translocation is disabled,
growth in uniform nutrient-rich conditions is largely unaffected,
suggesting diffusion alone suffices. However, in heterogeneous
environments, reduced active translocation decreases uptake on newly
colonized patches because less internal substrate reaches tips to drive
active uptake.

## Continuum Approach and Calibration

The continuum formulation treats variables as continuous densities
expressed as nonlinear partial differential equations, suited to dense
[[brassinosteroid-psilocybe-cubensis-mycelial-growth-research]] in laboratory conditions. Translocation modelling
accounts for the fractal branching structure by assuming shorter transit
times than free-space diffusion. The model was calibrated using
[[rhizoctonia-solani]] on glucose-amended mineral salts medium, with tip
velocities and branching rates estimated from 15-hour growth images.

Colony radial expansion showed good quantitative agreement with model
biomass expansion. Reducing tip velocity according to the Q10-rule
accurately predicted growth at lower temperatures. Model pH profiles
replicated experimental acidification patterns. Applied to tessellated
agar droplet systems with nutritional heterogeneity, the model predicted
growth characteristics similar to experimental observations and extended
them by explicitly mapping internal substrate concentrations.

## Hybrid Cellular Automaton Model

For sparse growth in structurally [[mycelial-growth-modeling-heterogeneous-environments]], a hybrid
cellular automaton model represents the mycelium as a discrete structure
on a hexagonal lattice while substrates remain continuous. This model
explicitly includes anastomosis and translocation, processes neglected in
earlier discrete models due to computational difficulties. A novel
feature is the simultaneous use of cell models for substrate and tips,
and bond models for active and inactive hyphae, enabling accurate
representation of network formation and internal redistribution.
