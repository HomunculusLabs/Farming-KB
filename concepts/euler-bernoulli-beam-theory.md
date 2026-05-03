---
title: "Euler-Bernoulli Beam Theory"
aliases: [classical beam theory, engineering beam theory, Bernoulli beam theory]
tags: [mechanics, structural-engineering, elasticity, beams, engineering]
created: 2026-05-02
type: concept
sources: []
---

## Definition

Euler-Bernoulli beam theory is the classical one-dimensional model used to predict bending stresses, slopes, and deflections in slender beams.

It reduces three-dimensional [[continuum-mechanics]] to a centerline displacement problem by assuming cross sections remain plane and normal to the neutral axis during bending.

In engineering practice it remains the first model checked for floor beams, bridge members, shafts, frames, laboratory specimens, and many machine components.

## Core Assumptions

The beam is slender: its length is much larger than its cross-sectional depth and width.

Material behavior is usually taken as linear elastic, homogeneous, and isotropic unless a transformed-section or equivalent stiffness is introduced.

Deflections and rotations are small enough that geometry can be linearized around the undeformed configuration.

Plane cross sections remain plane after deformation, so axial strain varies linearly over the depth of the beam.

Normals to the neutral axis remain normal after deformation, which means transverse shear deformation is neglected.

The neutral axis passes through the centroid for symmetric homogeneous sections under pure bending.

## Governing Equation

For a prismatic beam with constant flexural rigidity, the static equation is E I d^4 w / d x^4 = q(x).

Here w is transverse deflection, E is Young's modulus, I is the second moment of area, and q is load per unit length.

Curvature is approximated by d^2 w/dx^2, which is accurate for small slopes.

Bending moment is related to curvature by M = - E I d^2 w/dx^2, with sign convention depending on the course or code.

These relations make shear-force diagrams, bending-moment diagrams, and deflection curves different integrations of the same load information.

## Stiffness and Scaling

Flexural rigidity E I is the central stiffness parameter in the theory.

Young's modulus captures material stiffness, while the second moment of area captures how far material is placed from the neutral axis.

Because I scales strongly with depth, deeper sections usually increase bending stiffness more efficiently than simply adding material near the neutral axis.

A rectangular section has I = b h^3 / 12 about its strong axis, so doubling depth increases I by a factor of eight.

Deflection scales with span to a high power: a uniformly loaded simply supported beam has maximum deflection proportional to L^4.

This L^4 dependence explains why long-span serviceability limits can govern design even when stresses are moderate.

## Boundary Conditions

A fourth-order beam equation requires four boundary conditions for a single span.

A simply supported end fixes vertical displacement but allows rotation, while an ideal pin or roller transmits no bending moment.

A clamped end fixes both displacement and rotation and can develop a reaction moment.

A free end has zero applied moment and zero applied shear unless a tip moment or tip force is present.

Correct boundary modeling is often more important than adding mathematical detail to the beam theory itself.

## Stress Interpretation

Normal bending stress follows sigma = M y / I for a homogeneous elastic section.

The stress is tensile on one side of the neutral axis and compressive on the other side.

Maximum bending stress occurs at the extreme fibers farthest from the neutral axis.

For deep beams, short spans, sandwich panels, and low-shear-modulus materials, the neglected shear contribution may be significant.

## Dynamic Form

Natural frequencies depend on boundary conditions, mass per unit length, flexural rigidity, and span.

The model is widely used for vibration estimates in machine frames, microcantilevers, musical instruments, and structural health monitoring.

At high frequency or for thick beams, rotary inertia and shear deformation make Timoshenko beam theory more accurate.

## Design Uses

Classical beam tables give reactions, moments, slopes, and deflections for common spans and loading cases.

Engineers superpose load cases when linear assumptions hold, combining uniform loads, point loads, thermal curvature, and support settlements.

The method provides quick checks before more detailed [[finite-element-method]] models are built.

It is especially useful for sanity checking finite-element results because the simple model exposes expected orders of magnitude.

## Limitations

The slender-beam assumption weakens as span-to-depth ratio decreases.

Shear deformation can increase deflections in deep beams even when bending stress formulas look reasonable.

Large deflections require geometric nonlinearity because curvature is no longer well approximated by the second derivative of deflection.

Material nonlinearity, cracking, yielding, creep, and composite action can change the effective stiffness.

These limitations do not make the theory obsolete; they define the envelope in which its elegance is useful.

## Relationship to Other Models

Timoshenko beam theory extends the model by allowing cross sections to rotate independently from the deflected centerline slope.

Full elasticity solves stress and displacement fields in three dimensions but is usually less convenient for routine design.

[[fracture-mechanics-engineering-materials]] may be needed when cracks control failure rather than nominal bending stress.

[[finite-element-method]] beam elements often implement Euler-Bernoulli or Timoshenko kinematics depending on the element formulation.

## Common Pitfalls

Using the wrong end condition can produce deflection errors larger than the difference between beam theories.

Mixing sign conventions for shear, moment, and curvature can lead to correct magnitudes attached to wrong diagrams.

Treating a short thick member as a slender beam can underestimate deflection and misrepresent support reactions.

## See Also

- [[continuum-mechanics]]
- [[finite-element-method]]
- [[fracture-mechanics-engineering-materials]]
- [[creep-deformation-high-temperature-materials]]
- [[boundary-layer-theory-fluid-dynamics]]
