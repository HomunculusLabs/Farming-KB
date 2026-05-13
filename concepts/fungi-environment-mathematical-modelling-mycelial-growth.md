# Mathematical Modelling of Fungal Mycelial Growth

**Source:** Fungi in the Environment — Gadd, Watkinson & Dyer (2007), Ch. 4

## Core Concept

Mathematical modelling provides a powerful complementary approach to
experimental study of fungal growth, allowing researchers to isolate and
investigate key properties of mycelial systems that are difficult to study
through experiments alone. The challenge is finding the right balance between
simplicity and biological realism — as Einstein said, "everything should be
made as simple as possible, but no simpler." Modern fungal growth models
connect physiology at the hyphal level (tip growth, branching) to function
at the mycelial level (biomass distribution, [[gadd-mathematical-modelling-rhizoctonia-solani-mycelial-growth]] but is applicable to a broad class of fungi.

### Five State Variables
The model tracks five interacting components at each point in space:
1. **Active hyphae** — hyphae involved in translocation of internal
   metabolites
2. **Inactive hyphae** — hyphae no longer involved in translocation or
   growth (moribund or senescent)
3. **Hyphal tips** — the growing fronts that extend the colony
4. **Internal substrate** — nutrients within the fungal biomass
5. **External substrate** — nutrients in the environment

### Key Assumptions
- A single generic element (carbon) is assumed to be growth-limiting,
  given its central role and the relative abundance of nitrogen and oxygen
- Internal substrate is used for tip extension, branching, maintenance,
  and uptake of external resources
- Hyphae can transition between active and inactive states

### Model Structure
The rate of change in active hyphae equals new hyphae laid down by moving
tips, plus reactivation of inactive hyphae, minus inactivation of active
hyphae. Similarly, inactive hyphae increase through inactivation and
decrease through reactivation and degradation. These coupled differential
equations produce emergent colony-level patterns from individual hyphal
behaviors.

## Continuum vs. Discrete Approaches

### Continuum Formulation
Treats the mycelium as a continuous field of biomass density, modelled
using nonlinear partial differential equations describing the interaction
between fungal biomass and growth-limiting substrate. Ideal for dense
mycelia on uniform surfaces. Allows study of:
- Biomass distribution in homogeneous and heterogeneous conditions
- Translocation in various habitat configurations
- Functional consequences like acid production

### Discrete (Hybrid Cellular Automaton) Formulation
Represents individual hyphae as discrete structures in a continuous
substrate field. This approach explicitly includes anastomosis (hyphal
fusion) and translocation, which were neglected in earlier discrete models
due to computational limitations. More appropriate for sparse growth in
nutrient-poor or structurally [[gadd-fungal-imaging-techniques]] provide validation data, multi-scale models will become
increasingly predictive and biologically realistic.

## Translocation and Resource Bridging

A key finding from modelling is that hyphal translocation allows fungi to
grow through nutritionally impoverished or hostile zones by importing
resources from distant, resource-rich regions of the mycelium. This has
profound implications:
- Fungi can bridge air gaps, dry zones, and contaminated patches in soil
- Species with efficient translocation can dominate heterogeneous habitats
- The fungal mycelium functions as an integrated resource distribution
  network, not merely a collection of independent foraging hyphae

## Limitations and Challenges

Many discrete models use ad hoc rules for tip extension and branching that
are not derived from underlying biology, limiting predictive power across
species. Computational complexity is another barrier: explicit modelling of
anastomosis and translocation is expensive at soil-relevant spatial scales.
Validation against experimental data remains challenging, though PCSI
imaging provides suitable spatio-temporal data for transport predictions.

## Applications

- **Soil ecology**: Predicting [[fungal-contributions-soil-structure]] to nutrient fluxes

## See Also

- [[fungi-in-the-environment-symbiotic-relationships]]
