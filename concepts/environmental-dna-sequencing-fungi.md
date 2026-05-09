---
title: Environmental environmental dna sequencing fungi for Fungi
created: 2026-04-28
tags: mycology, metagenomics, sequencing, methodology]
date: 2026-04-28
updated: 2026-04-28
sources: [/Users/t3rpz/wiki/raw/papers/unknown-biodiversity-of-fungi.md]
type: concept
---

# Environmental DNA Sequencing for Fungi

Environmental DNA (eDNA) sequencing refers to the extraction and high-throughput
sequencing of fungal DNA directly from environmental samples — soil, water,
air, sediment, or host tissue — without isolating or culturing the organisms.
This approach has transformed [[biodiversity-fungal-biodiversity-estimation-methods]] studies by revealing the vast
majority of [[arbuscular-mycorrhizal-fungal-diversity-patterns-distribution]] that is invisible to traditional methods.

## The ITS Barcode Region

The Internal Transcribed Spacer (ITS) region of ribosomal RNA genes was adopted
as the official fungal DNA barcode in 2012. ITS sits between the 18S and 28S
rRNA genes and evolves rapidly enough to discriminate among closely related
species. The ITS1 and ITS2 subregions are both used, with ITS2 generally
preferred for its more consistent amplification and alignment properties.

Limitations of ITS barcoding include: inability to resolve species in some
groups (e.g., Fusarium, Penicillium), presence of intragenomic variation
(multiple ITS copies within a single genome), and primer bias that
preferentially amplifies some taxa over others.

## Workflow

A typical fungal eDNA sequencing pipeline follows these steps:

1. **Sample collection** — [[psilocybin-mushroom-field-collection-techniques]] of substrate (soil cores, leaf
   litter, water filters). Metadata recording is critical: GPS, depth,
   temperature, pH, vegetation, date.
2. **DNA extraction** — commercial kits (e.g., MoBio PowerSoil) or CTAB-based
   methods. Mechanical lysis (bead-beating) is essential for breaking tough
   fungal cell walls.
3. **PCR amplification** — fungal-specific primers (e.g., ITS1F/ITS2,
   fITS7/ITS4) target the ITS region. Negative controls detect
   contamination.
4. **Library preparation** — indexing and adapter ligation for multiplexed
   sequencing on Illumina, Ion Torrent, or Nanopore platforms.
5. **Sequencing** — Illumina MiSeq 2x300 bp reads are the current standard,
   providing sufficient overlap for full ITS coverage.
6. **Bioinformatics** — quality filtering, chimera removal, OTU clustering or
   ASV (amplicon sequence variant) denoising, taxonomic assignment against
   reference databases (UNITE, GenBank).

## Amplicon vs. Shotgun Metagenomics

Two main strategies exist. Amplicon sequencing targets a specific marker gene
(ITS) and is cost-effective for community profiling. Shotgun metagenomics
sequences all DNA in a sample, providing functional gene information and
reducing primer bias, but at higher cost and with more complex analysis.

For fungal biodiversity surveys, amplicon sequencing remains the dominant
approach due to its depth of coverage per sample and well-established analysis
pipelines (QIIME2, DADA2, UNOISE).

## Reference Database Challenges

Taxonomic assignment depends entirely on reference database quality. The UNITE
database is the primary resource for fungal ITS sequences, with expert-curated
species hypotheses. However, coverage is uneven: well-studied groups in
temperate regions are well-represented, while tropical and [[guzman-allen-gartz-africa-southern-hemisphere-underexplored-neurotropic-fungi]]
fungi, microfungi, and basal lineages are significantly underrepresented.

This creates a circular problem: dark taxa cannot be described without
cultures, but cultures are not prioritized for taxa only known from
environmental sequences that have no reference match.

## Primer Bias and False Negatives

No primer pair is truly universal. Different primer sets capture different
subsets of fungal diversity. Studies using multiple primer sets on the same
samples consistently find that each captures unique taxa missed by the others.
This means that even comprehensive metabarcoding surveys underestimate total
fungal diversity.

## Emerging Technologies

Long-read sequencing (Oxford Nanopore, PacBio HiFi) enables full-length ITS
sequencing without assembly, improving taxonomic resolution. Metatranscriptomics
captures actively expressed fungal genes, providing insight into which fungi are
[[isolation-metabolically-active-arbuscules-intraradical-hyphae]] rather than merely present. CRISPR-based enrichment methods
(e.g., HoloSeq) may allow targeted capture of fungal DNA from complex
environmental mixtures.

## Standardization Challenges

Comparability across studies remains a significant challenge. Different labs use
different primer pairs, sequencing platforms, bioinformatic pipelines, and
reference databases, making it difficult to combine datasets for global analyses.
The SPUN (Society for the Protection of Underground Networks) and other
initiatives are working toward standardized protocols for fungal eDNA surveys,
including recommended primer sets, quality thresholds, and data reporting
standards.

## From eDNA to Function

A growing frontier is linking eDNA detections to functional predictions. By
matching environmental sequences to genomes in reference databases, researchers
can infer the metabolic capabilities of detected fungi — whether they are
lignin degraders, nitrogen cyclers, plant pathogens, or [[fungal-biodiversity]]
- [[fungal-cryptic-species]]

## See Also

- [[singh-fungi-environmental-indicators]]
