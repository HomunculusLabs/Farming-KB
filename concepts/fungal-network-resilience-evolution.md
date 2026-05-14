---
title: Fungal Mycelial Network Resilience and Evolution
source: geoffrey-gadd-sarah-c-watkinson-paul-s-dyer-fungi-in-the-environment.md
type: concept
---

# Fungal Mycelial Network Resilience and Evolution

## Overview

Cord-forming saprotrophic basidiomycetes build extensive [[mycelial-networks]] that function as both foraging structures and transport systems. These networks are not static—they evolve dynamically through three distinct developmental phases and must maintain function despite damage from grazing invertebrates, physical disruption, and environmental stress. Research on *[[phanerochaete-velutina]]* has revealed that fungal networks balance efficient transport against resilience, using architectural strategies that differ markedly from random or engineered networks.

## Three-Phase Network Development

### Phase 1: Proliferation

When a fungal colony first establishes itself, growth proceeds through an initial **proliferation phase** in which many cords are formed rapidly. Fine foraging hyphae extend in multiple directions, exploring the substrate for new resources. During this phase, the network is dense and highly branched, with many redundant pathways. The colony grows symmetrically, distributing resources evenly across sectors.

### Phase 2: Selection and Reinforcement

Upon contact with a new resource (such as a wood block), the colony transitions to a second phase characterised by **selection and reinforcement**. A subset of cords connecting the inoculum to the new resource is preferentially strengthened through increased cytoplasmic flow and cord thickening. Simultaneously, the colony shifts from symmetric to **asymmetric growth**, directing growth and nutrient allocation tightly towards the newly discovered resource. Canalised flow patterns emerge within cords, reflecting the establishment of preferential transport routes.

### Phase 3: Regression

In the final phase, the remaining unselected cords **regress**, leaving a sparser network consisting primarily of reinforced pathways between resources. Fine foraging hyphae recede from areas that proved unproductive. The history of previous connections is preserved as a series of **degree-2 nodes** left on the main connecting cords—nodes that once represented branch points but where the subsidiary branches have been reabsorbed. After excluding these remnant nodes, the average degree of remaining nodes stabilises at approximately 3.5.

## In Silico Resilience Assessment

### Methodology

Network resilience is evaluated using computational removal simulations:

1. The corded mycelial network is translated into a **graph representation** with nodes (branch points, junctions, resource sites) and links (persistent cords).
2. Individual nodes or links are removed at random to simulate accidental damage or grazing.
3. The **network integrity** is measured as the fraction of remaining nodes still connected to the initial inoculum after each removal step.
4. This process is repeated for multiple random removal sequences, and the average connectivity decline is plotted.

### Comparison with Model Networks

The same removal protocol is applied to reference networks constructed using well-defined algorithms:

| Model Network | Connectivity | Expected Resilience |
|---|---|---|
| **Delaunay Triangulation (DT)** | Highly connected, many redundant links | Very high |
| **Relative Neighbourhood Graph (RNG)** | Intermediate connectivity | Moderate–high |
| **Minimum Spanning Tree (MST)** | No redundant links, tree structure | Low |
| **Fungal Network** | Intermediate, between RNG and DT | Moderate–high |

The fungal network consistently outperforms the minimum spanning tree, indicating meaningful redundancy, but does not reach the connectivity of a Delaunay triangulation, reflecting the metabolic cost of building and maintaining each additional cord.

### Spatial Constraints on Resilience

Unlike abstract graph-theoretic networks, fungal mycelia are **planar spatial networks** where:

- Links cannot cross without forming a new node (anastomosis point).
- Nodes can only connect to physically proximate neighbours.
- The probability of connection decreases steeply with distance.

These spatial constraints mean that fungal networks cannot create topological "shortcuts" between physically remote parts of the colony, limiting the architectural strategies available for resilience compared to non-spatial networks.

## Biological Damage and Rewiring

### Non-Random Damage Patterns

In natural environments, damage to mycelial networks is not random. Soil invertebrates such as Collembola graze preferentially on certain regions of the mycelium, with palatability varying across the network. This creates **correlated, spatially clustered damage** rather than the uniform random removal modelled in initial simulations. Such clustered damage may be more disruptive than random removal because it can sever multiple links in a localised area simultaneously.

### Self-Organising Rewiring

A critical advantage of biological over engineered or random networks is the capacity for **active rewiring**:

- After damage, the mycelium can regrow and reconnect severed pathways through continued hyphal extension and anastomosis (hyphal fusion).
- The spatial, self-organising nature of the network means that reconnection occurs along physically efficient routes guided by substrate gradients and resource locations.
- Rewiring is metabolically costly but can be targeted precisely where needed, unlike random networks where reconnection would require building entirely new connections without spatial guidance.

### Implications

The resilience of fungal mycelial networks depends on two factors operating at different timescales:

1. **Architectural resilience**: The pre-existing network structure provides immediate redundancy that maintains partial connectivity after damage.
2. **Dynamic resilience**: The capacity for regrowth and reconnection restores full network function over time.

This dual resilience strategy—structural redundancy plus active repair—may represent an optimal balance between the metabolic cost of maintaining excess cords and the cost of complete regrowth after catastrophic damage.

## Network Architecture and Metabolic Cost

The evolution of network architecture reflects a trade-off between competing pressures:

- **Efficient transport**: Fewer, thicker cords provide faster, lower-resistance transport between resources.
- **Resource capture**: Dense foraging frontiers maximise the probability of encountering new resources.
- **Damage tolerance**: Redundant pathways ensure continued function if primary routes are severed.
- **Metabolic economy**: Each cord requires resources to build and maintain, creating pressure to minimise unnecessary connections.

The observed three-phase development—proliferation, selection, regression—optimises this trade-off by initially investing in extensive exploration, then concentrating resources on proven productive routes while discarding unproductive ones.

## See Also

- [[fungal-mycelial-network-graph-theory]] — Graph-theoretic analysis of mycelial network topology
- [[pulsatile-nutrient-transport-fungal-mycelia]] — Oscillatory solute transport through corded networks
- [[vacuolar-diffusion-fungal-transport]] — Intracellular vacuolar pathways for longitudinal transport
