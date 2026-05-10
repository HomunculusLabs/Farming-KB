# QIIME Bioinformatics Pipeline for 16S rRNA Microbiome Analysis

## Overview

QIIME (Quantitative Insights Into Microbial Ecology) version 1.7.0 is an open-source
bioinformatics pipeline designed for analyzing high-throughput microbial community
sequencing data. The cannabis microbiome study by Winston et al. (2014) employed this
pipeline to process 16S rRNA gene amplicon sequences from the V4 hypervariable region,
characterizing bacterial communities across bulk soil, rhizosphere, and endorhiza
compartments of multiple Cannabis sativa cultivars.

This page describes each major stage of the pipeline as applied to that study.

## Quality Filtering

The pipeline begins with quality filtering of raw Illumina reads to remove low-quality
sequences that could introduce spurious operational taxonomic units (OTUs) or distort
diversity estimates. In QIIME 1.7.0, this step typically employs several filters:

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

The RDP Naive Bayes classifier assigns taxonomic labels to each OTU's representative
sequence. Trained on reference sequences with known taxonomy, it uses k-mer word
frequencies to calculate posterior probabilities at each rank. Assignments below a
confidence threshold (typically 0.80) are flagged as unreliable. This handles the
variable sequence quality and incomplete reference coverage of environmental amplicon
data better than simple BLAST-based methods.

## Alpha and Beta Diversity Metrics

**Alpha diversity** (within-sample) metrics computed in QIIME include:

- Observed OTU richness (simple count of unique OTUs)
- Chao1 richness estimator (accounts for undetected rare taxa)
- Shannon diversity index (combines richness and evenness)
- Faith's phylogenetic diversity (sum of branch lengths spanned by community taxa)

**Beta diversity** (between-sample) metrics leverage the phylogenetic tree through
UniFrac distances, which weight community differences by evolutionary relatedness:

- **Unweighted UniFrac** considers only the presence or absence of lineages, making
  it sensitive to rare taxa and community composition.
- **Weighted UniFrac** incorporates relative abundance, emphasizing dominant taxa.

Principal Coordinates Analysis (PCoA) ordinates samples based on pairwise UniFrac
distances, visualizing community-level patterns in reduced-dimensional space.

## Rarefaction and Statistical Testing

**Rarefaction** standardizes samples by subsampling to equal sequencing depth, ensuring
diversity comparisons are not confounded by unequal sampling effort. Multiple
rarefactions reveal whether diversity estimates have stabilized (reached an asymptote).

**ADONIS (Permutational MANOVA)** tests whether sample groups differ significantly in
community composition. It partitions variation by factor (cultivar, soil type,
compartment) and assesses significance through permutation, providing an R-squared
effect size and p-value.

**ANOSIM (Analysis of Similarities)** provides a rank-based alternative test, with
an R statistic from 0 (no difference) to 1 (complete separation).

**BEST (Bio-Env Stepwise) analysis** identifies which environmental variables best
explain community variation by testing combinations of parameters (soil pH, nutrients,
cultivar identity) against community distance matrices.

## References

- Winston, M.E., et al. (2014). Understanding Cultivar-Specificity and Soil
  Determinants of the Cannabis Microbiome. PLoS ONE, 9(6), e99641.
  https://doi.org/10.1371/journal.pone.0099641
- Caporaso, J.G., et al. (2010). QIIME allows analysis of high-throughput community
  sequencing data. Nature Methods, 7(5), 335–336.

## See Also

- [[cellvibrio-and-root-decay-microbiome]]
- [[16s-rrna-sequencing-microbiome-analysis-cannabis]]
- [[rhizosphere-fungal-community-analysis-rrna-rdna]]
- [[edaphic-determinants-cannabis-microbiome-community-structure]]
- [[cannabis-microbiome-agricultural-implications-and-future-directions]]
