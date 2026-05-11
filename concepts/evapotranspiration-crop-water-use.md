---
title: Evapotranspiration — Crop Water Use Fundamentals
created: 2026-05-10
updated: 2026-05-10
type: concept
tags: [irrigation, crop-water-use, evapotranspiration, water-management]
sources: []
---

# Evapotranspiration — Crop Water Use Fundamentals

## Definition

Evapotranspiration (ET) is the combined process of water loss from the land surface
through two mechanisms: **soil evaporation** and **plant transpiration**. Soil
evaporation is the [[lemon-cannabis-alchemy-direct-vaporization]] of water from the soil surface, while
transpiration moves water through a plant from roots to leaves, where it is released
as vapor through stomata. Together, these represent the primary pathway by which
water returns from agricultural fields to the atmosphere.

ET is the single largest consumptive use of water in most irrigated agricultural
systems, often accounting for 80–95% of total water applied. Accurately estimating
ET is essential for efficient [[crop-coefficients-irrigation-scheduling]], water rights management, and
sustainable agricultural water use.

## Reference Evapotranspiration (ET₀)

Reference evapotranspiration (ET₀) standardizes ET estimates for a well-watered
reference surface — typically a 12 cm tall, actively growing grass cover. ET₀
represents climatic demand and is computed from weather station data.

The **FAO-56 Penman-Monteith equation** is the internationally accepted standard
for calculating ET₀. It combines an energy balance component (net radiation, soil
heat flux) with an aerodynamic component (wind speed, [[cervantes-vapor-pressure-deficit-transpiration]],
temperature) to estimate [[evaporative-demand-gradient-stipe-elongation-mechanism-badham-1982]]. The equation requires four key inputs:
solar radiation, air temperature, wind speed, and relative humidity. ET₀ values are
reported in mm/day and vary widely — arid regions may see 8–12 mm/day in summer,
while cool humid climates may drop below 2 mm/day.

## Crop Evapotranspiration (ETc)

Crop evapotranspiration (ETc) adjusts reference ET for a specific crop by applying
a **crop coefficient (Kc)**:  `ETc = Kc × ET₀`

The Kc value integrates crop-specific characteristics such as canopy cover, rooting
depth, crop height, and stomatal behavior. Kc values typically range from 0.2–0.4
during initial growth stages, peak at 1.0–1.3 during mid-season, and decline as the
crop matures. FAO-56 provides standard Kc curves for dozens of major crops, adjusted for local
climate, planting date, and management. Dual crop coefficients separate basal Kc
(transpiration) from a soil evaporation coefficient (Ke) for precise budgeting.

## Factors Affecting ET

**Climatic factors** include temperature (higher temps increase vapor pressure deficit
and ET), humidity (lower humidity increases ET), wind speed (wind removes boundary-
layer moisture), and solar radiation (the primary energy source driving evaporation).

**Crop factors** include species, variety, [[mollison-shade-systems-and-canopy-architecture]], leaf area index,
rooting depth, and growth stage. A full-cover alfalfa field transpires far more
water than a sparse vegetable crop at the same location.

**Soil and management factors** include soil texture, organic matter, mulch,
residue cover, irrigation method (drip vs. flood), and soil water availability. As
soil dries, ET declines because plants close stomata to conserve water.

## Measurement Methods

Several methods exist for measuring ET directly or indirectly:

- **Lysimeters** — Weighable or drainage lysimeters measure actual ET by tracking
  water balance in an isolated soil column. Most accurate but expensive.
- **Eddy covariance** — Fast-response sensors measure vertical water vapor flux
  above the canopy, providing continuous field-scale measurements.
- **Bowen ratio** — Measures [[greg-green-temperature-and-humidity-control]] gradients to partition
  available energy into sensible and latent heat fluxes.
- **Atmometers and ET gauges** — Simple instruments simulating ET from a wet
  surface; low-cost and useful for farm-level scheduling.
- **Remote sensing** — Satellite thermal and vegetation indices estimate ET at
  regional scales using energy balance models like METRIC or SEBAL.

## Daily and Seasonal ET Patterns

Daily ET follows a diurnal curve, peaking in early-to-mid afternoon when solar
radiation and temperature are highest. Seasonally, ET increases from planting
through mid-season as canopy cover expands, then decreases as crops senesce.
Seasonal ET totals vary dramatically: winter wheat may use 400–500 mm, while fully
irrigated alfalfa in an arid valley can exceed 1,500 mm per year.

## Relationship to Irrigation Scheduling
