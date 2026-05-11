---
title: Superconductivity
type: concept
aliases: [superconductor, superconducting state, zero resistance, Meissner effect, Cooper pairing]
tags: [physics, condensed-matter, materials-science, quantum-mechanics, cryogenics]
created: 2026-05-02
updated: 2026-05-06
type: concept
sources: []
---

Superconductivity is a [[mckenna-quantum-mechanical-correlates-hallucinogenesis]] phenomenon in which certain materials exhibit
zero electrical resistance and expel magnetic fields below a characteristic critical
temperature (Tc). Discovered by Heike Kamerlingh Onnes in 1911 at Leiden University
in solid mercury at 4.2 K, it remains one of the most profound phenomena in condensed
matter physics with transformative applications in medicine, energy, and computing.

## Historical Milestones

The discovery timeline spans over a century of breakthroughs. Onnes achieved the first
liquefaction of helium in 1908, enabling temperatures below 4.2 K. His observation of
zero resistance in mercury (1911) opened the field. Walther Meissner and Robert
Ochsenfeld discovered flux expulsion (the Meissner effect) in 1933. Fritz and Heinz
London proposed their phenomenological equations in 1935. Vitaly Ginzburg and Lev Landau
published their order-parameter theory in 1950. The microscopic BCS theory arrived in
1957 from Bardeen, Cooper, and Schrieffer. Brian Josephson predicted Cooper pair
tunneling (Josephson effect) in 1962, earning the 1973 Nobel Prize. The revolution in
high-temperature superconductivity began with J. Georg Bednorz and K. Alex Müller's
discovery of Ba-La-Cu-O at 35 K (1986, Nobel 1987), followed by YBa2Cu3O7 (YBCO)
at 93 K by Paul Chu (1987), MgB2 at 39 K by Akimitsu (2001), iron pnictides by
Hosono (2008), and hydrogen-rich compounds H3S at 203 K under 150 GPa by Eremets
(2015) and LaH10 at 250 K under 170 GPa (2019).

## Cooper Pairs and BCS Theory

In the BCS framework, electrons near the Fermi surface form bound pairs via an attractive
interaction mediated by lattice vibrations (phonons). Each Cooper pair has total spin 0
(singlet, s-wave symmetry in conventional superconductors) and carries charge 2e. The
pairing condenses into a macroscopic quantum ground state described by a single coherent
wavefunction. The energy gap Delta(T) opens at the Fermi surface below Tc; at T = 0,
Delta(0) = 1.764 kB Tc. The coherence length xi_0 = hbar v_F / (pi Delta) sets the
Cooper pair size (typically 10-1000 nm). The BCS prediction for critical temperature:
kB Tc = 1.14 hbar omega_D exp(-1/N(0)V), where omega_D is the Debye frequency, N(0) the
density of states, and V the pairing interaction. The isotope effect Tc proportional
to M^(-0.5) confirmed the phonon [[trace-water-flash-steam-mechanism-microwave-surface-sterilization-physics|mechanism]] experimentally in mercury.

## Meissner Effect and Flux Quantization

Below Tc, a superconductor expels all magnetic flux from its interior (B = 0), not merely
failing to resist changes in flux. This distinguishes a superconductor from a perfect
conductor. The screening current flows in a surface layer of penetration depth lambda
(London penetration depth, typically 20-200 nm). The London equations govern this:
the first gives zero DC resistance; the second predicts exponential field decay over
lambda_L = sqrt(m* / (mu_0 n_s e^2)). Magnetic flux threading a superconducting loop
is quantized in units of the flux quantum Phi_0 = h/(2e) = 2.0678e-15 Wb, directly
confirming the Cooper pair charge carrier of 2e.

## Type I and Type II Superconductors

Type I superconductors exhibit a single critical field Hc with an abrupt transition:
full Meissner state below Hc, normal above. Hc values are low (0.01-0.1 T). Examples
include Pb (Tc=7.2 K, Hc=0.08 T), Hg (Tc=4.2 K), Al (Tc=1.2 K), and Sn (Tc=3.7 K).
Nearly all are elemental. Type II superconductors possess two critical fields (Hc1 and
Hc2). Between them, magnetic flux partially penetrates as quantized vortices in the
mixed (Shubnikov) state. Each vortex carries one flux quantum Phi_0 with a normal core
of radius ~xi surrounded by supercurrents decaying over lambda. Hc2 can reach tens of
Tesla. Examples: NbTi (Tc=9.8 K, Hc2=14.5 T), Nb3Sn (Tc=18.3 K, Hc2=28 T), YBCO
(Tc=93 K, Hc2>100 T). Nearly all practical superconductors are Type II.

## Ginzburg-Landau Theory and the Vortex State

The GL theory uses a complex order parameter psi(r) with free energy: F = alpha|psi|^2
+ (beta/2)|psi|^4 + (1/2m*)|(-i hbar grad - 2eA)psi|^2 + B^2/(2 mu_0). The GL
coherence length xi(T) = xi_0 / sqrt(1 - T/Tc) defines the distance over which psi
varies. The GL parameter kappa = lambda/xi determines type: kappa < 1/sqrt(2) gives
Type I; kappa > 1/sqrt(2) gives Type II. In the mixed state, vortices arrange in an
Abrikosov vortex lattice (hexagonal pattern, Nobel 2003). Vortex pinning by defects,
grain boundaries, or artificial pinning centers is essential for maintaining high
critical current density Jc in Type II superconductors.

## High-Temperature Superconductors

Cuprates feature general formulas Ln2-xMxCuO4 (electron-doped) or LnM2Cu2O7-delta
(hole-doped). YBCO achieves Tc=93 K with in-field Jc > 10^6 A/cm^2 at 77 K. Bi-2223
reaches Tc=110 K; Hg-1223 holds the ambient [[pressure-cooker-sterilization-time-temperature-jar-size-mushroom-substrate|pressure]] record at Tc=133 K (1993). Their
pairing mechanism is non-BCS with confirmed d-wave symmetry and strong electron
correlations. Iron-based superconductors (LaFeAsO, Ba1-xKxFe2As2, SmFeAsO-F at 55 K)
have multi-band Fe 3d structure with proposed s+/- pairing symmetry, less anisotropy
than cuprates, and easier wire fabrication. MgB2 (Tc=39 K) is a cheap two-gap
superconductor practical for MRI below 20 K.
