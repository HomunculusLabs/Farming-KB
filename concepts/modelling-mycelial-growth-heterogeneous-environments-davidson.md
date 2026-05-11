# Modelling Mycelial Growth in Heterogeneous Environments

## Overview
[[gadd-mathematical-modelling-fungal-mycelia]] provides a powerful tool for understanding how fungal mycelia
grow, function, and interact with their environments. By combining continuum
(partial differential equation) models with discrete (cellular automaton) approaches,
researchers can simulate mycelial growth in both uniform and heterogeneous
environments — including soils — with remarkable accuracy. This work, pioneered by
F.A. Davidson, G.P. Boswell, and colleagues, bridges [[bloomfield-buller-experimental-mycology]] with
computational biology. (see [[mathematical-modelling-fungal-mycelia-davidson]]).

## The Continuum Model
The foundation is a continuum mathematical model that describes mycelial growth
as a density field over space and time. The model captures several key processes:

### Core Processes Modelled
1. **Tip extension**: Growth occurs at hyphal tips, which extend into the
   surrounding medium at a rate dependent on internal nutrient reserves and
   external conditions. (see [[mycelial-growth-modeling-heterogeneous-environments]]).
2. **Substrate uptake**: Hyphae absorb nutrients (particularly carbon sources) from
   the surrounding environment through their surface area.
3. **Active translocation**: Internal nutrients are actively transported through
   the hyphal network from regions of surplus to regions of deficit, powering
   tip extension at the colony margin.
4. **Passive translocation (diffusion)**: Internal nutrients also move by
   diffusion over short distances within the hyphal network.
5. **Hyphal inactivation and reactivation**: Hyphae can become inactive when
   nutrient-depleted and be reactivated when nutrients become available.
6. **Branching**: New hyphal tips are produced through branching, with branching
   rate influenced by internal [[leaf-tissue-analysis-crop-nutrient-status]].
7. **Anastomosis**: Hyphae fuse where they contact each other, creating
   connections that enable [[lowenfels-mycorrhizal-network-nutrient-sharing]] and network formation.

### Environmental Interactions
The model accounts for the fungus's impact on its environment:
- **Acidification**: [[singh-fungal-metabolism-pahs]] acidifies the surrounding medium, which
  is modelled as proportional to internal substrate concentration.
- **Nutrient depletion**: External substrate is consumed as the colony grows,
  creating gradients that influence [[gadd-spitzenkorper-vesicle-supply-centre-hyphal-tip-growth-direction]].

## Tessellated Agar Droplet Experiments
The model was validated against experimental data from a tessellated agar droplet
system:
- Molten agar was pipetted into hexagonal arrays of 19 circular droplets (10 mm
  diameter) separated by 2 mm nutrient-free gaps.
- 16 combinations of droplet compositions were tested using standard medium,
  glucose-amended, calcium phosphate-amended, and both glucose and calcium
  phosphate amendments.

The model accurately replicated observed growth characteristics and extended
experimental results by explicitly mapping internal substrate concentrations and
predicting acidification patterns.

## Active vs Passive Translocation: A Reversal of Assumptions
One of the most significant insights from modelling concerns the roles of active
and passive translocation:

### Traditional Assumptions
- **Active translocation** = associated with exploration (outgrowth)
- **Passive translocation** (diffusion) = associated with exploitation (substrate
  utilization)

### Model Findings
The modelling results suggest the reverse:
- **Active translocation** is crucially involved in the initial exploitative
  phase. When active translocation rate was decreased, substrate uptake on newly
  colonized droplets decreased because less internal substrate was carried to
  hyphal tips, reducing the energy available for active uptake.
- **Passive translocation** (diffusion) is primarily used as a short-range
  exploratory mechanism, allowing nutrients to spread to nearby potential growth
  sites.

This reversal has important implications for understanding how fungi prioritize
resource exploitation versus exploration.

## The Hybrid Discrete-Continuum Model
For growth in heterogeneous environments (particularly soils), a continuum approach
is less relevant because growth is sparse and individual hyphae matter. The
researchers developed a hybrid model:

### Structure
- **Space**: Modelled as an array of hexagonal cells on a triangular lattice.
- **Time**: Discrete time steps.
- **Transition probabilities**: Derived from the finite-difference discretization
  of the continuum model, creating a meaningful link between the two approaches.

### Novel Features
The model uniquely combines:
- **"Cell" models**: Used for modelling internal/external substrate and hyphal
  tips (each cell takes a value representing current state).
