---
title: Soil Type cannabis-microbiome-otu-abundance-vs-presence-cannabis-strains vs Strain Community Structure in cultivar-cannabis-microbiome-two-tier-selection-model
created: 2026-05-08
tags: [microbiology, cannabis, microbiome, soil-science, otu-analysis, plant-microbe-interactions, community-ecology, endorhiza]
date: 2026-05-08
---

# Soil Type OTU Abundance vs Strain Community Structure in Cannabis Microbiome

## Overview

In the study of the Cannabis microbiome across five cultivars and multiple soil
types (Winston et al., 2014), a critical distinction emerged between the factors
that govern operational taxonomic unit (OTU) **presence/absence** versus those
that govern OTU **abundance**. This distinction has profound implications for
understanding how plant-microbiome interactions are assembled and maintained.

## The Two-Tier Selection Framework

The two-tier [[two-tier-selection-model-plant-microbiome]] predicts that edaphic (soil) factors determine
the broad composition of available microbial taxa in bulk soil, while host
genotype (cultivar/strain) fine-tunes the community that actually colonizes
the endorhiza. This model was tested by analyzing OTU distributions across
multiple Cannabis strains grown in different soil types.

## Unweighted vs Weighted UniFrac Results

The study employed both unweighted (presence/absence-based) and weighted
(abundance-based) UniFrac distance metrics to dissect community structure:

### Unweighted Analysis (Composition)
- Soil type produced 657 significant OTU differences
- Sample type (bulk soil, rhizosphere, endorhiza) produced 11 significant
  OTU differences
- **Strain produced zero significant OTU differences**

This result was striking: when considering only which taxa were present or
absent (binary membership), Cannabis strain had no statistically detectable
effect. The microbial membership of communities was overwhelmingly determined
by soil type and compartment (soil vs. rhizosphere vs. endorhiza).

### Weighted Analysis (Abundance)
- Soil type produced 690 significant OTU differences
- Sample type produced 51 significant OTU differences
- **Strain produced 71 significant OTU differences**

When relative abundance was considered, strain effects became significant.
This means that while Cannabis cultivars draw from the same pool of soil-
available taxa, they differ substantially in the proportions of those taxa
they support or enrich within the endorhiza.

## Interpretation: Membership vs Proportion

The divergent results between unweighted and weighted analyses reveal that:

1. **All available taxa are accessible to all cultivars.** The soil provides a
   shared species pool, and no cultivar uniquely recruits taxa that others
   cannot access.

2. **Cultivar identity acts as an abundance filter.** Each strain selectively
   enriches certain taxa from the shared pool through differential root
   exudation, immune responses, or metabolic compatibility.

3. **Soil type remains the dominant factor overall.** Even in the weighted
   analysis, soil type produced roughly 10x more significant OTU differences
   than strain (690 vs. 71).

## Methylophilus as a Strain-Specific Marker

The most dramatic strain-specific abundance difference was the enrichment of
*Pseudomonas* in one cultivar's endorhiza versus its near-absence in another.
One OTU of *Methylophilus* comprised 13% of the [[edaphic-factors-microbial-community-structure]] in the
Bookoo Kush endorhiza, only 0.13% in Burmese, and was entirely absent from
Sour Diesel. This extreme enrichment illustrates how strain-level differences
can produce large shifts in community proportions even when the underlying
taxonomic membership is similar.

## Phylogenetic Composition of Strain-Level Differences

The 71 OTUs showing significant strain-level abundance differences were
predominantly Proteobacteria, specifically from the orders:
- *Pseudomonadales*
- *Burkholderiales*
- *Sphingomonadales*
- *Rhizobiales*

Bacteroidetes from the orders *Sphingobacteriales* and *Flavobacteriales*
also contributed to strain differentiation. Notably, *Sphingomonas wittichii*
was prevalent in the Maui Wowie strain and has been implicated in increased
survival in soil environments through its ability to metabolize phenazine-1-
carboxylic acid.

## Implications for Agricultural Practice

These findings suggest that:
- Soil selection has the largest single effect on the microbial community
  available to Cannabis roots
- Cultivar choice fine-tunes which of those available organisms thrive
- Breeding for specific microbial associations would need to focus on
  [[amf-biocontrol-phytophthora-root-exudate-modification]] profiles that selectively enrich beneficial taxa
- Soil amendment strategies can shift the available species pool more
  dramatically than cultivar selection alone

## Methodological Considerations

The use of paired unweighted and weighted UniFrac analyses is essential for
distinguishing between compositional and structural effects in microbiome
studies. A study relying on only one metric would miss half the picture.
The 16S rRNA V4 region sequencing approach (via the Earth Microbiome
Project standard pipeline) provided adequate resolution for genus-level
differentiation, though strain-level functional differences within genera
remain an open question.

## Broader Relevance

This pattern — where environment governs community membership and host
genotype governs relative abundance — has been observed in other plant
species including Arabidopsis, maize, and rice, suggesting it may be a
general principle of plant-microbiome assembly rather than a Cannabis-
specific phenomenon.

## See Also

- [[two-tier-selection-model-plant-microbiome]]
- [[cannabis-endorhiza-microbiome]]
- [[alpha-beta-diversity-cannabis-root-microbiomes]]
- [[cannabis-endorhiza-shared-otu-soil-source-validation]]
- [[edaphic-determinants-cannabis-microbiome-community-structure]]

## Source

- Winston ME, Hampton-Marcell J, Zarraonaindia I, et al. Understanding
  Cultivar-Specificity and Soil Determinants of the Cannabis Microbiome.
  *PLoS ONE* 9(6): e99641, 2014.
