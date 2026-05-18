---
title: Fungal Mycelial Network Analysis
source: geoffrey-gadd-sarah-c-watkinson-paul-s-dyer-fungi-in-the-environment.md
type: concept
---

## Overview

Fungal mycelial network analysis applies graph theory and network science to the study of how saprotrophic and ectomycorrhizal fungi organize their filamentous growth into connected cord systems. By representing the physical structure of mycelial networks as mathematical graphs, researchers can quantify transport efficiency, resilience to disturbance, and the dynamic architectural strategies fungi use to colonize soil and decompose organic matter. This analytical framework has profound implications for understanding soil health, nutrient cycling, and the role of fungi in sustainable agricultural ecosystems.

## Representing Mycelia as Graphs

In graph-theoretic representations of fungal mycelia, the physical cord system of the fungus is abstracted into a network composed of **nodes** (vertices) and **links** (edges). Nodes typically represent junction points, branch tips, or discrete cord segments, while links represent the physical connections (cords or rhizomorphs) between them. This binary abstraction preserves the essential topology of the mycelial network while enabling quantitative analysis using well-established graph-theoretic measures.

The cord-forming habit is particularly well-developed in wood-decay basidiomycetes such as *Phanerochaete velutina*, which has served as a principal model organism for this type of analysis. The mycelium of *P. velutina* grows as an interconnected system of cords over the soil surface and through woody substrates, forming a network that can be readily digitized and subjected to network analysis.

## Key Network Measures

A suite of quantitative metrics drawn from graph theory is used to characterize the structure and function of mycelial networks:

### Degree Distribution

The **degree** of a node is the number of links connected to it. The degree distribution describes the frequency of nodes with different numbers of connections across the entire network. In mycelial networks, degree distribution reveals whether growth is dominated by a few highly connected hubs or is more evenly distributed, informing models of resource transport and vulnerability to targeted disruption.

### Diameter and Path Length

**Network diameter** is the longest shortest path between any two nodes in the graph, while **characteristic path length** is the average shortest path across all node pairs. Short path lengths indicate efficient transport — resources can move quickly between distant parts of the colony — which is ecologically critical for fungi that must reallocate carbon and minerals across their mycelial front.

### Clustering Coefficient

The **clustering coefficient** measures the degree to which nodes tend to cluster together, quantifying local interconnectedness. High clustering in mycelial networks suggests robust local transport redundancy, meaning that if one cord is severed, alternative pathways exist to maintain flow within a localized region. This property is directly relevant to a fungus's ability to withstand physical soil disturbance or grazing by soil invertebrates.

### Alpha, Beta, and Gamma Indices

These are landscape connectivity metrics adapted for mycelial network analysis:

- **Alpha index** measures circuit density — the ratio of actual circuits (loops) to the maximum possible number of circuits. Higher alpha values indicate greater redundancy and alternative routing capacity.
- **Beta index** is the ratio of total links to total nodes. Values greater than 1 indicate a connected network; higher values reflect greater complexity and interconnection.
- **Gamma index** compares the actual number of links to the maximum possible, providing a normalized measure of overall network connectivity (0 to 1).

Together, these indices provide a compact summary of network topology that can be compared across species, substrates, or experimental treatments.

## Model Reference Networks

To assess whether observed mycelial architectures are optimized or constrained, researchers compare real fungal networks against mathematical model networks that represent theoretical extremes:

### Delaunay Triangulation

A Delaunay triangulation connects all nodes such that no node falls inside the circumcircle of any triangle formed. It represents a **maximally connected** planar graph for the given node positions, serving as an upper bound for connectivity. If a mycelial network approaches Delaunay connectivity, it suggests the fungus is investing heavily in redundant link formation.

### Relative Neighbourhood Graph

The relative neighbourhood graph (RNG) connects two nodes only if no third node is closer to both than they are to each other. It produces a sparser network than Delaunay triangulation and represents a more selective connectivity pattern based on local spatial criteria.

### Minimum Spanning Tree

The **minimum spanning tree (MST)** is the least-cost connected subgraph linking all nodes — it contains no redundant paths or loops. It represents the absolute minimum of cord material required to keep the colony connected. Mycelial networks typically exceed MST connectivity but fall short of Delaunay triangulation, occupying an intermediate position that balances transport efficiency against construction cost.

Real fungal networks typically fall between the MST and Delaunay extremes, indicating an evolutionary trade-off between the metabolic cost of building and maintaining cords and the functional benefits of transport redundancy.

## Network Resilience Testing

Resilience — the capacity of a mycelial network to maintain function after disturbance — is tested experimentally through **simulated node removal**. In these assays, nodes are removed randomly (simulating non-selective disturbance such as trampling or frost heave) and the effects on network connectivity and transport are measured.

Key findings from resilience testing include:

- Mycelial networks with higher alpha indices (more loops and alternative paths) lose connectivity more slowly as nodes are removed.
- Networks exhibit a **threshold behavior**: connectivity remains largely intact until a critical proportion of nodes is removed, after which the network fragments rapidly.
- The spatial arrangement of removed nodes matters — removal concentrated in a single region is more disruptive than equivalent removal spread evenly across the colony.
- Species differences in resilience correlate with ecological strategy; cord-forming wood decomposers like *P. velutina* tend to build more resilient networks than diffuse, non-cord-forming species.

These resilience properties are directly relevant to soil management practices. Tillage, compaction, and soil fauna grazing all constitute network disturbance in agricultural soils, and understanding fungal resilience helps predict how decomposer communities recover.

## Spatial Constraints on Network Topology

Mycelial networks do not develop in abstract space — their topology is constrained by the physical environment. Key spatial constraints include:

- **Resource distribution**: Cords tend to grow toward and concentrate around nutrient-rich patches (wood fragments, organic matter), creating heterogeneous node density.
- **Physical obstacles**: Soil structure, stones, roots, and water-saturated zones channel or block cord growth.
- **Competition zones**: Encounter with other fungal colonies or plant roots can redirect growth and prune existing cords.
- **Substrate geometry**: The two-dimensional surface of the soil-litter interface constrains growth differently than the three-dimensional interior of decomposing wood.

These constraints mean that purely topological metrics must be interpreted alongside spatial context. A network with apparently low connectivity may simply be growing in a resource-poor region, while a highly connected network may reflect localized resource abundance rather than intrinsic architectural strategy.

## Network Evolution Dynamics

[[mycelial-network-architecture]] is not static — it evolves through four recognizable developmental phases:

### Proliferation

During **proliferation**, the fungus extends its mycelial front rapidly outward from the inoculum, exploring new territory. The network is relatively sparse, with long cords connecting newly established nodes. Growth priority is on coverage and resource discovery rather than efficiency.

### Selection

In the **selection** phase, some cords are maintained and strengthened while others are abandoned. The fungus preferentially retains connections that lead to profitable resource patches and prunes those that do not. This phase is driven by internal translocation of carbon and other resources, effectively "rewarding" productive pathways.

### Reinforcement

During **reinforcement**, retained cords thicken and may be bundled into larger, more robust structures. Transport capacity increases along these reinforced pathways, and the network becomes more resistant to mechanical disruption. Reinforcement is metabolically expensive and is directed only toward the most productive routes.

### Regression

In **regression**, peripheral regions of the colony are abandoned as resources are depleted and the colony redirects investment toward remaining resource hotspots. Cords in marginal zones senesce and are broken down, recycling their constituent materials. This phase represents a strategic contraction that conserves resources.

This developmental sequence — proliferation → selection → reinforcement → regression — reflects an economically rational foraging strategy analogous to optimal foraging theory in animal ecology. The fungus invests in exploration, evaluates returns, concentrates on winners, and cuts losses.

## Model Organism: Phanerochaete velutina

*Phanerochaete velutina* (syn. *P. velutina*) is a basidiomycete wood-decay fungus that has been extensively used as a model system for mycelial network analysis. It forms conspicuous cord systems on the surface of soil and wood, is readily culturable on defined media, and exhibits all four phases of network development within experimentally tractable time frames (typically 8–16 weeks). Its mycelial networks have been characterized across a wide range of experimental treatments including variable resource distribution, competition with other fungi, and simulated grazing disturbance. *P. velutina* occupies an intermediate position between efficient and resilient network architectures, making it a representative model for understanding how wood-decomposing fungi balance construction costs with functional performance.

## Ecological and Agricultural Significance

Understanding mycelial network architecture has direct relevance to farming and agriculture:

- **Soil structure formation**: Cord-forming fungi bind soil particles and create stable aggregates, improving water infiltration and erosion resistance. Networks with higher connectivity and reinforcement contribute more to soil physical stabilization.
- **Nutrient cycling**: The efficiency of decomposition and nutrient mineralization depends on the fungus's ability to translocate resources across its network. Well-connected networks cycle nutrients faster.
- **Disease suppression**: Resilient mycelial networks can compete more effectively with soil-borne plant pathogens for space and resources, contributing to natural disease suppression.
- **Composting optimization**: Knowledge of network development phases can inform composting management — maintaining conditions that favor the proliferation and reinforcement phases maximizes decomposition rates.
- **Tillage impact assessment**: Network resilience testing provides a quantitative basis for evaluating how different tillage practices affect soil fungal communities and the ecosystem services they provide.


## See Also
- Mycorrhizal Networks
- [[soil-fungal-ecology]]
- Wood Decomposition
- Graph Theory in Biology
- Saprotrophic Fungal Foraging
- [[mycelial-network-structure]]
- [[fungal-biology-fundamentals]]
- [[fungal-mycelial-networks-nutrient-translocation]]