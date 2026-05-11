---
title: [[comparison-laminar-flow-hood-vs-fruiting-chamber]] Blower and Filter Sizing
source: 2-laminar-flow-hood-construction.md
type: concept
---

# Laminar Flow Hood Blower and Filter Sizing

Selecting the correct blower and [[hepa-filter]] combination is the most critical engineering step in DIY laminar flow hood construction. An undersized blower fails to maintain sterile airflow; an oversized one wastes energy and creates turbulence. This page covers the calculations and [[cannabis-breeding-traits-selection-criteria-clarke]] from a proven DIY build using commercially available European components.

## How a Laminar Flow Hood Functions

- Air is drawn through a **filter pad** (prefilter) that traps large dust and debris particles
- Prefiltered air then passes through a **HEPA filter** (High Efficiency Particulates Air) removing fungi, bacteria, and fine dust
- Sterile air flows into the working (flasking) area for contamination-free work
- Two critical parameters: [[growing-gourmet-hepa-filtration-laboratory-air-systems]] efficiency (99.9%) and air speed (~0.5 m/s at the work surface)
- The system operates as a positive-pressure clean zone pushing contaminants away from the work area

## Horizontal vs. Vertical Airflow

- **Horizontal flow:** Air moves from the back of the working area to the front
  - Operator faces the airflow, which sweeps contaminants away from the work
  - Simpler to build; preferred for most DIY applications
  - Work area depth limited by filter width
- **Vertical flow:** Air moves from top to bottom, exiting through holes in the base
  - More common in professional laboratory settings
  - Better for operations that generate particles (grinding, weighing)
  - More complex base construction required for air exit
- The build described here uses **horizontal airflow** for simplicity and adequate performance

## Choosing the HEPA Filter

- Must remove 99.9% of airborne material (filter class **H14** per EN 1822 standard)
- Should be large enough to provide adequate working area space for intended tasks
- Prefilter pad recommendation: **HS-E/360** (coarse particle trap mounted before the HEPA)
- HEPA filter example: **HS-Mikro SF** (30.5 cm width × 61 cm height × 7.8 cm depth)
- Filter dimensions directly determine both the working area size and the blower airflow requirements
- The HEPA filter is the single most expensive component and the most critical for sterility
- Always verify the filter is rated H14 (99.995% efficiency at MPPS) rather than lower grades

## Blower Sizing Calculation

The required airflow is calculated from the HEPA filter face area and the target air velocity:

- **Width of HEPA filter:** 0.305 m
- **Height of HEPA filter:** 0.61 m
- **Required air speed:** 0.5 m/s
- **Airflow calculation:** 0.305 × 0.61 × 0.5 = 0.093025 m³/s
- **Convert to m³/h:** 0.093025 × 3600 = **334.89 m³/h**
- **Convert to CFM:** 334.89 × 0.5886 = **~197 CFM**

### CFM Conversion Reference

| Unit | Equivalent |
|------|-----------|
| 1 m³/h | 0.5886 CFM |
| 1 CFM | 1.6990 m³/h |
| 334.89 m³/h | ~197 CFM |

## Determining Required Pressure

- The HEPA filter creates aerodynamic resistance (pressure drop) that the blower must overcome
- Read the manufacturer's pressure-flow characteristic diagram for the specific HEPA [[psilocybin-serotonin-mimic-thalamic-filter-model]]
- At 334.89 m³/h (approximately 60% of nominal airflow for the HS-Mikro SF), required pressure is **150 Pa**
- This pressure value, combined with the airflow rate, defines the blower's operating point on its own performance curve
- Pressure requirements increase as filters age and accumulate particulate matter

## Selecting the Blower

- Example blower: **[[centrifugal-blower-g2e140]] G2E140-AI28-01** (Ziehl-ebm GmbH)
- The blower must be rated for at least 334.89 m³/h at 150 Pa on its performance curve
- Centrifugal (squirrel cage) blowers are preferred over axial fans for their higher static pressure capability
- The blower is intentionally chosen slightly stronger than minimum requirements

### Why Oversize the Blower

- The prefilter pad adds resistance not accounted for in HEPA-only pressure calculations
- Filters accumulate dust over time, increasing pressure drop and reducing delivered airflow
- It is far easier to throttle a slightly oversized blower than to upgrade an undersized one
- A speed controller (dimmer switch or fan speed controller) can reduce output to achieve target velocity
- A 10–20% oversizing margin accounts for aging filters and prefilter resistance

## Construction Materials

- **Main body:** 19 mm press boards (particle board or MDF), cut and screwed together
- **Top panel:** Transparent plexiglas recommended to maximize light in the work area
- **Sealing:** All joints must be airtight — use weatherstripping or silicone sealant
- **Filter chamber:** Enclosed space between blower and HEPA filter to ensure all air passes through the filters
- The blower mounts on one end; the HEPA filter on the opposite end of the filter chamber
- Ensure the HEPA filter is sealed around its entire perimeter with gasket material

## Cost Breakdown

| Component | Cost (€) |
|-----------|----------|
| Blower (G2E140-AI28-01) | 114.30 |
| Filter pad (E360) | 15.08 |
| HEPA filter (305 × 610 × 78 mm) | 131.08 |
| Press boards (19 mm) | 23.91 |
| Small parts (screws, sealant, etc.) | 20.00 |
| **Total** | **304.37** |

## Verification and Airflow Testing

- After assembly, verify airflow with an anemometer at the work surface
- Target velocity: 0.4–0.6 m/s across the entire filter face
- If velocity is too high, restrict the blower intake or use a speed controller
- If velocity is too low, check for air leaks around filter seals and joints
- Smoke testing (incense stick) can visualize laminar flow patterns and reveal turbulence

## Usage Protocol

- Turn on the blower and wipe the entire sterile area with 70% isopropyl alcohol on a paper towel
- Let the blower run continuously for **30 minutes** to purge airborne contaminants
- After 30 minutes, repeat the alcohol wipe of all work surfaces
- Use a glass petri dish as a sterile cutting surface, cleaned with alcohol before each use
- Avoid placing objects near the front edge that could disrupt laminar airflow patterns
- Never block the airflow path with large objects that create turbulent eddies
- Keep the prefilter clean by vacuuming or replacing it periodically

## See Also

- [[laminar-flow-hood-construction]]
- [[laminar-flow-hood-diy-construction]]
- [[laminar-flow-hood-guide]]
