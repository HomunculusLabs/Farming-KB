---
title: 16S 16s rrna sequencing microbiome analysis for Microbiome Analysis
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
sequenced across two experiments, analyzed using the QIIME bioinformatics
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
PowerSoil DNA Isolation Kit (MO BIO, USA). A modification was applied:
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
     sequences
   - Experiment 2: Both closed and open reference OTU picking methods
3. **Alignment**: Representative sequences aligned to the Greengenes core
   set using PyNAST; unaligned sequences discarded
4. **Phylogenetic tree**: Built from the alignment using FastTree
5. **Taxonomy assignment**: RDP classifier retrained on Greengenes

## Rarefaction

Samples were rarified to even sequencing depths before diversity analysis:

- **Experiment 1**: Rarefied to 3,000 sequences per sample
- **Experiment 2**: Rarefied to 45,000 sequences per sample

The large difference in rarefaction depth reflects different sequencing runs
and necessitates caution when comparing [[microbial-alpha-diversity-soil-plant-gradient]] between experiments.

## Diversity Metrics and Statistical Analysis

Alpha and beta-diversity metrics were computed using QIIME:

- **[[alpha-beta-diversity-cannabis-root-microbiomes]]**: Weighted and [[weighted-vs-unweighted-unifrac-cannabis-strain-microbiome]] distances calculated
  from pairwise sample comparisons
- **Visualization**: PCoA (principal coordinate analysis) and RDA (redundancy
  analysis) plots
- **Significance testing**: ANOSIM, ADONIS, ANOVA, Mantel tests, and BEST
  analysis using QIIME scripts (compare_categories.py and
  compare_distance_matrices.py)
- **OTU-level analysis**: G-test (unweighted) and ANOVA (weighted) with FDR
  multiple test correction

## UniFrac Analysis

UniFrac distances measure the phylogenetic distance between microbial
communities. Two versions were used:

- **Unweighted UniFrac**: Based on OTU presence/absence, reflecting community
  composition (which taxa are present)
- **Weighted UniFrac**: Accounts for [[cannabis-microbiome-otu-abundance-vs-presence-cannabis-strains]], reflecting community
  structure (which taxa are present and how abundant they are)

The complementary use of both metrics allowed the authors to distinguish
between effects on composition versus abundance, revealing that soil type
drives composition while cultivar drives abundance patterns.

## See Also

- [[16s-rrna-sequencing-microbiome-analysis-cannabis]]
- [[edaphic-factor-ranking-nitrogen-salinity-carbon-cannabis-microbiome]]
- [[soil-type-otu-abundance-vs-strain-structure-cannabis-microbiome]]

- [[microbial-alpha-diversity-soil-plant-gradient]] for diversity findings
- [[cannabis-microbiome-research]] for the complete study overview
