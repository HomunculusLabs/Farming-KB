---
title: Cannabis Rhizosphere Bulk Soil Similarity Endorhiza Divergence
source: understanding-cultivar-specificity-cannabis-microbiome.md
concepts: [rhizosphere, bulk-soil, endorhiza, beta-diversity, UniFrac, microbiome-dissimilarity]
tags: [microbiology, cannabis, rhizosphere, plant-microbiome, beta-diversity]
created: 2026-05-09
---

# Rhizosphere–Bulk Soil Similarity vs. Endorhiza Divergence in Cannabis

## Overview

One of the most consistently replicated findings across both experiments in Winston et al. (2014) is that the rhizosphere and bulk soil microbiomes are significantly more similar to each other than either is to the [[cannabinoid-concentration-endorhiza-microbiome-correlation-cannabis]].

This pattern holds regardless of the statistical approach, the cultivar tested, or the soil type used.

It provides strong support for the two-tier selection model of plant-microbiome assembly.

## Beta-Diversity Comparisons

### Unweighted UniFrac (Presence/Absence)

When beta distances between sample types were compared using unweighted UniFrac (which captures OTU presence/absence rather than abundance):

- Rhizosphere–bulk soil distances were significantly lower than rhizosphere–endorhiza distances (t = 24.59, p < 0.001)
- Rhizosphere–bulk soil distances were significantly lower than bulk soil–endorhiza distances (t = 25.15, p < 0.001)
- Rhizosphere–endorhiza distances were NOT significantly different from bulk soil–endorhiza distances (t = 22.10, p = 0.109)

This means that from a presence/absence perspective, the endorhiza is approximately equally distant from both the rhizosphere and bulk soil.

The rhizosphere acts as an intermediate but shares roughly the same set of OTUs as the bulk soil, just in somewhat different proportions.

### Weighted UniFrac (Abundance-Aware)

Using weighted UniFrac (which accounts for OTU relative abundance):

- Rhizosphere–bulk soil distances were significantly lower than rhizosphere–endorhiza distances (t = 211.82, p < 0.001)
- Rhizosphere–bulk soil distances were significantly lower than bulk soil–endorhiza distances (t = 211.56, p < 0.001)
- Rhizosphere–endorhiza distances were NOT significantly different from bulk soil–endorhiza distances (t = 22.23, p = 0.078)

The weighted analysis shows an even stronger pattern, with enormously significant t-values reflecting the dramatic restructuring of [[cannabis-cultivar-microbial-community-effects]] abundance that occurs during the transition from soil into plant root tissue.

The contrast between the unweighted and weighted results is itself informative. The [[unifrac-weighted-unweighted-analysis-cannabis-microbiome]] shows that most OTUs are shared across compartments — the community membership is broadly similar. But the weighted analysis reveals that when abundance is considered, the endorhiza stands apart dramatically. The same bacteria are present, but in very different proportions.

## Interpretation Within the Two-Tier Model

The two-tier selection model predicts that:

1. Soil type defines the composition of rhizosphere and root-inhabiting [[cannabis-endorhiza-bacterial-communities]] (Tier 1)
2. Migration from the rhizosphere into plant tissues involves plant genotype-dependent selection of the endorhiza (Tier 2)

The beta-diversity patterns observed here are consistent with this framework.

The rhizosphere remains closely related to the bulk soil because it is primarily shaped by the same edaphic forces: pH, nitrogen, salinity, carbon, water content.

The shift from rhizosphere to endorhiza, however, represents a second filtering event driven by the plant host's genotype and root chemistry. This results in a dramatically restructured community where certain bacterial groups are strongly enriched and others are suppressed.

## Sample Type as a Significant Factor

In the pooled analysis across both experiments, sample type (bulk soil, rhizosphere, endorhiza) was a highly significant factor structuring [[core-endorhiza-bacterial-community-composition-cannabis]] for both:

- Unweighted UniFrac: ADONIS R² = 0.086, p = 0.001
- Weighted UniFrac: ADONIS R² = 0.229, p = 0.001

The higher R² in the weighted analysis indicates that sample type differences are primarily differences in OTU abundance rather than presence/absence.

In other words, most of the same bacterial taxa are present in soil and root environments, but their relative abundances shift dramatically when bacteria colonize root tissue.

This is a critical distinction. It means the endorhiza is not populated by novel or exotic bacteria — it is populated by a subset of the soil community that has been differentially amplified by plant selection pressures.

## First Experiment vs. Second Experiment

### First Experiment (Burmese, BooKoo Kush, Sour Diesel; one soil)

In the first experiment with minimal edaphic variation, rhizosphere samples were NOT significantly different from other sample types using either unweighted (ADONIS: R² = 0.07, p = 0.07) or weighted (ADONIS: R² = 0.09, p = 0.10) UniFrac.

This is likely because the uniform soil reduced the contrast between bulk soil and rhizosphere, making it harder to detect differences at the rhizosphere level.

Endorhiza and bulk soil samples, however, remained significantly distinct from other categories in both analyses, demonstrating that even when soil variation is minimal, the endorhiza is consistently different.

The first experiment thus serves as a conservative test: even with reduced statistical power to detect rhizosphere effects, the endorhiza signal remains robust.

### Second Experiment (White Widow, Maui Wowie; two soils)

With greater edaphic variation, the second experiment showed significant differences for rhizosphere samples against other sample types in both unweighted (ADONIS: R² = 0.05, p = 0.04) and weighted (ADONIS: R² = 0.13, p = 0.001) analyses.

Bulk soil samples showed mixed results (weighted: ADONIS: R² = 0.06, p = 0.054), suggesting that when soil types are more different, even bulk soil communities become distinguishable as a category.

The comparison between experiments underscores the importance of experimental design in microbiome studies. Greater environmental variation increases the statistical power to detect compartment-level differences.

## Practical Applications

The principles and techniques discussed here have wide-ranging applications
across multiple disciplines and contexts. Practitioners and researchers
continue to explore new ways to integrate these concepts into modern practice,
adapting traditional knowledge to contemporary challenges and opportunities.

## Key Considerations

Several important factors influence the effectiveness and outcomes described
in this topic. Understanding these considerations helps practitioners make
informed decisions and avoid common pitfalls. Environmental conditions,
timing, and material selection all play critical roles.

## Historical Context

The historical development of this subject reflects centuries of accumulated
knowledge and practical experience. From traditional methods passed down
through generations to modern scientific approaches, the evolution continues
to inform current best practices and research directions.

## Common Challenges

Practitioners frequently encounter several challenges when working with
these concepts. Climate variability, resource limitations, and knowledge
gaps can all affect outcomes. Addressing these challenges requires patience,
observation, and a willingness to adapt approaches based on results.

## See Also
- [[rhizosphere-bulk-soil-similarity-cannabis-weak-first-tier]]
- [[beta-diversity-distances-bulk-soil-rhizosphere-cannabis-endorhiza]]
- [[cannabis-rhizosphere-bulk-soil-divergence-core-microbiome-conservation]]
- [[cannabis-alpha-diversity-gradient-bulk-soil-rhizosphere-endorhiza]]
- [[det]]
