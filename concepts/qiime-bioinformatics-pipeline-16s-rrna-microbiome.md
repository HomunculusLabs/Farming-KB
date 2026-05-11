# QIIME Bioinformatics Pipeline for 16S rRNA Microbiome Analysis

## Overview

QIIME (Quantitative Insights Into [[fukuoka-microbial-ecology-decomposition]]) version 1.7.0 is an open-source
bioinformatics pipeline designed for analyzing high-throughput [[cannabis-cultivar-microbial-community-effects]]
sequencing data. The [[winston-cannabis-microbiome-study-design]] by Winston et al. (2014) employed this
pipeline to process 16S rRNA gene amplicon sequences from the V4 hypervariable region,
characterizing [[cannabis-endorhiza-bacterial-communities]] across bulk soil, rhizosphere, and endorhiza
compartments of multiple [[blesching-cannabis-sativa-indica-classification]] cultivars.

This page describes each major stage of the pipeline as applied to that study.

## Quality Filtering

The pipeline begins with quality filtering of raw Illumina reads to remove low-quality
sequences that could introduce spurious operational taxonomic units (OTUs) or distort
[[fungal-diversity-estimates]]. In QIIME 1.7.0, this step typically employs several filters:

- **Phred quality score thresholds:** Sequences with average quality scores below a
  cutoff (commonly Q20 or Q30) are discarded. Sequences failing to meet the
  threshold across a sliding window may also be truncated rather than discarded.

- **Length filtering:** Reads outside the expected V4 amplicon length range are
  removed, as they likely represent non-target amplification or chimeric artifacts.

- **Ambiguous base filtering:** Sequences containing ambiguous nucleotide calls (N)
  are excluded to prevent downstream alignment or classification errors.

- **Primer sequence removal:** Forward and reverse primer sequences are trimmed to
  avoid interference with OTU picking and taxonomic assignment.

Quality filtering is critical because downstream analyses assume each sequence
represents a genuine biological observation. Poor-quality sequences inflate diversity
estimates and create phantom OTUs not corresponding to real organisms.

## OTU Picking: Open vs. Closed Reference

OTU (Operational Taxonomic Unit) picking clusters sequences into groups presumed to
represent the same taxonomic species or strain, typically at 97% sequence identity.
QIIME 1.7.0 supports two main strategies:

**Closed-reference OTU picking** maps each sequence to a predefined reference database
(Greengenes). Sequences that do not match are discarded — conservative but loses novel
taxa. **Open-reference OTU picking** performs closed-reference clustering first, then
clusters unmatched sequences de novo. This hybrid captures novel diversity while
maintaining reference-based comparability. Winston et al. used open-reference picking
to ensure cannabis-associated microbes absent from Greengenes were retained.

## Greengenes Database and 97% Clustering

The Greengenes database is a curated reference collection of 16S rRNA gene sequences
with associated taxonomy and phylogeny. Key characteristics include:

- **Curated alignment:** All sequences are pre-aligned using a consistent positional
  numbering scheme (NAST format), enabling direct comparison across taxa.

- **Hierarchical taxonomy:** Each reference sequence carries a seven-level taxonomic
  assignment from domain through species (or the lowest resolved rank).

- **Phylogenetic tree:** A pre-computed reference phylogeny allows rapid phylogenetic
  diversity calculations without de novo tree building for reference-matched OTUs.

Clustering at 97% identity is the conventional threshold for defining bacterial
species-level OTUs, based on empirical observations that strains sharing ≥97% 16S
rRNA sequence identity typically belong to the same species. This threshold balances
the risk of lumping distinct species together against over-splitting strains of the
same species into separate OTUs.

## PyNAST Alignment

After OTU picking, representative sequences are aligned using PyNAST (PyNAST-like
Alignment Search Tool), which maps queries to a template alignment from the Greengenes
core set using the NAST algorithm. This step is essential for phylogenetic analysis
because evolutionary distances require properly aligned sequences. PyNAST applies a
minimum identity threshold; sequences failing to align are excluded from phylogenetic
analyses. The resulting multiple sequence alignment positions homologous sites across
all OTUs for meaningful evolutionary comparison.

## FastTree Phylogenetic Tree Construction

From the PyNAST alignment, FastTree constructs a phylogenetic tree using approximate
maximum-likelihood methods. FastTree handles thousands of OTUs efficiently while
maintaining accuracy comparable to slower implementations. The resulting tree encodes
evolutionary relationships among all OTUs and is required for phylogenetic diversity
metrics such as UniFrac, which measure community dissimilarity based on shared branch
lengths between taxa in different samples.

## RDP Classifier for Taxonomic Assignment
