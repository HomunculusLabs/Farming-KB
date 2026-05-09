---
title: Molecular PCR Methods for pcr methods fungal identification monitoring and Monitoring
created: 2026-04-21
updated: 2026-04-21
type: concept
tags: [reference]
sources:
  - raw/papers/singh-harbhajan_-mycoremediation-_-fungal-bioremediation.md
---

# Molecular PCR Methods for Fungal Identification and Monitoring

Polymerase chain reaction (PCR) based methods have revolutionized [[molecular-methods-fungal-taxonomy-and-diversity]], enabling discrimination among morphologically indistinct taxa and assessment of genetic diversity in natural populations. These techniques are especially valuable for fungi with few morphological markers.

## Arbitrarily Primed PCR (apPCR / RAPD)

### Principle
Short oligonucleotide primers (10-20 bp) anneal to complementary DNA sequences. When matching sites are in opposite orientation on separate strands, a PCR product is amplified. Number and size of products depend on primer binding site frequency and distribution.

### Capabilities
- 10-20 primers can generate >100 genetic markers
- For 15-16 bp primers of simple sequence repeats [e.g., (CAG)5, (GACA)4]:
  - Conspecific individuals share 80-100% of bands
  - Different species share 0-20% of bands
- Species-specific band patterns allow unequivocal taxonomic identification

### Applications
- **Taxonomic discrimination:** Colletotrichum species that lost infectivity and sporulation were identified as 5 distinct species
- **Basidiomycete identification:** Boletus, Cantharellus, Cortinarius, Inocybe, Stropharia, Ganoderma all distinguished by apPCR patterns
- **Genetic [[ingham-soil-food-web-diversity-assessment-dna-molecular-methods]]:** Population-level variation within species

### Reproducibility Issues
Major source of nonreproducibility: **thermocycler inaccuracy**
- Only 3 of 20 tested thermocyclers from 9 companies achieved programmed denaturing temperatures
- Some machines never reached within 10C of target temperature
- Incomplete denaturation = unavailable primer binding sites = different band patterns
- Other factors: reaction buffer, primer composition, DNA polymerase source, template quality

### Thermocycler Testing Protocol
- Scanning thermocouple thermometer connected to 12 temperature probes
- 20 ul PCR reactions in 0.5 ml tubes
- Test denaturing accuracy, precision, and reproducibility
- Recommended brands: Barnstead Thermolyne, MJ Research, Stratagene

## Dual-Primer PCR (dpPCR)

Uses two primers instead of one:
- Same reaction buffer as apPCR
- No ramp times imposed
- Annealing temperature: 58C
- More specific than apPCR
- Products can be used for species-specific primer design

## Nested-Primer PCR (npPCR)

- dpPCR products diluted fivefold with Tris-HCl (pH 9.0)
- Transferred to fresh reaction with two nested primers
- Nested primers designed from terminal sequences of cloned apPCR products
- Higher specificity than dpPCR alone

## Cloning and Species-Specific Primer Design

1. Generate apPCR band pattern from target species
2. Isolate specific product from agarose gel
3. Purify by glass bead method
4. Clone into vector (e.g., pT7Blue) for sequence analysis
5. Sequence analysis by Sanger chain-termination method
6. Design species-specific dpPCR primers from terminal sequences
7. Design nested npPCR primers for additional specificity

## Nuclear vs. Mitochondrial DNA

### Nuclear DNA
- Very large genomes (1.5 x 10^7 to 820 x 10^7 bp)
- Thousands of genetic loci
- Contains both single-copy and repetitive DNA
- Best for genetic diversity and molecular fingerprinting
- Best for taxonomic discrimination

### Mitochondrial DNA
- Relatively small (20-80 kb)
- Maternally transmitted
- Functions similarly across fungi
- Single genetic locus (but some recombination observed)
- Best for phylogenetic differences between closely related species

## Requirements for Genetic Diversity Assessment

1. System must identify differences among individuals and be applicable to other species
2. Utility must be comparable to other methods
3. Must accommodate large sample numbers efficiently
4. Genetic markers must behave as normal Mendelian traits
5. Results must be reproducible across laboratories

## Future Directions

- Library of known apPCR band patterns available on the Internet for comparative analyses
- Integration with rDNA sequencing for comprehensive identification
- High-throughput sequencing reducing reliance on culture-based methods

## See Also

- [[dna-barcoding-fungal-identification]]
- [[ribosomal-rna-sequencing-yeast-identification]]
- [[arbuscular-mycorrhizal-fungal-diversity-patterns-distribution]]
- fungal-culture-media-formulas-applications
