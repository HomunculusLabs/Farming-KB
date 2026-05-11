---
title: Microwave Sterilizable Access Port Msap
created: 2026-05-11
updated: 2026-05-11
sources:
  - "Sterilizing Surfaces by Irradiation with Microwaves (NASA MSC-22484)"
type: concept
tags: [NASA, sterilization, microwave, spacecraft, access-port, ECLSS]
---

# Microwave Sterilizable Access Port (MSAP)

The Microwave Sterilizable Access Port (MSAP) is a three-subsystem device
developed at NASA's Lyndon B. Johnson Space Center to enable aseptic
transfer of materials into and out of biologically sensitive closed systems
aboard spacecraft. The MSAP was designed to solve the fundamental problem of
how to open a sterile system, add or remove materials, and reseal it without
introducing contamination.

## The Core Problem

Spacecraft carry closed biological systems including [[chen-maitake-growth-parameters-environmental-control]]
and [[eclss-environmental-control-life-support]] System (ECLSS) water recycling loops and scientific
experiments containing sensitive biological materials. Accessing these
systems requires opening a physical port, which exposes the previously
sterile interior to potential contamination from the mating surfaces of
the access hardware and the ambient environment.

Traditional approaches to this problem each have significant drawbacks.
Autoclaving the entire access assembly creates unacceptable thermal loads.
Chemical disinfection introduces contaminants into the closed biological
system. UV treatment cannot reach all surfaces of complex mating fixtures.
A new approach was needed that could sterilize all relevant surfaces
without heat, chemicals, or line-of-sight requirements.

## Three-Subsystem Architecture

The MSAP consists of three integrated subsystems, each addressing a
specific aspect of the [[eclss-water-system-aseptic-access-space-biology]] problem:

### 1. In-Line Valve Port Assembly

This is the permanent interface between the closed biological system and
the external environment. The valve port assembly is designed with mating
surfaces that can be exposed to microwave energy for sterilization. The
assembly uses a combination of microwave-reflective and microwave-
[[microwave-reflective-transparent-materials-surface-sterilization]] to direct energy precisely to the surfaces that
require treatment.

The valve design ensures that when closed, the biological system remains
sealed. When opened for material transfer, the previously sterilized
mating surfaces present a clean interface to the specimen transfer
assembly. The materials selection is critical -- metallic components
reflect microwaves while selected polymers and ceramics are transparent,
allowing the microwave energy to reach the interior mating surfaces.

### 2. Portable Microwave Sterilization Chamber

This subsystem delivers the sterilization treatment. It contains the
microwave source (magnetron), waveguide components, antennas, and the
trace water introduction system. The chamber is designed to accept the
mating end of the valve port assembly and the specimen transfer assembly,
exposing all critical surfaces to [[dry-microwave-irradiation-spore-resistance]] simultaneously.

The portability of the sterilization chamber is a key design feature.
Rather than integrating the microwave components into each access port,
a single portable unit can service multiple access points throughout
the spacecraft, reducing weight and complexity. The chamber connects
to the port assembly, delivers the sterilization cycle, and is then
disconnected for use at another location.

### 3. Specimen Transfer Assembly

This is the removable component that physically carries materials into
or out of the biological system. The transfer assembly is designed with
surfaces compatible with microwave sterilization and mates with both the
valve port assembly and the sterilization chamber.

Before each transfer operation, the specimen transfer assembly is
sterilized in the microwave chamber. It is then connected to the valve
port assembly, which has itself been pre-sterilized. Materials are
transferred through the mated, sterile interface. After transfer, the
process is reversed and all surfaces are re-sterilized before the next
use.

## Microwave Energy Management

A critical innovation in the MSAP design is the management of microwave
energy through material selection and geometry control. By using
microwave-reflective materials (metals) to contain the energy and
microwave-transparent materials (certain polymers, ceramics) to allow
penetration, the system directs energy precisely to the surfaces requiring
treatment while protecting surrounding components.

The radiation patterns and subsystem geometries are engineered to ensure
sufficient exposure of all desired surfaces. This includes the interior
surfaces of the valve port, the mating surfaces of the transfer assembly,
and any crevices or recessed features where microorganisms might survive
surface-level treatments.

## Application to Closed Biological Systems

The primary NASA application was accessing ECLSS waters -- the water
recycling system that provides drinking water and process water to crew
members aboard spacecraft. Contamination of this system could have serious
health consequences, making aseptic access critically important.

The technology is also applicable to any closed biological system where
aseptic material transfer is required, including bioreactors, cell culture
systems, and fermentation vessels. The ability to sterilize enclosed
surfaces without opening the system or applying heat makes it particularly
valuable for systems containing heat-sensitive biological materials.

## Development Team

The MSAP was developed by a team at NASA's Johnson Space Center led by
James E. Atwater (Technical Director), with Neil D. Streech as Project
Engineer and Frank C. Garmon serving as Microbiologist. The work was
published as NASA Technical Support Package MSC-22484 and made available
through NASA's Technology Transfer Program for wider commercial and
scientific application.

## See Also
- [[msap-subsystem-architecture-microwave-sterilizable-access-port]]
- [[microwave-sterilizable-access-port-nasa-msap-msc-22484]]
- [[msap-subsystem-architecture-microwave-sterilizable-access-port-design]]
