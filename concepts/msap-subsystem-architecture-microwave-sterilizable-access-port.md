---
title: aseptic-specimen-transfer-space-environment-microwave-sterilizable-access-port Access Port MSAP Subsystem Architecture
aliases: [MSAP subsystem design, microwave sterilization access port architecture, NASA sterile access system design]
tags: [sterilization, microwave, NASA, spacecraft-biology, aseptic-transfer, engineering-design]
created: 2026-05-08
source: sterilizing-surfaces-by-irradiation-with-microwaves.md
---

# Microwave Sterilizable Access Port (MSAP) Subsystem Architecture

## Overview

The Microwave Sterilizable Access Port (MSAP) is a three-subsystem device developed at NASA's Lyndon B. Johnson Space Center (under contract MSC-22484) to solve a critical problem in space biology: how to aseptically transfer materials into and out of sterile or biologically sensitive systems without compromising their sterility. The MSAP uses [[dry-microwave-irradiation-spore-resistance]] to sterilize all mating surfaces before and after specimen transfer, addressing limitations of traditional sterilization methods in the space environment.

## The Problem Context

Space-based biological experiments and Environmental Control and Life Support Systems (ECLSS) require reliable aseptic access — the ability to add materials to, or remove samples from, sterile systems without introducing contamination. Traditional sterilization techniques proved inadequate for this application:

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
- **Rectangular waveguide** — Conducts the electromagnetic energy from the magnetron to the antenna assembly with minimal loss
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
- **Hospital and clinical settings** — Sterile access to isolation chambers and biologic containment
- **Food processing** — Aseptic sampling and addition in sterile food production
- **Biotechnology research** — Maintaining sterility during long-term cell culture and fermentation experiments

## Innovation and Novelty Assessment

The MSAP represents several innovations in the field of surface sterilization:

- **First use of microwave energy for surface sterilization** — Prior to this development, microwaves had been used for bulk sterilization of materials (food, medical waste) but not for targeted surface sterilization of mating interfaces
- **Trace water enhancement** — The use of 9 µL/cm² trace water to convert microwave energy into localized steam is a novel technique that dramatically improves spore kill rates
- **Closed-system capability** — The demonstrated ability of microwaves to penetrate [[microwave-penetration-through-elastomeric-materials-sterilization]] and sterilize fully enclosed systems is unprecedented in the sterilization field
- **Minimal thermal impact** — Unlike autoclaving, the microwave method achieves sterilization with minimal temperature rise in the surrounding system, making it suitable for thermally labile applications
- **No chemical residues** — Unlike chemical disinfectants, microwave sterilization leaves no chemical residues that could contaminate biological experiments or food products

## Engineering Challenges

Several engineering challenges had to be overcome in the MSAP development:

- **Uniform coverage** — Ensuring that microwave energy reaches all surfaces of complex mating geometries, including recessed areas and internal channels
- **Power control** — Delivering consistent 3.6 W/cm² exposure rates across varying surface areas and geometries
- **Material selection** — Choosing materials for the valve port and transfer assembly that are compatible with both the biological systems being accessed and the microwave sterilization process
- **Water management** — Precisely delivering the 9 µL/cm² trace water dose to the correct surfaces without over-wetting or under-wetting
- **Integration** — Integrating three subsystems into a compact, reliable, crew-operable device suitable for the space environment

## Historical Context and NASA Technology Transfer

The MSAP was developed under NASA's Technology Transfer Program, which aims to make aerospace-related developments available for wider technological, scientific, or commercial application. NASA Tech Briefs like MSC-22484 serve as the primary publication mechanism for these technologies, providing sufficient technical detail for potential licensees to evaluate and adapt the technology.

The development team consisted of three innovators based in Oregon: James E. Atwater (Technical Director), Neil D. Streech (Project Engineer), and Frank C. Garmon (Microbiologist). This team combined expertise in electrical engineering, microwave systems, and microbiology — an interdisciplinary approach that was essential for developing a device operating at the intersection of these fields.

## See Also

- [[msap-subsystem-architecture-microwave-sterilizable-access-port-design]]

- [[microwave-sterilizable-access-port-nasa-space-biology]] — Detailed MSAP overview
- [[microwave-sterilization-system-hardware-architecture]] — Hardware component details
- [[coaxial-power-splitter-waveguide-microwave-sterilization]] — Microwave delivery system
- [[eclss-environmental-control-life-support]] — ECLSS context for MSAP development

## References

- Atwater JE, Streech ND, Garmon FC. Sterilizing Surfaces by Irradiation with Microwaves. NASA Tech Briefs MSC-22484. Lyndon B. Johnson Space Center, Houston, Texas.
