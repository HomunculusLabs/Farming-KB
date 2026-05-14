---
title: Mushroom Laminar Flow Hood Design
created: 2026-04-12
updated: 2026-04-12
type: concept
tags: [mushrooms, fungi, cultivation, indoor, equipment, engineering, lab-technique, filtration]
sources: []
---

## Overview

A [[laminar-flow-hood]] (LFH) is a piece of equipment that creates a continuous stream of HEPA-filtered air moving in parallel lines across a work surface. This sterile airflow prevents airborne contaminants from settling on exposed cultures during inoculation, agar work, and other sensitive procedures. For serious mushroom cultivators, a flow hood is the single most impactful upgrade over a still air box, dramatically reducing contamination rates and enabling faster, more comfortable work.

## How Laminar Flow Works

The concept is simple but effective. A blower fan draws room air through a HEPA (High-Efficiency Particulate Air) filter. The filter removes 99.97% of particles 0.3 microns and larger, including mold spores, bacteria, and dust. The clean air exits the filter as a uniform, non-turbulent (laminar) stream that flows across the work surface and out the front of the hood. Because the air is moving in parallel lines without turbulence, contaminants from the room cannot cross into the sterile zone.

Key principles:
- The work area must be within the "zone of laminarity" — the region where the air flows smoothly without breaking into turbulence.
- Nothing should block or disrupt the airflow across the work surface.
- The operator works with their hands inside the laminar flow, reaching in from the front.
- The hood does not need to be enclosed — the continuous outward flow of clean air creates the sterile zone.

## HEPA Filter Selection

### Filter Specifications

- **Filter class**: HEPA H13 (99.97% at 0.3 microns) is the minimum. H14 (99.995%) is better but more expensive and requires more powerful blowers due to higher resistance.
- **Depth**: 2 to 6 inches. Deeper filters have more surface area and lower air resistance. 4-6 inch filters are standard for DIY hoods.
- **Dimensions**: The filter size determines the work area. Common sizes:
  - 24 x 24 x 6 inches — large work area, requires significant blower power
  - 24 x 12 x 6 inches — popular compromise between size and power
  - 12 x 12 x 6 inches — minimum practical size for agar and jar work

### Filter Types

- **Mini-pleat**: Folded media in a V-pattern. Most common for DIY. Good balance of efficiency and air resistance.
- **Deep-pleat**: Heavier construction, more durable. Higher initial cost but longer life.
- **Compact**: Thinner profile (2-3 inches). Higher air resistance, requires more blower power.

### Purchasing HEPA Filters

Look for filters rated for laminar flow applications, not HVAC filters. HVAC HEPA filters are designed for different flow characteristics and may not produce true laminar flow. Verify the filter has a rated face velocity compatible with your blower design.

## Blower Sizing and Selection

### The Physics

The goal is to push air through the HEPA filter at approximately 100 feet per minute (fpm) face velocity. This speed is fast enough to maintain laminar flow and prevent contaminants from entering, but slow enough to avoid turbulence that would disturb your work.

### Calculating Required Airflow

Required CFM = Filter face area (square feet) x 100 fpm

Example for a 24 x 12 x 6 inch filter:
- Face area = 2.0 sq ft (24/12 x 12/12)
- Required CFM = 2.0 x 100 = 200 CFM

### Static Pressure

HEPA filters create significant air resistance (static pressure). A new 6-inch HEPA filter typically has a static pressure of 1.0 to 1.2 inches of water gauge (w.g.). This means the blower must be rated to deliver the required CFM at 1.0-1.2 inches of static pressure — not the "free air" CFM rating.

Most blower specs list free air CFM, which is much higher than the CFM at operating pressure. You must consult the blower's performance curve to find the actual CFM at your target static pressure.

### Blower Types

- **Inline centrifugal blower**: The standard choice. The Dayton 1TDU2 and similar models are popular. Look for shaded-pole or PSC motors.
- **Squirrel cage blower**: Can work but may be noisy and harder to mount.
- **EC (electronically commutated) fans**: More expensive but quieter, more efficient, and speed-adjustable. Growing in popularity for DIY builds.

### Blower Sizing Rule of Thumb

Multiply the required CFM (at filter face) by 1.5 to 2.0 to account for static pressure losses. Then check the blower curve to confirm it delivers the target CFM at 1.0-1.2 inches w.g.

Example: Need 200 CFM at 1.0" w.g. -> look for a blower rated at 300-400 CFM free air.

## DIY Build Guide

### Materials

- HEPA filter (sized for your needs)
- Centrifugal blower (properly sized)
- Prefilter (MERV 8-13) to extend HEPA life
- Plywood or MDF for the enclosure (3/4 inch thick)
- Silicone sealant (100% silicone, no mold inhibitors)
- Screws, hinges, and basic hardware
- Power switch and cord
- Fluorescent or LED light strip (optional but recommended)

### Construction Steps

1. **Build the plenum box**: A sealed box behind the HEPA filter that the blower mounts to. Must be airtight — all seams sealed with silicone.
2. **Mount the blower**: Bolt the blower to the plenum with a gasket (foam weatherstripping works) to prevent air leaks.
3. **Mount the HEPA filter**: The filter sits on the front of the plenum. Seal the edges with silicone or gasket material. The filter must be flush with the front edge of the work surface.
4. **Add a prefilter**: Mount a MERV 8-13 filter on the back or side of the plenum where air enters. This catches large dust and extends HEPA life.
5. **Build the work surface**: Extend a flat surface forward from the bottom edge of the HEPA filter. This is where you work.
6. **Add lighting**: Mount a light above the work surface for visibility.
7. **Test**: Turn on the blower and hold a lighter or incense stick at the work surface. The flame should bend steadily in one direction (parallel to airflow) without flickering turbulently.

### Cost Estimate

A DIY laminar flow hood typically costs $200-500 depending on size and blower choice. Commercial units cost $800-3000+. The DIY route produces equivalent performance for a fraction of the cost.

## Using the Flow Hood

- Turn on the hood at least 15 minutes before working to flush the area with clean air.
- Wipe the work surface with 70% isopropyl alcohol before and after use.
- Work within 6 inches of the filter face for maximum protection.
- Never place objects between the filter and your work — this disrupts laminar flow.
- Keep movements slow and deliberate to minimize air disturbance.
- Do not talk, cough, or breathe directly over the work area.
- Cover the filter when not in use to prevent dust accumulation.

## Maintenance

- **Prefilter**: Replace every 1-3 months depending on dust levels.
- **HEPA filter**: Typically lasts 3-5 years with a prefilter. Can be tested with a particle counter or DOP test.
- **Blower**: Lubricate bearings annually if applicable. Clean the impeller if dust accumulates.
- **Enclosure**: Wipe down monthly. Check seals annually.

## Flow Hood vs. Still Air Box

| Feature | Laminar Flow Hood | Still Air Box |
|---------|-------------------|---------------|
| Contamination rate | Very low (1-5%) | Low to moderate (5-20%) |
| Work speed | Fast, comfortable | Slow, cramped |
| Cost | $200-500 (DIY) | $10-30 |
- Complexity | Moderate build | Very simple |
| Space required | Significant | Minimal |

## Related Topics

- [[mushroom-sterile-technique-detailed]] — sterile procedures for working at the hood
- [[agar-work-guide]] — agar technique, the primary use case for a flow hood
- [[grain-spawn-preparation]] — sterile inoculation of grain jars
- [[mushroom-spore-printing-and-storage]] — creating spore syringes under sterile conditions
