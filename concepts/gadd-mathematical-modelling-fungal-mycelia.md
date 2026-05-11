---
title: Gadd Mathematical Modelling Fungal Mycelia
created: 2026-04-28
tags:
  - mathematical-modelling
  - mycelial-growth
  - fungal-ecology
  - systems-biology
  - rhizoctonia-solani
date: 2026-04-28
updated: 2026-04-28
sources:
  - /Users/t3rpz/wiki/raw/papers/geoffrey-gadd-sarah-c-watkinson-paul-s-dyer-fungi-in-the-environment.md
type: concept
---

# Mathematical Modelling of Fungal Mycelial Form and Function

Mathematical modelling of [[brassinosteroid-fungal-growth-promotion]] and function aims to reduce
complex biological systems to simpler mathematical representations where
rigorous logical structures can isolate, identify, and investigate key
properties. As Einstein noted, 'everything should be made as simple as
possible, but no simpler.' The art lies in achieving a meaningful balance
between simplification and biological fidelity.

## Historical context and scale challenges

Mathematical modelling of fungal growth has been conducted for several
decades. One of the main problems facing modellers is the choice of
scale. Biological questions must first be identified, then matched to
the scale at which they are most likely to be expressed. The ultimate
goal is multi-scale models that transfer information from individual
genes through to the growth and function of large-scale mycelia. Until
recently, modelling efforts either focused on the mycelium using
variables such as biomass yield, or focused on hyphal-level growth such
as tip extension, branching, and anastomosis. In the former, spatial
properties were generally ignored; in the latter, temporal effects were
often neglected.

## Continuum models for dense mycelia

Large-scale, spatio-temporal properties of fungal mycelia have been
addressed by deriving systems of nonlinear partial differential equations
that represent the interaction of [[bioremediation-fungal-biomass-biosorbent-material]] and a growth-limiting
substrate. This approach is ideal for modelling dense mycelia growing on
Petri dishes, foodstuffs, plant surfaces, and [[natural-building-materials-guide]]. The
strategy has allowed study of biomass distribution within mycelia in
homogeneous and heterogeneous conditions, translocation in various
habitat configurations, and functional consequences such as acid
production.

## Discrete models for sparse growth

When growth is sparse, as in nutrient-poor conditions or structurally
[[modelling-mycelial-growth-heterogeneous-environments-davidson]] such as soils, continuum approaches are less
relevant. Discrete modelling is more appropriate, where individual
hyphae are identified. Such models usually take the form of computer
simulations and are often derived from statistical properties of
experimental systems. Although these models can yield images almost
indistinguishable from real fungi, they often employ non-mechanistic
rules and must be re-formulated for different environments or species.
Computational difficulties have also meant that discrete models have
neglected anastomosis and translocation, processes crucial in
heterogeneous environments.

## A new hybrid model

A recent development by Boswell et al. connects physiology at the
hyphal level to growth at the mycelial level. The mycelium is modelled
as a distribution consisting of three components: active hyphae
(involved in translocation of internal metabolites), inactive hyphae
(not involved in translocation or growth), and hyphal tips. The model
distinguishes between nutrients within the fungus (internal) and those
free in the environment (external), with a single generic limiting
element assumed to be carbon.

## Model structure and equations

The model tracks five coupled variables across five equations:
(1) active hyphae change via new hyphal deposition, reactivation, and
    inactivation;
(2) inactive hyphae change via inactivation, reactivation, and
    degradation;
(3) hyphal tips change via movement, branching from active hyphae, and
    anastomosis;
(4) internal substrate changes via translocation, uptake, maintenance
    costs, growth costs, and active translocation costs;
(5) external substrate changes via diffusion and fungal uptake.

## Key biological features captured
