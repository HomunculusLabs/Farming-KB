---
title: Mycelium Network Architecture
created: 2026-04-28
tags: [[mycology]], fungal-biology, networks, ecology]
date: 2026-04-28
updated: 2026-04-28
sources: [/Users/t3rpz/wiki/raw/papers/unknown-mycelium-running.md]
type: concept
---

# [[mycelial-networks]] exhibit several distinct topological patterns depending on
species and environment:

- **Foraging networks** (e.g., *Physarum*, *Phanerochaete*): Radial
  structures with thick transport cords connecting exploration fronts. These
  balance exploration (extensive thin hyphae) with exploitation (dense
  transport highways).
- **Rhizomorphic networks**: Organized into differentiated cord-like
  structures with specialized vascular hyphae for long-distance transport.
- **Diffuse networks**: Uniform distribution of hyphae without obvious
  differentiation, common in decomposer fungi.

Research on *[[mycelial-networks]]
maintain connectivity while maximizing resource capture through a combination
of tip growth, branching, and fusion (anastomosis). The networks show
remarkable resilience, reconnecting around damaged areas.

## Transport Mechanisms

Mycelial networks move resources through two primary mechanisms:

1. **Cytoplasmic streaming**: Bulk flow of cytoplasm carrying organelles,
   nutrients, and signaling molecules along hyphae. Driven by motor proteins
   (myosin, kinesin) on actin microfilaments. Speeds reach 5–60 cm/hour.
2. **Diffusion**: Passive movement of small molecules along concentration
   gradients. Effective over short distances but insufficient for long-range
   resource distribution.

Translocation experiments using radioactive tracers showed that wood-decay
fungi can move carbon and phosphorus over distances exceeding one meter
through their networks, preferentially directing resources to growing tips
and nutrient-rich patches.

Cytoplasmic streaming is the dominant transport mechanism for bulk resource
movement in mycelial networks. The process is driven by the coordinated
action of myosin motor proteins moving along actin microfilaments that run
parallel to the hyphal axis. In mature, differentiated hyphae within cords
and rhizomorphs, specialized vascular hyphae develop wider diameters (up to
50 micrometers) and reduced septation, creating low-resistance conduits for
rapid cytoplasmic flow. These vascular hyphae are analogous to the xylem
and phloem of plants in their function, though they evolved independently.
The direction of cytoplasmic flow can reverse rapidly in response to
nutrient gradients, allowing the network to redirect resources toward newly
discovered nutrient sources within minutes.

Mycelial networks also transport signaling molecules that coordinate behavior
across the network. When one part of a mycelial network encounters a
resource, signals propagate through the network to stimulate growth toward
that resource and suppress exploration in unproductive directions. Research
using microelectrode arrays has detected electrical potential waves that
propagate through mycelial networks at speeds of 0.5-2 mm/s, suggesting
an electrical signaling mechanism in addition to chemical and hydraulic
signaling. These electrical signals may enable long-distance coordination
of growth and resource allocation across networks spanning many centimeters
or meters.

## Network Resilience

Mycelial networks demonstrate significant resilience to damage. When
connections are severed, fungi can:

- Redirect cytoplasmic flow through alternative pathways
- Regrow connections around damaged areas
- Adjust branching patterns to restore network efficiency
- Sacrifice less productive sectors to maintain core transport routes

Studies using graph-theoretic analysis showed that mycelial networks share
properties with engineered resilient networks, maintaining short path lengths
and high connectivity even after random edge removal.

Network optimization theory provides a framework for understanding mycelial
architecture. Research by Dan Bebber and colleagues at Oxford University
applied graph theory to digitized images of [[phanerochaete-velutina]]* growing across soil and wood chip substrates.
They found that fungal networks minimize the total length of connections
while maintaining multiple redundant pathways between resource nodes, an
optimization problem analogous to the minimum spanning tree with redundancy
constraints. This cost-benefit tradeoff between building and maintaining
network material versus ensuring connectivity produces networks that
approximate solutions found by human engineers designing transportation
and communication networks. The networks also demonstrate "graceful
degradation": as connections are severed, the network reroutes resources
through alternative pathways with minimal loss of overall function, a
property that makes them robust models for studying fault-tolerant systems
in computer science and engineering. The degree of network optimization
varies with environmental predictability; in stable environments with
permanent resource patches, networks converge toward more efficient,
streamlined configurations, while in variable environments they maintain
more exploratory, redundant architectures.
- [[fungal-ecology]]
