---
title: "Phase-Change Materials for Thermal Energy Storage"
aliases: [pcm, latent-heat-storage, phase-change-energy-storage]
tags: [materials-science, thermodynamics, energy-storage, heat-transfer, engineering]
created: 2026-05-02
type: concept
sources: []
---

## Definition

Phase-change materials are substances chosen because they absorb or release large amounts of heat while melting, freezing, crystallizing, or otherwise changing phase.

Their engineering value comes from latent heat: energy can enter or leave the material while temperature remains close to the phase transition point.

A water-ice mixture near 0 °C is the familiar example, but practical systems also use paraffins, fatty acids, salt hydrates, eutectic mixtures, metals, polymers, and encapsulated composites.

In thermal energy storage, a PCM acts like a thermal buffer that smooths heat supply and demand across hours, daily cycles, or intermittent operating conditions.

The material is not a battery in the electrochemical sense; it stores energy as phase equilibrium rather than as separated charge or chemical potential.

## Thermodynamic Basis

Sensible heat storage raises or lowers the temperature of a mass according to its heat capacity.

Latent heat storage instead uses an enthalpy change associated with a phase transition, often allowing far higher heat storage density over a narrow temperature interval.

The useful storage capacity is approximately the mass of PCM multiplied by its latent heat, plus smaller sensible heat terms before and after the transition.

A good PCM therefore has a transition temperature matched to the application, such as comfort cooling near room temperature or process heat near an industrial set point.

The transition should be repeatable, reversible, and narrow enough that stored heat can be discharged at a useful temperature rather than spread across an overly broad range.

Subcooling, hysteresis, and incomplete crystallization reduce effective capacity because the material may fail to freeze or melt when the system expects it to.

## Classes of Materials

Organic PCMs include paraffin waxes, fatty acids, and polyethylene glycols; they tend to be chemically stable and congruent melting but can have low thermal conductivity and flammability concerns.

Inorganic PCMs include salt hydrates, nitrates, chlorides, and metal alloys; they often have high volumetric storage density but may suffer from corrosion, phase segregation, or supercooling.

Eutectic PCMs combine two or more compounds to create a tailored melting point lower than or different from the individual components.

Solid-solid PCMs store heat through crystal-structure changes and can avoid liquid leakage, though their latent heats are usually smaller than solid-liquid transitions.

Metallic PCMs such as aluminum-silicon alloys operate at high temperature and are considered for concentrated solar power, waste heat recovery, and compact industrial storage.

Composite PCMs embed the active material in graphite, metal foam, expanded vermiculite, polymer networks, or porous ceramics to improve heat transfer and shape stability.

## Selection Criteria

The most important criterion is transition temperature, because a PCM outside the needed range behaves mostly like an ordinary heat capacity.

Latent heat per unit mass and per unit volume determine storage density and therefore tank size, wall area, and system cost.

Thermal conductivity controls how fast heat can be charged and discharged; many organics store plenty of energy but move heat slowly without fins or conductive additives.

Cycling stability matters because a building panel, cold-chain pack, or industrial thermal battery may experience thousands of melt-freeze cycles.

Compatibility with containment materials is essential: salt hydrates can corrode metals, and organic liquids can swell some polymers.

Safety screening includes flash point, toxicity, vapor pressure, gas evolution, freeze expansion, and behavior during fire exposure.

Cost is not just the price per kilogram; it includes encapsulation, heat exchangers, installation, maintenance, and degradation over lifetime.

## Encapsulation and Containment

Macroencapsulation packages PCM in pouches, tubes, plates, spheres, or panels large enough to install as discrete modules.

Microencapsulation surrounds tiny PCM droplets with polymer or inorganic shells, allowing the material to be mixed into gypsum board, textiles, coatings, or slurries.

Shape-stabilized PCMs retain liquid phase inside a porous matrix or cross-linked polymer so that melting does not create bulk leakage.

Containment must accommodate expansion during phase change, repeated thermal strain, chemical attack, and the possibility of local overheating.

Heat exchanger geometry is often as important as PCM chemistry because stored heat is useless if it cannot be moved into or out of the phase-change volume quickly.

Designers use fins, graphite foams, cascaded melting points, shell-and-tube layouts, and forced convection loops to reduce charging time.

## Applications

Building envelopes use PCMs in wallboards, ceiling tiles, concrete, or ventilation units to reduce indoor temperature swings and shift cooling loads away from peak hours.

Cold-chain logistics use PCM packs tuned to vaccine, food, or pharmaceutical temperature ranges, providing more stable control than plain ice when 0 °C is not the desired set point.

Electronics thermal management uses PCMs as transient heat sinks for pulsed loads, absorbing spikes while fans, cases, or heat pipes remove energy more slowly.

Solar thermal and district heating systems use PCMs to store daytime heat for evening demand or to increase storage density in tanks.

Industrial waste heat recovery can pair PCMs with batch processes that release heat intermittently but require steady preheating elsewhere.

Textiles, protective equipment, and footwear use microencapsulated PCMs to moderate short-term thermal discomfort, although total storage mass is limited.

High-temperature PCMs are studied for space systems, thermal protection, and concentrated solar receivers where compact storage at hundreds of degrees Celsius is valuable.

## Engineering Limitations

Low thermal conductivity is the most common bottleneck and can make nominal storage density misleading when the interior melts or freezes too slowly.

Phase segregation occurs when components of a salt hydrate or eutectic separate during cycling, changing the composition that actually crystallizes later.

Supercooling delays solidification below the nominal freezing point, so the PCM may remain liquid and fail to release heat at the required temperature.

Volume change can stress containers, rupture capsules, or create voids that reduce thermal contact after repeated cycles.

Flammable organic PCMs require careful fire design when installed in occupied buildings or near electrical equipment.

Materials advertised by melting point alone should be treated skeptically; real performance requires differential scanning calorimetry, cycling tests, leakage tests, and system-level heat transfer measurements.

## Design Strategies

Cascaded PCM systems place several materials with different transition temperatures in series so heat is absorbed or released over a broader useful range.

Conductive enhancement adds expanded graphite, carbon fibers, metal foams, fins, or nanoparticles, trading some storage density for faster heat flow.

Nucleating agents reduce supercooling by providing favorable sites for crystallization.

Thickening agents and porous supports reduce leakage and phase separation, especially in hydrated salts and wax composites.

Control systems may deliberately leave part of the PCM unmelted or uncrystallized to preserve response capacity for the next heat pulse.

The best design often combines a modest PCM volume with conventional insulation, heat pipes, sensors, and predictive control rather than relying on the material alone.

## Related Concepts

Phase-change storage connects thermodynamics, heat-transfer mechanisms, and materials compatibility more tightly than many energy technologies.

It is especially useful where the desired output temperature is fixed, because latent heat naturally holds the system near a plateau.

It is less useful where the application demands high power density, very fast response, or broad temperature lift without an auxiliary heat pump.

Important neighboring topics include [[heat-transfer-mechanisms]], [[heat-exchanger-effectiveness-ntu]], thermodynamic entropy, thermal runaway, and energy storage systems.

## References

Standard references include heat-transfer textbooks, thermal energy storage handbooks, and materials data measured by differential scanning calorimetry.

Useful web overviews include the Wikipedia articles on phase-change materials, latent heat, and thermal energy storage, which summarize classifications, selection criteria, and common applications.

Engineering evaluation should always rely on measured data for the specific supplier grade, because additives, purity, and encapsulation method can dominate field performance.
- [[permaculture-designers-manual-climate-factors]]
- [[low-energy-futures-in-permaculture]]
- [[mollison-designers-climate-zone-1-intensive-garden]]
