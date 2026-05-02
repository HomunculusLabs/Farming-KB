---
title: DIY Laminar Flow Hood Construction
created: 2026-04-13
updated: 2026-04-15
type: concept
tags: [reference]
sources: [/Users/t3rpz/wiki/raw/papers/laminar-flow-hood-construction-1.md]
---
# DIY Laminar Flow Hood Construction

A laminar flow hood is the single most important piece of [[mushroom-grow-equipment]] for reliable [[sterile-technique-mushroom-cultivation]] in mushroom cultivation. It provides a continuous stream of HEPA-filtered air, creating a sterile workspace for inoculation, agar work, and spore handling.

## How It Works

Air is drawn through a three-stage filtration system:

1. **Blower** draws room air into the unit
2. **Filter pad** (prefilter) traps large dust particles
3. **HEPA filter** (H14 class per EN 1822) removes 99.9% of airborne contamination including fungi, bacteria, and dust
4. **Sterile laminar air** flows into the working area

## Critical Parameters

- **HEPA filtration**: Must remove 99.9% of airborne material (filter class H14, EN 1822)
- **Air speed in working area**: approximately **0.5 m/s** (100 fpm)
- Airflow must be calculated based on HEPA filter dimensions

## Horizontal vs Vertical Flow

| Type | Air Direction | Advantage | Disadvantage |
|------|--------------|-----------|--------------|
| Horizontal | Back to front | Easier to build, wider working area | Operator sits directly in airflow path |
| Vertical | Top to bottom | Better operator protection | More complex base construction, exits through floor holes |

## Sizing the Blower

### Airflow Calculation

Given HEPA filter dimensions, calculate required airflow:

```
airflow (m^3/s) = filter_width (m) x filter_height (m) x air_speed (m/s)
```

For a 30.5 cm x 61 cm filter at 0.5 m/s:
- airflow = 0.305 x 0.61 x 0.5 = 0.093 m^3/s
- Convert to m^3/h: 0.093 x 3600 = **335 m^3/h** (~197 CFM)

### Pressure Drop

The HEPA filter creates resistance. From the filter's pressure diagram, airflow of 335 m^3/h is typically ~60% of nominal flow, requiring approximately **150 Pa** pressure.

### Unit Conversions
- 1 m^3/h = 0.5886 CFM
- 1 CFM = 1.699 m^3/h

### Blower Selection

Choose a blower rated for the calculated airflow at the required pressure:
- Select slightly **oversized** to account for:
  - Prefilter resistance
  - Filter degradation over time (dirt accumulation)
  - Easier to restrict an oversized blower than upgrade an undersized one
- Centrifugal blowers (e.g., Ziehl-ebm G2E series) work well

## Construction

### Materials
- 19mm press boards for the cabinet
- Transparent plexiglas for the top (to let light in)
- HEPA filter (e.g., HS-Mikro SF series)
- Prefilter pad (e.g., HS-E/360)
- Centrifugal blower
- Screws and hardware

### Build Steps
1. Build the cabinet box from press boards to fit the HEPA filter dimensions
2. Install the blower in the prefilter chamber
3. Mount the prefilter pad between blower and HEPA
4. Install the HEPA filter at the boundary between filter chamber and working area
5. Seal all joints to prevent air bypassing the filters
6. Install plexiglas top for illumination

### Example Cost Breakdown

| Component | Cost |
|-----------|------|
| Centrifugal blower (G2E140-AI28-01) | 114 EUR |
| Prefilter pad (E360) | 15 EUR |
| HEPA filter (305 x 610 x 78 mm) | 131 EUR |
| Press boards | 24 EUR |
| Hardware (screws, etc.) | 20 EUR |
| **Total** | **304 EUR** |

## Usage Protocol

Before working in the flow hood:
1. Turn on the blower
2. Wipe the sterile area with alcohol-soaked paper
3. Let the blower run for **30 minutes**
4. Repeat the alcohol wipe of the sterile area
5. Begin work — keep movements slow and deliberate
6. Never block the airflow with hands or objects
7. Work items should be placed downstream (between filter and operator)

## Flow Hood vs Steam Method

| Aspect | Flow Hood | Steam Method |
|--------|-----------|--------------|
| Space | Large working area | Limited |
| Visibility | Excellent | Limited by steam |
| Duration | Can work for hours | Limited by heat |
| Cost | ~300 EUR | Minimal |
| Space required | Needs dedicated area | Any kitchen |
| Best for | High-volume, tissue culture | Occasional transfers |

## See Also

- [[laminar-flow-hood-construction-hepa-filter]]

- [[laminar-flow-hood-guide]] — laminar flow hood usage guide
- [[mushroom-cultivation-sterile-technique]] — sterile technique overview
- [[mushroom-sterile-technique-detailed]] — detailed sterile procedures
- [[agar-work-guide]] — agar work procedures
- [[mushroom-grow-equipment]] — equipment guide
- [[hepa-filter-selection-and-testing]] — HEPA filter specifications and testing
- [[mushroom-laminarar-flow-hood]] — laminar flow hood overview

## Multi-Station Design (Forister & Burger)

Forister and Burger (University of California, Davis) described an innovative construction connecting two laminar flow hoods to a single blower via dryer vent hose. This approach serves multiple workstations from one blower, reducing overall cost.

### Fan Housing

The fan housing is built from 3/4" plywood cut from a 4' x 8' sheet:
1. Assemble a square open-top box from SIDEs and ENDs with bottom, using rabbet joints (3/4" wide, 1/2" deep)
2. Build a fan hood from #2 pine that fits inside the box, attached to the blower outlet with #10 3/4" screws
3. The top center piece has 4" diameter holes for air distribution
4. Hose attachments are made from 4" aluminium irrigation pipe, 3" long
5. The blower used was a Dayton #5C094 direct-drive unit

### Hood Construction

Each laminar flow hood features:
- Double-layer 3/4" plywood bottom (laminated with Formica for easy cleaning)
- HEPA filter (24" x 30" x 6") set back from the table by the width of an egg crate white panel
- Egg crate lighting panel between filter face and working area for even light distribution
- 1" x 12" pine enclosure dadoed to receive the filter edges for better sealing
- Clear plexiglas hood top formed from a single continuous piece of 1" angle aluminium
