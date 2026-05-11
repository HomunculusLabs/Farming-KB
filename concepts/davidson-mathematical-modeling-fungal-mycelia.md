---
title: Davidson Mathematical Modeling Fungal Mycelia
source: "geoffrey-gadd-sarah-c-watkinson-paul-s-dyer-fungi-in-the-environment.md"
source_author: "Fordyce A. Davidson"
source_book: "Fungi in the Environment"
published: 2007
tags: [fungal-modeling, mycelial-growth, mathematical-biology, diffusion, morphogenesis, foraging, tip-growth]
---

# Mathematical Modeling of Fungal Mycelia: Form and Function

## Overview

Fordyce Davidson's Berkeley Award Lecture chapter presents
mathematical modeling approaches for understanding [[fungal-mycelial-competition-and-combat-outcomes]]
growth, morphology, and function. The work addresses how physical
and biological constraints shape fungal form, and how mathematical
frameworks can predict mycelial behavior in response to environmental
variables. These models bridge empirical observation and mechanistic
understanding of fungal colony development.

## Why Model Fungal Mycelia?

Fungal mycelia present unique modeling challenges: they are
multiscale systems spanning molecular transport within individual
hyphae to colony-level networks covering meters of substrate. Growth
occurs at tips, yet colony-level behavior emerges from collective
activity of thousands of interacting hyphal tips operating under
local rules. Models help determine whether global coordination
mechanisms exist or whether colony behavior is purely emergent from
local hyphal interactions.

## Tip Growth Kinetics

The fundamental unit of fungal growth is the hyphal tip, extending
through targeted vesicle delivery of cell wall and membrane
components. Mathematical descriptions must account for:

- **Vesicle flux:** Rate of delivery to the apex, driving wall
  synthesis and membrane expansion
- **[[bloomfield-turgor-pressure-and-hyphal-invasion]]:** Hydrostatic pressure providing driving
  force for extension
- **Wall yielding:** Mechanical properties determining how
  pressure translates into extension
- **Spitzenkorper dynamics:** The [[gadd-spitzenkorper-vesicle-supply-centre-hyphal-tip-growth-direction]] center
  orchestrating polarized growth

Models typically use [[continuum-mechanics]], treating the hyphal apex
as a viscoelastic shell under internal pressure, with wall synthesis
rates depending on local stress and strain conditions. The
Spitzenkorper acts as a organizing center that maintains growth
polarity by concentrating vesicle delivery at the extreme apex.

## Nutrient Uptake and Translocation Models

**Microscale (within hyphae):** Vacuolar diffusion models based on
FRAP (fluorescence recovery after photobleaching) measurements provide
quantitative parameters for intracellular transport. Cytoplasmic
streaming is modeled as advection, and vesicular transport as
discrete cargo movement along cytoskeletal tracks.

**Mesoscale (colony-level):** Diffusion-limited aggregation models
capture colony morphology; reaction-diffusion equations describe
nutrient gradients around growing colonies; lattice-based models
represent branching patterns with probabilistic rules.

**Macroscale (network-level):** Graph-theoretic models of cord
[[mycelial-network-architecture]] enable quantitative comparison of foraging
strategies; network flow models describe translocation routing;
optimization models evaluate foraging efficiency tradeoffs.

## Branching Patterns and Colony Morphology

[[hyphal-branching-regulation-nutrient-sensing-gadd]] is regulated by internal and external cues captured
through deterministic rules (based on tip age, extension rate,
[[leaf-tissue-analysis-crop-nutrient-status]]), stochastic branching (probabilistic, triggered
by environmental variation), and lateral branching frequency
(related to nutrient gradients). The balance between extension and
branching determines colony form — from compact spherical colonies
to diffuse, exploration-oriented networks.

## Foraging Strategy Optimization

[[brassinosteroid-effects-on-fungal-morphology]] represents an evolutionary tradeoff between:
(1) resource capture efficiency — maximizing contact with nutrient
patches in [[fungal-mycelial-foraging-heterogeneous-environments]]; (2) transport economy —
minimizing metabolic cost of maintaining biomass; (3) damage
resilience — maintaining connectivity after disturbance; (4)
exploration vs. exploitation — balancing widespread searching with
focused utilization. Different species optimize these differently:
