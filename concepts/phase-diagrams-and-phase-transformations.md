---
title: Phase Diagrams and Phase Transformations
type: concept
aliases: [phase diagram, phase equilibria, Gibbs phase rule, eutectic, peritectic, TTT diagram, CCT diagram, precipitation hardening, CALPHAD]
tags: [physics, materials-science, thermodynamics, metallurgy, phase-transformations, alloy-design, engineering]
created: 2026-05-02
type: concept
---

A **phase diagram** is a graphical map showing the equilibrium states of a material system as a function of thermodynamic variables (temperature, pressure, composition). Each region represents a stable phase or phase combination. For binary systems at constant pressure, the horizontal axis is composition (weight or atomic percent) and the vertical axis is temperature. A **tie line** drawn through a two-phase region gives the compositions of coexisting phases. The **lever rule** yields mass fractions: for overall composition x₀ between x_α and x_β, fraction of α is (x_β − x₀)/(x_β − x_α), fraction of β is (x₀ − x_α)/(x_β − x_α).

## Types of Phase Diagrams

**Unary diagrams** plot pressure vs. temperature for a single component (e.g., H₂O, Fe, SiO₂), showing triple points and critical points. Iron exhibits α (BCC) → γ (FCC) at 912°C and γ → δ (BCC) at 1394°C at 1 atm. Water's phase diagram is notable for the negative slope of the ice I–liquid boundary, meaning ice melts under pressure — essential for glacier flow dynamics.

**Binary diagrams** (temperature–composition at fixed pressure) include:
- **Isomorphous** (complete solid solubility): Cu–Ni, Ag–Au. Single lens-shaped L + S region between liquidus and solidus. The Hume-Rothery rules predict solid solubility: atomic size difference < 15%, same crystal structure, similar electronegativity, same valence.
- **Eutectic**: Two terminal solid solutions with limited solubility meeting at the eutectic point where L → α + β on cooling.
- **Peritectic**: L + α → β invariant reaction; common in Fe–C, Cu–Zn, Cu–Sn systems.
- **Monotectic**: L₁ → L₂ + α, involving immiscible liquids (e.g., Cu–Pb at 954°C).
- **Eutectoid**: Solid-state analog of eutectic: γ → α + Fe₃C in the Fe–C system at 727°C and 0.76 wt% C (pearlite). Critical to steel microstructure control.

**Ternary diagrams** use an equilateral Gibbs triangle for three-component systems. Isothermal sections and liquidus projections are standard. Ternary eutectic points involve L → α + β + γ. The Al–Cu–Mg system (basis of 2000-series aerospace alloys) features multiple ternary invariant points.

## Thermodynamic Basis

Equilibrium phases minimize the **Gibbs free energy** G = H − TS. The **chemical potential** μᵢ = (∂G/∂nᵢ)_{T,P,n_{j≠i}} of each component must be equal across coexisting phases. The **Gibbs phase rule**, F = C − P + 2, constrains degrees of freedom: at fixed pressure (F = C − P + 1), a binary eutectic invariant (C=2, P=3) has zero degrees of freedom — fixed composition and temperature. Phase boundaries correspond to tangent-point constructions on G–x curves (common tangent method). See [[laws-of-thermodynamics]].

The **ideal solution model** gives G = ΣxᵢGᵢ° + RT Σxᵢ ln xᵢ, but real solutions require **excess Gibbs energy** G^xs, modeled by Redlich–Kister polynomials: G^xs = x₁x₂ Σ Lⱼ(x₁ − x₂)ʲ where Lⱼ are temperature-dependent interaction parameters.

## Solid-State Phase Transformations

**Allotropic transformations** change crystal structure without composition change. Iron is canonical:
- **α-ferrite** (BCC, a = 2.866 Å): stable below 912°C, max C solubility ≈ 0.022 wt% at 727°C.
- **γ-austenite** (FCC, a = 3.656 Å): stable 912–1394°C, max C solubility ≈ 2.14 wt% at 1147°C. Much larger interstitial sites (octahedral) explain the dramatic solubility difference.
- **δ-ferrite** (BCC): stable 1394–1538°C above the liquidus.

**Martensitic transformations** are diffusionless, displacive, and athermal — the lattice shears via coordinated atomic motion (Bain correspondence in steels: FCC → BCT). Carbon supersaturation produces body-centered tetragonal martensite with c/a ratio increasing with C content (~1.00 at 0% C to ~1.08 at 1.0% C). Martensite start (Mₛ) and finish (M_f) temperatures decrease with alloying: each 1 wt% C lowers Mₛ by ~320°C, 1 wt% Mn by ~33°C. Retained austenite forms when M_f is below room temperature.

**Diffusional transformations** (pearlite, precipitation) require atomic diffusion and are time-dependent. **Displacive transformations** (martensite, bainite) involve coordinated shear without long-range diffusion. Bainite forms between 250–550°C via shear with subsequent carbon diffusion, producing upper bainite (feathery, sheaves of laths with interlath carbides) and lower bainite (acicular plates with intralath carbides).

## Eutectic Systems: Pb–Sn

The Pb–Sn system is the textbook eutectic example, widely used in solders:
- **Eutectic point**: 61.9 wt% Sn, 183°C — the lowest melting point in the system.
- Terminal solid solutions: Pb-rich α (max ~19.2 wt% Sn at 183°C), Sn-rich β (max ~2.5 wt% Pb at 183°C).
- Hypoeutectic alloys (< 61.9% Sn) form proeutectic α dendrites + fine eutectic (α + β) matrix.
- Hypereutectic alloys form proeutectic β + eutectic matrix.
- Eutectic morphology depends on volume fraction: **lamellar** (near-equal fractions, regular alternating plates with interlamellar spacing λ ∝ 1/ΔT), **rod** (minor phase as rods in major matrix, favored when minor fraction < ~30%), **divorced eutectic** (phases nucleate separately, common when one phase already exists as proeutectic).

The Jackson-Hunt model (1966) describes lamellar eutectic growth, predicting λ²V = constant (V is growth velocity), experimentally verified for many systems.

## Peritectic Systems: Fe–C

Near the Fe-rich end of the Fe–C diagram:
- **Peritectic reaction** at 1495°C, ~0.16 wt% C: L + δ-ferrite → γ-austenite.
- Compositions: liquid (~0.53 wt% C), δ-ferrite (~0.09 wt% C), austenite (~0.17 wt% C).
- Solidification challenges: new austenite must grow between existing δ-solid and liquid, causing **peritectic segregation** and shrinkage porosity. In continuous casting of steel, this reaction is associated with hot tearing and cracking susceptibility, especially in Nb-bearing and Al-bearing grades where peritectic solidification ranges are wide.

## TTT and CCT Diagrams

**Isothermal Transformation (TTT) diagrams** plot time (log scale) vs. temperature for steel held at constant temperature after austenitizing:
- **Pearlite nose**: shortest incubation (~550°C for eutectoid 1080 steel), representing the balance of nucleation rate (increases with undercooling) and diffusion rate (decreases with temperature). Pearlite forms as alternating ferrite and cementite lamellae with colony growth rate V ∝ ΔT².
- **Bainite region**: 250–550°C. Upper bainite (feathery sheaves of ferrite laths with interlath cementite) forms at higher temperatures; lower bainite (acicular plates with intraplate carbides at ~60° to plate axis) at lower temperatures. Lower bainite has superior toughness.
- **Martensite**: horizontal lines at Mₛ (~220°C for 1080) and M_f. Transformation is athermal — fraction depends only on temperature, not time.

**Continuous Cooling Transformation (CCT) diagrams** are more practically relevant: transformation occurs over a temperature range. CCT curves shift right and down vs. TTT (less time for diffusion at each temperature). Critical cooling rates determine final microstructure: slow (< ~1°C/s) → pearlite; moderate → bainite; rapid (> ~140°C/s for plain carbon eutectoid) → martensite. **Jominy end-quench tests** empirically determine hardenability: a bar quenched from one end develops a hardness gradient reflecting CCT behavior at each cooling rate.

## Precipitation Hardening: Al–Cu

In the Al–Cu system (e.g., Al–4 wt% Cu, Duralumin, the first age-hardening alloy discovered by Wilm in 1906):
1. **Solution treatment**: heat to 500–540°C (single-phase α), hold to homogenize, quench to room temperature to retain supersaturated solid solution (SSSS).
2. **Aging sequence** on subsequent heating (natural aging at RT or artificial at 130–190°C):
   - **GP zones** (Guinier–Preston): Cu-rich coherent clusters on {100} planes; 1–10 nm diameter, fully coherent with matrix, no resolvable strain field contrast in TEM.
   - **θ″ (GP II)**: ordered, tetragonal (a = 4.04 Å, c ≈ 7.68 Å), coherent disc-shaped precipitates on {100}; maximum coherency strains → **peak hardness**.
   - **θ′**: semi-coherent, tetragonal (a = 4.04 Å, c ≈ 5.8 Å); plates on {100} with interfacial dislocations; still strengthens but less than θ″.
   - **θ (CuAl₂)**: equilibrium incoherent phase (C16/tetragonal structure, a = 6.07 Å, c = 4.87 Å); **overaging** — coarsening via Ostwald ripening reduces strength and increases ductility.
3. Maximum hardness at θ″ stage; coarsening follows Lifshitz–Slyozov–Wagner kinetics (⟨r⟩³ ∝ t). Overaging is irreversible — re-solution treatment is required to restore hardness.

## Order–Disorder and Spinodal Decomposition

**Order–disorder transformations** change from a random solid solution to an ordered superlattice: Cu₃Au (FCC → L1₂, T_c = 390°C), CuZn (BCC β → B2, T_c = 465°C), Fe₃Al (BCC → DO₃). Long-range order parameter η ranges from 0 (disordered) to 1 (perfectly ordered). Above T_c, long-range order vanishes but short-range order persists up to ~1.5 T_c. Ordering can strengthen alloys (e.g., Ni₃Al γ′ in superalloys) through antiphase boundary (APB) strengthening.

**Spinodal decomposition** occurs within a miscibility gap when ∂²G/∂x² < 0: no nucleation barrier exists, and composition fluctuations amplify spontaneously, producing interconnected modulated microstructures (e.g., Cu–Ni–Fe, Al–Zn, Au–Pt). The Cahn–Hilliard theory describes the amplification factor R(β) = −M(∂²G/∂x² + 2κβ² + 2Eε²Y), where β is wavenumber, κ is gradient energy coefficient, and Eε²Y is elastic strain energy penalty. A characteristic wavelength λ* maximizes R, producing periodic microstructures visible in TEM. This contrasts with classical nucleation and growth, which requires overcoming a barrier (∂²G/∂x² > 0 outside the spinodal).

## Computational Approaches

**CALPHAD** (Calculation of Phase Diagrams) builds thermodynamic databases by fitting Gibbs energy functions (Redlich–Kister polynomial expansions for excess Gibbs energy of solution phases, sublattice models for ordered phases such as the Compound Energy Formalism) to experimental phase diagram data, thermochemical measurements, and first-principles (DFT) calculations. Software: Thermo-Calc, FactSage, PANDAT, PyCalphad (open-source). Enables multicomponent equilibrium calculations (e.g., Ni-base superalloys with 8–10 elements, high-entropy alloys with 5+ principal elements). Scheil solidification simulations using CALPHAD predict microsegregation and nonequilibrium phase fractions.

**Phase field modeling** simulates microstructure evolution by solving coupled PDEs for order parameters describing phase and composition fields. Naturally handles interface curvature, anisotropy, and concurrent transformations (e.g., simultaneous precipitation and grain growth). Popular codes: MOOSE ( Idaho National Lab), MICRESS, OpenPhase. Computational cost has decreased dramatically with GPU acceleration, enabling 3D simulations of polycrystalline microstructures.

## Applications

- **Steel heat treatment**: Austenitizing, quenching, and tempering guided by TTT/CCT and Fe–C diagrams. Alloying (Cr, Mo, Ni, Mn) shifts CCT curves right, increasing hardenability — enabling martensite formation in larger sections.
- **Alloy design**: CALPHAD-aided design of Ni-base superalloys (γ/γ′ two-phase microstructure, 700–1100°C service), high-entropy alloys, lightweight Al/Ti alloys for aerospace.
- **Semiconductor processing**: Phase diagrams of Si–Ge, Ga–As, and ternary III–V systems guide crystal growth (Czochralski, Bridgman) and thin-film deposition conditions.
- **Geological systems**: Silicate phase diagrams (Mg₂SiO₄–SiO₂ forsterite–silica, CaO–Al₂O₃–SiO₂) underpin petrology and metamorphic facies interpretation.

## Martensite Tempering and Steel Microstructures

After quenching to martensite, steel is invariably **tempered** (reheated to 150–700°C) to relieve residual stresses and improve toughness at the cost of some hardness. The tempering sequence in medium-carbon steel involves:
- **Stage 1** (100–200°C): Precipitation of ε-carbide (Fe₂.₄C, hexagonal) from supersaturated martensite. Retained austenite decomposes below ~200°C.
- **Stage 2** (200–350°C): Retained austenite transforms to ferrite + cementite (if not fully decomposed in stage 1).
- **Stage 3** (250–700°C): ε-carbide dissolves, replaced by equilibrium cementite (Fe₃C, orthorhombic). Martensite loses tetragonality as C diffuses out, forming tempered martensite (ferrite + fine carbides).
- **Stage 4** (> 350°C for alloy steels): Alloy carbide precipitation (e.g., Mo₂C, V₄C₃, Cr₂₃C₆) replacing cementite, providing **secondary hardening** peaks critical in tool steels and creep-resistant alloys.

**Bainite** offers an alternative to quenched-and-tempered martensite in some applications: lower bainite achieves comparable hardness with superior toughness due to its finer carbide distribution. Austempering (isothermal hold in the bainite region) produces bainitic microstructures directly, avoiding the distortion and cracking risks of quenching.

## Iron-Carbon Phase Diagram Specifics

The Fe–C (technically Fe–Fe₃C) diagram is the most industrially important phase diagram:
- **Eutectoid point**: 727°C, 0.76 wt% C → α-ferrite + Fe₃C (cementite, orthorhombic, a = 4.524 Å, b = 5.089 Å, c = 6.741 Å). This mixture is **pearlite**, with interlamellar spacing λ inversely proportional to undercooling (λ ∝ 1/ΔT).
- **Eutectic point**: 1147°C, 4.30 wt% C → γ-austenite + Fe₃C. This mixture is **ledeburite**, relevant to cast iron microstructure.
- Hypoeutectoid steels (< 0.76% C) form proeutectoid ferrite along prior austenite grain boundaries before the eutectoid reaction.
- Hypereutectoid steels (> 0.76% C) form proeutectoid cementite networks, which are typically harmful to toughness and must be spheroidized by heat treatment.

## Key References

Porter, D.A., Easterling, K.E. & Sherif, M. (2009). *Phase Transformations in Metals and Alloys*, 3rd ed. CRC Press.
Massalski, T.B. (Ed.) (1990). *Binary Alloy Phase Diagrams*, 2nd ed. ASM International.
ASM Handbook Vol. 3: *Alloy Phase Diagrams* (1992). ASM International.
Hillert, M. (2007). *Phase Equilibria, Phase Diagrams and Phase Transformations*, 2nd ed. Cambridge.
Saunders, N. & Miodownik, A.P. (1998). *CALPHAD: Calculation of Phase Diagrams*. Pergamon.
Cahn, J.W. & Hilliard, J.E. (1958). "Free Energy of a Nonuniform System. I. Interfacial Free Energy." *J. Chem. Phys.* 28, 258.
Aaronson, H.I. (1999). *Lectures on the Theory of Phase Transformations*, 2nd ed. TMS.

## See Also

- [[laws-of-thermodynamics]]
- [[heat-transfer-mechanisms]]
- [[stress-strain-and-elasticity]]
- [[dislocation-theory-crystal-plasticity]]
- [[fracture-mechanics-engineering-materials]]
- [[superconductivity]]
