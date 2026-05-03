---
title: "Semiconductor Band Structure"
aliases: [energy bands in semiconductors, semiconductor band theory, band gap physics]
tags: [solid-state-physics, electrical-engineering, materials-science, semiconductors]
created: 2026-05-02
type: concept
sources: []
---

## Overview

Semiconductor band structure describes the allowed and forbidden electron energies in a crystalline semiconductor. It explains why silicon,
germanium, gallium arsenide, and related materials conduct better than insulators but worse than metals under ordinary conditions.

The central feature is the band gap between a filled valence band and an empty or partly populated conduction band. Electrons promoted
across the gap behave as mobile negative carriers, while the missing valence electrons behave as mobile positive holes.

Band structure connects quantum mechanics to device engineering. The same energy diagram that explains optical absorption also explains
rectifying junctions, transistors, solar cells, light-emitting diodes, photodiodes, and many failure modes in integrated circuits.

Unlike a simple circuit model, band structure is spatially local. Bands can bend near surfaces, junctions, gates, and charged defects, so
device behavior depends on electrostatics as well as the bulk material band gap.

## From Atomic Levels to Bands

Isolated atoms have discrete orbitals. When many atoms form a crystal, overlapping orbitals split into enormous numbers of closely spaced
states that are treated as continuous bands.

The Pauli exclusion principle limits how many electrons can occupy each state. In a semiconductor at low temperature, bonding-derived
valence bands are nearly full and antibonding-derived conduction bands are nearly empty.

The periodic lattice potential allows electron wavefunctions to be written as Bloch states. Each state is labeled by a band index and a
crystal wavevector inside the Brillouin zone, producing an energy relation E(k).

The curvature of E(k) matters because it determines effective mass. Electrons and holes in a crystal respond to forces as if they had masses
different from the free electron mass, sometimes with strong directional dependence.

## Direct and Indirect Gaps

A direct band gap occurs when the conduction-band minimum and valence-band maximum occur at the same crystal momentum. Optical transitions
can then conserve momentum while emitting or absorbing a photon efficiently.

An indirect band gap occurs when those extrema lie at different wavevectors. A phonon is needed to conserve momentum, so radiative
recombination is much less likely even if the energy gap is appropriate.

Gallium arsenide is a common direct-gap semiconductor and is useful for efficient light emission. Silicon has an indirect gap, which is one
reason ordinary silicon is a poor light-emitting material despite dominating electronics.

Direct versus indirect character shapes photovoltaic absorption thickness, laser diode design, detector response, and the choice between
compound semiconductors and silicon for optoelectronic systems.

## Carrier Statistics

At finite temperature, some electrons occupy conduction-band states and some holes exist in the valence band. The probability of occupation
is governed by Fermi-Dirac statistics and the position of the Fermi level.

In an intrinsic semiconductor, electron and hole concentrations are equal. The intrinsic carrier concentration rises rapidly with
temperature and falls exponentially as the band gap increases.

Doping shifts the carrier balance by introducing impurity levels. Donors contribute electrons and move the Fermi level toward the conduction
band, while acceptors contribute holes and move it toward the valence band.

Degenerate doping can push the Fermi level into a band, making a semiconductor behave partly like a metal. This regime is important for
contacts, source and drain regions, and transparent conducting oxides.

## Band Bending and Junctions

When two semiconductor regions with different Fermi levels are joined, charge redistributes until electrochemical equilibrium is reached.
The resulting electric field bends the bands and creates depletion or accumulation regions.

A p-n junction is the canonical example. Ionized dopants remain fixed in the depletion region, producing a built-in potential that allows
current easily under forward bias and blocks most current under reverse bias.

Metal-semiconductor contacts form either Schottky barriers or approximately ohmic contacts depending on work function, interface states,
doping, and tunneling probability. Real contacts often deviate from ideal textbook diagrams.

In a MOS capacitor or MOSFET, a gate voltage bends bands near the oxide interface. Accumulation, depletion, and inversion describe whether
majority carriers, fixed ionized dopants, or minority carriers dominate the surface charge.

## Effective Density of States and Mobility

The number of available states near a band edge is summarized by an effective density of states. Combined with Fermi- level position, it
determines carrier concentration in nondegenerate semiconductor equations.

Mobility measures how quickly carriers drift under an electric field. It is limited by phonon scattering, ionized impurity scattering, alloy
disorder, interface roughness, and crystal defects.

High mobility is not always paired with a desirable band gap. Narrow-gap materials may conduct easily but leak current at high temperature,
while wide-band-gap materials can block large voltages but may be harder to dope or contact.

The product of mobility, carrier concentration, charge, and geometry becomes device conductance. Band structure therefore sets the material
side of what circuit designers experience as resistance, transconductance, capacitance, and leakage.

## Materials and Band-Gap Engineering

Silicon is successful because it has a useful band gap, a stable native oxide, abundant processing knowledge, and adequate carrier mobility.
Its band structure is not optimal for every purpose, but its manufacturing ecosystem is unmatched.

Compound semiconductors allow band gaps and lattice constants to be tuned by composition. Aluminum gallium arsenide, indium gallium
arsenide, gallium nitride, and related alloys support heterostructures, lasers, high-speed devices, and power electronics.

Wide-band-gap semiconductors such as silicon carbide and gallium nitride tolerate high electric fields and temperatures. They are important
in efficient power conversion, radio-frequency devices, and harsh environments.

Quantum wells, superlattices, and strained layers deliberately modify band structure. Confinement changes allowed energies, while strain
shifts valley positions and effective masses, enabling engineered optical wavelengths and faster transistors.

## Defects, Surfaces, and Real Devices

Vacancies, interstitials, dislocations, impurities, and dangling bonds can introduce states inside the band gap. These states trap carriers,
assist recombination, pin the Fermi level, or create leakage paths.

Surface and interface states are especially important because modern devices have large interface area relative to volume. The quality of
the silicon dioxide interface was historically decisive for MOS technology.

Recombination mechanisms depend on band structure. Direct radiative recombination dominates in some optoelectronic materials, while
Shockley-Read-Hall recombination through defect levels and Auger recombination dominate in other regimes.

Thermal generation across the band gap contributes to leakage current. As devices shrink and electric fields rise, tunneling through thin
barriers and narrow depletion regions becomes increasingly important.

## Measurement and Modeling

Optical absorption, photoluminescence, electrical conductivity, Hall measurements, and capacitance-voltage profiling reveal different
aspects of band structure and carrier behavior.

Angle-resolved photoemission can directly probe electronic bands near surfaces, while cyclotron resonance and magnetotransport can estimate
effective masses. Device engineers often infer band parameters indirectly from calibrated test structures.

Theoretical models range from simple parabolic bands to tight-binding, k dot p, empirical pseudopotential, and density- functional
calculations. Each trades accuracy, physical transparency, and computational cost.

Compact circuit models hide most band-structure detail, but their parameters are grounded in it. Threshold voltage, subthreshold slope,
saturation current, breakdown voltage, and optical response all trace back to bands, carriers, and interfaces.

## Related Concepts

- p-n junctions
- MOSFETs
- [[kirchhoffs-circuit-laws]]
- [[piezoelectric-materials-and-transducers]]
- crystallography
- solid-state diffusion

## References

- Wikipedia, "Electronic band structure," accessed for Bloch-state, Brillouin-zone, and direct-gap terminology.
- Wikipedia, "Semiconductor," accessed for carrier, doping, and device context.
- Wikipedia, "Band gap," accessed for valence-band, conduction-band, and optical transition definitions.
