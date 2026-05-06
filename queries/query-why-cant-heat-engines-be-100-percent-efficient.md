---
title: "Why can't heat engines be 100 percent efficient?"
type: query
question: "Why can't heat engines be 100 percent efficient?"
tags: [thermodynamics, heat-engines, carnot-cycle, entropy, efficiency]
related: [carnot-cycle-and-heat-engines, rankine-cycle, laws-of-thermodynamics]
created: 2026-05-02
updated: 2026-05-06
sources: []
---

# Why can't heat engines be 100 percent efficient?

## Short Answer

Heat engines cannot be 100 percent efficient because the second law of thermodynamics requires them to reject some heat.
A cyclic engine can produce work only when heat flows from a hotter source toward a colder sink.
The engine converts part of that heat flow into work, but it cannot convert all of it while returning to its starting state.
The ideal upper limit is the Carnot efficiency: η = 1 - T_C/T_H.
Here T_H is the hot-reservoir temperature and T_C is the cold-reservoir temperature, both in kelvin.
To make η equal 1, the cold reservoir would have to be at 0 K, or absolute zero.
Real machines also contain many additional losses.

## What does "100 percent efficient" mean?

For a heat engine, thermal efficiency means net work output divided by heat absorbed from the hot source.
An engine with 100 percent efficiency would turn every unit of absorbed heat into useful work.
It would reject no heat to the surroundings.
That idea sounds like ordinary conservation of energy, but conservation of energy alone is not enough.
The first law says energy is conserved.
The second law says not all energy has the same ability to become work.
Low-temperature heat is less useful than high-temperature heat because it has less exergy relative to the environment.

## Why must some heat be rejected?

A heat engine operates in a cycle.
At the end of each cycle, the working fluid or working system must return to its initial state.
That means its internal energy and entropy cannot keep increasing indefinitely from cycle to cycle.
When the engine absorbs heat from the hot reservoir, it also receives entropy.
To return to its initial state, the working substance must get rid of that entropy.
The usual way it does so is by rejecting heat to a colder reservoir.
If no heat were rejected, entropy balance would fail for a cyclic device producing only work from a single heat reservoir.
That is why the Kelvin-Planck statement of the second law forbids a perfect one-reservoir heat engine.

## What does the Carnot limit say?

The [[carnot-cycle-and-heat-engines]] gives the best possible efficiency for any engine between two temperatures.
Its efficiency is η = 1 - T_C/T_H.
If the hot reservoir is 600°C, or 873 K, and the cold reservoir is 40°C, or 313 K, the ideal limit is about 64 percent.
No engine operating between those temperatures can exceed that limit.
A real steam plant using the [[rankine-cycle]] will be lower because it is not perfectly reversible.
The Carnot formula also shows why using Celsius directly is wrong.
Thermodynamic efficiency depends on absolute temperature ratios, so kelvin must be used.

## Why doesn't better engineering remove the limit?

Engineering can reduce avoidable losses, but it cannot repeal the second law.
Better bearings reduce friction.
Better turbines reduce aerodynamic losses.
Better heat exchangers reduce temperature differences and pressure drops.
Higher-temperature materials can raise the hot-side temperature.
Improved condensers can lower the cold-side temperature.
All of these changes can improve efficiency.
Even a flawless reversible engine still has to reject heat unless its cold reservoir is at absolute zero.

## What losses make real engines worse than Carnot?

Real engines generate entropy internally.
Friction converts organized motion into heat.
Combustion occurs irreversibly through mixing and chemical reaction.
[[heat-transfer-mechanisms]] requires finite temperature differences, which destroy available work.
Turbines, pistons, pumps, compressors, valves, seals, and ducts all have mechanical or fluid losses.
Steam plants have pressure drops in boilers, reheaters, condensers, and piping.
Internal-combustion engines lose heat through cylinder walls and exhaust.
These losses explain why actual efficiencies can be far below the Carnot ceiling.

## Does a heat pump violate this rule?

No.
A heat pump or refrigerator is not a heat engine producing work from heat.
It consumes work to move heat from a colder place to a warmer place.
Its coefficient of performance can be greater than one because the useful output is moved heat, not created work.
For example, a heat pump may deliver three units of heat indoors for one unit of electrical work.
That does not mean it is 300 percent efficient as a heat engine.
It means it used work to transfer environmental heat in the desired direction.
The reversed Carnot cycle sets the ideal limit for heat pumps and refrigerators.

## Practical takeaway

A heat engine needs both a hot source and a cold sink.
The temperature difference provides the opportunity to produce work.
The cold sink also receives the entropy that must leave the working substance each cycle.
The hotter the source and the colder the sink, the higher the possible efficiency.
Real designs then lose additional potential through irreversibility and finite-rate operation.
So the reason heat engines cannot be 100 percent efficient is not merely bad engineering.
It is a fundamental consequence of entropy, absolute temperature, and the second law of thermodynamics.

## See Also

- [[carnot-cycle-and-heat-engines]]
- [[rankine-cycle]]
- [[laws-of-thermodynamics]]
