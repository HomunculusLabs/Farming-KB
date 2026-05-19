---
title: Semiconductor Physics and Devices
type: concept
category: physics
related:
  - [[crystal-structure-and-crystal-defects]]
  - [[maxwell-equations-electromagnetism]]
  - [[dislocation-theory-crystal-plasticity]]
tags: [physics, semiconductor, band-theory, pn-junction, transistor,
  MOSFET, optoelectronics, fabrication, quantum-wells, doping,
  carrier-transport, integrated-circuits, materials-science]
created: 2026-05-02
type: concept
updated: 2026-05-02
sources:
  - "raw/papers/permaculture-a-designers-manual-bill-mollison.md"
---

## Overview

Semiconductor physics governs materials with electrical conductivity between
metals and insulators, typically with band gaps of 0.1–3.5 eV. [[gallium-arsenide]], and compound semiconductors form the basis of
modern electronics, optoelectronics, and photovoltaics. The field bridges
[[quantum-mechanics-fundamentals]] and electrical engineering. Key milestones: the transistor
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

## See Also
- [[dom]]
- [[mollison-designers-hand-pump-and-water-lifting-devices]]
- [[dmt-entity-encounters-and-the-logos]]
## Practical Applications
The principles discussed here have direct applications in agricultural systems, ecological restoration, and sustainable resource management.
Practitioners have demonstrated successful implementation across diverse climates and soil conditions.
Adaptation to local conditions and careful observation remain central to effective application.

## Research Directions
Current research explores the intersections between traditional knowledge and modern scientific understanding.
Comparative studies across different bioregions provide valuable insights into generalizable principles.
Long-term monitoring and documentation continue to build the evidence base for these approaches.
Collaborative research networks facilitate knowledge exchange and accelerate innovation.

## Key Considerations
Context-specific implementation requires attention to local ecology, climate patterns, and community needs.
Integration with existing systems often yields better results than complete replacement strategies.
Monitoring and adaptive management are essential for long-term success and continuous improvement.

## Integration Strategies
Successful implementation often draws on multiple complementary approaches working in concert.
Scale-appropriate solutions range from backyard gardens to broadacre agricultural systems.
Knowledge sharing between practitioners accelerates collective learning and refinement of methods.
## Practical Considerations
Successful implementation requires attention to detail and adaptation to local conditions.
Field experience and systematic observation remain the most reliable guides for practitioners.

## Future Directions
Emerging research continues to validate and refine traditional approaches.
Integration with modern technology offers new possibilities for monitoring and optimization.
## Further Considerations
Ongoing research and field trials continue to expand our understanding of this subject.
Practical experience combined with systematic observation yields the most reliable insights.

## Future Directions
Emerging approaches and technologies offer new opportunities for advancement.
Collaborative knowledge sharing accelerates progress across related domains.
