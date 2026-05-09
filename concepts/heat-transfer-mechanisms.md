---
title: Heat Transfer Mechanisms
created: 2026-04-28
tags: [physics, thermodynamics, engineering, heat-transfer]
date: 2026-05-02
updated: 2026-05-02
sources:
  sources: []
type: concept
---

## Overview

Heat transfer is the transport of [[phase-change-materials-thermal-energy-storage]] from regions of
higher temperature to regions of lower temperature, driven by
temperature gradients. It is governed by three fundamental
mechanisms: conduction, convection, and radiation. Understanding
these mechanisms is essential for designing thermal systems
including heat exchangers, building insulation, electronic
cooling, power generation equipment, and refrigeration cycles.
Each mechanism operates through distinct physical principles and
dominates in different practical scenarios.

## Conduction

Conduction transfers thermal energy through a stationary medium
via molecular interactions without bulk motion. In gases and
liquids, conduction occurs through random molecular collisions
where higher-energy molecules transfer kinetic energy to
neighbors. In solids, particularly metals, conduction proceeds
through lattice vibrations called phonons and through free
electron drift, explaining why metals are superior conductors.
Fourier's law states that conductive heat flux equals negative k
times dT/dx, where k is thermal conductivity. This property
ranges from roughly 0.02 W/m-K for insulating foams to over 400
W/m-K for pure copper. Conduction dominates in solids and in the
thin stagnant fluid layers adjacent to surfaces.

## Convection

Convection combines molecular conduction with bulk fluid motion.
It subdivides into natural convection, driven by buoyancy from
density differences in heated fluid, and forced convection,
driven by pumps, fans, or blowers. Newton's law of cooling gives
the governing equation: q equals h times A times delta-T, where h
is the convective heat transfer coefficient and A is the surface
area. The coefficient h depends on fluid properties, geometry,
velocity, and flow regime characterized by the and flow regimes.
Typical values range from 5 to 25 W/m^2-K for natural air
convection, 25 to 250 for forced air, 50 to 10,000 for forced
water, and 2,500 to 250,000 for boiling or condensation.
Dimensionless Nusselt number correlations predict h for specific
configurations.

## Radiation

Thermal radiation is electromagnetic energy emission by matter at
finite temperature. Unlike conduction and convection, it requires
no medium and propagates through vacuum, enabling [[fukuoka-textdoc-three-dimensional-solar-energy-methodless-method]] to
reach Earth. All bodies above absolute zero emit radiation. The
Stefan-Boltzmann law gives the maximum emissive power of an ideal
blackbody: q equals sigma times T to the fourth power, where
sigma equals 5.67 times 10 to the negative 8 W/m^2-K^4 and T is
absolute temperature in Kelvin. Real surfaces emit less according
to their emissivity, a material property between zero and one.
Radiation exchange between surfaces depends on geometry, surface
properties, and view factors, analyzed using radiosity methods
for enclosures with multiple reflections.

## Combined Mechanisms

In most engineering systems, all three mechanisms operate
simultaneously. In a building wall, heat conducts through solid
material, convects from outer surfaces to ambient air, and
radiates to surroundings. Relative importance depends on
temperature level and geometry. Below roughly 500 Kelvin,
conduction and convection dominate; above this threshold,
radiation grows increasingly significant. In furnaces above 1000
Kelvin, radiation often accounts for most heat transfer. Thermal
resistance networks, analogous to electrical circuits, analyze
combined modes by assigning each mechanism a resistance term:
conductive resistance equals L/kA, convective resistance equals
1/hA, and radiative resistance depends on emissivities and view
factors.

## Phase Change Heat Transfer

Boiling and condensation are special convection cases with
exceptionally high transfer coefficients. During nucleate
boiling, vapor bubbles form at surface nucleation sites and
agitate surrounding liquid, producing coefficients an order of
magnitude higher than single-phase convection. Film boiling,
occurring at excessive temperature differences, insulates the
surface with a continuous vapor layer and reduces transfer
dramatically. Condensation similarly achieves high rates: film
condensation on vertical surfaces follows Nusselt's classical
theory, while dropwise condensation on non-wetting surfaces
achieves even greater performance. These processes are critical
to power plant condensers, refrigeration evaporators, and nuclear
reactor cooling.

## Thermal Insulation

Insulation reduces unwanted heat transfer using materials with
very low thermal conductivity such as fiberglass, mineral wool,
expanded polystyrene, polyurethane foam, and aerogels.
Effectiveness is measured by R-value (thermal resistance per unit
area) or U-value (overall heat transfer coefficient). Building
insulation reduces heating and cooling energy consumption
significantly. Electronic thermal management employs heat sinks,
heat pipes, thermal interface materials, and forced-air or liquid
cooling to dissipate processor heat. Insulation selection
balances thermal performance, cost, fire safety, moisture
resistance, and mechanical durability.

## See Also

- [[heat-exchanger-effectiveness-ntu]] design
- fourier law of conduction
- convection correlations
- thermal radiation and emissivity
- [[biomass-compost-greenhouse-heating-systems]]
- [[heat-transfer-coefficient]]
