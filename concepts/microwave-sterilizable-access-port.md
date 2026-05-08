---
title: microwave sterilizable access port
aliases: [MSAP, NASA access port [[sterilization]], spacecraft aseptic transfer]
tags: [NASA, sterilization, spacecraft, ECLSS, mycology, aseptic-technique]
sources:
  - sterilizing-surfaces-by-irradiation-with-microwaves.md
created: 2026-05-08
---

# Microwave Sterilizable Access Port (MSAP)

The Microwave Sterilizable Access Port (MSAP) is a NASA-developed system
designed to provide aseptic access to biologically sensitive systems aboard
spacecraft. Designated MSC-22484, the MSAP was created at the Lyndon B.
Johnson Space Center to solve a persistent problem in spaceflight operations:
the inability to reliably sterilize mating fixtures when accessing closed
biological systems.

## The Problem

Spacecraft carry biologically sensitive systems includ [[stamets-pinning-initiation-stages-environmental-control]] trol
and Life Support Systems (ECLSS) waters and flight experiments. Crew members
need to aseptically remove samples and products from these systems, as well
as add materials to sterile or susceptible environments. However, every access
event introduces contamination risk through the mating fixtures and ports that
connect the external environment to the sterile interior.

Traditional [[sterilization-techniques-mushroom-cultivation]] were inadequate for this application:

- **Autoclaving**: Excessive thermal impact on vulnerable spacecraft systems.
  The high temperatures (121°C+) required could damage biological samples,
  electronic components, and fluid systems.
- **Gamma irradiation**: Capable of sterilization but impractical for in-situ
  use during missions. Requires heavy shielding and specialized facilities.
- **Chemical disinfection**: Introduces chemical contaminants into the very
  systems being protected. Residual ethylene oxide, [[hydrogen-peroxide-tissue-culture-wild-polypores]], or
  alcohols could compromise biological experiments or water supplies.
- **UV irradiation**: Cannot effectively sterilize complex surface geometries
  due to its line-of-sight limitation. Shadowed areas remain contaminated.

## MSAP Architecture

The MSAP consists of three integrated subsystems:

### 1. In-Line Valve Port Assembly

The valve port assembly is permanently installed on the spacecraft system
being accessed. It serves as the interface between the sterile internal
environment and the external access point. The assembly is designed with
materials that are transparent to 2.45 GHz microwave radiation, allowing
sterilization energy to reach all mating surfaces during the process.

The valve mechanism ensures that the system remains sealed when not actively
being accessed, maintaining sterility between operations.

### 2. Portable [[microwave-sterilization]] Chamber

This is the core innovation of the MSAP. The sterilization chamber is a
portable unit that couples with the valve port assembly to deliver microwave
energy to all mating surfaces. Key design features include:

- **Microwave-reflective materials**: Used to direct and contain the
  microwave energy within the chamber, ensuring efficient energy delivery.
- **Microwave-transparent materials**: Used for the chamber walls and mating
  surfaces, allowing [[microwave-penetration-elastomeric-materials]] to reach all contaminated areas.
- **Controlled radiation patterns**: Antenna placement and chamber geometry
  are engineered to ensure uniform energy distribution across all surfaces.
- **[[trace-water-enhanced-microwave-surface-sterilization]] delivery**: A system for introducing the small quantity of
  water (~9 µL/cm²) required for effective spore destruction.

The chamber operates at 2.45 GHz with an exposure rate of 3.6 W/cm²,
delivering a total dose of 13.1 W-hr per operation. This achieves complete
sterilization of all mating surfaces in a single cycle.

### 3. Specimen Transfer Assembly

Once sterilization is complete, the specimen transfer assembly allows
materials to be passed through the sterilized port without re-contaminating
the mating surfaces. This assembly is designed to maintain the aseptic
barrier during the actual transfer operation, whether adding or removing
materials from the protected system.

## Operating Procedure

The MSAP is designed to sterilize mating surfaces both before and after
specimen transfer, providing a double-sterilization protocol:

1. **Pre-transfer sterilization**: The microwave chamber is engaged with the
   valve port. Trace water is applied to all mating surfaces. Microwave
   irradiation at 2.45 GHz sterilizes all surfaces. The chamber is removed
   and the specimen transfer assembly is connected through the now-sterile
   port.

2. **Specimen transfer**: Materials are passed through the aseptic barrier.
   The transfer assembly maintains separation between internal and external
   environments.

3. **Post-transfer sterilization**: The transfer assembly is disconnected.
   The microwave chamber is re-engaged and the sterilization cycle is repeated
   to ensure the port is clean for future access.

## Significance for Spaceflight

The MSAP represents a critical enabling technology for long-duration
spaceflight missions where biological system integrity is paramount:

- **ISS operations**: Enables repeated access to biological experiments
  without contamination risk.
- **Planetary protection**: Supports containment protocols for sample return
  missions by ensuring outbound transfers do not introduce contaminants.
- **Life support maintenance**: Allows safe maintenance access to ECLSS
  water systems without compromising water quality.
- **Reduced consumables**: Eliminates the need for chemical sterilants, which
  represent mass and volume penalties on spacecraft.

## Relevance to Mycology

While designed for spaceflight, the MSAP concept has direct applications in
mycological research and cultivation:

- **Culture transfer**: The principle of sterilizing mating fixtures before
  and after transfer applies directly to laminar flow hood work and still-air
  box inoculation procedures.
- **Bulk substrate access**: Large-scale cultivation systems could benefit
  from microwave-sterilizable ports for adding supplements or taking samples
  from sealed growing chambers.
- **Contamination prevention**: The dual-sterilization approach (before and
  after access) is a model for aseptic technique in any sterile cultivation
  environment.

## See Also

- microwave-surface-sterilization — The underlying sterilization
  technology
- [[comparison-of-surface-sterilization-methods]] — How MSAP compares to
  other approaches

## References

- Atwater, J.E., Streech, N.D., & Garmon, F.C. "Sterilizing Surfaces by
  Irradiation with Microwaves." NASA Tech Briefs, MSC-22484.
