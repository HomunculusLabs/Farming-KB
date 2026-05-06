---
title: Semiconductor Physics and Devices
type: concept
category: physics
related:
  - statistical-mechanics
  - crystal-structure-and-crystal-defects
  - phase-diagrams-and-phase-transformations
  - maxwell-equations-electromagnetism
  - dislocation-theory-crystal-plasticity
tags: [physics, semiconductor, band-theory, pn-junction, transistor,
  MOSFET, optoelectronics, fabrication, quantum-wells, doping,
  carrier-transport, integrated-circuits, materials-science]
created: 2026-05-02
type: concept
updated: 2026-05-02
sources: []
---

## Overview

Semiconductor physics governs materials with electrical conductivity between
metals and insulators, typically with band gaps of 0.1–3.5 eV. Silicon,
germanium, gallium arsenide, and compound semiconductors form the basis of
modern electronics, optoelectronics, and photovoltaics. The field bridges
quantum mechanics and electrical engineering. Key milestones: the transistor
at Bell Labs (1947, Shockley/Bardeen/Brattain) and the integrated circuit
(1958, Kilby; planar process, Noyce).

## Band Theory of Solids

In crystalline solids, discrete atomic energy levels broaden into continuous
energy bands via Pauli exclusion and orbital overlap. The **valence band**
(VB) is the highest occupied band at 0 K; the **conduction band** (CB) is
the lowest unoccupied band. The **band gap** E_g = E_C − E_V separates them.
Metals have overlapping bands (E_g ≈ 0), insulators large gaps (> 4 eV),
semiconductors moderate gaps. Key values at 300 K: Si (1.12 eV), Ge
(0.66 eV), GaAs (1.42 eV), GaN (3.4 eV), 4H-SiC (3.26 eV). Band gaps
shrink with temperature: E_g(T) = E_g(0) − αT²/(T + β).

## Intrinsic and Extrinsic Semiconductors

Intrinsic semiconductors are pure crystals where n = p: n_i = √(N_C N_V)
exp(−E_g/2kT). Extrinsic semiconductors are doped: **n-type** uses Group V
donors (P, As, Sb) contributing electrons; **p-type** uses Group III
acceptors (B, Ga, In) creating holes. The mass-action law holds: np = n_i².
At room temperature, n ≈ N_D (n-type) or p ≈ N_A (p-type).

## Carrier Statistics and Transport

The Fermi-Dirac distribution f(E) = 1/[1 + exp((E − E_F)/kT)] governs
state occupation. Under Boltzmann approximation: n = N_C exp((E_F − E_C)/kT)
and p = N_V exp((E_V − E_F)/kT). Drift current J = q(nμ_n + pμ_p)E arises
from electric fields; diffusion current J_n = qD_n(dn/dx) from gradients.
The Einstein relation links them: D = (kT/q)μ. Mobility is limited by
phonon scattering (μ ∝ T^{−3/2}) and impurity scattering. Conductivity
σ = q(nμ_n + pμ_p).

## Recombination and Generation

Electron-hole pairs recombine via: **band-to-band** (radiative, dominant
in direct-gap materials like GaAs); **Shockley-Read-Hall** trap-assisted
recombination through gap states; **Auger** recombination at high injection;
and **surface** recombination at dangling bonds. Carrier lifetime τ governs
excess carrier decay. These processes determine device switching speed,
efficiency, and noise characteristics.

## The p-n Junction

Joining p- and n-type material creates a depletion region of width
W = √(2ε_s(V_bi − V_a)(1/N_A + 1/N_D)/q) with built-in potential
V_bi = (kT/q)ln(N_A N_D/n_i²). The Shockley diode equation:
I = I_S[exp(qV_a/nkT) − 1], where I_S is saturation current and n is
ideality factor. Reverse breakdown occurs via avalanche or Zener tunneling.
Depletion capacitance C_j = ε_s/W enables voltage-variable capacitors.

## Bipolar Junction Transistors

A BJT has three regions (emitter, base, collector). In active mode,
I_C = βI_B where β = α/(1−α). The Ebers-Moll model describes all regions;
the Gummel-Poon model adds high-level injection and Early effect. BJTs
remain essential in analog and RF circuits for high transconductance.

## MOSFET Operation

A MOSFET controls current via a gate field across an insulator. Threshold
voltage V_T = V_{FB} + 2φ_F + √(2ε_s qN_A · 2φ_F)/C_{ox}. Saturation:
I_D = (½)μ_n C_{ox}(W/L)(V_GS − V_T)²(1 + λV_DS). Linear region:
I_D = μ_n C_{ox}(W/L)[(V_GS − V_T)V_DS − V_DS²/2]. Short-channel effects
include velocity saturation, DIBL, and subthreshold conduction. FinFETs and
gate-all-around nanosheets address scaling below 10 nm.

## Optoelectronic Devices

**LEDs**: Forward-biased junctions with radiative recombination at λ = hc/E_g.
Materials: GaAs (IR), InGaN (blue), AlGaN (UV). **Photodiodes**: Reverse-
biased; absorbed photons generate carriers with quantum efficiency η.
**Solar cells**: Maximum power point operation; Shockley-Queisser limit
~33% for single junction. **Laser diodes**: Population inversion in direct-
gap junctions with Fabry-Perot optical feedback.

## Compound Semiconductors

GaAs (1.42 eV, direct gap, μ_n ≈ 8500 cm²/Vs): RF, LEDs, lasers, solar
cells. InP (1.35 eV): fiber-optic communications (1.3–1.55 μm). GaN
(3.4 eV): blue LEDs, HEMTs for RF power. SiC (3.26 eV): high breakdown
field (~3 MV/cm) for power devices and EV inverters. Wide-bandgap materials
(GaN, SiC, diamond, β-Ga₂O₃) extend performance beyond Si limits.

## Fabrication Processes

Semiconductor fabrication: crystal growth (Czochralski for bulk; MBE/MOCVD
for epitaxy), photolithography (193 nm immersion, 13.5 nm EUV for sub-5 nm
nodes), doping (ion implantation, thermal diffusion), etching (RIE, wet),
metallization (sputtering, Cu damascene), and oxidation (thermal SiO₂).
Each step requires sub-nanometer precision in Class 1–10 cleanrooms.

## Quantum Wells and Heterostructures

Heterostructures combine semiconductors with different band gaps (AlGaAs/GaAs).
Quantum wells confine carriers in one dimension with discrete sub-bands:
E_n = ℏ²π²n²/(2m*L²). The 2D electron gas at AlGaN/GaN interfaces yields
sheet densities > 10¹³ cm⁻² without doping. Strain engineering in Si/SiGe
and InGaAs enhances mobility for CMOS and quantum computing.

## Modern Applications

CMOS scales to sub-3 nm nodes with >100 billion transistors per chip. SiC
MOSFETs and GaN HEMTs enable efficient power conversion for EVs, renewables,
and data centers. Silicon photonics integrates optical components on-chip.
CMOS image sensors dominate digital imaging. MEMS accelerometers and
biosensors leverage semiconductor processing for sensing applications.

## See Also

- [[finite-element-method]]

- [[quantum-mechanics-fundamentals]]
- [[stereochemistry-and-chirality]]
- [[tryptamines-and-quantum-mechanics]]
