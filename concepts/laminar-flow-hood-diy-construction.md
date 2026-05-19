---
title: Laminar Flow Hood Diy Construction
created: 2026-04-13
updated: 2026-04-15
type: concept
tags: [reference]
sources: ["raw/papers/laminar-flow-hood-construction-1.md"]
---
## DIY Laminar Flow Hood Construction

A laminar flow hood is the single most important piece of [[accessible-mushroom-cultivation-for-disabilities]]. It provides a continuous stream of HEPA-filtered air, creating a sterile workspace for inoculation, agar work, and [[stamets-growing-room-air-circulation-co2-management]] into the unit
2. **Filter pad** (prefilter) traps large dust particles
3. **[[growing-gourmet-hepa-filtration-laboratory-air-systems]]**: Must remove 99.9% of airborne material (filter class H14, EN 1822)
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

## Practical Applications

The principles and techniques discussed here have wide-ranging applications
across multiple disciplines and contexts. Practitioners and researchers
continue to explore new ways to integrate these concepts into modern practice,
adapting traditional knowledge to contemporary challenges and opportunities.

## Key Considerations

Several important factors influence the effectiveness and outcomes described
in this topic. Understanding these considerations helps practitioners make
informed decisions and avoid common pitfalls. Environmental conditions,
timing, and material selection all play critical roles.

## Historical Context

The historical development of this subject reflects centuries of accumulated
knowledge and practical experience. From traditional methods passed down
through generations to modern scientific approaches, the evolution continues
to inform current best practices and research directions.

## Common Challenges

Practitioners frequently encounter several challenges when working with
these concepts. Climate variability, resource limitations, and knowledge
gaps can all affect outcomes. Addressing these challenges requires patience,
observation, and a willingness to adapt approaches based on results.

## See Also
- [[laminar-flow-hood]]
- [[spore]]
- [[laminar-flow-hood-construction-hepa-filter]]
## Further Reading
Continued research and practical application deepen understanding of this topic.
Field observations and experimental data continue to inform best practices.
Cross-disciplinary approaches offer promising avenues for further investigation.
Integration with ecological principles enhances long-term sustainability.
Historical context provides important lessons for modern applications.
Collaborative networks and knowledge sharing accelerate progress in this field.
## Practical Applications
The principles discussed here have direct applications in agricultural systems, ecological restoration, and sustainable resource management.
Practitioners have demonstrated successful implementation across diverse climates and soil conditions.
Adaptation to local conditions and careful observation remain central to effective application.

## Research Directions
Current research explores the intersections between traditional knowledge and modern scientific understanding.
Comparative studies across different bioregions provide valuable insights into generalizable principles.
