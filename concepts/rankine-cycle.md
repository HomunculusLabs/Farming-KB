---
title: "Rankine Cycle"
aliases: [steam power cycle, vapor power cycle, Clausius-Rankine cycle]
tags: [thermodynamics, power-engineering, heat-engines, energy, engineering]
created: 2026-05-02
updated: 2026-05-06
type: concept
sources: []
---

## Definition

The Rankine cycle is the idealized thermodynamic cycle used to model steam power plants and many vapor power systems.

It converts heat addition into net work by pumping a liquid working fluid, boiling it, expanding the vapor through a turbine, and condensing it back to liquid.

Water is the most common working fluid in large plants because it is cheap, chemically familiar, and has favorable phase-change properties.

## Four Ideal Processes

Process 1 to 2 is pumping of saturated or subcooled liquid from condenser pressure to boiler pressure.

Process 2 to 3 is heat addition at high pressure in a boiler, heat recovery steam generator, reactor steam generator, or solar receiver.

During this step the working fluid is heated, vaporized, and often superheated before entering the turbine.

Process 3 to 4 is expansion through a turbine, producing shaft work as pressure and temperature fall.

Process 4 to 1 is heat rejection in a condenser, returning the vapor or vapor-liquid mixture to liquid at low pressure.

The condenser closes the cycle and creates the low turbine exhaust pressure that helps extract work.

## Energy Accounting

Rankine analysis usually treats each component as a steady-flow control volume.

Specific enthalpy differences determine turbine work, pump work, boiler heat input, and condenser heat rejection.

Turbine work is approximately h3 minus h4, while pump work is approximately h2 minus h1.

Boiler heat input is h3 minus h2, and condenser heat rejection is h4 minus h1.

Thermal efficiency is net work output divided by heat input, or one minus rejected heat over supplied heat.

The pump work term is often small but should not be ignored in high-pressure cycles.

## Temperature and Pressure Choices

Raising boiler pressure can increase mean heat-addition temperature and improve efficiency.

Raising turbine inlet temperature by superheating steam also improves efficiency and reduces moisture at the turbine exit.

Lowering condenser pressure increases turbine expansion ratio and work output, but it also increases moisture risk and requires colder heat rejection.

Material limits constrain maximum temperature because boiler tubes, turbine blades, and headers must resist creep, oxidation, and fatigue.

## Real-Cycle Irreversibilities

Real pumps and turbines are not isentropic; friction, turbulence, leakage, and finite-rate processes generate entropy.

Pressure drops occur in boilers, reheaters, condensers, piping, valves, and heat exchangers.

Heat transfer across finite temperature differences destroys available work even when total energy is conserved.

## Reheat

Reheat cycles expand steam in a high-pressure turbine, return it to the boiler for additional heating, and expand it again in lower-pressure stages.

Reheat increases the average temperature of heat addition and reduces moisture content in the final turbine stages.

It is especially valuable in high-pressure steam plants where a single long expansion would produce excessive wetness.

## Regeneration

Regenerative feedwater heating extracts steam from intermediate turbine stages to preheat feedwater before it reaches the boiler.

This raises the average temperature at which external heat is added to the cycle.

Open feedwater heaters mix extraction steam directly with feedwater at a common pressure.

Closed feedwater heaters transfer heat across tubes without mixing the extraction steam and feedwater streams.

## Organic Rankine Cycles

Organic Rankine cycles replace water with an organic fluid selected for low or moderate heat-source temperatures.

They are used with geothermal brines, industrial waste heat, biomass systems, solar thermal collectors, and engine exhaust recovery.

Some organic fluids produce dry or isentropic expansion behavior, reducing the risk of turbine blade erosion from liquid droplets.

## Supercritical and Advanced Cycles

Supercritical steam cycles operate above the critical pressure of water, eliminating a distinct boiling plateau in the boiler.

They can achieve higher efficiencies by increasing the mean temperature of heat addition.

Combined-cycle plants use a gas turbine topping cycle and a Rankine bottoming cycle to recover exhaust heat.

## Equipment Interpretation

The pump is small in power demand but critical for pressure control and feedwater delivery.

The boiler or steam generator is a coupled heat-transfer, combustion, nuclear, or solar receiver system rather than a single ideal component.

The turbine converts enthalpy drop into rotating shaft power through staged nozzles and blades.

The condenser is a heat sink interface and often a major determinant of plant location and water use.

## Practical Metrics

Heat rate expresses how much fuel energy is required per unit electrical output.

Back work ratio is small for steam Rankine cycles but much larger for gas cycles such as Brayton systems.

Specific steam consumption relates mass flow rate to power output and is useful for turbine sizing.

Moisture fraction at turbine exit affects erosion, efficiency, and maintenance intervals.

## Common Pitfalls

Confusing Carnot efficiency with achievable Rankine efficiency hides the effects of finite heat transfer and equipment limits.

Ignoring condenser pressure can miss one of the strongest influences on turbine work and plant heat rate.

Using ideal isentropic expansion without moisture checks can produce turbine outlet states that are mechanically unacceptable.

## See Also

- [[carnot-cycle-and-heat-engines]]
- [[heat-transfer-mechanisms]]
- [[heat-exchanger-effectiveness-ntu]]
- [[creep-deformation-high-temperature-materials]]
- [[corrosion-electrochemistry]]
