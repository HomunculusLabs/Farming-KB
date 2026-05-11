---
title: 16S Rrna Sequencing Microbiome Analysis
created: 2026-04-28
tags: [methods, sequencing, bioinformatics]
date: 2026-04-28
updated: 2026-04-28
sources:
  - /Users/t3rpz/wiki/raw/papers/understanding-cultivar-specificity-cannabis-microbiome.md
type: concept
---

# 16S rRNA Sequencing for Microbiome Analysis

## Overview

Winston et al. (2014) used Illumina 16S rRNA gene sequencing to characterize
[[cultivar-endorhiza-bacterial-communities-cannabis]] associated with Cannabis roots and soil. The study
targeted the V4 hypervariable region of the 16S rRNA gene, following the
Earth Microbiome Project standard protocols. A total of 69 samples were
sequenced across two experiments, analyzed using the [[qiime-bioinformatics-pipeline-16s-rrna-microbiome]]
pipeline with both closed and open reference OTU picking methods.

## Sample Summary

The study sequenced samples from three compartments (endorhiza, rhizosphere,
bulk soil) across five Cannabis cultivars in two separate experiments:

- **Experiment 1**: 27 samples from three cultivars (Burmese, Bookoo Kush,
  [[maui-wowie]])
  grown in two soil types (Vista and Orange County, California). Samples
  were taken 2 weeks before harvest. One sample was discarded due to
  insufficient coverage, leaving 41 samples.

## DNA Extraction

DNA was isolated from 0.25 g of soil or root per extraction using the
PowerSoil [[power-soil-dna-isolation-16s-microbiome]] Kit (MO BIO, USA). A modification was applied:
heating the extraction at 65 degrees Celsius for 10 minutes prior to the
initial vortex step. Root samples were rinsed with alcohol and sterile water
before extraction to remove surface contaminants and isolate true endorhiza
bacteria from rhizoplane adherents.

## PCR Amplification of the V4 Region

The 291 bp V4 region of the 16S rRNA gene was amplified using primers from
Caporaso et al. (2012), following the Earth Microbiome Project standard
pipeline:

- **Forward primer**: 515F
- **Reverse primer**: 806R with Golay barcodes for sample multiplexing

Each 25 microliter PCR reaction contained:
- 12 microliters MO BIO PCR Water (Certified DNA-Free)
- 10 microliters 5 Prime HotMasterMix (1x)
- 1 microliter Forward Primer (5 mM concentration, 200 pM final)
- 1 microliter Golay Barcode Tagged Reverse Primer (5 mM, 200 pM final)
- 1 microliter template DNA

### Thermal Cycling Conditions

- Initial denaturation: 94 degrees C for 3 minutes
- 35 cycles of: 94 degrees C for 45 s, 50 degrees C for 60 s, 72 degrees C
  for 90 s
- Final extension: 72 degrees C for 10 minutes

PCR was completed in triplicate and products were pooled to reduce
amplification bias.

## Library Preparation and Sequencing

Pooled PCR products were quantified using Invitrogen PicoGreen with a plate
reader. Equal amounts (ng) of DNA from each sample were pooled into a single
tube and cleaned using the UltraClean PCR Clean-Up Kit (MO BIO). The pooled
library was diluted to 2 nM, denatured, and diluted to a final concentration
of 6.1 pM with a 30% PhiX spike for sequencing quality control.

Sequencing was performed on the Illumina MiSeq platform using a 151 bp x 12
bp x 151 bp configuration with custom sequencing primers described in
Caporaso et al. (2012). All raw sequence data was deposited publicly on
Figshare.

## QIIME Bioinformatics Pipeline

All sequence analysis was performed using QIIME 1.7.0 with the following
workflow:

1. **Quality filtering**: QIIME defaults applied to raw Illumina reads
2. **OTU picking**: Two methods employed:
   - Experiment 1: Open reference OTU picking against Greengenes database
     pre-clustered at 97% identity, with de novo clustering of unmatched

## Practical Applications
16S Rrna Sequencing Microbiome Analysis has significant applications in sustainable agriculture, ecological design, and regenerative practices. Practitioners and researchers continue to explore innovative methods for implementing these concepts in diverse climates and scales of operation.

## Historical Significance
The development and understanding of 16s rrna sequencing microbiome analysis has evolved considerably over recent decades, with contributions from researchers, practitioners, and indigenous knowledge systems worldwide.

## See Also
- [[16s-rrna-sequencing-microbiome-analysis-cannabis]]
- [[16s-rrna-sequencing-cannabis-microbiome-profiling]]
- [[rhizosphere-fungal-community-analysis-rrna-rdna]]
- [[cannabis-microbiome-unifrac-beta-diversity-analysis]]
- [[unifrac-weighted-unweighted-analysis-cannabis-microbiome]]
