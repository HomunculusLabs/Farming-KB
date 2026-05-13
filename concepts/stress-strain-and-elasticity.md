---
title: "Stress, Strain, and Elasticity"
type: concept
category: materials-science
related:
  - [[fracture-mechanics-engineering-materials]]
tags: [mechanics, materials-science, elasticity, stress, strain, hooke-law, solid-mechanics, engineering]
created: 2026-05-02
updated: 2026-05-06
type: concept
sources:
  - "raw/papers/bill-mollison-permaculture-design-course.md"
  - "raw/papers/a-golden-guide-to-hallucinogenic-plants.md"
---

Stress, strain, and elasticity form the foundational framework of solid mechanics mollison [[slimy-clump-water-logged-grass-seed-substrate-failure-modes]] in everything from microscopic semiconductor structures to massive bridges and spacecraft.

Understanding the relationship between applied loads and resulting deformation is critical for ensuring safety, durability, and performance. This page covers the fundamental definitions, constitutive laws, yield criteria, anisotropic behavior, viscoelastic effects, and practical measurement techniques that form the backbone of continuum solid mechanics.

## Fundamental Definitions

**Stress** is force per unit area within a material. Normal stress (σ, sigma) acts perpendicular to a surface: σ = F/A. Shear stress (τ, tau) acts parallel to a surface: τ = V/A for transverse shear, or τ = Tr/J for torsional shear (J = polar moment of inertia). Units are Pascals (Pa = N/m²) in SI or psi in US customary units. The **Cauchy stress tensor** σᵢⱼ fully describes the state of stress at a point as a 3×3 symmetric matrix, with diagonal elements (normal stresses) and off-diagonal elements (shear stresses). Principal stresses (σ₁, σ₂, σ₃) obtained by diagonalization represent normal stresses on planes where shear stress vanishes. The **hydrostatic (mean) stress** σ_m = (σ₁ + σ₂ + σ₃)/3 causes volume change without shape change. The **deviatoric stress** sᵢⱼ = σᵢⱼ − σ_m δᵢⱼ causes shape change without volume change and drives plastic yielding.

**Strain** measures deformation. Engineering (nominal) strain: ε_eng = ΔL/L₀ = (L − L₀)/L₀. True (natural) strain: ε_true = ln(L/L₀) = ln(1 + ε_eng). For small deformations (<~2%) these are nearly identical; the divergence matters in plastic deformation where true strain is always less than engineering strain. True stress σ_true = F/A_current accounts for area reduction during deformation and always exceeds engineering stress beyond the elastic limit. Strain is also a second-order tensor; the infinitesimal strain tensor εᵢⱼ = ½(∂uᵢ/∂xⱼ + ∂uⱼ/∂xᵢ) relates to the displacement field u.

## Hooke’s Law and Elastic Constants

Robert Hooke established the first quantitative relationship in elasticity in 1678 (“ut tensio, sic vis” — “as the extension, so the force”). For uniaxial loading: **σ = Eε**, where E is Young’s modulus (elastic modulus), the slope of the linear elastic region on the stress-strain curve. The generalized 3D form is σᵢⱼ = Cᵢⱼₖₗ · εₖₗ, where C is the fourth-order elasticity tensor (81 components reduced to 21 for general anisotropy, 3 for cubic symmetry, and 2 for isotropy).

**Poisson’s ratio (ν)** describes lateral contraction under axial tension: ν = −ε_transverse/ε_axial. Most metals: ν ≈ 0.28–0.35. Rubber: ν ≈ 0.49 (nearly incompressible). Cork: ν ≈ 0. Thermodynamic stability requires −1 < ν < 0.5.

**Shear modulus G = τ/γ = E/[2(1+ν)]** relates shear stress to shear strain. **Bulk modulus K = −V(dP/dV) = E/[3(1−2ν)]** relates volumetric stress to volumetric strain. For isotropic materials, only 2 of the 4 constants (E, ν, G, K) are independent. Key relationships include: E = 9KG/(3K+G), ν = (3K−2G)/[2(3K+G)], and K = 2G(1+ν)/[3(1−2ν)].

## The Stress-Strain Curve

A typical engineering stress-strain curve for a ductile metal progresses through distinct regions:

**Elastic region:** Linear, reversible deformation with slope E. Stress is proportional to strain (Hooke’s law). The proportional limit marks the end of strict linearity, very close to the elastic limit for most metals. **Yield point:** Some materials (mild steel) show a distinct upper yield point (~250–350 MPa for S235 steel) and lower yield point, followed by Lüders band propagation. Most materials exhibit a gradual transition. The **offset yield strength** is defined by the 0.2% strain offset method: a line parallel to the elastic region from ε = 0.002 intersects the curve at σ_y.

**Strain hardening (work hardening):** Beyond yield, the material strengthens as it deforms plastically. Dislocation density increases from ~10¹⁰ m/² (annealed) to ~10¹⁵ m/² (heavily cold-worked), impeding further dislocation motion. Stress increases with strain at a decreasing rate. The **strain hardening exponent n** from σ = Kε^n correlates with uniform elongation — higher n means more uniform stretching before necking. **Ultimate tensile strength (UTS)** is the maximum engineering stress. After UTS, engineering stress decreases due to localized necking (Considère criterion: dσ/dε = σ at onset of necking), even though true stress continues to rise. **Fracture** occurs when the necked region can no longer sustain the load. Ductile fracture shows cup-and-cone morphology with microvoid coalescence; brittle fracture shows flat, faceted cleavage surfaces.

Typical properties at room temperature: mild steel (AISI 1020): E = 200–205 GPa, σ_y = 250 MPa, UTS = 395–550 MPa, elongation 15–25%. Aluminum 6061-T6: E = 68.9 GPa, σ_y = 276 MPa, UTS = 310 MPa, elongation 12–17%. Annealed copper: E = 110–130 GPa, σ_y = 33–70 MPa, elongation 30–60%. Brittle materials (cast iron, ceramics, concrete) have little or no plastic region.

## Types of Stress

**Tensile stress** (σ = F/A) produces elongation — cables, bolts in tension. **Compressive stress** produces shortening; materials are often stronger in compression than tension (concrete ~10:1, cast iron ~3:1). **Shear stress** acts parallel to surfaces; τ = V/A for transverse shear, τ = Tr/J for torsion. **Bending stress** combines tension and compression in a beam: σ = My/I, maximum at outermost fibers (M = bending moment, y = distance from neutral axis, I = area moment of inertia). **Bearing stress** acts on contact surfaces: σ_b = F/(d·t) for a bolt in a plate.

Mohr’s circle provides a graphical representation of stress state transformation. Maximum shear stress τ_max = (σ₁ − σ₃)/2 occurs on planes oriented at 45° to the principal stress directions. For the general 2D state, principal stresses are σ₁,₂ = (σ_x + σ_y)/2 ± √[((σ_x − σ_y)/2)² + τ_xy²].

**Combined loading** is ubiquitous in real structures. A shaft under torque and bending experiences both shear and normal stresses: the maximum shear stress is τ_max = √[(σ_bending/2)² + τ_torsion²] at the surface. Pressure vessels combine hoop stress σ_hoop = pr/t and longitudinal stress σ_long = pr/(2t) (thin-wall, p = internal pressure, r = radius, t = wall thickness). The von Mises equivalent stress for this biaxial state is σ_vm = √(σ_hoop² − σ_hoopσ_long + σ_long²), yielding σ_vm = √·pr/(2t) ≈ 0.866 pr/t.

## Strain Energy, Resilience, and Toughness

**Elastic strain energy density** (energy per unit volume stored during elastic deformation): u = ∫₀ᵛ σ dε = σ²/(2E) = Eε²/2 for linear elastic uniaxial loading. For a general 3D state: u = (1/2E)[σ₁² + σ₂² + σ₃² − 2ν(σ₁σ₂ + σ₂σ₃ + σ₃σ₁)].

**Modulus of resilience** U_r = σ_y²/(2E) is the maximum elastic strain energy per unit volume before permanent deformation begins. It quantifies how much energy a material can absorb and fully release, a critical parameter for springs, impact absorbers, and precision instruments. Spring steel (σ_y ≈ 1000 MPa, E ≈ 200 GPa): U_r ≈ 2.5 MJ/m³. Mild steel: U_r ≈ 0.156 MJ/m³. **Toughness** is the total energy absorbed up to fracture — the entire area under the engineering stress-strain curve. Ductile materials are tough; brittle materials are not, even if strong. Toughness is measured by Charpy V-notch and Izod impact tests (units: J).

Strain energy decomposes into distortional and volumetric components: U = U_distortion + U_volumetric.

The volumetric component is U_vol = (1−2ν)(σ₁+σ₂+σ₃)²/(6E).

This [[douglas-fir]] fir ~13), E_radial ≈ 0.6–1.8 GPa (~1/10 of longitudinal), E_tangential ≈ 0.4–1.0 GPa. Carbon fiber/epoxy composites are transversely isotropic (5 independent constants): E₁ ≈ 130–180 GPa along fiber, E₂ ≈ 7–10 GPa transverse, G₁₂ ≈ 5–7 GPa. Quasi-isotropic laminates ([0/±45/90]_s) approximate isotropic in-plane behavior.

Cubic metal crystals have 3 independent elastic constants: C₁₁, C₁₂, and C₄₄. The Zener anisotropy ratio Z = 2C₄₄/(C₁₁−C₁₂) measures deviation from isotropy: aluminum Z ≈ 1.22 (nearly isotropic, good for polycrystal approximations), tungsten Z ≈ 1.01 (exceptionally isotropic), iron Z ≈ 2.41, copper Z ≈ 3.21 (significantly anisotropic), and gold Z ≈ 2.85. Single-crystal elastic constants directly influence polycrystal behavior through texture (preferred grain orientation), particularly in rolled sheets and drawn wires where mechanical properties vary with direction relative to the processing direction.

## Viscoelasticity: Time-Dependent Behavior

Viscoelastic materials exhibit both elastic (instantaneous, recoverable) and viscous (time-dependent, dissipative) response. Stress depends on both strain and strain rate.

**Creep** is time-dependent deformation under constant stress. Three stages: primary/transient (decreasing rate), secondary/steady-state (constant rate, most important for design), and tertiary (accelerating, leading to rupture). Creep is significant above ~0.3–0.4 T_melt for metals, and at room temperature for polymers. The Larson-Miller parameter P = T(C + log t_r) predicts time-to-rupture at temperature T.

**Stress relaxation** is the time-dependent decrease in stress under constant strain. A preloaded bolt in a viscoelastic gasket loses clamping force over time. **Maxwell model** (spring E and dashpot η in series): stress relaxes as σ(t) = σ₀ exp(−t/τ), where τ = η/E is relaxation time. **Kelvin-Voigt model** (parallel): strain approaches σ/E exponentially under constant stress. The **Standard Linear Solid** (Zener model) combines elements to capture both creep and relaxation realistically.

Dynamic mechanical analysis (DMA) measures storage modulus E’ (elastic response), loss modulus E’’ (viscous dissipation), and loss tangent tan δ = E’’/E’. The glass transition temperature T_g appears as a sharp peak in tan δ faires-thermal-mass-applications-in-building on his 1820 work on suspension bridges. Augustin-Louis Cauchy (1789–1857) introduced the stress tensor concept in 1823 — the **Cauchy stress principle** states that the traction vector on a surface depends only on the unit normal, establishing the mathematical foundat  echanics. George Green (1793–1841) introduced the strain energy function in 1837, establishing the correct count of 21 independent elastic constants for general anisotropy (resolving a longstanding dispute between Cauchy’s 15-constant theory and Navier’s single-constant “rari-constant” theory). Siméon Denis Poisson (1781–1840) developed the Poisson’s ratio concept and predicted the existence of longitudinal and transverse waves in elastic solids. Woldemar Voigt (1850–1919) conducted extensive elastic constant measurements of single crystals, experimentally confirming the 21-constant theory. Stephen Timoshenko (1878–1972) authored the definitive textbooks *Theory of Elasticity* (1934) and *Strength of Materials*, and is widely regarded as the father of modern engineering mechanics education.

## Yield Criteria and Plasticity Fundamentals

Plastic deformation is permanent, non-recoverable deformation above the yield stress. In metals, plasticity occurs primarily by dislocation motion along slip planes. Schmid’s law governs the resolved shear stress for slip initiation: τ = σ cos(φ) cos(λ) ≥ τ_cr, where φ is the angle between load axis and slip plane normal, and λ is the angle between load axis and slip direction.

**Tresca criterion** (maximum shear stress, 1864): yielding occurs when max(|σ₁−σ₂|, |σ₂−σ₃|, |σ₃−σ₁|)/2 = k = σ_y/2. In principal stress space, this defines a regular hexagonal prism on the deviatoric plane. Conservative but less commonly used in modern design codes.

**Von Mises criterion** (maximum distortional energy, 1913): yielding when the distortional strain energy reaches a critical value: σ_vm = √[½((σ₁−σ₂)² + (σ₂−σ₃)² + (σ₃−σ₁)²)] = σ_y. This defines a circle on the deviatoric (π) plane. More accurate for most ductile metals, the von Mises cylinder circumscribes the Tresca hexagon; maximum difference between them is ~15.5%.

For the general stress state: σ_vm = √(σ_x² + σ_y² + σ_z² − σ_xσ_y − σ_yσ_z − σ_zσ_x + 3τ_xy² + 3τ_yz² + 3τ_zx²).

## See Also

- [[microfungal-life-strategies-ruderal-competitive-stress-tolerant]]
