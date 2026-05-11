---
title: Symbiotic Fungi Rrna Versus Rdna Fungal Community Analysis
source: symbiotic-fungi.md
source_author: Ari Jumpponen, in Varma & Kharkwal (eds.)
extracted: 2026-05-10
tags: [molecular-ecology, rRNA, rDNA, fungal-community, rhizosphere, PCR, metagenomics, symbiotic-fungi]
---

# rRNA Versus rDNA for Fungal Community Analysis in the Rhizosphere

## The Fundamental Distinction

Two major molecular approaches exist for characterizing fungal communities in
environmental samples: targeting ribosomal DNA (rDNA) and targeting ribosomal RNA
(rRNA). Both target the ribosomal operon, but they reveal fundamentally different
information about the microbial community. rDNA-based assays detect organisms that
are present — including dormant, dead, or relic DNA — while rRNA-based assays
detect organisms that are metabolically active at the time of sampling.

This distinction has profound implications for ecological interpretation. An rDNA
survey may reveal hundreds of fungal taxa in a soil sample, but many of those
organisms may be present only as dormant spores or residual extracellular DNA.
An rRNA survey of the same sample reveals the subset of those organisms that are
actively growing, respiring, and participating [[fungi-in-ecosystem-processes-dighton]] at that
moment.

## Why the Ribosomal Operon?

The fungal rDNA is arranged in tandem repeats in multiple copies per genome. Each
repeat contains both coding regions for the primary rRNAs (18S, 5.8S, 28S in the
large subunit; 18S is also called SSU or small subunit) and non-coding internal
transcribed spacer (ITS) regions with varying levels of sequence conservation.
The ITS region has been adopted as the standard barcode for fungal identification,
while the 18S region is useful for broader phylogenetic placement.

The multi-copy nature of rDNA provides high sensitivity — even organisms present
in low abundance can be detected because each cell contributes multiple template
copies for PCR amplification. However, this same feature complicates quantitative
interpretation, as copy number varies among taxa.

## Limitations of rDNA-Based Surveys

rDNA persists in environmental DNA pools for organisms that maintain no metabolic
activity. Environmental DNA can include:

- DNA from dead organisms (necromass)
- Extracellular DNA adsorbed to soil particles
- DNA from dormant spores [[fungal-sclerotia-and-resting-structures]]
- DNA from organisms that were once active but are no longer contributing to
  ecosystem function

This creates a fundamental difficulty: rDNA assays conflate historical and
contemporary community composition. The detected diversity may substantially
overestimate the number of functionally important taxa. This is particularly
problematic in soils, where DNA adsorption to clay minerals and organic matter
can preserve genetic material for weeks, months, or even years.

## Advantages of rRNA-Based Approaches

Ribosomal RNA is less stable than rDNA in the environment. RNA degrades rapidly
upon cell death, and metabolically active organisms maintain higher numbers of
rRNA molecules (or transcribe rRNA precursors at higher rates). By extracting and
reverse-transcribing rRNA directly from environmental samples, researchers can:

- Target the metabolically active fraction of the community
- Avoid signal from relic DNA and dead organisms
- Obtain a snapshot of real-time community function
- Reduce the apparent diversity to functionally relevant taxa

The underlying assumptions are that rRNA turns over more rapidly than rDNA and
that active organisms maintain elevated rRNA levels relative to inactive ones.

## Methodology: rRNA Extraction and Analysis

The workflow for rRNA-based community analysis follows these steps:

1. **Sample collection with immediate preservation** — flash-freezing in liquid
   nitrogen is critical to prevent RNA degradation. Samples must be kept at -80°C
   until extraction.
2. **RNA extraction** — using commercial kits designed for soil (e.g., FastRNA
   Pro Soil-Direct kit). Nuclease-free consumables and work surfaces are essential.
3. **Reverse transcription** — converting rRNA to cDNA using a reverse
   transcriptase with the NS8 primer (near the 3' end of the SSU rRNA).
4. **PCR amplification** — using fungal-specific primers targeting an ~760bp
   region within the SSU rRNA gene.
5. **Cloning and sequencing** — cloning PCR products and sequencing individual
   clones to generate community profiles.

A parallel rDNA extraction from the same samples allows direct comparison between
the DNA-detected and RNA-detected communities.

## Key Findings from Comparative Studies

Studies comparing rRNA and rDNA communities from the same samples have found:

- **rDNA communities are more species-rich** — they include dormant and relic
  taxa not detected in rRNA surveys
- **rRNA communities are a subset of rDNA communities** — all active taxa are
  also present in the DNA pool, but not vice versa
- **Community composition differs** — the relative abundance of taxa shifts
  substantially between rDNA and rRNA profiles
- **Dominant taxa may differ** — a species abundant in rDNA may be rare in rRNA
  if it is predominantly dormant

In tallgrass prairie rhizosphere samples (Jumpponen's study system at Konza
Prairie Biological Station, Kansas), the fungal communities detected by rRNA
represented a subset of those found by rDNA, confirming the hypothesis that
DNA-based surveys overestimate active diversity.

## The Konza Prairie Study System

The comparative study was conducted in the rhizosphere of *[[andropogon-gerardii]]*
(big bluestem) at the Konza Prairie LTER site in eastern Kansas. This native
tallgrass prairie is dominated by big bluestem, Indiangrass (*Sorghastrum
nutans*), little bluestem (*[[schizachyrium-scoparium]]*), and switchgrass (*Panicum
virgatum*). The site represents tallgrass prairie under a frequent fire cycle,
providing a well-characterized ecological context for community analysis.

## Practical Considerations

rRNA work is technically more demanding than rDNA work:

- RNA degrades rapidly; samples must be preserved immediately
- RNase contamination is a constant concern (use RNase-free consumables)
- Reverse transcription adds complexity and potential for bias
- Yields are typically lower than DNA extraction
- Replicates are essential due to higher technical variability

Despite these challenges, the ecological insight gained from distinguishing active
from relic community members justifies the additional effort, particularly in
studies where functional interpretation is the primary goal.

## Implications for Symbiotic Fungi Research

For mycorrhizal research, the rRNA/rDNA distinction is particularly relevant.
[[arbuscular-mycorrhizal-fungi]] (AMF) form intraradical hyphae and arbuscules that
may persist in root tissue after metabolic activity ceases. rDNA surveys of roots
may detect AMF species that are no longer actively exchanging nutrients with the
host plant, while rRNA surveys reveal the truly functional symbiotic partnerships.

## See Also

- [[rhizosphere-fungal-community-analysis-rrna-rdna]]
- [[symbiotic-fungi-arbuscular-mycorrhizal-mechanisms]]
- [[arbuscular-mycorrhizal-fungal-diversity-patterns-distribution]]
- [[arbuscular-mycorrhizal-fungi-biology-symbiosis]]
