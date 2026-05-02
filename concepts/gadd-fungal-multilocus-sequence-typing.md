---
title: "Fungal Multilocus Sequence Typing"
tags: [mycology, genotyping, epidemiology, population-genetics, MLST]
date: 2026-04-25
updated: 2026-04-25
sources: [geoffrey-gadd-sarah-c-watkinson-paul-s-dyer-fungi-in-the-environment.md]
---

# Fungal Multilocus Sequence Typing

Multilocus sequence typing (MLST) and multilocus microsatellite typing (MLMT)
have become essential tools for characterizing genetic variation in fungal
populations. Originally developed by the bacterial research community for
molecular epidemiology, these approaches have been adapted for fungi and
revolutionized our understanding of fungal species boundaries, population
structure, biogeography, and the evolution of pathogenicity. By providing
portable, reproducible, and web-accessible genotype data, MLST and MLMT
address many of the limitations of earlier fingerprinting techniques and
complement the phylogenetic approaches described in [[gadd-fungal-species-recognition]].

## Origins and Rationale

The characterization of genetic variation has been central to advances in
medical mycology and phytopathology, driven by the need for effective
molecular epidemiological tools. Earlier methods including VNTRs, MLEE,
RFLPs, RAPDs, and PFGE were typically developed in-house for specific
problems, suffered from poor reproducibility between laboratories, and
produced data that could not be easily shared or re-analyzed. Genotypes
were effectively "fossilized" upon publication.

MLST was developed to address these limitations by meeting four criteria:
(1) 100% reproducibility between laboratories; (2) ability to discriminate
between isolates while remaining stable over time; (3) accurate portrayal of
evolutionary relationships at multiple scales; and (4) portability and
accessibility to the wider research community.

## MLST Methodology

MLST works by directly amplifying, using PCR, a 450 to 500 nucleotide
fragment from each of 7 to 10 housekeeping genes for each isolate. This
fragment length allows complete bidirectional sequencing with a single primer
pair, ensuring that all polymorphisms are scored at least twice. The
resulting ~3,500 nucleotides per isolate represent seven independent samples
of genome-wide genetic variation.

Each unique allele at a particular locus receives a unique integer code. The
concatenated string of integers across all loci defines the allelic profile,
or sequence type (ST), of an isolate. Sequences differing by a single
nucleotide change are assigned different alleles and unique STs. No
weighting schemes are used: a single point mutation carries as much weight
as a recombinational exchange, simplifying analyses while preserving access
to raw sequence data for more nuanced investigations.

## Web-Based Databases

A defining feature of MLST is the centralization of data in web-accessible
databases. STs are held in SQL server relational databases accessible via web
interfaces, primarily at http://www.mlst.org/. This allows laboratories
worldwide to upload and compare their isolates' STs to existing data,
enabling direct comparison across studies. As the database grows, its power
to portray the genetic structure of a species increases. Separate websites
house MLMT schemes at http://www.multilocus.net/.

## MLST Applications in Fungi

The first fungal MLST scheme was developed for Coccidioides immitis by
sequencing five genes (CHS1, pyrG, tcrP, CTS2, and a serine proteinase),
revealing an average 1.4% nucleotide diversity between isolates and
demonstrating two strongly supported clades separated by 11 to 12.8 million
years. This evidence led to the naming of C. posadasii as a new sister
species. The scheme further showed that North and Central American isolates
comprised geographically separated, recombining populations with geography
covarying linearly with genetic distance, indicating low long-distance
spore dispersal.

For [[candida-albicans]], an internationally agreed seven-gene scheme (AAT1a,
ACC1, ADP1, MPIb, SYA1, VPS13, ZWF1b) is hosted at calbicans.mlst.net. With
279 isolates catalogued, 87% represent unique STs, reflecting high genetic
diversity. A Candida glabrata scheme with six genes (FKS, LEU2, NMT1, TRP1,
UGP1, URA3) identified five principal clusters with a geographical component,
though resolution was insufficient for microevolutionary studies, highlighting
the limitation of MLST in genetically depauperate species.

## Multilocus Microsatellite Typing (MLMT)

When nucleotide diversity is too low for MLST discrimination, microsatellite
markers provide the necessary resolution. Microsatellites are short DNA
stretches composed of repeated di-, tri-, tetra-, or pentanucleotide motifs
that accumulate length polymorphisms through strand slippage mispairing
during meiosis. Mutation rates are orders of magnitude higher (10^-4 to 10^-5
per generation) than point mutations (10^-9), generating substantially more
genetic diversity.

MLMT typing is analogous to MLST: a fragment spanning a microsatellite is
PCR-amplified, but instead of sequencing, alleles are scored by size using
high-resolution acrylamide gel or capillary electrophoresis. The composite
string of microsatellite alleles defines the microsatellite type (MT) of an
isolate.

## MLMT Resolving Power

The superior resolution of MLMT is demonstrated by Coccidioides posadasii
from South America. MLST showed all 14 isolates sharing an identical ST,
while a nine-locus MLMT system revealed 10 unique MTs. Similarly, Penicillium
marneffei from Thailand showed only 0.141% sequence diversity across four
genes (seven polymorphic nucleotides in 4,955 bp), rendering MLST useless.
A 21-locus MLMT scheme identified 19 unique MTs among 21 isolates, revealing
eastern and western clades with strong geographical structuring.

## Limitations and Considerations

MLMT data are subject to homoplasy: because of the stepwise mutation model,
identically sized alleles can evolve independently in unrelated lineages.
Microsatellites underestimate deep divergences; in Coccidioides, flanking
sequence genealogies estimated the species split at 12.8 million years while
microsatellites estimated only 760,000 years, an order of magnitude
difference. However, for recently diverged populations (~40,000 years),
both methods gave concordant results.

To compensate for homoplasy, the solution is to use more loci. Fisher and
colleagues used 20 microsatellites for Penicillium marneffei. The combination
of MLST for species-level questions and MLMT for population-level resolution
provides a powerful hierarchical approach to [[fungal-population-genetics]].

## Broader Applications

Beyond medical mycology, extensive multilocus genealogies have been generated
for Histoplasma capsulatum, [[cryptococcus-neoformans]], Batrachochytrium
dendrobatidis, Saccharomyces species, Fusarium species, and lichenized
ascomycetes such as Letharia. These methods are not limited to pathogens and
have enormous potential for addressing questions in [[fungal-biodiversity]],
conservation, and the population ecology of environmental fungi. As genome
sequences become available for more fungal species, MLST schemes will
increasingly be developed, enabling truly global studies of fungal species
and their evolution.

## See Also

- [[fungi-multilocus-sequence-typing-molecular-epidemiology]]
