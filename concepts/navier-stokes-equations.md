---
title: "Navier-Stokes Equations"
aliases: [Navier Stokes, fluid dynamics equations, NS equations]
tags: [physics, fluid-dynamics, engineering, partial-differential-equations]
related: [reynolds-number-and-flow-regimes, heat-transfer-mechanisms, laws-of-thermodynamics]
---

## Overview

The Navier-Stokes equations are the fundamental partial differential equations governing the motion of viscous fluid substances. Derived from Newton's
second law applied to fluid elements, they describe how the velocity field, pressure, temperature, and density of a moving fluid evolve in space and
time. Together with an equation of state and appropriate boundary conditions, they form a complete mathematical description of fluid flow. The
equations are central to aerodynamics, meteorology, oceanography, biomedical engineering, chemical processing, and astrophysics. Their mathematical
complexity — arising primarily from the nonlinear convective acceleration term — makes them among the most important and challenging equations in all
of mathematical physics. Despite being formulated in the 19th century, fundamental questions about their solutions remain unanswered, including
whether smooth solutions always exist in three dimensions — the subject of the Clay Mathematics Millennium Prize (US$1,000,000).

## Mathematical Formulation

### Compressible Form

The full compressible Navier-Stokes system consists of three equations: the continuity equation for mass conservation, the momentum equation derived
from Cauchy's stress principle, and the energy equation from the first law of thermodynamics. The continuity equation is ∂ρ/∂t + ∇·(ρu) = 0, where ρ
is the fluid density and u is the velocity vector field. The momentum equation is:

    ρ(∂u/∂t + u·∇u) = −∇p + ∇·τ + ρf

Here p is thermodynamic pressure, τ is the deviatoric (viscous) stress tensor, and f represents body forces per unit mass. For a Newtonian fluid, the
constitutive relation links stress to rate-of-strain linearly: τ = μ[∇u + (∇u)ᵀ − (2/3)(∇·u)I] + λ(∇·u)I, where μ is dynamic viscosity and λ is bulk
viscosity. Stokes' hypothesis sets λ = −(2/3)μ, exact for monatomic gases. The energy equation is ρ(∂e/∂t + u·∇e) = −p(∇·u) + τ:∇u + ∇·(k∇T) + ρq̇,
where e is specific internal energy, k is thermal conductivity, and q̇ is volumetric heat source. The system is closed by an equation of state,
typically p = ρRT for gases.

### Incompressible Form

When density is approximately constant (Mach number below ~0.3), the equations simplify considerably. The continuity equation reduces to the
incompressibility constraint ∇·u = 0, and the momentum equation becomes ρ(∂u/∂t + (u·∇)u) = −∇p + μ∇²u + ρf. Introducing kinematic viscosity ν = μ/ρ
gives the standard form: ∂u/∂t + (u·∇)u = −(1/ρ)∇p + ν∇²u + f. This is a system of four coupled nonlinear PDEs for three velocity components and
pressure. The pressure acts as a Lagrange multiplier enforcing incompressibility, determined through a Poisson equation from the divergence of
momentum.

## Historical Development

Leonhard Euler derived the inviscid Euler equations in 1755. Claude-Louis Navier introduced viscous effects in 1822 using molecular arguments.
Augustin-Louis Cauchy (1823-28) developed the stress tensor concept, formulating the Cauchy momentum equation ρDu/Dt = ∇·σ + ρf as the foundation for
all fluid models. Poisson (1829) independently derived equations with two viscosity coefficients. Saint-Venant (1843) arrived at the same form via
continuum arguments. George Gabriel Stokes provided the definitive derivation in 1845, assuming a linear, isotropic stress-rate-of-strain relationship
— defining a Newtonian fluid. His paper "On the Theories of the Internal Friction of Fluids in Motion" is the canonical reference. The equations bear
both names: Navier first included viscosity and Stokes provided the correct general derivation.

## Physical Interpretation of Terms

Each term in the momentum equation has a distinct physical role. The unsteady acceleration ρ∂u/∂t represents local inertia from time-varying flow. The
convective acceleration ρ(u·∇)u represents nonlinear momentum transport by the flow itself — the sole source of nonlinearity, responsible for boundary
layer separation, vortex shedding, and turbulence. The pressure gradient −∇p drives fluid from high to low pressure. The viscous diffusion μ∇²u
represents molecular friction diffusing momentum, smoothing velocity gradients; it dominates at low Reynolds numbers and is mathematically analogous
to heat conduction. Body forces ρf include gravity, Lorentz forces in magnetohydrodynamics, Coriolis forces in rotating frames, and buoyancy via the
Boussinesq approximation.

## Boundary Conditions

The equations require initial velocity data and boundary conditions. The no-slip condition (u = 0 at walls) is standard for Newtonian fluids when the
Knudsen number (mean free path / characteristic length) is below ~0.01; it fails for rarefied gases. Free-slip conditions enforce impermeability with
zero tangential stress, used for symmetry planes. Periodic boundaries are standard in DNS/LES of homogeneous turbulence. Inlet conditions prescribe
velocity profiles or mass flow rates; outlet conditions include zero-gradient (Neumann), convective, pressure-specified, and non-reflecting
characteristic formulations. Free surfaces require kinematic conditions (surface particles remain on interface) and dynamic stress balance including
surface tension via the Young-Laplace equation Δp = σκ.

## Dimensionless Numbers and Flow Similarity

Non-dimensionalizing the Navier-Stokes equations reveals key similarity parameters. The Reynolds number Re = UL/ν (inertial/viscous force ratio) is
the single most important parameter in fluid mechanics: low Re → laminar, high Re → turbulent, with critical Re ~2300 for pipe flow (Reynolds, 1883).
The Mach number Ma = U/c governs compressibility: incompressible for Ma < 0.3, supersonic for Ma > 1, hypersonic for Ma > 5. The Froude number Fr =
U/√(gL) governs free-surface flows (ships, open channels). The Strouhal number St = fL/U characterizes oscillatory phenomena — vortex shedding occurs
at St ≈ 0.2 for cylinders. The Weber number We = ρU²L/σ controls surface tension effects (droplet breakup, inkjet printing). The Prandtl number Pr =
μcₚ/k governs relative thickness of velocity and thermal boundary layers.

## Exact Analytical Solutions

Exact solutions exist only for highly simplified configurations where the nonlinear term vanishes or simplifies. Couette flow (1890) between parallel
plates gives a linear profile u(y) = Uy/h. Plane Poiseuille flow (1840) is pressure-driven between plates with parabolic profile u(y) =
(1/2μ)(dp/dx)(y² − h²). Hagen-Poiseuille flow (1839-40) in a circular pipe of radius R gives u(r) = (1/4μ)(−dp/dz)(R² − r²) with volumetric flow rate
Q = πR⁴Δp/(8μL) — the fourth-power law, fundamental to piping design and hemodynamics.

Stokes flow (Re << 1) neglects inertia entirely, yielding the linear system μ∇²u = ∇p − ρf with Stokes' drag law F_D = 6πμRU for a sphere —
fundamental to microfluidics, particle settling, and biological flows (flagella, cilia). Hiemenz stagnation point flow (1911) reduces Navier-Stokes to
the ODE f''' + ff'' − f'² + 1 = 0. Taylor-Green and Burgers vortices provide additional exact solutions for testing turbulence models.

## Turbulence and the Closure Problem

Reynolds averaging (u = ū + u') introduces the Reynolds stress tensor τ^R_ij = −ρ<u'_iu'_j>, creating six additional unknowns with no equations — the
fundamental closure problem (Reynolds, 1895). Computational approaches form a hierarchy: RANS models all turbulence using models like mixing length
(Prandtl, 1925), k-ε (Launder-Spalding, 1974), and k-ω SST (Menter, 1994) — cheapest but cannot capture unsteady structures. LES resolves large eddies
while modeling sub-grid scales (Smagorinsky 1963, dynamic model of Germano et al. 1991). DNS resolves all scales to the Kolmogorov microscale η =
(ν³/ε)^(1/4), requiring ~Re^(9/4) grid points in 3D — prohibitive for engineering Re. Hybrid RANS-LES methods like DES (Spalart, 1997) combine
approaches. Kolmogorov's 1941 theory predicts E(k) ~ k^(−5/3) in the inertial subrange.

## Computational Methods

The finite volume method (FVM) dominates industrial CFD, enforcing conservation on unstructured grids (ANSYS Fluent, STAR-CCM+, OpenFOAM) with
SIMPLE/PISO pressure-velocity coupling. The finite difference method (FDM) uses Taylor series on structured grids for high-order accuracy (WENO,
compact schemes). Spectral methods expand solutions in global basis functions (Fourier, Chebyshev) with exponential convergence — the gold standard
for DNS. The [[finite-element-method]] (FEM) handles complex geometries via weak formulations (FEniCS, COMSOL). The lattice Boltzmann method (LBM)
simulates fluid via particle distributions on a lattice, excelling in complex geometries and multiphase flows. Smoothed particle hydrodynamics (SPH)
is a meshless Lagrangian method natural for free-surface flows.

## The Millennium Prize Problem

The Navier-Stokes existence and smoothness problem is one of seven Clay Mathematics Millennium Prize Problems (US$1M). The challenge: prove or
disprove that in three dimensions, given smooth (C^∞) divergence-free initial data with finite energy and zero body forces, the equations admit a
unique smooth solution for all time. Ladyzhenskaya proved existence and uniqueness in 2D (1969). In 3D, Leray proved existence of weak (finite-energy)
solutions (1934), but whether these develop singularities (finite-time blowup) is unknown. The convective term can amplify velocity gradients via
vortex stretching. No blowup has been constructed, nor proven impossible. Terence Tao published important partial results on averaged and modified
equations (2014–2019).

## Applications

In aerospace, Navier-Stokes solutions govern aircraft aerodynamics, drag reduction, lift, and re-entry heating — modern aircraft design relies
entirely on CFD. Automotive applications include vehicle aerodynamics, engine flows, and cooling systems. Civil engineers apply them to river
hydraulics, pollutant dispersion, and wind loading on structures. Meteorologists and oceanographers use them for weather prediction and climate
modeling — the atmosphere and oceans are Navier-Stokes flows on a rotating sphere with Coriolis forces.

Biomedical applications include hemodynamics (blood flow, aneurysm assessment, heart valves), respiratory airflow, and drug delivery. Energy
applications span turbomachinery, combustion, and nuclear thermal-hydraulics. Astrophysical applications include stellar interiors, mantle convection,
accretion disks, and magnetohydrodynamics (MHD). The equations also describe manufacturing processes including casting, injection molding, and
additive manufacturing flow simulation.

## See Also

- [[navier-stokes-equations-fluid-dynamics]]

- [[hyphal-growth-dynamics]]

- [[fungal-growth-dynamics]]

- [[phase-transitions-and-critical-phenomena]]
