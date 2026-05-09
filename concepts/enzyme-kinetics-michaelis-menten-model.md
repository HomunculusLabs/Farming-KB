---
title: Enzyme Kinetics and the Michaelis-Menten Model
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
per second, ranging from ~0.5 s^-1 (slow regulatory enzymes) to ~10^6 s^-1
(carbonic anhydrase). Catalase achieves kcat ~ 4 x 10^7 s^-1, among the highest
of all enzymes.

The specificity constant kcat/Km is the second-order rate constant at low [S]
(M^-1 s^-1). The diffusion limit is ~10^8 to 10^9 M^-1 s^-1, set by three-
dimensional diffusion. Enzymes at this ceiling are catalytically perfect:
acetylcholinesterase (~1.6 x 10^8), triosephosphate isomerase (~4 x 10^8), and
superoxide dismutase (~2 x 10^9, enhanced by electrostatic steering of charged
substrate toward positively charged active site residues).

## Mechanisms of Enzyme Catalysis

**Transition state theory:** Enzymes stabilize the transition state, lowering
activation energy. Rate enhancement = e^(delta-deltaG/RT): a 10 kcal/mol
reduction at 298 K yields ~10^7-fold enhancement. Enzymes bind the transition
state ~10^10 to 10^15 times more tightly than substrate. This underlies
transition state analog inhibitors: statins mimic HMG-CoA reductase;
mycophenolic acid mimics IMP dehydrogenase.

**Additional strategies:** proximity and orientation (effective molarities of
10^4 to 10^8 M in the active site), acid-base catalysis (His57 in serine
proteases activates Ser195), covalent catalysis (acyl-enzyme intermediates in
chymotrypsi [[singh-metal-ion-resistance-fungi]] ion catalysis (Zn2+ in carbonic anhydrase, Mg2+ in
kinases), electrostatic preorganization (Warshel's theory), and active site
desolvation.

## Allosteric Enzymes and Cooperative Binding

Allosteric enzymes bind effectors at sites distinct from the active site,
modulating activity through conformational changes. Cooperative binding produces
sigmoidal kinetics enabling switch-like responses at metabolic control points
such as phosphofructokinase in glycolysis.

The Hill equation: v/Vmax = [S]^n / (K0.5^n + [S]^n), where n is the Hill
coefficient: n = 1 (non-cooperative, Michaelis-Menten), n > 1 (positive
cooperativity), n < 1 (negative). Hemoglobin has n ~ 2.8 for O2. Two models: the
MWC model (1963) proposes concerted T-to-R state transitions; the KNF model
(1966) proposes sequential induced-fit changes between subunits.

## Assumptions and Limitations

Requires: single substrate or pseudo-first-order conditions; steady-state [ES];
[S] >> [E]; negligible product accumulation; no cooperativity; no enzyme
inactivation or substrate inhibition.

Fails for allosteric enzymes with sigmoidal kinetics (aspartate
transcarbamoylase, phosphofructokinase); cannot describe multi-substrate
reactions without Cleland notation extensions; cannot handle substrate
inhibition (dead-end ESS complexes). The Hill equation, MWC/KNF allosteric
models, or complex rate equations are needed for these cases.

## Historical Development

Michaelis and Menten published in Biochemische Zeitschrift (1913) using
invertase, assuming rapid equilibrium. Victor Henri outlined similar ideas in
1903. Briggs and Haldane introduced the steady-state approximation (1925),
giving the modern Km = (k-1 + k2)/k1 definition. Lineweaver and Burk introduced
the double-reciprocal plot (1934). The field expanded with the MWC allosteric
model (1963), KNF sequential model (1966), and transient kinetics techniques in
the 1970s-1980s.
## See Also

- [[fungal-extracellular-enzyme-production]]
- [[ligninolytic-enzyme-systems-white-rot-fungi]]
