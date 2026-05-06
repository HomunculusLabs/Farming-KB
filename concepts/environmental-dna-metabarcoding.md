---
title: Environmental DNA Metabarcoding
created: 2026-04-28
tags: [genomics, mycology, ecology, biodiversity]
date: 2026-04-28
updated: 2026-04-28
sources: [/Users/t3rpz/wiki/raw/papers/unknown-biodiversity-of-fungi.md]
type: concept
---

# Environmental DNA Metabarcoding

## Overview

Environmental DNA (eDNA) metabarcoding is a molecular approach that identifies
organisms from DNA extracted directly from environmental samples such as soil,
water, air, or bulk tissue. For fungal biodiversity, eDNA metabarcoding has
revolutionized diversity estimates by revealing vast numbers of taxa invisible
to traditional morphology-based surveys. The technique has become the standard
tool for large-scale fungal biodiversity assessment, enabling surveys that would
be prohibitively expensive or impossible using traditional culturing and
microscopy.

## How It Works

### Sample Collection

Soil cores, leaf litter, water filters, or air samplers capture total
environmental DNA. For fungi, soil samples of approximately 0.25 grams are
typical, though larger samples increase detection of rare taxa. Sample
preservation methods (freezing, ethanol storage, or commercial preservation
buffers) affect downstream DNA quality and community representation. Spatial
sampling design -- number of samples, spacing, and composite versus individual
sampling -- critically influences diversity estimates.

### DNA Extraction and Amplification

Total genomic DNA is extracted from the sample using commercial kits optimized
for environmental matrices that contain inhibitors like humic acids. Specific
marker regions are then PCR-amplified using universal primers. For fungi, the
internal transcribed spacer (ITS) region of ribosomal DNA is the standard
barcode, designated as the official fungal barcode by the International Society
for Human and Animal Mycology (ISHAM) in 2012. ITS1 and ITS2 subregions are
commonly used, each with different taxonomic resolution and primer
specificities. The choice of primer pair and PCR conditions significantly
affects which taxa are detected.

### Sequencing

Amplified fragments are sequenced using high-throughput platforms, typically
Illumina MiSeq (2x300 bp reads) which produces millions of reads per sample.
These reads are then clustered into operational taxonomic units (OTUs) using
97% similarity thresholds, or more recently, resolved into amplicon sequence
variants (ASVs) using single-nucleotide resolution methods. ASVs offer several
advantages over OTUs: they are more reproducible, comparable across studies,
and avoid the arbitrary clustering threshold problem.

### Bioinformatic Processing

Standard pipelines such as QIIME2, DADA2, mothur, and UNOISE process raw
sequences through quality filtering (removing low-quality reads and chimeras),
sequence inference (ASV or OTU clustering), and taxonomic assignment using
reference databases. The UNITE database for fungi and the SILVA database for
general eukaryotes are the primary reference resources. Taxonomic assignment
confidence varies widely, from kingdom-level certainty to species-level
uncertainty for most environmental sequences.

## Impact on Fungal Diversity Estimates

eDNA metabarcoding has consistently revealed 5-10x more fungal taxa in samples
than traditional culturing or fruiting body surveys detect. A single soil
sample from a tropical forest may yield 500-1,000 fungal ASVs, most of which
cannot be assigned to described species. Global-scale studies using eDNA have
sampled thousands of sites across all continents, revealing biogeographic
patterns that were invisible to traditional methods. These findings have driven
upward revisions of global fungal species estimates from Hawksworth's 1.5
million to 2.2-3.8 million or higher.

## Limitations and Biases

### Primer Bias

No primer pair perfectly amplifies all fungal taxa. Primer mismatches
systematically exclude certain groups -- the commonly used ITS1F primer, for
example, poorly matches many basidiomycete genera. This makes diversity
estimates method-dependent rather than absolute, and comparisons across studies
using different primer pairs require careful standardization.

### DNA Persistence

Extracellular DNA can persist in soil for weeks to months, and in some
environments for years. This creates "ghost signals" from dead organisms that
inflate diversity estimates beyond the active, living community. Propidium
monoazide (PMA) treatment can distinguish living from dead cells, but adds
complexity and cost to the workflow.

### Reference Database Gaps

Most environmental sequences cannot be confidently assigned to known species
because reference databases cover only a fraction of described taxa and an even
smaller fraction of total fungal diversity. UNITE, the primary fungal reference
database, contains approximately 1 million fungal sequences, but an estimated
80%+ of fungal diversity remains unrepresented. This "dark taxa" problem means
that most diversity detected by eDNA surveys remains taxonomically
unresolved.

### Quantification Challenges

PCR amplification is not quantitative. Read abundance does not reliably reflect
organism abundance due to variable ribosomal gene copy numbers (ranging from
tens to hundreds of copies per genome), differential primer binding efficiency,
and PCR stochasticity. While metabarcoding provides excellent presence-absence
data, quantitative interpretation requires additional approaches like qPCR or
quantitative metatranscriptomics.

## Emerging Approaches

### Metatranscriptomics

Sequencing expressed RNA from environmental samples captures only actively
transcribing organisms, filtering out DNA from dormant, dead, or extracellular
sources. This provides a more dynamic view of functional community composition
but is more expensive and technically challenging due to rapid RNA degradation.

### Shotgun Metagenomics

Whole-genome shotgun sequencing of environmental DNA avoids primer bias entirely
and captures information about all organisms and functional genes present.
Computational requirements are much higher, but the approach enables detection
of non-fungal organisms and functional pathway analysis without relying on
marker genes.

### Long-Read Sequencing

PacBio HiFi and Oxford Nanopore platforms enable full-length ITS sequencing,
spanning both ITS1 and ITS2 plus portions of the flanking 18S and 28S genes.
This dramatically improves taxonomic resolution compared to short-read
approaches and allows phylogenetic placement of environmental sequences that
cannot be assigned to species-level taxa using reference databases alone.

## See Also

- [[environmental-dna-fungal-survey]]

- [[fungal-species-estimates]]
- [[biodiversity-fungi-soil-fungal-communities]]
- [[fungal-species-estimates]]
- [[fungal-endophytes]]
- [[fungal-ecology]]
