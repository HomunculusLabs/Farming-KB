---
title: Fungal Genetics
created: 2026-04-11
updated: 2026-04-12
type: concept
tags: [fungi, biology, academia, lab-technique, microbes]
sources: []
---

# Fungal Genetics

Fungal genetics encompasses the study of heredity, variation, and gene function in fungi. Fungi serve as powerful model organisms for genetic research — they have compact genomes, short life cycles, and haploid genetics that make mutant analysis straightforward. Advances in fungal genetics drive applications in medicine, agriculture, and biotechnology.

## Fungal Genomes

### General Features

- **Size**: Fungal genomes range from ~10 Mb (in compact yeasts like Ashbya) to over 1 Gb (in some [[basidiomycetes]])
- **Gene count**: Typically 5,000-15,000 protein-coding genes
- **Gene density**: Higher than in plants and animals — fewer introns, less repetitive DNA
- **Chromosomes**: Vary from 4-6 in yeasts to 10+ in filamentous fungi. Chromosome number does not correlate with genome size
- **Ploidy**: Predominantly haploid during vegetative growth (unlike plants and animals), which simplifies genetic analysis

### Model Organism Genomes

| Species | Genome Size | Genes | Chromosomes | Year Sequenced |
|---------|------------|-------|-------------|---------------|
| [[saccharomyces-cerevisiae]] | 12.1 Mb | ~6,275 | 16 | 1996 |
| Schizosaccharomyces pombe | 13.8 Mb | ~4,929 | 3 | 2002 |
| Aspergillus nidulans | 30.1 Mb | ~11,000 | 8 | 2003 |
| [[neurospora-crassa]] | 40 Mb | ~10,000 | 7 | 2003 |
| Coprinopsis cinerea | 37.5 Mb | ~13,000 | 13 | 2003 |
| [[schizophyllum-commune]] | 38.5 Mb | ~14,000 | 11 | 2011 |

## Mating Types and Sexual Genetics

See [[fungal-sexual-reproduction]] for comprehensive coverage of mating systems.

### Mating Type Loci

- Fungal mating is controlled by **mating type (MAT) loci**, which are functionally analogous to sex chromosomes in animals
- MAT loci encode transcription factors, pheromones, and pheromone receptors
- Unlike male/female in animals, fungal mating types are not differentiated by size or gamete type — they are molecularly defined

### Bipolar Systems

- Single MAT locus with multiple alleles
- ~50% inter-fertility among spores from a single fruiting body
- Example: Coprinellus (Coprinus) with A1, A2, A3... alleles

### Tetrapolar Systems

- Two unlinked loci (A and B) with multiple alleles each
- ~25% inter-fertility among spores from a single fruiting body
- A locus: regulates nuclear pairing and [[clamp-connection]] formation
- B locus: regulates nuclear migration and septal dissolution
- Example: Schizophyllum commune has hundreds of A and B alleles, creating thousands of possible mating types

## Heterokaryosis

The condition where fungal cells contain two or more genetically distinct nuclei:

- **Dikaryon**: The most common form — cells contain exactly two nuclei from different parents (n+n)
- **Heterokaryon**: May contain multiple nuclei from different parents in varying ratios
- **Advantage**: Genetic diversity within a single mycelium allows rapid adaptation without sexual reproduction
- **Regulation**: Nuclei cooperate but maintain separate identities. Each nucleus continues to divide independently
- **Stability**: In basidiomycetes, the dikaryotic state is remarkably stable — maintained indefinitely by clamp connections

## The Parasexual Cycle

Discovered by Pontecorvo (1956) in Aspergillus nidulans, the parasexual cycle allows genetic recombination without sexual reproduction:

1. **Heterokaryosis**: Two genetically distinct haploid strains fuse (anastomose) to form a heterokaryon
2. **Diploidization**: Occasionally, two unlike nuclei in the heterokaryon fuse to form a diploid nucleus (2n)
3. **Mitotic recombination**: During mitosis, crossing over can occur between homologous chromosomes, producing recombinant genotypes
4. **Haploidization**: The diploid nucleus may lose chromosomes through nondisjunction events during subsequent mitoses, returning to a haploid state with a recombinant genotype

The parasexual cycle is significant because:
- It occurs in fungi that lack a known sexual cycle (asexual fungi like Aspergillus and Penicillium)
- It generates genetic diversity without meiosis
- It has been exploited for genetic mapping and strain improvement in industrial fungi

## Genetic Tools and Techniques

### Classical Mutagenesis

- **UV irradiation**: Induces point mutations and small deletions. Standard method for creating mutant libraries
- **Chemical mutagens**: EMS (ethyl methanesulfonate), NTG (N-methyl-N'-nitro-N-nitrosoguanidine) — high mutation rates
- **Selection**: Grow mutants on selective media (antibiotic resistance, nutritional requirements)
- **Complementation testing**: Cross two mutants with the same phenotype; if the offspring are wild-type, the mutations are in different genes

### Transformation

Introducing foreign DNA into fungal cells:

- **Protoplast transformation**: Remove cell wall with enzymes, expose naked cells to DNA, regenerate cell wall
- **Agrobacterium-mediated transformation**: Use [[agrobacterium-tumefaciens]] to deliver DNA — works for many fungi including mushrooms
- **Electroporation**: Apply electric pulse to create temporary pores in the cell membrane
- **Biolistics**: Coat DNA on gold/tungsten particles and shoot into cells with a gene gun
- **Lithium acetate method**: Standard for S. cerevisiae — makes cells permeable to DNA

### Gene Silencing

- **RNAi (RNA interference)**: Introduce double-stranded RNA targeting a specific gene; cellular machinery degrades the corresponding mRNA
- Works well in many ascomycetes; less reliable in basidiomycetes
- Used for functional gene studies and potential crop protection

### Fluorescent Markers

- **GFP (Green Fluorescent Protein)**: Reporter gene for visualizing gene expression and protein localization in living hyphae
- **mCherry, YFP**: Other fluorescent proteins for multi-color labeling
- Allows real-time observation of hyphal growth, organelle movement, and nuclear behavior

## CRISPR in Fungi

CRISPR-Cas9 genome editing has revolutionized fungal genetics since ~2015:

### Applications

- **Gene knockout**: Precisely delete target genes to study function
- **Gene knock-in**: Insert genes at specific genomic locations
- **Allele replacement**: Swap one allele for another to study variants
- **Promoter engineering**: Modify gene expression levels
- **Multiplex editing**: Edit multiple genes simultaneously

### Status in Major Fungal Groups

| Group | CRISPR Status | Notable Achievements |
|-------|--------------|---------------------|
| Yeasts (S. cerevisiae) | Well established | Precise metabolic engineering for biofuel production |
| Aspergillus spp. | Well established | Strain improvement for enzyme production |
| Penicillium spp. | Established | Enhanced penicillin production |
| Trichoderma spp. | Established | Improved enzyme cocktails |
| Neurospora crassa | Established | Model for repeat-induced point mutation (RIP) |
| Pleurotus spp. (oyster) | Emerging | Early-stage editing for cultivation traits |
| [[agaricus-bisporus]] | Emerging | Challenging due to multinucleate cells |
| Psilocybe spp. | Nascent | Potential for understanding psilocybin biosynthesis |

### Challenges in Mushroom-Forming Fungi

- Many basidiomycetes are dikaryotic — two nuclei per cell complicates editing
- Efficient transformation protocols are still being developed for many species
- Some species have robust DNA repair systems that reduce editing efficiency
- Regulatory concerns for genome-edited cultivated mushrooms

## Epigenetics in Fungi

- **DNA methylation**: Variable across fungal groups. Heavy in some basidiomycetes; minimal in S. cerevisiae (no detectable methylation)
- **Repeat-Induced Point Mutation (RIP)**: A fungal-specific genome defense in Neurospora and related genera. Duplicates DNA sequences are mutated by C-to-T transitions during the sexual cycle, silencing transposons and duplicated genes
- **Histone modifications**: H3K9 methylation, H3K27 methylation regulate gene expression
