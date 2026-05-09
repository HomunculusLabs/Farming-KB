---
title: Navier-Stokes Equations in Fluid Dynamics
type: concept
aliases: [Navier-Stokes, Navier Stokes equations, N-S equations, fluid motion equations]
tags: [physics, fluid-dynamics, PDE, continuum-mechanics, CFD, engineering, mathematics]
created: 2026-05-02
updated: 2026-05-06
type: concept
sources:
  - "raw/papers/permaculture-a-designers-manual-bill-mollison.md"
---

The **[[mollison-designers-home-energy-conservation-and-solar-heating]] y conservation:

**Mass:** ∂ρ/∂t + ∇·(ρ**u**) = 0

**Momentum:** ∂(ρ**u**)/∂t + ∇·(ρ**u**⊗**u**) = −∇p + ∇·**τ** + **f**

**Energy:** ∂(ρE)/∂t + ∇·[(ρE + p)**u**] = ∇·(**τ**·**u**) − ∇·**q** + **f**·**u** + Q

Where **τ** = μ[∇**u** + (∇**u**)ᵀ − (2/3)(∇·**u**)**I**] + λ(∇·**u**)**I** is the viscous stress tensor (λ is the bulk viscosity), *E* = *e* + ½|**u**|² is total specific energy, **q** = −*k*∇T is Fourier heat flux, and *Q* is volumetric heating. An equation of state (e.g., *p* = ρRT) closes the system.

## Physical Meaning of Each Term

| Term | Expression | Meaning |
|------|-----------|---------|
| Local acceleration | ∂**u**/∂t | Velocity change at a fixed point (unsteadiness) |
| Convective acceleration | (**u**·∇)**u** | Momentum transport by fluid motion (nonlinear) |
| Pressure gradient | −∇p/ρ | Force from spatial pressure variations |
| Viscous diffusion | ν∇²**u** | Momentum diffusion from internal friction |
| Body forces | **f**/ρ | External forces (gravity, Coriolis, electromagnetic) |

The convective term is the source of nonlinearity, responsible for turbulence and flow instability. The viscous term is linear and [[continuum-mechanics]] foundations.
- **1831 — Poisson**: Extended to compressible fluids, introducing the second viscosity coefficient (dilatational viscosity).
- **1843 — Saint-Venant**: Derived based on the hypothesis that viscous stress is proportional to the rate of deformation — the Newtonian fluid assumption.
- **1845 — Stokes**: Definitive derivation using the Cauchy stress principle and linear stress-rate-of-strain dependence. Identified the Stokes' hypothesis (λ = −2μ/3), exact for monatomic ideal gases.

## Simplifications and Special Cases

- **Euler equations** (μ → 0, inviscid): Valid at high Reynolds numbers away from boundaries. Foundation of potential flow and aerodynamic lift theory. Hyperbolic character.
- **Stokes flow** (Re ≪ 1, creeping flow): Inertia negligible, equation becomes linear: 0 = −∇p + μ∇²**u** + **f**. Governs microfluidics, lubrication theory, biological flows at Re ~ 10⁻⁵.
- **Potential flow** (irrotational + inviscid): **u** = ∇φ, Bernoulli's equation holds throughout. Cannot predict drag (d'Alembert's paradox) but useful for preliminary aerodynamic design.
- **Boundary layer approximation** (Prandtl, 1904): At high Re near walls, viscous effects confined to thin layer. Yields parabolic Prandtl equations. See boundary [[bloomfield-buller-drop-surface-tension-spore-catapult-basidiospore-discharge]] ency vs. flow timescale; vortex shedding |
| Weber | We = ρU²L/σ | Inertial vs. [[bloomfield-buller-drop-surface-tension-spore-catapult-basidiospore-discharge]]; droplet and bubble dynamics |
| Prandtl | Pr = μcₚ/k = ν/α | Momentum vs. thermal diffusivity |
| Eckert | Ec = U²/(cₚΔT) | Kinetic energy vs. enthalpy; viscous dissipation heating |

Low Re → viscous-dominated; high Re → inertia-dominated (turbulent); Ma > 0.3 → compressible.

## Boundary Conditions

- **No-slip**: **u** = **u**_wall at solid boundaries. Standard for viscous flows; creates boundary layers and skin friction.
- **Free-slip**: **u**·**n** = 0, tangential stress vanishes. Used for inviscid approximations and symmetry planes.
- **Periodic**: **u**(**x** + **L**) = **u**(**x**). Standard in DNS and homogeneous turbulence simulations.
- **Inflow/outflow**: Prescribed profiles at inflow; zero-gradient or convective outflow at outlets. Absorbing BCs prevent spurious reflections in compressible flows.
- **Moving boundaries**: No-slip at instantaneous wall position for fluid-structure interaction; requires moving mesh or immersed boundary methods.

## Exact Solutions

- **Couette flow**: Steady flow between parallel plates, one moving. Linear profile *u*(*y*) = *Uy*/*h*; constant wall shear τ_w = μU/h.
- **Poiseuille flow**: Pressure-driven flow in a circular pipe. Parabolic profile *u*(*r*) = (1/4μ)(−dp/dx)(*R*² − *r*²). Hagen-Poiseuille law: *Q* = π*R*⁴(−dp/dx)/(8μ).
- **Hiemenz stagnation-point flow** (1911): Normal impingement on a flat plate. Similarity solution with boundary layer thickness δ ~ √(ν/a).

Other exact solutions: Taylor-Couette (concentric rotating cylinders), Burgers vortex, Jeffery-Hamel (converging/diverging channel).

## Turbulence and the Closure Problem

At Re > ~2300 (pipe) or Re_x > ~5×10⁵ (flat plate), solutions become turbulent. Reynolds decomposition (**u** = ū + **u'**) introduces the Reynolds stress tensor τᵢⱼ^R = −ρ⟨u'ᵢu'ⱼ'⟩ — six unknowns with no additional equations. This is the **closure problem**.

Modeling hierarchy (see [[finite-element-method]] (FEM) | Weak/variational formulation | Complex geometries; rigorous math framework | Historically lacked discrete conservation |
| Spectral | Global basis functions (Fourier, Chebyshev) | Exponential convergence for smooth solutions | Restricted to regular domains |
| Lattice Boltzmann (LBM) | Kinetic theory / Boltzmann equation | Excellent parallelism; complex boundaries | Compressibility artifacts; limited Mach range |

Hybrid approaches include Discontinuous Galerkin (DG), Immersed Boundary Methods (IBM) for moving geometries, and Arbitrary Lagrangian-Eulerian (ALE) for fluid-structure interaction.

## The Millennium Prize Problem

The Clay Mathematics Institute (2000) offers $1M for proving (or counterexample): in three dimensions, do smooth, sufficiently decaying initial conditions always produce smooth solutions for all time? Formally stated by Fefferman, the problem asks whether finite-time singularities can form from the nonlinear convective term transferring energy to arbitrarily small scales.

Leray (1934) proved existence of weak solutions (H¹) in 3D but could not show they remain smooth. In 2D, existence and uniqueness of smooth solutions is established. Despite extensive DNS showing no singularities, no 3D proof exists — it remains one of the most important open problems in mathematics.

## Applications

- **Aerospace**: Aircraft aerodynamics, re-entry heating, jet engine combustion, rotor aerodynamics
- **Mechanical/Civil**: Wind loading, HVAC design, pipe networks, hydraulic machinery
- **Chemical**: Reactor mixing, slurry transport, polymer processing, crystallization
- **Biomedical**: Blood flow (pulsatile, non-Newtonian), respiratory airflow, microfluidics
- **Geophysical**: Atmospheric/oceanic circulation, pollutant dispersion, tsunami propagation
- **Energy**: Wind turbines, nuclear thermal hydraulics, reservoir simulation, battery cooling

## Key References

Batchelor, G.K. (1967). *An Introduction to Fluid Dynamics*. Cambridge.
Landau, L.D. & Lifshitz, E.M. (1987). *Fluid Mechanics*, 2nd ed. (Vol. 6). Pergamon.
Panton, R.L. (2013). *Incompressible Flow*, 4th ed. Wiley.
White, F.M. (2015). *Viscous Fluid Flow*, 3rd ed. McGraw-Hill.
Pope, S.B. (2000). *Turbulent Flows*. Cambridge.
Toro, E.F. (2009). *Riemann Solvers and Numerical Methods for Fluid Dynamics*, 3rd ed. Springer.
## See Also

- boundary layer theory fluid dynamics
- [[heat-transfer-mechanisms]]
