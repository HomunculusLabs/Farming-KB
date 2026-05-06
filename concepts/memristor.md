---
title: "Memristor"
created: 2026-04-28
updated: 2026-05-06
sources: []
type: concept
tags: [reference]
---

# Memristor
## Overview
A memristor is an electrical circuit element whose resistance depends on the history of current or voltage that has passed through it.
The name combines memory and resistor, emphasizing that the device can retain a conductance state after power is removed.

In ideal circuit theory, the memristor relates electric charge to magnetic flux linkage, complementing the resistor, capacitor, and inductor.

In practical engineering, the term usually refers to two-terminal resistive switching devices made from oxides, chalcogenides, polymers, or nanoscale filaments.

Memristive behavior matters because it blurs the boundary between storage and computation.

A device can both encode information and participate directly in analog computation through its conductance.

This makes memristors important in non-volatile memory, neuromorphic computing, and in-memory accelerator architectures.
They are also studied as physical models of synaptic plasticity because conductance can change gradually with repeated stimulation.

The concept is simple at the circuit level, but the materials science is diverse and often difficult.

Different devices called memristors may rely on ion migration, phase change, redox reactions, ferroelectric polarization, or spintronic effects.

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

## History and context
The theoretical memristor was proposed by Leon Chua in 1971 as a missing basic circuit element.

Chua argued that symmetry in circuit variables implied a relation between charge and flux analogous to the known resistor, capacitor, and inductor relations.
For decades, the idea remained largely mathematical and had limited technological impact.

Related resistive switching phenomena were observed earlier in thin films, but they were not always interpreted through memristor theory.

Interest surged in 2008 when researchers at Hewlett-Packard reported nanoscale titanium dioxide devices described as physical memristors.

The report connected older switching observations to a compact theoretical framework and to possible memory applications.

It also triggered debate about whether real devices should be called ideal memristors or more broadly memristive systems.

This debate is partly semantic and partly technical.

Ideal memristors obey strict mathematical relationships that many real materials do not satisfy exactly.
Engineers often use the term pragmatically for resistive switching elements with memory.

The development of memristors overlaps with the search for post-CMOS memory technologies.

Flash memory scaling limits, data-center energy costs, and artificial intelligence workloads all increased interest in non-volatile, dense, low-energy devices.

At the same time, machine learning created demand for hardware that can multiply matrices efficiently.

Crossbar arrays of programmable conductances appeared attractive because Ohm's law and Kirchhoff's law can perform multiply-accumulate operations in parallel.

The field therefore sits at the intersection of semiconductor fabrication, materials science, and computational neuroscience.
## Applications and significance
The most direct application is non-volatile memory.

Resistive memory can in principle be fast, dense, and compatible with back-end-of-line integration above CMOS logic.

Some commercial embedded memory products use related resistive switching technologies.

Another major application is in-memory computing.

A crossbar array can store matrix weights as conductances and process vector inputs as voltages.

The resulting currents represent analog sums, reducing data movement between memory and processor.

This approach is promising for energy-efficient inference but faces precision, noise, drift, and calibration challenges.
Memristors are also explored for neuromorphic systems.

Their history-dependent conductance resembles synaptic weight adaptation in simplified neural models.

Pulse timing, pulse amplitude, and pulse repetition can implement plasticity rules such as potentiation and depression.

However, biological synapses are biochemical systems, so the analogy should not be pushed too literally.

Security applications include physically unclonable functions because device variability can provide unique fingerprints.

Analog signal processing, adaptive filters, and reconfigurable circuits are additional research directions.
Scientific significance comes from the way memristors force circuit theory to include memory at the component level.

They also make material defects, ions, and interfaces central to computation rather than merely sources of failure.

The main unresolved question is not whether resistive switching exists, but where it can outperform mature alternatives at scale.

Success depends on integration, reliability, architecture, and software as much as on the individual device.

## Related concepts
non-volatile memory

neuromorphic computing

semiconductor fabrication
materials science

machine learning

analog computing

spintronics

phase-change memory

ferroelectricity

nanotechnology
- [[slime-mold-computation]]
- [[biological-memory-non-neural]]
- [[unconventional-computing]]
