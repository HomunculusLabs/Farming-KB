# Mycelial Cord Network Topology and Graph Theory Analysis

## Overview
Fungal mycelial [[mycelial-network-graph-theory-analysis]] networks — particularly those formed by cord-forming basidiomycetes
such as *Phanerochaete velutina* — can be analyzed using tools from graph [[mycelial-network-graph-theory-analysis]] theory,
the same mathematical framework used to study ecological food webs, metabolic
networks, and genetic networks. This approach translates the morphological structures
of fungal networks into a form appropriate for network modeling, enabling quantitative
analysis of their architecture, efficiency, and resilience.

## From Mycelium to Graph
The fundamental assumption is that the fungal mycelium forms a planar spatial
network that can be represented as a graph comprising a set of nodes (or vertices, V)
connected by links (or edges, E).

### Constructing the Network Graph
The translation from biological structure to mathematical graph follows these steps:
1. **Identify cords**: Mycelial cords are the most convenient spatial scale for
   analysis, as they are readily identifiable discrete structures representing
   the major transport pathways.
2. **Define nodes**: Each branch point or junction (anastomosis) is represented
   as a node.
3. **Define links**: The persistent cords connecting nodes form the links.
4. **Represent resources**: Each food resource (agar plate or wood block) is
   represented as a single hub node with many links.

### Node Degree
The number of links associated with any node is termed its degree (k):
- **Tips** have a degree of 1 (connected to only the previous node)
- **Branch points** typically have degree 3 (single branch or fusion at each point)
- **Resource nodes** have high degree, resembling hubs in other network systems
- Loops where a link curls back to the same node are unlikely in 2-D planar networks

## Network Metrics
A range of quantitative measures characterize fungal network properties:

### Path-Based Measures
1. **Minimum path length**: The shortest path that must be traversed between any
   two nodes. Shorter average path lengths indicate more efficient transport.
2. **Network diameter**: The maximum distance between any two nodes, measured in
   both physical distance and number of nodes traversed.

### Degree Distribution
The frequency of nodes with different numbers of links. In fungal networks, the
degree distribution reveals the balance between exploration (many tips of degree 1)
and connectivity (branch points and fusions of higher degree).

### Topological Indices (from Physical Geography)
Three indices derived from physical geography describe natural and artificial
networks:

1. **Alpha index (α)**: Ratio of actual number of closed paths (cycles) to the
   maximum possible number. Higher values indicate greater connectivity and
   redundancy.
2. **Beta index (β)**: Ratio of actual number of links to number of nodes. Values
   greater than 1 indicate a connected network; higher values suggest greater
   connectivity.
3. **Gamma index (γ)**: Ratio of actual number of links to maximum possible number
   of links. Provides a normalized measure of connectivity (0 to 1).

### Clustering Coefficient
The local clustering or transitivity measures the probability that if a node is
connected to two other nodes, they will also be connected to each other. High
clustering indicates local redundancy — if one link fails, alternative paths exist
nearby.

## Network Evolution Over Time
The network architecture of *P. velutina* is not static but continuously evolves
through three distinct phases:

### Phase 1: Proliferation
During initial growth from inoculum toward a new food source, many links form
rapidly. The network is dense and exploratory, with high connectivity but
relatively low transport efficiency.

### Phase 2: Selection and Reinforcement
A subset of paths is selected and reinforced to create a smaller number of strong,
thick cords. This pruning process concentrates resources into the most efficient
transport routes.

### Phase 3: Regression
The remainder of the links from Phase 1 regress and are reabsorbed, leaving a
sparser but more efficient network. The result is a streamlined transport system
connecting resources.

## Resilience Testing
Network resilience estimates the extent to which network properties change as
nodes or links are removed. This simulates damage from grazing, physical
disturbance, or resource depletion.

### Methodology
1. Randomly remove nodes (up to 120 in experimental networks).
2. Measure the fraction of remaining nodes still connected to the initial inoculum.
3. Compare resilience to model networks (Delaunay triangulation, relative
   neighbourhood graph, minimum spanning tree).

### Findings
- Fungal networks show intermediate resilience — more robust than minimum
  spanning trees but less than fully connected Delaunay triangulations.
- The three-phase development process (proliferation → selection → regression)
  produces networks that balance transport efficiency with damage tolerance.
- The spatial constraints of planar networks limit the ability to create "short
  cuts" between physically remote parts of the network.

## Spatial Constraints
Most network analysis has focused on topology rather than spatial relations. However,
fungal networks are inherently spatial, and this imposes constraints:
- Nodes have much higher probability of connecting to physical neighbors.
- In 2-D planar networks, links cannot cross without forming a new node.
- This makes it difficult to create topological equivalents to "short cuts" between
  physically remote network regions.
- Weighting links by transport speed and capacity may have an equivalent effect to
  long-range communication, bringing distant parts of the network into closer
  effective contact.

## Network Size
In *P. velutina* grown in a 24 cm square microcosm:
- Corded networks comprise approximately 300-500 main nodes.
- Including the finest discernible hyphae increases the count to approximately
  3,000 nodes.
- Links are considered bidirectional since the physiological direction of nutrient
  flux varies depending on source-sink relations and cannot be predicted a priori.

## Implications
Graph-theoretic analysis of fungal networks reveals that fungi construct
transport systems with remarkably sophisticated engineering:
- **Efficiency**: Short path lengths and high clustering enable rapid resource
  distribution.
- **Resilience**: Multiple redundant pathways ensure function despite damage.
- **Adaptability**: Dynamic reconfiguration allows response to changing resource
  availability.
- **Economy**: The three-phase development process minimizes biomass investment
  while maximizing functional connectivity.

## Source
- Bebber, D.P. et al. "Imaging mycelial nutrient dynamics." In Gadd, G.M.,
  Watkinson, S.C. & Dyer, P.S. (eds.) *Fungi in the Environment*. Cambridge
  University Press. Lines 1320-1500 of the full text.

## See Also
- [[pcsi-scintillation-imaging-mycelial-nutrient-transport-bebber]]
- [[gadd-mycelial-network-resilience-graph-theory]]
- [[fungal-mycelial-networks-nutrient-translocation]]
- [[mycelial-foraging-strategy-resource-capture]]
