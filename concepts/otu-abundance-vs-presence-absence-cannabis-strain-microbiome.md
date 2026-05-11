---
title: Otu Abundance Vs Presence Absence Cannabis Strain Microbiome
tags: [microbiome, cannabis, bioinformatics, otu, weighted-unifrac, unweighted-unifrac, strain-specificity]
related: [weighted-vs-unweighted-unifrac-cannabis-strain-microbiome, cannabis-microbiome-unifrac-beta-diversity-analysis, unifrac-weighted-unweighted-analysis-cannabis-microbiome]
source: [understanding-cultivar-specificity-cannabis-microbiome]
created: 2026-05-10
---

# OTU Abundance vs Presence-Absence Analysis: What Drives Cannabis Strain Microbiome Differences

## Overview

A critical methodological insight from the Winston et al. (2014) [[winston-cannabis-microbiome-study-design]] is the distinction between OTU (Operational Taxonomic Unit) abundance differences and presence-absence differences across [[purple-and-color-changing-cannabis-strains]]. The study found that [[cannabis-cultivar-effects-soil-microbiome]] identity had a strong effect on the relative abundance of microbial taxa but zero significant effect on which taxa were present or absent. This finding has profound implications for understanding the nature of cultivar-specificity in the [[cannabis-microbiome-agricultural-implications-and-future-directions]] and for the design of future studies.

## Weighted vs Unweighted UniFrac: The Analytical Framework

### Weighted UniFrac (Abundance-Sensitive)
Weighted UniFrac calculates phylogenetic distances between communities while accounting for the relative abundance of each lineage. It asks: "Given the evolutionary relationships between taxa, how different are two communities when we consider both what is there AND how much of each is there?"

In the Cannabis study, weighted UniFrac detected highly significant strain-level differences:
- First experiment: ADONIS R² = 0.59, p = 0.004 (endorhiza by strain)
- Pooled experiments: ADONIS R² = 0.301, p = 0.001 (all samples by strain)

### Unweighted UniFrac (Presence-Absence Only)
Unweighted UniFrac calculates phylogenetic distances based only on which lineages are present, ignoring their abundances. It asks: "Given the evolutionary relationships between taxa, how different are two communities in terms of which lineages are present, regardless of how abundant each one is?"

In the Cannabis study, unweighted UniFrac also detected strain differences but with weaker effect sizes:
- First experiment: ADONIS R² = 0.39, p = 0.003 (endorhiza by strain)
- Pooled experiments: ADONIS R² = 0.178, p = 0.001 (all samples by strain)

The consistently lower R² values for [[unifrac-weighted-unweighted-analysis-cannabis-microbiome]] indicate that strain-specificity is driven more by shifts in abundance than by presence-absence changes.

## OTU-Level Statistical Tests

### Individual OTU Analysis: Two Approaches

The study tested each individual OTU for significant differences using two complementary statistical approaches:

#### Weighted Analysis: ANOVA
Analysis of variance (ANOVA) tests whether the mean abundance of each OTU differs between groups. This is sensitive to changes in how much of each taxon is present.

**Results for strain effect:**
- 71 OTUs showed significant abundance differences between Cannabis strains (FDR-corrected)
- These were composed mostly of differences in Proteobacteria: Pseudomonadales, Burkholderiales, Sphingomonadales, and Rhizobiales
- Bacteroidetes orders Sphingobacteriales and Flavobacteriales also contributed

#### Unweighted Analysis: G-Test
The G-test (likelihood ratio test) evaluates whether the presence or absence of each OTU differs between groups, without considering how abundant it is when present.

**Results for strain effect:**
- Zero (0) OTUs showed significant presence-absence differences between Cannabis strains
- This is the critical finding: no individual taxon was completely present in one strain and absent in another

## What This Means: Cultivar-Specificity Is About Proportions, Not Membership

The combination of 71 significant weighted OTUs and 0 significant unweighted OTUs for the strain factor tells us something fundamental about Cannabis microbiome cultivar-specificity:

### The "Shared Pool, Different Proportions" Model

All Cannabis cultivars share the same basic pool of microbial taxa — the same species are available in the soil and capable of colonizing roots. What differs between cultivars is the relative abundance of these shared taxa. Each cultivar acts as a "volume knob" that turns some taxa up and others down, rather than a "selector" that admits some taxa and excludes others.

This has several implications:

1. **[[cannabis-endorhiza-core-microbiome-pseudomonas-rhizobiales]] is truly universal**: Every Cannabis strain sampled harbored members of the same core taxa (Pseudomonas, Cellvibrio, Oxalobacteraceae, Xanthomonadaceae, Actinomycetales, Sphingobacteriales)
2. **Strain-specificity is quantitative, not qualitative**: The Methylophilus enrichment in Bookoo Kush (13% of community) vs. near-absence in Burmese (0.13%) and absence in [[cannabis-sour-diesel]] is a difference of degree, not kind — the potential for Methylophilus colonization exists in all strains, but Bookoo Kush creates conditions where it thrives
3. **No "private" taxa**: No microbial taxon was found exclusively in one Cannabis cultivar — there are no strain-specific "signature" species in the presence-absence sense

## Contrast with Soil Type and Sample Type Effects

The strain effect (abundance-only) contrasts sharply with the effects of soil type and sample type:

| Factor | Significant Weighted OTUs | Significant Unweighted OTUs | Interpretation |
|--------|--------------------------|----------------------------|----------------|
| Soil Type | 690 | 657 | Soil changes both WHAT is there and HOW MUCH |
| Sample Type | 51 | 11 | [[endorhiza-endophytes-root-interior-bacteria]] changes membership slightly and abundance strongly |
| Strain | 71 | 0 | Strain changes abundance only, not membership |

Soil type is by far the strongest driver of both presence-absence and abundance differences, explaining why the two-tier [[cultivar-cannabis-microbiome-two-tier-selection-model]] emphasizes soil as the primary determinant. Sample type (bulk soil, rhizosphere, endorhiza) also affects which taxa are present, likely reflecting the physiological filtering that occurs as bacteria transition from soil into root tissue.

## The Statistical Power Question

An important caveat is that the unweighted analysis for strain might have been underpowered. The g-test for presence-absence differences requires that a taxon be present in some samples and absent in others — if a taxon is present in all samples but at very different abundances (like Methylophilus in Bookoo Kush vs. Sour Diesel), the unweighted test would not detect a difference even though the biological effect is substantial.

However, the dramatic contrast between 71 weighted and 0 unweighted significant OTUs suggests this is not merely a power issue. The absence of any unweighted strain signal, combined with the strong unweighted soil signal (657 OTUs), indicates that strain effects genuinely operate through abundance modulation rather than presence-absence filtering.

## Bioinformatic Pipeline Context

These analyses were performed in QIIME 1.7.0 using:
- OTU picking against the Greengenes database (pre-clustered at 97% identity) with open reference de novo clustering
- Sequence alignment with PyNAST against the Greengenes core set
