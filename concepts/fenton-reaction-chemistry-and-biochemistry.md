---
title: "Fenton Reaction: Chemistry and Biochemistry"
created: 2026-04-28
updated: 2026-05-06
aliases:
  - hydroxyl radical generation
  - iron-catalyzed oxidation
  - Haber-Weiss reaction
  - [[bioremediation-fenton-chemistry-brown-rot-fungi]]
  - advanced oxidation processes
tags:
  - biochemistry
  - inorganic-chemistry
  - oxidative-stress
  - environmental-chemistry
  - pharmacology
  - toxicology
related:
  - reactive-oxygen-species
  - glutathione-and-cellular-antioxidant-defense
  - brown-rot-fungi-biodegradation
  - ferroptosis
  - bioremediation-fenton-chemistry
  - bioremediation-laccase-mediator-systems
type: concept
sources:
  - "raw/papers/permaculture-a-designers-manual-bill-mollison.md"
---

## Overview

The Fenton reaction is a redox process in which ferrous iron (Fe2+) catalyzes the decomposition of [[cervantes-hydrogen-peroxide-sterilization]] (H2O2) to produce the hydroxyl radical (OH.), one of the strongest oxidants known in chemistry. The canonical equation is:

**Fe2+ + H2O2 -> Fe3+ + OH. + OH-**

First observed by H.J.H. Fenton in 1894 during tartaric acid oxidation at the University of Cambridge, this reaction underpins phenomena from [[fungal-industrial-wastewater-treatment]] treatment to the molecular basis of neurodegenerative disease. The hydroxyl radical has a standard reduction potential of E = +2.80 V, second only to fluorine among common oxidants, and reacts at diffusion-limited rates with virtually all biomolecules it encounters.

## Historical Discovery

Henry John Horstman Fenton (1854-1929) reported in 1894 that a mixture of Fe2+ and H2O2 could oxidize tartaric acid, describing it as a "new oxidizing agent" in the Journal of the Chemical Society. He did not identify the hydroxyl radical as the active species. Fritz Haber and Joseph Weiss proposed the radical mechanism involving superoxide and H2O2 in 1934 (*Proc. R. Soc. Lond. A*, 147, 332-351). Through the 1930s-1950s, Baxendale, Evans, Uri, and Weiss progressively elucidated radical intermediates. Chester Walling and colleagues in the 1960s-1970s established the detailed mechanism and kinetics, demonstrating the hydroxyl radical as the key intermediate using radical traps and product analysis (*Acc. Chem. Res.*, 1975, 8, 125-131).

## The Haber-Weiss Cycle

Haber and Weiss (1934) proposed the overall reaction: **O2.- + H2O2 -> O2 + OH. + OH-**. This proceeds negligibly on its own (k < 0.3 M-1s-1) but becomes significant when catalyzed by transition metals. The cycle decomposes into two steps: the Fenton reaction and [[bioremediation-fungal-iron-reduction-chelation-metal-solubilization]] by superoxide:

**Fe3+ + O2.- -> Fe2+ + O2**  (k ~10^5 M-1s-1)

This superoxide-mediated Fe3+ reduction is far faster than H2O2-mediated regeneration (k ~0.001-0.01 M-1s-1), making it the dominant pathway in biological systems where superoxide is continuously produced by mitochondrial electron transport and NADPH oxidases.

## Mechanism and Kinetics

The classical Fenton reaction proceeds through inner-sphere electron transfer with O-O bond cleavage. The rate constant at pH 3 is approximately 40-80 M-1s-1. The regeneration of Fe2+ from Fe3+ is rate-limiting in catalytic cycles. The recovery step (Fe3+ + H2O2 -> Fe2+ + OOH. + H+) is orders of magnitude slower than the primary Fenton reaction. The net catalytic reaction yields: **2 H2O2 -> 2 OH. + H2O + O2** (iron-catalyzed).

## pH Dependence

Optimal hydroxyl radical production occurs at pH 2.5-3.5. Below pH 2, H2O2 is stabilized as H3O2+ and excess protons quench the hydroxyl radical. Above pH 4, Fe3+ precipitates as Fe(OH)3, removing the catalyst from solution. At pH > 5, iron forms various hydroxo complexes (Fe(OH)2+, Fe(OH)2+, Fe(OH)3(aq), Fe(OH)4-) that alter reactivity. At neutral pH, chelated iron (Fe-EDTA, Fe-citrate, siderophore complexes from humic substances) can sustain Fenton activity, which is how the reaction operates in biological and environmental systems. In cells, the labile iron pool is maintained at extremely low concentrations (~0.1-1 uM) by ferritin storage and transferrin binding, constraining Fenton activity.

## Fenton-Like Reactions with Other Metals

Other transition metals catalyze analogous reactions with hydrogen peroxide. Copper is more reactive (**Cu+ + H2O2 -> Cu2+ + OH. + OH-**, k ~10^4 M-1s-1), relevant to Wilson's disease where copper accumulates in tissues and Cu/Zn-SOD acts as a pro-oxidant when depleted of zinc. Manganese is far less reactive (k ~1.5 M-1s-1), which is evolutionarily significant: Mn-SOD is used in mitochondria precisely because it dismutates superoxide without generating hydroxyl radicals. Cobalt (cobalt toxicity) and chromium(V) (chromium carcinogenesis) also participate. The general reactivity order is: **Cu+ > Fe2+ > Cr(V) > Co2+ > Mn2+**.

## Role in Biological Oxidative Stress

The hydroxyl radical is extraordinarily short-lived (~10^-9 s in biological media) and damages whatever biomolecule it encounters at its site of generation. Key molecular targets include DNA bases (forming mutagenic 8-hydroxy-2'-deoxyguanosine, 8-OHdG), polyunsaturated [[blesching-cannabis-apoptosis-and-cancer-cell-death]] driven by lipid peroxidation -- is directly linked to Fenton chemistry and represents an active area of cancer drug development.

## Antioxidant Defense Systems

Cells employ a three-tiered defense against Fenton-generated reactive oxygen species. The **enzymatic first line** includes superoxide dismutase (three isoforms: Cu/Zn-SOD cytosolic, Mn-SOD mitochondrial, EC-SOD extracellular) removing superoxide to limit Fe3+ reduction; catalase in peroxisomes (2 H2O2 -> 2 H2O + O2, k ~10^7 M-1s-1, turnover ~4 x 10^7 molecules/s); glutathione peroxidase using GSH as electron donor (effective at low H2O2 concentrations where catalase is less efficient); and peroxiredoxins (highly abundant, sensitive to low H2O2 levels). The **non-enzymatic second line** includes glutathione (1-10 mM), vitamin E (chain-breaking in membranes), vitamin C (paradoxically pro-oxidant at high concentrations with free iron), uric acid, and melatonin. The **metal sequestration third line** includes transferrin (Kd ~10^-22 M), ferritin (intracellular iron storage), metallothioneins (copper/zinc binding), and lactoferrin.

## Advanced Oxidation Processes in Water Treatment

The Fenton reaction is a cornerstone of advanced oxidation processes (AOPs) for degrading recalcitrant organic pollutants. Effective targets include phenols, azo dyes, pesticides, pharmaceuticals, endocrine disruptors, and BTEX compounds. Typical conditions: 10-100 mg/L Fe2+ and 50-500 mg/L H2O2 at pH 2.5-3.5. Hydroxyl radicals attack through hydrogen abstraction from C-H bonds, electrophilic addition to double bonds and aromatic rings, and electron transfer from anions and amines.

### Photo-Fenton

UV irradiation enhances the process through Fe3+ photoreduction (Fe3+ + H2O + hv -> Fe2+ + OH. + H+, lambda < 400 nm) and direct H2O2 photolysis (H2O2 + hv -> 2 OH., lambda < 300 nm). Fe(III)-oxalate complexes extend activity into visible wavelengths, enabling solar-driven treatment and extending the effective pH range to approximately 3-5 with higher hydroxyl radical yields.

### Electro-Fenton

Cathodic H2O2 production (O2 + 2H+ + 2e- -> H2O2 at carbonaceous cathodes) combined with cathodic Fe3+ regeneration eliminates H2O2 storage needs. Boron-doped diamond anodes provide additional direct oxidation. Four configurations exist: classic electro-Fenton, Fenton peroxi-coagulation, peroxi-electrocoagulation, and photoelectro-Fenton. Mineralization efficiencies exceeding 90% are achievable.

### Heterogeneous Fenton

Solid catalysts including magnetite (Fe3O4), goethite, iron-loaded zeolites, and zero-valent iron (Fe0) address the iron sludge problem. These operate at near-neutral pH and allow catalyst recovery, though with slower kinetics (Brillas et al., *Chem. Rev.*, 2009, 109, 6570-6631).

## Fenton Chemistry in Brown Rot Fungi

[[brown-rot-and-white-rot-fungi-in-mycoremediation]] fungi to degrade cellulose and hemicellulose while leaving lignin intact (Kersten & Cullen, *J. Biotechnol.*, 2007, 129, 608-617).

## Environmental and Atmospheric Fenton Chemistry

In soils, Fe(II)-bearing minerals (pyrite FeS2, siderite FeCO3, magnetite Fe3O4, green rust) generate hydroxyl radicals through Fenton-like reactions with microbially and photochemically produced H2O2. [[mycoremediation]]
- [[glutathione-biochemistry-and-redox-biology]]
