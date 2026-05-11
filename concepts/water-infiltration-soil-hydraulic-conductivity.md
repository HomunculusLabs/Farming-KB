---
title: Water Infiltration and Soil Hydraulic Conductivity
created: 2026-05-10
updated: 2026-05-10
type: concept
tags: [soil-physics, water-infiltration, hydrology, irrigation]
sources: []
---

# Water Infiltration and Soil Hydraulic Conductivity

## Definition

Water infiltration is the process by which water enters the soil surface from
rainfall, irrigation, snowmelt, or other sources. It represents the transition of
water from the atmosphere into the vadose zone, where it becomes soil moisture
available for plant uptake or deep percolation to groundwater.

The infiltration rate (mm/hr) describes the speed at which water enters the soil at
any moment, while cumulative infiltration (mm) is the total depth of water that has
entered over a period. Understanding both is essential for designing irrigation
systems, predicting runoff, and managing stormwater.

## The Infiltration Process

Infiltration follows a characteristic curve with three phases. During the initial
phase, dry soil rapidly absorbs water at a high rate controlled by capillary suction
and gravity, declining quickly as pores fill and the wetting front advances. The
transition phase follows, where the rate declines gradually as the driving gradient
decreases. Finally, steady-state infiltration is reached, stabilizing at
approximately the saturated hydraulic conductivity. In layered soils, the steady
rate may be limited by a less permeable subsurface horizon.

## Factors Affecting Infiltration

**Soil texture** is a primary control. Sandy soils have large, well-connected pores
that transmit water quickly. Clay soils restrict movement through fine particles and
small pores. Silt loams occupy an intermediate position but can develop surface
seals under intense rainfall.

**Soil structure** modifies texture effects. Well-aggregated soils offer stable
macropores that conduct water efficiently. Compacted structure collapses pores and
reduces infiltration. [[fukuoka-textdoc-composting-critique-futility-prepared-organic-matter]] promotes aggregation by binding particles into
stable crumbs resistant to slaking.

**Initial moisture content** influences early infiltration through matric suction.
Dry soils have strong capillary forces that pull water in rapidly; as soil wets,
these forces diminish and the rate declines toward steady-state.

**Surface cover** plays a protective role. Vegetation canopy and mulch absorb
raindrop kinetic energy, preventing sealing and crusting. Bare soil can develop a
structural crust within minutes, reducing infiltration by 50-80% compared to
protected surfaces.

**Slope** influences opportunity time. On steep slopes, water flows quickly across
the surface, reducing time available for entry. Gentle slopes allow ponding and
longer contact time, promoting deeper infiltration.

## Soil Hydraulic Conductivity

Soil hydraulic conductivity (K) quantifies how easily water moves through soil.
Saturated hydraulic conductivity (Ksat) describes flow when all pores are water-
filled, while unsaturated conductivity K(θ) varies with water content and decreases
as larger pores drain first.

Darcy's Law provides the fundamental equation: Q = -K · A · (dh/dl), where Q is
volumetric flow rate, K is conductivity, A is cross-sectional area, and dh/dl is
the hydraulic gradient. In unsaturated soil, K becomes a function of matric
potential, creating nonlinear relationships described by van Genuchten or Brooks-
Corey models. Ksat ranges from <0.1 cm/hr in heavy clays to >25 cm/hr in coarse
sands — one of the most variable soil properties, often differing by orders of
magnitude within a single field due to texture, structure, and biopore heterogeneity.

## Infiltration Models

The **Kostiakov model** is empirical: I = a·t^b, where I is cumulative infiltration,
t is time, and a and b are fitted parameters. It fits data well but predicts zero
steady-state rate, limiting long-duration use.

The **Green-Ampt model** assumes a sharp wetting front advancing into uniformly
wettable soil, relating infiltration to wetting front suction, Ksat, and the change
in water content. It provides physical insight but simplifies real heterogeneity.

The **Horton model** describes exponential decline: f(t) = fc + (f0 - fc)·e^(-kt),
where f0 is initial rate, fc is steady-state, and k is a decay constant.

## Measurement Methods

**Double-ring infiltrometers** are the standard field method. An inner ring measures
infiltration while an outer buffer ring prevents lateral flow. Ponded water levels

## See Also
- [[mollison-designers-soil-water-storage-and-field-capacity]]
- [[holzer-water-power-hydraulic-ram]]
