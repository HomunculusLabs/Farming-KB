---
title: Laminar Flow Hood Guide
created: 2026-04-11
updated: 2026-04-12
type: concept

tags:
- mushrooms
- cultivation
- equipment
- homestead-crafts
- underground-press
- lighting
- lighting-hardware
- troubleshooting
- reference

sources:
- raw/papers/laminar-flow-hood-construction-1.md
- raw/papers/2-laminar-flow-hood-construction.md
---

# Laminar Flow Hood Guide

A laminar flow hood (LFH) provides a continuous stream of HEPA-filtered air, creating a sterile workspace for mushroom cultivation, agar work, and tissue culture. It is the gold standard for contamination prevention.

Related: [[mushroom-sterile-technique-detailed]], [[mushroom-grow-equipment]]

## How It Works

A blower fan draws room air through a prefilter (removing large particles) then forces it through a HEPA (High Efficiency Particulate Air) filter. The HEPA removes 99.97% of particles 0.3 microns and larger — well below the size of fungal spores (typically 5-20 microns) and bacteria (0.5-5 microns). The filtered air exits as a smooth, non-turbulent (laminar) stream, creating a sterile work zone.

## Core Components

| Component | Spec | Typical Cost |
|-----------|------|-------------|
| HEPA filter | 24x12x6 in or 24x24x12 in, 99.97% at 0.3 microns | $80-200 |
| Blower motor | Squirrel cage type, matched to filter static pressure | $50-150 |
| Prefilter | MERV 8-13, washable or disposable | $10-30 |
| Enclosure box | Plywood, MDF, or melamine, sealed | $30-80 |
| Hardware | Screws, caulk, weather stripping, switch | $10-20 |
| **Total DIY** | | **$180-480** |

## Sizing

The standard DIY size is 2 ft x 4 ft (24x48 in working face). This provides ample workspace for agar plates, grain jars, and inoculation work. Smaller hoods (12x24 in) work for limited budgets.

## Calculating Airflow

Proper airflow is critical. The HEPA filter has a rated face velocity of 100 FPM (feet per minute). To achieve this:

1. Calculate filter face area: 24 x 48 in = 1152 sq in = 8 sq ft
2. Required CFM = area x velocity = 8 x 100 = 800 CFM
3. Account for filter static pressure (typically 1.0-1.2 in w.g.) — the blower must deliver 800 CFM at that pressure
4. Always check the blower"s performance curve, not just free-air CFM rating

A minimum of 100 CFM per square foot of filter area ensures laminar flow. Too little and contaminants enter; too much and turbulence disrupts the sterile curtain.

## DIY Build Steps

1. **Build the box**: Cut plywood to size. The box should be deep enough (12-18 in) to house the blower and allow air to distribute evenly before hitting the HEPA.
2. **Mount the blower**: Position on the intake side. Use a plenum (baffle) if needed to distribute air evenly across the filter face.
3. **Install prefilter**: Mount on the blower intake to extend HEPA life.
4. **Seal everything**: Caulk all joints. Use weather stripping around the HEPA filter frame. Any air leak bypasses filtration.
5. **Mount the HEPA**: The filter is the weak structural point. Support it well and seal its perimeter.
6. **Wire the blower**: Include a switch. Consider a speed controller for fine-tuning airflow.
7. **Test**: Run for 30 minutes before first use to clear any construction debris.

## UC Davis Dual-Hood Design (Forister & Burger)

Forister and Burger (UC Davis, Dept. of Environmental Horticulture) published a detailed design for two laminar flow hoods connected to one blower by dryer vent hose, based on Meyer (1986, HortScience 21(4)):

### Fan Housing Construction
- Built from 3/4" plywood, 4x8 ft sheet
- All rabbets cut 3/4" wide and 1/2" deep
- Air passages cut in END and END inside pieces
- Fan hood made from #2 pine, fits inside the main box
- Top center piece with 4" diameter holes (6 minimum) for hose attachments
- Hose attachments made from 4" aluminum irrigation pipe, 3" long
- Rotary switch (ELECTROSWITCH #21301A)
- Blower: Dayton #5C094

### Hood Construction
- Base: Two layers of 3/4" plywood, glued and screwed, laminated with Formica
- HEPA filter set back from table edge by width of egg crate white panel
- Egg crate panel holds HEPA filter in place via machine screws through 1/2" channel
- Enclosure: 1x12" pine, dadoed to receive filter edges for better seal
- Back: 1/4" plywood
- Top: Clear plexiglass hood with 1" angle aluminum frame (1/16" thick), continuous piece with 90-degree bends

### Verified Sterility
- Open petri plate contamination tests confirmed the hoods provide a sterile environment for plant tissue culture work

### Cost Breakdown (Two Hoods, One Fan — 1990s Prices)

**Hood materials:** HEPA filters (2x 24x30x6") $220, plywood (3/4") $34, plywood (1/4") $10, pine (1x12x16") $17, Formica $24, adhesive $6, plexiglass (4x8x1/4") $110, egg crate panels (2) $24, aluminum channel $25, paint $15, angle aluminum $10, miscellaneous $30 = **$525**

**Fan housing:** Dayton #5C094 blower $185, rotary switch $40, plywood $30, molding $18, prefilters (case of 6) $24, dryer vent hose $35, misc $46 = **$378**

**Grand total: $903** (for two complete hoods sharing one fan)

## Testing the Hood

- **Smoke test**: Hold incense smoke near the filter face. The smoke should flow straight down in smooth parallel lines with no turbulence or eddies.
- **Particle counter** (ideal): Verify particle count drops to near-zero in the work zone.
- **Agar test**: Pour plates in front of the hood and incubate unopened. Zero growth on control plates confirms sterility.

## Maintenance

- **Prefilter**: Clean or replace every 1-3 months depending on dust load
- **HEPA filter**: Lasts 5-10 years with proper prefilter maintenance. Do not wash or vacuum. Replace when airflow drops noticeably.
- **Seals**: Inspect caulk and weather stripping annually; re-caulk as needed

## Commercial Alternatives

Pre-built laminar flow hoods cost $500-3000+. For occasional home use, a still air box (SAB) at $5-20 is a viable alternative, though the flow hood dramatically reduces contamination rates for regular agar work.

## See Also

[[mushroom-contamination-identification]], [[mushroom-indoor-cultivation]]
- [[mushroom-sterile-technique-detailed]] for workspace protocols beyond the hood
- [[agar-work-guide]] for detailed agar procedures
- [[mushroom-grow-equipment]] for full equipment lists
