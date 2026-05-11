---
title: Rectangular Waveguide Dipole Antenna Microwave Surface Sterilization
tags: [mycology, sterilization, microwave, NASA, waveguide, antenna, engineering, hardware, 2-45-ghz, surface-sterilization]
created: 2026-05-09
source: sterilizing-surfaces-by-irradiation-with-microwaves.md
---

# Rectangular Waveguide and Dipole Antenna Array Design for Microwave Surface Sterilization

## Overview

The [[challenge-organisms-nasa-microwave-surface-sterilization-testing]] sterilization system (MSC-22484) employs a
specific [[microwave-sterilization-system-hardware-architecture]] to deliver 2.45 GHz microwave energy to
contaminated surfaces. The system comprises a [[magnetron-oscillator-microwave-sterilization]], power
supply, rectangular waveguide, waveguide-to-coaxial adapter, coaxial
[[coaxial-power-splitter-waveguide-microwave-sterilization]], and multiple dipole antennas. Understanding this
architecture is essential for reproducing or adapting the system for
specific applications.

## System Architecture Overview

The microwave energy follows this path from generation to application:

```
Power Supply → Magnetron Oscillator → Rectangular Waveguide →
Waveguide-Coaxial Adapter → Coaxial Power Splitter → Dipole Antennas →
Target Surface
```

Each component plays a specific role in converting electrical power into
controlled electromagnetic radiation on the target surface.

## Magnetron Oscillator

The magnetron is the microwave source. It converts high-voltage DC
electrical power from the power supply into 2.45 GHz microwave radiation
through the interaction of electrons with a magnetic field in a resonant
cavity structure. Key characteristics for sterilization applications:

- **Frequency**: 2.45 GHz, the ISM (Industrial, Scientific, Medical)
  band frequency reserved for microwave heating applications worldwide.
  This frequency couples efficiently with water molecules through
  dipolar rotational absorption.

- **Power output**: The magnetron must deliver sufficient power to
  achieve the target exposure rate of 3.6 W/cm² at the surface. The
  actual magnetron power rating depends on the surface area being
  sterilized and the coupling efficiency of the antenna system.

- **Continuous wave operation**: Unlike pulsed radar magnetrons,
  sterilization magnetrons operate in continuous wave (CW) mode,
  delivering constant power output throughout the exposure period.

## Rectangular Waveguide

The rectangular waveguide is a hollow metallic conduit that channels
microwave energy from the magnetron to the antenna array. At 2.45 GHz,
the standard waveguide dimensions (WR284: 72.14 mm × 34.04 mm) are
optimized for low-loss propagation of the dominant TE₁₀ mode.

The waveguide serves several purposes:

- **Impedance matching**: The waveguide dimensions are chosen to match
  the magnetron's output impedance, maximizing power transfer efficiency.
- **Directional control**: Unlike free-space radiation, waveguide
  propagation confines the microwave energy to a defined path, allowing
  precise delivery to the antenna array.
- **Power handling**: The waveguide can handle higher power densities
  than coaxial cable at microwave frequencies, reducing losses over the
  distance between magnetron and antennas.

## Waveguide-to-Coaxial Adapter

The adapter transitions the microwave energy from the rectangular
waveguide format to a coaxial cable format. This transition is necessary
because the coaxial power splitter and antenna feeds use coaxial
connectors. The adapter must maintain impedance matching across the
transition to minimize reflected power, which could damage the magnetron
or reduce the energy delivered to the surface.

## Coaxial Power Splitter

The power splitter divides the single coaxial input into multiple
outputs, each feeding one dipole antenna. The split ratio and number of
outputs are determined by the surface geometry being sterilized:

- **Uniform coverage**: Multiple antennas ensure that all areas of the
  target surface receive adequate exposure. A single antenna would create
  a radiation pattern with high-intensity and low-intensity zones.
- **Phased array potential**: By controlling the phase of the signals
