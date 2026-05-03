---
title: "Carnot Cycle vs Rankine Cycle"
type: comparison
tags: [thermodynamics, heat-engines, power-cycles, steam-power, efficiency]
related: [carnot-cycle-and-heat-engines, rankine-cycle]
created: 2026-05-02
---

# Carnot Cycle vs Rankine Cycle

The Carnot cycle and the Rankine cycle are both heat-engine cycles, but they serve very different purposes.
The Carnot cycle is a reversible ideal that defines the maximum efficiency possible between two temperatures.
The Rankine cycle is an idealized but practical model of steam and vapor holmgren trees nature.
Carnot asks what nature allows in principle.
Rankine asks how a real boiler, turbine, condenser, and pump can convert heat into useful shaft work.
The distinction matters because comparing real steam plants directly to Carnot efficiency can be misleading.
A Rankine plant may be well designed while still operating far below the Carnot limit.

## Short Answer

Use the Carnot cycle as a theoretical benchmark for maximum efficiency.
Use the Rankine cycle as the working model for steam power plants, nuclear plants, geothermal units, and many waste-heat systems.
Carnot is defined by two isothermal and two isentropic processes.
Rankine is defined by pumping liquid, adding heat at high pressure, expanding vapor through a turbine, and condensing it.
Carnot efficiency depends only on hot and cold reservoir temperatures.
Rankine efficiency depends on component enthalpies, pressures, temperatures, turbine efficiency, pump work, moisture, and [[heat-transfer-mechanisms]] design.

## Basic Comparison

| Feature | Carnot cycle | Rankine cycle |
|---|---|---|
| Main role | Absolute theoretical limit | Practical vapor-power model |
| Typical working fluid | Any reversible working substance | Usually water/steam, sometimes organic fluids |
| Heat addition | Isothermal at T_H | Constant-pressure heating, boiling, and superheating |
| Heat rejection | Isothermal at T_C | Constant-pressure condensation |
| Expansion | Reversible adiabatic expansion | Turbine expansion, ideally isentropic but real turbines are not |
| Compression | Reversible adiabatic compression | Liquid pumping with relatively small work input |
| Efficiency formula | η = 1 - T_C/T_H | η = W_net/Q_in from enthalpy differences |
| Practical machine? | No, because it requires perfect reversibility | Yes, it approximates steam power plants |

## Process Differences

A Carnot engine absorbs heat while the working substance remains exactly at the hot-reservoir temperature.
It then expands without heat transfer until it reaches the cold-reservoir temperature.
It rejects heat isothermally at the cold temperature.
Finally it is compressed adiabatically back to the hot temperature.
Every stage is reversible, so there is no entropy generation.
A Rankine cycle begins with liquid leaving the condenser.
A pump raises the liquid to boiler pressure.
The boiler adds heat, vaporizes the liquid, and often superheats the steam.
The turbine expands the steam and produces most of the cycle's work.
The condenser rejects heat and turns the exhaust vapor back into liquid.
The Rankine sequence matches equipment that engineers can actually build and operate continuously.

## Why Rankine Replaced Carnot for Steam Plants

A pure Carnot vapor cycle would require compressing a wet vapor-liquid mixture during part of the cycle.
That compression is mechanically awkward and inefficient compared with pumping liquid water.
The Rankine cycle avoids this problem by completing condensation before pressurization.
Pumping liquid requires far less work than compressing vapor because liquids have low specific volume.
The boiler then supplies the large heat input after pressure has already been raised.
This arrangement is one reason steam power became practical at large scale.
The cost is that heat addition does not occur at one perfectly constant high temperature.
Because boiling, preheating, and superheating span a range of temperatures, the average heat-addition temperature is lower than the maximum boiler temperature.
That lowers efficiency relative to the Carnot ideal between the same extremes.

## Efficiency Interpretation

Carnot efficiency is simple because the cycle is reversible and exchanges heat with reservoirs at fixed temperatures.
If T_H is 873 K and T_C is 313 K, the Carnot limit is about 64 percent.
A real steam plant operating with similar extreme temperatures will normally be much lower.
The gap does not automatically mean poor engineering.
Part of the gap arises because Rankine heat addition occurs over a temperature range rather than at T_H alone.
Another part comes from turbine losses, pump losses, pressure drops, condenser approach temperatures, generator losses, and auxiliary loads.
Modern subcritical coal plants may achieve roughly 35 to 40 percent net efficiency.
Supercritical and ultra-supercritical plants can approach the mid-to-high 40 percent range.
Combined-cycle plants use gas-turbine exhaust to run a Rankine bottoming cycle and can exceed 60 percent in favorable designs.
All of these remain constrained by Carnot reasoning.

## Temperature-Entropy View

On a temperature-entropy diagram, the Carnot cycle is a rectangle.
The top horizontal line represents reversible heat absorption at a single high temperature.
The bottom horizontal line represents reversible heat rejection at a single low temperature.
The vertical lines are isentropic expansion and compression.
The enclosed area is net work.
The Rankine cycle has a shape determined by the liquid region, saturation dome, superheat region, and condenser pressure.
Heat is added as compressed liquid warms, boils, and sometimes superheats.
Heat is rejected as low-pressure vapor condenses across the saturation region.
The area inside the Rankine loop also represents net work, but its shape is not the ideal Carnot rectangle.
This diagram makes clear why raising the average temperature of heat addition improves Rankine efficiency.

## Design Levers

Carnot suggests two broad levers: raise the hot temperature or lower the cold temperature.
Rankine engineering translates those levers into concrete design choices.
Higher boiler pressure can raise the average heat-addition temperature.
Higher turbine inlet temperature through superheating increases work output and reduces wetness.
Lower condenser pressure increases turbine expansion work but demands better cooling and may increase moisture.
Reheat sends partially expanded steam back to the boiler before further turbine expansion.
Regenerative feedwater heating extracts steam from the turbine to preheat feedwater.
Supercritical operation eliminates the distinct boiling plateau and can improve efficiency.
Organic Rankine cycles select fluids better suited to low-temperature heat sources.
Each improvement moves the practical Rankine cycle closer to, but never beyond, the relevant Carnot boundary.

## When to Use Each Concept

Use Carnot analysis when establishing an upper bound or explaining why 100 percent thermal efficiency is impossible.
Use Carnot analysis when evaluating the quality of heat at different temperatures.
Use Rankine analysis when estimating steam-plant work, heat rate, condenser duty, turbine outlet moisture, or pump power.
Use Rankine analysis when comparing reheat, regeneration, superheat, and condenser-pressure choices.
In education, Carnot usually comes first because it defines the second-law limit.
Rankine follows because it shows how vapor power is actually implemented.
Together they form a useful pair: one supplies the ceiling, the other supplies the engineering map.

## See Also

- [[carnot-cycle-and-heat-engines]]
- [[rankine-cycle]]
- [[laws-of-thermodynamics]]
