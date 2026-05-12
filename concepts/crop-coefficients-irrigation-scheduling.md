---
title: Crop Coefficients — Irrigation Scheduling with Kc Values
created: 2026-05-10
updated: 2026-05-10
type: concept
tags: [irrigation, crop-coefficient, water-management, evapotranspiration]
sources:
  - "raw/papers/solomon-gardening-west.md"
---

# Crop Coefficients for Irrigation Scheduling

## Definition

The crop coefficient (Kc) is the ratio of actual crop evapotranspiration (ETc) to
reference evapotranspiration (ETo). It translates weather-based reference ET estimates
into crop-specific water demand: Kc = ETc / ETo. ETc is crop evapotranspiration and
ETo is reference ET, typically computed using the FAO Penman-Monteith equation for a
standard grass reference surface. By multiplying Kc by ETo, irrigators estimate daily,
weekly, or seasonal water requirements for any crop under non-stressed conditions.

## The Three Kc Growth Stages

Crop coefficients vary across [[query-how-to-protect-plants-from-frost-and-extend-the-growing-season]] as the canopy develops, reaches full
cover, and senesces. FAO-56 defines four growth stages, but Kc is commonly described
across three practical phases: **Initial stage** — from planting to ~10% ground cover,
with low Kc values (0.15–0.50) because soil evaporation dominates; **Mid-season stage**
— from full ground cover to senescence onset, where Kc peaks (0.95–1.30) as
transpiration through the full canopy dominates; and **Late season stage** — from
senescence to harvest, where Kc declines (0.60–0.90) as leaves dry and the canopy no
longer shades the soil. A fourth transition period (crop development) bridges initial
and mid-season stages with a linear or curvilinear increase in Kc.

## FAO-56 Single vs. Dual Crop Coefficient Approach

The **single crop coefficient** (Kc) combines transpiration and soil evaporation into
one value. It is simpler and suitable when soil evaporation is minor or frequent
irrigation keeps the surface near [[bulk-substrate-field-capacity]]. The **dual crop coefficient** splits
Kc into two components: Kc = Kcb + Ke, where Kcb is the basal crop coefficient
representing transpiration from a dry, evaporation-free surface, and Ke is the soil
evaporation coefficient. The dual approach is more accurate for fields where the soil
surface is frequently wetted and then dries between events.

## Kcb vs. Ke — Basal and Evaporation Components

Kcb represents crop transpiration when the soil surface is visually dry but the root
zone contains adequate water. Ke accounts for evaporation from the topsoil layer —
after a wetting event, Ke can spike to 0.80–1.00, then decays exponentially as the
soil dries. The decay rate depends on soil texture, [[evaporative-demand-gradient-stipe-elongation-mechanism-badham-1982]], and the
evaporation layer depth (typically 0.10–0.15 m). The dual approach requires tracking
soil moisture in the evaporation layer separately from the root zone, adding
complexity but yielding more precise recommendations, especially for wide-row crops
with significant exposed soil.

## Typical Kc Values for Major Crops

FAO-56 publishes tabulated Kc values for hundreds of crops. Representative values
under standard sub-humid conditions (RHmin ≈ 45%, wind ≈ 2 m/s):

| Crop            | Initial | Mid   | Late  |
|----------------|---------|-------|-------|
| Wheat          | 0.30    | 1.15  | 0.40  |
| Corn (maize)   | 0.30    | 1.20  | 0.60  |
| Rice           | 1.05    | 1.20  | 0.90  |
| Cotton         | 0.35    | 1.20  | 0.70  |
| Tomato         | 0.35    | 1.15  | 0.70  |
| Potato         | 0.35    | 1.15  | 0.75  |
| Alfalfa        | 0.40    | 1.20  | 1.05  |
| Orchard (apple)| 0.45    | 0.95  | 0.70  |

These values must be adjusted for local climate. Rice is unique — flooding maintains
a saturated surface, so even initial Kc values are high.

## Factors Modifying Kc

Published Kc values assume standard sub-humid climate. When conditions deviate,
adjustments are necessary. **Climate correction**: FAO-56 formulae adjust mid-season
Kc based on minimum relative humidity and wind speed — arid, windy climates increase
Kc by 0.05–0.20. **Planting date and cultivar**: earlier or later planting shifts
growth stage timing relative to evaporative demand. **Crop density and [[wide-row-spacing-intensive-gardening-comparison]]**:
higher populations and narrower rows accelerate canopy closure, raising Kc during
development. **[[query-how-do-i-choose-the-right-irrigation-method-for-my-vegetable-garden]]**: [[cervantes-drip-irrigation-systems]] reduces Ke compared to sprinkler
or flood. **Soil properties**: coarse sandy soils lose more water to evaporation than
fine-textured soils after each wetting event.

## Stress-Adjusted Kc Using Ks

When root zone water is insufficient, actual crop ET falls below potential ET. FAO-56
introduces a water stress coefficient (Ks, 0 to 1): ETc_adj = Ks × Kc × ETo. Ks
depends on the fraction of available soil water depleted (p) and total available
water (TAW). When depletion exceeds the readily available threshold, Ks declines

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
- [[dom]]
- [[winter-harvest-scheduling-year-round]]
- [[shulgin-future-psychedelics-scheduling-and-regulation]]
- [[solomon-irrigation-systems-sprinkler-design]]
- [[solomon-drip-irrigation-limitations-home-garden]]
