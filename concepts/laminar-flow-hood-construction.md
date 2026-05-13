---
title: "Laminar Flow Hood Construction"
source: 2-laminar-flow-hood-construction.md
type: concept
---

# Laminar Flow Hood Construction

A laminar flow hood is an enclosed workspace designed to maintain a sterile environment by continuously passing filtered air across the work surface. It is essential for [[vermiculite-particle-size-water-retention-calibration-pf-tek]])
2. **Airflow velocity** — must maintain approximately 0.5 m/s in the working area; too slow and contaminants can drift in, too fast and turbulence disrupts the laminar flow

## Flow Configurations

Laminar flow hoods come in two configurations:

### Horizontal Flow

Air moves from the back of the working area toward the front (the operator). This is the most common configuration for mycology and plant tissue culture work. The operator works with their hands between themselves and the sterile air stream.

### Vertical Flow

Air moves from the top of the working area downward, exiting through a perforated base. This configuration is preferred for applications where the product (not the operator) must remain in the sterile airstream, such as electronics manufacturing and some pharmaceutical compounding.

## Advantages Over the Steam Method

| Aspect | Steam Method | Laminar Flow Hood |
|--------|-------------|-------------------|
| Sterile area size | Limited | Ample |
| Temperature | Hot (limits exposure time) | Room temperature (extended work sessions) |
| Flask compatibility | Wide lids problematic | Accommodates wide-lid flasks |
| Cost | Low | Higher (~€300) |
| Space requirement | Minimal | Needs dedicated space |
| Best for | Home propagation | High-volume or precision work |

## Sizing the Blower and Filter

### Choosing the HEPA Filter

The HEPA filter should be selected based on:

- **Filtration class**: H14 per EN 1822 (removes 99.995% of particles ≥0.1 μm)
- **Physical dimensions**: large enough to provide adequate working area. A common size is 305 mm × 610 mm × 78 mm
- **Pressure drop**: typically around 150 Pa at 60% of nominal airflow

### Calculating Required Airflow

The blower must deliver sufficient air volume at the pressure drop imposed by the filters. The calculation proceeds as follows:

```
Required air speed: 0.5 m/s
Filter face area: 0.305 m × 0.61 m = 0.186 m²

Volumetric flow = area × velocity
                = 0.186 m² × 0.5 m/s
                = 0.093 m³/s
                = 335 m³/h (× 3600 s/h)
                ≈ 198 CFM (× 0.5886)
```

### Unit Conversions

- 1 m³/h = 0.5886 CFM
- 1 CFM = 1.699 m³/h

### Selecting the Blower

With the required airflow (335 m³/h) and pressure drop (~150 Pa for the HEPA plus ~10–20 Pa for the pre-filter), select a [[mycoremediation-bioreactor-design-considerations]]:

- **Top panel**: Transparent plexiglass to maximize light in the working area
- **Sealed enclosure**: All joints must be airtight to prevent unfiltered air bypassing the HEPA filter
- **HEPA filter mounting**: Gasket-sealed frame to ensure all air passes through the filter media
- **Blower housing**: Located upstream of the pre-filter, securely mounted to minimize vibration

### Typical Bill of Materials

| Component | Example | Cost |
|-----------|---------|------|
| Centrifugal blower | G2E140-AI28-01 | ~€114 |
| Pre-filter pad | HS-E/360 | ~€15 |
| HEPA filter | HS Mikro SF 305×610×78 mm | ~€131 |
| Press boards / sheet material | 19 mm | ~€24 |
| Hardware (screws, gaskets, etc.) | — | ~€20 |
| **Total** | | **~€304** |

## Operating Procedure

Proper use is critical to maintaining sterility:

1. **Pre-run cleaning**: Turn on the blower and wipe the entire sterile working area with 70% isopropyl alcohol on clean kitchen paper
2. **Purge period**: Let the blower run continuously for 30 minutes to flush any residual airborne contaminants
3. **Second wipe**: After 30 minutes, repeat the alcohol wipe of the working surface
4. **Work surface**: Use sterilizable tools (e.g., glass Petri dishes wiped with alcohol) for all manipulations

### Best Practices

- Never block the airflow path with objects
- Work slowly and deliberately to minimize air turbulence
- Keep hands downstream of (or at the same level as) the work materials in horizontal-flow hoods
- Replace pre-filter pads regularly (monthly under heavy use)
- HEPA filters typically last 3–5 years depending on use and ambient [[growing-gourmet-hepa-filtration-laboratory-air-systems]]
- [[mushroom-cultivation-equipment-sourcing-jarrold]]
