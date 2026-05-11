---
title: "Microwave Sterilizable Access Port"
wikitarget: microwave-sterilizable-access-port
aliases: [MSAP, microwave access port, sterile access port, NASA access port]
created: 2026-05-11
source: sterilizing-surfaces-by-irradiation-with-microwaves.md
tags: [NASA, sterilization, space-technology, ECLSS, microwave, bioprocessing]
---

# Microwave Sterilizable Access Port

The Microwave Sterilizable Access Port (MSAP) is a three-subsystem device
designed by NASA to provide aseptic (sterile) access to biologically
sensitive closed systems. Developed at the Lyndon B. Johnson Space Center
and documented in NASA Tech Brief MSC-22484, the MSAP solves a fundamental
problem in spaceflight and bioprocessing: how to add materials to or remove
samples from sterile systems without introducing contamination. The device
uses [[dry-microwave-irradiation-spore-resistance]] to sterilize all mating surfaces before and after
specimen transfer, achieving sterility without the thermal damage or
chemical contamination associated with traditional methods.

## The Problem

Many biologically sensitive systems require absolute sterility, including:

- **Environmental Control and Life Support Systems (ECLSS)**: Water
  recycling and air revitalization systems on spacecraft that must remain
  free of microbial contamination
- **Space flight experiments**: Biological experiments conducted in the
  microgravity environment of spacecraft, where contamination would
  invalidate results
- **Bioprocessing equipment**: Fermenters, bioreactors, and pharmaceutical
  manufacturing systems that require aseptic sampling and feeding

The challenge is accessing these systems — adding nutrients, removing
samples, or introducing products — while maintaining sterility. Traditional
[[mushroom-agar-media-pouring-sterilization-techniques]] each have significant drawbacks:

- **Autoclaving**: Too much thermal impact on vulnerable systems
- **Gamma irradiation**: Not suitable for in-place sterilization of assembled
  systems
- **Chemical disinfection**: Introduces chemical contaminants that are
  unacceptable in closed biological systems
- **UV irradiation**: Cannot sterilize complex surface geometries or surfaces
  within enclosed assemblies

## MSAP Design: Three Subsystems

The MSAP concept consists of three integrated subsystems:

### 1. In-Line Valve Port Assembly
Permanently installed on the enclosed system, the valve port serves as the
sterile boundary. It incorporates microwave-transparent materials allowing
energy to reach mating surfaces. The valve opens only after the sterilization
cycle is complete and closes again before the next cycle.

### 2. Portable Microwave Sterilization Chamber
A portable unit that couples with the valve port for the sterilization cycle:

- **[[magnetron-oscillator-microwave-sterilization]]**: Generates 2.45 GHz radiation
- **Power supply**: Regulated power to the magnetron
- **Waveguide system**: Conducts energy via [[rectangular-waveguide-dipole-antenna-microwave-surface-sterilization]] and coaxial
  adapter
- **[[coaxial-power-splitter-waveguide-microwave-sterilization]]**: Divides energy for multiple dipole antennas
- **Dipole antennas**: Direct radiation onto all mating surfaces
- **Trace water system**: Introduces ~9 μL/cm² for enhanced spore kill

The chamber is portable — it can be moved between multiple access ports,
sterilizing each as needed.

### 3. Specimen Transfer Assembly
Provides the mechanical interface for moving materials through the sterilized
port: sample containers, mechanical coupling, seals maintaining sterility
during transfer, and a mechanism ensuring the pathway opens only after both
internal and external surfaces are sterilized.

## Operating Sequence

1. **Pre-sterilization**: The portable microwave chamber is coupled to the
   valve port assembly. Trace water is introduced to the mating surfaces
2. **Microwave cycle**: 2.45 GHz radiation at 3.6 W/cm² is applied for a
   total exposure of 13.1 W·hr, sterilizing all mating surfaces
3. **Valve opening**: After sterilization is confirmed, the valve is opened
   to create a sterile pathway
4. **Specimen transfer**: Material is passed through the sterile pathway
   using the specimen transfer assembly
5. **Valve closing**: The valve is closed after transfer is complete
6. **Post-sterilization**: A second microwave cycle sterilizes the external
   surfaces again before the chamber is decoupled

This two-cycle approach (sterilize before and after) ensures that
contamination is prevented at every step of the process.

## Materials Engineering

The MSAP requires careful selection of materials with specific electromagnetic
properties:

- **Microwave-transparent materials**: Used for the valve port body and
  seals, allowing microwaves to reach the mating surfaces from inside the
  chamber. PTFE (Teflon), polyethylene, and certain ceramics are candidates
- **Microwave-reflective materials**: Used to contain and direct the
  microwave energy within the treatment zone, preventing leakage
- **Radiation pattern control**: The geometry of the chamber and antenna
  placement is engineered to ensure that all mating surfaces receive
  sufficient exposure

The use of microwave-transparent materials is critical — it allows
microwaves to penetrate through the valve port body to sterilize surfaces
that would be inaccessible to UV light or chemical vapors.

## Applications Beyond Spaceflight

While developed for NASA spaceflight applications, the MSAP concept has
broader relevance:

- **Pharmaceutical manufacturing**: Aseptic sampling from bioreactors
- **Tissue engineering**: Sterile access to bioreactor-grown tissues
- **Cell culture**: Contamination-free media changes in sensitive cell
  culture systems
- **Food safety**: Sterile sampling from closed food processing systems
- **Laboratory automation**: Integration with robotic sample handling
  systems requiring sterile access

## Technical Specifications

Based on the NASA Tech Brief:

- **Frequency**: 2.45 GHz
- **Exposure rate**: 3.6 W/cm²
- **Total exposure**: 13.1 W·hr per sterilization cycle
- **Water requirement**: ~9 μL/cm² of surface
- **Effective organisms**: Bacteria (*E. coli*, *P. cepacia*, *B. pumilus*
  including spores), yeasts, molds
- **Initial population tested**: 2 × 10⁵ CFU reduced to zero

## See Also

- [[microwave-surface-sterilization]]
- [[microwave-vs-traditional-sterilization]]

## References

1. Atwater, J.E., Streech, N.D., Garmon, F.C. NASA Tech Briefs MSC-22484.
   Lyndon B. Johnson Space Center, Houston, Texas 77058.
