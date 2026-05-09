---
title: Microbial microbial alpha diversity soil plant gradient Across the Soil-Plant Gradient
created: 2026-04-28
tags: [microbiome, diversity, soil-science]
date: 2026-04-28
updated: 2026-04-28
sources:
  - /Users/t3rpz/wiki/raw/papers/understanding-cultivar-specificity-cannabis-microbiome.md
type: concept
---

# Microbial Alpha Diversity Across the Soil-Plant Gradient

## Overview

Alpha diversity (within-sample microbial richness) in Cannabis follows a
consistent pattern: it peaks in bulk soil, decreases slightly in the
rhizosphere, and drops dramatically in the endorhiza. This gradient reflects
the progressive filtering of microbial diversity as bacteria transition from
the open soil environment through the root zone and into root tissue. Winston
et al. (2014) quantified this pattern using both observed species counts and
the chao1 richness estimator across two experiments.

## The Diversity Gradient Pattern

The alpha diversity gradient follows a consistent three-step pattern:

1. **Bulk soil**: Highest diversity, representing the full complement of
   soil microbial life adapted to the local edaphic conditions.
2. **Rhizosphere**: Slight reduction from bulk soil, as [[mycorrhizal-root-exudates-pathogen-interactions]]
   selectively enrich certain bacterial groups while creating competitive
   conditions that exclude others.
3. **Endorhiza**: Dramatic reduction from rhizosphere, as the plant immune
   system and internal tissue conditions create a highly selective environment
   that only certain bacteria can colonize.

## Experiment 2: Deep Sequencing Results

The second experiment provided the most detailed diversity measurements due to
deeper sequencing (rarefaction to 45,000 sequences per sample). Both observed
species and chao1 metrics showed the same gradient pattern:

### Chao1 Richness Estimates

| Compartment  | Mean   | Std Dev |
|-------------|--------|---------|
| Bulk soil   | 4,947  | 717     |
| Rhizosphere | 4,525  | 542     |
| Endorhiza   | 3,321  | 420     |

The reduction from bulk soil to rhizosphere was modest (approximately 8.5%),
while the reduction from rhizosphere to endorhiza was substantial
(approximately 26.6%), indicating that plant internal tissue imposes stronger
filtering than the rhizosphere environment.

### Soil-Type Differences in Diversity

Significant differences existed between the two soil types in the second
experiment, but only in the bulk soil and rhizosphere compartments:

**Bulk soil chao1:**
- MB soil (Mo-Bio): mean = 5,597, s = 89
- OC soil (Orange County): mean = 4,296, s = 85

**Rhizosphere chao1:**
- MB soil: mean = 4,859, s = 286
- OC soil: mean = 3,913, s = 290

**Endorhiza chao1 (no significant difference):**
- MB soil: mean = 3,325, s = 517
- OC soil: mean = 3,311, s = 112

The convergence of endorhiza diversity across soil types supports the
two-tier [[two-tier-selection-model-plant-microbiome]]: despite different starting diversities in the
soil, the plant selects a similarly diverse endorhiza community regardless
of soil origin.

## Experiment 1: Shallow Sequencing Results

Despite much shallower sequencing (rarefaction to 3,000 sequences per sample),
the same gradient pattern was recovered:

| Compartment  | Chao1 Mean | Chao1 Std Dev |
|-------------|-----------|---------------|
| Bulk soil   | 2,010.7   | 146.2         |
| Rhizosphere | 1,837.2   | 114.0         |
| Endorhiza   | 916.1     | 161.7         |

The endorhiza in experiment 1 showed dramatically lower diversity compared to
experiment 2, which is attributed to [[cannabis-root-decay-cellvibrio-biomarker-post-harvest]]. Experiment 1 samples were
collected 8 weeks post-harvest, while experiment 2 samples were taken from
actively growing plants two weeks before harvest.

## Cross-Experiment Comparison

When samples from both experiments were pooled and rarified to the level of
the first experiment (3,000 sequences), the endorhiza diversity difference
became clear:

- Experiment 1 endorhiza: chao1 mean = 916.1, s = 161.7
- MB soil endorhiza (experiment 2): chao1 mean = 1,413, s = 280.1
- OC soil endorhiza (experiment 2): chao1 mean = 1,374, s = 64.4

The experiment 1 endorhiza diversity was greatly reduced compared to
experiment 2, consistent with the early stages of root decay following
harvesting. However, the bulk soil diversity of MB1 was intermediate
(chao1: m = 2,010.7, s = 146.2) between the MB bulk soil (m = 2,319.1,
s = 124.3) and OC bulk soil (m = 2,004.8, s = 118.6), indicating that
the diversity reduction was specific to the endorhiza compartment and not
a general soil effect.

## Implications for the Two-Tier Selection Model

The alpha diversity pattern provides additional support for the two-tier
selection model:

1. The large and consistent diversity drop from rhizosphere to endorhiza
   confirms strong host genotype-dependent filtering at the root interior.
2. The convergence of endorhiza diversity across different soil types shows
   that the plant imposes a ceiling on endorhiza diversity regardless of
   the available soil microbial pool.
3. The modest diversity drop from bulk soil to rhizosphere reflects the
   more permissive selective environment created by root exudates, where
   soil type remains the dominant factor.

## See Also

- [[rhizosphere-microbiome-selection-model]] for the assembly framework
- [[cellvibrio-and-root-decay-microbiome]] for post-harvest diversity effects
- [[cannabis-microbiome-research]] for the complete study overview
