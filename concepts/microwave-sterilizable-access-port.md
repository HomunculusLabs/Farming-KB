# Microwave Sterilizable Access Port

The Microwave Sterilizable Access Port (MSAP) is a NASA-developed
system designed to provide [[eclss-water-system-aseptic-access-space-biology]] to biologically sensitive
enclosed systems such as spacecraft [[chen-maitake-growth-parameters-environmental-control]] and Life
Support Systems (ECLSS) and in-flight biological experiments. The
MSAP uses microwave energy to sterilize all mating surfaces before
and after [[aseptic-specimen-transfer-space-environment-microwave-sterilizable-access-port]], enabling contamination-free access
without traditional autoclaving, chemical disinfection, or gamma
irradiation.

## Problem Statement

Spacecraft life support systems and biological experiments require
strict aseptic conditions. However, accessing these systems for
sample collection, product addition, or maintenance inevitably
exposes internal sterile environments to potential contamination
through the access port fixtures. Traditional sterilization
methods were inadequate because autoclaving caused thermal damage
to sensitive biological systems, chemical disinfectants left
residues incompatible with biological experiments, gamma
irradiation was impractical for complex surface geometries, and
UV light could not reach shadowed surfaces within enclosed
systems.

## System Architecture

The MSAP consists of three integrated subsystems:

1. **In-line Valve Port Assembly**: The permanent connection
   point to the enclosed system, incorporating a valve mechanism
   that seals the system when not in use. The valve port is
   designed with surfaces that can be effectively irradiated
   by microwaves from an external source.

2. **Portable [[coaxial-power-splitter-waveguide-microwave-sterilization]] Chamber**: A detachable
   unit that mates with the valve port and contains the
   microwave generation and irradiation components. This
   chamber houses the magnetron, waveguide system, antennas,
   and trace water delivery system needed for surface
   sterilization.

3. **Specimen Transfer Assembly**: The component that moves
   through the sterilized interface to deliver or retrieve
   materials from the enclosed system. The transfer assembly
   surfaces are sterilized both before entry and after exit.

## Microwave Engineering

The sterilization chamber uses a [[magnetron-oscillator-microwave-sterilization]] operating
at 2.45 GHz as the microwave source, coupled with a power
supply and [[rectangular-waveguide-dipole-antenna-microwave-surface-sterilization]] for energy delivery. A coaxial
power splitter distributes energy to multiple antennas for
uniform surface coverage. Both waveguide antennas and dipole
antennas are employed to address different surface geometries
within the mating interface.

The system uses a combination of microwave-reflective and
microwave-transparent materials to direct energy precisely to
the surfaces requiring sterilization. [[cervantes-reflective-materials-grow-room-walls]]
channel microwaves toward target areas, while transparent
materials allow energy penetration to reach otherwise
inaccessible surfaces. Control of radiation patterns and
subsystem geometries ensures sufficient exposure of all mating
surfaces.

## Sterilization Cycle

The MSAP operates through a defined sequence:

1. The microwave sterilization chamber is mated to the valve
   port assembly.
2. Trace water (approximately 9 microliters per square
   centimeter) is introduced to all surfaces to be sterilized.
3. [[dry-microwave-irradiation-spore-resistance]] at 3.6 W/cm2 is applied for a total
   exposure of 13.1 watt-hours.
4. All mating surfaces are confirmed sterilized by the
   complete kill of [[challenge-organisms-nasa-microwave-surface-sterilization-testing]].
5. The valve opens, allowing the specimen transfer assembly
   to pass through the sterilized interface.
6. After transfer, the cycle repeats to sterilize surfaces
   that were exposed during the transfer operation.

## Key Innovations

The MSAP introduces several novel concepts to aseptic access
technology. The use of microwave energy for [[challenge-microorganisms-microwave-surface-sterilization]]
of mating fixtures is an entirely new application of this
electromagnetic spectrum region. The combination of reflective
and transparent materials for energy control enables sterilization
of complex three-dimensional surface geometries that cannot be
addressed by conventional methods.

The ability to sterilize surfaces after penetrating elastomeric
materials is particularly significant. This means the microwave
energy can pass through flexible seals and gaskets to sterilize
the actual mating surfaces, eliminating the need to disassemble
sealed connections for sterilization.

## Validation Results

The MSAP sterilization system was validated against a panel of
challenge microorganisms including [[bacillus-pumilus-radiation-resistance-surface-decontamination]] spores,
Escherichia coli, and [[e-coli-pseudomonas-cepacia-microwave-susceptibility-surface-sterilization]]. Initial surface
populations of 2 x 10^6 CFU were reduced to zero after the
standard 13.1 W-hr exposure cycle, demonstrating complete
sterilization of all surfaces within the access port interface.

## Spacecraft Applications

The primary intended application is maintaining sterility of
spacecraft water systems (ECLSS) during sample collection and
resupply operations. Additional applications include aseptic
access to biological experiments carried on spacecraft, where
contamination would invalidate experimental results. The
portable nature of the microwave chamber allows one sterilization
unit to service multiple access ports throughout a spacecraft.

## Terrestrial Adaptation Potential

The MSAP concept could be adapted for terrestrial bioprocessing
applications where aseptic access to closed systems is required.
Bioreactors, fermenters, and sterile processing lines in
pharmaceutical and biotechnology manufacturing could benefit from
microwave-sterilizable access ports. The technology is
particularly attractive for systems containing thermally labile
components that cannot withstand autoclaving temperatures.

## See Also

- [[microwave-surface-sterilization]]
- microbial kill by microwave irradiation

## References

1. Atwater, J.E., Streech, N.D., & Garmon, F.C. NASA Tech Briefs, MSC-22484.
   Lyndon B. Johnson Space Center, Houston, Texas.
