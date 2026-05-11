---
title: [[aseptic-specimen-transfer-space-environment-microwave-sterilizable-access-port]] Port
aliases: [MSAP, microwave access port, aseptic transfer port, spacecraft sterile access]
tags: [sterilization, microwaves, aerospace, contamination-control, ECLSS, mycology]
created: 2026-05-10
source: sterilizing-surfaces-by-irradiation-with-microwaves.md
---

# Microwave Sterilizable Access Port (MSAP)

The Microwave Sterilizable Access Port (MSAP) is a three-subsystem device designed to provide aseptic (sterile) access to closed biological systems. Developed at NASA's Lyndon B. Johnson Space Center under the designation MSC-22484, the MSAP was conceived to solve a persistent problem in spacecraft operations: the inability to reliably sterilize mating fixtures when accessing biologically sensitive systems such as [[chen-maitake-growth-parameters-environmental-control]] and [[eclss-environmental-control-life-support]] Systems (ECLSS) waters and flight experiments.

## Problem Statement

In spacecraft and controlled biological environments, there is a recurring need to:

- Aseptically remove samples from sterile or susceptible systems
- Add materials (nutrients, reagents, specimens) without introducing contamination
- Maintain sterility of closed systems across multiple access events

Traditional [[comparison-of-surface-sterilization-methods]] are inadequate for this purpose. Autoclaving applies too much [[phase-change-materials-thermal-energy-storage]] to heat-vulnerable systems. Gamma irradiation requires specialized facilities and can degrade sensitive materials. Chemical disinfectants (ethylene oxide, [[cervantes-hydrogen-peroxide-sterilization]], alcohols, quaternary amines, iodine) leave residues that contaminate the system being accessed. UV light cannot reach all surfaces of complex mating fixtures.

## MSAP Architecture

The MSAP consists of three integrated subsystems, each serving a distinct function in the aseptic transfer process:

### 1. In-Line Valve Port Assembly

The valve port is the permanent interface mounted on the closed system being accessed. It provides:

- A sealed connection point that integrates with the biological system
- Mating surfaces designed for microwave-transparent construction
- Valve mechanism to isolate the system when the transfer assembly is disconnected
- Compatibility with the [[coaxial-power-splitter-waveguide-microwave-sterilization]] chamber geometry

The valve port remains in place on the system at all times. Its mating surfaces are the critical [[fungicide-treated-seed-contamination-risk-mushroom-substrate]] points that must be sterilized before and after each transfer event.

### 2. Portable Microwave Sterilization Chamber

The sterilization chamber is a detachable unit that:

- Encloses the valve port's mating surfaces during the sterilization cycle
- Contains the microwave generation and delivery apparatus (magnetron, waveguide, antennas)
- Provides controlled [[microbial-kill-curve-microwave-exposure-dose-response]] at 2.45 GHz, 3.6 W/cm², for the full 13.1 W-hr protocol
- Includes the trace water introduction system for spore-level sterilization
- Is portable, allowing a single chamber to service multiple access ports on different systems

The chamber's interior geometry is designed using microwave-reflective and microwave-transparent materials to ensure all mating surfaces receive adequate irradiation. Control of radiation patterns and subsystem geometries guarantees sufficient exposure of all desired surfaces without hot spots or shadowed areas.

### 3. Specimen Transfer Assembly

The transfer assembly is the removable component that:

- Connects to the sterilized valve port after the microwave cycle completes
- Provides a sealed conduit for moving materials in or out of the system
- Is designed so that its own mating surfaces are also exposed to microwave sterilization while docked in the chamber
- Allows physical transfer of samples, nutrients, or other materials through the aseptic barrier

## Operating Sequence

A complete MSAP access cycle follows these steps:

1. **Docking**: The sterilization chamber is connected to the in-line valve port assembly, enclosing the mating surfaces of both components.
2. **Trace water application**: A thin film of water (~9 µL/cm²) is applied to all surfaces requiring sterilization.
3. **Microwave sterilization cycle**: The chamber delivers 13.1 W-hr of 2.45 GHz microwave energy at 3.6 W/cm². This destroys all viable bacteria, yeasts, molds, and spores on the exposed mating surfaces.
4. **Chamber removal**: After the cycle completes, the sterilization chamber is detached, leaving the valve port mating surfaces sterile.
5. **Transfer assembly connection**: The specimen transfer assembly is connected to the now-sterile valve port.
6. **Material transfer**: Samples or materials are passed through the assembly into or out of the closed system.
7. **Post-transfer sterilization**: The chamber is re-docked and a second microwave cycle sterilizes the mating surfaces again, restoring aseptic conditions.

## Design Principles

### Microwave-Reflective vs. Transparent Materials

A key innovation in the MSAP design is the strategic use of materials with different microwave interactions:

- **Microwave-reflective materials** (metals) are used to contain the microwave field within the sterilization zone, preventing energy loss and protecting external components
- **Microwave-transparent materials** (certain polymers, glass, ceramics) are used for the mating surfaces and barriers that must be penetrated by the sterilizing radiation

This combination allows microwaves to reach all contamination-vulnerable surfaces while preventing energy waste and ensuring operator safety.

### Radiation Pattern Control

The geometry of the chamber, antenna placement, and waveguide configuration are designed to produce uniform radiation coverage across all mating surfaces. Without careful pattern control, shadowed areas could harbor surviving microorganisms, compromising the sterility assurance level.

## Relevance to Mycology

While designed for aerospace applications, the MSAP concept is directly relevant to mycological research and cultivation:

- **[[duggar-flat-ridge-beds-and-spawn-transfer]]**: Aseptic transfer of grain spawn or mycelial culture between containers without contamination
