---
title: "gadd-mycelial-network-dynamics Graph Theory Analysis — Modeling Fungal Foraging Networks"
source: "Fungi in the Environment (Gadd, Watkinson, Dyer)"
topics: [fungi, mycelium, network-theory, graph-theory, foraging, nutrient-transport, cords, resilience]
---

# Mycelial Network Graph Theory Analysis

## Overview

Fungal mycelia form complex, spatially extended networks that can be analyzed using graph theory — the mathematical study of networks represented as nodes connected by links. This approach, pioneered by researchers studying cord-forming basidiomycetes, translates the morphological structures of mycelia into a form suitable for network modeling, enabling quantitative analysis of transport efficiency, resilience to damage, and resource allocation strategies.

## From Mycelium to Graph

The starting assumption is that the fungal mycelium forms a (planar) spatial network that can be represented as a graph comprising a set of nodes (vertices, V) connected by links (edges, E). The translation process works as follows:

### Defining Nodes and Links
- **Cords** (the most convenient spatial scale) serve as the primary structural elements, representing major transport pathways through the mycelium
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

Graph theory provides tools for analyzing network resilience — the ability to maintain function despite damage. In fungal networks, this relates to:
- **Random link removal**: Simulating damage to individual cords
- **Random node removal**: Simulating the loss of junction points or resources
- **Targeted attacks**: Removing the most connected nodes (highest degree)

Fungal networks typically show greater resilience than purely random or regular networks because of their intermediate connectivity — enough redundancy to survive partial damage, but not so much connectivity that the cost becomes prohibitive.

## Comparison with Mathematical Network Models

Researchers have compared fungal networks against three mathematical models generated with the same node positioning:
1. **Delaunay triangulation (DT)**: Maximally connected network
2. **Relative neighborhood graph (RNG)**: Intermediate connectivity
3. **Minimum spanning tree (MST)**: Minimal connectivity (no redundancy)

Fungal networks fall between these extremes, suggesting they optimize the trade-off between transport efficiency (favors more connections) and material cost (favors fewer connections). This balance reflects the fundamental biological constraint: building and maintaining mycelial connections has metabolic costs that must be justified by improved resource capture.

## Ecological Implications

Different fungal species exhibit different [[mycelial-foraging-strategies-nutrient-translocation]] that represent different points on the efficiency-vs-resilience spectrum:
- **Phanerochaete velutina**: A cord-forming saprotroph that invests heavily in persistent transport networks, enabling rapid reallocation of nutrients across large distances
- Species with less developed cord systems may sacrifice long-range transport efficiency for lower material investment
- The choice of strategy likely reflects adaptation to specific environmental conditions — resource [[guzman-global-distribution-patterns-neurotropic-fungi]], disturbance frequency, competition intensity

## Key Research References

- Bebber, D.P. et al. (2006). Imaging [[gadd-mycelial-nutrient-translocation-imaging]] dynamics. In Fungi in the Environment, pp. 3–21. Cambridge University Press.
- Tlalka, M. et al. (2002). Continuous imaging of amino acid translocation in intact mycelia of Phanerochaete velutina reveals rapid, pulsatile fluxes. New Phytologist 153, 173–84.
- Tlalka, M. et al. (2003). Noncircadian oscillations in amino acid transport have complementary profiles in assimilatory and foraging hyphae. New Phytologist 158, 325–35.
- Albert, R. & Barabási, A.L. (2001). Statistical mechanics of complex networks. Reviews of Modern Physics.

## See Also

- [[fungal-vacuolar-system-nutrient-translocation]]
- [[woronin-bodies-septal-pore-plugging-fungal-hypha]]
- [[mycorrhizal-networks-common-mycelial-network]]
- [[fungi-in-the-environment-decomposition-wood-decay]]
