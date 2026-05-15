---
title: QIIME
source: understanding-cultivar-specificity-cannabis-microbiome.md
type: entity
---

## Description

**QIIME** (Quantitative Insights Into Microbial Ecology, pronounced "chime") is an open-source bioinformatics software pipeline for performing microbiome analysis from raw DNA sequencing data. It is one of the most widely used tools in microbial ecology for processing 16S rRNA gene amplicon sequencing data. QIIME was referenced as a core analysis tool in the Cannabis microbiome study for community sequencing data analysis. The pipeline produces diversity metrics including the [[chao1-index]] for alpha diversity and [[unifrac]] for beta diversity analysis.

## Classification

- **Category:** Bioinformatics software pipeline
- **Type:** Open-source microbiome analysis platform
- **Primary use:** 16S rRNA amplicon sequencing analysis
- **Languages:** Python (QIIME 1), Python 3 (QIIME 2)
- **License:** BSD license

## Key Facts

- QIIME was developed by the Knight Lab at the University of Colorado and first published in Nature Methods in 2010 (Caporaso et al., 2010).
- The pipeline handles the complete workflow: demultiplexing, quality filtering, OTU picking (operational taxonomic unit clustering), taxonomic assignment, and diversity analysis.
- In the Cannabis microbiome study, QIIME was used alongside the Greengenes database for taxonomic classification of bacterial communities.
- Key QIIME-supported analyses used in the study include: alpha diversity ([[chao1-index]], observed species), beta diversity (weighted and unweighted [[unifrac]]), and principal coordinate analysis (PCoA).
- QIIME supports ultra-high-throughput microbial community analysis on Illumina HiSeq and MiSeq platforms (Caporaso et al., 2012).
- The successor, QIIME 2, introduced a modernized plugin-based architecture with improved reproducibility and visualization tools.

## QIIME Workflow

The QIIME pipeline processes raw sequencing data through a series of well-defined stages:

### 1. Raw Data Input and Demultiplexing
Raw paired-end or single-end FASTQ files from Illumina sequencing are demultiplexed according to barcode sequences. Each sample is identified by its unique barcode, and sequences are assigned to their respective samples. Quality scores are retained for downstream filtering.

### 2. Quality Filtering
Low-quality sequences are removed based on criteria including:
- Minimum Phred quality score threshold (typically Q19 or Q20)
- Maximum number of consecutive low-quality bases
- Minimum and maximum sequence length
- Presence of ambiguous bases (N characters)
- Primer mismatch tolerance

### 3. OTU Picking and Clustering
Sequences are clustered into Operational Taxonomic Units (OTUs) at a specified similarity threshold (typically 97% for species-level resolution):
- **De novo clustering:** Groups sequences without a reference database (e.g., UCLUST, USEARCH)
- **Closed-reference clustering:** Maps sequences against a reference database (Greengenes, SILVA, or UNITE)
- **Open-reference clustering:** Combines both approaches — sequences are first matched to a reference, then remaining sequences are clustered de novo

### 4. Taxonomic Assignment
Representative sequences from each OTU are classified taxonomically using:
- The Greengenes database (used in the Cannabis microbiome study)
- The SILVA ribosomal RNA database
- The RDP (Ribosomal Database Project) classifier
- The UNITE database for fungal ITS sequences

### 5. Phylogenetic Tree Construction
For phylogenetic-based diversity metrics like [[unifrac]], a phylogenetic tree is constructed from aligned representative sequences. QIIME supports multiple alignment methods (PyNAST, MAFFT, MUSCLE) and tree-building algorithms (FastTree, RAxML).

### 6. Diversity Analysis
QIIME calculates both alpha and beta diversity metrics:
- **Alpha diversity (within-sample):** [[chao1-index]], observed species, Shannon index, Simpson index, PD whole tree
- **Beta diversity (between-sample):** Weighted and unweighted [[unifrac]], Bray-Curtis dissimilarity, Jaccard distance
- Results are visualized through PCoA (Principal Coordinate Analysis) plots and Emperor interactive visualizations

## QIIME 1 vs QIIME 2

### QIIME 1 (2010-2018)
- Written in Python 2
- Monolithic script-based architecture
- Wide ecosystem of contributed scripts
- No built-in provenance tracking
- Deprecated but still referenced in older publications

### QIIME 2 (2017-present)
- Written in Python 3
- Plugin-based modular architecture
- Semantic type system for data validation
- Complete provenance tracking for reproducibility
- Visualizations delivered as `.qzv` files viewable in q2view
- Regular plugin updates from the community
- Integrates with [[16s-rrna-sequencing-microbiome-analysis]] workflows

## Application in Cannabis Microbiome Research

In the Cannabis cultivar-specificity study, QIIME was used to analyze bacterial community structure across three compartments:
- **Bulk soil:** The background soil community
- **Rhizosphere:** Soil tightly adhering to roots
- **Endorhiza:** Root interior (endophytic community)

Key analyses performed with QIIME in this study:
1. **Alpha diversity** using the [[chao1-index]] revealed highest richness in bulk soil and lowest in the endorhiza
2. **Beta diversity** using [[unifrac]] showed that soil type dominates community membership while cultivar genotype shapes community abundance
3. **PCoA** visualization demonstrated the clustering of communities by compartment and soil type

See weighted unifrac strain clustering cannabis endorhiza community structure and weighted vs unweighted unifrac cannabis strain microbiome for detailed analysis of the UniFrac results from this study.

## Relevance to Cultivation and Mycology

- **Microbiome research standard:** QIIME is the de facto standard for analyzing plant-associated microbial communities, including those of Cannabis, medicinal mushrooms, and other cultivated organisms.
- **Community profiling:** Enables researchers to identify bacterial taxa present in bulk soil, rhizosphere, and endorhiza, revealing how cultivar genotype and soil type structure these communities.
- **Diversity analysis:** Provides built-in methods for both alpha (within-sample) and beta (between-sample) diversity calculations essential for comparing microbial communities across growth conditions.
- **Reproducibility:** QIIME 2's artifact-based provenance tracking ensures that microbiome analyses can be reproduced, which is critical for peer-reviewed cultivation research.

## See Also

- [[chao1-index]] — Alpha diversity metric calculated by QIIME
- [[unifrac]] — Beta diversity metric calculated by QIIME
- [[16s-rrna-sequencing-microbiome-analysis]] — The sequencing method processed by QIIME
- unifrac weighted unweighted analysis cannabis microbiome — UniFrac analysis in Cannabis research
- [[fungal-identification-and-biodiversity-assessment]] — [[fungal-biodiversity-assessment-methods]]

## Sources

- Understanding cultivar-specificity in the Cannabis microbiome (PLOS ONE, 2014)
- Caporaso JG, et al. (2010) QIIME allows analysis of high-throughput community sequencing data. Nature Methods, 7(5):335-336.
- Caporaso JG, et al. (2012) Ultra-high-throughput microbial community analysis on the Illumina HiSeq and MiSeq platforms. ISME J, 6(8):1621-1624.
