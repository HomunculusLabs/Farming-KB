---
title: "Lagrangian Mechanics"
aliases: [analytical mechanics, Lagrange equations, variational mechanics]
tags: [physics, mechanics, dynamics, engineering, mathematics]
created: 2026-05-02
updated: 2026-05-06
type: concept
sources:
  - "raw/papers/[[greg-green-odor-control-and-air-filtration]].md"
---

## Overview

Lagrangian mechanics is a formulation of classical dynamics that describes motion by comparing kinetic and potential energy rather than by summing forces component by component. Its central object is the Lagrangian, usually written as L = T - V for conservative mechanical systems.

The method is equivalent to Newtonian mechanics for ordinary particles, but it changes the bookkeeping. Instead of resolving every constraint force, it uses generalized coordinates that describe the independent ways a system can move.

This coordinate freedom makes Lagrangian mechanics especially useful for pendulums, linkages, robots, vibrating structures, spacecraft attitude models, electrical analog networks, and continuum field theories.

The formulation is one of the main bridges between [[finite-element-method]], [[quantum-mechanics-fundamentals]], and modern field theory.

A Lagrangian model is not merely a change of notation. It exposes symmetry, conservation laws, constraints, and [[savory-energy-flow-and-solar-capture]] in a way that is often hidden in direct force balance.

## Generalized Coordinates

Generalized coordinates are variables chosen to describe the configuration of a system. They may be distances, angles, modal amplitudes, link rotations, charge coordinates, or any other independent descriptors.

A double pendulum can be described by two angles rather than by four Cartesian coordinates plus two rod-length constraints. A bead on a wire can be described by its distance along the wire rather than by three coordinates and two constraint equations.

The number of generalized coordinates equals the number of degrees of freedom after holonomic constraints have been applied. This reduction is one reason the method is popular in multibody dynamics.

The generalized velocities are the time derivatives of the coordinates. The Lagrangian is written as a function of coordinates, velocities, and sometimes time: L(q, qdot, t).

Choosing coordinates is an engineering judgment. Good coordinates make symmetries visible, reduce algebra, and avoid singularities over the operating range of the model.

Poor coordinates can make a simple system look complicated, introduce numerical stiffness, or hide conserved quantities that would otherwise simplify analysis.

## Action and Stationary Paths

The action is the time integral of the Lagrangian over a candidate path. Hamilton's principle states that the actual path followed by the system makes the action stationary with respect to small variations that keep the endpoints fixed.

Stationary does not always mean minimum. In many systems the true path is a saddle point of the action functional, but the first-order variation still vanishes.

This variational statement is powerful because it treats an entire trajectory at once rather than building motion from instantaneous force balance alone.

For conservative finite-dimensional systems, applying calculus of variations to the action produces the Euler-Lagrange equations. These are the differential equations that replace Newton's second law in generalized coordinates.

The action viewpoint also generalizes naturally to fields. In electromagnetism, elasticity, fluids, and quantum field theory, the dynamical variables are functions over space and time rather than a finite list of coordinates.

## Euler-Lagrange Equations

For each generalized coordinate q_i, the equation of motion has the form d/dt of the partial derivative of L with respect to qdot_i, minus the partial derivative of L with respect to q_i, equals any generalized nonconservative force.

When only conservative forces are present, the right side is zero. The resulting equations automatically include many constraint effects because the coordinates already respect the constraints.

The partial derivative with respect to velocity defines generalized momentum. For a Cartesian free particle this reduces to ordinary linear momentum, but for angles it becomes angular momentum or a related conjugate quantity.

The Euler-Lagrange equation is particularly useful when forces are awkward but energies are easy. Springs, gravity, rotating reference terms, and coupled inertias often enter more cleanly through energy expressions.

In small vibration problems, expanding the Lagrangian to quadratic order yields mass and stiffness matrices. This connects analytical mechanics directly to modal analysis and structural dynamics.

In finite element models, weak forms and variational principles echo the same idea: approximate fields are chosen so that an energy or residual statement is stationary over allowable variations.

## Constraints and Multipliers

Holonomic constraints can be built into the coordinate choice. If a point is constrained to move on a circle, an angle coordinate can eliminate the constraint force entirely.

When constraints are easier to state than to eliminate, Lagrange multipliers introduce additional unknowns. The multipliers often have direct physical meaning as constraint forces or reaction loads.

Nonholonomic constraints, such as rolling without slipping, require more care because they involve velocities and may not integrate into simple coordinate restrictions.

Engineering systems often combine both types. A vehicle model may have suspension coordinates, steering constraints, rolling constraints, actuator inputs, and contact forces.

Dissipation can be added through generalized forces or Rayleigh dissipation functions. Pure Lagrangian mechanics is most elegant for conservative systems, but practical models routinely include damping, friction, and control inputs.

The method is therefore not limited to ideal classroom mechanisms. It is a modeling framework that can be extended while retaining a clear separation between inertia, stored energy, dissipation, and actuation.

## Symmetry and Conservation

A coordinate is cyclic if the Lagrangian does not depend on that coordinate directly. The conjugate momentum for a cyclic coordinate is conserved.

This is the mechanical expression of a broader principle formalized by Noether's theorem. Continuous symmetries imply conserved quantities.

If the Lagrangian is invariant under spatial translation, linear momentum is conserved. If it is invariant under rotation, angular momentum is conserved. If it has no explicit time dependence, energy is conserved for ordinary conservative systems.

These results are useful diagnostically. If a numerical simulation loses energy in an undamped conservative model, the discretization or time integrator may be suspect.

Symmetry also guides design. Balanced rotors, vibration absorbers, spacecraft attitude systems, and resonant structures all exploit or manage conserved quantities.

In field theory, symmetry-conservation links become even more central because local conservation laws shape the form of allowable equations.
