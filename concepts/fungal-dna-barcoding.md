---
title: Fungal DNA Barcoding
created: 2026-04-12
updated: 2026-04-12
type: concept
tags: [fungi, mycology, genomics, lab-technique, taxonomy, species, biology, ecology, methods]
sources: []
---

# Fungal DNA Barcoding

## Overview

Fungal DNA barcoding uses standardized DNA regions to rapidly identify fungal species from small tissue samples. It has revolutionized [[molecular-methods-fungal-taxonomy-and-diversity]], ecology, and monitoring, enabling identification of fungi that are difficult or impossible to distinguish by morphology alone. The technique is essential for environmental DNA (eDNA) studies, biosecurity, and citizen science.

## The ITS Region

### Why ITS?

The Internal Transcribed Spacer (ITS) region is the official fungal DNA barcode, adopted by the mycological community in 2012. The ITS sits between the 18S, 5.8S, and 28S ribosomal RNA genes in the nuclear ribosomal operon.

Structure: 18S -- ITS1 -- 5.8S -- ITS2 -- 28S

The ITS region is ideal for barcoding because:
1. **High copy number**: Ribosomal DNA exists in multiple copies per genome (50-200+), making it easy to amplify even from small or degraded samples
2. **High variability**: ITS1 and ITS2 evolve quickly, providing species-level discrimination
3. **Conserved flanking regions**: The 18S and 28S regions are conserved, allowing universal primer binding
4. **Comprehensive databases**: More fungal ITS sequences exist than for any other locus

### Limitations

- Cannot reliably distinguish between very closely related species in some groups
- Intra-strain variation (multiple ITS copies within one genome can differ)
- Does not work well for some early-diverging fungal lineages
- Cannot distinguish living from dead organisms in eDNA samples

## PCR Amplification

### Primer Sets

The most commonly used primers for fungal ITS amplification:

- **ITS1 / ITS4**: Classic primer pair that amplifies the full ITS region (~600-700 bp)
  - ITS1: 5'-TCCGTAGGTGAACCTGCGG-3'
  - ITS4: 5'-TCCTCCGCTTATTGATATGC-3'

- **ITS1F / ITS4**: Modified forward primer that is more fungal-specific (excludes plants)
  - ITS1F: 5'-CTTGGTCATTTAGAGGAAGTAA-3'

- **ITS3 / ITS4**: Amplifies only the ITS2 region (~300-400 bp), useful for degraded samples or Illumina sequencing
  - ITS3: 5'-GCATCGATGAAGAACGCAGC-3'

- **fITS7 / ITS4**: Another ITS2-specific pair widely used in metabarcoding studies

### PCR Protocol (Standard)

1. DNA extraction: CTAB method, commercial kits, or Chelex extraction
2. PCR reaction: 25-50 uL volume with Taq polymerase, primers, dNTPs, buffer
3. Cycling conditions:
   - Initial denaturation: 94C for 2-5 min
   - 30-35 cycles: 94C (30s), 52-55C (30s), 72C (45-60s)
   - Final extension: 72C for 5-10 min
4. Verify product on agarose gel (~600 bp band expected for full ITS)

### Challenges

- PCR inhibitors in soil, wood, and environmental samples
- Co-amplification of non-target DNA (bacteria, plants)
- Bias in primer matching across diverse fungal groups
- Chimeric sequences formed during PCR

## Sequencing

### Sanger Sequencing

- Used for single-species identification (culture isolates, fruiting body tissue)
- One sequence per sample
- Gold standard for reference sequences
- Cost: ~$5-15 per sample

### High-Throughput Sequencing (HTS)

- Used for metabarcoding — identifying all fungi in an environmental sample (soil, air, water)
- Platforms: Illumina MiSeq (most common), Ion Torrent, PacBio, Oxford Nanopore
- Can generate millions of sequences per run
- Enables community-level studies of [[arbuscular-mycorrhizal-fungal-diversity-patterns-distribution]]
- Illumina MiSeq: ~300 bp paired-end reads (ITS2 region ideal)

### PacBio Long-Read Sequencing

- Can sequence the full ITS region plus flanking ribosomal genes
- Useful for generating full-length reference sequences
- Lower throughput but higher accuracy per read

## Databases

### UNITE

- The primary database for fungal ITS sequences
- URL: unite.ut.ee
- Curated, species hypothesis-based system
- Contains over 1 million fungal ITS sequences
- Provides operational taxonomic units (OTUs) and species hypotheses (SHs)
- Integrated with PlutoF analysis platform
- Regularly updated with environmental sequences

### GenBank (NCBI)

- Comprehensive nucleotide database
- Contains all fungal ITS sequences deposited worldwide
- Less curated than UNITE — contains misidentified sequences
- BLAST search against GenBank is the standard identification method
- Caveat: always check top hits carefully, as misidentifications propagate

### BOLD (Barcode of Life Data System)

- Originally designed for COI (animal barcode)
- Now includes fungal ITS sequences
- Less comprehensive than UNITE for fungi

### Other Resources

- **CBS/KNAW culture collection**: Type strain sequences
- **MycoBank**: Fungal nomenclature database linked to sequence data
- **Q-bank**: Plant pathogenic fungi database for biosecurity
- **EUROFUNGI**: European [[biodiversity-fungal-culture-preservation]] collection sequences

## Bioinformatics Pipeline

1. **Quality filtering**: Remove low-quality reads, trim primers and adapters
2. **Clustering/Denoising**: Group similar sequences into OTUs (97% similarity) or ASVs (exact sequence variants)
3. **Taxonomic assignment**: Compare against reference databases using BLAST, RDP classifier, or machine learning approaches
4. **[[rhizosphere-fungal-community-analysis-rrna-rdna]]**: Calculate diversity metrics, compare communities

Common software: QIIME2, DADA2, mothur, OBITOOLS, USEARCH

## Citizen Science
## See Also

- [[mushroom-taxonomy-history]] — How molecular methods revolutionized fungal classification
- [[fungal-symbiosis-types]] — Identifying [[mycelium-running-symbiotic-fungi-relationships]] through barcoding
- [[fungal-parasites-and-predators]] — [[biodiversity-fungal-molecular-identification-dna-barcoding]] of predatory fungi
- [[fungal-biology-fundamentals]]
- [[lichen-biology-guide]]

## Related

- [[fungal-species-estimates-taxonomy]]
- [[fungal-species-concept-and-taxonomy]]
