---
title: Msap Subsystem Architecture Microwave Sterilizable Access Port Design
tags: [mycology, sterilization, microwave, NASA, space-biology, ECLSS, access-port, aseptic-transfer, closed-system]
created: 2026-05-09
source: sterilizing-surfaces-by-irradiation-with-microwaves.md
---

# Microwave Sterilizable Access Port (MSAP) Subsystem Architecture

## Overview

The Microwave Sterilizable Access Port (MSAP) was conceived by NASA
researchers at the Lyndon B. Johnson Space Center as a solution to a
persistent problem in space biology: how to aseptically add or remove
materials from closed sterile systems. The MSAP consists of three
integrated subsystems that together enable contamination-free specimen
transfer in environments where traditional [[comparison-of-surface-sterilization-methods]] are
impractical.

## The Problem: Aseptic Access in Closed Systems

[[space-station-closed-system-aseptic-access-sterilization]] [[chen-maitake-growth-parameters-environmental-control]] and life support systems (ECLSS)
and enclosed flight experiments maintain biological sterility as a
fundamental requirement. However, the practical need to add nutrients,
remove samples, or introduce new organisms creates a contamination risk
at every access point. Traditional sterilization methods fail in this
context:

- **Autoclaving**: Too much thermal impact on adjacent sensitive
  biological systems and electronic components.
- **Gamma irradiation**: Cannot be applied locally to mating fixtures
  without irradiating the entire experiment.
- **Chemical disinfection**: Introduces chemical contaminants into
  closed biological systems. Ethylene oxide, alcohols, and other
  disinfectants leave residues that are unacceptable in space biology.

The MSAP was designed to solve this access problem using microwave
energy, which provides rapid, dry, residue-free sterilization of the
mating surfaces immediately before and after each transfer event.

## Subsystem 1: In-Line Valve Port Assembly

The valve port assembly is the physical interface between the sterile
internal system and the external environment. It functions as the door
through which specimens and materials pass. Key design requirements:

- **Seal integrity**: Must maintain a hermetic seal during non-access
  periods to prevent contamination of the enclosed system.
- **Microwave transparency**: The mating surfaces of the valve must be
  made from materials that allow 2.45 GHz microwave energy to pass
  through to the contamination zone, or must be designed so that
  microwave energy reaches all critical surfaces through the
  sterilization chamber.

- **Complex geometry accommodation**: Real valve ports have threads,
  O-rings, and crevices where organisms can hide. The sterilization
  system must reach all of these surfaces.

- **Reusable**: Unlike single-use sterile connectors, the MSAP valve
  is designed for repeated sterilization cycles throughout a mission.

## Subsystem 2: Portable Microwave Sterilization Chamber

The sterilization chamber is the core innovation of the MSAP concept.
It is a portable unit that can be positioned over the valve port for
sterilization cycles. Its architecture includes:

- **[[magnetron-oscillator-microwave-sterilization]]**: The microwave source, generating 2.45 GHz
  radiation at controlled power output.
- **Power supply**: Provides regulated electrical power to the
  magnetron.
- **Waveguide system**: Conducts microwave energy from the magnetron to
  the [[dipole-antenna-array-configuration-microwave-surface-sterilization]], using rectangular waveguides and coaxial adapters.
- **[[coaxial-power-splitter-waveguide-microwave-sterilization]]**: Divides the microwave power among
  multiple antennas for uniform coverage of the target surfaces.
- **Antenna array**: Multiple dipole antennas arranged to irradiate all
  mating surfaces of the valve port from different angles, ensuring no
  shadow zones where organisms could survive.

The portable nature of the chamber means it can be shared among multiple
access ports on a space station, reducing the mass and volume
requirements compared to integrating a sterilization system into each
port individually.

## Subsystem 3: Specimen Transfer Assembly

The transfer assembly is the physical mechanism for moving specimens
through the sterilized valve port. It must:

- **Minimize recontamination**: After sterilization, the transfer
