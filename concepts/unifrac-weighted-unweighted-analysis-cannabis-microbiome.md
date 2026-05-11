---
title: Unifrac Weighted Unweighted Analysis Cannabis Microbiome
created: 2026-05-10
updated: 2026-05-10
type: concept
tags:
  - cannabis
  - microbes
  - microbiome
  - beta-diversity
  - unifrac
  - soil-science
  - research-methods
sources:
  - raw/papers/understanding-cultivar-specificity-cannabis-microbiome.md
---

# UniFrac Weighted vs Unweighted Analysis in Cannabis Microbiome

The application of both weighted and unweighted UniFrac distance metrics in
Winston et al. (2014) revealed fundamentally different patterns in the Cannabis
microbiome, with each metric capturing a distinct ecological dimension. This
dual-metric approach was central to the study's key finding: that soil type
determines microbial [[core-endorhiza-bacterial-community-composition-cannabis]] (which taxa are present), while
cultivar determines [[edaphic-determinants-cannabis-microbiome-community-structure]] (how abundant each taxon is). Without
examining both metrics, this critical insight would have been missed entirely.

## What Are Weighted and Unweighted UniFrac?

UniFrac is a phylogenetic distance metric developed by Lozupone and Knight
(2005) that measures dissimilarity between [[cannabis-rhizosphere-microbial-communities]] based on
branch lengths unique to one community or shared between them. The two variants
differ fundamentally in how they handle taxon abundance.

**Unweighted UniFrac** considers only the presence or absence of lineages,
measuring the fraction of branch lengths leading to descendants found in only
one of two communities. It ignores abundance entirely and is sensitive to rare
taxa — it asks "which microbes are here versus there?" Communities sharing the
same taxa at different abundances appear similar under this metric.

**Weighted UniFrac** incorporates relative abundance, weighting each branch by
the difference in proportional abundance of descendant taxa between communities.
It is dominated by abundant taxa — it asks "how much of each microbe is here
versus there?" Communities with the same taxa but different dominant organisms
appear very different.

When unweighted distances are large but weighted distances are small, it
suggests compositional turnover with similar abundance structure. When weighted
distances are large but unweighted are small, the same taxa are present but in
very different proportions — the community "ingredients" are the same but the
"recipe" differs.

## Bioinformatics Methodology

All analysis was performed using QIIME 1.7.0 (Caporaso et al., 2010). The V4
region of the 16S rRNA gene was amplified using the Earth Microbiome Project
standard pipeline (Caporaso et al., 2012) with primers 515F and 806R
Golay-barcoded reverse primers, producing a 291 bp amplicon. PCR conditions:
94°C for 3 min, then 35 cycles of 94°C/45s, 50°C/60s, 72°C/90s, with final
extension of 10 min at 72°C. PCR was triplicated and products pooled.

OTUs were picked against the Greengenes database (McDonald et al., 2012)
pre-clustered at 97% identity using an open-reference approach. Sequences not
matching the reference were clustered de novo. Representative sequences were
aligned with PyNAST; unaligned sequences were discarded. A phylogenetic tree
was built using FastTree (Price et al., 2009). Taxonomy was assigned using the
RDP classifier (Wang et al., 2007) retrained on Greengenes.

Samples from Experiment 1 were rarified to 3,000 sequences; Experiment 2 to
45,000 sequences. Significance tests used compare_categories.py in QIIME with
ADONIS, ANOSIM, ANOVA, and RDA. Individual OTU analyses used g-tests
(unweighted) and ANOVA (weighted), both with FDR correction.

## Experiment 2: The Critical Divergence Between Metrics

The second experiment — [[soil-heritability-otu-sharing-white-widow-cross-soil-cannabis-endorhiza]] and Maui Wowie in two distinct soil types
(Mo-Bio and Orange County) — produced the clearest illustration of the
weighted versus unweighted divergence.

### Unweighted UniFrac Results (Presence/Absence)

PC1 explained 32.06% of variance, dominated by soil type. PC2 explained 11.34%
(sample type gradient: bulk soil → rhizosphere → endorhiza). PC3 explained
5.67% of variance. ADONIS: soil type R² = 0.32 (p = 0.001), sample type
R² = 0.12 (p = 0.005), strain R² = 0.10 (p = 0.008).

For individual OTUs, the unweighted g-test identified **657 significant OTUs by
soil type**, **11 by sample type**, and **zero by strain**. Cultivar had no
detectable effect on OTU presence or absence — the same taxa were found in
both cultivars' roots when grown in the same soil.
