---
title: "memristor"
created: 2026-04-28
updated: 2026-05-06
sources:
  - "raw/papers/permaculture-a-designers-manual-bill-mollison.md"
type: concept
tags: [reference]
---
# Memristor
## Overview
A memristor is an electrical circuit element whose resistance depends on the history of current or voltage that has passed through it.
The name combines [[plant-memory-and-learning-mechanisms|memory]] and resistor, emphasizing that the device can retain a conductance state after power is removed.

In ideal circuit theory, the memristor relates electric charge to magnetic flux linkage, complementing the resistor, capacitor, and inductor.

In practical engineering, the term usually refers to two-terminal resistive switching devices made from oxides, chalcogenides, polymers, or nanoscale filaments.

Memristive behavior matters because it blurs the boundary between storage and computation.

A device can both encode information and participate directly in analog computation through its conductance.

This makes memristors important in non-volatile memory, neuromorphic computing, and in-memory accelerator architectures.
They are also studied as physical models of synaptic plasticity because conductance can change gradually with repeated stimulation.

The concept is simple at the circuit level, but the materials science is diverse and often difficult.

Different devices called memristors may rely on ion migration, [[phase-change-materials-thermal-energy-storage]], redox reactions, ferroelectric polarization, or spintronic effects.

For this reason, memristor is best understood as both a theoretical element and a family of technologies.

## Key aspects
The defining feature of a memristive system is state dependence.

A voltage pulse can increase or decrease conductance, and the new conductance persists for some retention time.

The device response often shows a pinched hysteresis loop in a current-voltage plot.
At high frequency, the hysteresis may shrink because the internal state cannot follow the external signal.

Many practical memristors are resistive random-access memory cells, often abbreviated ReRAM or RRAM.

A common structure is a metal-insulator-metal stack only nanometers thick.

Switching may occur when a conductive filament forms, ruptures, widens, or narrows inside the insulating layer.

Filamentary switching can produce large on-off ratios but also variability from cycle to cycle.

Interface-type devices change resistance more uniformly across an electrode boundary.
They may provide smoother analog updates but may have lower contrast or different endurance limits.

Important performance measures include switching voltage, write energy, retention, endurance, speed, variability, and scalability.

Retention describes how long the conductance state survives without refresh.

Endurance describes how many write cycles the device can tolerate before failure or drift becomes unacceptable.

Analog memristors are evaluated by linearity, symmetry, dynamic range, and number of stable conductance levels.

Digital memory applications usually prefer abrupt, reproducible switching between high and low resistance states.

Computing applications may prefer many intermediate states and predictable incremental updates.
Sneak-path currents are a major challenge in dense crossbar arrays.

Selector devices, nonlinear switching, and architectural constraints are used to reduce unwanted current paths.

Thermal effects are also important because nanoscale switching can localize heat in very small volumes.

Device-to-device variation is not just a manufacturing problem; it is part of the physical nature of many switching mechanisms.

## History [[slime-mold-computation]]

## See Also
- [[plant-memory-environmental-learning]]
- [[plant-memory-and-associative-learning]]
## Practical Considerations

Successful implementation of memristor requires attention to
several practical factors including environmental conditions,
resource availability, and timing. Careful monitoring and
adaptive management help optimize outcomes across varying
conditions. Integration with other system elements enhances
overall effectiveness and creates beneficial synergies that
improve resilience and productivity over time.

## Future Directions

Continued development in this area promises new insights and
improved approaches for both research and practical application.
Cross-disciplinary collaboration and advances in analytical
methods create opportunities for innovation and refinement.
Recommended resources include current literature, practitioner
communities, and systematic experimentation to build expertise.
