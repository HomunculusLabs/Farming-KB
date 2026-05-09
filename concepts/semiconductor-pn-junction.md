---
title: "Semiconductor P-N Junction"
aliases: [pn junction, p-n diode junction, depletion junction]
tags: [electrical-engineering, semiconductors, electronics, solid-state-physics, materials-science]
created: 2026-05-02
updated: 2026-05-06
type: concept
sources:
  - "raw/papers/permaculture-a-designers-manual-bill-mollison.md"
---

## Overview

A semiconductor p-n junction is the interface between p-type and n-type regions within one semiconductor crystal or device structure.
The p side contains holes as majority carriers because acceptor dopants create empty valence-band states.
The n side contains electrons as majority carriers because donor dopants supply extra conduction-band electrons.
When the two regions meet, electrons and holes diffuse across the interface and recombine.
This leaves behind fixed ionized dopants near the junction and creates a depletion region with very few mobile carriers.
The resulting built-in electric field opposes further diffusion and establishes equilibrium.
This simple interface is the basis of diodes, bipolar transistors, solar cells, LEDs, photodiodes, and many integrated-circuit structures.
Its importance comes from rectification: current flows much more easily under forward bias than under reverse bias.
The p-n junction is therefore one of the core devices linking [[silicon]] has relatively few thermally generated carriers at room temperature compared with a doped device.
Doping with group V atoms such as phosphorus creates donor levels and increases the electron concentration.
Doping with group III atoms such as boron creates acceptor levels and increases the hole concentration.
The terms p type and n type describe majority carrier sign, not net electrical charge of the bulk material.
Each neutral region remains approximately charge neutral because mobile carriers balance ionized dopants.
The Fermi level shifts upward toward the conduction band on the n side and downward toward the valence band on the p side.
Before contact, these different Fermi levels indicate different carrier chemical potentials.
After contact and equilibrium, the Fermi level becomes constant across the structure.
Band bending near the junction is the energy-band expression of the internal electric field.
The amount of band bending is related to the built-in potential.

## Depletion Region

The depletion region forms because mobile electrons and holes diffuse away from the immediate junction and annihilate by recombination.
Ionized donors on the n side and ionized acceptors on the p side cannot move in the crystal lattice.
Their exposed charge creates a space-charge region and an electric field pointing from the n side toward the p side.
This field produces drift currents that oppose diffusion currents.
At thermal equilibrium, electron and hole diffusion are exactly balanced by drift.
The depletion width depends on doping concentration, semiconductor permittivity, temperature, and applied voltage.
Lightly doped sides deplete more widely than heavily doped sides because more volume is needed to expose the required fixed charge.
An abrupt junction has a sharper doping transition than a graded junction, so its field and capacitance profiles differ.
The depletion approximation treats the region as carrier-free and the neutral regions as field-free.
Although idealized, that approximation is accurate enough for many hand calculations.

## Forward Bias

Forward bias connects the p side to a higher potential than the n side.
This reduces the junction barrier and narrows the depletion region.
Majority carriers are injected across the interface where they become minority carriers on the other side.
Injected electrons in p material and injected holes in n material then diffuse away from the junction and recombine.
The resulting current rises approximately exponentially with applied voltage over a useful operating range.
For silicon diodes, a forward drop near 0.6 to 0.8 volts is common at ordinary currents, but it is not a fixed threshold.
The exact voltage depends on current, temperature, device area, doping, series resistance, and recombination mechanisms.
At high current, ohmic resistance in the semiconductor and contacts bends the current-voltage curve away from ideal exponential behavior.
At low current, recombination in the depletion region can dominate and change the ideality factor.
Forward-biased junctions also store charge, which affects switching speed.

## Reverse Bias

Reverse bias connects the p side to a lower potential than the n side.
This increases the barrier and widens the depletion region.
Only a small reverse saturation current flows in an ideal diode, mainly from thermally generated minority carriers.
Real reverse current also includes leakage along surfaces, defects, and generation within the depletion region.
If the reverse voltage becomes large enough, breakdown occurs.
Zener breakdown is associated with strong electric fields and tunneling in heavily doped junctions.
Avalanche breakdown occurs when carriers gain enough energy to create additional electron-hole pairs by impact ionization.
Breakdown is not necessarily destructive if current is externally limited and heat is managed.
Zener diodes and avalanche diodes deliberately use controlled breakdown for voltage reference and surge protection applications.
Uncontrolled breakdown can cause local heating, defect generation, and permanent failure.

## Shockley Diode Equation

The ideal current-voltage relation is commonly written I = Is(exp(V/(n Vt)) - 1).
Is is the reverse saturation current and Vt = kT/q is the thermal voltage.
At 300 K, Vt is about 25.9 millivolts.
The ideality factor n accounts for deviations from the simplest diffusion-current model and is often between one and two.
An ideality factor near one suggests diffusion-dominated current in the neutral regions.
An ideality factor near two often indicates significant recombination in the depletion region.
The equation is most useful for moderate forward bias and simple device modeling.
It does not fully describe high-level injection, series resistance, breakdown, self-heating, tunneling, or transient charge storage.
Temperature strongly affects Is, so diode voltage at a fixed current usually decreases as temperature rises.
This temperature dependence is useful for sensing but can create thermal-runaway concerns in power devices.

## Capacitance and Transient Behavior

A reverse-biased p-n junction behaves like a voltage-dependent capacitor because the depletion region separates fixed charges.
Increasing reverse bias widens the depletion region and usually lowers junction capacitance.
This property is exploited in varactor diodes for tuning radio-frequency circuits.
Forward-biased junctions exhibit diffusion capacitance because injected minority carriers are stored near the junction.
When a diode switches from forward to reverse bias, this stored charge must be removed before the diode blocks effectively.
The reverse-recovery effect matters in rectifiers, switching power supplies, motor drives, and radio-frequency circuits.
Fast-recovery diodes, Schottky diodes, and wide-bandgap devices are chosen when switching loss or recovery noise is critical.
Small-signal diode models include dynamic resistance, junction capacitance, diffusion capacitance, and sometimes package parasitics.
At high frequency, the physical package and contacts can matter as much as the ideal junction physics.
Transient behavior is therefore a device-level consequence of carrier transport and geometry.

## Optoelectronic Junctions

A solar cell is a p-n junction designed to separate photogenerated carriers before they recombine.
Light creates electron-hole pairs, and the built-in electric field helps collect them as electrical current.
A photodiode uses a similar principle but is optimized for detection speed, sensitivity, or wavelength range.
An LED is a forward-biased junction in which electron-hole recombination emits photons.
Efficient light emission requires a semiconductor with a suitable band gap and favorable radiative recombination pathways.
Direct-bandgap materials such as [[semiconductor-band-structure]] explains energy bands, band gaps, and carrier populations.
[[maxwell-equations-electromagnetism]] underlies the electrostatic field and potential in the depletion region.
Future pages on depletion regions and the Shockley diode equation could expand the space-charge and exponential-current details.
Related engineering pages include MOSFET, bipolar junction transistor, solar cell, LED, avalanche breakdown, and Schottky barrier.
The p-n junction is a compact example of how materials processing creates useful electrical nonlinearity.

## References

Research basis: Wikipedia articles on p-n junction, depletion region, diode, Shockley diode equation, and semiconductor, consulted 2026-05-02.
