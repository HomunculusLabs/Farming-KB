---
title: "Fatigue Crack Growth"
aliases: [fatigue crack propagation, crack growth rate, Paris law fatigue]
tags: [materials-science, fracture-mechanics, fatigue, engineering, reliability]
created: 2026-05-02
updated: 2026-05-06
type: concept
sources: []
---

## Overview
Fatigue crack growth is the progressive extension of a crack under repeated loading.
It is central to damage tolerant design because many structures contain small flaws before service begins.
A component may survive millions of cycles while a crack is microscopic, then fail rapidly once the crack reaches a critical size.
The subject connects [[fracture-mechanics-engineering-materials]], [[continuum-mechanics]], [[dislocation-theory-crystal-plasticity]], inspection planning, and reliability engineering.
Unlike static strength checks, fatigue crack growth treats failure as a history-dependent process driven by load cycles.
The practical question is not only whether a crack is present, but how fast it will grow under the expected spectrum of stresses.
Aircraft fuselages, bridges, pressure vessels, shafts, rails, turbine disks, and offshore structures are common damage-tolerance examples.

## Stages of Fatigue Damage
Fatigue is often divided into crack initiation, stable crack growth, and final fracture.
Initiation begins at stress concentrations such as holes, weld toes, corrosion pits, inclusions, machining marks, or persistent slip bands.
Small cracks can behave differently from long cracks because their plastic zone and local microstructure are comparable to crack length.
Stable growth occurs when each load cycle advances the crack by a very small increment.
Final fracture occurs when the applied stress intensity reaches the material fracture toughness.
The transition between stages is gradual in real components and depends on surface finish, residual stress, environment, and load ratio.
For conservative life management, engineers often assume a detectable initial flaw and calculate the cycles required to reach critical size.

## Stress Intensity Range
Linear elastic fracture mechanics describes the near-tip field with the stress intensity factor K.
Under cyclic loading, the important driving force is the range delta K between maximum and minimum values in a cycle.
For many geometries, delta K equals a geometry factor times the stress range times the square root of pi times crack length.
As a crack grows longer, the same nominal stress range produces a larger delta K.
This feedback explains why fatigue crack growth often accelerates with crack length.
The stress ratio R, defined as minimum stress divided by maximum stress, changes crack closure and the effective driving force.
Tensile mean stresses usually increase growth rates, while compressive portions of a cycle may partially close the crack.

## Paris Law Region
The Paris-Erdogan relation states that da/dN equals C times delta K raised to the exponent m.
Here da/dN is crack extension per cycle, while C and m are empirical material and environment constants.
On a log-log plot of growth rate versus delta K, the Paris region appears approximately linear.
The law is useful because it converts crack growth into an integrable life prediction problem.
It does not describe the entire fatigue curve, and careless extrapolation outside its range is a common engineering error.
Typical metallic materials have Paris exponents around 2 to 4, but high-strength brittle alloys can show steeper slopes.
Test data must be generated for the relevant heat treatment, environment, temperature, thickness, stress ratio, and frequency.

## Threshold and Near-Threshold Growth
At low delta K, many long cracks approach a threshold below which growth is extremely slow.
The threshold is not a universal constant; it depends on crack closure, load ratio, environment, grain size, and measurement method.
Short cracks may grow below the long-crack threshold because they do not experience the same closure mechanisms.
This short-crack effect is important for high-cycle fatigue, where much of life may be spent before a long crack is detectable.
Surface cracks initiated at notches can therefore be more dangerous than long-crack data alone suggests.
Near-threshold testing requires careful control because very slow rates are sensitive to oxide debris, roughness-induced closure, and small load-history changes.
Design rules sometimes avoid relying on a threshold unless inspection and loading assumptions are especially well justified.

## Rapid Growth and Critical Crack Size
At high delta K, growth accelerates as the maximum K approaches fracture toughness.
The final instability is usually governed by Kmax compared with KIC or another appropriate toughness measure.
Plane strain toughness is most applicable to thick sections with high constraint, while thin sections may show greater apparent toughness.
The critical crack size can be estimated from geometry, maximum stress, and fracture toughness.
Safety margins are introduced because real cracks are three-dimensional, loads are uncertain, and toughness has statistical scatter.
This rapid-growth region is why inspection intervals must leave enough time between detectable crack size and critical crack size.

## Load Sequence Effects
Real structures rarely see constant-amplitude loading.
Overloads can temporarily retard crack growth by creating plastic wake effects and crack closure behind the tip.
Underloads can reduce retardation or accelerate subsequent growth in some sequences.
Variable-amplitude spectra require cycle counting methods, crack closure models, or direct spectrum testing.
Miner's rule is useful for simple cumulative fatigue damage, but crack growth analysis tracks crack length explicitly.
Spectrum truncation can be dangerous if rare high loads dominate crack extension or residual plasticity.
Operational monitoring helps convert uncertain service histories into better growth predictions.

## Environment and Material Dependence
Corrosive environments can accelerate fatigue crack growth by chemical attack at the crack tip.
Hydrogen embrittlement, stress corrosion, saltwater exposure, and high temperature oxidation can change both threshold and Paris behavior.
Aluminum alloys, steels, titanium alloys, nickel superalloys, ceramics, polymers, and composites each show distinct mechanisms.
In fiber composites, delamination and matrix cracking may replace the simple single-crack picture used for metals.
Welded structures combine residual tensile stress, geometric notches, microstructural gradients, and possible defects.
Shot peening, cold expansion of holes, and surface treatments can slow growth by introducing compressive residual stress.
Any beneficial treatment must be checked against relaxation, machining damage, corrosion, and thermal exposure.

## Measurement and Inspection
Laboratory crack growth tests often use compact tension or middle-crack tension specimens.
Crack length can be measured optically, by compliance, by potential drop, or by direct fractography after testing.
Field inspection uses dye penetrant, magnetic particle, ultrasonic, eddy current, radiography, acoustic emission, or structural health monitoring.
The detectability of a flaw is expressed through probability of detection curves rather than a single perfect threshold.
Inspection intervals should account for missed detections, measurement uncertainty, and growth scatter.
Fracture surfaces often show beach marks from variable loading and microscopic striations from individual or grouped cycles.
Fractography can reconstruct whether failure was dominated by fatigue, overload, corrosion, or manufacturing defects.

## Engineering Uses
Damage tolerant design assumes flaws exist and asks whether they remain safe until the next inspection.
Safe-life design retires a component before fatigue damage is expected, often without relying on crack detection.
Fail-safe design provides redundant load paths so one cracked element does not immediately collapse the system.
Modern aerospace practice combines all three philosophies depending on part criticality and inspectability.
Civil infrastructure uses similar reasoning for steel bridges, crane structures, pressure piping, and offshore platforms.
Rotating machinery uses crack growth analysis to set vibration monitoring alarms and shutdown criteria.
The method is strongest when geometry, stress spectrum, material data, and inspection capability are all credible.

## Modeling Pitfalls
Using nominal stress instead of local stress can underpredict growth near notches and welds.
Assuming a through crack when the real defect is a semi-elliptical surface crack can misstate both K and growth shape.
Ignoring residual stress can be nonconservative when tensile residual stress opens the crack during most of the cycle.
Using handbook constants without matching environment and stress ratio can create false precision.
Very small cracks, mixed-mode loading, plasticity, fretting, and contact can violate simple Paris-law assumptions.
Finite element models help compute geometry factors, but they do not remove the need for material crack growth data.
A useful analysis states its initial flaw assumption, detectability basis, load spectrum, crack shape model, and failure criterion.

## Practical Interpretation
The key engineering output is usually an inspection interval, a retirement limit, or a redesign of the stress concentration.
Crack growth calculations should be treated as decision support rather than as exact predictions of a single failure date.
Scatter in material constants and service loads makes probabilistic safety margins more honest than single deterministic numbers.
When failure consequences are high, conservative assumptions are paired with inspection evidence and fracture-surface investigation.

## Related Concepts
Fatigue crack growth complements S-N curves by focusing on crack size rather than only cycles to failure.
It is linked to [[fracture-mechanics-engineering-materials]], creep deformation high temperature materials, [[phase-diagrams-and-phase-transformations]], and [[finite-element-method]].
It also informs nondestructive evaluation, maintenance scheduling, reliability assessment, and forensic failure analysis.
Understanding the topic explains why apparently small surface defects can control the lifetime of large machines.

## References
- Wikipedia contributors, "Fatigue (material)," accessed 2026-05-02.
- Wikipedia contributors, "Paris law," accessed 2026-05-02.
- Wikipedia contributors, "Fracture mechanics," accessed 2026-05-02.
