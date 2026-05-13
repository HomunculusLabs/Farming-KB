---
title: Cannabis Strain Effects on OTU Abundance vs Presence/Absence
tags:
  - unifrac
  - weighted-analysis
  - strain-specificity
  - cannabis
  - microbiome
  - OTU
  - abundance
  - presence-absence
  - community-structure
  - beta-diversity
  - Winston
date: 2024-01-01
paper: Winston et al. 2014
---

# Cannabis Strain Effects on OTU Abundance vs Presence/Absence

## Overview

One of the most striking findings from Winston et al. (2014) is the
dramatic difference between **weighted** and **unweighted** UniFrac
analyses when evaluating the effect of Cannabis strain on the root
microbiome. Strain identity has **zero** influence on which taxa are
present or absent, yet it has a **substantial** effect on the relative
abundance of taxa already present. This decoupling of composition from
structure is central to understanding how host genotype shapes the
[[purple-and-color-changing-cannabis-strains]] draw from the same pool of soil-derived
microorganisms, but each strain alters the proportional representation
of those organisms.

## Ordination: PC1 Shifts Between Metrics

| Analysis | PC1 Dominant Factor | Variance Explained |
|----------|--------------------:|-------------------:|
| Unweighted UniFrac | Soil type | 32.06% |
| Weighted UniFrac | Strain | 34.51% |

In unweighted space, soil type drives the largest axis — the **set of
taxa** colonizing roots is determined by soil availability. In weighted
space, strain displaces soil type as the dominant PC1 factor, showing
that **how abundant** each taxon becomes is controlled by host genotype.

## Pooled Analysis: R² Values for Strain

When all sample types were pooled, PERMANOVA yielded:

- **Weighted UniFrac**: R² = 0.301 (p = 0.001)
- **Unweighted UniFrac**: R² = 0.178 (p = 0.001)

The weighted R² is ~70% higher, confirming that strain effects are
**concentrated in abundance patterns** rather than taxonomic turnover.

## Taxonomic Identity of Strain-Differentiating OTUs

The 71 strain-responsive OTUs were enriched in two phyla:

### Proteobacteria

- **Pseudomonadales**: Common rhizosphere colonists; includes plant growth-promoting and pathogenic species.
- **Burkholderiales**: Diverse plant-associated lifestyles.
- **Sphingomonadales**: Organic compound degraders; frequent in rhizosphere soils.
- **Rhizobiales**: Root-associated nitrogen fixers; key rhizosphere functional group.

### Bacteroidetes

- **Sphingobacteriales**: Environmental generalists; some with plant growth-promoting properties.
- **Flavobacteriales**: Polysaccharide specialists; enriched in rhizosphere environments.

The overrepresentation of Proteobacteria and Bacteroidetes reflects
their status as fast-growing, copiotrophic taxa that respond rapidly to
root exudate signals. Different strains likely produce different exudate
profiles, favoring different subsets of these lineages.

## Convergent Host Genotype-Dependent Selection

Winston et al. describe the mechanism as **"convergent host genotype-
dependent selection."** Different Cannabis strains converge on similar
species pools (soil is the primary filter) but diverge in relative
abundances (each genotype selectively enriches or depletes specific
taxa from the shared pool).

1. **Composition is supply-driven**: The soil seed bank determines which taxa can colonize the root zone.
2. **Structure is demand-driven**: [[root-exudates]] alter competitive dynamics, shifting abundances without eliminating taxa.
3. **Convergence across genotypes**: All strains share enough basic rhizosphere chemistry to attract broadly similar assemblages.
4. **Divergence in proportions**: Subtle exudate differences create measurable abundance shifts detectable only with weighted methods.

## Practical Implications for Cultivation

- **Cultivar selection shapes the microbiome by altering proportions of soil-derived microbes, not by recruiting unique taxa.**
- **Soil management remains the primary lever** for influencing which organisms are available to colonize roots.
- **Strain-specific breeding could optimize functional outcomes** if certain abundance profiles associate with [[ph-and-nutrient-availability-garden-soils]].
- **[[cannabis-endorhiza-bacterial-communities]] in the rhizosphere of two Cannabis sativa genotypes. *Applied Soil Ecology*, 79, 77–88.
  - Table 2: PERMANOVA results for weighted and unweighted UniFrac.
  - Figure 2: PCoA ordinations showing factor loadings on PC1.
  - Supplementary materials: OTU-level taxonomic assignments.
