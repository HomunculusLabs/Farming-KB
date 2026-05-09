---
title: Mycorrhizal Proteomics
created: 2026-04-16
updated: 2026-04-16
type: concept
tags: [[mycology, soil-biology, symbiosis]
sources: [papers/symbiotic-fungi.md]
---
# Mycorrhizal Proteomics

Mycorrhizal proteomics is the large-scale study of protein expression patterns in mycorrhizal symbioses, using techniques such as two-dimensional gel electrophoresis (2-DE) and mass spectrometry (MALDI-TOF). This field complements transcriptomics and genomics by providing direct information on the proteins actually present and active during symbiosis, including post-translational modifications that transcript-level studies cannot detect.

## Why Proteomics in Mycorrhizal Research?

Transcriptomics reveals gene expression at the mRNA level, but there is often poor correspondence between mRNA abundance and actual protein levels. Key reasons for studying mycorrhizal proteomics include:

- **Post-translational modifications**: Phosphorylation, glycosylation, and other modifications alter protein function without changing transcript levels. Signal transduction events involving Ca2+ influx and kinase activation are particularly affected
- **Protein turnover rates**: Some defense-related proteins may be rapidly degraded, making their mRNA appear elevated while protein levels remain low
- **Spot overlap**: A single 2-DE spot may contain multiple proteins, and the protein of interest may be masked by more abundant proteins
- **Membrane proteins**: Many signaling receptors are membrane-bound and resist standard 2-DE separation, requiring sub-cellular fractionation

## Experimental Approaches

### 2-DE and MALDI-TOF

The classical proteomics workflow for mycorrhizal research involves:

1. **Protein extraction**: Simultaneous extraction of mRNA and proteins from root tissue using protocols that preserve both analytes
2. **2-DE separation**: Proteins are separated by isoelectric point (first dimension) and molecular weight (second dimension)
3. **Staining**: Coomassie Blue or silver staining visualizes protein spots; micropreparative gels allow spot excision
4. **In-gel trypsin digestion**: Excised spots are digested into peptides
5. **MALDI-TOF**: Peptide mass fingerprinting (PMF) identifies proteins by matching mass spectra to database entries

### Sub-Cellular Proteomics

Targeted sub-cellular fractionation improves coverage:

- **Microsomal proteomics**: Enriches for membrane-associated proteins involved in recognition and signaling
- **Plasmalemma proteomics**: Identifies plasma membrane proteins including transporters and receptors
- **Cell wall proteomics**: Relevant for understanding recognition events during early mycorrhizal infection
- **Mitochondrial/vacuolar proteomics**: Energy metabolism and compartment-specific responses

## Key Proteins Identified in AM Symbiosis

### Defense-Related Proteins

Proteomic studies of Medicago truncatula colonized by Glomus mosseae identified several defense-related proteins that change in abundance during early symbiosis stages:

- **Peroxidases** (MtC40023, MtC10717): Upregulated in response to colonization; peroxidase activity increases in both ecto- and endomycorrhizal symbioses. May be involved in cell wall reinforcement or reactive oxygen species signaling
- **Glutathione-S-transferases (GST)**: Multiple GST isoforms show differential regulation. Tau-class GSTs are downregulated, while other GSTs accumulate. GSTs are associated with stress tolerance and may participate in arbuscule development or degradation
- **Chalcone reductase** (MtC00294): A NAD(P)H-dependent enzyme involved in flavonoid biosynthesis. Upregulated during early elicitor-mediated signaling, suggesting overlap between mycorrhizal and pathogen recognition pathways

### Signaling Proteins

- **GTP-binding proteins** (MtC00498, MtC00087): Guanine nucleotide-binding proteins anchored on the cytoplasmic membrane, mediating signal transduction, protein transport, and growth regulation
- **Serine/threonine kinase** (MtC50061): Protein kinases involved in adaptation to changing environmental conditions. At least three MAP kinases are upregulated during early root colonization
- **Alanine aminotransferase** (MtC00229): A primary metabolism enzyme that also increases during early AM colonization

### Ribosomal Proteins

- **40S ribosomal protein S5** (MtC00128): Confirmed at the protein level among several ribosomal genes predicted to be overexpressed at the transcript level

## Transcript-Protein Correspondence

A major finding from comparative transcriptomic-proteomic studies is the limited correspondence between the two levels. In M. truncatula/G. mosseae interactions:

- In silico analysis of SSH library transcripts predicted 13 proteins potentially detectable on 2-DE gels from 29 overexpressed genes
- Only a few results were common at transcript and protein levels
- Some in silico-predicted proteins were not confirmed; instead, different proteins were identified at the same spot positions

This discrepancy has several explanations:
- Spot overlap (multiple proteins co-migrating)
- Post-translational modifications altering protein charge and position on gels
- Membrane proteins being excluded from 2-DE analysis
- Sub-cellular compartmentalization diluting signal

## Defense Response Paradox

A recurring theme in mycorrhizal proteomics is the observation that molecular events similar to plant-pathogen interactions occur during AM symbiosis, including:

- Signal perception and transduction
- Defense gene activation
- Production of reactive oxygen species
- Cell wall modifications

However, the defense response in AM symbiosis is characteristically weak and transient. This may reflect:
- Low capacity of AM fungi to trigger strong defense responses
- Active suppression mechanisms employed by the fungus
- Plant-mediated regulation that dampens defense once compatibility is established

The transient nature of early defense responses may serve a surveillance function, allowing the plant to distinguish symbionts from pathogens before committing to full colonization.

## Future Directions

Key areas for advancement in mycorrhizal proteomics include:

- **Sub-cellular fractionation**: Improving coverage of membrane, cell wall, and organelle proteins
- **Quantitative proteomics**: Isotope labeling and label-free quantification methods
- **Phosphoproteomics**: Mapping kinase signaling networks during symbiosis
- **Dual-organism proteomics**: Simultaneously profiling both plant and fungal proteins
- **Time-course studies**: Following proteome dynamics through all stages from presymbiotic contact to mature arbuscule function

## See Also

- [[functional-genomics-arbuscular-mycorrhiza]] — Broader context of genomic approaches to symbiosis
- [[mycorrhizal-biocontrol]] — How defense responses relate to pathogen protection
- [[plant-cell-membrane-transport-proteins]]
- [[plant-cell-membrane-transport-proteins-channels-carriers-and-pumps]]
