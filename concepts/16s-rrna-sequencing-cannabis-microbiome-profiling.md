---
title: 16S rRNA Sequencing for Cannabis Microbiome Profiling
created: 2026-05-11
source: understanding-cultivar-specificity-cannabis-microbiome.md
tags: [16s-rrna, microbiome, sequencing, cannabis, illumina, bioinformatics, qiime]
aliases: [Cannabis 16S Sequencing, Microbiome Profiling Methods Cannabis]
---

# 16S rRNA Sequencing for Cannabis Microbiome Profiling

The characterization of Cannabis-associated [[cannabis-rhizosphere-microbial-communities]] relies heavily on
amplicon sequencing of the 16S ribosomal RNA gene. The 2014 Winston et al. study
established the methodological foundation for [[cannabis-microbiome-research]] using
Illumina MiSeq sequencing of the V4 hypervariable region, following the Earth
Microbiome Project's standardized protocols.

## The 16S rRNA Gene as a Molecular Marker

The 16S rRNA gene is present in all [[teaming-with-microbes-bacteria-and-archaea-in-soil]], containing both
conserved regions (suitable for universal primer binding) and nine hypervariable
regions (V1–V9) that provide species-level discriminatory power. For Cannabis
microbiome studies, the V4 region has become the standard target for several
reasons:

- **Universal coverage** — the 515F/806R primer pair amplifies across the vast
  majority of bacterial phyla with minimal bias
- **Appropriate length** — the ~291 bp amplicon is ideal for paired-end Illumina
  sequencing (151 bp × 2 with overlap)
- **Established databases** — extensive reference libraries (Greengenes, SILVA)
  exist for V4 sequences
- **Community standards** — the Earth Microbiome Project validated V4 for soil
  and plant microbiome surveys

## Laboratory Protocol

### DNA Extraction

Root and soil DNA was extracted from 0.25 g samples using the PowerSoil DNA
Isolation Kit (MO BIO Laboratories, now Qiagen DNeasy PowerSoil) with a critical
modification: heating the extraction at 65°C for 10 minutes prior to the initial
vortex step. This pre-heating step improves cell lysis, particularly for
Gram-positive bacteria and fungi with robust cell walls that are common in soil
and root environments.

Sample types required different preparation:
- **Bulk soil**: 50 g collected 10 cm from stem at 20 cm depth, stored at 4°C
- **Rhizosphere soil**: soil adhering to roots after gentle shaking into whirlpak
  bags
- **Endorhiza**: root tissue rinsed with alcohol and sterile water to remove
  epiphytic bacteria before extraction

### PCR Amplification

Each 25 µL PCR reaction contained:
- 12 µL MO BIO PCR Water (DNA-free)
- 10 µL 5 Prime HotMasterMix (1×)
- 1 µL Forward Primer 515F (5 mM, 200 pM final)
- 1 µL Golay Barcode-Tagged Reverse Primer 806R (5 mM, 200 pM final)
- 1 µL template DNA

Thermal cycling conditions:
1. Initial denaturation: 94°C for 3 minutes
2. 35 cycles of: 94°C for 45 s, 50°C for 60 s, 72°C for 90 s
3. Final extension: 72°C for 10 minutes

PCR was performed in triplicate and products were pooled per sample to reduce
stochastic amplification bias.

### Library Preparation and Sequencing

Pooled PCR products were quantified using PicoGreen fluorescence with a plate
reader, then pooled at equal DNA amounts (ng). The pooled library was cleaned
using the UltraClean PCR Clean-Up Kit, quantified to determine molarity, diluted
to 2 nM, denatured, and diluted to a final concentration of 6.1 pM with a 30%
PhiX spike. Sequencing was performed on the Illumina MiSeq platform with a
151 bp × 151 bp × 151 bp run using custom sequencing primers.

The PhiX control spike provides diversity to the low-complexity amplicon pool,
enables error rate monitoring, and improves base calling quality.

## Bioinformatic Pipeline

### QIIME 1.7.0 Workflow

All sequence analysis was performed using QIIME (Quantitative Insights Into
Microbial Ecology) version 1.7.0:

1. **Quality filtering** — default QIIME parameters
2. **OTU picking** — open reference against Greengenes (97% identity), de novo
   clustering of unmatched sequences
3. **Alignment** — PyNAST alignment to Greengenes core set; unaligned discarded
4. **Phylogenetic tree** — constructed using FastTree
5. **Taxonomy** — RDP classifier retrained on Greengenes
6. **Rarefaction** — Exp. 1: 3,000 seqs/sample; Exp. 2: 45,000 seqs/sample

### Alpha and Beta Diversity Metrics

**Alpha diversity** (within-sample) metrics included observed OTUs, Chao1,
Shannon index, and Faith's phylogenetic diversity. These measure richness,
evenness, and evolutionary breadth of each community.

**Beta diversity** (between-sample) was calculated using:
- **[[weighted-unifrac-strain-clustering-cannabis-endorhiza-community-structure]]** — phylogenetic + abundance; sensitive to dominant taxa
- **weighted unweighted unifrac discrepancy cannabis cultivar** — phylogenetic + presence/absence; sensitive to rare taxa

### Statistical Analyses

- **ADONIS (PERMANOVA)** — partitions variance in community composition by
  categorical factors (soil type, cultivar, sample compartment)
- **ANOSIM** — non-parametric test of group differences
- **ANOVA** — comparison of alpha diversity between groups
- **BEST analysis** — identifies which environmental variables best explain
  community dissimilarities (vegan::bioenv in R)
- **RDA** — redundancy analysis for community-environment relationships
- **Mantel test** — correlation between community and environmental distance matrices

## Sample Size and Rarefaction Depth

The study analyzed 69 total samples. Four were discarded from Experiment 1 and
one from Experiment 2 due to insufficient coverage. This highlights the
importance of adequate sequencing depth for soil and root samples, which often
contain high amounts of plant chloroplast and mitochondrial DNA that compete with
bacterial templates.

The dramatic difference in rarefaction depth between experiments (3,000 vs.
45,000) reflects advances in MiSeq throughput and enables deeper community
characterization.

## Considerations for Cannabis Samples

1. **PCR inhibitors** — polyphenols, polysaccharides, [[plant-defense-chemistry-and-secondary-metabolites]]
   can inhibit PCR; the PowerSoil kit includes inhibitor removal steps.
2. **Plant organelle sequences** — chloroplast 16S and mitochondrial 12S can
   dominate amplicon pools; the 515F/806R pair has relatively low plant
   organelle amplification.
3. **Regulatory constraints** — legal restrictions have historically limited
   sample sizes and replication in Cannabis microbiome research.

## See Also

- cannabis rhizosphere microbiome zonation — community structure findings
- cannabis cultivar specificity endorhiza microbiome — cultivar effects
- [[16s-rrna-sequencing-microbiome-analysis]] — general 16S methodology
- [[qiime-bioinformatics-pipeline-16s-rrna-microbiome]] — QIIME workflow details
