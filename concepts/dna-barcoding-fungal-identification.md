---
title: DNA Barcoding for Fungal Identification
created: 2026-04-21
updated: 2026-04-21
type: concept
tags: [reference]
sources: []
---

# DNA Barcoding for Fungal Identification

DNA barcoding uses short, standardized DNA sequences to identify fungal species. The Internal Transcribed Spacer (ITS) region has been adopted as the official fungal barcode, revolutionizing fungal identification and biodiversity assessment.

## The Fungal Barcode: ITS Region

### Why ITS?
- Universal primers exist (ITS1, ITS4, ITS5) that amplify across all major fungal groups
- High interspecific variability — distinguishes most species
- Moderate intraspecific variability — allows species-level identification
- Multiple copies per genome — easy to amplify from small amounts of DNA
- Two variable spacers (ITS1, ITS2) flanking the conserved 5.8S gene
- Largest existing reference database for fungi

### ITS Structure
1. **ITS1:** Variable spacer between 18S and 5.8S rRNA genes
2. **5.8S rRNA:** Conserved (~160 nucleotides)
3. **ITS2:** Variable spacer between 5.8S and 26S rRNA genes

### Reference Databases
- **UNITE:** Curated database of fungal ITS sequences with species hypotheses
- **GenBank:** Largest sequence database but contains errors and misidentified sequences
- **BOLD:** Barcode of Life Data System
- **CBS/KNAW:** Culture collection sequences

## Applications

### Species Identification
- Identify unknown specimens by comparing ITS sequences to reference databases
- Particularly valuable for:
  - Microfungi that cannot be identified morphologically
  - Sterile cultures
  - Environmental samples
  - Species with plastic morphology

### Metabarcoding
- High-throughput sequencing of ITS amplicons from environmental samples (soil, water, air)
- Reveals fungal community composition without cultivation
- Can detect rare and unculturable species
- Dramatically increases estimates of fungal diversity
- Reveals that cultivation detects only a fraction of actual diversity

### Environmental Sampling
Soil DNA extraction followed by ITS metabarcoding reveals fungal communities that are:
- Far more diverse than culture-based surveys
- Include many unculturable species
- Include both active and dormant organisms
- Require careful interpretation (DNA persists after organism death)

## Limitations

### Technical Issues
- **DNA extraction:** Humic substances in soil interfere with PCR; require specialized protocols
- **Primer bias:** Some primers preferentially amplify certain fungal groups
- **Copy number variation:** rDNA copy number varies from tens to hundreds among species
- **Intragenomic variation:** Multiple ITS copies within a single genome may differ
- **Chimera formation:** PCR artifacts during amplification

### Biological Issues
- **Cryptic species:** Some morphologically identical species are distinct genetically
- **Species concepts:** DNA barcoding assumes species are genetically distinct, which is not always true
- **Incomplete lineage sorting:** In recently diverged species, ITS may not have sorted
- **Hybridization:** Hybrid species may have conflicting signals
- **No DNA = no detection:** Species absent from reference database cannot be identified

### Interpretation Issues
- **Presence vs. activity:** DNA detection does not confirm the organism is alive or active
- **Quantification:** ITS copy number variation complicates abundance estimates
- **Taxonomic resolution:** ITS may not distinguish closely related species in some groups
- **Database errors:** Misidentified sequences in GenBank can lead to incorrect identifications

## Best Practices

1. **Voucher specimens** for all sequenced material (deposit in herbarium)
2. **Multiple gene regions** for robust identification (ITS + one additional marker)
3. **Use curated databases** (UNITE) rather than raw GenBank
4. **Include negative controls** in PCR to detect contamination
5. **Replicate extractions and PCR** to assess reproducibility
6. **Report sequence accession numbers** in publications
7. **Deposit cultures** in recognized collections when possible
8. **Combine molecular and morphological data** whenever possible

## Complementary Barcoding Regions

When ITS is insufficient:
- **28S rDNA D1/D2:** Better for yeast identification; ~600 nt; 1% divergence = separate species
- **TEF1-alpha (translation elongation factor 1-alpha):** Protein-coding; good for many filamentous fungi
- **RPB1/RPB2 (RNA polymerase subunits):** Excellent for deep phylogenetics
- **beta-tubulin:** Useful for Penicillium, Aspergillus, and other genera
- **mtSSU (mitochondrial small subunit):** Additional phylogenetic marker

## Impact on Fungal Biodiversity Studies

DNA barcoding and metabarcoding have revealed that:
- Cultivation detects only a fraction of actual fungal diversity
- Soil fungal communities are far more complex than previously thought
- Many putatively cosmopolitan species are actually complexes of cryptic species
- Tropical fungal diversity is vastly underestimated
- Fungal endophyte communities are extraordinarily diverse

## See Also

- [[ribosomal-rna-sequencing-yeast-identification]]
- [[fungal-phylogeny-kingdom-classification]]
- [[biodiversity-of-fungi-soil-fungal-communities-agriculture]]
- [[rhizosphere-fungal-community-analysis-rrna-rdna]]
