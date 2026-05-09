---
title: Evapotranspiration and Crop Water Use
created: 2026-05-02
updated: 2026-05-02
type: concept
tags: [irrigation, water, hydrology, agriculture, crop-science, climate,
  soil-moisture, plant-physiology, meteorology, farming, drought, plants]
sources:
  sources:
  - "raw/papers/marijuana-horticulture-cervantes.md"
---
Evapotranspiration (ET) is the combined process of water transfer from land
surface to atmosphere through **evaporation** from soil, water surfaces, and
canopy interception, plus **transpiration** through plant stomata. In
agricultural systems, ET represents the largest component of the field water
balance, typically 60–80% of precipitation or irrigation inputs in rainfed and
irrigated systems respectively. Accurate ET quantification underpins irrigation
scheduling, hydrologic modeling, drought monitoring, and climate impact
assessments. Global terrestrial ET is estimated at ~60,000–65,000 km³/yr,
returning ~40% of land precipitation to the atmosphere. Crop ET varies from
~300 mm/yr (wheat in cool semi-arid regions) to >1,500 mm/yr (tropical rice
with standing water).

## ET Components

Three main components contribute to total ET (ET = E + T + Ei):
- **Soil evaporation (E)**: Dominates during [[cervantes-seedling-care-early-growth]] stages with sparse
  canopy cover (can be 40–60% of ET during germination). Driven by net
  radiation, wind speed, [[cervantes-vapor-pressure-deficit-transpiration]] deficit (VPD), and near-surface soil
  moisture. The energy-limited stage (Stage 1, soil at [[bulk-substrate-field-capacity]]) gives
  E ≈ E₀; the falling-rate stage (Stage 2, below a threshold ~60% of field
  capacity) declines as hydraulic conductivity drops exponentially.
- **Plant transpiration (T)**: Dominates once canopy cover exceeds ~30–40%
  (typically 60–90% of seasonal ET). Controlled by stomatal conductance, leaf
  area index (LAI), root-zone available water, and atmospheric demand. Stomata
  optimize the tradeoff between CO₂ uptake and water loss via ABA signaling;
  transpiration efficiency is ~2–5 g biomass per kg water (C₃ crops) or 3–6 g/
  kg (C₄ crops like maize and sorghum).
- **Interception evaporation (Ei)**: Water evaporating directly from wet
  canopy surfaces before reaching soil. Typically 10–30% of gross precipitation
  in dense canopies, higher in forests (20–40%) than row crops (5–15%).
  Often estimated as a fixed fraction or via Rutter/Pearce models.

## The Penman-Monteith Equation

The **FAO-56 Penman-Monteith** equation is the global standard for ET₀:

  λET₀ = [Δ(Rₙ − G) + ρₐcₚ(es − ea)/rₐ] / [Δ + γ(1 + rₛ/rₐ)]

Where Δ = slope of saturation [[query-what-is-vapor-pressure-deficit-and-why-does-it-matter-for-cannabis]] curve (kPa/°C), Rₙ = net
radiation (MJ/m²/d), G = soil heat flux (MJ/m²/d), ρₐ = air density (kg/m³),
cₚ = specific heat of moist air (MJ/kg/°C), es − ea = vapor pressure deficit
(kPa), rₐ = aerodynamic resistance (s/m), rₛ = surface (canopy) resistance
(s/m), γ = psychrometric constant (kPa/°C), λ = latent heat of vaporization
(MJ/kg). For reference ET₀ over a hypothetical 0.12 m grass: rₐ = 208/u₂
(where u₂ = wind speed at 2 m height), rₛ = 70 s/m (active canopy).

## Reference ET and Crop Coefficients

The FAO-56 dual crop coefficient approach partitions ET into:
  ETc = (Kcb × ET₀) + Ke × ET₀

where **Kcb** = basal crop coefficient (transpiration component, species- and
stage-specific) and **Ke** = soil evaporation coefficient (function of wet soil
surface fraction and [[evaporative-demand-hypothesis-mushroom-tropism]]). Four growth stages define Kcb:
- **Initial** (planting to 10% cover): Kcb ≈ 0.15–0.30; Ke dominates
- **Development** (10% to effective full cover): Kcb increases linearly
- **Mid-season** (full cover to senescence onset): Kcb ≈ 0.95–1.20 for most
  field crops (maize 1.15, wheat 1.10, rice 1.05, soybean 1.15)
- **Late season** (senescence [[query-how-do-i-know-when-my-cannabis-is-ready-to-harvest]]): Kcb decreases linearly

Kcb is adjusted for local climate: Kcb_adj = Kcb + [0.04(u₂ − 2) − 0.004(RHₘᵢₙ
− 45)] × (h/3)^0.3, where h = mean plant height (m). Stress adjustments:
Ks = f(θ) reduces Kcb when root-zone depletion exceeds the readily available
water (RAW = p × TAW, where p ≈ 0.50 for high-frequency irrigation, 0.55–0.70
for row crops).

## Measurement Methods

Direct ET measurement remains technically challenging. Key approaches:
- **Weighing lysimeters**: Gold standard — measure mass change of an
  undisturbed soil monolith (typically 1–3 m² surface, 1.5–2 m depth) with
  precision <0.05 mm. Expensive (~$30–50K), but provides direct ET₀ and ETc.
- **Eddy covariance**: Measures vertical flux of water vapor via rapid (10–20
  Hz) sonic anemometry and infrared gas analysis. Tower-based, footprint 100–
  500 m. Energy balance closure typically 80–90% — residual attributed to
  advection and measurement error.
- **Bowen ratio energy balance (BREB)**: ET = λET = (Rₙ − G)/(1 + β), where
  β = γ × ΔT/Δe (ratio of sensible to latent heat flux). Fails when β → −1.
- **Scintillometry**: Measures refractive index turbulence along a path (0.5–
  5 km) to infer sensible heat flux; ET from energy balance residual.
- **Sap flow sensors**: Granier-type thermal probes measure transpiration of
  individual trees/vines; scaled to stand level via sapwood area.
- **Soil water balance**: ET = P + I − D − R − ΔS (precipitation + irrigation
  − deep drainage − runoff − change in storage). Simple but accumulates error.

## Remote Sensing of ET

Satellite-based ET estimation has become operational at field to continental
scales. Key approaches include **surface energy balance** methods (SEBAL,
METRIC) using thermal band temperatures to partition available energy into H
and λE; **vegetation index-based** methods relating NDVI/EVI to Kc (e.g.,
SSEBop, MOD16); **Priestley-Taylor** parameterizations calibrated from
microwave soil moisture; and **machine learning** fusion products combining
multiple sensors. Sentinel-3 (SLSTR thermal bands at 1 km, revisit 1.5 days)
and Landsat-9 (TIRS at 100 m, 16-day revisit) are primary optical/thermal
sources. GRACE/GRACE-FO gravimetry captures basin-scale ET from total water
storage anomalies. ECOSTRESS (ISS) provides 70 m thermal data at diurnal scale.

## Deficit Irrigation and Regulated Deficit

**Deficit irrigation (DI)** deliberately applies less water than full ETc to
improve water productivity (WP = yield/ET). **Regulated deficit irrigation
(RDI)** targets specific phenological stages where water stress has minimal
yield impact. Key principles:
- mollison-village-complex-elements-in-the-humid-tropics at the same temperatirrigation-systemsiation**: Primary energy source. Aerosols, clouds, and panel
  shading (agrivoltaics) directly reduce available energy for ET.
## See Also

- [[irrigation-systems]] and water delivery
- [[mollison-designers-soil-water-storage-and-field-capacity]] — soil water storage and availability
- drought stress physiology in plants — plant responses to water deficit
