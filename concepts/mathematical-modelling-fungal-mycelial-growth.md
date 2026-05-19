---
title: Mathematical Modelling of Fungal Mycelial Growth and Function
source: geoffrey-gadd-sarah-c-watkinson-paul-s-dyer-fungi-in-the-environment.md
type: concept
---

# Mathematical Modelling of Fungal Mycelial Growth and Function

## Overview

Mathematical modelling provides a powerful complement to experimental studies of fungal mycelia, enabling researchers to isolate key processes, test hypotheses, and make predictions about growth dynamics that are difficult to measure directly. The work of Davidson, Boswell, and colleagues has developed a comprehensive modelling framework that connects **hyphal-level physiology** (tip growth, branching, nutrient uptake) to **mycelial-level function** (biomass distribution, translocation, acidification) across both **uniform and heterogeneous environments**. Their approach spans continuum (density-based) and discrete (network-based) formulations within a single coherent framework.

## Why Model Fungi?

Fungi present unique modelling challenges and opportunities:

- **Scale**: Mycelia operate from the sub-micron (individual hyphae) to the metre scale (colony networks).
- **Heterogeneity**: Natural growth environments (soils, wood, leaf litter) are spatially complex.
- **Complexity**: Interconnected processes—growth, translocation, anastomosis, resource uptake—operate simultaneously.
- **Inaccessibility**: Many processes (e.g., internal nutrient translocation) are difficult to measure experimentally.

As Turing (1952) noted, a mathematical model is "a simplification and an idealisation." The goal is not to replicate every detail but to identify and investigate key properties through rigorous logical structure.

## The Five-Variable Model

The core model represents the mycelium as a distribution of five interacting variables:

| Variable | Description |
|---|---|
| **Active hyphae** | Hyphae involved in translocation of internal metabolites |
| **Inactive hyphae** | Hyphae not involved in translocation or growth (moribund) |
| **Hyphal tips** | Growing apices that extend and create new hyphae |
| **Internal substrate** | Nutrients within the fungal biomass (assumed to be carbon) |
| **External substrate** | Nutrients in the surrounding environment |

### Model Equations

The model equations track how each variable changes in space and time:

1. **Active hyphae** change due to: new hyphae laid down by moving tips + reactivation of inactive hyphae − inactivation of active hyphae
2. **Inactive hyphae** change due to: inactivation of active hyphae − reactivation − degradation
3. **Hyphal tips** change due to: movement out of/into area + branching from active hyphae − anastomosis (tip–hypha fusion)
4. **Internal substrate** changes due to: translocation (active + passive) + uptake from external sources − maintenance costs − tip growth costs − active translocation costs
5. **External substrate** changes due to: diffusion − fungal uptake

### Key Physiological Assumptions

- **Tip growth**: Hyphae extend in approximately straight lines with small random fluctuations; growth rate depends on internal substrate status.
- **Branching**: Proportional to internal substrate concentration (consistent with the role of turgor pressure and tip vesicle accumulation).
- **Nutrient uptake**: Depends on external substrate concentration, internal substrate (energy for active transport), and hyphal biomass (membrane surface area).
- **Translocation**: Both **active** (metabolically driven, towards tips) and **passive** (diffusive) mechanisms for carbon redistribution.

## Continuum Approach

### Method

Variables are treated as continuous densities, producing a system of **nonlinear partial differential equations** solved using finite-difference approximation on a square grid:

- Space is divided into grid cells, each containing quantities of all five variables.
- Time is divided into discrete steps; variables update according to the model equations.
- Both local values and gradients (neighbourhood effects) are considered at each step.

### Calibration and Validation

The model was calibrated using *[[rhizoctonia-solani]]* AG4 (R3) grown on mineral salts medium with 2% glucose at 30°C:

- Tip velocities, branching rates, and anastomosis rates estimated from 15-hour time-lapse images.
- Diffusion coefficients and uptake rates taken from literature.
- **Validation**: Modelled colony radial expansion matched experimental measurements at 30°C.
- **Temperature prediction**: Applying the Q₁₀ rule (reaction rate halves per 10°C decrease) to tip velocity alone predicted 15°C growth with surprising accuracy.

### Key Finding: Role of Active Translocation

A remarkable result emerged when **active translocation was disabled** in the model:

- Radial growth rate and biomass distribution in uniform, substrate-rich conditions were **largely unaffected**.
- **Conclusion**: Diffusion alone is sufficient for internal metabolite redistribution in nutrient-rich habitats.
- **Prediction**: *R. solani* does not use energetically costly active translocation in favourable conditions, relying instead on the "energy-free" process of diffusion.

### Heterogeneous Environments

The model was applied to **tessellated agar droplet systems** (Jacobs et al., 2002b)—hexagonal arrays of nutrient-rich and nutrient-free droplets separated by 2 mm gaps:

- Model predictions matched experimental growth patterns across multiple tessellation configurations.
- The model extended experimental results by explicitly mapping internal substrate concentrations.
- **Critical insight on translocation roles**: Decreasing active translocation reduced substrate uptake on newly colonised droplets (less internal substrate at tips = less energy for active uptake). This suggests:
  - **Active translocation** is crucially involved in the **exploitative phase** (establishing uptake on new resources).
  - **Passive translocation** (diffusion) serves as a **short-range exploratory mechanism**.

This reverses the traditional view that associated active transport with exploration and diffusion with exploitation.

### Acidification Modelling

Since *R. solani* produces acidity only in the presence of utilizable carbon, and internal substrate represents carbon in the model, acidity production was modelled as proportional to internal substrate concentration:

- Model pH profiles accurately replicated experimental pH gradients.
- Provides spatial predictions of acidification that extend beyond experimental resolution.

## Hybrid Discrete-Continuum Model

### Motivation

Continuum models are ideal for **dense** mycelia (e.g., on agar plates) but become less appropriate when growth is **sparse**, as in nutrient-poor conditions or structurally heterogeneous environments (soils). Discrete models—where individual hyphae are explicitly represented—better capture network structure but have traditionally suffered from:

- Non-mechanistic rules for growth and branching.
- Difficulty in parameterisation.
- Computational expense that prevented inclusion of **anastomosis** and **translocation**.

### The Hybrid Approach

The Davidson/Boswell hybrid model overcomes these problems by **deriving the discrete model directly from the calibrated continuum model**:

- Space: Hexagonal cell array with mycelium defined on the embedded triangular lattice.
- Time: Discrete steps with transition probabilities derived from the finite-difference discretization of the continuum equations.
- **Dual representation**: "Cell" models for substrate and tips (particles at sites) + "bond" models for hyphae (connections between sites).

### Why Cell + Bond Models?

- **Cell models**: Ideal for particle-like quantities (substrate concentration, tip presence/absence at a site).
- **Bond models**: Essential for network modelling—adjacent hyphae running in parallel should NOT be automatically connected. Connections occur only at **anastomosis points**, which bond models represent explicitly.
- Without the bond approach, parallel hyphae would spuriously exchange internal substrate.

### Performance

The hybrid model:

- Replicates qualitative features of mycelial growth in uniform conditions.
- Produces fractal dimensions consistent with experimental observations.
- Enables study of relationships between substrate concentration and fractal dimension.
- Uses **identical parameter values** as the calibrated continuum model—no re-parameterisation needed.

## Growth and Function in Soils

### Modelling Soil Heterogeneity

Soils present spatiotemporal, nutritional, and structural heterogeneity:

- **Structural**: Determined by particle locations and pore space architecture.
- **Nutritional**: Modulated by water film distribution; nutrients confined to water films due to surface tension.
- **Water films**: Nutrients diffuse within films but not across the air-water interface.

### Model Soil Construction

Artificial soil structures were created by randomly removing hexagonal cell blocks from the growth domain:
## See Also

- [[fungal-mycelial-network-graph-theory]] — Network topology analysis of corded mycelia
- [[fungal-network-resilience-evolution]] — Resilience and evolutionary dynamics of [[fungal-mycelial-networks-nutrient-translocation]]
- [[pulsatile-nutrient-transport-fungal-mycelia]] — Oscillatory nutrient dynamics in mycelia
