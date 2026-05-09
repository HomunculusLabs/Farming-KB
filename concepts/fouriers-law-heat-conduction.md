---
title: "Fourier's Law of Heat Conduction"
aliases: [Fourier law, heat conduction equation, conductive heat flux]
tags: [thermodynamics, heat-transfer, materials-science, physics, engineering]
created: 2026-05-02
updated: 2026-05-06
type: concept
sources:
  - "raw/papers/permaculture-a-designers-manual-bill-mollison.md"
---

## Definition
Fourier's law states that conductive heat flux is proportional to the negative temperature gradient in a material.

In one dimension the common engineering form is q = -k dT/dx, where q is heat flux and k is thermal conductivity.

The minus sign records that heat flows from higher temperature toward lower temperature when no external work drives it otherwise.

For a flat wall of thickness L under steady conditions, the heat rate is Qdot = k A (Thot - Tcold) / L.

[[query-how-to-make-a-diy-still-air-box-for-mushroom-cultivation]] ferent heat fluxes in copper, glass, still air, or an insulating foam.

That locality works extremely well for ordinary engineering scales where microscopic carrier mean free paths are much smaller than the component.

## Differential and Integral Forms
The vector form is q vector = -k grad T for an isotropic material with scalar thermal conductivity.

For anisotropic media such as composites, single crystals, or layered laminates, k becomes a second-rank tensor.

The tensor form allows heat to flow in a direction that is not exactly opposite the temperature gradient.

Cylinders and spheres require geometry-dependent area terms because the conduction area changes with radius.

For a cylindrical pipe wall, radial conduction gives a logarithmic resistance proportional to ln(r2/r1) / (2 pi k L).

Thermal resistance notation writes conduction as Qdot = delta T / Rth, making heat-transfer networks resemble electrical circuits.

This analogy is useful for multilayer walls, insulation systems, electronic packages, and heat exchanger design.

## Link to the Heat Equation
Combining Fourier's law with conservation of internal energy produces the transient heat equation.

For constant properties and no internal generation, the result is partial T partial t = alpha nabla squared T.

The thermal diffusivity alpha = k / (rho cp) measures how quickly a temperature disturbance spreads through a material.

High conductivity increases diffusivity, while high density or heat capacity stores more energy and slows temperature change.

With internal heat generation, a volumetric source term appears and is essential for nuclear fuel, batteries, reactors, and electronics.

Many design calculations are therefore boundary-value problems built around Fourier conduction and energy conservation.

Analytical solutions exist for simple shapes, while complex assemblies usually require finite difference, finite volume, or finite element methods.

## Material Dependence
Thermal conductivity varies over many orders of magnitude across [[phase-change-materials-thermal-energy-storage]] olids, and phase-change materials.

Moisture content is important in building materials because liquid water conducts heat much better than dry air in pores.

Microstructure matters: grain boundaries, dislocations, precipitates, porosity, and interfaces scatter heat carriers.

Engineered materials exploit this fact in thermal barrier coatings, thermoelectrics, ceramic substrates, and composite heat spreaders.

## Engineering Uses
Fourier's law is the starting point for insulation thickness calculations in buildings, furnaces, cryogenic tanks, and process piping.

It estimates temperature drops across electronic packages, where small thermal resistances can determine device reliability.

It is used in quenching, casting, welding, and additive manufacturing because therm passive solar greenhouse design and energy systems rive cooling rates and residual stresses.

In energy systems, conductive losses through walls and supports are part of efficiency, safety, and thermal management budgets.

In geophysics, conductive heat flow helps interpret geothermal gradients and the thermal history of rocks.

In biology and medicine, conduction helps estimate heat transfer in tissues, probes, implants, and cryotherapy tools.

The same law appears in dimensional analysis through the Biot number and Fourier number for transient conduction.

Engineers often pair it with convection correlations and radiation laws because real systems rarely use only one heat-transfer mode.

## Assumptions and Limits
Classical Fourier conduction assumes local thermal equilibrium, continuum behavior, and finite material properties.

It predicts that temperature disturbances propagate with infinite speed, a mathematical artifact that is negligible in ordinary conditions.

At very short times, very low temperatures, or nanoscale dimensions, non-Fourier and ballistic transport models may be needed.

When carrier mean free paths approach device dimensions, heat flow depends on boundaries and may not be captured by bulk conductivity.

Strongly nonlinear conductivity requires solving with k as a function of temperature, phase, composition, or damage state.

Moving boundaries complicate the picture in melting, freezing, ablation, and solidification problems.

Contact resistance can dominate a joint even when both solids individually have high conductivity.

Radiation across gaps or convection in fluids can masquerade as conduction if an experiment is not c [[heat-exchanger-effectiveness-ntu]] through wall conduction and overall heat-transfer coefficients.

In numerical simulation it is commonly solved with [[nitrogen-transfer-through-common-mycorrhizal-networks]]
