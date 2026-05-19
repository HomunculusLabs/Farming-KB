---
title: Solar Water Heating
created: 2026-04-12
updated: 2026-04-12
type: concept
tags: [homesteading, energy, off-grid, engineering, water, sustainability]
sources:
  - "raw/papers/bill-mollison-permaculture-design-course.md"
---

## Solar Water Heating

Solar water heating uses the sun's energy to heat water for domestic use,
reducing or eliminating the need for gas or electric water heating. A
properly sized system can provide 50-80% of a household's hot water needs.
This guide covers system types, [[aact-brewer-design-principles-aeration-systems-ingham]], DIY construction, and
sizing for the homestead.

## Why Solar Water Heating

- **Energy savings** — water heating accounts for 15-25% of home energy use
- **Off-grid viability** — reduces generator run time or battery demand
- **Simple technology** — fewer moving parts than PV systems; long lifespan
- **Low maintenance** — annual inspection is typically sufficient
- **Payback period** — 3-8 years depending on system and fuel costs avoided

## System Types

### Batch Heater (Integrated Collector-Storage)

A tank of water inside an insulated, glazed box with a dark absorber surface.
The simplest and cheapest solar water heater.

**How it works:**
- Cold water flows into the tank from the supply line
- Sun heats the water directly in the tank
- Hot water is drawn from the top of the tank for use
- Cold water from the supply replaces what is drawn

**Advantages:**
- Simple to build — essentially a water tank in a box
- No pumps, controllers, or moving parts
- Passive operation — no electricity required
- Low cost ($200-500 DIY)

**Disadvantages:**
- Heat loss overnight — water cools when sun is not shining
- Limited capacity — typically 30-50 gallons
- Best suited for mild climates and moderate hot water demand
- Seasonal performance drops significantly in winter

**DIY Batch Heater Construction:**
1. Obtain a used electric water heater tank (40-50 gallon); strip the
   outer shell and insulation, repaint the tank black with high-heat paint
2. Build an insulated box from 2x4 lumber and rigid foam insulation (R-20+)
3. Glaze the top with tempered glass or twin-wall polycarbonate
4. Mount the tank inside the box on a south-facing roof or ground stand
5. Plumb cold water in (bottom) and hot water out (top)
6. Install a tempering valve on the output to prevent scalding
7. Tilt the collector at latitude + 15 degrees for winter optimization

### Thermosiphon System

A separate collector panel heats water that rises by natural convection
(natural thermosiphon effect) to an insulated storage tank mounted above
the collector.

**How it works:**
- Cold water from the bottom of the tank flows down to the collector
- Sun heats water in the collector
- Hot water rises naturally back to the top of the storage tank
- Continuous circulation occurs whenever the sun heats the collector
- No pump needed — relies on the fact that hot water is less dense

**Advantages:**
- Passive — no pump or controller required
- Storage tank stays warmer than batch system (insulated separately)
- Better winter performance than batch heaters
- Reliable — no mechanical parts to fail

**Disadvantages:**
- Storage tank must be mounted above the collector (usually on the roof)
- Roof structural requirements for the tank weight (400+ lbs full)
- More complex plumbing than batch heater
- Freeze protection needed [[query-how-do-i-grow-figs-in-cold-climates]] (drainback or glycol)

### Active Closed-Loop System

A pump circulates a heat-transfer fluid (propylene glycol) through the
collector and a heat exchanger in the storage tank. A differential
controller activates the pump when the collector is hotter than the tank.

**How it works:**
- Collector heats glycol solution
- Pump circulates glycol through a heat exchanger coil in the storage tank
- Heat transfers from glycol to potable water via the exchanger
- Controller monitors temperatures and runs the pump only when beneficial

**Advantages:**
- Best performance in cold climates (glycol prevents freezing)
- Storage tank can be located anywhere (basement, utility room)
- Highest overall efficiency and year-round performance
- Scalable to large systems

**Disadvantages:**
- Requires electricity for the pump and controller
- Most complex and expensive system
- Requires maintenance (glycol replacement every 5-7 years)
- Professional installation recommended for code compliance

## Sizing a Solar Water Heating System

### Daily Hot Water Demand
Estimate 15-20 gallons per person per day for a typical household.

| Household Size | Daily Demand (gallons) |
|---|---|
| 1-2 people | 30-40 |
| 3-4 people | 45-60 |
| 5-6 people | 60-80 |

### Collector Sizing
Rule of thumb: 1 square foot of collector area per gallon of daily hot
water demand in sunny climates; 1.5-2 square feet in moderate climates.

For a family of 4 (60 gallons/day):
- Sunny climate (Southwest US): 60 sq ft collector
- Moderate climate (Mid-Atlantic): 90-120 sq ft collector

### Storage Tank Sizing
Storage tank should hold 1.5-2 days of hot water demand to account for
cloudy days. For 60 gallons/day demand, use an 80-120 gallon storage tank.

### Orientation
- **Azimuth**: due south (in the Northern Hemisphere)
- **Tilt angle**: latitude for year-round optimization; latitude - 15
  degrees for summer emphasis; latitude + 15 for winter emphasis
- **Shading**: collector must have full sun from 9AM-3PM year-round

## Freeze Protection

In climates with freezing temperatures, freeze protection is essential:

## See Also

- [[mollison-designers-passive-solar-heating-building-design]]
- [[comparison-charcoal-production-for-cooking-vs-solar-cooking-methods]]
- [[comparison-agrovoltaics-vs-traditional-solar-farms]]
- [[holmgren-trees-solar-power-plants-detailed]]
- [[mollison-designers-home-energy-conservation-and-solar-heating]]
