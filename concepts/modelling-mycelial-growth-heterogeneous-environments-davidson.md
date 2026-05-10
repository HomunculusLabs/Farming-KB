# Modelling Mycelial Growth in Heterogeneous Environments

## Overview
Mathematical modelling provides a powerful tool for understanding how fungal mycelia
grow, function, and interact with their environments. By combining continuum
(partial differential equation) models with discrete (cellular automaton) approaches,
researchers can simulate mycelial growth in both uniform and heterogeneous
environments — including soils — with remarkable accuracy. This work, pioneered by
F.A. Davidson, G.P. Boswell, and colleagues, bridges experimental mycology with
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
   rate influenced by internal nutrient status.
7. **Anastomosis**: Hyphae fuse where they contact each other, creating
   connections that enable nutrient sharing and network formation.

### Environmental Interactions
The model accounts for the fungus's impact on its environment:
- **Acidification**: Fungal metabolism acidifies the surrounding medium, which
  is modelled as proportional to internal substrate concentration.
- **Nutrient depletion**: External substrate is consumed as the colony grows,
  creating gradients that influence growth direction.

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
- **"Bond" models**: Used for modelling active/inactive hyphae as connections
  between cells.

This distinction is critical because a cell-based approach alone would
automatically connect adjacent hyphae, allowing nutrient transfer that wouldn't
occur in reality. The bond-based approach explicitly models anastomosis points,
accurately representing when parallel hyphae can and cannot share resources.

## Growth and Function in Soils
Soils present particular challenges: spatiotemporal, nutritional, and structural
heterogeneity. The model simulates soil conditions by randomly removing hexagonal
blocks to create artificial pore spaces.

### Key Findings
- Early biomass growth is confined to water films where external substrate is
  available.
- A small number of tips emerge from water films and extend rapidly across pore
  spaces to locate new substrate resources.
- Water surface tension plays a significant role: reducing surface tension in the
  model results in greater biomass distribution in pore spaces and faster overall
  expansion.
- The fractal dimension of model growth matches experimental observations from
  real soil systems.

## Biotechnology Applications
Mathematical modelling of mycelial growth has direct applications:
- **Biological control agents**: Fungi used as biocontrol agents against plant
  pests and diseases operate in heterogeneous soil environments.
- **Bioremediation**: Fungi that transform toxic metals operate in contaminated
  soils with complex spatial heterogeneity.
- **Nutrient cycling**: Understanding how fungi explore and exploit soil resources
  improves predictions of decomposition and nutrient availability.

The combination of modelling with experimental data yields more detailed results
than either approach alone. Mathematical modelling is predicted to play a central
role in the successful application of fungi to biotechnological areas.

## Quantitative Validation
The hybrid model replicates many important qualitative and quantitative features:
- Colony radial expansion rates
- Biomass distribution patterns
- Acidification of the growth environment
- Fractal dimension of mycelial networks
- Relations between substrate concentration and fractal dimension

## Source
- Davidson, F.A. "Modelling of mycelial form and function." In Gadd, G.M.,
  Watkinson, S.C. & Dyer, P.S. (eds.) *Fungi in the Environment*. Cambridge
  University Press. Lines 3500-3770 of the full text.

## See Also
- [[pcsi-scintillation-imaging-mycelial-nutrient-transport-bebber]]
- [[mycelial-cord-network-topology-graph-theory-bebber]]
- [[fungal-mycelial-foraging-heterogeneous-environments]]
- [[fungal-biogeochemical-mineral-transformations]]
