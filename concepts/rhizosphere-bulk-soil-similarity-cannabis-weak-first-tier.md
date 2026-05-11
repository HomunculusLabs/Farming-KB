---
title: "Rhizosphere-Bulk Soil Similarity in Cannabis: The Weak First Tier"
tags: [microbiome, cannabis, rhizosphere, bulk-soil, two-tier-selection, microbial-ecology, rhizodeposition]
related: [cannabis-microbiome-two-tier-selection, rhizodeposition-microbial-filtering-two-step-colonization, cannabis-endorhiza-bacterial-communities]
source: [understanding-cultivar-specificity-cannabis-microbiome]
created: 2026-05-10
---

# Rhizosphere-Bulk Soil Similarity in Cannabis: The Weak First Tier

## Overview

A surprising and often underappreciated finding from the Winston et al. (2014) [[winston-cannabis-microbiome-study-design]] was that rhizosphere and bulk soil [[cannabis-rhizosphere-microbial-communities]] were far more similar to each other than either was to the endorhiza. In the first experiment, rhizosphere samples were not significantly different from other sample types by either unweighted (ADONIS: R² = 0.07, p = 0.07) or [[weighted-unifrac-strain-clustering-cannabis-endorhiza-community-structure]] (ADONIS: R² = 0.09, p = 0.10). This finding challenges the common assumption that the rhizosphere is a strongly differentiated microbial zone and has important implications for how we think about Cannabis root-microbe interactions.

## What Is the Rhizosphere?

The rhizosphere is the narrow zone of soil directly influenced by root secretions and associated soil microorganisms. It extends only a few millimeters from the root surface and is conceptually divided into:

- **Endorhiza (endosphere)**: Bacteria [[endophytic-fungi-living-inside-plants]] root tissue
- **Rhizoplane**: Bacteria attached to the root surface
- **Rhizosphere**: Soil influenced by [[mycorrhiza-root-exudates]] but not in direct contact with the root
- **Bulk soil**: Soil beyond the influence of root secretions

In theory, the rhizosphere should be distinct from bulk soil because roots exude large quantities of carbon compounds (sugars, amino acids, organic acids, mucilage) that fuel microbial growth. This "rhizosphere effect" has been documented in many plant species, typically showing 2- to 100-fold increases in microbial numbers in the rhizosphere compared to bulk soil.

## The Statistical Evidence for Rhizosphere-Soil Similarity

### First Experiment (Three Cultivars, One Soil)

The first experiment used Sour Diesel, Bookoo Kush, and Burmese cultivars grown in a single soil type with minimal edaphic variation. In this experiment:

- **Endorhiza vs. all other types**: Significant (unweighted R² = 0.26, p = 0.001; weighted R² = 0.59, p = 0.001)
- **Bulk soil vs. all other types**: Significant (unweighted R² = 0.14, p = 0.001; weighted R² = 0.29, p = 0.004)
- **Rhizosphere vs. all other types**: NOT significant (unweighted R² = 0.07, p = 0.07; weighted R² = 0.09, p = 0.10)

The rhizosphere failed to form a distinct cluster, suggesting that in this Cannabis system with minimal soil variation, the rhizosphere effect was not strong enough to create statistically separable communities from bulk soil.

### Second Experiment (Two Cultivars, Two Soil Types)

The second experiment introduced more edaphic variation by using [[soil-heritability-otu-sharing-white-widow-cross-soil-cannabis-endorhiza]] and [[maui-wowie]] in two different soil types. Here, the rhizosphere did show significant separation from other sample types (unweighted R² = 0.05, p = 0.04; weighted R² = 0.13, p = 0.001), but the effect size was much smaller than for endorhiza (R² = 0.10–0.26).

### Beta-Distance Comparisons

Direct comparison of community distances confirmed the pattern:

- Rhizosphere-to-bulk-soil distances were significantly lower than rhizosphere-to-endorhiza distances (both unweighted: t = 24.59, p < 0.001; weighted: t = 211.82, p < 0.001)
- Rhizosphere-to-bulk-soil distances were significantly lower than bulk-soil-to-endorhiza distances (unweighted: t = 25.15, p < 0.001; weighted: t = 211.56, p < 0.001)
- Rhizosphere-to-endorhiza distances were NOT significantly different from bulk-soil-to-endorhiza distances (unweighted: t = 2.10, p = 0.109; weighted: t = 2.23, p = 0.078)

This last finding is particularly striking: it means that, in terms of community dissimilarity, the rhizosphere is essentially no closer to the endorhiza than the bulk soil is. The rhizosphere is not acting as a strong transitional zone in Cannabis.

## OTU Abundance Correlations: The Sliding Scale

The Pearson correlation of mean OTU abundances between sample types provided further evidence:

| Comparison | Pearson's rho | Interpretation |
|-----------|--------------|----------------|
| Bulk soil ↔ Rhizosphere | 0.92 | Very high similarity |
| Rhizosphere ↔ Endorhiza | 0.63 | Moderate similarity |
| Bulk soil ↔ Endorhiza | 0.42 | Weak similarity |

The 0.92 correlation between bulk soil and rhizosphere indicates that the rhizosphere largely mirrors the bulk soil [[core-endorhiza-bacterial-community-composition-cannabis]], with only modest shifts in relative abundances. In contrast, the jump from rhizosphere to endorhiza represents a major compositional restructuring.

## Why Is the Cannabis Rhizosphere Effect Weak?

Several factors may explain why the rhizosphere effect was less pronounced in Cannabis than in some other plant systems:

### 1. Minimal Edaphic Variation in Experiment 1
The first experiment used locally composted soil from a single source, with very similar [[soil-physicochemical-properties-cannabis-microbiome-assembly-winston]] across samples (pH 6.63–6.94, similar sand-silt-clay ratios). Without strong baseline differences in soil chemistry, the incremental effect of root exudates on the rhizosphere community may have been insufficient to create statistical separation.

### 2. Root Exudate Composition
Cannabis produces unique [[antifungal-secondary-metabolites-coprophilous-fungi]] (cannabinoids, terpenes) that may influence microbial communities differently than the primary metabolites (sugars, organic acids) that typically drive the rhizosphere effect in other plants. If Cannabis roots allocate more carbon to defensive [[biodiversity-fungal-secondary-metabolites]] and less to simple exudates, the rhizosphere effect may be naturally attenuated.

### 3. Sampling Methodology
Rhizosphere samples were collected by shaking roots into a whirlpak bag — a standard method, but one that may include some bulk soil contamination. The boundary between rhizosphere and bulk soil is inherently fuzzy, and the method may not have captured the tightly root-associated microbes most likely to be differentiated.

### 4. Sampling Timing
In the first experiment, samples were taken eight weeks post-harvest of flowering bud and foliage. Root exudation patterns change dramatically during flowering and after harvest, potentially weakening the rhizosphere effect compared to actively growing plants. The second experiment sampled two weeks pre-harvest, where a stronger rhizosphere effect was indeed detected.

## Implications for the Two-Tier Selection Model

The weak rhizosphere effect in Cannabis has an interesting implication for the two-tier selection model:

- **Tier 1 (soil → rhizosphere)**: In Cannabis, this tier appears to be relatively weak. The rhizosphere community is largely a diluted reflection of the bulk soil community.
- **Tier 2 (rhizosphere → endorhiza)**: This tier is the dominant selective step. The plant genotype exerts strong filtering pressure that dramatically reshapes the community as bacteria transition from soil/root surface into root tissue.

This suggests that in Cannabis, the plant's immune system and root tissue chemistry — rather than exudate-mediated rhizosphere enrichment — are the primary drivers of microbial [[biodiversity-fungal-community-assembly]]. The rhizosphere may serve more as a transit zone than as an active selection chamber.

## Practical Implications for Cultivation
