---
title: Fungal Rdna Primers Molecular Identification
created: 2026-04-16
updated: 2026-04-16
type: concept
tags: [mycology, fungi]
sources: []
---
# Fungal Ribosomal DNA Primers and Molecular Identification

Ribosomal DNA (rDNA) is the most widely used molecular marker for fungal identification, phylogenetics, and biodiversity assessment. The ribosomal RNA gene cluster in fungi contains conserved and variable regions that enable identification at multiple taxonomic levels.

## The Ribosomal RNA Gene Cluster

The fungal nuclear rDNA is organized as tandem repeats containing, in order:
- **18S (SSU)**: small subunit ribosomal RNA gene — highly conserved, useful for deep phylogenetic relationships
- **ITS1**: Internal Transcribed Spacer 1 — moderately variable, useful for species-level identification
- **5.8S rRNA gene**: conserved region of approximately 160 nucleotides
- **ITS2**: Internal Transcribed Spacer 2 — moderately variable, complementary utility to ITS1
- **28S (LSU)**: large subunit ribosomal RNA gene — intermediate variability, useful for genus to family-level relationships
- **IGS**: Intergenic Spacer — highly variable, useful for population-level and strain-level discrimination

The 5.8S rRNA molecule contains modified nucleotides but is more conserved than the ITS regions. Walker (1985) noted that 5.8S rDNA data can be problematic for some analyses because certain nucleotide positions are difficult to determine.

## The ITS Region as the Primary Fungal Barcode

The ITS region (ITS1 + 5.8S + ITS2) has been adopted as the official DNA barcode for fungi. Its advantages include:
- Universal primer binding sites in the conserved flanking 18S and 28S regions
- Sufficient variability for species-level discrimination in most fungal groups
- Available reference sequences in public databases (UNITE, GenBank) for comparison
- Short enough length (~500-700 bp) for routine PCR amplification and Sanger sequencing

### Universal ITS Primers

The most widely used primer pairs include:
- **ITS1/ITS4**: amplifies the entire ITS region plus portions of flanking 18S and 28S; ITS5/ITS4 is an equivalent pair
- **ITS1-F/ITS4**: ITS1-F is specific to fungi, reducing amplification of plant DNA in environmental samples
- **ITS3/ITS4**: amplifies ITS2 plus 5.8S, useful when ITS1 is difficult to sequence

Gardes and Bruns (1993) designed ITS1-F, which has enhanced specificity for basidiomycetes and reduces co-amplification of plant DNA — a critical advantage when amplifying DNA from mycorrhizal root tips or plant-associated environmental samples.

## 18S (SSU) rDNA

The small subunit (18S) ribosomal RNA gene is approximately 1,800 bp and is highly conserved. It is most useful for:
- Deep phylogenetic analyses at the phylum to kingdom level
- Environmental surveys targeting broad taxonomic groups
- Studies of early-diverging fungal lineages
- Metagenomic analyses where broad-range detection is needed

Swann and Taylor (1995a, 1995b) used 18S rDNA sequences for phylogenetic analyses of basidiomycete relationships. The high conservation of 18S limits its resolution for species-level identification in many groups.

## 28S (LSU) rDNA

The large subunit (28S) ribosomal RNA gene provides intermediate phylogenetic resolution:
- More variable than 18S, allowing discrimination among genera and families
- Conserved enough for broad-range primer design
- D1-D2 and D3-D4 domains are the most variable regions
- Widely used in environmental sequencing studies
- LSU alone or in combination with ITS provides robust identification

## RFLP Analysis

Restriction Fragment Length Polymorphism (RFLP) analysis of rDNA regions was historically important before widespread DNA sequencing:
- RFLP patterns of the ITS and IGS regions can distinguish among strains and species
- Magee and colleagues (1990) used RFLP patterns to map genetic profiles
- RFLP analysis of the IGS region resolved strains within species
- Cost-effective alternative to sequencing when only a few taxa are being distinguished

However, RFLP analysis has limited resolution compared to sequence analysis and is increasingly replaced by direct sequencing approaches.

## RFLP vs. Sequence Analysis

The costs (time and expense) of RFLP and sequence analysis differ considerably. Evolutionary trees generated from RFLP data have limited resolution, whereas sequence analysis provides greater resolution, producing trees with well-resolved nodes. Cloned fragments and analysis of RFLPs provide greater diversity at the mitochondria level, but sequence analysis provides the most definitive results.

## Challenges in Molecular Identification

Several challenges complicate rDNA-based fungal identification:
- **Intraspecific variation**: some species contain significant ITS variation among strains
- **Interspecific conservation**: some closely related species share identical ITS sequences
- **Database quality**: many reference sequences are misidentified or lack voucher specimens
- **Undescribed species**: sequences from novel taxa have no database matches
- **Heterogeneity in environmental samples**: mixed templates may produce ambiguous sequences
- **Numts**: nuclear mitochondrial pseudogenes may be co-amplified, confusing results

## PCR Protocols for Fungal rDNA

Standard PCR conditions for fungal rDNA amplification include:
- Initial denaturation at 94-95 degrees C
- 30-35 cycles of denaturation (94 degrees C), annealing (50-55 degrees C for ITS primers), and extension (72 degrees C)
- Final extension at 72 degrees C
- Products visualized on agarose gels and purified for sequencing

For environmental samples, nested PCR approaches (npPCR) or touchdown PCR protocols may improve specificity and yield.

## Related Topics

- [[fungal-molecular-identification]]
- [[fungal-dna-barcoding]]
- [[fungal-dna-extraction-methods]]
- [[fungal-metagenomics]]
- [[culturing-culture-independent-fungi]]

## References

- Biodiversity of Fungi (2004), Chapter 6: Molecular Approaches to Assessing Fungal Biodiversity
- Gardes, M. and Bruns, T.D. 1993. ITS primers with enhanced specificity for basidiomycetes
- White, T.J. et al. 1990. Amplification and direct sequencing of fungal ribosomal RNA genes
- Nilsson, R.H. et al. 2008. The UNITE database for molecular identification of fungi
- [[arbuscular-mycorrhizal-fungal-diversity-patterns-distribution]]
- [[rhizosphere-fungal-community-analysis-rrna-rdna]]
- [[fungal-biodiversity-data-analysis]]
