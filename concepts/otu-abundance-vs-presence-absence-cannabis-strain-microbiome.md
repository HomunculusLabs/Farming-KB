---
title: Otu Abundance Vs Presence Absence Cannabis Strain Microbiome
tags: [microbiome, cannabis, bioinformatics, otu, weighted-unifrac, unweighted-unifrac, strain-specificity]
related: [weighted-vs-unweighted-unifrac-cannabis-strain-microbiome, cannabis-microbiome-unifrac-beta-diversity-analysis, unifrac-weighted-unweighted-analysis-cannabis-microbiome]
source: [understanding-cultivar-specificity-cannabis-microbiome]
created: 2026-05-10
---

## OTU Abundance vs Presence-Absence Analysis: What Drives Cannabis Strain Microbiome Differences

## Overview

A critical methodological insight from the Winston et al. (2014) [[purple-and-color-changing-cannabis-strains]]. The study found that [[cannabis-microbiome-agricultural-implications-and-future-directions]] and for the design of future studies.

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

The consistently lower R² values for [[cannabis-endorhiza-core-microbiome-pseudomonas-rhizobiales]] is truly universal**: Every Cannabis strain sampled harbored members of the same core taxa (Pseudomonas, Cellvibrio, Oxalobacteraceae, Xanthomonadaceae, Actinomycetales, Sphingobacteriales)
2. **Strain-specificity is quantitative, not qualitative**: The Methylophilus enrichment in Bookoo Kush (13% of community) vs. near-absence in Burmese (0.13%) and absence in [[endorhiza-endophytes-root-interior-bacteria]] changes membership slightly and abundance strongly |
| Strain | 71 | 0 | Strain changes abundance only, not membership |

Soil type is by far the strongest driver of both presence-absence and abundance differences, explaining why the two-tier [[cultivar-cannabis-microbiome-two-tier-selection-model]] emphasizes soil as the primary determinant. Sample type (bulk soil, rhizosphere, endorhiza) also affects which taxa are present, likely reflecting the physiological filtering that occurs as bacteria transition from soil into root tissue.

## The Statistical Power Question

An important caveat is that the unweighted analysis for strain might have been underpowered. The g-test for presence-absence differences requires that a taxon be present in some samples and absent in others — if a taxon is present in all samples but at very different abundances (like Methylophilus in Bookoo Kush vs. Sour Diesel), the unweighted test would not detect a difference even though the biological effect is substantial.

However, the dramatic contrast between 71 weighted and 0 unweighted significant OTUs suggests this is not merely a power issue. The absence of any unweighted strain signal, combined with the strong unweighted soil signal (657 OTUs), indicates that strain effects genuinely operate through abundance modulation rather than presence-absence filtering.

## Bioinformatic Pipeline Context

These analyses were performed in QIIME 1.7.0 using:
- OTU picking against the Greengenes database (pre-clustered at 97% identity) with open reference de novo clustering
- Sequence alignment with PyNAST against the Greengenes core set

## Overview

Otu Abundance Vs Presence Absence Cannabis Strain Microbiome represents an important element within sustainable
design and ecological management systems. Its proper understanding
and integration contributes to the resilience and productivity of
designed ecosystems and agricultural systems.

## Key Characteristics

Several defining characteristics distinguish otu abundance vs presence absence cannabis strain microbiome
from related concepts in permaculture and ecological design.
Understanding these traits supports effective implementation
and management across diverse environmental conditions.

## Ecological Context

The ecological relationships involving otu extend
across multiple trophic levels and functional groups.
Soil biology, water cycles, and energy flows all interact
with this element in complex and beneficial ways.

## Practical Applications

Otu Abundance Vs Presence Absence Cannabis Strain Microbiome finds practical application in multiple design contexts.
Permaculture principles guide integration strategies that maximize
beneficial interactions while minimizing external inputs.
Site-specific adaptation ensures relevance to local conditions.

## Management and Implementation

Effective management requires attention to seasonal patterns
and environmental feedback loops. Monitoring outcomes supports
adaptive management strategies that improve results over time.
Integration with complementary elements enhances system function.

## Regional Considerations

Different geographic regions present unique challenges and
opportunities for otu abundance vs presence absence cannabis strain microbiome. Climate adaptation
strategies vary across cultivation zones and latitude ranges.
Local knowledge and site observation remain essential guides.

## Sustainability

Sustainable management practices ensure long-term viability.
Biodiversity considerations guide implementation decisions.
Responsible stewardship maintains ecological health over time.
Economic sustainability balances environmental and social needs.

## Research and Development

Ongoing research continues to expand understanding of
otu abundance vs presence absence cannabis strain microbiome and its applications. Active investigation
areas include ecological interactions and optimization.
Published findings contribute to an evolving evidence base.

## Historical Context

Otu Abundance Vs Presence Absence Cannabis Strain Microbiome has been recognized across multiple knowledge traditions.
Indigenous and traditional practices have informed modern approaches.
The synthesis of historical and contemporary knowledge enriches
current understanding and implementation strategies.

## Integration Strategies

Successful integration of otu abundance vs presence absence cannabis strain microbiome into broader
systems requires careful planning and observation.
Design for multiple functions increases overall efficiency.
Monitoring integration outcomes supports adaptive management.

## Challenges and Solutions

Common challenges include environmental variability, resource
constraints, and knowledge gaps. Diversified approaches and
proactive planning mitigate potential problems effectively.
Knowledge sharing among practitioners accelerates solutions.

## See Also

- [[biodiversity-fungal-species-abundance-diversity]]
- [[cannabis-microbiome-otu-abundance-vs-presence-cannabis-strains]]
- [[gadd-saprotrophic-fungi-15n-13c-natural-abundance-isotopes]]
- [[soil-type-otu-abundance-vs-strain-structure-cannabis-microbiome]]
- [[strain-otu-presence-absence-vs-abundance-cannabis-microbiome]]
