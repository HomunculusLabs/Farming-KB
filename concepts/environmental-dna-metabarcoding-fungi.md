---
title: Environmental DNA Metabarcoding for arbuscular-mycorrhizal-fungal-diversity-patterns-distribution
created: 2026-04-28
tags: [mycology, metagenomics, methodology, dna sequencing]
date: 2026-04-28
updated: 2026-04-28
sources: [/Users/t3rpz/wiki/raw/papers/unknown-biodiversity-of-fungi.md]
type: concept
---

# Environmental DNA Metabarcoding for Fungal Diversity

Environmental DNA (eDNA) metabarcoding has revolutionized the study of fungal
biodiversity. By extracting and sequencing DNA directly from environmental
samples, researchers can detect fungal species without observing fruiting bodies
or culturing organisms in the laboratory. This approach has revealed that
previously known fungal diversity represents only a small fraction of the total.

## How Metabarcoding Works

The standard fungal metabarcoding workflow begins with collecting an environmental
sample and extracting total genomic DNA. A specific region of fungal DNA, most
commonly the Internal Transcribed Spacer (ITS) region of ribosomal RNA genes,
is then amplified using universal fungal primers. The ITS region sits between
the 18S, 5.8S, and 28S ribosomal subunits and exhibits high sequence variability,
making it ideal for distinguishing among fungal species.

The resulting amplicons are sequenced on high-throughput platforms, typically
Illumina MiSeq or HiSeq, generating millions of reads per sample. Bioinformatic
pipelines then cluster reads into operational taxonomic units (OTUs) or resolve
exact amplicon sequence variants (ASVs). These sequences are compared against
reference databases such as UNITE or GenBank to assign taxonomic identities.

## The ITS Region as a Fungal Barcode

The fungal barcoding community has converged on the ITS region as the primary
barcode locus for fungi. ITS2, the second spacer, is generally preferred for
taxonomic assignment because it is shorter and more variable. ITS1 is also
widely used and may perform better for certain groups.

Neither ITS1 nor ITS2 is perfect. Sequence alignment across broad taxonomic
groups is difficult because of length variation and indels. Some fungal genera
show very low ITS variability, making species-level discrimination impossible.
Many sequences in reference databases are themselves misidentified or
insufficiently annotated, leading to propagating errors in taxonomic assignment.

## Metabarcoding vs Traditional Identification

Traditional [[pcr-methods-fungal-identification-monitoring]] relies on observing and culturing fruiting
bodies, a process that is labor-intensive, seasonally limited, and biased toward
conspicuous macrofungi. Many fungi never produce visible structures under
laboratory conditions, making them invisible to traditional methods.
Metabarcoding bypasses these limitations by detecting DNA from all life stages,
including dormant spores and microscopic mycelia.

However, metabarcoding cannot distinguish between viable and dead organisms.
DNA from dead hyphae, dormant spores, and extracellular material can persist
for weeks to years, producing ghost signals that do not reflect active community
composition. Culture-based methods remain essential for linking DNA sequences
to [[savory-living-organisms-as-tools]] and for studying fungal physiology and ecology.

## Primer Selection for Fungal Surveys

Primer selection strongly influences which taxa are recovered. No primer pair
amplifies all fungal groups equally. The ITS1F/ITS2 primer pair is widely used
but underrepresents Basidiomycota. The gITS7/ITS4 pair offers better coverage
of Basidiomycota but may miss some early-diverging lineages. Researchers must
choose primers based on their target groups and study objectives.

Primer bias is compounded by PCR stochasticity. At low template concentrations,
which are common in oligotrophic environments, PCR may amplify some templates
preferentially over others. Using multiple primer pairs in parallel can partially
mitigate this bias and provide a more complete picture of [[core-endorhiza-bacterial-community-composition-cannabis]].

## Bioinformatics Pipeline

A typical fungal metabarcoding bioinformatics pipeline involves several steps.
Raw sequencing reads are quality-filtered to remove low-quality bases and
adapter sequences. Forward and reverse reads are merged, and chimeric sequences
are removed using tools like DADA2, UNOISE, or VSEARCH.

Processed sequences are then clustered into OTUs at 97% similarity or resolved
as exact amplicon sequence variants (ASVs). ASV methods generally recover more
rare taxa and provide finer resolution, but may also include more sequencing
artifacts if filtering is not stringent enough. Taxonomic assignment against
reference databases like UNITE completes the pipeline.

## Applications in Fungal Ecology

Metabarcoding has transformed our understanding of [[air-pollution-fungal-community-responses]] ecology.
It enables large-scale studies of how [[biodiversity-of-fungi-soil-fungal-communities-agriculture]] respond to
environmental gradients, land-use change, and climate shifts. Soil metabarcoding
surveys have revealed that a single gram of forest soil may contain hundreds
of fungal species, the vast majority of which have never been cultured.

In applied contexts, metabarcoding is used for indoor air quality assessment,
agricultural soil health monitoring, and detection of plant pathogens. Clinical
metabarcoding can identify fungal pathogens directly from patient samples,
reducing diagnosis time compared to traditional culture methods.

## Limitations and Biases

Sequencing depth determines the detection threshold for rare taxa.
Undersampling means that rare species, which may constitute the majority of
diversity, are missed or detected inconsistently. The relationship between read
abundance and biological abundance is complex and nonlinear, making quantitative
inferences from metabarcoding data unreliable.

Complementary approaches like metatranscriptomics and shotgun metagenomics
provide additional information about active community members and functional
potential, but at much higher cost and with greater computational demands.

## See Also

- [[gadd-environmental-sensing-filamentous-fungi]]

- [[fungal-habitats-and-niches]]
- [[bloomfield-mycorrhizal-symbiosis-and-fungal-ecology]]
- [[fungal-conservation-challenges]]
