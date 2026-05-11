---
title: Laws of Thermodynamics
created: 2026-04-28
tags: [physics, thermodynamics, entropy, energy, engineering, chemistry]
date: 2026-05-02
updated: 2026-05-02
sources: []
type: concept
---

## Overview

Thermodynamics is the branch of physics governing energy transformations,
heat, work, and the behavior of macroscopic systems. It rests on four
fundamental laws (numbered 0 through 3) that together define the limits
of energy conversion, establish the arrow of time, and underpin virtually
every engine, refrigerator, chemical reaction, and biological process.
The field emerged from 19th-century studies of [[query-why-cant-heat-engines-be-100-percent-efficient]], with key
contributions by [[sadi-carnot]] (1824), James Joule (1843), Rudolf Clausius
(1865), Lord Kelvin, Walther Nernst (1906), and J. Willard Gibbs.

## Zeroth Law and Temperature

The zeroth law states that if system A is in thermal equilibrium with
system B, and B with C, then A is in thermal equilibrium with C. This
transitive property establishes temperature as a well-defined physical
quantity. Formulated by Ralph Fowler around 1935, it was placed first
logically because temperature is foundational to all other laws. Thermal
equilibrium means no net heat flows between systems. Empirical scales
(Celsius, Fahrenheit) were replaced by the thermodynamic Kelvin scale,
defined by the triple point of water at exactly 273.16 K.

## First Law: Conservation of Energy

Energy cannot be created or destroyed, only transformed. For any
process: dU = dQ - dW, where dU is change in internal energy, dQ is
heat added to the system, and dW is work done by the system (IUPAC
convention). Internal energy U is a state function depending only on the
current equilibrium state, not the path taken. Enthalpy H = U + PV
simplifies constant-pressure calculations since dH = dQ_p. Joule's 1843
experiment established the mechanical equivalent of heat: 1 cal = 4.184 J.
Systems are classified as closed (energy exchange only), open (energy
and matter exchange), or isolated (no exchange).

## Second Law: Entropy and Irreversibility

The Clausius statement holds that heat cannot spontaneously flow from a
colder body to a hotter body without external work. The Kelvin-Planck
statement adds that no cyclic process can convert heat from a single
reservoir entirely into work. Entropy S is defined for reversible
processes as dS = dQ_rev / T. For any spontaneous process in an
isolated system, the total entropy increases: dS_universe >= 0. Boltzmann
provided the statistical interpretation: S = k_B ln(Omega), where k_B =
1.381 x 10^-23 J/K and Omega counts the number of microstates. The Carnot
cycle sets the maximum efficiency for any heat engine operating between
temperatures T_H and T_C: eta_Carnot = 1 - T_C/T_H. Real engines fall
below this limit: coal plants reach 33-40%, combined-cycle gas ~60%,
automotive engines ~20-35%.

## Third Law and Absolute Zero

Nernst's heat theorem (1906) states that as temperature approaches
absolute zero (0 K = -273.15 C), the entropy of a perfect crystal
approaches a minimum constant, taken as zero. Absolute zero has never
been achieved; the lowest recorded temperature is approximately 38
picokelvin (Fraunhofer Institute, 2021). The unattainability principle
states that zero kelvin cannot be reached in a finite number of
operations. Some substances like carbon monoxide exhibit residual
entropy (S_0 ~ 4.6 J/(mol K)) at 0 K due to frozen-in disorder among
degenerate ground-state configurations.

## Thermodynamic Potentials

Four potentials govern equilibrium under different constraints. Internal
energy U has natural variables S and V with dU = T dS - P dV. Enthalpy
H = U + PV uses S, P with dH = T dS + V dP. Helmholtz free energy
A = U - TS uses T, V with dA = -S dT - P dV. Gibbs free energy G = H
- TS uses T, P with dG = -S dT + V dP. Each potential is minimized at
equilibrium under its natural variable constraints. Gibbs free energy is
central to chemistry and biology: at constant T and P, a process is
spontaneous when dG < 0 and at equilibrium when dG = 0.

## Maxwell Relations

Derived from equality of mixed second partial derivatives of exact
differentials, the four Maxwell relations connect unmeasurable quantities
(entropy changes) to measurable ones (pressure, volume, temperature):
(dT/dV)_S = -(dP/dS)_V, (dT/dP)_S = (dV/dS)_P,
(dS/dV)_T = (dP/dT)_V, and (dS/dP)_T = -(dV/dT)_P. These relations
are essential for deriving equations of state, material property

## See Also
- [[fukuoka-critique-laws-agricultural-science]]
