---
title: "Computational Fluid Dynamics"
aliases: [CFD, numerical fluid dynamics, fluid-flow simulation]
tags: [engineering, fluid-dynamics, computational-physics, simulation, numerical-methods]
created: 2026-05-02
updated: 2026-05-06
type: concept
sources: []
---

## Overview
Computational fluid dynamics, usually abbreviated CFD, is the numerical simulation of fluid flow and related transport processes.

It uses computers to approximate the governing equations for liquids, gases, plasmas, sprays, bubbles, [[heat-transfer-coefficient]], reacting mixtures, and moving interfaces.

CFD is valuable when analytical solutions are unavailable and physical experiments are expensive, dangerous, slow, difficult to instrument, or impossible at full scale.

It does not replace experiments; it complements them by providing detailed fields of velocity, pressure, temperature, species concentration, vorticity, and wall shear.

The method is central in aerospace, turbomachinery, automotive design, electronics cooling, civil engineering, weather prediction, biomedical flows, chemical reactors, marine hydrodynamics, and energy systems.

## Governing Equations
Most CFD begins with conservation of mass, momentum, and energy written for a continuum fluid.

The Navier-Stokes equations relate velocity, pressure, density, viscosity, body forces, and acceleration for viscous flow.

The energy equation is needed when compressibility, heat transfer, combustion, [[phase-change-materials-thermal-energy-storage]], or temperature-dependent material properties matter.

Species-transport equations track mixtures, pollutants, vapor, combustion products, dissolved substances, or chemical reactants.

Simplified models include potential flow, Euler equations, boundary- layer equations, shallow-water equations, lubrication theory, and incompressible Navier-Stokes equations.

Choosing the governing equations is an engineering judgment about which physics controls the result and which terms can be safely neglected.

## Discretization
CFD converts partial differential equations into algebraic equations over a finite set of cells, nodes, or elements.

Finite volume methods integrate conservation equations over control volumes and compute fluxes through their faces.

This conservative form makes finite volume schemes especially common in industrial aerodynamics, compressible flow, turbomachinery, and general- purpose CFD software.

Finite difference methods approximate derivatives on structured grids and are efficient for canonical, atmospheric, oceanic, and high-order research simulations.

[[finite-element-method]] methods represent fields with basis functions over elements and are useful for complex geometry, incompressible flow, multiphysics coupling, and stabilized formulations.

Spectral, spectral-element, discontinuous Galerkin, lattice Boltzmann, vortex, particle, and immersed-boundary methods serve specialized accuracy, geometry, or physics needs.

## Meshes and Geometry
A mesh divides the physical domain into computational cells, and its quality strongly affects accuracy, stability, convergence, and cost.

Structured meshes provide regular indexing and high efficiency for simple geometries, boundary layers, ducts, channels, and canonical flows.

Unstructured meshes handle complex aircraft, engines, buildings, vessels, valves, and biological geometries using tetrahedra, prisms, pyramids, polyhedra, or hybrid cells.

Important mesh-quality measures include cell size, skewness, orthogonality, aspect ratio, smoothness of transitions, and boundary conformity.

Wall-bounded turbulent flows require careful near-wall resolution, often measured by the nondimensional wall distance y-plus.

Adaptive mesh refinement concentrates resolution near shocks, shear layers, vortices, interfaces, flames, recirculation zones, or error indicators.

## Numerical Solution
A CFD solver assembles and solves large algebraic systems, often through iterative methods and time marching.

Pressure-velocity coupling in incompressible flow may use SIMPLE, PISO, projection methods, or related algorithms.

Compressible solvers commonly use density-based schemes, flux splitting, approximate Riemann solvers, limiters, and shock-capturing methods.

The Courant-Friedrichs-Lewy condition links time step, cell size, and wave speed or flow speed, influencing stability and computational cost.

Spatial order, temporal order, numerical diffusion, dispersion, residual convergence, under-relaxation, and nonlinear solver tolerance all affect the computed solution.

A visually smooth result can still be wrong if convergence is false, boundary conditions are inconsistent, or discretization error dominates the signal.

## Turbulence Modeling
Turbulence contains interacting eddies across many length and time scales, making direct resolution too costly for most engineering Reynolds numbers.

Direct numerical simulation resolves all dynamically relevant scales and avoids turbulence modeling, but it is mostly limited to research and low-to-moderate Reynolds-number benchmarks.

Large eddy simulation resolves large unsteady eddies while modeling smaller subgrid scales, giving rich flow physics at much higher cost than steady industrial methods.

Reynolds-averaged Navier-Stokes methods solve for mean flow quantities and model all turbulent fluctuations, making them the workhorse of routine engineering CFD.

Common RANS closures include Spalart-Allmaras, k-epsilon, k-omega, shear-stress-transport k-omega, and Reynolds stress models.

Hybrid RANS-LES methods, such as detached eddy simulation, combine wall- modeled averaging with resolved separated structures but are sensitive to grid design and model assumptions.

## Boundary and Initial Conditions
Boundary conditions translate the physical problem into mathematical constraints on the computational domain.

Common boundaries specify no-slip walls, slip walls, inlet velocity, mass flow, stagnation conditions, turbulence quantities, outlet pressure, symmetry, periodicity, or far-field flow.

Thermal problems may require wall temperature, heat flux, convective heat transfer, radiation, conjugate heat transfer, or contact resistance.

Multiphase and reacting simulations require additional conditions for volume fraction, species, droplet injection, evaporation, [[bloomfield-buller-drop-surface-tension-spore-catapult-basidiospore-discharge]], kinetics, or phase change.

Initial conditions matter for transient flows, vortex shedding, combustion ignition, multiphase startup, turbulence development, and simulations with multiple stable states.

Many CFD failures arise less from the solver than from boundary conditions that are convenient but physically inconsistent.

## Verification and Validation
Verification asks whether the equations were solved correctly by the code and by the chosen mesh, time step, and convergence criteria.

Code verification may use exact solutions, manufactured solutions, benchmark cases, regression tests, and comparison with trusted algorithms.

Solution verification estimates numerical uncertainty through grid convergence, time-step convergence, residual monitoring, conservation checks, and sensitivity studies.

Validation asks whether the equations and models represent the real physical system for the intended application.

Validation compares predictions with wind-tunnel data, full-scale tests, pressure taps, particle-image velocimetry, heat-transfer measurements, force balances, or field observations.

A credible CFD study reports assumptions, boundary conditions, mesh independence, model choices, uncertainty, and the range in which conclusions are valid.

## Applications
Aerospace engineers use CFD for airfoils, wings, inlets, nozzles, reentry vehicles, rotorcraft, aeroacoustics, icing, and propulsion.

Automotive engineers use it for drag, underbody flow, engine combustion, cabin ventilation, battery cooling, brake cooling, and soiling.

Energy applications include wind turbines, gas turbines, nuclear thermal hydraulics, hydropower, oil-and-gas pipelines, boilers, heat exchangers, and carbon-capture equipment.

Civil and environmental applications include wind loading on buildings, urban pollutant dispersion, rivers, floods, coastal flows, sediment transport, and ventilation.

Biomedical simulations examine blood flow, aneurysms, heart valves, respiratory airflow, drug delivery, and medical-device performance.

Entertainment and graphics also use fluid simulation, though production visual effects often prioritize plausible motion over engineering validation.

## Limitations and Pitfalls
CFD accuracy depends on the governing equations, mesh, numerics, boundary conditions, material properties, turbulence model, and user judgment.

Strong separation, transition, shocks, cavitation, combustion, sprays, free surfaces, wall roughness, fluid-structure interaction, and multiphase flow remain difficult.

RANS models can give plausible but misleading answers when calibrated outside their domain of validity.

LES and DNS reduce some modeling errors but shift the burden to resolution, wall treatment, sampling time, and computational expense.

Poor meshes may create artificial diffusion, unstable iterations, nonphysical pressure fields, or hidden local errors.

## See Also
- [[turbulence-modeling-fluid-dynamics]]
- [[heat-transfer-mechanisms]]
- [[navier-stokes-equations-fluid-dynamics]]

## References
- Wikipedia, "Computational fluid dynamics," accessed 2026-05-02.
- NASA Glenn Research Center, "Navier-Stokes Equations," accessed 2026-05-02.
- Versteeg and Malalasekera, An Introduction to Computational Fluid Dynamics: The Finite Volume Method.

## See Also

- [[navier-stokes-equations-fluid-dynamics]]
