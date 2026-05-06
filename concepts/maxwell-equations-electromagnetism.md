---
title: Maxwell's Equations of Electromagnetism
type: concept
aliases: [Maxwell equations, Maxwell's equations, electromagnetic field equations]
tags: [physics, electromagnetism, classical-electrodynamics, wave-equation]
created: 2026-05-02
type: concept
---

Maxwell's equations are the four foundational equations of classical electromagnetism,
unifying electric fields, magnetic fields, electric charge, and electric current into
a single coherent framework. Together with the Lorentz force law, they form the basis
of all classical electromagnetic phenomena, from static charges and magnets to radio
[[turbulence-modeling-fluid-dynamics|wave]]s, light, and X-rays. The equations were developed by James Clerk Maxwell between
1855 and 1865, building on the experimental work of Michael Faraday, André-Marie Ampère,
and Carl Friedrich Gauss. Their prediction that light is an electromagnetic wave —
traveling at speed c = 1/√(μ₀ε₀) — is one of the greatest unifications in physics.

## Historical Development

Faraday's 1831 discovery of [[electromagnetic-induction-faraday-law]] — changing magnetic fields
produce electric fields — provided the conceptual foundation. Maxwell formalized these
ideas in his 1865 paper "A Dynamical Theory of the Electromagnetic Field," originally
using 20 quaternion equations. In 1884, Heaviside and Hertz reformulated them into the
compact four vector equations used today, introducing div, curl, and grad operators.
Hertz verified Maxwell's wave prediction in 1887 by generating and detecting radio waves.

## The Four Equations

In SI units within linear media, the four equations in differential form are:

**Gauss's Law for Electricity:** ∇·**D** = ρ_free

The net electric flux through any closed surface equals the total free charge enclosed.
Electric field lines originate on positive charges and terminate on negative charges.
In vacuum this becomes ∇·**E** = ρ/ε₀, with integral form ∮_S **E**·d**A** = Q_enc/ε₀.

**Gauss's Law for Magnetism:** ∇·**B** = 0

There are no magnetic monopoles — magnetic field lines form continuous closed loops.
The integral form ∮_S **B**·d**A** = 0 states that net magnetic flux through any
closed surface is zero. While Dirac theorized magnetic monopoles might exist, none
have been observed experimentally.

**Faraday's Law of Induction:** ∇×**E** = −∂**B**/∂t

A time-varying magnetic field generates a circulating electric field. The negative sign
embodies Lenz's law: the induced EMF opposes the change causing it. Integral form:
∮_C **E**·d**l** = −d/dt ∮_S **B**·d**A**. This law governs generators, transformers,
and inductors — the foundation of nearly all electric power generation worldwide.

**Ampère–Maxwell Law:** ∇×**H** = **J**_free + ∂**D**/∂t

Magnetic fields circulate around both conduction currents and changing electric fields.
The displacement current ∂**D**/∂t was Maxwell's key contribution, extending Ampère's
original law (∇×**B** = μ₀**J**) to include time-varying fields. Integral form:
∮_C **H**·d**l** = I_enc + d/dt ∮_S **D**·d**A**.

## The Displacement Current

Maxwell's addition of ∂**D**/∂t resolved a fundamental inconsistency. Taking the
divergence of the original Ampère's law gives ∇·**J** = 0, contradicting charge
conservation (∇·**J** = −∂ρ/∂t). The displacement current restores consistency.
Physically, in a charging capacitor where no conduction current crosses the gap, the
changing electric field between plates provides the displacement current that sustains
the magnetic field, matching the conduction current in the wires. Crucially, the
displacement current creates the ∂**E**/∂t ↔ ∂**B**/∂t symmetry with Faraday's law
that enables self-sustaining electromagnetic wave solutions.

## Constitutive Relations

The auxiliary fields **D** and **H** relate to **E** and **B** through constitutive
equations characterizing each medium's electromagnetic response. For linear, isotropic
media: **D** = ε**E** (ε = ε₀ε_r, permittivity), **B** = μ**H** (μ = μ₀μ_r,
permeability), and **J** = σ**E** (Ohm's law, σ = conductivity). Vacuum constants are
ε₀ = 8.854 × 10⁻¹² F/m and μ₀ = 4π × 10⁻⁷ H/m. For anisotropic media such as
birefringent [[dislocation-theory-crystal-plasticity|crystal]]s, these become tensor relations: D_i = ε_ij E_j. In dispersive
media, ε and μ depend on frequency ε(ω), producing chromatic dispersion. Nonlinear
media exhibit intensity-dependent responses including the Kerr effect and second-
harmonic generation, essential to nonlinear optics and photonics.

## [[boundary-layer-theory-fluid-dynamics|Boundary]] Conditions

At an interface between two media, Maxwell's equations impose conditions derived from
the integral forms using infinitesimal pillboxes and Amperian loops: **n̂**·(**D**₂ −
**D**₁) = σ_f (normal D jumps by free surface charge); **n̂**·(**B**₂ − **B**₁) = 0
(normal B is continuous); **n̂**×(**E**₂ − **E**₁) = **0** (tangential E continuous);
**n̂**×(**H**₂ − **H**₁) = **K**_f (tangential H jumps by surface current). For a
perfect conductor, fields vanish inside and decay with skin depth δ = √(2/ωμσ).
These conditions yield Snell's law and the Fresnel equations at dielectric interfaces.

## Electromagnetic Waves

In source-free vacuum (ρ = 0, **J** = 0), taking the curl of Faraday's law and
substituting the Ampère–Maxwell law produces the wave equation: ∇²**E** − μ₀ε₀
∂²**E**/∂t² = 0, with an identical equation for **B**. The propagation speed is
c = 1/√(μ₀ε₀) ≈ 2.998 × 10⁸ m/s — precisely the measured speed of light. EM waves
are transverse: **E** ⊥ **B** ⊥ **k**, with |**B**| = |**E**|/c. They carry energy
via the Poynting vector **S** = **E**×**H** (W/m²) and momentum density **S**/c².

## Potentials and Gauge Freedom

Because ∇·**B** = 0, the magnetic field can be written as **B** = ∇×**A** for a
vector potential **A**. Substituting into Faraday's law yields **E** = −∇φ − ∂**A**/∂t,
where φ is the scalar electric potential. The gauge transformation **A** → **A** + ∇Λ,
φ → φ − ∂Λ/∂t leaves all observable fields invariant. The Lorenz gauge (∇·**A** +
με ∂φ/∂t = 0) produces wave equations for both potentials and is relativistically
covariant. The Coulomb gauge (∇·**A** = 0) is preferred in magnetostatics. Retarded
potentials describe radiation: fields at (**r**, t) depend on sources at (**r'**,
t − |**r**−**r'**|/c).

## Relativistic Formulation

Maxwell's equations are naturally Lorentz covariant — they were the clue that led
Einstein to special relativity in 1905. The antisymmetric electromagnetic field tensor
F^μν combines all six components of **E** and **B** into a single geometric object.
The four-potential A^μ = (φ/c, **A**) gives F^μν = ∂^μA^ν − ∂^νA^μ. The two
covariant equations are ∂_μ F^μν = μ₀J^ν (inhomogeneous) and ∂_μ F̃^μν = 0
(homogeneous, using the dual tensor). Under Lorentz boosts, parallel field components
remain unchanged while perpendicular components mix: **E**⊥' = γ(**E**⊥ + **v**×**B**⊥)
and **B**⊥' = γ(**B**⊥ − **v**×**E**⊥/c²), revealing **E** and **B** are frame-
dependent aspects of a single electromagnetic field.

## Applications

Maxwell's equations govern radio and wireless communications (antenna radiation,
waveguide modes, transmission line theory), optics (Snell's law, Fresnel equations,
birefringence, diffraction), microwave engineering (cavity resonators, scattering
theory), and antenna theory (radiation patterns, directivity, gain, impedance).
Electromagnetic compatibility and interference analysis depend entirely on solving
Maxwell's equations with appropriate boundary conditions.

## Numerical Methods

Analytical solutions exist only for simple geometries. Modern engineering relies on
computational electromagnetics. **FDTD** (Finite-Difference Time-Domain, Yee 1966)
discretizes Maxwell's curl equations on a staggered grid with leapfrog integration,
providing broadband results in one simulation. **FEM** uses Nédélec edge elements on
unstructured meshes for frequency-domain problems (COMSOL, ANSYS HFSS). **MoM** solves
surface integral equations, ideal for open-boundary scattering and radiation.
Additional methods include FIT (CST Studio), TLM, and Discontinuous Galerkin.

## Unit Systems

In **SI units** (engineering standard), ε₀ and μ₀ appear explicitly with **E** in V/m
and **B** in Tesla. In **Gaussian CGS** (theoretical physics), ε₀ = μ₀ = 1, **E**
and **B** share dimensions, and c appears explicitly in Faraday's and Ampère's laws.
The Lorentz force also differs: **F** = q(**E** + **v**×**B**) in SI versus **F** =
q(**E** + **v**×**B**/c) in Gaussian. Converting requires careful tracking of 4π
factors and powers of c. SI simplifies engineering calculations; Gaussian produces
more symmetric theoretical expressions.
