---
title: Cannabis Rhizosphere and Soil Microbiome Structure
source: understanding-cultivar-specificity-cannabis-microbiome.md
type: concept
---

# Cannabis Rhizosphere and Soil Microbiome Structure

> Source: Winston et al. 2014, PLoS ONE 9(6):e99641 — Experiment 2 and pooled analyses.

## Overview

The Cannabis root–soil microbiome exhibits a structured gradient from bulk soil through the [[rhizosphere]] to the endorhiza (root interior). [[core-endorhiza-bacterial-community-composition-cannabis]] is shaped by a hierarchy of factors: **soil type** is the dominant determinant, followed by **cultivar (strain)** and **sample compartment** (bulk soil vs. rhizosphere vs. endorhiza). These patterns emerge consistently across both weighted and [[weighted-unweighted-unifrac-discrepancy-cannabis-cultivar]] distance metrics, though the relative contributions shift depending on whether abundance-weighted or presence/absence-based distances are considered.

## Beta-Diversity Patterns

### Experiment 2 (Unweighted UniFrac)

Unweighted UniFrac captures phylogenetic turnover based on OTU presence/absence. In Experiment 2, ADONIS permutation tests revealed:

| Factor | R² | p-value |
|--------|----|---------|
| Soil type | 0.32 | 0.001 |
| Sample type | 0.12 | 0.005 |
| Strain | 0.10 | 0.008 |
| Bulk soil (alone) | 0.04 | 0.12 (n.s.) |

The endorhiza and rhizosphere communities were significantly distinct from one another, while bulk soil alone did not explain a significant portion of variation — indicating that the rhizosphere and endorhiza compartments drive most of the sample-type signal.

### Experiment 2 (Weighted UniFrac)

Weighted UniFrac incorporates OTU abundances, revealing a different balance of effects:

| Factor | R² | p-value |
|--------|----|---------|
| Soil type | 0.21 | 0.001 |
| Sample type | 0.27 | 0.001 |
| Strain | 0.27 | 0.001 |
| Bulk soil (alone) | — | 0.054 (borderline) |

Under the abundance-weighted metric, strain and sample type each matched or exceeded the effect of soil type. The bulk soil compartment approached significance (p=0.054), suggesting that abundance shifts occur even in the non-root-influenced zone.

### Pooled Experiments

When Experiments 1 and 2 were combined, all three factors — soil type, sample type, and strain — were highly significant (all p=0.001) for **both** weighted and unweighted UniFrac. This confirms the robustness of the three-factor hierarchy across experimental replicates.

## OTU-Level Analysis

### Relative Influence of Factors on Individual OTUs

[[otu-differential-abundance-cannabis-microbiome]] testing at the OTU level reinforced the dominance of soil type:

- **Soil type**: 690 weighted-significant OTUs, 657 unweighted-significant OTUs — by far the strongest effect.
- **Strain**: 71 weighted-significant OTUs, but **zero** unweighted-significant OTUs. This is a critical distinction: cultivar identity reshapes *relative abundances* of taxa without fundamentally altering *which taxa are present*.
- **Sample type**: 51 weighted-significant OTUs, fewer than strain.

The absence of any strain-driven presence/absence differences means that cultivar effects operate through **niche filtering and competitive modulation** of already-present community members, not through recruitment of novel lineages.

### Taxonomic Identity of Strain-Responsive OTUs

OTUs that shifted significantly between Cannabis strains were overwhelmingly drawn from two phyla:

- **Proteobacteria**: Pseudomonadales, Burkholderiales, Sphingomonadales, Rhizobiales.
- **Bacteroidetes**: Sphingobacteriales, Flavobacteriales.

A notable strain-specific association was *[[sphingomonas-wittichii-cannabis-endorhiza-strain-specificity]]*, which was prevalent in the [[maui-wowie]] cultivar. This species can metabolize phenazine-1-carboxylic acid, a compound with [[medicinal-mushroom-antimicrobial-properties]]. Its enrichment may reflect a cultivar-specific root exudate profile or a role in pathogen suppression, potentially contributing to increased survival in certain soils.

## Soil-to-Root Microbiome Gradients

### Compartment Similarity Structure

Beta-diversity distances between compartments revealed a clear hierarchical grouping:

- **Rhizosphere ↔ bulk soil**: significantly lower beta distance (p<0.001 vs. both endorhiza comparisons).
- **Rhizosphere ↔ endorhiza** and **bulk soil ↔ endorhiza**: both significantly larger distances.
- Rhizosphere-to-endorhiza distances were **not significantly different** from bulk-soil-to-endorhiza distances.

This pattern indicates that the endorhiza represents a strongly differentiated microbial habitat, regardless of whether the source community is rhizosphere or bulk soil. The rhizosphere, by contrast, remains broadly similar to the surrounding bulk soil, acting as an intermediate rather than a sharply bounded zone.

### Alpha-Diversity Gradient

The Chao1 richness estimator revealed a stepwise diversity decline from soil to root interior:

| Compartment | Chao1 (mean) | Std. dev. |
|-------------|-------------|-----------|
| Bulk soil | 4,947 | 717 |
| Rhizosphere | 4,525 | 542 |
| Endorhiza | 3,321 | 420 |

The bulk-soil-to-rhizosphere transition involves a modest ~8.5% reduction in estimated richness. The rhizosphere-to-endorhiza transition is far more dramatic, representing a ~26.6% decline. This two-step pattern mirrors the beta-diversity results and is consistent with sequential filtering: first by root exudate-mediated selection in the rhizosphere, then by host immune surveillance and endophytic colonization barriers at the root interior.

### Soil-Type Effects on Alpha Diversity

The MB (Living Soil mix) supported significantly higher diversity than the OC (organic [[compost]]) soil in the external compartments:

- **Bulk soil**: MB 5,597 vs. OC 4,296.
- **Rhizosphere**: MB 4,859 vs. OC 3,913.
- **Endorhiza**: MB ~3,325 vs. OC ~similar (no significant difference).

Notably, the endorhiza showed **convergent diversity** regardless of soil type. This suggests that host-level filtering in the root interior imposes a ceiling on endophytic richness that is relatively insensitive to the starting soil community composition.

## Two-Tier Colonization Model: OTU Sharing Evidence

A key experiment tested whether endorhiza communities are primarily derived from their *own* soil environment or represent a universal Cannabis endophyte pool. White Widow plants were grown in two distinct soils (MB and OC), and the number of OTUs shared between each endorhiza sample and each soil type was counted.

- OTUs shared with **home soil** (the soil the plant was grown in): mean = 2,934.
- OTUs shared with **foreign soil** (the other soil type): mean = 2,162.
- Difference: p = 1.209 × 10⁻¹⁵.

This highly significant result supports a **two-tier colonization model**:

1. **Tier 1 — Soil selection**: The resident soil community serves as the primary reservoir from which rhizosphere and endorhiza taxa are drawn. Different soils provide different starting pools.
2. **Tier 2 — Host filtering**: The plant then applies its own selective pressures (immune responses, exudate chemistry, oxygen gradients), progressively narrowing the community from bulk soil through rhizosphere to endorhiza.

The convergence of endorhiza alpha diversity across soil types (noted above) reflects Tier 2 filtering, while the OTU-sharing asymmetry reflects Tier 1 sourcing.

## Cannabinoid–Microbiome Correlations

Delta-9-THC concentration varied significantly between Cannabis strains and correlated with community structure (unweighted UniFrac Mantel r=0.863, p=0.001). However, THC production was itself **confounded with soil type** — one soil consistently supported higher THC levels — making it impossible to disentangle cannabinoid-driven microbiome effects from edaphic effects.

This confound is a recurring challenge in [[cannabis-microbiome-research]]: chemical phenotype (chemotype) and soil environment co-vary, and experimental designs that orthogonally vary both factors are needed to isolate direct cannabinoid–microbe interactions.

## Edaphic Determinant Rankings

All measured [[cannabinoid-microbiome-correlation-confounded-edaphic-factors]] (nitrogen, salinity, carbon, water content, pH) were significantly correlated with community beta-diversity across all experiments (all p=0.001). Their relative effect sizes, ranked by Mantel correlation coefficient:

| Rank | Factor | Weighted r | Unweighted r |
|------|--------|-----------|-------------|
| 1 | Nitrogen | 0.465 | 0.630 |
| 2 | Salinity | 0.437 | 0.620 |
| 3 | Carbon | 0.330 | 0.512 |
| 4 | Water content | 0.281 | 0.466 |
| 5 | pH | 0.221 | 0.292 |

The ranking order is identical for both weighted and unweighted analyses. Nitrogen and salinity are the two dominant edaphic drivers, with nitrogen showing the strongest single-factor correlation. Unweighted correlations are uniformly higher than weighted ones, suggesting that edaphic factors have a stronger influence on *which taxa can persist* (presence/absence) than on their relative abundances once established. pH, despite its importance in many soil microbiome studies, ranked last among the measured variables in this Cannabis system.

## Key Takeaways

1. **Soil type is the primary determinant** of Cannabis-associated microbiome composition at both community and OTU levels.
2. **Cultivar (strain) shapes abundances, not membership** — no presence/absence OTU differences between strains.
3. **Endorhiza communities are strongly filtered** from their soil of origin (two-tier model), but converge to similar diversity regardless of starting soil.
4. **Nitrogen and salinity** are the dominant edaphic drivers; pH is surprisingly weak in this system.
5. **Cannabinoid–microbiome links** are promising but confounded with soil type in current experimental designs.
