---
title: "Crystal Structure and Crystal Defects"
type: concept
category: materials-science
related:
  - dislocation-theory-crystal-plasticity
  - phase-diagrams-and-phase-transformations
  - stress-strain-and-elasticity
  - fracture-mechanics-engineering-materials
tags: [materials-science, crystallography, defects, metallurgy, semiconductor,
  dislocations, grain-boundaries, precipitation, lattice-structure, xrd]
created: 2026-05-02
updated: 2026-05-06
type: concept
sources: []
---

Crystal structure and crystal defects are central concepts in materials
science, governing the mechanical, electrical, thermal, and optical
properties of virtually all engineering materials. A perfect crystal is
an idealized periodic arrangement of atoms, but real materials always
contain defects — point, line, planar, and volume imperfections that
profoundly influence behavior. Understanding both ideal structures and
their defects is essential for metallurgy, semiconductor manufacturing,
and advanced materials design.

## Fundamental Crystal Structures

Five crystal structures dominate engineering materials. **Simple cubic (SC)**
has coordination number 6, one atom per unit cell, and atomic packing
factor (APF) of 0.52. Only polonium crystallizes in SC; it is uncommon.

**Body-centered cubic (BCC)** has CN = 8, 2 atoms/cell, APF = 0.68.
Atoms touch along the body diagonal: √3·a = 4r. Common BCC metals:
α-iron (a = 0.2866 nm), chromium (0.2884 nm), tungsten (0.3165 nm),
molybdenum (0.3147 nm), vanadium, niobium, tantalum. BCC metals are
strong but less ductile than FCC, with lower packing density.

**Face-centered cubic (FCC)** has CN = 12, 4 atoms/cell, APF = 0.74 —
the highest packing for single-element structures. Atoms touch along
the face diagonal: √2·a = 4r. Common FCC metals: copper (0.3615 nm),
aluminum (0.4050 nm), nickel (0.3524 nm), silver (0.4086 nm), gold
(0.4079 nm), platinum (0.3924 nm), γ-iron (austenite, 0.3647 nm).
FCC metals are typically ductile with many slip systems.

**Hexagonal close-packed (HCP)** has CN = 12, 6 atoms/cell, APF = 0.74.
Ideal c/a = √(8/3) ≈ 1.633; real metals deviate (Ti: 1.587, Zn: 1.856).
Common: magnesium (0.3209 nm), titanium (0.2951 nm), zinc (0.2665 nm),
beryllium, cobalt, zirconium.

**Diamond cubic** has CN = 4, 8 atoms/cell, APF = 0.34 — two
interpenetrating FCC lattices offset by ¼[111]. Silicon (0.5431 nm),
germanium (0.5658 nm), diamond (0.3567 nm). The open covalent structure
makes these critical for semiconductor and optical applications.

## Bravais Lattices and Miller Indices

Seven crystal systems (cubic, tetragonal, orthorhombic, hexagonal,
trigonal, monoclinic, triclinic) are defined by axial lengths and
interaxial angles. Bravais (1850) showed only 14 distinct lattice types
exist: primitive (P), body-centered (I), face-centered (F), base-centered
(C), and rhombohedral (R). **Miller indices (hkl)** denote planes as
reciprocals of axis intercepts; directions are [uvw]. Key slip systems:
FCC = {111}〈110〉 (12 systems), BCC = {110}〈111〉, HCP basal =
{0001}〈11-20〉. FCC's 12 independent slip systems enable extensive ductility.

## Point Defects

**Vacancies** — missing atoms — exist at equilibrium concentration
C_v = exp(-Q_f/kT). Formation energies: Cu ~1.0 eV, Al ~0.75 eV,
Fe ~1.7 eV. At melting point, C_v ≈ 10⁻³-10⁻⁴; at room T, ~10⁻¹².
Vacancies enable solid-state diffusion via the vacancy mechanism.

**Self-interstitials** — extra atoms in non-lattice positions — have
formation energies 3-5× higher (Cu ~4.0 eV), making them rare.
**Substitutional impurities** replace host atoms; Hume-Rothery rules
predict extensive solid solution when atomic radii differ by <15%,
crystal structures match, and electronegativities are similar. Examples:
Cu-Zn (brass), Cu-Sn (bronze), Ni in Fe (stainless steel).

**Schottky defects** are paired cation-anion vacancies in ionic crystals
(NaCl: Q_f ≈ 2.3 eV/pair), maintaining charge neutrality.
**Frenkel defects** displace an ion to an interstitial site (AgBr:
Q_f ≈ 1.1 eV), more likely in structures with large interstitial sites.

## Line Defects: Dislocations

Dislocations are line defects enabling plastic deformation at stresses
far below theoretical shear strength. **Edge dislocations** have an extra
half-plane; Burgers vector b is perpendicular to the dislocation line.
**Screw dislocations** form a spiral ramp; b is parallel to the line,
allowing cross-slip. **Mixed dislocations** combine both; most real
dislocations are mixed.

Burgers vector magnitudes: FCC |b| = a/√2 ≈ 0.255 nm (Cu), BCC |b| =
a√3/2 ≈ 0.248 nm (Fe), HCP |b| = a ≈ 0.295 nm (Ti). **Dislocation
density** ρ (m⁻²): annealed metals 10⁶-10⁸, cold-worked 10¹⁴-10¹⁶,
single-crystal semiconductors <10³. The Frank-Read source mechanism
multiplies dislocations under applied stress: τ = Gb/L where L is the
pinning distance between obstacles.

## Planar Defects

**Grain boundaries** separate crystals with different orientations.
Low-angle (θ < 15°) are dislocation arrays; high-angle (θ > 15°) are
disordered regions 2-5 atomic layers wide (~0.3-0.5 J/m²). Hall-Petch
strengthening: σ_y = σ₀ + k_y · d⁻¹ᐟ². For steels k_y ≈ 0.5-1.0
MPa·m¹ᐟ²; for Cu, ~0.07 MPa·m¹ᐟ².

**Twin boundaries** have mirror symmetry. Annealing twins are common in
FCC metals with low SFE (Cu, Ag). TWIP steels use mechanical twinning
for elongations >60% with σ > 1 GPa. **Stacking faults** are errors in
close-packed plane sequence. Stacking fault energy varies: Al ~166 mJ/m²
(high, no faults), Cu ~45, austenitic SS ~20-30, Ag ~22 mJ/m² (low,
wide faults). Low SFE promotes twinning and partial dislocation activity.

## Volume Defects and Strengthening Mechanisms

**Voids** form during solidification, irradiation, or sintering.
Reactor void swelling can reach 10% volume change. **Precipitates**
strengthen via age hardening: coherent GP zones → semi-coherent →
incoherent phases. Ni-base superalloys achieve >1.2 GPa at 1000°C via
γ' (Ni₃Al) precipitates up to 70% volume fraction. **Inclusions**
(MnS, Al₂O₃) initiate fatigue cracks; clean steel needs <10 ppm oxygen.

Four strengthening mechanisms operate simultaneously: (1) grain boundary
(Hall-Petch), (2) work hardening σ ∝ √ρ (Taylor relation), (3) solid
solution Δσ ∝ ε^{3/2}c^{1/2}, (4) precipitation hardening. Carbon in
BCC iron provides ~5500 MPa/at% — the basis of steel hardening.
Grain boundaries strengthen at room temperature but accelerate creep
(diffusion pathways) at high T, motivating single-crystal superalloy
turbine blades that eliminate boundaries entirely.

## Characterization Techniques

**X-ray diffraction (XRD)** uses Bragg's law (nλ = 2d sinθ) to identify
phases, measure lattice parameters (±0.0001 nm), and determine
crystallite size via Scherrer broadening. **Transmission electron
microscopy (TEM)** directly images dislocations, stacking faults, and
precipitates at ~0.05 nm resolution (aberration-corrected). **Scanning
electron microscopy (SEM)** with EBSD maps crystal orientations and
grain boundaries at 10-50 nm spatial resolution. These are complementary:
XRD for bulk phase ID, TEM for atomic-scale defects, SEM/EBSD for
microstructural mapping. Advanced techniques include atom probe
tomography (APT) for 3D composition at sub-nm resolution and synchrotron
XRD for in-situ studies of phase transformations under load.

## See Also

- [[palmer-mushroom-anatomy-and-structure]]
- [[mollison-wet-tropical-forest-structure-and-polyculture]]
- [[eleusinian-mysteries-history-and-structure]]
- [[plant-cell-structure-and-organelles]]
