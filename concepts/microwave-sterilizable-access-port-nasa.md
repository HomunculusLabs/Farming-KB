---
title: Microwave Sterilizable Access Port Nasa
concept_category: Aerospace Sterilization
related_concepts:
  - microwave-surface-sterilization
  - contamination-control-mycology
source: sterilizing-surfaces-by-irradiation-with-microwaves.md
created: 2026-05-10
---

# Microwave Sterilizable Access Port (MSAP)

## Overview

The Microwave Sterilizable Access Port (MSAP) is a three-subsystem device developed at NASA's Lyndon B. Johnson Space Center under document MSC-22484. It was designed to solve a fundamental problem in spaceflight biology: how to aseptically add or remove materials from sterile systems without introducing contamination. The MSAP uses [[dry-microwave-irradiation-spore-resistance]] to sterilize all mating surfaces before and after specimen transfer, eliminating the need for chemical disinfectants, autoclaving, or other traditional methods that are impractical in spacecraft environments.

## The Spaceflight Sterilization Challenge

### The Core Problem

Spacecraft carry biologically sensitive systems that must remain sterile, including:

- **ECLSS ([[chen-maitake-growth-parameters-environmental-control]] and [[eclss-environmental-control-life-support]] System) waters** — recycled water for crew consumption and hygiene
- **Flight experiments** — biological experiments requiring contamination-free conditions
- **Sample return containers** — planetary protection protocols demand sterility

The ability to aseptically remove samples and products, or add materials to these sterile systems, has always been compromised by the lack of a reliable means of sterilizing the mating fixtures — the physical connections through which materials pass.

### Why Traditional Methods Fail in Space

| Method | Spaceflight Limitation |
|--------|----------------------|
| Autoclaving | Excessive thermal impact on vulnerable spacecraft systems |
| Gamma irradiation | Requires heavy shielding, damages sensitive electronics |
| Ethylene oxide | Toxic [[surface-sterilization-methods-comparison-complex-geometries-thermal-chemical-residue]] incompatible with closed environments |
| UV light | Cannot reach shadowed surfaces in complex geometries |
| Alcohols/peroxides | Flammable, leave residues, limited [[ingham-aact-holding-time-shelf-life-decay]] in microgravity |

Spacecraft need a [[pf-tek-alcohol-flaming-sterilization-method]] that is:
- Non-chemical (no residues in closed-loop life support)
- Low thermal impact (protect adjacent electronics and fluids)
- Capable of complex geometries (reaches all mating surfaces)
- Rapid (minimizes crew time and EVA requirements)
- Reliable (consistent kill across diverse microbial populations)

## MSAP System Architecture

The MSAP consists of three integrated subsystems:

### Subsystem 1: In-Line Valve Port Assembly

The valve port assembly is the physical interface through which materials pass between the sterile system and the external environment. Key [[mycoremediation-bioreactor-design-considerations]]:

- Provides a sealable connection point
- Must survive repeated sterilization cycles
- Constructed from materials with controlled microwave interaction (reflective or transparent as needed)
- Geometry designed to expose all mating surfaces to microwave energy

### Subsystem 2: Portable Microwave Sterilization Chamber

The sterilization chamber delivers microwave energy to the valve port surfaces. Design elements include:

- **Microwave-reflective materials**: Used to contain and direct energy within the chamber
- **Microwave-transparent materials**: Allow energy to reach target surfaces
- **Controlled radiation patterns**: Antenna placement and waveguide design ensure uniform coverage
- **Subsystem geometry**: Chamber shape is optimized so all desired surfaces receive sufficient exposure

The portability of the chamber means it can be moved between different access points on the spacecraft, sterilizing each as needed.

### Subsystem 3: Specimen Transfer Assembly

The transfer assembly provides the mechanical means to move materials through the sterilized port:

- Allows controlled introduction or extraction of specimens
- Maintains sterility during the transfer process
- Interfaces with both the sterile internal system and the external environment
- Designed for minimal surface complexity to facilitate sterilization

## Operational Sequence

A typical MSAP use cycle follows these steps:

1. **Pre-transfer sterilization**: The portable microwave chamber is positioned over the valve port. Microwave energy sterilizes all mating surfaces of both the port and the transfer assembly.
2. **Connection**: The transfer assembly mates with the now-sterile valve port.
3. **Specimen transfer**: Materials are moved through the port under [[psilocybe-cubensis-strain-potency-variability-controlled-conditions-bigwood-beug]].
4. **Disconnection**: The transfer assembly is separated from the port.
5. **Post-transfer sterilization**: The port surfaces are sterilized again to address any contamination introduced during the transfer process.

## Microwave Energy Design
