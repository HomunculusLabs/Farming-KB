---
title: Off-Grid Electricity Basics
created: 2026-04-12
updated: 2026-04-12
type: concept
tags: [homesteading, engineering, equipment, sustainability]
sources: []
---

# Off-Grid Electricity Basics

Off-grid electricity systems generate, store, and distribute power independently from the utility grid. For the homesteader, an off-grid system provides energy independence, resilience during grid outages, and the ability to live on remote land. The core components are solar panels, batteries, charge controllers, and inverters.

## Daily Watt-Hour Calculation

The first step in system design is calculating daily energy consumption. Every appliance has a power draw (watts) and a usage duration (hours). The product is watt-hours (Wh).

### Common Appliance Wattages

- LED light bulb: 5-10 watts
- Laptop computer: 50-100 watts
- Refrigerator (ENERGY STAR): 150-400 watts (runs ~30% of the time)
- Well pump (1/2 HP): 800-1200 watts (runs 1-2 hours/day)
- Chest freezer: 100-200 watts (runs ~30% of the time)
- Washing machine: 400-800 watts
- Microwave: 600-1200 watts
- Phone charger: 5-10 watts
- Internet router: 10-20 watts
- Water pressure pump: 200-500 watts

### Sample Daily Calculation

| Appliance | Watts | Hours/Day | Watt-Hours |
|-----------|-------|-----------|------------|
| LED lights (6) | 60 | 6 | 360 |
| Refrigerator | 250 | 8 (duty cycle) | 2000 |
| Well pump | 1000 | 1.5 | 1500 |
| Laptop | 80 | 4 | 320 |
| Phone chargers | 20 | 3 | 60 |
| Internet router | 15 | 24 | 360 |
| Washing machine | 500 | 0.5 | 250 |
| Misc (fans, tools) | 200 | 1 | 200 |
| **Daily Total** | | | **5050 Wh (5.05 kWh)** |

Add 25% for system losses and inefficiency: 5050 x 1.25 = 6313 Wh/day.

## Solar Panels

Solar panels convert sunlight to DC electricity. Panel output is rated in watts under Standard Test Conditions (STC).

### Panel Sizing

To meet the 6313 Wh/day example:

- Determine sun hours for your location (3-6 hours peak sun is typical; use 4 hours conservative average)
- Daily panel output needed = 6313 Wh / 4 hours = 1578 watts
- Add 20% for degradation and weather: 1578 x 1.2 = 1894 watts
- Round up: 2000 watts (2 kW) of solar panels

This means approximately six 330W panels or eight 250W panels.

### Panel Types

- Monocrystalline: Highest efficiency (18-22%), best performance per square foot, most expensive
- Polycrystalline: Moderate efficiency (15-18%), good value
- Thin-film: Lowest efficiency, flexible, best for curved surfaces or mobile applications

### Mounting

- Roof mount: Saves ground space, uses existing structure. Harder to clean and adjust angle.
- Ground mount: Easier to install, clean, and optimize angle. Takes up space.
- Pole mount: Can be adjusted seasonally. Good for small arrays.
- Adjustable tilt: Set angle to latitude for year-round, or adjust seasonally (latitude -15 in summer, +15 in winter).

## Batteries

Batteries store solar energy for use when the sun is not shining. Battery capacity is measured in amp-hours (Ah) at a specific voltage.

### Battery Sizing

For 3 days of autonomy (no sun) at the example load:

- Total storage needed: 6313 Wh/day x 3 days = 18,939 Wh
- For a 12V system: 18,939 / 12 = 1578 Ah
- For a 48V system: 18,939 / 48 = 395 Ah
- Add 20% depth of discharge buffer for lead-acid: 395 / 0.50 = 790 Ah at 48V (lead-acid, 50% max discharge)
- For lithium: 395 / 0.80 = 494 Ah at 48V (80% usable capacity)

### Battery Types

- Lead-acid (flooded): Lowest cost per Ah, requires regular maintenance (watering, equalizing), 3-7 year lifespan, 50% max depth of discharge, toxic electrolyte.
- Lead-acid (AGM): Maintenance-free, sealed, 3-7 year lifespan, 50% max depth of discharge, higher cost than flooded.
- Lead-acid (gel): Maintenance-free, sensitive to overcharging, 3-5 year lifespan.
- Lithium iron phosphate (LiFePO4): Higher upfront cost, 10-15+ year lifespan, 80%+ depth of discharge, no maintenance, lighter weight, safer chemistry. Best long-term value for off-grid.

### 12V vs 24V vs 48V Systems

Higher system voltage means lower current for the same power, allowing smaller wire gauge and less voltage drop over distance:

- 12V: Small systems under 1000W. Simple but limited.
- 24V: Medium systems 1000-3000W. Good compromise.
- 48V: Systems over 3000W. Recommended for full homestead systems. More efficient, smaller wire, wider inverter selection.

## Charge Controllers

Charge controllers regulate voltage and current from solar panels to batteries, preventing overcharging.

- PWM (Pulse Width Modulation): Simple, inexpensive, less efficient. Suitable for small systems.
- MPPT (Maximum Power Point Tracking): More efficient (10-30% more power harvest), higher cost, required for larger systems and mismatched panel/battery voltages.

Size the charge controller to handle the total solar array amperage plus 25% safety margin.

## Inverters

Inverters convert DC battery power to AC household power (120V or 240V).

- Modified sine wave: Inexpensive, causes hum in electronics, not recommended.
- Pure sine wave: Clean power, required for sensitive electronics and motors, higher cost.

### Inverter Sizing

Calculate peak surge demand (the highest combined wattage at any one moment):

- If the well pump (1000W) and refrigerator (250W) start simultaneously: 1250W surge, plus base loads.
- Add 30% safety margin: 1250 x 1.3 = 1625W minimum.
- For a full homestead with well pump, recommend 3000-5000W continuous inverter.

## System Layout

A typical off-grid system flows:

Solar panels --> Charge controller --> Battery bank --> Inverter --> AC breaker panel --> Household circuits

All DC wiring (panels to controller, controller to batteries) should use appropriate gauge wire with fusing. All AC wiring should follow standard electrical code (NEC in the US).

## Cost Estimates

A basic 2-4 kW off-grid system:

- Solar panels (2 kW): $1500-3000
- Lithium battery bank (10 kWh): $3000-5000
- MPPT charge controller: $200-600

## See Also

- [[van-life-off-grid]]
- [[query-what-are-the-best-heating-options-for-an-off-grid-homestead]]
- [[off-grid-energy-and-homestead-infrastructure]]
- [[cotter-off-grid-mushroom-cultivation]]
- [[off-grid-waste-management]]
