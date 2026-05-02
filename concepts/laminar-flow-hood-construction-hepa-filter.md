---
title: Laminar Flow Hood HEPA Filter Selection and Integration
created: 2026-04-24
updated: 2026-04-24
type: concept
tags: [equipment, mycology, reference]
sources:
  - "Laminar Flow Hood Construction - Forister and Burger, UC Davis"
---
# Laminar Flow Hood HEPA Filter Selection and Integration

The HEPA (High Efficiency Particulate Air) filter is the critical component that makes a [[comparison-laminar-flow-hood-vs-fruiting-chamber]] functional. Selecting the right filter, sizing it correctly, and integrating it properly into the hood enclosure determines whether the workspace achieves true sterility. This page covers HEPA filter specifications, selection criteria, and integration techniques based on published construction designs including the Forister and Burger (UC Davis) dual-hood system.

## HEPA Filter Fundamentals

### What HEPA Filters Remove
- **99.97%** of particles 0.3 microns and larger (US DOE standard)
- **99.99%** of all airborne materials per the Forister and Burger specification
- Fungal [[spore]]s (typically 5-20 microns) are well within the capture range
- Bacteria (0.5-5 microns) are reliably filtered
- Dust, pollen, mycelial fragments, and other particulates

### Filter Ratings and Standards
- **HEPA class**: H13-H14 per EN 1822 (European standard)
- **US standard**: 99.97% DOP efficiency at 0.3 microns
- **ULPA** (Ultra-Low Penetration Air) filters offer even higher efficiency (99.999%) but are overkill for [[mushroom-cultivation]] and create excessive pressure drop

### Filter Construction
- Deep-pleated filter media (typically glass fibre or synthetic) in an aluminium or wood frame
- Standard depths: 2", 4", 6", and 12"
- Deeper filters have more media surface area, resulting in lower pressure drop for the same face velocity
- The Forister and Burger design specified 24" x 30" x 6" HEPA filters (deep-pleated, high capacity)

## Sizing the HEPA Filter

### Filter Face Area
The filter dimensions determine the working area of the hood and the required blower capacity:

| Filter Size | Face Area | Required CFM at 100 FPM |
|-------------|-----------|------------------------|
| 12" x 24" | 2 sq ft | 200 CFM |
| 24" x 24" | 4 sq ft | 400 CFM |
| 24" x 30" | 5 sq ft | 500 CFM |
| 24" x 36" | 6 sq ft | 600 CFM |
| 24" x 48" | 8 sq ft | 800 CFM |

### Face Velocity
The standard face velocity for laminar flow hoods is **100 feet per minute (0.5 m/s)**. This speed is fast enough to prevent contaminants from entering the work zone but slow enough to maintain smooth, non-turbulent (laminar) airflow.

- Too slow: Contaminants can drift into the sterile zone
- Too fast: Turbulence disrupts the laminar curtain and creates eddies that pull in unfiltered room air

### Pressure Drop
HEPA filters create significant resistance to airflow (static pressure):

- A new 6" deep HEPA filter typically has a pressure drop of ~0.8-1.2 inches water gauge (in. w.g.) at rated face velocity
- As the filter loads with dust over time, pressure drop increases
- The blower must be rated to deliver the required CFM **at the operating pressure**, not at free air
- Always check the blower's performance curve against the filter's pressure drop specification

## Filter Selection Criteria

### Physical Dimensions
- Choose filter width and height based on the desired working area
- Deeper filters (6" or 12") have lower pressure drop and longer service life than shallow ones (2")
- Ensure the filter frame material is compatible with your sealing method (aluminium frames seal best with gasketing)

### Frame Type
- **Aluminium frame**: Best choice — rigid, non-porous, easy to seal, compatible with gasket tape and caulk
- **Wood frame**: Less common, harder to seal perfectly, can warp with humidity
- **Plastic frame**: Avoid — may off-gas and is less rigid

### Seal Integration
The filter-to-enclosure seal is the most critical point in hood construction. Air that bypasses the filter is unfiltered air:

- **Gasket tape** (neoprene or silicone): Applied to the filter frame perimeter before installation. Compresses when the enclosure is screwed down, creating a reliable seal
- **Weather stripping**: Foam or rubber strip around the filter opening in the enclosure
- **Caulk**: Silicone or polyurethane caulk applied after filter installation for a permanent seal (makes filter replacement difficult)
- **Forister and Burger method**: 1" x 12" pine enclosure dadoed to receive the filter edges, providing a precise mechanical fit supplemented by the enclosure screws

## Integration in the Forister and Burger Design

The UC Davis dual-hood design demonstrates several important HEPA integration principles:

### Filter Mounting
- The HEPA filter is set back from the table edge by the width of an egg crate white lighting panel
- This creates a light-diffusing space between the filter face and the working surface
- Spacer blocks attached to the base hold the filter in position
- The egg crate panel is secured to the HEPA filter via machine screws through 1/2" aluminium channel, plastic grid, and foam insulation into the aluminium filter frame

### Filter Enclosure
- 1" x 12" pine boards form the enclosure around the filter
- The pine is dadoed (grooved) to receive the filter edges, providing both alignment and improved sealing
- The enclosure is screwed into the 3/4" plywood base
- The back of the enclosure is covered with 1/4" plywood

### Filter Lid Design
- Loose-fitting filter lids are made to cover the filters when not in use
- Lids have handles for easy removal
- No screws attach the lids — they simply rest in place for easy access when filters need replacement
- This design protects the filter face from physical damage and dust accumulation during storage

### Pre-Filter Integration
- Extended surface air pre-filters (16" x 20" x 2") protect the HEPA filters
- The pre-filter catches large dust particles before they reach the HEPA, dramatically extending HEPA life
- Pre-filters are inexpensive (~$4 each in bulk) and should be cleaned or replaced every 1-3 months

## Cost Considerations

HEPA filters represent the single largest expense in hood construction. A 24" x 30" x 6" filter costs $110-200; smaller 12" x 24" x 2" filters run $50-100. In the Forister and Burger construction, two HEPA filters cost $220 (1990s pricing); modern equivalents are $200-350 for the same specification.

## Filter Maintenance and Replacement

### Service Life
- With proper pre-filter maintenance, HEPA filters last 5-10 years
- Never wash, vacuum, or attempt to clean a HEPA filter — this damages the media
- The only maintenance is ensuring the pre-filter is functioning

### Signs of Filter Degradation
- Noticeably reduced airflow from the hood face
- Increased blower noise (motor working harder against higher pressure drop)
- Failed smoke test (turbulence instead of smooth laminar flow)
- Positive contamination test on open [[agar]] plates in the work zone

### Replacement Procedure
1. Turn off and unplug the blower
2. Remove the filter lid
3. Unscrew the enclosure or release clamping mechanism
4. Carefully lift out the old filter
5. Clean the seating area and install new gasket material if using compressible gaskets
6. Position the new filter, secure the enclosure, and verify seal integrity with a smoke test

## Testing Filter Performance

### Smoke Test
- Hold incense or a smoke source near the filter face
- The smoke should flow in smooth, parallel lines perpendicular to the filter
- Any turbulence, eddies, or horizontal drift indicates filter damage or seal leaks
- This is the standard field test recommended by Forister and Burger (they verified sterility via open petri plate contamination tests)

### Agar Plate Test
- Pour sterile agar plates in front of the running hood
- Incubate unopened for 48-72 hours
- Zero growth on plates confirms the filter and seals are functioning correctly

## See Also

- [[laminar-flow-hood-diy-construction]] — complete hood construction guide with blower sizing
- [[laminar-flow-hood-guide]] — laminar flow hood usage and protocols
