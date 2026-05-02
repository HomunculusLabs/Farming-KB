---
title: Fungal Cyanide Degradation
created: 2026-04-14
updated: 2026-04-14
type: concept
tags: [mycology, fungi]
sources: []
---
# Fungal Cyanide Degradation

## Overview

Cyanide is a potent metabolic inhibitor that targets cytochrome oxidase in the mitochondrial respiratory chain. Despite its extreme toxicity, several fungal species can tolerate, degrade, and even utilize cyanide as a nitrogen source. This capability has applications in treating industrial wastes from gold mining, electroplating, and coal gasification. For broader context on fungal enzymatic degradation, see [[enzymatic-degradation-in-mycoremediation]].

## Cyanide Contamination Sources

Cyanide-containing wastes arise from:

- **Gold and silver mining**: Heap leaching with alkaline cyanide solutions (KCN, NaCN)
- **Steel manufacturing**: Coke ovens and blast furnace gas scrubbing
- **Coal gasification**: Former gasworks sites contaminated with spent oxide and Prussian Blue
- **Electroplating and metal finishing**: Metal-cyanide complexes in rinse waters
- **Chemical industry**: Nitrile and cyanohydrin production byproducts

At contaminated gasworks sites, cyanide occurs as free cyanide (CN⁻/HCN), weak acid dissociable complexes (e.g., Ni(CN)₄²⁻), and strong complexes (e.g., Fe(CN)₆³⁻/⁴⁻). Prussian Blue (ferric ferrocyanide) is particularly problematic due to its stability.

## Cyanide Hydratase Pathway

The primary fungal enzyme for cyanide degradation is **cyanide hydratase**, which converts cyanide to formamide:

```
HCN + H₂O → HCONH₂  (catalyzed by cyanide hydratase)
```

Formamide is subsequently hydrolyzed by formamidase and formate dehydrogenase:

```
HCONH₂ + H₂O → HCOOH + NH₃  (formamidase)
HCOOH → CO₂ + 2H⁺ + 2e⁻    (formate dehydrogenase)
```

Ammonia serves as a nitrogen source for fungal growth, while formic acid is oxidized to CO₂. The complete pathway detoxifies cyanide to harmless end products.

## Cyanide Hydratase Properties

Cyanide hydratase is a large oligomeric protein (~300+ kDa) composed of 43–45 kDa subunits. Key properties:

| Species | pH Optimum | Native Mass (kDa) | Km (mmol/L) |
|---|---|---|---|
| Fusarium solani | 7.5 | 9 × 300 | 4.7 |
| Fusarium lateritium | 8.5 | 9 × 300 | 43 |
| Gloeocercospora sorghi | 7–8 | 9 × 300 | 12 |
| Fusarium solani IHEM8026 | 7–8 | — | — |
| Stemphylium loti | 7–9 | 9 × 600 | — |

The relatively high Km values (4–43 mmol/L) indicate low affinity for cyanide, which may limit commercial potential for high-volume effluent treatment.

## Fungal Species Capable of Cyanide Degradation

### Fusarium solani
The most extensively studied cyanide-degrading fungus. Key strains:

- **F. solani IHEM 8026**: Isolated from contaminated alkaline wastes; degrades cyanide at pH 9.2–10.7. Cyanide degradation associated with large biomass increase.
- **F. solani (Barclay strain)**: Degrades both free and metal-complexed cyanides under neutral and acidic conditions (pH 4–7). Part of consortia with Trichoderma polysporum or F. oxysporum + Scytalidium thermophilium + Penicillium miczynski.

### Fusarium oxysporum
Isolated at pH 8 growing on cyanide as sole nitrogen source. Converts cyanide to formamide via cyanide hydratase.

### Fusarium lateritium
Cyanide hydratase gene (chy) shares 65% nucleotide homology with G. sorghi and 82% with L. maculans. Cys-163 identified as essential active site residue.

### Other Species
- **Gloeocercospora sorghi**: Pathogen of cyanogenic sorghum plants
- **Leptosphaeria maculans**: Gene for cyanide hydratase identified with GATA regulatory elements
- **Stemphylium loti**: Immobilized mycelia packed into columns for cyanide waste treatment
- **Cladosporium cladosporioides**: Highly efficient biosorbent of copper and nickel cyanides (optimal at pH 4)

## Metal-Cyanide Complex Degradation

Fungal degradation of metal-cyanide complexes depends on complex stability:

- **Nickel cyanide** K₂Ni(CN)₄: Complete cyanide removal in 3–5 days at neutral pH
- **Iron cyanide** K₄Fe(CN)₆: Complete removal takes up to 28 days at pH 4; no degradation at pH 7

The enzyme likely acts on free cyanide (HCN) released through partial dissociation, not on the intact complex. Evidence: identical chy genes induced by both KCN and metal-cyanide complexes, and growth rate correlates with complex stability.

## Cyanide-Insensitive Respiration

Since cyanide inhibits cytochrome oxidase, cyanide-degrading fungi require an alternative terminal oxidase pathway:

- Induced by cyanide and antimycin A
- Becomes active when the ubiquinone pool is 50–60% reduced
- Provides energy for cyanide hydratase induction and activity
- Confirmed in F. oxysporum and S. loti
- Encoding genes are highly conserved across organisms

## Molecular Biology

Key findings from genetic studies:

- **Gene induction**: chy transcription begins 30–60 minutes after cyanide exposure; stops 12–24 hours after exposure
- **Regulation**: Cyanide hydratase promoter contains four GATA protein sites for nitrogen metabolism regulation
- **Inducers**: KCN, propionitrile, and metal cyanides induce chy; formamide and acetonitrile do not
- **Essential residue**: Cys-163 is part of the active site in both cyanide hydratase and cyanide dihydratase
- **Phylogenetics**: Cyanide hydratase groups with nitrilase enzymes, not nitrile hydratases

## Applications

### Wastewater Treatment
Fusarium strains can treat cyanide-containing wastewaters under acidic, neutral, and alkaline conditions. Combined biosorption + biodegradation approaches have been proposed.

### Soil Remediation
Ex situ slurry treatment of cyanide-contaminated soils using Fusarium spp. has been demonstrated. In situ remediation is theoretically possible but undeveloped.

### Commercial Products
ICI Biological Products produced dried F. lateritium mycelia that could be sprayed onto cyanide-containing wastes.

### Monitoring
Molecular probes (PCR for chy gene, RT-PCR for mRNA) can monitor in situ bioremediation activity and optimize treatment conditions.

## Comparison with Bacterial Systems

While bacteria like Pseudomonas fluorescens possess cyanide oxygenase and cyanide dihydratase with higher cyanide affinity (Km ~1.2 mmol/L), fungi offer advantages: broader pH tolerance, ability to degrade both free and metal-complexed cyanides, and tolerance to high metal concentrations. See [[combined-biological-remediation-approaches]] for integrated treatment strategies.

## Related

- [[mycoremediation-textile-dye-degradation]]
- [[fungal-heavy-metal-biosorption-detailed]]
- [[white-rot-fungi-bioremediation]]
- [[fungal-cyanide-biodegradation-detailed]]

- [[staycare-cyanide-biodegradation-by-fungi]]
- [[singh-fungal-treatment-industrial-wastewaters-overview]]
