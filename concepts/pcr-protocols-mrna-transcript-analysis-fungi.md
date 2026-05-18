---
title: PCR Protocols and mRNA Transcript Analysis in Fungi
source: unknown-biodiversity-of-fungi.md
type: concept
---

# PCR Protocols and mRNA Transcript Analysis in Fungi

## Overview

PCR-based methods and mRNA transcript analysis are cornerstone techniques for studying [[fungal-biodiversity]], species detection, and gene expression in environmental and laboratory settings. This concept covers the progression from arbitrary priming through dual-primer and nested-primer PCR strategies for sensitive species detection, detailed fungal tissue collection and DNA extraction protocols, and the specialized challenges of mRNA transcript analysis in complex fungal substrata.

## Arbitrary-Primed PCR (apPCR) as a Foundation

Arbitrary-primed PCR (apPCR) serves as the foundational screening method for generating species-specific genetic markers. Single short primers of arbitrary sequence anneal at low stringency to multiple sites across a fungal genome, producing reproducible banding patterns that differentiate species. These patterns are then cloned and sequenced to design targeted primers for downstream applications.

### apPCR Reaction Conditions

| Parameter          | Value                      |
|--------------------|----------------------------|
| Reaction volume    | 20 µl                      |
| Number of cycles   | 35                         |
| Denaturation       | 93°C for 15 seconds        |
| Annealing          | 56°C for 1.5 minutes       |
| Extension          | 72°C for 1.5 minutes       |
| Ramp times         | 1 minute between steps     |

The deliberate 1-minute ramp times provide the low stringency necessary for arbitrary primers to bind at multiple genomic loci.

## Dual-Primer PCR (dpPCR)

Dual-primer PCR employs two defined primers flanking a target region identified through apPCR, providing robust species-specific detection suitable for environmental monitoring.

### Sensitivity

- Detects target species DNA at ratios as low as **1:100** in mixed samples.
- As little as **25 picograms** of genomic DNA is sufficient for reliable detection.
- Does not require slow ramp times, making it faster and more amenable to standard thermocycler programs.

### Reaction Conditions

dpPCR uses the same buffer composition as apPCR but with two specific primers: annealing at **58°C** with no ramp times (standard transitions).

### Species Monitoring

dpPCR is well suited for detecting target fungal species directly in environmental samples such as soil, plant tissue, and water. Its tolerance for modest thermocycler accuracy makes it practical for ecological surveys and plant pathology diagnostics.

## Nested-Primer PCR (npPCR)

Nested-primer PCR introduces a two-step amplification strategy that dramatically increases detection sensitivity over dpPCR alone.

### Mechanism

1. **First round:** dpPCR is performed, producing an amplicon of known size.
2. **Second round:** The dpPCR product is diluted **fivefold** and re-amplified using **nested primers** positioned 10–20 bp inward from the terminal ends of the dpPCR product.

### Sensitivity and Applications

- Increases detection sensitivity by **100–1000 fold** compared to dpPCR alone.
- Capable of detecting **a few fungal genomes** within highly complex environmental matrices.
- Like dpPCR, npPCR is relatively forgiving of thermocycler temperature accuracy.

| Method   | Sensitivity          | Use Case                              |
|----------|---------------------|---------------------------------------|
| dpPCR    | ~25 pg DNA, 1:100   | General species screening             |
| npPCR    | Few genome copies    | Trace detection in complex samples    |

## Fungal Tissue Collection and DNA Extraction

### Tissue Preservation

Fungal tissue is placed in a preservation buffer containing **EDTA, Tris, and N-lauroylsarcosine**, which stabilizes nucleic acids for **1+ year at ambient temperature**, eliminating the need for immediate freezing during field collection.

### Extraction Protocol

1. **Pulverization:** Preserved tissue is mechanically pulverized (bead beating or mortar and pestle with liquid nitrogen).
2. **Lysis:** Samples incubated at **65°C** for cell wall disruption and protein denaturation.
3. **Centrifugation:** Cellular debris pelleted; supernatant containing nucleic acids recovered.
4. **PEG/NaCl Precipitation:** Polyethylene glycol and sodium chloride precipitate polysaccharides and contaminants.
5. **Ammonium Acetate Protein Precipitation:** Proteins removed by ammonium acetate treatment and centrifugation.
6. **Isopropanol DNA Precipitation:** Purified DNA recovered by isopropanol precipitation, washed, and resuspended in TE buffer.

### Mycelial Culture and Harvest

For species such as *Colletotrichum*, mycelial cultures are grown under defined conditions, harvested by filtration or centrifugation, and processed through the same extraction pipeline. Cultured mycelium provides abundant, high-quality DNA essential for initial primer design and assay validation.

## Thermocycler Calibration

Thermocycler performance should be verified using a **scanning thermocouple thermometer with 12 probes**, which simultaneously measures temperature across all block positions to ensure uniform heating and cooling. While dpPCR and npPCR tolerate minor inaccuracies, apPCR with its deliberate ramp times depends on precise calibration.

## Cloning apPCR Products for Species-Specific Primer Design

Target bands are excised from gels and processed through: **glass bead purification** → ligation into the **pT7Blue vector** for *E. coli* propagation → **Sanger sequencing** → species-specific primer design.

### Example: *Colletotrichum magna*

| Primer Set | Purpose                | Primers   |
|------------|-----------------------|-----------|
| Primary    | dpPCR detection       | p365/p366 |
| Nested     | npPCR detection       | p413/p415 |

The nested primers p413/p415 were positioned inward from the dpPCR amplicon ends, enabling the 100–1000 fold sensitivity boost.

## mRNA Transcript Analysis in Fungi

Drawing on work by Dan Cullen, this section addresses the unique challenges and methods for fungal transcript analysis in environmental contexts.

### Challenges in Complex Substrata

mRNA is **rarely analyzed directly** from complex environmental samples due to:

- **RNA lability:** mRNA degrades rapidly upon cell lysis, requiring immediate stabilization.
- **Humic substance interference:** Humic acids potently **inhibit Taq polymerase**, causing false negatives in RT-PCR.
- **Low abundance:** Target transcripts may be at extremely low copy numbers in environmental samples.

### Magnetic Capture Techniques

**Oligo(dT) magnetic bead capture** selectively isolates polyadenylated RNA (mRNA) from total [[nucleic-acid]] extracts. This enriches mRNA by binding the poly(A) tail, removes PCR inhibitors (including humic substances) during washing, and yields RNA of sufficient purity for reverse transcription and PCR.

### Competitive RT-PCR

**Competitive RT-PCR** is the preferred quantitative method: a known quantity of synthetic competitor RNA (identical amplification efficiency but distinguishable by size or sequence) is co-amplified with the target transcript. The target-to-competitor product ratio provides absolute transcript abundance, correcting for variations in reverse transcription and PCR efficiency between samples.

### Application: Lignin Peroxidase in *Phanerochaete chrysosporium*

The [[lignin-peroxidase]] (LiP) gene family in the white-rot fungus *P. chrysosporium* serves as a model system:

- **Defined media:** Multiple LiP transcripts are readily detected at high abundance.
- **Soil pollutant degradation:** Some LiP transcripts abundant in defined media are **absent** during actual soil-based pollutant degradation, highlighting limitations of inferring *in situ* activity from laboratory culture data.

### Genomic Context

The *P. chrysosporium* genome, completed at the **DOE Joint Genome Institute**, reveals **>10,000 predicted genes**, enabling potential microarray-based expression profiling. However, fabrication cost and substantial RNA quantity requirements have limited routine environmental application.

### Housekeeping Genes as Internal Standards

| Gene       | Full Name                                    | Function                |
|------------|----------------------------------------------|-------------------------|
| GAPDH      | Glyceraldehyde-3-phosphate dehydrogenase     | Glycolysis              |
| β-actin    | Beta-actin                                   | Cytoskeletal structure  |
| HPRT       | Hypoxanthine phosphoribosyltransferase       | Purine salvage pathway  |

Stability of these reference genes should be empirically validated for each experimental system.

### Critical Considerations

1. **Transcript levels ≠ protein levels:** mRNA abundance does not necessarily correlate with functional protein levels due to post-transcriptional regulation and protein turnover.
2. **Avoid over-cycling:** Excessive PCR cycles distort the linear template-to-product relationship, compromising quantitative accuracy.
3. **Environmental relevance:** Laboratory expression data must be validated against environmental samples to confirm ecological relevance.
