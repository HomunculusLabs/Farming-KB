---
title: "gadd-mycelial-network-dynamics Graph Theory Analysis — Modeling Fungal Foraging Networks"
source: "Fungi in the Environment (Gadd, Watkinson, Dyer)"
topics: [fungi, mycelium, network-theory, graph-theory, foraging, nutrient-transport, cords, resilience]
---

# Mycelial Network Graph Theory Analysis

## Overview

[[gadd-mathematical-modelling-fungal-mycelia-form-function]] complex, spatially extended networks that can be analyzed using graph theory — the mathematical study of networks represented as nodes connected by links. This approach, pioneered by researchers studying cord-forming basidiomycetes, translates the [[ectomycorrhizal-morphological-structures]] of mycelia into a form suitable for network modeling, enabling quantitative analysis of transport efficiency, resilience to damage, and [[mycelial-foraging-resource-allocation]] strategies.

## From Mycelium to Graph

The starting assumption is that the fungal mycelium forms a (planar) spatial network that can be represented as a graph comprising a set of nodes (vertices, V) connected by links (edges, E). The translation process works as follows:

### Defining Nodes and Links
- **Cords** (the most convenient [[fungal-spatial-scale-biodiversity-hierarchical-zak-willig]]) serve as the primary structural elements, representing major [[the-apoplastic-symplastic-and-transcellular-transport-pathways]] through the mycelium
- **Branch points and junctions** are represented as nodes
- **Persistent cords** connecting junctions form the links
- **Tips** have a degree of 1 (connected to only one previous node)
- **Branch points** typically have a degree of 3, because growth processes usually produce a single branch or a single fusion (anastomosis) at each point
- **Food resources** (wood blocks, agar inocula) are each represented as a single node, since the fine mycelial structure within cannot be resolved at this scale

### Scale Considerations
The cord-based approach focuses on macro-scale transport architecture. While it captures the major transport pathways, it necessarily abstracts away the fine-scale hyphal network that performs the actual resource capture and metabolic processing. This is a deliberate trade-off: cord-level analysis reveals principles of network organization that are obscured at finer scales.

## Network Measures for Fungal Mycelia

### Basic Metrics

**Node degree (k)**: The number of links associated with any node. Tips (degree 1), branch points (typically degree 3), and resource nodes form the basic building blocks of the network.

**Network diameter**: The longest shortest path between any two nodes in the network — a measure of how "spread out" the mycelial network is.

**Total length**: The sum of all link lengths — reflecting the total material investment in the network.

**Mean shortest path**: The average of all shortest paths between pairs of nodes — indicating how efficiently any two points in the network can communicate.

### Connectivity Indices

**Clustering coefficient**: Measures the degree to which nodes tend to cluster together. In fungal networks, this reflects the tendency to form loops and redundant connections.

**Alpha index**: The ratio of actual circuits (loops) to the maximum possible circuits — measuring network connectivity and redundancy.

**Beta index**: The ratio of links to nodes — a simple measure of network complexity.

**Gamma index**: The ratio of actual links to the maximum possible links — another measure of connectivity density.

## Growth and Network Development

Time-lapse imaging of [[fungal-mycelial-networks-nutrient-translocation]] growing on compressed soil from wood-block inocula reveals dynamic network development:

1. **Initial phase (symmetrical growth)**: The colony expands uniformly with roughly equal growth in all directions. Transport and area increase are nearly symmetrical.

2. **Transition**: A shift from uniform to asymmetric growth, triggered by nutrient depletion in the inoculum or the discovery of new resources.

3. **Second phase (asymmetric, foraging growth)**: Growth becomes sparser and more directed toward new resources. Canalized flow patterns in cords emerge. Cord formation concentrates transport into defined pathways.

These growth phases can be described by two superimposed logistic equations, allowing normalization of data sets to a common developmental stage.

## Resource Allocation and Transport Dynamics

When a new resource (such as a wood block or filter paper) is encountered by the foraging margin:
- Local branching and proliferation increase near the resource
- Internal nitrogen allocation shifts to prioritize the new resource
- Growth becomes tightly focused on the resource location
- Transport through specific cords is enhanced (route-switching)

Not all cords transport simultaneously. Some cords act as transport routes only transiently — filling and then emptying as the network reconfigures its transport priorities. This dynamic rerouting suggests active control of resource distribution rather than passive diffusion.

## Pulsatile Transport

A striking feature of mycelial transport is its pulsatile nature. Rather than steady flow, nutrients move through corded systems in rhythmic pulses:

- Fourier analysis of 14C-AIB (a non-metabolized [[cho-fish-amino-acid-preparation]] analogue) transport reveals oscillations superimposed on net translocation
- Signals from assimilatory hyphae at the inoculum and from foraging hyphae oscillate but are out of phase with each other
- Phase differences become established as distinct domains that are locally synchronized
- The amplitude of pulsing centers can shift toward newly discovered resources
- Pulsatile behavior continues for extended periods (5–7 days observed in some experiments)

The functional significance of pulsatile transport may relate to:
- Enhanced mixing of nutrients within the network
- Coordination of growth and resource capture
- Signaling between different parts of the colony
- More efficient use of limited transport capacity

## Resilience to Damage

Graph theory provides tools for analyzing [[gadd-mycelial-network-resilience-grazing-pressure]] — the ability to maintain function despite damage. In fungal networks, this relates to:
