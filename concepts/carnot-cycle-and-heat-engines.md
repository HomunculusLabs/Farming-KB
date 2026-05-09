---
title: "Carnot Cycle and query-why-cant-heat-engines-be-100-percent-efficient"
type: concept
category: thermodynamics
related:
  - laws-of-thermodynamics
  - heat-transfer-mechanisms
  - navier-stokes-equations
tags: [thermodynamics, heat-engine, carnot, efficiency, energy-conversion, physics]
created: 2026-05-02
updated: 2026-05-06
type: concept
sources: []
---

The Carnot cycle is the foundational theoretical model of heat engine operation, establishing the maximum possible efficiency any engine can achieve when converting [[phase-change-materials-thermal-energy-storage]] into mechanical work. Proposed by Nicolas Léonard Sadi Carnot in 1824, it remains the benchmark against which all real engines are measured and was instrumental in the development of the second law of thermodynamics and the concept of entropy.

## Historical Context

Sadi Carnot (1796–1832) published *Réflexions sur la puissance motrice du feu* (“Reflections on the Motive Power of Fire”) in 1824 at age 28. The work received little attention during his lifetime — fewer than 600 copies were printed, and Carnot died of cholera in 1832 at age 36. His father, Lazare Carnot, was a noted mathematician, engineer, and political figure (“Organizer of Victory” during the French Revolution) who had written on machine efficiency and the conservation of mechanical energy, deeply influencing Sadi’s thinking.

Carnot worked entirely within the caloric theory of heat, which held that heat was a conserved, weightless fluid called “caloric” that flowed from hotter to colder bodies. Although this theory was incorrect (the kinetic theory of heat eventually replaced it), Carnot’s conclusions about maximum engine efficiency turned out to be entirely correct — a remarkable case of arriving at the right answer through flawed reasoning. His key insight was that work production requires a temperature difference: heat flowing from hot to cold, analogous to water falling from a higher to a lower elevation to turn a waterwheel. He wrote: “The motive power of heat is independent of the agents employed to realize it; its quantity is fixed solely by the temperatures of the bodies between which is effected, finally, the transfer of the caloric.”

Émile Clapeyron reformulated Carnot’s verbal arguments into mathematical graphical form using pressure-volume indicator diagrams in 1834. Rudolf Clausius (1850) and William Thomson, Lord Kelvin (1851), independently recognized that Carnot’s results required abandoning caloric theory while preserving his fundamental insight about the directionality of heat flow, leading to the formulation of the second law of thermodynamics. Carnot’s private notes (discovered in 1878) revealed he had himself abandoned caloric theory and correctly anticipated the equivalence of heat and work decades before Joule’s experiments.

## The Four Stages of the Carnot Cycle

The cycle operates between two thermal reservoirs at absolute temperatures T_H (hot) and T_C (cold), consisting of two isothermal and two adiabatic (isentropic) reversible processes:

**Stage 1→2: Isothermal Expansion at T_H.** The working gas is placed in thermal contact with the hot reservoir and expands quasi-statically, absorbing heat Q_H. For an ideal gas, internal energy change ΔU = 0 during isothermal processes, so all absorbed heat converts directly to work: Q_H = W₁₂ = nRT_H · ln(V₂/V₁). On a PV diagram this traces the hyperbolic isotherm PV = nRT_H from high pressure and small volume to lower pressure and larger volume.

**Stage 2→3: Adiabatic (Isentropic) Expansion.** The gas is thermally insulated and continues to expand. No heat is exchanged (Q = 0), so all work done comes at the expense of internal energy. Temperature drops from T_H to T_C following the steeper adiabat PV^γ = constant, where γ = C_p/C_v is the heat capacity ratio. On a TS diagram this appears as a vertical line (constant entropy).

**Stage 3→4: Isothermal Compression at T_C.** The gas contacts the cold reservoir and is compressed isothermally, rejecting heat Q_C to the cold reservoir. Since ΔU = 0 again, work is done on the gas: Q_C = nRT_C · ln(V₃/V₄). Volume decreases from V₃ to V₄.

**Stage 4→1: Adiabatic (Isentropic) Compression.** The gas is again insulated and compressed adiabatically. Temperature rises from T_C back to T_H, closing the cycle. The adiabatic constraints couple the volume ratios: V₂/V₁ = V₃/V₄, and entropy values satisfy S₁ = S₄ and S₂ = S₃ throughout.

On a TS diagram, the Carnot cycle forms a perfect rectangle — the simplest and most elegant representation. The top and bottom edges are horizontal isotherms at T_H and T_C; the left and right edges are vertical isentropes. The enclosed area equals the net work output: W_net = (T_H − T_C)(S₂ − S₁) = Q_H − Q_C.

## Key Equations and Relationships

The core quantitative relationships governing the Carnot cycle and related thermodynamic cycles are summarized below:

| Quantity | Formula | Notes |
|----------|---------|-------|
| Carnot efficiency | η = 1 − T_C/T_H | Absolute temperatures (K); independent of working fluid |
| Net work per cycle | W_net = Q_H − Q_C = (T_H − T_C)ΔS | Enclosed area on PV or TS diagram |
| Heat absorbed (hot) | Q_H = T_H(S₂ − S₁) | During isothermal expansion at T_H |
| Heat rejected (cold) | Q_C = T_C(S₂ − S₁) | During isothermal compression at T_C |
| COP (refrigerator) | COP_R = T_C/(T_H − T_C) | Heat removed per unit work input |
| COP (heat pump) | COP_HP = T_H/(T_H − T_C) | Heat delivered per unit work input |
| Otto efficiency | η = 1 − 1/r^(γ−1) | r = compression ratio, γ = C_p/C_v |
| Brayton efficiency | η = 1 − 1/r_p^((γ−1)/γ) | r_p = pressure ratio |

The relationship COP_HP = COP_R + 1 always holds. Both COPs approach infinity as T_H approaches T_C (zero temperature difference), but real systems always have significant ΔT, keeping COPs finite and practical.

## Carnot Efficiency

The efficiency formula η_Carnot = 1 − T_C/T_H follows from the first law of thermodynamics. Net work W_net = Q_H − Q_C, so efficiency η = W_net/Q_H = 1 − Q_C/Q_H. For the Carnot cycle, Q_H = T_H·ΔS and Q_C = T_C·ΔS, therefore Q_C/Q_H = T_C/T_H. Crucially, this efficiency is independent of the working substance — it applies equally to ideal gases, steam, mercury vapor, or any other medium. This universality is what makes the Carnot cycle so powerful as a theoretical benchmark, and it is the reason the Carnot efficiency depends only on reservoir temperatures, not on engine design details.

Numerical examples illustrate the constraints imposed by the Carnot limit. A steam power plant with T_H = 873 K (600°C) and T_C = 313 K (40°C) achieves η = 64.2% maximum. An automotive engine with T_H = 2400 K (peak combustion) and T_C = 300 K (ambient) has η = 87.5% Carnot limit, though actual Otto engines deliver only 25–35%. An engine between equal-temperature reservoirs produces zero work (η = 0); achieving 100% efficiency would require T_C = 0 K, forbidden by the third law.

To maximize real-world efficiency, engineers pursue higher T_H (advanced materials, blade cooling) and lower T_C (improved condensers, [[bloomfield-mushroom-evaporative-cooling-fungal-frigidity]]), while minimizing internal irreversibilities through regenerative feedwater heating, reheat cycles, and multi-stage compression with intercooling. The gap between Carnot and actual efficiency serves as a diagnostic tool — a large gap indicates opportunities for thermodynamic improvement.

## Carnot’s Theorem

Carnot’s theorem establishes two fundamental results: (1) no heat engine operating between two reservoirs can exceed the efficiency of a Carnot engine between those same reservoirs; and (2) all reversible engines between identical reservoirs share the same efficiency regardless of working substance. The classical proof by contradiction assumes a super-efficient engine E exists and couples it with a reversed Carnot engine C running as a heat pump between the same reservoirs. The combined system would transfer heat from cold to hot with no net work input, violating the Kelvin-Planck statement of the second law.

An important corollary states that all irreversible engines have strictly lower efficiency than reversible ones operating between the same reservoirs. The **second law efficiency** (effectiveness) quantifies this gap: η_II = η_actual / η_Carnot. A modern combined cycle plant with η_actual ≈ 64% operating between T_H ≈ 1873 K and T_C ≈ 313 K gives η_Carnot ≈ 83.3%, yielding η_II ≈ 0.77. This reveals that roughly 23% of available energy conversion potential is lost to irreversibilities even in the best commercial systems.

## The Carnot Engine as Idealization

The Carnot engine is a thought experiment that cannot be physically constructed. Its requirements are mutually incompatible with real-world operation: quasi-static processes maintaining mechanical, thermal, and chemical equilibrium at every instant (requiring infinite time); zero friction in all moving parts; heat transfer only at zero temperature difference (requiring infinite heat exchanger area); perfectly insulating walls during adiabatic stages; and complete absence of irreversibilities from combustion, mixing, throttling, or fluid turbulence.

The inevitable consequence is zero power output: P = W/t → 0 as t → ∞. Real engines must sacrifice some efficiency to produce useful power at finite rates. This fundamental trade-off between efficiency and power output is the subject of finite-time thermodynamics and endoreversible thermodynamics, which seek to optimize real engine performance under practical constraints such as finite heat transfer rates, finite compression and expansion speeds, and non-zero pressure drops.

## Practical Cycles Compared to Carnot

**Otto cycle** (spark-ignition gasoline engines): Two isochoric (constant volume) and two adiabatic processes modeling the four strokes of a piston engine. Efficiency η = 1 − 1/r^(γ−1), where r is compression ratio (typically 8:1 to 13:1, limited by knock). At r = 10, γ = 1.4: η_ideal = 60.2%. Actual brake thermal efficiency: 25–35%. The gap arises from non-isothermal heat addition, irreversible combustion, heat loss through cylinder walls, finite-time processes, and throttling losses.

**Diesel cycle** (compression-ignition engines): Similar to Otto but with constant-pressure heat addition as fuel burns during expansion. Higher compression ratios (14:1 to 25:1, no knock constraint) yield η_ideal ≈ 65% at r = 20, cutoff ratio 2. Actual: 35–45%, with additional irreversibility from fuel-air mixing during injection.

**Brayton cycle** (gas turbines and jet engines): Two isobaric (constant pressure) and two adiabatic processes in continuous flow. η = 1 − 1/r_p^((γ−1)/γ), where r_p is pressure ratio. At r_p = 20: η_ideal = 57.6%. Simple cycle: 30–40%. Combined Brayton-Rankine cycles recover exhaust heat in a heat recovery steam generator (HRSG) to reach 63–64% actual — the highest of any commercial power generation technology.

**[[query-why-cant-heat-engines-be-100-percent-efficient]]

- [[fracture-mechanics-engineering-materials]]

- [[fenton-reaction-chemistry-and-biochemistry]]

## See Also

- [[sadi-carnot]]
