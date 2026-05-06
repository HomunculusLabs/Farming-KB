---
title: Dislocation Theory and Crystal Plasticity
type: concept
aliases: [crystal dislocations, Burgers vector, slip systems, work hardening, Hall-Petch, Frank-Read source]
tags: [physics, materials-science, engineering, crystal-plasticity, dislocations, metallurgy, deformation]
created: 2026-05-02
type: concept
---

## Overview

Dislocations are **line defects** in crystalline solids — one-dimensional imperfections where the regular periodic arrangement of atoms is disrupted along a line. They are the primary carriers of plastic deformation in crystalline materials, responsible for the dramatic difference between theoretical shear strength (~G/10 to G/30) and observed yield strength (~G/10,000 to G/100,000). Three types exist: **edge** (extra half-plane of atoms, b ⊥ ξ), **screw** (spiral atomic planes, b ∥ ξ), and **mixed** (b at angle to ξ). The strain [[turbulence-modeling-fluid-dynamics|energy]] per unit length scales as E/L ≈ (Gb²/4π)ln(R/r₀), where G is shear modulus, b is Burgers vector magnitude, R is outer cutoff (~half spacing to nearest dislocation), and r₀ is core radius (~|b|). Core [[boundary-layer-theory-fluid-dynamics|energy]] accounts for ~10–25% of total dislocation energy.
Dislocation density in annealed metals is ~10¹⁰ m⁻², rising to ~10¹⁶ m⁻² after heavy cold work.

**Orowan's equation** dγ/dt = ρ_m × b × v links macroscopic strain rate to mobile dislocation density ρ_m, Burgers vector b, and average dislocation velocity v. The concept was independently proposed by **Taylor, Polanyi, and Orowan in 1934**, building on Volterra's (1907) elastic theory of distortions. Taylor derived a parabolic work-hardening law from dislocation interactions and introduced dislocation density. Orowan established the strain rate–dislocation relationship (Orowan's equation). Polanyi noted that low observed strength requires localized defects allowing slip propagation without simultaneous shear of the entire plane. Key subsequent milestones include:
- Burgers vector (1939), - Peierls-Nabarro model (1940/47), - Frank-Read source (1950), - Hall-Petch relationship (1951/53), - Nye's dislocation density tensor (1953), and - Ashby's GND/SSD distinction (1970).

## Burgers Vector and Dislocation Reactions

The **Burgers vector b** is defined via a Burgers circuit (FS/RH convention): a closed atom-to-atom path in a perfect lattice fails to close in the real crystal, with closure failure equaling b. It is invariant along the dislocation line and conserved at nodes (Σbᵢ = 0, Frank's rule). Magnitude: |b| = a/√2 for FCC (e.g., a/2[110]), |b| = a√3/2 for BCC (e.g., a/2[111]), |b| = a for HCP basal (a/3[11-20]).

**Frank's rule** (energy criterion): a reaction b₁ + b₂ → b₃ is favorable when b₁² + b₂² > b₃², since E ∝ Gb². This governs junction formation — e.g., the Lomer-Cottrell lock in FCC: a/2[101] + a/2[011] → a/2[110], a sessile barrier on {001} that is a major work-hardening contributor. The Hirth lock (a/2[110] + a/2[-1-10] → a/2[001]) is weaker but also sessile.

**Partial dislocations** in FCC: perfect dislocations dissociate into Shockley partials separated by a stacking fault: a/2[110] → a/6[211] + a/6[12-1]. Equilibrium separation d = (Gb₁·b₂)/(2πγ_sf) depends on stacking fault energy. High SFE (Al, ~166 mJ/m²) → narrow, easy cross-slip, planar slip, high work hardening rate; low SFE (brass, ~20 mJ/m²) → wide, extended dislocations, twinning tendency, TRIP/TWIP effects. Frank partials (b = a/3[111]) are sessile since b is not in the fault plane. The **Thompson tetrahedron** catalogs all FCC Burgers vectors and slip planes: perfect (AB, AC edges), Shockley partials (αB, αC center-to-vertex), stair-rod (αβ, αγ center-to-face), and Frank partials (Aα vertex-to-face).

## Slip Systems and Schmid's Law

A **slip system** is a slip plane + slip direction pair. FCC has 12 systems ({111}<110>), BCC has 48+ ({110}, {112}, {123}<111>, no single close-packed plane — "pencil glide"), and HCP has 3–30+ depending on c/a ratio and temperature (basal, prismatic, pyramidal <a> and <c+a>). The **von Mises criterion** requires 5 independent slip systems for arbitrary homogeneous deformation, explaining FCC ductility (always sufficient), BCC temperature-dependent brittleness (thermally activated), and HCP anisotropy (often < 5 at room temperature in Mg, Zn).

**Schmid's law**: slip initiates when resolved shear stress τ = σ cos(φ)cos(λ) reaches critical value τ_c, where φ is the angle between tensile axis and slip plane normal, λ is the angle between tensile axis and slip direction. The Schmid factor m = cos(φ)cos(λ) has maximum 0.5 (both angles at 45°). For FCC single crystals: Stage I (easy glide, single slip, low hardening τ ~ γ^0.1), Stage II (linear hardening, multiple systems, forest interactions, dτ/dγ ~ G/200–G/400), Stage III (dynamic recovery via cross-slip, temperature-dependent decreasing rate).

**Peierls-Nabarro stress** (lattice resistance to dislocation motion): τ_PN ≈ (2G/(1-ν))exp(−2πw/b), where w = b/(2π(1-ν)) is dislocation half-width. FCC: ~10⁻⁴G (very low, glide easy); BCC: ~10⁻²G (high, non-planar core spread over several {110} planes); covalent crystals (Si, diamond): ~10⁻²G. BCC yield stress is strongly temperature and strain-rate dependent due to thermally activated kink-pair nucleation overcoming the Peierls barrier at T > 0.3T_m.

## Dislocation Interactions and Forest Hardening

**Junction formation**: intersecting dislocations on different slip planes react to form sessile locks (Lomer-Cottrell, Hirth) that impede glide. These junctions are a primary source of work hardening in FCC metals.

**Dipoles**: opposite-sign dislocations on adjacent planes are trapped by elastic attraction but cannot annihilate (different planes). Stress to separate scales as ~Gb/h (h = spacing). Dipole formation is a major storage mechanism during deformation; at high temperatures they climb and annihilate, contributing to dynamic recovery.

**Pile-ups**: dislocations blocked by barriers (grain boundaries, precipitates, locks) create stress concentrations. The Eshelby-Stroh model gives n ≈ πτL/(Gb) dislocations in a pile-up of length L, with tip stress τ_tip ≈ nτ reaching G/10 or more. This can activate sources in adjacent grains, nucleate cracks (Zener-Stroh mechanism), or cause grain boundary sliding.

**Forest hardening**: flow stress increment Δτ = αGb√ρ_f, where ρ_f is forest dislocation density and α ≈ 0.2–0.5. Gliding dislocations bow between forest obstacles with Friedel sampling spacing l_f ≈ ρ_f^(−1/2). This dominates Stage II hardening in FCC metals at low temperatures.

## Strengthening Mechanisms

### Solid Solution Strengthening

Solute atoms interact with dislocations through size misfit (δ = Δa/a) and modulus misfit (η = ΔG/G). **Fleischer model** (1963): Δτ ∝ c^(1/2)ε^(3/2) for point-like strong obstacles (ε = |δ| + η). **Labusch model** (1970): Δτ ∝ c^(2/3)ε^(4/3) for diffuse overlapping fields, better fitting most substitutional alloys. Interstitial solutes (C in Fe) are extremely potent (~5000 MPa/at.%) due to large tetragonal distortion. Practical examples: Cu in Al (~50 MPa/at.%), Mg in Al (5000-series alloys).

### Precipitation Hardening

Small coherent precipitates are sheared by dislocations through chemical (new interface), order (APB creation), coherency (stress field), and modulus strengthening mechanisms. Large incoherent precipitates (>10 nm) are bypassed by **Orowan looping**: τ = (Gb/L)ln(2r/b), where L is inter-particle spacing. Peak aging occurs at the transition radius between cutting and looping; overaging causes coarsening (Ostwald ripening) and strength loss. Classic example: Al-Cu Duralumin — GP zones → θ'' → θ' → θ(Al₂Cu), peak hardness at θ' stage.

### Grain Boundary Strengthening (Hall-Petch)

σ_y = σ₀ + k_y d^(−1/2), where σ₀ is friction stress and d is grain diameter. Mechanism: shorter pile-ups in smaller grains (n ∝ √d) require higher stress for cross-grain deformation transmission. k_y = 0.1–1 MPa·m^(1/2). Breakdown occurs at d < 10–20 nm (inverse Hall-Petch, grain boundary sliding) and T > 0.5T_m (diffusional creep dominates). Severe plastic deformation (ECAP, HPT, ARB) achieves 100–500 nm grains yielding 1–2 GPa in Al and Cu.

### Work Hardening

**Taylor hardening**: σ = σ₀ + MαGb√ρ, where M ≈ 3.06 (Taylor factor for random FCC texture) and α ≈ 0.3–0.5. The **Kocks-Mecking model**: dρ/dγ = k₁√ρ − k₂ρ, where storage (forest trapping, dipoles) competes with dynamic recovery (cross-slip annihilation, climb). Saturation: ρ_sat = (k₁/k₂)², σ_sat = MαGb(k₁/k₂). Higher temperature or SFE increases k₂ (easier cross-slip), reducing work hardening capacity and saturation stress. The Estrin-Mecking extension adds thermally activated recovery: dρ/dε = k₁√ρ − k₂ρ − k₃(ρ − ρ₀)exp(−Q/RT).

## Dislocation Sources and Motion

**Frank-Read source** (1950): a pinned dislocation segment bows under applied stress τ = Gb/L, eventually forming a loop that expands while the pinned segment resets — the primary multiplication mechanism. Double cross-slip (Friedel source) is an alternative where a screw dislocation creates a new source on a parallel plane.

**Cross-slip**: screw dislocations moving between intersecting planes sharing b. Critical for dynamic recovery (annihilation between parallel planes), multiplication, and obstacle bypass. Thermally activated via the Friedel-Escaig mechanism: leading partial constricts, perfect dislocation cross-slips, partials re-dissociate. Rate strongly depends on SFE.

**Climb**: edge dislocations moving ⊥ to slip plane via vacancy absorption/emission at the core. Non-conservative, requiring diffusion: v_climb = (D_v/kT)(F_climb/b). Enables recovery, creep (dislocation climb over obstacles), and obstacle bypass at elevated temperatures.

**Twinning**: shear transformation reorienting crystal to mirror image across twin plane. FCC: γ = 1/√2 on {111} (rare, low SFE); BCC: γ = √2/2 on {112} (common at low T, high strain rate); HCP: on {10-12} (very common in Mg, Ti). TWIP steels (Fe-Mn-C-Al-Si, SFE ~20–40 mJ/m²) exploit deformation twinning for >1 GPa strength with >60% elongation via the Dynamic Hall-Petch effect.

## Crystal Plasticity

**Texture** (preferred grain orientation) evolves during deformation and recrystallization, quantified by orientation distribution functions (ODFs) in Euler angle space (Bunge: φ₁, Φ, φ₂). Deformation textures: FCC rolling (copper {112}<111>, brass {110}<112>, S {123}<634>); BCC (rotated cube, γ-fiber {111}<uvw>); HCP (strong basal in Mg, split basal in Ti). Recrystallization textures: cube {001}<100> in Al, Goss {110}<001> in electrical steels.

**Anisotropy**: direction-dependent yield and r-value (Lankford coefficient r = ε_width/ε_thickness). High r >> 1 resists thinning (good for deep drawing). Elastic anisotropy: FCC (Zener ratio A ≈ 1), BCC (A ≈ 2–3 for Fe), HCP (highly anisotropic).

**CPFEM**: crystal plasticity [[finite-element-method]] method incorporating orientation and slip physics: dγ^α/dt = γ̇₀|τ^α/τ_c^α|^(1/m)sign(τ^α), with hardening matrix h_αβ coupling slip systems (self = 1, latent q ≈ 1.0–1.4). **VPSC models** treat grains as ellipsoidal inclusions in a homogeneous effective medium for efficient texture simulation.

## Dislocation Density Evolution and GNDs

**Kocks-Mecking evolution**: dρ/dγ = k₁√ρ − k₂ρ. Storage dominates Stage II (d√ρ/dε ≈ const); recovery grows in Stage III; saturation as ρ → ρ_sat. Typical saturation densities: Al ~10¹⁴–10¹⁵ m⁻², Cu ~10¹⁵–10¹⁶ m⁻², heavily cold-worked ~10¹⁶ m⁻² (σ ~ 500–1000 MPa).

**Nye's dislocation density tensor** αᵢⱼ = ∂βⱼ/∂xᵢ provides continuum dislocation density. **Ashby (1970)** distinguished **statistically stored dislocations** (SSDs, random trapping, net b = 0) from **geometrically necessary dislocations** (GNDs, accommodating lattice curvature, net b ≠ 0). GNDs arise from grain boundaries, particles, bending, indentation, and strain gradients. The Nye tensor relates: ρ_GND ≈ |αᵢⱼ|/b.

**Size effects**: ρ_GND ∝ ε_p/ℓ where ℓ is a characteristic length (grain size, particle spacing, indent depth). Smaller ℓ → higher ρ_GND → smaller is stronger. Explains: Hall-Petch (ℓ = d), indentation size effect (Nix-Gao model), thin film strengthening, and micro-pillar compression experiments. GNDs measured via EBSD lattice orientation gradients, 3D-XRD, and DIC full-field strain analysis.

## Observation Techniques

**TEM** (two-beam diffraction contrast, invisibility criterion g·b = 0 for Burgers vector determination) is the primary tool. Weak-beam dark field achieves ~1–2 nm resolution for partial dislocations. In situ TEM observes real-time dislocation motion. Limitations: 2D projection, thin-foil effects. **Etch pits**: simple, large-area surveys, but surface-only, no Burgers vector info, ~1 μm resolution limit. **X-ray topography** (Berg-Barrett, synchrotron): non-destructive bulk imaging, ~1 μm resolution, used for semiconductor wafer quality. **Atom probe tomography**: 3D atomic-scale composition (~0.1–0.3 nm depth resolution) revealing Cottrell atmospheres, solute-decorated dislocations, and precipitate-dislocation interactions. **EBSD**: electron channeling contrast imaging for bulk dislocation observation (~10 nm); orientation gradients for GND density estimation. **HRXRD**: high-resolution X-ray diffraction peak broadening analysis (Williamson-Hall method) for bulk dislocation density measurement.

## Applications

**Metallurgy**: HSLA steels (Nb, V, Ti microalloy precipitation), AHSS (DP, TRIP, TWIP, martensitic, 500–2000 MPa), age-hardenable Al alloys (2xxx, 6xxx, 7xxx), Ti-6Al-4V (HCP α + BCC β slip differences), Cu alloys (work + precipitation hardening).

**Semiconductors**: dislocation-free CZ/FZ Si growth (<100 cm⁻²), epitaxial misfit dislocations at critical thickness h_c ≈ (b/ε)[ln(h_c/b) + 1] (Matthews-Blakeslee), threading dislocations degrading GaN-on-Sapphire and SiGe-on-Si device performance, gettering via controlled oxygen precipitation.

**Creep**: power-law (dislocation climb, ε̇ = A(σ/G)ⁿexp(−Q/RT), n ≈ 3–5, Q ≈ Q_self-diffusion), Nabarro-Herring (volume diffusion, ε̇ ∝ σD_v/Gd²), Coble (grain boundary diffusion, ε̇ ∝ σD_gbδ/Gd³).

**Fatigue**: cyclic loading evolves dislocation structures (initial hardening then saturation); persistent slip bands (PSBs) in FCC with low-moderate SFE nucleate cracks via surface intrusions/extrusions from irreversible dislocation motion. Paris law: da/dN = CΔK^m governs crack growth. Coffin-Manson: Δε_p/2 × N_f^β = C for low-cycle fatigue life prediction.

**Fracture**: pile-up stress concentrations cause brittle cleavage (Stroh mechanism, σ_max = (nτ)²/[Gb(1-ν)]); ductile fracture involves void nucleation at inclusions (decohesion or particle fracture), Rice-Tracey growth, and coalescence. DBTT in BCC: σ_y rises with Peierls barrier at low T while σ_f is T-independent; when σ_y > σ_f, fracture becomes brittle.

## Key [[maxwell-equations-electromagnetism|Equations]] Summary

| Equation | Expression | Application |
|---|---|---|
| Orowan equation | dγ/dt = ρ_m b v | Strain rate from dislocation motion |
| Schmid's law | τ = σ cos(φ)cos(λ) | Slip initiation criterion |
| Taylor hardening | τ = αGb√ρ | Stress vs. dislocation density |
| Hall-Petch | σ_y = σ₀ + k_y d^(−1/2) | Grain size effect |
| Frank's rule | b₁² + b₂² > b₃² | Dislocation reaction favorability |
| Kocks-Mecking | dρ/dγ = k₁√ρ − k₂ρ | Density evolution |
| Power-law creep | ε̇ = A(σ/G)ⁿ exp(−Q/RT) | High-temperature deformation |
| Nye tensor | αᵢⱼ = ∂βⱼ/∂xᵢ | Continuum dislocation density |

## Key References

Hull, D. & Bacon, D.J. (2011). *Introduction to Dislocations* (5th ed.). Butterworth-Heinemann.
Hirth, J.P. & Lothe, J. (1992). *Theory of Dislocations* (2nd ed.). Krieger.
Kocks, U.F., Tomé, C.N. & Wenk, H.-R. (1998). *Texture and Anisotropy*. Cambridge.
Argon, A.S. (2008). *Strengthening Mechanisms in Crystal Plasticity*. Oxford University Press.
