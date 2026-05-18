---
title: Cannabis Cultivar-Specificity and Soil Determinants of the Microbiome
source: understanding-cultivar-specificity-cannabis-microbiome.md
type: concept
---

# Cannabis Cultivar-Specificity and Soil Determinants of the Microbiome

## Overview

This concept page summarizes the second experiment from Winston et al. (2014), which investigated how **cannabis cultivar (strain)**, **soil type**, and **sample compartment** interact to shape the root-associated microbiome. The experiment grew two cannabis strains — **White Widow** and **[[maui-wowie]]** — in two distinct soil types (MB and OC), providing a factorial design to disentangle these overlapping influences on microbial [[core-endorhiza-bacterial-community-composition-cannabis]].

## Experimental Design

- **Strains:** White Widow (indica-dominant) and Maui Wowie (sativa-dominant)
- **Soil types:** Two distinct soils (MB and OC), differing in physical and chemical properties
- **Sample compartments:** Bulk soil, [[rhizosphere]] soil, and endorhiza (root interior)
- **Analysis:** 16S rRNA amplicon sequencing with OTU-based community profiling

Variance in [[edaphic-factors-microbial-community-structure]] was partitioned using PERMANOVA (ADONIS) on both **unweighted** (presence/absence) and **weighted** (abundance-aware) UniFrac distances.

## Beta Diversity: Partitioning the Drivers of Community Variation

### Unweighted UniFrac Results

When considering only the presence or absence of microbial lineages:

| Factor | R² | p-value |
|---|---|---|
| Soil type | 0.32 | 0.001 |
| Sample type (compartment) | 0.12 | 0.005 |
| Strain (cultivar) | 0.10 | 0.008 |

Soil type was the dominant driver, explaining roughly one-third of community variation. This underscores the primacy of the **edaphic environment** in filtering which microbial taxa can exist in the root zone. However, both sample compartment and strain were also significant, indicating plant-mediated selection occurs even after accounting for soil differences.

### Weighted UniFrac Results

When relative abundance was incorporated, the variance partitioning shifted substantially:

| Factor | R² | p-value |
|---|---|---|
| Sample type (compartment) | 0.27 | 0.001 |
| Strain (cultivar) | 0.27 | 0.001 |
| Soil type | 0.21 | 0.001 |

Under weighted analysis, sample compartment and strain each explained more variance than soil type. While soil type determines *which taxa are present*, the **plant** — and specifically the cultivar — strongly influences *how abundant those taxa become*. This reveals that cannabis exerts **abundance-based selection** on its microbiome rather than strictly filtering taxa.

### Strain-Specific Signatures

Strain-level differences were driven by the prevalence of ***[[sphingomonas-wittichii-cannabis-endorhiza-strain-specificity]]*** in Maui Wowie. This species can **metabolize phenazine-1-carboxylic acid** — an antibiotic compound produced by certain soil bacteria — potentially conferring a competitive advantage in the rhizosphere. Its differential enrichment suggests cultivar-specific root exudate profiles select for functionally distinct microbial partners.

## Compartmental Differentiation: Bulk Soil → Rhizosphere → Endorhiza

Bulk soil and rhizosphere communities were significantly more similar to each other than either was to the endorhiza (all pairwise t-tests, p < 0.001). This pattern is consistent with the established understanding that the rhizosphere is a transitional zone where soil-derived microbes first encounter [[root-exudates]], while the endorhiza is subject to much stronger plant immune selection.

### The Two-Step Root Colonization Model

White Widow grown in two different soils provided a direct test of colonization dynamics:

- Endorhiza shared significantly more OTUs with its **own native soil** (mean = 2,934) than with the **other soil** where the same strain was grown (mean = 2,162; t = −10.05, p = 1.2 × 10⁻¹⁵)

This strongly supports a **two-step colonization model**:

1. **Step 1 — Soil filtering:** The local soil provides the primary pool of potential root colonizers
2. **Step 2 — Plant selection:** The plant selectively enriches certain taxa from this pool during endorhiza colonization

Soil source identity persists as a legacy in the root microbiome and is not erased by plant selection.

## Cannabinoid Concentration and the Endorhiza Microbiome

Cannabinoid concentration correlated with [[weighted-unifrac-strain-clustering-cannabis-endorhiza-community-structure]] (unweighted r = 0.863, p = 0.001 between strains). However, this relationship is **confounded by soil type effects on THC production** — different soils produced different THC concentrations in the same strain, and soil type independently shapes microbial community structure. Disentangling whether cannabinoids directly influence the microbiome requires further experimentation.

## Edaphic Factors as Master Regulators

All measured edaphic factors were significantly correlated with beta-diversity (p = 0.001). Their ranked importance (weighted UniFrac):

| Rank | Factor | Correlation (r) |
|---|---|---|
| 1 | Nitrogen content | 0.465 |
| 2 | Salinity | 0.437 |
| 3 | Carbon content | 0.330 |
| 4 | Water content | 0.281 |
| 5 | pH | 0.221 |

The same ranking held for unweighted UniFrac but with stronger correlations, consistent with soil factors primarily influencing taxon presence/absence. **Nitrogen and salinity** emerged as the strongest drivers, with practical implications for [[arbuscular-mycorrhizal-fungi-cannabis-cultivation]] management.

## Alpha Diversity Across Compartments

A consistent pattern of **diversity reduction** was observed moving into the root:

| Compartment | Mean Chao1 (Richness) |
|---|---|
| Bulk soil | 4,947 |
| Rhizosphere | 4,525 |
| Endorhiza | 3,321 |

Bulk soil harbored the highest richness, with a modest rhizosphere reduction (~8.5%) and a **dramatic endorhiza reduction** (~33% from bulk). This reflects increasing selection pressure as microbes approach and enter root tissues.

The MB soil supported higher diversity than OC soil in bulk and rhizosphere compartments, but this advantage **disappeared in the endorhiza** — suggesting plant internal selection converges on similar richness regardless of starting soil diversity.

## OTU-Level Differential Abundance Analysis

### By Factor

- **Soil type:** Dominant influence — **690 weighted**, **657 unweighted** significant OTUs
- **Strain:** 71 weighted, **0 unweighted** significant OTUs — cultivar selection operates on **abundance only**, not presence/absence
- **Sample type:** 51 weighted, 11 unweighted significant OTUs

That strain influenced zero OTUs unweighted but 71 weighted provides definitive evidence: all strains sampled the same soil taxa but differentially enriched or suppressed specific members.

### Taxa Enriched and Depleted in the Endorhiza

- **17 OTUs increased** in endorhiza: predominantly **Proteobacteria**, especially the order **Rhizobiales** — many known plant associates including nitrogen fixers and PGPR
- **Acidobacteria decreased dramatically** in endorhiza, particularly order **iii1-15** (p = 1.12 × 10⁻⁷) — consistent with oligotrophic Acidobacteria being outcompeted by copiotrophic Proteobacteria in the carbon-rich root interior

## Synthesis: A Hierarchical Model of Microbiome Assembly

1. **Soil provides the species pool** — Edaphic factors (especially nitrogen, salinity, carbon) determine which taxa are available; soil type exerts the strongest presence/absence effect
2. **Compartment filters the community** — Progressive selection from bulk soil through rhizosphere to endorhiza reduces diversity, enriching Proteobacteria and depleting Acidobacteria
3. **Cultivar fine-tunes abundances** — Strain does not determine *which* taxa colonize, but strongly modulates *how abundant* they become via exudate profiles [[plant-defense-chemistry-and-secondary-metabolites]]
4. **Cannabinoid-microbiome correlations** are promising but confounded by soil effects, requiring controlled experiments for causal claims

## Key Takeaways

- **Soil type is the primary determinant** of available microbial taxa for root colonization
- **Cannabis cultivar selection acts on abundance, not presence/absence** — all strains draw from the same soil pool
- **Two-step colonization** is supported: soil legacy persists in endorhiza alongside plant selection
- **Nitrogen and salinity** are the strongest individual edaphic predictors of community structure
- **Endorhiza enriches Proteobacteria (Rhizobiales)** and depletes Acidobacteria
- **Cannabinoid-microbiome correlations** require disentangling from soil effects before mechanistic conclusions
