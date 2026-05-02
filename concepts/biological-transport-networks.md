---
title: Biological Transport Networks
tags: [biology, networks, physics, transport]
date: 2026-04-28
updated: 2026-04-28
sources: [/Users/t3rpz/wiki/raw/papers/unknown-mycelium-running.md]
---

# Biological Transport Networks

Biological transport networks are branched distribution systems that move
materials — nutrients, gases, signalling molecules, waste — across spatial
scales within and between organisms. They are found in every kingdom of
life and share remarkable design principles despite their diverse
evolutionary origins. Prominent examples include fungal mycelia, animal
vasculature, plant xylem and phloem, and slime mould foraging networks.

## Universal Design Principles

### Murray's Law

Formulated by Cecil Murray in 1926 for blood vessels, Murray's law states
that the cube of the radius of a parent vessel equals the sum of the cubes
of the radii of daughter vessels (r₀³ = r₁³ + r₂³). This minimises the
biological work of maintaining the vessel plus the work of pumping fluid
through it. The same principle has been observed in:

- **Xylem conduits** in vascular plants
- **Hyphal branching** in fungal networks
- **Tracheal tubes** in insect respiratory systems
- **Slime mould veins** in *Physarum polycephalum*

### Supply-Demand Matching

Efficient transport networks dynamically adjust capacity to local demand:

- **Angiogenesis** creates new blood vessels in response to hypoxia.
- **Fungal cords** thicken along productive foraging routes.
- **Xylem** produces wider vessels in environments with high transpiration
  demand.
- **Leaf venation** density correlates with photosynthetic capacity.

### Redundancy and Robustness

Biological networks are typically highly redundant. In mammalian vasculature,
the presence of multiple parallel pathways means that occlusion of a single
vessel rarely causes tissue death. Similarly, fungal mycelia maintain
multiple connections between resource patches, allowing the network to
function even when substantial portions are damaged.

## Fungal Networks as Model Systems

Slime moulds (*Physarum polycephalum*) have become a model organism for
studying biological network optimisation. Despite lacking a nervous system,
*Physarum* can:

- **Solve mazes** by finding the shortest path between food sources
  (Nakagaki et al., 2000).
- **Recreate the Tokyo rail network** with comparable efficiency to human
  engineers when food sources are placed at city locations (Tero et al.,
  2010).
- **Make adaptive decisions** by weighting connections proportional to
  nutrient flux, implementing a form of reinforcement learning.

These behaviours emerge from simple local rules: tubes carrying more flow
widen, while unused tubes are pruned — a positive feedback loop that
optimises the network without central coordination.

## Mathematical Frameworks

### Minimum Cost Hypothesis

Many biological networks appear to minimise a cost function combining
conduction resistance and construction material:

    Cost = α × resistance + β × material volume

The balance between α and β determines the optimal branching angle and
vessel taper, and varies with organism size and metabolic demand.

### Allometric Scaling

West, Brown, and Enquist's (1997) metabolic scaling theory predicts that
biological transport networks constrain metabolic rate to scale as mass
raised to the 3/4 power. This arises from the fractal branching of
distribution networks that fill space while minimising transport distance.

### Graph-Theoretic Approaches

Network analysis has revealed that biological transport systems often
exhibit **small-world** properties (short characteristic path length with
high clustering), **scale-free** degree distributions (few highly connected
hubs, many weakly connected nodes), and **modular** community structure
that isolates damage to local regions.

## Plant Vascular Systems

### Xylem

Xylem is the water-conducting tissue in vascular plants, composed of dead,
hollow cells (tracheids and vessels) that form continuous columns from roots
to leaves. Key design features:

- **Pit membranes** between adjacent conduits allow water passage while
  trapping air bubbles (embolism resistance).
- **Scalariform, reticulate, and pitted** secondary wall thickening
  patterns balance mechanical strength against conductance.
- **Conduit diameter** increases from tips to base following Murray's
  law, minimising flow resistance per unit investment.
- **Cavitation** — the formation of vapour bubbles under tension — is
  a major failure mode, especially during drought.

### Phloem

Phloem transports photosynthates from source (leaves) to sink (roots,
fruits, growing tips) tissues via the pressure-flow hypothesis (Münch,
1930): osmotic loading of sugars at sources creates hydrostatic pressure
driving bulk flow toward sugar-depleted sinks. Transport speed ranges from
0.5–2 m/h, with sieve tube elements connected by porous sieve plates.

## Applications

Understanding biological transport networks has inspired engineering
solutions:

- **Microfluidic chip design** borrowing from leaf venation patterns.
- **Urban logistics optimisation** informed by slime mould networks.
- **Traffic flow algorithms** based on ant foraging trail formation.
- **Distributed sensor networks** mimicking fungal resource sensing.

## See Also

- [[savory-biological-pest-control-and-succession]]
- [[growing-gourmet-biological-efficiency-yield]]
- [[ingham-glomalin-biological-soil-glues]]

- [[mycelial-network-structure]]
- [[wood-wide-web]]
- [[fungal-ecology]]
