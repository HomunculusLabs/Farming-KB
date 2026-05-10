---
title: "Mycelial Network Graph Theory Analysis Cord Architecture and Transport Routing"
source: "geoffrey-gadd-sarah-c-watkinson-paul-s-dyer-fungi-in-the-environment.md"
source_author: "Bebber, Tlalka, Hynes, Darrah, Ashford, Watkinson, Boddy, Fricker"
source_book: "Fungi in the Environment"
published: 2007
tags: [mycelial-network, graph-theory, fungal-cords, network-analysis, nutrient-transport, phanerochaete-velutina, foraging, resource-allocation]
---

# Mycelial Network Graph Theory and Cord Transport Routing

## Overview

Bebber, Fricker, and colleagues developed a novel approach to
analyzing fungal mycelial architecture using graph theory —
translating the morphological structures of corded fungal networks
into mathematical graph representations. This framework, presented
in *Fungi in the Environment*, enables quantitative comparison of
fungal foraging strategies, assessment of network resilience, and
modeling of nutrient transport routing across complex mycelial
systems spanning meters of territory.

## Corded Mycelial Networks as Spatial Graphs

Basidiomycete fungi form complex networks of persistent,
specialized high-conductivity channels called cords that can extend
for meters or hectares. These cords connect resource patches
through branch points and junctions, forming the transport
infrastructure of the mycelial colony.

The graph representation translates morphological structures:
- **Nodes (vertices):** Branch points, junctions, and resource
  bases (wood blocks, agar inoculum)
- **Links (edges):** Persistent cords connecting nodes
- **Degree (k):** Number of links per node — tips have degree 1,
  branch points typically degree 3

Resource bases (agar or wood blocks) are each represented as a
single node since internal fine mycelial structure cannot be
resolved at this scale.

## Network Development Over Time

Mycelial networks are not static — they are continuously
reconfigured in response to local nutritional cues, environmental
conditions, damage, or predation through growth, branching, fusion,
and regression. Time-lapse imaging of mycelial networks growing on
compressed soil from wood-block inocula reveals dynamic architectural
development over periods of days to weeks.

As a colony grows from its resource base, nutrient translocation
flows predominantly toward the growing margin. When new resources
are found, redistribution back to the base can occur through
potentially different transport pathways. The network architecture
represents a balance between efficient resource capture, tolerance
to damage, and metabolic cost.

## Comparative Network Measures

The graph-theoretic framework enables quantitative comparison of
fungal networks using standard network analysis metrics:

- **Node degree distribution:** Pattern of connections per node
- **Network diameter:** Longest shortest path between any two nodes
- **Total link length:** Sum of all cord lengths (metabolic cost)
- **Mean shortest path:** Average minimum steps between nodes
- **Clustering coefficient:** Degree of local interconnectedness
- **Alpha index:** Ratio of actual circuits to maximum possible
- **Beta index:** Ratio of links to nodes
- **Gamma index:** Ratio of actual links to maximum possible links

These measures allow comparison between fungal species, growth
stages, and environmental conditions.

## Resilience Testing: Random vs. Targeted Removal

The framework supports simulated damage experiments by removing
nodes or links from the graph model:

- **Random node removal:** Simulates non-specific damage (e.g.,
  trampling, grazing)
- **Random link removal:** Simulates cord breakage
- **Targeted removal:** Simulates directed attack on critical
  network components

Comparing fungal networks against mathematical test networks
(Delaunay triangulation, relative neighbourhood graph, minimum
spanning tree) reveals how fungal architecture balances
connectivity with efficiency. Fungal networks typically show
intermediate properties — more connected than minimum spanning
trees (providing redundancy) but less connected than Delaunay
triangulations (conserving resources).

## Route Switching and Transport Dynamics

Radioisotope tracing with 14C-labelled amino-isobutyric acid
(AIB) revealed complex transport dynamics in *Phanerochaete
velutina* networks. Key observations include:

- Rapid transport — AIB traveled 250 mm along major cords within
  one hour of loading
- **Route switching:** Pre-existing cords became transiently
  labelled as alternative transport routes, then fell silent —
  the network dynamically reroutes nutrients
- Not all cords transport simultaneously — the network shows
  selective activation of specific pathways
- **Pulsatile transport:** Nutrient movement occurs in oscillating
  pulses with distinct frequency, amplitude, and phase domains

## Phase Synchronization Domains

Fourier analysis of time-series transport data revealed that
different regions of the mycelial network oscillate with locally
synchronized behavior. Assimilatory hyphae in the inoculum, new
resources, and foraging hyphae all oscillate but are out of phase
with each other. These phase differences establish distinct
synchronization domains across the colony.

## Comparison with Other Biological Networks

The graph-theoretic approach places fungal mycelial networks in
context with other biological networked systems: ecological food
webs, metabolic networks, and genetic regulatory networks. Tools
originally developed for graph theory (Albert and Barabasi, Strogatz,
Dorogovtsev and Mendes, Newman, Amaral and Ottino) prove applicable
to fungal systems, suggesting universal principles of biological
network organization.

## Implications for Understanding Fungal Ecology

This framework provides tools to address fundamental questions:
Are there specific global mechanisms coupling local sensory
perception across the colony, or is collective behavior an emergent
property of local hyphal interactions? How do different species
optimize the tradeoff between transport efficiency, damage
tolerance, and resource capture cost? These questions connect
fungal physiology to broader principles of biological network
design and resilience.

## See Also

- [[mycelial-network-nutrient-dynamics]]
- [[fungal-pulsatile-nutrient-transport-mycelial-networks]]
- [[fungal-mineral-transformations-biogeochemical-cycles]]
- [[environmental-sensing-filamentous-fungi-read]]
