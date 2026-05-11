---
title: "Phase phase transitions and critical phenomena Phenomena"
created: 2026-04-28
updated: 2026-05-06
aliases: [phase transitions, critical phenomena, critical exponents, universality, renormalization group]
tags: [physics, thermodynamics, statistical-mechanics, condensed-matter, materials-science]
related: [[laws-of-thermodynamics]], [[heat-transfer-mechanisms]], [[navier-stokes-equations]]
type: concept
sources: []
---

## Overview

A phase transition is a transformation of a thermodynamic system from one phase to another, characterized by non-analytic behavior in thermodynamic
quantities such as the free energy, entropy, or specific heat. Phase transitions are ubiquitous in nature — from the boiling of water to the onset of
[[superconductivity]] — and their study connects thermodynamics, [[statistical-mechanics]], and condensed matter physics. The behavior of systems near
critical points, where the distinction between phases vanishes, reveals remarkable universal properties that are independent of microscopic details,
described by renormalization group theory and characterized by critical exponents and universality classes.

## Classification of Phase Transitions

Phase transitions are classified by the behavior of thermodynamic quantities at the transition. First-order transitions involve a discontinuous first
derivative of the free energy (entropy, volume), with latent heat absorbed or released. Examples include melting, boiling, and most structural
transitions in solids. Phases can coexist along the coexistence curve, and metastability (supercooling, superheating) is common due to nucleation
barriers.

Second-order (continuous) transitions involve a continuous first derivative but a divergent second derivative (specific heat, compressibility,
susceptibility). No latent heat is released. The order parameter changes continuously from zero in the disordered phase to nonzero in the ordered
phase. The system exhibits critical phenomena: power-law divergences, scale invariance, and universal scaling. Examples include the Curie point in
ferromagnets, the superfluid transition in helium-4, and the liquid-gas critical point.

Lambda transitions (named for the λ-shaped specific heat curve) are a subclass of continuous transitions, most famously the lambda point in liquid ⁴He
at T_λ ≈ 2.17 K where helium transitions from normal fluid (He I) to superfluid (He II). Glass transitions are fundamentally different — a kinetic
phenomenon where structural relaxation time exceeds experimental timescales as a supercooled liquid is cooled, with no symmetry breaking. Quantum
phase transitions occur at T = 0, driven by non-thermal parameters (pressure, magnetic field, doping) and governed by quantum fluctuations rather than
thermal fluctuations.

## Thermodynamic Framework

Phase equilibrium requires equality of temperature T, pressure P, and chemical potential μ = (∂G/∂N)_{T,P} between coexisting phases. The phase with
the lowest Gibbs free energy G = U − TS + PV is thermodynamically stable. For a first-order transition, the Clausius-Clapeyron equation dP/dT = ΔS/ΔV
= L/(TΔV) determines the slope of phase boundaries in the P-T diagram, where L is the latent heat.

The Ehrenfest classification (1933) defines an nth-order transition as one where the (n−1)th derivatives of G are continuous but the nth derivatives
are discontinuous. While conceptually useful, this classification has limitations — actual second-order transitions typically involve divergences
rather than finite discontinuities, and some transitions (like the lambda transition) do not fit neatly. Modern classifications focus on order
parameter behavior and critical exponents.

## Order Parameters and Landau Theory

An order parameter is a thermodynamic quantity that is zero in the disordered (high-symmetry) phase and nonzero in the ordered (lower-symmetry) phase.
Examples include magnetization M for ferromagnets (breaks rotational symmetry), density difference ρ_L − ρ_G for the liquid-gas transition,
superconducting gap Δ for superconductors (breaks U(1) gauge symmetry), and superfluid density ρ_s for ⁴He. Spontaneous symmetry breaking occurs when
the ground state has lower symmetry than the governing Hamiltonian.

Landau theory (1937) provides a phenomenological mean-field description by expanding the free energy as a power series in the order parameter ψ:
F(T,ψ) = F₀(T) + a(T)ψ² + bψ⁴ + cψ⁶ + ... − hψ, where a(T) = a₀(T − T_c) changes sign at T_c, b > 0 ensures stability, and h is a conjugate field.
Minimizing yields ψ = 0 for T > T_c and ψ ∝ (T_c − T)^{1/2} for T < T_c, predicting mean-field critical exponents β = 1/2, α = 0, γ = 1, δ = 3. These
are approximate for d < 4 dimensions where fluctuations are important.

## Critical Exponents and Universality

Near a critical point, thermodynamic quantities follow power laws characterized by critical exponents. Defining the reduced temperature t = (T −
T_c)/T_c, the key exponents are: α (specific heat C ~ |t|^{−α}), β (order parameter ψ ~ (−t)^β), γ (susceptibility χ ~ |t|^{−γ}), δ (critical isotherm
ψ ~ h^{1/δ}), ν (correlation length ξ ~ |t|^{−ν}), and η (correlation function G(r) ~ 1/r^{d−2+η}). These six exponents are related by scaling laws
(Widom, Rushbrooke, Griffiths, Fisher, Josephson), reducing them to only two independent values.

Universality is the remarkable observation that systems with different microscopic details share the same critical exponents if they have the same
spatial dimensionality d and order parameter dimensionality n. Key universality classes include: 2D Ising (d=2, n=1): β = 1/8, γ = 7/4, ν = 1; 3D
Ising (d=3, n=1): β ≈ 0.326, γ ≈ 1.237, ν ≈ 0.630; 3D XY (d=3, n=2): β ≈ 0.349, γ ≈ 1.317; 3D Heisenberg (d=3, n=3): β ≈ 0.369, γ ≈ 1.396. Mean-field
exponents (β = 1/2, γ = 1, ν = 1/2) become exact above the upper critical dimension d_c = 4.

## The Ising Model

The Ising model is the simplest lattice model exhibiting a phase transition. Defined on a lattice of N sites with spins s_i = ±1, the Hamiltonian is H
= −J Σ_{<i,j>} s_i s_j − h Σ_i s_i, where J > 0 is the ferromagnetic coupling. Despite its simplicity, it captures the essential physics of uniaxial
magnets, binary alloys, and the liquid-gas transition (via the lattice gas mapping). The 1D Ising model (1925) has no phase transition at T > 0. The
2D square lattice model was solved exactly by Lars Onsager in 1944, a landmark achievement in statistical mechanics, yielding T_c = 2J/[k_B ln(1+√2)]
≈ 2.269 J/k_B with exact exponents β = 1/8, γ = 7/4, δ = 15. The 3D model has no exact solution; exponents are known from high-precision numerical
methods.

## Renormalization Group Theory

The renormalization group (RG) provides the deep theoretical framework for understanding critical phenomena and universality. Leo Kadanoff introduced
the block spin concept in 1966: near T_c the correlation length diverges, so the system is scale-invariant. Dividing the lattice into blocks and
replacing each block's spins with a single effective spin defines an RG transformation that [[maps]] coupling constants to new values. Kenneth Wilson made
RG quantitative in 1971 (Nobel Prize 1982) by integrating out short-wavelength fluctuations [[fukuoka-rice-barley-step-by-step-method]] via momentum-shell RG.

Under successive RG transformations, coupling constants flow through parameter space. Fixed points of this flow correspond to scale-invariant critical
points. Relevant perturbations (growing under RG) drive the system away from criticality and determine critical exponents; irrelevant perturbations
