---
title: Fungal Rdna Primers biodiversity-fungal-molecular-identification-dna-barcoding
created: 2026-04-16
updated: 2026-04-16
type: concept
tags: [mycology, fungi]
sources: []
---
# Fungal Ribosomal DNA Primers and Molecular Identification
Ribosomal DNA (rDNA) is the most widely used [[rapd-molecular-marker-techniques-fungi]] for fungal
identification, phylogenetics, and [[fungal-biodiversity-assessment-methods]]. The ribosomal RNA
gene cluster in fungi contains conserved and variable regions that enable
identification at multiple taxonomic levels.

## The Ribosomal RNA Gene Cluster
The fungal nuclear rDNA is organized as tandem repeats containing, in order:
- **18S (SSU)**: small subunit ribosomal RNA gene — highly conserved, useful
  for deep phylogenetic relationships
- **ITS1**: Internal Transcribed Spacer 1 — moderately variable, useful for
  species-level identification
- **5.8S rRNA gene**: conserved region of approximately 160 nucleotides
- **ITS2**: Internal Transcribed Spacer 2 — moderately variable,
  complementary utility to ITS1
- **28S (LSU)**: large subunit ribosomal RNA gene — intermediate variability,
  useful for genus to family-level relationships
- **IGS**: Intergenic Spacer — highly variable, useful for population-level
  and strain-level discrimination

The 5.8S rRNA molecule contains modified nucleotides but is more conserved
than the ITS regions. Walker (1985) noted that 5.8S rDNA data can be
problematic for some analyses because certain nucleotide positions are
difficult to determine.

## The ITS Region as the Primary Fungal Barcode
The ITS region (ITS1 + 5.8S + ITS2) has been adopted as the official DNA
barcode for fungi. Its advantages include:
- Universal primer binding sites in the conserved flanking 18S and 28S
  regions
- Sufficient variability for species-level discrimination in most fungal
  groups
- Available reference sequences in public databases (UNITE, GenBank) for
  comparison
- Short enough length (~500-700 bp) for routine PCR amplification and
  Sanger sequencing

### Universal ITS Primers
The most widely used primer pairs include:
- **ITS1/ITS4**: amplifies the entire ITS region plus portions of flanking
  18S and 28S; ITS5/ITS4 is an equivalent pair
- **ITS1-F/ITS4**: fungal-specific forward primer (ITS1-F) reduces
  amplification of plant DNA in environmental samples
- **ITS3/ITS4**: amplifies ITS2 plus partial 5.8S and 28S, useful when
  only ITS2 is needed for identification
- **ITS1-F/ITS2**: fungal-specific amplification of ITS1 region only

## Primer Bias and Limitations
No single primer pair amplifies all fungal taxa equally. Understanding primer
bias is critical for interpreting biodiversity data from environmental
samples:

- **Taxonomic coverage gaps**: Standard ITS primers may underrepresent certain
  fungal groups. For example, some early-diverging fungal lineages have
  mismatches at universal primer sites that reduce or prevent amplification.
  Glomeromycota ([[comparison-soil-food-web-vs-arbuscular-mycorrhizal-fungi]] fungi) are notoriously difficult to
  amplify with standard ITS primers, requiring group-specific alternatives.

- **Copy number variation**: rDNA copy number varies enormously among fungi,
  from fewer than 10 copies in some genomes to over 200 copies in others.
  This variation means that sequence read abundance in metabarcoding studies
  does not directly reflect species abundance or biomass. Fungi with many
  rDNA copies are overrepresented relative to those with few copies.

- **Intraspecific variation**: Multiple ITS types can exist within a single
  fungal genome (intra-genomic variation), which can complicate species
  delimitation. Some species harbor divergent ITS paralogs that could be
  mistaken for distinct species in environmental sequencing data.

- **Primer dimers and non-specific amplification**: In samples with low
  [[bioremediation-fungal-biomass-biosorbent-material]] or high background DNA, primers can amplify non-target
  sequences or form primer dimers that consume reagents and generate
  spurious sequences. Touchdown PCR protocols and optimized annealing
  temperatures can help reduce these artifacts.

## Alternative and Supplementary Genetic Markers
While the ITS region serves as the primary fungal barcode, additional markers
are needed for certain [[coprophilous-fungi-taxonomic-groups-distribution]] or research questions:

### Large Subunit (28S LSU) rDNA
The D1/D2 domains at the 5-prime end of the 28S rDNA gene provide
phylogenetic signal at genus to order level. Primers LR0R and LR7 are
commonly used for yeast identification. The 28S region is increasingly
recommended as a complementary barcode because it aligns more readily
across distantly related fungi and provides better resolution for some
groups where ITS is insufficient.

### Small Subunit (18S SSU) rDNA
The 18S rDNA gene is highly conserved and most useful for deep
phylogenetic studies and environmental surveys targeting all eukaryotes.
Primers such as NS1/NS8 and FR1/FF390 target the 18S region. While too
conserved for routine species identification, 18S provides a broad
framework for placing unknown fungi within the tree of life.

### Protein-Coding Genes
Single-copy protein-coding genes offer advantages for phylogenetic
resolution where ITS is insufficient:
- **TEF1-alpha (translation elongation factor 1-alpha)**: widely used in
  Ascomycota systematics, provides good resolution at species level
- **RPB1 and RPB2 (RNA polymerase II subunits)**: powerful for deep
  phylogenetic relationships across all fungal groups
- **Beta-tubulin**: useful for Penicillium, Aspergillus, and other
  Ascomycete genera where ITS resolution is limited
- **Actin**: provides phylogenetic signal at species to genus level but
  can have paralogs that complicate analysis
- **MCB7, RPB2, and TUB2**: recommended multi-locus approaches for
  challenging genera with extensive cryptic speciation

### Mitochondrial Markers
Mitochondrial markers including mitochondrial SSU rDNA and cytochrome
oxidase I (COI) have been explored as alternative barcodes. COI shows
promise for some fungal groups but primer design has been challenging
due to mitochondrial intron variability. The mitochondrial SSU rDNA
provides useful phylogenetic signal for certain basidiomycete groups.

## PCR Protocols and Optimization
Successful amplification of fungal rDNA from diverse sample types requires
careful protocol optimization:

- **Standard PCR conditions**: Typical ITS amplification uses 30-35 cycles
  with annealing temperatures of 52-58 degrees Celsius, depending on the
  primer pair and sample type. Extension times of 30-60 seconds are
  sufficient for the relatively short ITS amplicons.

- **Touchdown PCR**: Starting with a higher annealing temperature and
  progressively reducing it over successive cycles improves specificity
  by favoring amplification of perfectly matched templates during early
  cycles when reagent concentrations are highest.

- **Nested PCR approaches**: For environmental samples with very low
  fungal DNA concentrations, a first round of PCR with universal primers
  followed by a second round with fungal-specific primers can dramatically
  increase sensitivity. However, nested approaches increase the risk of
  contamination and may introduce PCR artifacts.

- **PCR inhibitor management**: Humic acids, phenolics, and polysaccharides
## See Also
- [[fungal-dna-extraction-methods]]
- [[fungal-metagenomics]]
- [[fungal-metatranscriptomics]]
- [[fungal-species-estimation-methods-total-diversity]]
- [[fungal-biodiversity-assessment-methods]]
