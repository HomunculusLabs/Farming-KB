---
title: "Quantum Error Correction"
created: 2026-04-28
updated: 2026-05-06
sources:
  - "raw/papers/terence-mckenna-food-of-the-gods.md"
type: concept
tags: [reference]
---

# Quantum Error Correction

## Overview

Quantum error correction is the [[microdosing-theory-and-practice]] of protecting quantum information from noise.

It is essential because quantum states are fragile and cannot be copied directly like classical bits.

A useful quantum computer must preserve superpositions and entanglement long enough to perform reliable computation.

Physical qubits suffer from decoherence, imperfect gates, measurement errors, leakage, and environmental coupling.

Quantum error correction encodes one logical qubit into many physical qubits.

The encoded system allows errors to be detected and corrected without measuring the stored quantum information itself.

This is possible because error syndromes reveal what kind of error occurred without revealing the encoded logical state.

The field combines [[quantum-mechanics-fundamentals]], information theory, algebra, computer science, and experimental engineering.

It is one of the main reasons scalable quantum computing is difficult.

It is also one of the main reasons scalable quantum computing is considered possible.

## Key Aspects

Classical error correction often relies on redundancy, such as repeating a bit several times.

Quantum information cannot be protected by simple copying because of the no-cloning theorem.

Instead, quantum codes distribute information nonlocally across entangled states.

A single physical error then changes detectable relationships among qubits rather than immediately destroying the logical qubit.

The three-qubit bit-flip code is an introductory example.

It protects against accidental X errors that exchange zero and one.

The three-qubit phase-flip code protects against Z errors that change relative phase.

Real quantum noise can be decomposed into combinations of Pauli errors.

This makes correction of bit flips and phase flips sufficient in many code models.

The Shor code uses nine physical qubits to protect against arbitrary single-qubit errors.

The Steane code uses seven qubits and has deep links to classical Hamming codes.

Stabilizer codes describe valid code states as simultaneous eigenstates of commuting operators.

Measuring stabilizers yields a syndrome that indicates likely errors.

The syndrome does not identify the logical state, preserving quantum information.

A decoder interprets syndrome data and chooses a correction or tracking update.

Corrections are often handled in software as changes to a Pauli frame.

[[byzantine-fault-tolerance]] extends correction to the operations used during computation.

A fault-tolerant circuit prevents a small number of physical faults from spreading into an uncorrectable logical failure.

Threshold theorems state that arbitrarily long quantum computation is possible if physical error rates are below a threshold and resources are sufficient.

The threshold is not a single universal number.

It depends on the code, noise model, architecture, connectivity, measurement speed, and decoder.

The surface code is the leading architecture for many superconducting and trapped-ion roadmaps.

It arranges qubits on a two-dimensional lattice and uses local stabilizer measurements.

Its appeal comes from high thresholds and compatibility with nearest-neighbor hardware.

Its cost is a very large overhead in physical qubits.

Topological codes store information in global features that are resistant to local perturbations.

Subsystem codes reduce measurement complexity by introducing gauge degrees of freedom.
