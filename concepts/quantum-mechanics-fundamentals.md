---
title: [[tryptamines-and-quantum-mechanics]] Fundamentals
type: concept
category: physics
related:
  - [[statistical-mechanics]]
  - [[maxwell-equations-electromagnetism]]
  - [[crystal-structure-and-crystal-defects]]
  - [[laws-of-thermodynamics]]
tags: [physics, quantum-mechanics, wave-function, schrodinger-equation,
  hilbert-space, entanglement, uncertainty-principle, superposition,
  quantum-computing, wave-particle-duality]
created: 2026-05-02
type: concept
updated: 2026-05-02
sources: []
---

## Overview

Quantum mechanics (QM) is the fundamental theory describing nature at
atomic and subatomic scales, where classical mechanics fails. It replaces
deterministic trajectories with probability amplitudes and introduces
phenomena such as superposition and entanglement. The theory emerged from
the crisis of classical physics — the ultraviolet catastrophe, atomic
stability, and discrete spectral lines — motivating breakthroughs by
Planck, Einstein, Bohr, de Broglie, Heisenberg, Schrödinger, Born,
Dirac, and Pauli. Max Planck (1900) introduced energy quanta (E = hν);
Einstein (1905) extended this to light; Bohr (1913) proposed quantized
orbits; de Broglie (1924) hypothesized wave-particle duality (λ = h/p);
Heisenberg (1925) developed matrix mechanics; Schrödinger (1926)
formulated wave mechanics; Born gave the probabilistic interpretation;
Dirac (1928) unified QM with relativity, predicting antimatter.

## Core Postulates

1. **State vector**: A quantum system is completely described by a
   vector |ψ⟩ in a Hilbert space.
2. **Observables**: Every measurable quantity corresponds to a
   Hermitian operator; measurement yields an eigenvalue with
   probability |⟨a|ψ⟩|².
3. **Time evolution**: States evolve unitarily via iℏ ∂|ψ⟩/∂t = Ĥ|ψ⟩.
4. **Wave-particle duality**: All entities exhibit both wave-like
   (interference) and particle-like (discrete detection) behavior.
5. **Uncertainty principle**: Δx Δp ≥ ℏ/2; non-commuting observables
   cannot be simultaneously measured with arbitrary precision.
6. **Superposition**: A system can exist in a linear combination of
   eigenstates until measurement causes collapse.
7. **Measurement problem**: The act of measurement causes a non-unitary
   "collapse" — the mechanism remains debated across interpretations.

## The Schrödinger Equation

The time-dependent form governs dynamical evolution:
iℏ ∂Ψ(r,t)/∂t = Ĥ Ψ(r,t), where Ĥ = −ℏ²/(2m)∇² + V(r).
For stationary states Ψ(r,t) = ψ(r)e^(−iEt/ℏ), this reduces to the
time-independent eigenvalue equation Ĥ ψ(r) = E ψ(r). Solving yields
energy eigenvalues E_n and eigenfunctions ψ_n. The wavefunction is
not directly observable; |ψ(r)|² gives the probability density.

## Key Solutions

**Particle in a box** (width L): E_n = n²π²ℏ²/(2mL²), demonstrating
quantization, zero-point energy, and nodal structure.

**Harmonic oscillator** (V = ½mω²x²): E_n = ℏω(n + ½) with equally
spaced levels — foundational for molecular vibrations and quantum field
theory. Eigenfunctions involve Hermite polynomials H_n(x).

**Hydrogen atom** (Coulomb potential): E_n = −13.6 eV/n² with quantum
numbers n (principal), ℓ (orbital), m (magnetic). Eigenfunctions use
spherical harmonics Y_ℓm(θ,φ) and associated Laguerre polynomials.

## Angular Momentum and Spin

Orbital angular momentum L̂ = r̂ × p̂ satisfies [L̂_i, L̂_j] = iℏ ε_ijk L̂_k
with eigenvalues L² = ℏ²ℓ(ℓ+1), L_z = ℏm. Spin is intrinsic angular
momentum with no classical analog. Electrons have s = ½ (↑, ↓ states).
The Pauli exclusion principle forbids identical fermions from sharing
a quantum state, dictating mollison soil elements structure and chemistry.

## Perturbation Theory and Approximations

Most real systems lack exact solutions. Time-independent perturbation
theory expands corrections: E_n = E_n⁽⁰⁾ + ⟨ψ_n⁽⁰⁾|V̂'|ψ_n⁽⁰⁾⟩ + ...
Fermi's golden rule gives transition rates: Γ_{i→f} = (2π/ℏ)|⟨f|V̂'|i⟩|²ρ(E_f).
The WKB approximation treats nearly-classical systems; variational
methods provide upper bounds on ground-state energies.

## Entanglement and Bell's Theorem

Two particles are entangled when their joint state cannot be factored:
|Ψ⟩ = (1/√2)(|00⟩ + |11⟩). Measurement of one determines the other
instantly — "spooky action at a distance" (Einstein). Bell's theorem
(1964) proved no local hidden-variable theory reproduces all QM
predictions. Experimental violations (Aspect 1982; Nobel Prize 2022)
confirmed entanglement as genuine, now a resource for quantum
cryptography, teleportation, and computing.

## Mathematical Formalism

Quantum mechanics operates on Hilbert spaces — complete inner-product
vector spaces over ℂ. Observables are Hermitian operators (Â = Â†)
with real eigenvalues. The commutator [Â,B̂] = ÂB̂ − B̂Â determines
simultaneous measurability. The density operator ρ̂ describes mixed
states: Tr(ρ̂) = 1, with ρ̂² = ρ̂ for pure states and Tr(ρ̂²) < 1
for mixed states. The spectral theorem guarantees eigenfunction
expansions for Hermitian operators.

## Interpretations

- **Copenhagen** (Bohr, Heisenberg): Wavefunction collapses upon
  measurement; dominant practical interpretation.
- **Many-worlds** (Everett, 1957): Universal wavefunction never
  collapses; all outcomes realized in decoherent branches.
- **Pilot-wave / de Broglie–Bohm**: Deterministic particle trajectories
  guided by ψ; nonlocal but recovers standard predictions.
- **Decoherence** (Zurek): Environmental interaction suppresses
  superpositions, explaining the quantum-to-classical transition.

## Key Experimental Confirmations

- **Photoelectric effect** (Einstein, 1905): Electron KE depends on
  light frequency, not intensity — confirming photons (E = hν).
- **Compton scattering** (1923): Wavelength shift Δλ = (h/m_e c)(1 − cos θ)
  confirms photon momentum p = h/λ.
- **Double-slit experiment** (Davisson–Germer 1927): Individual particles
  build interference patterns — direct evidence of wave-particle duality.
- **Stern–Gerlach experiment** (1922): Discrete atomic deflections in a
  magnetic field demonstrate spatial quantization and spin-½.

## Applications

- **Atomic/molecular physics**: Electronic structure, spectroscopy,
  chemical bonding (MO and VB theory).
- **Solid-state physics**: Band theory explains conductors, semiconductors,
  insulators — the foundation of modern electronics.
- **Quantum computing**: Qubits exploit superposition and entanglement;
  Shor's algorithm (factoring) and Grover's search offer speedups.
- **Quantum optics**: Single-photon sources, squeezed light, QKD (BB84),

## See Also
- [[stereochemistry-and-chirality]]
- [[teaming-with-microbes-soil-food-web-trophic-structure-and-succession]]
- [[teaming-with-microbes-soil-food-web-overview]]
