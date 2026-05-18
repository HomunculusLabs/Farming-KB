---
title: [[enzyme]] Kinetics and the Michaelis-Menten Model
created: 2026-04-28
updated: 2026-05-06
aliases: [Michaelis-Menten kinetics, enzyme kinetics, Vmax, Km, enzyme catalysis]
tags: [biochemistry, enzymology, kinetics, catalysis]
type: concept
sources: []
---

## The Michaelis-Menten Equation

The Michaelis-Menten equation describes the rate of an enzyme-catalyzed reaction
as a function of substrate concentration:

v = (Vmax x [S]) / (Km + [S])

where v is the initial reaction velocity, [S] is substrate concentration, Vmax
is the maximum velocity, and Km is the Michaelis constant. The model assumes a
single-substrate reaction forming an enzyme-substrate complex (ES) that breaks
down to product: E + S <-> ES -> E + P, with forward binding rate k1,
dissociation rate k-1, and catalytic rate k2 (kcat).

Under the steady-state approximation (Briggs and Haldane, 1925), d[ES]/dt = 0,
yielding [ES] = ([E]0 x [S]) / (Km + [S]) where Km = (k-1 + k2) / k1.
Substituting v = k2[ES] and Vmax = k2[E]0 gives the Michaelis-Menten equation.
The original 1913 derivation by Michaelis and Menten used the rapid equilibrium
assumption (k-1 >> k2), making Km = Ks = k-1/k1. The steady-state form is
preferred as it applies even when catalysis is comparable to dissociation.

## Vmax and Km: Meaning and Determination

Vmax is the maximum rate when all active sites are saturated: Vmax = kcat x
[E]total (units: concentration/time). It scales linearly with enzyme
concentration — doubling the enzyme doubles Vmax. Km is the substrate
concentration at half Vmax, reflecting apparent affinity: lower Km means higher
affinity (exact under rapid equilibrium). Typical Km values span 10^-8 to 10^-2
M.

Hexokinase has Km ~ 0.05 mM for glucose; glucokinase (hexokinase IV) has Km ~
5-10 mM as a liver glucose sensor; chymotrypsin has Km ~ 1-5 mM; carbonic
anhydrase has Km ~ 8 mM for CO2.

## Linear Transformations and Modern Fitting

Three classical linear plots convert the hyperbolic equation into straight-line
forms:

- **Lineweaver-Burk (double-reciprocal):**:1/v = (Km/Vmax)(1/[S]) + 1/Vmax. Slope = Km/Vmax; y-intercept = 1/Vmax;
    x-intercept = -1/Km. Useful for identifying inhibition type visually,
    but severely overweights low-[S] data points.

- **Eadie-Hofstee:**:v = -Km x (v/[S]) + Vmax. Slope = -Km; y-intercept = Vmax. Less error
    distortion, but both axes contain v.

- **Hanes-Woolf:**:[S]/v = (1/Vmax)[S] + Km/Vmax. Most statistically robust linearization.
    Modern practice prefers direct nonlinear regression (Levenberg-
    Marquardt).

## [[enzyme-inhibition]] Types

Four classical patterns are distinguished by effects on Vmax and Km:

**Competitive:** Inhibitor binds free enzyme at active site. Km,app = Km x (1 +
[I]/Ki); Vmax unchanged. High [S] overcomes inhibition. Lines converge at
y-intercept on Lineweaver-Burk. Examples: methotrexate vs. DHFR; sildenafil vs.
PDE5; sulfonamides vs. dihydropteroate synthase.

**Non-competitive:** Inhibitor binds E and ES with equal affinity. Vmax,app =
Vmax/(1 + [I]/Ki); Km unchanged. Cannot be overcome by [S]. Lines converge at
x-intercept. Example: alanine inhibiting pyruvate kinase.

**Uncompetitive:** Inhibitor binds only ES complex. Both Km,app and Vmax,app
decrease by 1/(1 + [I]/Ki). Parallel lines on Lineweaver-Burk. Example:
L-phenylalanine inhibiting alkaline phosphatase.

**Mixed:** Inhibitor binds E and ES with different affinities. Both Vmax and Km
change; lines intersect off both axes. Ki and Ki' from secondary plots of slope
or intercept versus [I].

## Catalytic Efficiency and the Diffusion Limit

The turnover number kcat = Vmax/[E]total is molecules converted per active site
per second, ranging from ~0.5 s^-1 (slow regulatory [[singh-white-rot-fungi-lignin-modifying-enzymes]]) to ~10^6 s^-1
(carbonic anhydrase). Catalase achieves kcat ~ 4 x 10^7 s^-1, among the highest
of all enzymes.

The specificity constant kcat/Km is the second-order rate constant at low [S]
(M^-1 s^-1). The diffusion limit is ~10^8 to 10^9 M^-1 s^-1, set by three-
dimensional diffusion. Enzymes at this ceiling are catalytically perfect:

## See Also
- [[det]]
- [[cannabis-acidobacteria-iii1-15-endorhiza-decline-two-tier-model]]
- [[coleman-unheated-greenhouse-economic-model-passive-winter-production]]
