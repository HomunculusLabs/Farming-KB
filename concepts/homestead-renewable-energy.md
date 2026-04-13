---

title: Homestead Renewable Energy
created: 2026-04-11
updated: 2026-04-12
type: concept

tags:
- equipment
- regenerative
- troubleshooting
- old-world
- homesteading
- season-extension
- new-world
- plant-systems

sources:
- raw/masanobu-fukuoka-the-natural-way-of-farming-the-theory.md
- raw/the-modern-farm-why-cannabis-grown-with-lab-might-produce.md
- raw/unknown-effect-of-spawn-grains-with-culture-medium-on-carpophore.md
---

# Homestead Renewable Energy

Solar PV, wind, micro-hydro, wood heating, and energy conservation for zone 7-8 homesteads. Priority: reduce loads first, then generate.

## Solar PV Systems

### Off-Grid vs Grid-Tied
- **Off-grid:** Battery required, $8-15/W installed, for remote properties
- **Grid-tied with backup:** Lower cost ($3-6/W), net metering, battery optional
- **Recommendation:** If grid available, grid-tied with battery backup; if remote, off-grid sized for winter

### Panel Types
| Type | Efficiency | Cost/W | Lifespan | Best For |
|------|-----------|--------|----------|----------|
| Monocrystalline | 20-23% | $0.80-1.20 | 25-30 yr | Cold climates, limited space |
| Polycrystalline | 16-19% | $0.60-0.90 | 25 yr | Budget, large arrays |
| Thin-Film | 10-13% | $0.70-1.00 | 15-20 yr | Flexible mounting |

Mono panels gain ~0.3-0.5% efficiency per °C below 25°C — ideal for zone 7-8 winters. Snow reflection boosts output 10-20%.

### Battery Storage
| Chemistry | Cycle Life | DoD | Cost/kWh | Efficiency | Cold Note |
|-----------|-----------|-----|----------|------------|-----------|
| **LiFePO4** | 3,000-6,000 | 80-100% | $150-250 | 95% | Cannot charge below 32°F |
| Lead-Acid (FLA) | 500-1,500 | 50% | $100-150 | 80-85% | Better cold tolerance |
| AGM | 500-1,200 | 50% | $150-250 | 85% | Better cold tolerance |

**LiFePO4 recommended** for new systems. Cold workaround: insulated enclosure + small heating element + temperature-managed BMS.

### Charge Controllers & Inverters
- **MPPT** (93-97% efficient): Always preferred; 20-30% more harvest than PWM
- **PWM** (70-80%): Small 12V budget systems only
- **Inverter:** Pure sine wave required for electronics and well pumps; 3,000-5,000W continuous for typical homestead
- **Top brands:** Victron MultiPlus, Schneider Conext, EG4 (budget)

### Mounting
- **Ground or pole mount** for zone 7-8 — easy snow removal, optimal angle
- **Adjustable tilt** (60-70° winter) adds 15-25% winter production
- Fixed roof mount: cheaper but harder to maintain in snow country

## Solar Water Heating

| System | Cost | Winter Efficiency | Freeze Protection |
|--------|------|-------------------|-------------------|
| Batch (ICS) | $500-2,000 DIY | 40-50% | Poor |
| Thermosiphon | $1,500-4,000 | 50-65% | Poor |
| Drainback | $3,000-6,000 | 60-70% | Excellent (drains when off) |
| Glycol Closed-Loop | $3,500-7,000 | 55-65% | Excellent |

**Zone 7-8 recommendation:** Evacuated tube collectors with glycol closed-loop. Superior winter performance, vacuum insulation resists freezing, tubes shed snow. Saves 50-70% on water heating costs. See [[water-management]] for rainwater integration.

## Small Wind Turbines

**Reality check:** Most homestead sites lack adequate wind. Install an anemometer for 12+ months before investing. Average wind ≥10 mph at turbine height required.

- **HAWT** (horizontal): 30-45% efficient, $3,000-15,000, needs 60-100 ft tower
- **VAWT** (vertical): 15-25% efficient, often oversold, not recommended
- Wind + solar hybrid: Complementary (wind blows when sun doesn't), but higher complexity
- **Recommendation:** Only after confirming excellent wind resource. Most homesteads better served by more solar + battery.

## Micro-Hydro Power

Most cost-effective renewable **IF** you have year-round flowing water with adequate head or flow.

**Power formula:** Watts = Head (ft) × Flow (GPM) × 0.18 × Efficiency

| Head | Flow | Power |
|------|------|-------|
| 50 ft | 20 GPM | 180 W |
| 100 ft | 50 GPM | 900 W |
| 200 ft | 50 GPM | 1,800 W |

- **Turbine types:** Pelton (high head), Cross-flow (low head), Turgo (medium)
- Produces 24/7 — allows smaller battery bank than solar-only
- **Zone 7-8 challenge:** Streams may freeze or reduce in winter; bury penstock below frost line
- **Permits:** FERC exemption <100 kW; state water rights permits often required
- **Cost:** $5,000-15,000 installed for 500W-1kW systems

## Rocket Stoves & Mass Heaters

See [[natural-farming-fukuoka]] for holistic design philosophy. Rocket mass heaters (RMH) burn wood at 80-90% efficiency vs 40-60% for conventional stoves.

- **J-tube combustion:** Insulated burn tunnel, vertical chimney, complete gas combustion
- **Cob thermal mass:** Stores and releases heat over 12-24 hours
- **Wood use:** 25-50% of conventional stove for same heat output
- **DIY cost:** $400-800 (firebrick, perlite, steel barrel, cob, ductwork)
- **Heats:** 500-2,000 sq ft depending on size; excellent for [[greenhouse-design]] heating
- Integrate copper coil in thermal mass for [[water-management]] pre-heating

## Energy Conservation (Do This First)

Every watt saved = $5-10 less in system cost.

### Insulation (Zone 7-8)
| Location | Recommended R-Value |
|----------|-------------------|
| Attic/Ceiling | R-60 |
| Walls | R-30+ |
| Basement | R-20 |
| Floor over crawlspace | R-30 |

### Load Reduction
- **LED lighting:** Entire home on 100-200W total
- **Efficient fridge:** 150-350 kWh/yr (DC fridges like SunDanzer eliminate inverter loss)
- **Phantom loads:** Smart power strips eliminate 100-300W of constant draw
- **Variable speed well pump:** 50% less energy than conventional

### Passive Solar Design
- South-facing glazing (8-12% of floor area) with overhangs sized for winter sun / summer shade
- Thermal mass (concrete, tile, stone) on south side stores daytime heat
- Deciduous trees for summer shade, winter sun; light-colored roof reduces cooling load 10-20%
- See [[homesteading-infrastructure]] and [[greenhouse-design]] for integration

## System Sizing

### Load Calculation Example
| Load | Watts | Hours/Day | Wh/Day |
|------|-------|-----------|--------|
| Well pump (1/2 HP) | 1,000 | 1 | 1,000 |
| Efficient refrigerator | 150 | 8 (33% duty) | 1,200 |
| LED lights | 100 | 5 | 500 |
| Laptop + router | 100 | 8 | 800 |
| Phone charging | 20 | 4 | 80 |
| Small tools | 500 | 0.5 | 250 |
| **Total** | | | **4,230 Wh/day** |

### Peak Sun Hours (Zone 7-8, adjustable tilt)
| Season | Hours |
|--------|-------|
| Summer | 5.5-6.5 |
| Spring/Fall | 4.5-5.5 |
| **Winter** | **3.0-4.0** |

**Always size for winter.** For 4,230 Wh/day at 3.0 PSH with 85% system efficiency: ~1,660W array → round up to 1,800-2,000W.

### Quick Sizing Rules
| Homestead Scale | Daily Load | Solar Array | Battery Bank |
|----------------|-----------|-------------|--------------|
| Small cabin | 1,500 Wh | 800-1,200 W | 5-8 kWh |
| 1-2 people | 3,000-4,000 Wh | 1,500-2,500 W | 10-15 kWh |
| Family of 4 | 5,000-8,000 Wh | 3,000-5,000 W | 15-25 kWh |

Battery bank sizing: Daily Load × Days of Autonomy ÷ DoD ÷ 0.9 (temp derating). Use 2-3 days autonomy with generator, 4-5 days without.

## Costs & Incentives

### System Costs (DIY installed)
| Scale | Solar + Battery + Controller + Inverter |
|-------|------------------------------------------|
| $5K system | 1,500W panels + 5kWh LiFePO4 — lights, electronics, small fridge |
| $10K system | 3,000W panels + 13kWh LiFePO4 — full small homestead with well pump |
| $25K system | 7,000W panels + 25kWh LiFePO4 + generator — family homestead + shop |

### Incentives
- **Federal ITC:** 30% of solar PV, solar water heating, and battery costs (through 2026+)
- **USDA REAP:** Up to 25% grant for rural agricultural producers (<50,000 population)
- **State programs:** Check DSIREusa.org for tax credits, property tax exemptions, net metering
- Generator backup ($2,000-4,000): Essential for off-grid zone 7-8 winters

## Maintenance & Winter Operations

### Battery Care
- **LiFePO4:** Never charge below 32°F; store at 50-60% SoC long-term; 10-15 year lifespan
- **Lead-acid:** Check water monthly; equalize charge every 1-3 months; ventilate enclosure

### Winter Checklist
- Oversize array 50-100% vs summer needs
- Steep tilt (60-70°) + ground mount for snow shedding
- Battery heating for LiFePO4
- Generator on standby for extended cloudy periods
- Load shift: run well pump and heavy tools midday when solar peaks
- See [[seasonal-planning]] for integrated seasonal routines

### Monitoring
- Battery SoC, solar input, load consumption (Victron BMV-712: $200, or Cerbo GX: $400)
- Panel cleaning: 2-4×/year; soft brush, deionized water
