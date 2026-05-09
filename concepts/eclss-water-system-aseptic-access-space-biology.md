---
title: "ECLSS Water System Aseptic Access for Space Biology"
tags:
  - eclss
  - space-biology
  - aseptic-access
  - nasa-msap
  - water-systems
  - spacecraft
  - sterilization|sterilization
  - specimen-transfer
  - contamination-control
source:
  - NASA Tech Brief MSC-22484
  - Lyndon B. Johnson Space Center, Houston, Texas
  - Innovators: James E. Atwater, Neil D. Streech, Frank C. Garmon
---

# ECLSS Water System Aseptic Access for Space Biology

## Overview

The Environmental Control and Life Support System (ECLSS) aboard spacecraft provides
crew with breathable air, potable water, and temperature regulation. Maintaining
sterile integrity within ECLSS water recovery and distribution systems is critical
for crew health and the validity of space biology experiments that depend on
controlled, contaminant-free water supplies. The NASA [[msap-subsystem-architecture-microwave-sterilizable-access-port]] Access
Port (MSAP) was developed at the Lyndon B. Johnson Space Center specifically to
solve the problem of aseptic access to biologically sensitive ECLSS water systems
and flight experiments, enabling sample removal and material addition without
introducing microbial contamination.

## The ECLSS Water System Contamination Problem

ECLSS water systems operate as closed-loop recovery and distribution networks that
recycle wastewater, humidity condensate, and other moisture sources into potable
water. This architecture creates several contamination vulnerabilities:

- **Extensive internal surface area**: Miles of tubing, fittings, valves, and
  reservoir walls provide surface area for microbial colonization, particularly at
  joints, bends, and low-flow sections where biofilm accumulates.
- **Mating fixture interfaces**: Every connection represents a potential contamination
  pathway. Opening a port for sampling or nutrient addition exposes the sterile
  interior to ambient organisms carried on fixture surfaces.
- **Nutrient availability**: Trace organic compounds in recycled water support
  microbial growth, particularly for opportunistic organisms such as _Pseudomonas
  cepacia_, _Escherichia coli_, and other environmental bacteria.
- **Microgravity effects**: Reduced sedimentation and convection alter biofilm
  formation dynamics and [[edaphic-factors-microbial-community-structure]] structure in ways that complicate
  disinfection strategies developed from terrestrial experience.

## The Aseptic Access Challenge

The fundamental operational challenge is enabling two types of interactions with
sterile water systems without compromising microbial integrity:

1. **Aseptic sample removal**: Withdrawing water or biological specimens from a
   sealed sterile system for analysis, requiring external sampling hardware and
   its interface to be sterile at the moment of connection.
2. **Aseptic material addition**: Introducing nutrients, reagents, experimental
   organisms, or other materials into a sterile system without carrying organisms
   across the system boundary.

Both operations require mating surfaces of access ports, valves, and transfer
fixtures to be sterilized immediately before and after each connection event.

## Why Traditional Sterilization Fails

Conventional methods cannot adequately address aseptic access for ECLSS mating
fixtures and complex geometries:

- **Autoclaving is destructive**: The 121°C saturated steam requirement causes
  thermal expansion and degradation of polymers, elastomers, and seals in fluid
  fittings. Repeated cycles compromise O-rings and gaskets. Autoclaving also
  requires removing components from the system, defeating in-situ access.
- **Gamma irradiation is impractical**: Irradiation facilities are unavailable
  in-space, and ionizing radiation degrades polymers and embrittles elastomers in
  assembled system interfaces containing sensitive materials.
- **UV light cannot reach shadowed surfaces**: Mating fixture interfaces contain
  crevices, O-ring grooves, threads, and interior surfaces shielded from UV
  radiation, where organisms survive treatment and contaminate upon connection.
- **Chemical disinfectants leave residues**: Ethylene oxide, alcohols, quaternary
  amines, [[cervantes-hydrogen-peroxide-sterilization]], and elemental iodine all leave chemical residues that
  contaminate water supplies, affect crew health, and invalidate experimental
  outcomes. EtO additionally requires extensive aeration and poses flammability
  hazards incompatible with spacecraft environments.

## The MSAP Three-Subsystem Solution

The [[microwave-sterilizable-access-port-nasa-space-biology|Microwave Sterilizable Access Port]] addresses these limitations through an
integrated three-subsystem architecture using 2.45 GHz [[challenge-microorganisms-microwave-surface-sterilization]]
sterilization:

### Subsystem 1: In-Line Valve Port

A permanently installed component within the ECLSS water system or flight
experiment hardware, providing a standardized sterile interface for external
connection. The valve port incorporates mechanisms that seal the system interior
when no external device is attached. It minimizes dead volumes, eliminates
crevice geometries that harbor organisms, and provides smooth mating surfaces
compatible with microwave sterilization.

### Subsystem 2: Portable Microwave Chamber

The sterilization apparatus that treats external mating surfaces of the valve
port and [[aseptic-specimen-transfer-space-environment-microwave-sterilizable-access-port]] assembly before and after each connection. The chamber
delivers 2.45 GHz microwave energy at 3.6 W/cm² effective intensity through
waveguide components, coaxial adapters, power splitters, and dipole antennas.
Trace water delivery (~9 µL/cm²) enables microwave energy coupling. The total
cycle delivers 13.1 W-hr accumulated energy, providing margin beyond demonstrated
kill thresholds of ~4 W-hr for 10⁶ reduction and ~8 W-hr for 10⁸ reduction.

### Subsystem 3: Specimen Transfer Assembly

External hardware that connects to the in-line valve port through the microwave
chamber for sample removal or material addition. Designed for microwave chamber
compatibility with features that minimize surface complexity and eliminate shadow
zones. Provides the mechanical interface for fluid transfer, sample containment,
and reagent delivery while maintaining aseptic integrity throughout the cycle.

## Operational Sequence

1. Specimen transfer assembly is positioned at the microwave chamber and
   sterilized by [[microbial-kill-curve-microwave-exposure-dose-response]] to eliminate organisms on mating surfaces.
2. Microwave chamber is positioned over the in-line valve port, and external
   valve port surfaces are sterilized by microwave exposure.
3. With both interfaces verified sterile, the transfer assembly engages the
   valve port through the chamber, establishing a sealed fluid connection.
4. The desired operation (sample removal or material addition) is performed.
5. The connection is disengaged, and both mating surfaces are re-sterilized
   before the chamber is removed and the valve port resealed.

This sequence ensures no contaminated surface contacts the sterile system interior.

## Relevance Beyond Spacecraft

The MSAP concept applies to any setting requiring aseptic access to closed sterile
fluid systems: controlled environment agriculture (aseptic nutrient delivery in
hydroponic/aeroponic systems), biopharmaceutical manufacturing (validated aseptic
connections without chemical residues), mycological research (axenic fungal culture
maintenance and [[spore|spore]] transfer), and clinical settings where sterile fluid systems
must be accessed without thermal or chemical damage to connected instrumentation.
## See Also
- [[space-station-closed-system-aseptic-access-sterilization]]
