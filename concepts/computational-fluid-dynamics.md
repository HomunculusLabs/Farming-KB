---
title: Computational Fluid Dynamics
aliases: [CFD, numerical [[turbulence-modeling-fluid-dynamics]], fluid-flow simulation]
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

The energy equation is needed when compressibility, [[heat-transfer-mechanisms]], combustion, [[phase-change-materials-thermal-energy-storage]], or temperature-dependent material properties matter.

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
