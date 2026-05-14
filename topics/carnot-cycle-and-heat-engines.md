---
title: "Carnot Cycle and query-why-cant-heat-engines-be-100-percent-efficient"
type: topic
category: thermodynamics
tags: [thermodynamics, heat-engines, carnot-cycle, entropy, energy-conversion]
related: [rankine-cycle, laws-of-thermodynamics, heat-transfer-mechanisms]
created: 2026-05-02
---

# Carnot Cycle and Heat Engines

The Carnot cycle is the ideal reversible heat-engine cycle used to define the upper limit on thermal efficiency.
It describes a theoretical engine operating between a hot reservoir and a cold reservoir.
The cycle converts part of the heat flowing from high temperature to low temperature into mechanical work.
Its importance is not that it represents a practical machine, but that it sets a boundary no practical machine can exceed.
For this reason the Carnot cycle is central to thermodynamics, power engineering, refrigeration, and [[mollison-designers-home-energy-conservation-and-solar-heating]] plus entropy production.
Kelvin used Carnot's result to define an absolute thermodynamic temperature scale.
Together these developments made the Carnot cycle more than an engine model: it became a statement about nature's limits.

## Heat Engines in General

A heat engine is any cyclic device that receives heat, produces work, and rejects unused heat.
Common examples include steam turbines, internal-combustion engines, gas turbines, and Stirling engines.
Each operates by repeatedly returning a working substance or working system to its initial thermodynamic state.
Because the system returns to its starting state, its net internal-energy change over a full cycle is zero.
The first law therefore requires net work output to equal heat input minus heat rejected.
The second law requires some heat rejection whenever the engine exchanges heat with only two finite-temperature reservoirs.
No cyclic heat engine can convert all absorbed heat into work while producing no other effect.
This is the Kelvin-Planck statement of the second law.
The Carnot cycle expresses the most efficient version of that permitted heat-to-work conversion.

## The Four Reversible Processes

The ideal Carnot heat engine contains four internally and externally reversible processes.
First, the working fluid expands isothermally at the hot-reservoir temperature T_H.
During this stage it absorbs heat Q_H while doing work on its surroundings.
For an ideal gas the internal energy does not change during isothermal expansion, so absorbed heat equals expansion work.
Second, the working fluid expands adiabatically and reversibly.
No heat crosses the boundary, and the gas cools from T_H to T_C as it performs additional work.
This stage is also called isentropic expansion because entropy remains constant in a reversible adiabatic process.
Third, the working fluid is compressed isothermally at the cold-reservoir temperature T_C.
Heat Q_C is rejected to the cold reservoir as work is done on the fluid.
Fourth, the fluid is compressed adiabatically and reversibly until its temperature returns to T_H.
The final state matches the initial state, closing the cycle.
On a temperature-entropy diagram these four steps form a rectangle.
The horizontal sides are the isothermal heat-transfer processes.
The vertical sides are the isentropic compression and expansion processes.
The area enclosed by the rectangle equals the net work delivered per cycle.

## Efficiency

Thermal efficiency is the ratio of net work output to heat absorbed from the hot reservoir.
For any cyclic heat engine, efficiency equals 1 minus rejected heat divided by supplied heat.
For the reversible Carnot cycle, the heat exchanges occur at constant temperatures.
The entropy gained during hot-side heat absorption equals Q_H divided by T_H.
The entropy lost during cold-side heat rejection equals Q_C divided by T_C.
Because the cycle is reversible and returns to its initial state, these entropy changes are equal in magnitude.
It follows that Q_C/Q_H equals T_C/T_H.
The Carnot efficiency is therefore η = 1 - T_C/T_H, with temperatures measured on an absolute scale.
The formula depends only on reservoir temperatures and not on working fluid, engine size, or mechanism.
Raising T_H increases the theoretical work fraction available from a unit of heat.
Lowering T_C also increases the theoretical work fraction, though condenser and environmental limits usually constrain it.
An engine operating between equal temperatures has zero Carnot efficiency because heat has no thermodynamic fall to exploit.
An engine reaching 100 percent efficiency would require T_C to be absolute zero, which cannot be achieved in finite operations.

## Carnot's Theorem

Carnot's theorem states that no engine between two reservoirs can be more efficient than a reversible engine between those reservoirs.
It also states that all reversible engines between the same two reservoirs have the same efficiency.
The usual proof is a contradiction argument.
If an irreversible or special engine exceeded Carnot efficiency, it could drive a reversed Carnot refrigerator.
The combination would move heat from cold to hot without net work input.
That result would violate the second law.
The theorem makes reversibility the criterion for maximum possible performance.
It also explains why the Carnot limit is universal rather than tied to steam, air, or any particular substance.
Real engines fall below the Carnot limit because they contain friction, turbulence, finite-rate heat transfer, combustion losses, leakage, throttling, and pressure drops.
The ratio of actual efficiency to Carnot efficiency is often called second-law efficiency or exergetic efficiency.

## Entropy and Irreversibility

The Carnot cycle helped motivate the formal definition of entropy.
In a reversible heat transfer, entropy change equals heat transferred divided by absolute temperature.
For any real process, entropy is generated by irreversibility.
Entropy generation represents lost opportunity to convert energy into useful work.
Friction converts organized mechanical energy into disordered internal energy.
Heat transfer across a finite temperature difference destroys available work even though total energy is conserved.
Mixing, unrestrained expansion, electrical resistance, chemical reaction, and shock waves all create entropy.
A perfect Carnot engine avoids all such effects, which is why it reaches the theoretical boundary.
However, avoiding them completely requires quasi-static operation and infinitesimal driving differences.
That condition implies vanishing power output, so useful engines must trade some efficiency for finite rate of operation.

## Relation to Practical Power Cycles

The [[jadam-ambient-temperature-principle]].
This idea underlies [[exergy-analysis]], which measures maximum useful work relative to the environment.
Power-plant designers use Carnot reasoning to justify higher boiler temperatures, lower condenser temperatures, reheat, regeneration, and combined cycles.
Materials engineers use it to understand why hotter turbines promise higher efficiency but demand creep-resistant alloys and cooling systems.
Building engineers use the reversed cycle to evaluate heat pumps and refrigeration equipment.
Environmental analysts use it to explain waste heat, cooling-water demand, and the limits of thermal power generation.
The Carnot cycle is therefore both a historical milestone and a practical compass.
It does not tell engineers how to build a machine directly.
It tells them what losses matter, what improvements are thermodynamically meaningful, and what goals are impossible.
## See Also

- [[laws-of-thermodynamics]]
- [[heat-exchanger-effectiveness-ntu]]
- creep deformation high temperature materials
