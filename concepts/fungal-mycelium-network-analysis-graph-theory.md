---
title: Fungal Mycelium Network Analysis Using Graph Theory
source: geoffrey-gadd-sarah-c-watkinson-paul-s-dyer-fungi-in-the-environment.md
type: concept
---

# Fungal Mycelium Network Analysis Using Graph Theory

## Overview

Fungal mycelia form complex, interconnected networks that can be analysed using tools from **graph theory** and **network science**. By representing the morphological structures of a fungal mycelium as a mathematical graph comprising nodes (vertices) connected by links (edges), researchers can quantify network properties such as connectivity, efficiency, resilience, and transport capacity. This approach, pioneered in studies of *[[phanerochaete-velutina]]*, has revealed that fungal networks share organizational principles with other biological and engineered networked systems.

## From Mycelium to Graph

The fundamental assumption is that the fungal mycelium forms a **planar spatial network** that can be represented as a graph. The translation from biological structure to mathematical model proceeds as follows:

### Nodes (Vertices, V)
- **Branch points:** Where a hypha or cord splits into two or more branches
- **Anastomoses (fusions):** Where two hyphae or cords fuse together
- **Tips:** The growing ends of cords (degree 1)
- **Resource nodes:** Food resources (agar or wood blocks) are represented as nodes with many links, resembling hubs

### Links (Edges, E)
- **Persistent cords:** The thick-walled, differentiated hyphae that serve as major transport pathways
- Each cord connecting two nodes forms a link in the graph

### Node Degree
The **degree (k)** of a node is the number of links associated with it:
- Tips have degree 1 (connected to only the previous node)
- Branch points typically have degree 3 (growth processes tend to give a single branch or a single fusion at each point)
- Resource nodes have high degree (hub-like)
- Degree-2 nodes (simple transit points along a cord) can be removed to simplify analysis

## Network Parameters

A comprehensive set of parameters is measured to characterize fungal networks:

### Path-Based Measures
- **Minimum path length:** The shortest path (in number of links or physical distance) between two nodes
- **Network diameter:** The maximum path length across the network, measured in both physical distance and number of nodes traversed
- **Mean shortest path:** The average minimum path length between all pairs of connected nodes

### Topological Measures
- **Degree distribution:** The frequency of nodes with different numbers of links, revealing whether the network follows a particular organizational pattern (e.g., scale-free, random)
- **Clustering coefficient (transitivity):** The probability that if a node is connected to two other nodes, those two nodes are also connected to each other. High clustering indicates local redundancy and alternative pathways.

### Connectivity Indices (from Physical Geography)
Three standard indices describe network connectivity:
- **Alpha index:** The ratio of actual closed paths (cycles) to the maximum possible number of closed paths
- **Beta index:** The ratio of actual links to the number of nodes (L/V). Values below 1 indicate a tree-like network; values above 1 indicate redundant connectivity
- **Gamma index:** The ratio of actual links to the maximum possible number of links

### Total Length
The sum of all link lengths, representing the total material investment in the transport network.

## Network Development Over Time

The network architecture of *P. velutina* is not static but evolves through three distinct phases:

### Phase 1: Proliferation
- Initial rapid growth from the inoculum
- Many links form as the mycelium explores the environment
- Considerable fine foraging hyphae that may not be clearly resolvable
- High connectivity but many weak, transient connections

### Phase 2: Selection and Reinforcement
- Contact with a new food resource triggers increased branching
- A subset of paths is selected and reinforced to create stronger, more limited connections
- More obvious cords develop
- Fine mycelium begins to recede

### Phase 3: Regression and Simplification
- The number of interconnected cords reduces further
- The network becomes sparser and more efficient
- The history of previous connections remains as degree-2 nodes along main connecting cords
- Average node degree stabilizes at approximately 3.5 (excluding degree-2 transit nodes)

## Comparison with Model Networks

To evaluate the properties of real fungal networks, they are compared against theoretical model networks constructed from the same node positions using different algorithms:

### Delaunay Triangulation (DT)
- **Highly connected** network where every possible connection that does not cross existing links is made
- Represents the maximum possible connectivity given the spatial constraints
- Serves as an upper bound for connectivity measures

### Relative Neighbourhood Graph (RNG)
- **Intermediate connectivity** -- a link exists only if no other node is closer to both endpoints than they are to each other
- Represents a moderate level of connectivity

### Minimum Spanning Tree (MST)
- **Minimally connected** -- the minimum set of links needed to connect all nodes with no cycles
- Represents the most economical network in terms of total length
- Serves as a lower bound for connectivity

Real fungal networks typically fall between the RNG and MST, suggesting they balance transport efficiency against resilience.

## Resilience Analysis

Network resilience estimates the extent to which network properties change as nodes or links are removed, simulating damage from grazing, physical disturbance, or predation. The analysis is performed **in silico** by progressively removing nodes (typically around 120 in experimental illustrations) and measuring the fraction of remaining nodes still connected to the initial inoculum.

### Key Findings
- Fungal networks show **greater resilience** than random networks or MST-type networks
- The resilience approaches that of DT-type networks in some respects
- In real [[fungal-mycelial-networks-nutrient-translocation]], damage is unlikely to be random -- grazing by soil invertebrates occurs preferentially in specific locations where hyphae are more palatable
- A self-organizing spatial network may have considerable advantages in the **cost, consistency, and efficacy of the rewiring process** needed to re-establish a functioning system after damage

## Spatial Constraints

Fungal networks are **spatial networks**, meaning the physical locations of nodes constrain which connections are possible:
- Nodes have a much higher probability of connecting to physical neighbours
- In planar (2D) networks, links cannot cross without forming a new node, making topological "short cuts" between remote parts of the network impossible
- However, weighting links by transport speed and/or capacity may effectively bring distant parts of the network into closer communication than expected from their spatial separation or unweighted path length

## Directed vs. Undirected Networks

While links could theoretically be directed based on their initial growth direction, in practice:
- The physiological direction of nutrient fluxes is more important and does not follow developmental connection sequences
- Flux direction varies depending on source-sink relations within the network
- Without direct flux mapping, it is simpler to assume links are **bidirectional**

## Network Scale

In *P. velutina* grown in a 24 cm square microcosm:
- **Cord-level network:** approximately 300-500 main nodes
- **Including finest discernible hyphae:** approximately 3,000 nodes

## Broader Context

The application of graph theory to fungal networks connects mycology to the broader field of **complex network science**, which has successfully analysed ecological food webs, metabolic networks, genetic regulatory networks, neural networks, and infrastructure networks. Fungal mycelia represent a particularly interesting case because they are **living, adaptive, spatially embedded networks** that continuously remodel themselves in response to environmental conditions.

## References

- Albert, R. and Barabasi, A.-L. (2001). Statistical mechanics of complex networks. *Reviews of Modern Physics* 74, 47-97.
- Strogatz, S. H. (2001). Exploring complex networks. *Nature* 410, 268-76.
- Newman, M. E. J. (2003). The structure and function of complex networks. *SIAM Review* 45, 167-256.
- Dorogovtsev, S. N. and Mendes, J. F. F. (2002). Evolution of networks. *Advances in Physics* 51, 1079-87.
- Amaral, L. A. N. and Ottino, J. M. (2004). Complex networks: augmenting the framework for the study of complex systems. *European Physical Journal B* 38, 147-62.

## See Also

- [[mycelial-network-structure]]
- [[fungal-biology-fundamentals]]
- [[fungal-mycelial-networks-nutrient-translocation]]
