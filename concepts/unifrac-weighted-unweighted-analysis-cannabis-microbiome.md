---
title: UniFrac Weighted vs Unweighted Analysis in Cannabis Microbiome
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
determines microbial community composition (which taxa are present), while
cultivar determines community structure (how abundant each taxon is). Without
examining both metrics, this critical insight would have been missed entirely.

## What Are Weighted and Unweighted UniFrac?

UniFrac is a phylogenetic distance metric developed by Lozupone and Knight
(2005) that measures dissimilarity between microbial communities based on
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

The second experiment — White Widow and Maui Wowie in two distinct soil types
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

### Weighted UniFrac Results (Abundance)

The pattern inverted. PC1 explained 34.51% of variance, dominated by strain.
PC2 explained 25.41% (sample type). PC3 explained 19.31%. ADONIS: soil type
R² = 0.21 (p = 0.001), sample type R² = 0.27 (p = 0.001), strain R² = 0.27
(p = 0.001). Strain now matched sample type in explanatory power.

For individual OTUs, weighted ANOVA identified **690 significant OTUs by soil
type**, **51 by sample type**, and **71 by strain**. The same taxa present
across cultivars (zero unweighted differences) had significantly different
relative abundances, driven by host genotype-dependent selection.

## Consistency Across Experiments and Pooled Analysis

When both experiments were pooled (five cultivars, three soil types), the
pattern held. Unweighted UniFrac: soil type R² = 0.196, sample type R² =
0.086, strain R² = 0.178 (all p = 0.001). Weighted UniFrac: soil type
R² = 0.323, sample type R² = 0.229, strain R² = 0.301 (all p = 0.001). The
The increased strain effect in pooled weighted analysis reflects broader cultivar variation from combining five cultivars.

In Experiment 1 (post-harvest), strain was not significant across all samples
(unweighted R² = 0.11, p = 0.15; weighted R² = 0.11, p = 0.25). However,
endorhiza-only analysis showed significance for both weighted (R² = 0.59,
p = 0.004) and unweighted (R² = 0.39, p = 0.003), suggesting post-harvest
root decay had diminished the rhizosphere cultivar signal.

## Endorhiza Distinctiveness and Rhizosphere Inconsistency

Both metrics consistently showed endorhiza forming distinct clusters. In
Experiment 1, endorhiza was significantly different under both unweighted
(ADONIS: R² = 0.26, p = 0.001) and weighted (R² = 0.59, p = 0.001). The much
higher weighted R² indicates dramatically different abundance profiles in the
endorhiza, consistent with strong host genotype filtering.

Rhizosphere showed inconsistent significance: not significant in Experiment 1
(post-harvest: unweighted p = 0.07, weighted p = 0.10) but significant in
Experiment 2 (pre-harvest: weighted R² = 0.13, p = 0.001; unweighted R² =
0.05, p = 0.04). This difference is attributable to post-harvest root decay
in Experiment 1 masking the rhizosphere cultivar signal, as discussed in the
sampling timing analysis.

## Implications for Interpreting Beta-Diversity Studies

The findings carry several critical methodological implications. First, single-
metric studies are incomplete — using only unweighted UniFrac would miss the
cultivar effect entirely; using only weighted would understate soil composition
effects. Second, OTU-level tests provide essential mechanistic context: the
zero versus 71 significant OTUs by strain explains the PCoA pattern in a way
distance-based statistics alone cannot. Third, the two-tier selection model is
only fully visible when both metrics are examined in parallel — soil determines
composition, cultivar determines structure. Fourth, the pattern is robust to
sequencing effort despite different rarification depths (3,000 vs 45,000).

## Related Concepts
- [[cannabis-microbiome-two-tier-selection]] — The two-tier selection model for plant microbiomes
- [[cannabis-microbiome-soil-type-composition-strain-structure]] — Soil composition vs strain structure
- [[alpha-beta-diversity-cannabis-root-microbiomes]] — Alpha and beta diversity across root compartments
- [[16s-rrna-sequencing-microbiome-analysis]] — 16S rRNA sequencing methodology
- [[edaphic-factors-structuring-cannabis-microbiome]] — Edaphic factors and community structure
