---
title: Ribosomal RNA Sequencing for Yeast and Fungal Identification
created: 2026-04-21
updated: 2026-04-21
type: concept
tags: [reference]
sources: []
---

# Ribosomal RNA Sequencing for Yeast and Fungal Identification

Ribosomal RNA (rRNA) and ribosomal DNA (rDNA) sequence comparisons have become the gold standard for fungal identification and phylogenetic analysis. The multi-copy nature of rDNA and its combination of conserved and variable regions make it ideal for comparisons across different taxonomic levels.

## Ribosomal RNA Gene Structure

The fungal rDNA repeat unit contains:
- **18S (small subunit) rRNA gene:** ~1,800 nucleotides; conserved; for broad phylogenetic placement
- **ITS1 (internal transcribed spacer 1):** Variable; useful for species-level discrimination
- **5.8S rRNA gene:** ~160 nucleotides; contains modified nucleotides
- **ITS2 (internal transcribed spacer 2):** Variable; useful for species-level discrimination
- **26S (large subunit) rRNA gene:** ~3,400 nucleotides; contains variable domains (D1-D12)
- **5S rRNA gene:** ~120 nucleotides; limited phylogenetic information

## rRNA/rDNA Comparison Methods

### DNA Reassociation
- Total genomic DNA from two species is denatured and allowed to reassociate
- Degree of reassociation (measured spectrophotometrically) indicates relatedness
- Limited to closely related species (75-80% similarity required for duplexing)
- Labor-intensive for many species pairs

### Direct rRNA Sequencing
- Enzymatic sequencing of purified rRNA molecules
- 5S rRNA was first used (1970s-1980s)
- Replaced by 18S and 26S rRNA sequencing which provide more information

### Restriction Fragment Length Polymorphisms (RFLPs)
- rDNA occurs in multiple copies — amenable to RFLP analysis
- Used for medically important yeasts (Candida species identification)
- Can distinguish closely related species

### Direct rDNA Sequencing
- PCR amplification followed by sequencing
- Now the standard approach
- Rapid and reliable

## Key Domains for Identification

### 26S rDNA D1/D2 Domains (~600 nucleotides)
The most widely used region for yeast identification:
- Sufficiently variable to recognize individual ascomycetous and basidiomycetous yeast species
- **1% or greater nucleotide substitution = separate species** (ascomycetous yeasts)
- Conspecific strains: 0-1% divergence
- Distantly related species: up to 47% substitution
- Kurtzman and Robnett (1998) sequenced D1/D2 for ~500 ascomycetous yeast species
- Fell et al. (2000) sequenced D1/D2 for 230 basidiomycetous yeast species in 42 genera

### 18S rRNA (~1,800 nucleotides)
- More conserved than D1/D2
- Useful for higher-level phylogenetic placement (order, class, phylum)
- Less resolving power at species level
- Best for distant phylogenetic relationships

### ITS Regions (ITS1 + ITS2)
- Most variable regions of the rDNA repeat
- Standard DNA barcode for fungi (ITS is the official fungal barcode)
- Excellent for species-level discrimination
- May over-split species in some groups
- Universal primers available (ITS1, ITS4, ITS5)

## Major Phylogenetic Findings from rRNA/rDNA

### Ascomycetous Yeasts
- **Yeasts form a monophyletic clade** distinct from euascomycetes (filamentous fungi)
- **Schizosaccharomyces** is phylogenetically distant from both budding yeasts and euascomycetes (separate order: Schizosaccharomycetales)
- **Taphrina, Protomyces, Saitoella:** Form a divergent clade basal to the yeast-euascomycete branch
- **Eremascus:** Aligned with euascomycetes despite lacking a fruiting body
- **Ascospore morphology is a poor phylogenetic indicator**
- **Budding vs. fission reproduction** does not define monophyletic groups
- **Saccharomyces bayanus/pastorianus:** Partial amphidiploid from hybridization

### Basidiomycetous Yeasts
- Fall into three classes: Ustilaginomycetes, Urediniomycetes, Hymenomycetes
- Teliosporic and nonteliosporic taxa found in each class
- Carotenoids and ballistoconidia — previously considered phylogenetically informative — found in all three classes
- D1/D2 domain distinguishes most closely related species but insufficient for basal relationships

### Limitations
- Some sibling species pairs show unexpectedly low divergence (e.g., Williopsis saturnus varieties: 43% nuclear DNA relatedness but 0% D2 divergence)
- Amphidiploidy can mask divergence (hybrid species retain one parent's rDNA)
- Phenotypic characters often poor indicators of phylogenetic relationships

## Reliability of Phylogenies

rRNA gene trees may not accurately reflect species trees because:
- rDNA is multi-copy (intra-genomic variation possible)
- Concerted evolution may homogenize paralogous copies
- Different rRNA regions evolve at different rates
- Long-branch attraction can group fast-evolving taxa together

## Practical Guidelines
1. Sequence D1/D2 for species-level identification of yeasts
2. Sequence ITS for general fungal barcoding
3. Sequence 18S for higher-level phylogenetic placement
4. Use multiple gene regions for robust phylogenetic analysis
5. Compare sequences against curated databases (GenBank, UNITE)

## See Also

- [[dna-barcoding-fungal-identification]]
- [[fungal-phylogeny-kingdom-classification]]
- [[pcr-methods-fungal-identification-monitoring]]
- [[yeast-biodiversity-isolation-ecology]]
- [[rhizosphere-fungal-community-analysis-rrna-rdna]]
- [[fungal-rdna-primers-molecular-identification]]
- [[rhizosphere-fungal-community-analysis-rrna-rdna]]
- [[fungal-kingdom-classification]]
