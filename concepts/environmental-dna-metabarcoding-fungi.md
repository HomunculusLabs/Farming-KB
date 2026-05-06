---
title: Environmental DNA Metabarcoding for Fungal Diversity
created: 2026-04-28
tags: [mycology, metagenomics, methodology, dna-sequencing]
date: 2026-04-28
updated: 2026-04-28
sources: [/Users/t3rpz/wiki/raw/papers/unknown-biodiversity-of-fungi.md]
type: concept
---

# Environmental DNA Metabarcoding for Fungal Diversity

Environmental DNA (eDNA) metabarcoding has revolutionized the study of fungal
biodiversity. By extracting and sequencing DNA directly from environmental
samples — soil, water, air, or tissue — researchers can detect fungal species
without the need to observe fruiting bodies or culture organisms in the
laboratory. This approach has revealed that previously known fungal diversity
represents only a small fraction of the total.

## How Metabarcoding Works

The standard fungal metabarcoding workflow begins with collecting an
environmental sample and extracting total genomic DNA. A specific region of
fungal DNA — most commonly the Internal Transcribed Spacer (ITS) region of
ribosomal RNA genes — is then amplified using universal fungal primers. The
ITS region sits between the 18S, 5.8S, and 28S ribosomal subunits and
exhibits high sequence variability, making it ideal for distinguishing among
fungal species.

The resulting amplicons are sequenced on high-throughput platforms
(typically Illumina MiSeq or HiSeq), generating millions of reads per
sample. Bioinformatic pipelines then cluster reads into operational taxonomic
units (OTUs) or, more commonly now, resolve exact amplicon sequence variants
(ASVs). These sequences are compared against reference databases such as
UNITE or GenBank to assign taxonomic identities.

## The ITS Region as a Fungal Barcode

The fungal barcoding community has converged on the ITS region as the primary
barcode locus for fungi. ITS2, the second spacer, is generally preferred for
taxonomic assignment because it is shorter and more variable. ITS1 is also
widely used and may perform better for certain groups.

Neither ITS1 nor ITS2 is perfect. Sequence alignment across broad taxonomic
groups is difficult because of length variation and indels. Some fungal
genera show very low ITS variability, making species-level discrimination
impossible. Additionally, many sequences in reference databases are
themselves misidentified or insufficiently annotated, leading to propagating
errors in taxonomic assignment.

## Limitations and Biases

Metabarcoding is subject to several well-documented biases. Primer selection
strongly influences which taxa are recovered; no primer pair amplifies all
fungal groups equally. Some major fungal lineages are systematically
underrepresented by commonly used ITS primers. PCR also favors shorter
amplicons and templates in better condition, biasing against degraded or
longer ITS fragments.

Sequencing depth determines the detection threshold for rare taxa.
Undersampling means that rare species — which may constitute the majority of
diversity — are missed or detected inconsistently. The relationship between
read abundance and biological abundance or biomass is complex and nonlinear,
making quantitative inferences from metabarcoding data unreliable.

Perhaps most fundamentally, metabarcoding detects DNA, not organisms. DNA
from dead hyphae, dormant spores, and extracellular material can persist in
the environment for weeks to years, producing "ghost signals" that do not
reflect active community composition.

## Complementary Molecular Approaches

Metatranscriptomics — sequencing of community RNA — can distinguish active
from dormant taxa by capturing only transcribed genes. Metagenomics
(shotgun sequencing of total DNA) avoids primer bias entirely and provides
additional functional information, though at much higher cost and with
greater computational demands. Both approaches are increasingly used alongside
metabarcoding to build a more complete picture of fungal communities.

## Laboratory Workflow

A typical fungal metabarcoding workflow begins with environmental sample
collection (soil cores, leaf litter, root samples, or air filters), followed
by DNA extraction using commercial kits optimized for challenging matrices
like humic-rich soils. The ITS2 region is then amplified with fungal-specific
primers (typically ITS3/ITS4), fused with sequencing adapters and sample
barcodes in a two-step PCR process. After purification and quantification,
amplicons are pooled in equimolar ratios and sequenced on Illumina MiSeq
or HiSeq platforms, generating 10,000-100,000 reads per sample.

Bioinformatic processing involves quality filtering (removing low-quality
reads and chimeras), clustering into operational taxonomic units (OTUs) at
97% similarity or generating amplicon sequence variants (ASVs) using DADA2
or UNOISE, and taxonomic assignment against reference databases such as
UNITE or GenBank. The choice between OTU clustering and ASV methods
significantly affects diversity estimates — ASV methods generally recover
more rare taxa and provide finer resolution, but may also include more
sequencing artifacts if filtering is not stringent enough.
## See Also

- [[fungal-biodiversity-estimates]]
- [[fungal-habitats-and-niches]]
- [[cryptic-fungal-species]]
- [[bloomfield-mycorrhizal-symbiosis-and-fungal-ecology]]
- [[fungal-conservation-challenges]]
