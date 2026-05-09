---
title: "Analytical Methods for Psilocybin and reversed-phase-hplc-psilocybin-psilocin-quantification-bigwood-beug"
concept_type: chemistry
topic: analytical-chemistry
related: ["variation-of-psilocybin-and-psilocin-levels-bigwood-beug", "street-sample-potency-variability-in-psilocybe-cubensis", "tihkal-psilocin-psilocybin-chemistry"]
created: 2026-05-09
---

# Analytical Methods for Psilocybin and Psilocin Quantification

## Introduction

Accurate quantification of psilocybin (O-phosphoryl-4-hydroxy-N,N-dimethyltryptamine) and psilocin (4-hydroxy-N,N-dimethyltryptamine) in mushroom tissue, spores, mycelium, and biological matrices is essential for pharmacological research, clinical trials, forensic analysis, and quality control in cultivation. The analytical challenge is significant: psilocybin is thermally labile, psilocin oxidizes readily at ambient conditions, and both compounds are present alongside numerous structural analogs (baeocystin, norbaeocystin, aeruginascin) that require chromatographic separation.

### Historical Context

The first quantitative [[hplc-analysis-of-psilocybin-and-psilocin]] in mushrooms was performed by Albert Hofmann and colleagues at Sandoz in 1959, using paper chromatography and UV spectroscopy. The Bigwood and Beug study (published in 1981) was a landmark, employing HPLC-UV to systematically quantify alkaloid content across multiple *Psilocybe* species, flushes, and tissue types. Since then, LC-MS/MS has become the preferred method, offering orders-of-magnitude improvements in sensitivity and enabling simultaneous multi-analyte quantification in complex biological matrices.

## Sample Collection and Stability

### Pre-Analytical Considerations

Proper sample handling is critical for accurate quantification:

- **Psilocybin stability**: Relatively stable in dried mushroom tissue when stored at -20°C in the dark. Degrads slowly at room temperature through non-enzymatic dephosphorylation to psilocin.
- **[[shirota-psilocin-instability-chromatographic-challenges]]**: Rapidly oxidizes in solution and in fresh tissue. Oxidation products include blue pigments (quinone polymers) visible in bruised mushroom tissue.
- **Drying effects**: Air-drying at moderate temperatures (<40°C) preserves alkaloid content. Oven-drying above 60°C causes significant psilocybin degradation.
- **Storage**: Long-term storage of dried material at -20°C in amber vials under inert atmosphere preserves >95% of alkaloid content for years.

### Sample Preparation Methods

**Extraction** is typically performed using methanol, ethanol, or acidified aqueous-organic mixtures. The choice of extraction solvent affects recovery: methanol provides the best extraction efficiency for both psilocybin and psilocin, with the addition of 0.1% formic acid improving psilocin recovery by reducing oxidation. Ethanol is preferred in some regulatory contexts for safety compliance. A standard protocol: homogenize 100 mg dried mushroom powder in 10 mL methanol, sonicate 15 min, centrifuge at 4000 rpm for 10 min, filter through 0.22 μm PTFE membrane, and inject. For biological matrices (blood, urine, plasma), solid-phase extraction (SPE) using mixed-mode [[mollison-designers-tropical-soils-and-cation-exchange-management]] cartridges provides cleaner extracts and lower matrix effects.

## Chromatographic Methods

### HPLC-UV

HPLC with UV detection is the most widely used method for routine quantification. Standard conditions: C18 reversed-phase column (150–250 mm × 4.6 mm, 5 μm), UV detection at 267–270 nm (near the indole chromophore absorption maximum), ammonium formate or acetate buffer (pH 3–4) with acetonitrile or methanol gradient, flow rate 0.8–1.2 mL/min. LOD ~0.1 μg/mL for psilocybin, ~0.05 μg/mL for psilocin; LOQ ~0.3 and ~0.15 μg/mL respectively. Advantages: widely available instrumentation, good reproducibility, adequate sensitivity. Limitation: UV detection cannot distinguish co-eluting indole alkaloids without complete chromatographic separation.

### LC-MS/MS

LC-MS/MS is the gold standard for specificity and sensitivity. Electrospray ionization (ESI) in positive mode with multiple reaction monitoring: psilocybin m/z 285→168 (quantifier) and 285→240 (qualifier); psilocin m/z 205→160 (quantifier) and 205→188 (qualifier). LOD 0.01–0.05 ng/mL, LOQ 0.03–0.15 ng/mL. Enables simultaneous quantification of psilocybin, psilocin, baeocystin, norbaeocystin, and aeruginascin in biological matrices (blood, urine, plasma). Sample preparation typically involves protein precipitation or solid-phase extraction.

### GC-MS

GC-MS requires derivatization due to thermal lability. Silylation with BSTFA (N,O-bis(trimethylsilyl)trifluoroacetamide) or MSTFA converts psilocin to its TMS derivative; psilocybin may be analyzed as the TMS-ester or after enzymatic dephosphorylation. DB-5MS column (30 m × 0.25 mm), temperature program 70°C initial ramping to 280°C at 15°C/min. LOD ~1 ng on-column for derivatized psilocin. Valuable in forensic applications due to extensive spectral libraries, but derivatization adds time and introduces variability.

### HPTLC and CE

**HPTLC** (High-Performance Thin-Layer Chromatography) with silica gel 60 F₂₅₄ plates and ethyl acetate:methanol:ammonia (17:2:1) mobile phase provides low-cost, high-throughput screening. Ehrlich's spray reagent gives characteristic purple-pink indole visualization. Densitometric scanning at 285 nm allows semi-quantitative analysis with ±10–15% accuracy. HPTLC is particularly useful for rapid screening of large sample batches in cultivation settings and for preliminary identification in forensic contexts.

**Capillary electrophoresis** (CE) offers fast, minimal-solvent separation based on charge-to-size ratio. Micellar electrokinetic chromatography (MEKC) with sodium dodecyl sulfate as the micellar phase provides separation of psilocybin and psilocin within 10 minutes. UV detection at 267 nm provides LODs comparable to HPLC-UV. CE requires minimal sample volume (<5 nL injection) and generates essentially no organic solvent waste, making it attractive for green chemistry applications.

## Spectroscopic Methods

### UV-Visible Spectrophotometry

Simple UV-Vis spectroscopy provides crude quantification based on the indole absorption at 267 nm. While not specific (any indole compound absorbs at this wavelength), it can be useful for rapid screening when combined with prior chromatographic separation. Psilocybin shows λmax at 267 nm in acidic aqueous solution with molar absorptivity ε ≈ 34,000 L·mol⁻¹·cm⁻¹. Beer's law is linear over the concentration range 2–40 μg/mL.

### NMR and Immunochemical Methods

¹H-NMR in DMSO-d₆ shows characteristic psilocybin signals: singlet at δ 2.95 ppm (6H, N-CH₃), aromatic multiplets at δ 6.8–7.4 ppm, and phospho-methylene at δ 3.6 ppm. Quantitative NMR (qNMR) using maleic acid as internal standard provides absolute quantification without reference standards — valuable when certified reference materials are unavailable. ELISA methods using polyclonal antibodies raised against psilocybin-protein conjugates achieve LOD of 0.1–1.0 ng/mL for screening urine and blood samples, but cross-reactivity with psilocin, baeocystin, and other 4-substituted tryptamines limits specificity. Lateral flow immunoassay devices for point-of-care detection are in development for law enforcement and harm reduction applications.

## Colorimetric Methods

### Colorimetric Screening

**Ehrlich's reagent** (1% p-dimethylaminobenzaldehyde in ethanol:concentrated HCl, 1:1) produces a characteristic purple-pink color with indoles within seconds. This is the classic field identification method — it reacts with all indole compounds and is not specific to psilocybin, but is useful for rapid screening of mushroom tissue. Color intensity correlates approximately with alkaloid concentration, though extraction efficiency, oxidation state, and matrix effects affect the correlation. The **van Urk reagent** (similar composition with different acid proportions) provides slightly different color responses for different indole alkaloids, enabling crude discrimination in TLC applications. For semi-quantitative work, densitometric scanning of HPTLC plates at 285 nm provides approximate quantification with ±10–15% accuracy.

## Factors Affecting Analytical Results

### Post-Harvest Degradation

Alkaloid content changes significantly after harvest:

- **Fresh to dry conversion**: Psilocybin is stable during air-drying; psilocin may decrease 10–30% due to oxidation.
- **Enzymatic dephosphorylation**: Phosphatase enzymes in fresh tissue can convert psilocybin to psilocin if drying is delayed.
- **Long-term storage**: Even properly stored samples show gradual alkaloid loss of 1–5% per year.

### Intra-Fruiting Body Variation

[[cap-and-stem-alkaloid-distribution-in-psilocybe-cubensis-strains]] is non-uniform within a single mushroom: caps contain 2–3× more psilocybin than stipes (dry weight basis), gill lamellae have the highest concentrations, and the basal mycelium has the lowest. Mature fruiting bodies have higher total alkaloid content than young pins. This variation has implications for [[lichen-biodiversity-sampling-protocols-data-analysis]] — homogenizing the entire fruiting body is recommended for representative results.

### Reporting Conventions

Standard reporting requires: dry-weight basis (mg/g or % dry weight), species identification with voucher specimen, extraction method, analytical method with LOD/LOQ, and individual compound concentrations (psilocybin, psilocin, baeocystin, norbaeocystin separately). Certified reference materials are available from Cerilliant, Cayman Chemical, and Toronto Research Chemicals. Reference solutions in methanol are stable for months at -20°C; psilocin solutions degrade within days at room temperature. Method validation should include assessment of linearity (r² > 0.999), precision (intra-day and inter-day RSD < 5%), accuracy (recovery 85–115%), and matrix effects (<15% ion suppression/enhancement in biological matrices).

## Applications by Context

### Clinical and Pharmacological Research

In clinical trials of psilocybin-assisted therapy, LC-MS/MS is the standard for pharmacokinetic studies. Blood plasma samples require protein precipitation (typically with acetonitrile) prior to analysis. Psilocybin has a short half-life (~2–3 hours), being rapidly dephosphorylated to psilocin, which has a longer half-life (~4–6 hours). Both parent compound and metabolite must be quantified to characterize the full pharmacokinetic profile.

### Forensic Analysis

Forensic laboratories primarily use GC-MS for seized mushroom samples, leveraging extensive spectral libraries for identification and legal proceedings. LC-MS/MS is increasingly adopted for toxicological screening of biological samples in DUI and death investigation cases. Immunoassay screening followed by confirmatory LC-MS/MS is the recommended two-tier approach.

### Cultivation Quality Control

Cultivators use HPLC-UV for routine potency testing due to lower cost and wider availability. Results are typically reported as total psilocybin equivalent (sum of psilocybin and psilocin × 0.718 molecular weight correction factor). Batch-to-batch consistency monitoring helps optimize cultivation conditions for target alkaloid levels.

### Mycelium and Biomass Testing

Testing of mycelium grown in liquid culture (biomass) is increasingly relevant as commercial production scales for nutraceutical and therapeutic applications. Alkaloid levels in mycelium are typically 10–100× lower than in fruiting bodies, requiring the sensitivity of LC-MS/MS for reliable detection. The mycelial alkaloid profile may also differ from fruiting body profiles, with relatively higher proportions of baeocystin and norbaeocystin in some strains.

## Emerging Techniques

### DART-MS and Ambient Ionization

**Direct Analysis in Real Time mass spectrometry** (DART-MS) enables rapid screening of mushroom tissue with minimal sample preparation — a small piece of dried cap is placed in the DART gas stream and spectra are acquired within seconds. While less precise than chromatographic methods, DART-MS can detect psilocybin at ng/g levels and distinguish *Psilocybe* species from non-active lookalikes. This technique is being explored for field-portable screening by law enforcement and customs agencies.

### Electrochemical Sensors

Electrochemical biosensors using screen-printed carbon electrodes modified with molecularly imprinted polymers (MIPs) offer a promising low-cost alternative for point-of-use detection. These devices measure the oxidation current of psilocin at the electrode surface and can achieve LODs of 0.1–1.0 μg/mL. Integration with smartphone-based potentiostats could enable decentralized potency testing by consumers and harm reduction organizations.

## See Also

- [[bigwood-beug-miniculture-rye-grain-flush-variation-method]]
- [[street-sample-potency-variability-in-psilocybe-cubensis]]
- [[tihkal-psilocin-psilocybin-chemistry]]
- [[baeocystin-and-norbaeocystin-in-psilocybin-biosynthesis]]
