# Mathematical Modelling of Mycelial Form and Function

**Source:** Gadd, Watkinson & Dyer, *Fungi in the Environment*, Chapter 4
**Domain:** Mycology → [[bloomfield-mycorrhizal-symbiosis-and-fungal-ecology]] → Mathematical Biology

---

## Overview

Mathematical modelling of fungal mycelia complements experimental
approaches for understanding how [[environmental-sensing-filamentous-fungi-read]] grow, explore
resources, and function in [[fungal-mycelial-foraging-heterogeneous-environments]]. Fordyce A.
Davidson's chapter presents a hybrid continuum-discrete model connecting
hyphal-level physiology (tip growth, branching, anastomosis) to
mycelial-level properties (biomass distribution, [[dighton-fungal-nutrient-translocation-element-redistribution]],
colony form). The model was calibrated against [[rhizoctonia-solani]], a
ubiquitous soil-borne saprotroph.

The fundamental challenge is scale: fungi operate from micrometre-scale
[[aact-microbial-foliar-nutrient-uptake-co2-stomata-ingham]] to metre-scale resource translocation, and from seconds
(tip vesicle fusion) to weeks (colony expansion).

## Scale Choices in Fungal Modelling

Two broad modelling approaches exist, each suited to different scales:

**Continuum models**: Treat biomass as a density field using PDEs. Best for
dense growth in uniform conditions (Petri dishes). Individual hyphal
properties are averaged.

**Discrete models**: Track individual hyphae as computational objects.
Reproduce realistic branching and fractal morphology but used non-
mechanistic rules and neglected anastomosis and translocation.

Both approaches had significant limitations. Continuum models ignored
the fractal nature of [[fungal-mycelial-networks-nutrient-translocation]]. Discrete models neglected
anastomosis and translocation — processes crucial for growth in
[[modelling-mycelial-growth-heterogeneous-environments-davidson]] — due to computational constraints.

## The Hybrid Model

Davidson's innovation is a hybrid cellular automaton model that combines
the strengths of both approaches:

**Five state variables** tracked on a 2D grid:
1. Active hyphae (involved in metabolite translocation)
2. Inactive hyphae (moribund, not translocating)
3. Hyphal tips (growing points)
4. Internal substrate (nutrients within the fungus)
5. External substrate (nutrients in the environment)

**Key model equations:**

Change in active hyphae = new hyphae from moving tips + reactivation
of inactive hyphae − inactivation of active hyphae

Change in hyphal tips = tip movement + branching − anastomosis

Change in internal substrate = translocation (active + passive) +
uptake from environment − maintenance costs − growth costs −
translocation energy costs

Change in external substrate = diffusion − fungal uptake

The model explicitly includes both active (metabolically driven) and
passive (diffusive) translocation, and represents anastomosis (hyphal
fusion) as a tip-removal process.

## Growth Characteristics Modelled

**Tip extension**: Hyphal tips move in approximately straight lines with
small random fluctuations (due to wall incorporation patterns). Tip
growth rate depends on internal substrate concentration.

**Branching**: Modelled as proportional to internal substrate
concentration, reflecting the biological relationship between turgor
pressure, tip vesicle accumulation, and branch initiation.

**Anastomosis**: When a tip contacts an existing hypha, the tip is
absorbed into the hyphal network. This is a simplification of the
biological process of hyphal fusion but captures its population-level
effect on tip count.

**Nutrient uptake**: Depends on external substrate concentration,
internal substrate concentration (energy for [[diffusion-osmosis-and-active-transport-in-plants]]), and
hyphal surface area.

**Active translocation**: Moves internal substrate toward hyphal tips
(the major growth sinks) and depletes energy reserves. This is
distinguished from passive diffusion, which is energy-free.

## Practical Applications

The principles and techniques discussed here have wide-ranging applications
across multiple disciplines and contexts. Practitioners and researchers
continue to explore new ways to integrate these concepts into modern practice,
adapting traditional knowledge to contemporary challenges and opportunities.

## Key Considerations

Several important factors influence the effectiveness and outcomes described
in this topic. Understanding these considerations helps practitioners make
informed decisions and avoid common pitfalls. Environmental conditions,
timing, and material selection all play critical roles.

## Historical Context

The historical development of this subject reflects centuries of accumulated
knowledge and practical experience. From traditional methods passed down
through generations to modern scientific approaches, the evolution continues
to inform current best practices and research directions.

## Common Challenges

Practitioners frequently encounter several challenges when working with
these concepts. Climate variability, resource limitations, and knowledge
gaps can all affect outcomes. Addressing these challenges requires patience,
observation, and a willingness to adapt approaches based on results.

## See Also
- [[dom]]
- [[mycology]]
- [[mycorrhiza]]
- [[fungi-environment-mathematical-modelling-mycelial-growth]]
- [[gadd-mathematical-modelling-fungal-mycelia]]
