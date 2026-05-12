---
title: Environmental environmental-dna-metabarcoding-fungi
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
water, air, or bulk tissue. For [[biodiversity-fungal-biodiversity-estimation-methods]], eDNA metabarcoding has
revolutionized [[fungal-diversity-estimates]] by revealing vast numbers of taxa invisible
to traditional morphology-based surveys. The technique has become the standard
tool for large-scale fungal [[fungal-biodiversity-assessment-methods]], enabling surveys that would
be prohibitively expensive or impossible using traditional culturing and
microscopy.

## How It Works

### Sample Collection

Soil cores, [[dighton-fungal-decomposition-leaf-litter-dynamics]], water filters, or air samplers capture total
environmental DNA. For fungi, soil samples of approximately 0.25 grams are
typical, though larger samples increase detection of rare taxa. Sample
[[egg-preservation-methods]] (freezing, ethanol storage, or commercial preservation
buffers) affect downstream DNA quality and community representation. Spatial
[[macrofungal-sampling-design-plots-transects]] -- number of samples, spacing, and composite versus individual
sampling -- critically influences diversity estimates.

### DNA Extraction and Amplification

Total genomic DNA is extracted from the sample using commercial kits optimized
for environmental matrices that contain inhibitors like [[humic-acids-soil-biology-ingham]]. Specific
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
than traditional culturing or [[bloomfield-mushroom-formation-fruiting-body-development-cultivation]] surveys detect. A single soil
sample from a [[arbuscular-mycorrhizal-fungi-in-tropical-forest-restoration]] may yield 500-1,000 fungal ASVs, most of which
cannot be assigned to described species. Global-scale studies using eDNA have
sampled thousands of sites across all continents, revealing biogeographic
patterns that were invisible to traditional methods. These findings have driven
upward revisions of global [[fungal-species-estimates]] from Hawksworth's 1.5
million to 2.2-3.8 million or higher.

## Limitations and Biases

### Primer Bias

No primer pair perfectly amplifies all fungal taxa. Primer mismatches
systematically exclude certain groups -- the commonly used ITS1F primer, for
example, poorly matches many basidiomycete genera. This makes diversity
estimates method-dependent rather than absolute, and comparisons across studies
using different primer pairs require careful standardization.

### DNA Persistence

## Practical Applications

The principles and techniques discussed here have wide-ranging applications
across multiple disciplines and contexts. Practitioners and researchers
continue to explore new ways to integrate these concepts into modern practice,
adapting traditional knowledge to contemporary challenges and opportunities.

## Key Considerations

Several important factors influence the effectiveness and outcomes described
in this topic. Understanding these considerations helps practitioners make
informed decisions and avoid common pitfalls. Environmental conditions,
timing, and material selection all play critical roles.

## Historical Context

The historical development of this subject reflects centuries of accumulated
knowledge and practical experience. From traditional methods passed down
through generations to modern scientific approaches, the evolution continues
to inform current best practices and research directions.

## Common Challenges

Practitioners frequently encounter several challenges when working with
these concepts. Climate variability, resource limitations, and knowledge
gaps can all affect outcomes. Addressing these challenges requires patience,
observation, and a willingness to adapt approaches based on results.

## See Also
- [[dom]]
- [[det]]
- [[soma]]
- [[fungal-diversity-estimates]]
- [[ethanol]]
