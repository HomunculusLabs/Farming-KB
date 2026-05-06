---
title: Creep Deformation High Temperature Materials
created: 2026-05-06
updated: 2026-05-06
type: concept
tags: []
sources: []
---

---
ti

Creep is the time-dependent, permanent (plastic) deformation of a material under
sustained stress at elevated temperature. Unlike instantaneous elastic or plastic
strain, creep accumulates progressively over time even at stresses well below the
yield strength. It is the dominant failure mechanism for components operating at high
temperatures: turbine blades, pressure vessels, boiler tubes, nuclear fuel cladding,
and jet engine components. Creep becomes engineering-significant when the homologous
temperature T/Tm exceeds approximately 0.3-0.4 (where Tm is the absolute melting
point in Kelvin). For steel (Tm ~ 1811 K) this threshold is about 400 degrees C; for
aluminum (Tm ~ 933 K) about 100 degrees C; for lead (Tm ~ 600 K) even room temperature.

## Three Stages of Creep

A typical creep curve (strain vs. time at constant stress and temperature) exhibits
three distinct stages. Primary creep (stage I, transient/Andrade) features a decreasing
strain rate as work hardening exceeds recovery and dislocation density increases,
often described by the Andrade equation epsilon = beta * t^(1/3). Secondary creep
(stage II, steady-state) maintains a constant minimum creep rate as dynamic equilibrium
between hardening and recovery is reached; this minimum rate determines service life.
Tertiary creep (stage III) shows accelerating strain rate leading to rupture through
necking, void nucleation and growth, grain boundary cavitation, and microstructural
degradation. The Monkman-Grant relationship links steady-state rate to rupture life:
epsilon_dot_min * t_r = C_M where C_M is approximately 0.05-0.3 for many metals.

## Creep Mechanisms

Dislocation creep (power-law creep) dominates at intermediate stresses and temperatures
(T/Tm > 0.5). Dislocations overcome obstacles by thermally activated climb via vacancy
diffusion to and from dislocation cores, with stress exponent n = 3-7. Nabarro-Herring
creep operates at very low stresses and large grain sizes through volume diffusion:
epsilon_dot_NH = (A * D_v * sigma * Omega) / (d^2 * kT), where D_v is the lattice
self-diffusion coefficient, d is grain size, and Omega is atomic volume. Stress
exponent n = 1; grain size exponent p = 2. Coble creep dominates at lower temperatures
in fine-grained materials (d < 10 micrometers) through grain boundary diffusion:
epsilon_dot_Coble = (A' * D_GB * delta * sigma * Omega) / (d^3 * kT), with n = 1 and
p = 3, where delta is grain boundary width (~1 nm). Harper-Dorn creep is a low-stress
mechanism (n = 1) in coarse-grained materials with very low dislocation density
(~10^8 m^-2), observed in Al, Pb, Sn, and some ceramics at T/Tm > 0.6. Grain boundary
sliding accommodated by diffusion contributes to superplastic flow and cavitation.
Solute-drag creep in solid-solution alloys produces n = 3 with strong solute dependence.

## Creep Equations and Activation Energies

The Norton power law for steady-state creep is epsilon_dot = A * sigma^n * exp(-Q_c / RT),
where R = 8.314 J/(mol K) and Q_c is the activation energy. The Dorn equation normalizes
temperature dependence through diffusivity: epsilon_dot / (D * G * b * T) = f(sigma/G).
Representative activation energies: aluminum Q_lattice ~ 142 kJ/mol, Q_GB ~ 84 kJ/mol;
nickel Q_lattice ~ 284 kJ/mol; iron (alpha) Q_lattice ~ 251 kJ/mol, (gamma) ~ 270 kJ/mol;
copper Q_lattice ~ 197 kJ/mol. Deformation mechanism [[maps]] plot normalized stress
(sigma/G) versus homologous temperature to identify which mechanism dominates for a
specific material in any given operating regime.

## Creep in Specific Materials

Nickel-base superalloys (Inconel 718, CMSX-4, René 88, Mar-M247) are the gold standard
for creep resistance, operating up to 85-90% of their melting point (~1100 degrees C for
single-crystal grades). Creep resistance derives from coherent L12 gamma-prime (Ni3(Al,Ti))
precipitates providing precipitation strengthening. CMSX-4 composition: Ni-6.5Cr-9Co-
0.6Mo-6W-5.6Al-1Ti-3Re-0.1Hf (wt%) with ~70% gamma-prime volume fraction. Rhenium (3-6
wt%) partitions to the gamma matrix, slowing diffusion and improving creep life.
Ceramics (Al2O3, Si3N4, SiC) have high melting points and low creep rates but are brittle.
Polymers creep at room temperature due to low glass transition temperatures; above Tg,
viscoelastic creep follows time-temperature superposition (WLF equation). Composites
like SiC/SiC ceramic matrix composites operate to ~1300 degrees C in turbine applications.

## Larson-Miller Parameter and Life Prediction

The Larson-Miller parameter (LMP) extrapolates creep-rupture life from short-term tests:
P_LM = T(C + log t_r), where T is absolute temperature, t_r is rupture time in hours,
and C is approximately 15-25 (originally 20) depending on the alloy. For Inconel 718 at
650 degrees C (923 K) with 1000-hour rupture life, P_LM = 923 * (20 + 3) = 21,229. At
700 degrees C (973 K) with the same P_LM, t_r drops to approximately 54 hours, illustrating
the exponential sensitivity. Other parametric methods include Manson-Haferd, Orr-Sherby-Dorn,
and Wilshire equations for time-temperature extrapolation of creep data.

## Superalloys and Creep-Resistant Materials

Single-crystal turbine blades eliminate grain boundaries entirely, preventing grain
boundary sliding and cavitation. First-generation (PWA 1480): Ni-10Cr-5Co-4W-12Ta-5Al-
1.5Ti; fourth generation adds ruthenium for phase stability. Operating temperatures reach
1150 degrees C with internal cooling channels and thermal barrier coatings (YSZ,
yttria-stabilized zirconia, providing ~200 degrees C surface temperature reduction).
The L12 gamma-prime phase has cube-on-cube orientation with the FCC gamma matrix.
Dislocations must cut through precipitates (anti-phase boundary energy 0.1-0.3 J/m^2) or
bow between them (Orowan looping). The gamma/gamma-prime lattice misfit (~ -0.1% to -0.5%)
creates coherency strains. Rafting (directional coarsening under stress along <001>) can
be beneficial or detrimental. ODS alloys (oxide dispersion strengthened) with Y2O3
dispersoids (5-50 nm) in Fe-Cr-Al matrices resist creep to ~1300 degrees C.

## Testing Methods and Standards

ASTM E139 covers constant-load creep testing, the most common industrial method where
stress increases as cross-section decreases during necking. Constant-stress testing
uses lever arms or servo-control for more accurate intrinsic behavior measurement.
Stress-rupture testing (ASTM E292) carries specimens to failure for time-to-rupture and
elongation data used in Larson-Miller parameter generation. ISO 204 specifies uniaxial
tensile creep testing. Typical specimens have 25-50 mm gauge lengths with extensometry
accuracy of plus or minus 0.5 micrometers. Tests range from 100 to over 100,000 hours for
power plant component qualification.

## Engineering Applications and Failure Cases

Gas turbine blades operate at 800-1150 degrees C with 20,000-40,000 hour design lives.
Steam turbine rotors and blades serve at 540-620 degrees C for >200,000 hours. Boiler
superheater tubes at 540-650 degrees C target 100,000-200,000 hour lives. Nuclear fuel
cladding (Zr alloys) at 300-400 degrees C experiences irradiation-accelerated creep.
The ASME Boiler and Pressure Vessel Code Section III Division 1 Subsection NH governs
elevated temperature design. Notable failures include the F-111 wing pivot fitting
(1969) from creep-induced embrittlement in cold-worked D6ac steel, grounding the fleet
for two years. Creep-fatigue interaction accounts for 50-80% of failures in high-
temperature rotating machinery, as cyclic loading superimposes on sustained stress.
Design creep strain limits for power plants are typically ~1% in 100,000-200,000 hours.

## Microstructural Stability During Creep

Long-term creep exposure causes microstructural changes that degrade properties.
Precipitate coarsening follows the Ostwald ripening law: d^3 = d_0^3 + Kt, where K
is proportional to D*gamma*Vm/C_infinity, reducing precipitation strengthening over
time. In superalloys, gamma-prime rafting, carbide [[decomposition]], and sigma-phase
formation can occur during extended service. Creep exposure diagrams (analogous to TTT
diagrams) map the onset of microstructural instability as a function of service time
and temperature for specific alloys. In austenitic steels, long-term exposure can
transform M23C6 carbides to brittle M6C. These instabilities set the upper temperature
limit for practical service life and inform inspection and replacement schedules.
## Related Topics

- [[fracture-mechanics-engineering-materials]]
- [[stress-strain-and-elasticity]]
- [[bamboo-as-building-material]]
