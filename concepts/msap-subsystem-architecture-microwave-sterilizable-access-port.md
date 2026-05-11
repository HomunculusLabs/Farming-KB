---
title: Msap Subsystem Architecture Microwave Sterilizable Access Port
aliases: [MSAP subsystem design, [[coaxial-power-splitter-waveguide-microwave-sterilization]] access port architecture, NASA sterile access system design]
tags: [sterilization, microwave, NASA, spacecraft-biology, aseptic-transfer, engineering-design]
created: 2026-05-08
source: sterilizing-surfaces-by-irradiation-with-microwaves.md
---

# Microwave Sterilizable Access Port (MSAP) Subsystem Architecture

## Overview

The Microwave Sterilizable Access Port (MSAP) is a three-subsystem device developed at NASA's Lyndon B. Johnson Space Center (under contract MSC-22484) to solve a critical problem in space biology: how to aseptically transfer materials into and out of sterile or biologically sensitive systems without compromising their sterility. The MSAP uses [[dry-microwave-irradiation-spore-resistance]] to sterilize all mating surfaces before and after [[aseptic-specimen-transfer-space-environment-microwave-sterilizable-access-port]], addressing limitations of traditional sterilization methods in the space environment.

## The Problem Context

Space-based biological experiments [[fruiting-chamber-design-and-environmental-control]] and Life Support Systems (ECLSS) require reliable aseptic access — the ability to add materials to, or remove samples from, sterile systems without introducing contamination. Traditional [[mushroom-agar-media-pouring-sterilization-techniques]] proved inadequate for this application:

- **Autoclaving** — Requires high temperatures (121°C+) that cause excessive thermal impact on sensitive biological systems and flight hardware
- **Gamma irradiation** — Effective but requires large, heavy equipment unsuitable for spacecraft; also poses radiation exposure risks to crew
- **Chemical disinfection** — Introduces chemical contaminants (ethylene oxide, alcohol, [[cervantes-hydrogen-peroxide-sterilization]]) into closed biological systems, potentially interfering with experiments
- **UV irradiation** — Cannot sterilize complex surface geometries or surfaces within enclosed systems due to line-of-sight limitations

## Three-Subsystem Architecture

The MSAP consists of three integrated subsystems, each serving a specific function in the aseptic transfer process:

### Subsystem 1: In-Line Valve Port Assembly

The valve port assembly is the structural interface between the sterile system and the external environment. It serves as the physical connection point through which specimen transfer occurs. Key design requirements include:

- **Sealing integrity** — Must maintain a hermetic seal under the pressure differentials encountered in spacecraft environments
- **Material compatibility** — Must be constructed from materials that can withstand repeated [[microbial-kill-curve-microwave-exposure-dose-response]] without degradation
- **Microwave transparency** — The mating surfaces must be accessible to microwave energy, either directly or through microwave-transparent materials
- **Mechanical reliability** — Must function reliably through multiple sterilization and transfer cycles without mechanical failure

The valve port is designed to be permanently installed on the sterile system, providing a standardized access point that can be mated with the transfer assembly for each specimen transfer operation.

### Subsystem 2: Portable Microwave Sterilization Chamber

The microwave sterilization chamber is the core sterilization subsystem. It generates and delivers microwave energy to the mating surfaces of the valve port and transfer assembly. Based on the experimental data in the NASA Tech Brief, the chamber system consists of:

- **Power supply** — Provides regulated electrical power to the microwave generation components
- **Magnetron oscillator** — Generates 2.45 GHz microwave radiation, the standard frequency used in commercial microwave ovens and chosen for its optimal coupling with water molecules
- **[[rectangular-waveguide-dipole-antenna-microwave-surface-sterilization]]** — Conducts the electromagnetic energy from the magnetron to the antenna assembly with minimal loss
- **Waveguide-to-coaxial adapter** — Transitions the waveguide output to a coaxial format suitable for powering multiple antennas
- **Coaxial power splitter** — Distributes the microwave power to multiple dipole antennas for uniform coverage
- **Dipole antennas** — One or more antennas that radiate microwave energy toward the surfaces to be sterilized

The sterilization chamber is designed to be portable, allowing it to be moved between different access ports on a spacecraft as needed. This portability is essential for efficient use of limited spacecraft mass and volume resources.

### Subsystem 3: Specimen Transfer Assembly

The specimen transfer assembly is the removable component that carries materials to be introduced into or extracted from the sterile system. It mates with the valve port assembly and must be sterilized on both its external mating surfaces and any internal surfaces that will contact the sterile system. Design considerations include:

- **Mating surface geometry** — Must create a reliable seal with the valve port while allowing microwave penetration to all contaminated surfaces
- **Specimen containment** — Must securely hold the specimen during transfer without contamination
- **Single-use vs. reusable design** — May be designed for single use (to minimize cross-contamination risk) or repeated use with sterilization between transfers
- **Material selection** — Must be compatible with both the specimen material and the microwave sterilization process

## Microwave Energy Delivery System

The experimental sterilization system described in the Tech Brief uses a specific [[microwave-sterilization-system-hardware-architecture-power-waveguide-antenna]] for microwave energy delivery:

1. **Power supply** provides electrical power to the system
2. **Magnetron oscillator** converts electrical energy to 2.45 GHz microwave radiation
3. **Rectangular waveguide** channels the microwave energy from the magnetron
4. **Waveguide-to-coaxial adapter** transitions the waveguide mode to a coaxial transmission line
5. **Coaxial power splitter** divides the microwave power among multiple output paths
6. **Dipole antennas** radiate the microwave energy toward the target surfaces

This architecture allows the microwave energy to be distributed across multiple antennas, ensuring uniform coverage of complex surface geometries. The use of dipole antennas rather than a single waveguide aperture provides more flexible radiation pattern control.

## Sterilization Protocol

The MSAP sterilization protocol involves the following sequence:

1. The specimen transfer assembly is positioned against the valve port
2. Trace water (approximately 9 µL per cm² of surface) is introduced to the mating surfaces
3. Microwave energy is applied at 3.6 W/cm² exposure rate
4. Total exposure of 13.1 W-hr is delivered to achieve complete sterilization
5. The water flashes to steam, contacting all exposed surfaces and destroying microorganisms
6. After sterilization, the valve is opened and specimen transfer proceeds
7. After transfer, the valve is closed and the mating surfaces are re-sterilized before disconnection

## Applications Beyond Space Biology

While developed for NASA's space biology program, the MSAP concept has potential applications in terrestrial settings:

- **Pharmaceutical manufacturing** — Aseptic transfer in sterile production environments
