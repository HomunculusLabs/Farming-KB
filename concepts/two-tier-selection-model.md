---
title: Two-Tier Selection Model
created: 2026-05-09
source: raw/papers/understanding-cultivar-specificity-cannabis-microbiome.md
tags: [microbiology, plant-microbiome, rhizosphere, endophytes, soil-science]
aliases: [two tier selection, rhizosphere selection model, endorhiza selection]
---

# Two-Tier Selection Model

## Overview

The **two-tier selection model** describes how plant-associated microbial
communities are assembled through two sequential filtering stages: first by
**soil (edaphic) factors**, then by **host genotype**.

The model predicts that soil type determines [[rhizosphere-bacterial-community-dynamics]]
composition, while plant genotype-dependent selection shapes the endorhiza
(internal root) [[cannabis-cultivar-microbial-community-effects]]. This framework was formally tested in
Cannabis by Winston et al. (2014) and resolves a long-standing debate about
the relative importance of edaphic versus host factors in microbiome assembly.

## Tier 1: Soil-Driven Selection (Rhizosphere)

The first tier is governed by **[[cannabinoid-microbiome-correlation-confounded-edaphic-factors]]** — physical and chemical soil
properties:

- **pH**: Strongest single predictor of soil [[edaphic-factors-microbial-community-structure]];
  small shifts alter nutrient bioavailability and metal solubility.
- **Salinity**: Selects for halotolerant taxa in saline environments.
- **Total nitrogen and organic carbon**: Shapes metabolism and competitive
  dynamics between copiotrophic and oligotrophic strategists.
- **Water content**: Governs aerobic vs. anaerobic niche availability.
- **Soil texture**: Determines pore structure and microbial habitat connectivity.

The bulk soil microbiota — structured primarily by edaphic variables — serves as
the **source pool** for rhizosphere colonization. Root exudates create a
nutrient-rich zone selecting a subset of the bulk soil community. This first
selection is broad and driven more by soil chemistry than plant identity.

Key prediction: rhizosphere communities from the same soil type are more similar
to each other than to those from different soil types, regardless of plant
species growing in them.

## Tier 2: Host Genotype-Driven Selection (Endorhiza)

The second tier occurs during **migration into plant tissues**. The endorhiza
community faces a fundamentally different selective environment. The plant host
exerts genotype-dependent selection through:

- **Root exudate profiles**: Cultivar-specific blends of sugars, organic acids,
  and [[antifungal-secondary-metabolites-coprophilous-fungi]] selectively feed or inhibit specific bacteria.
- **Immune recognition**: Pattern-triggered and effector-triggered immunity
  differentially permits or excludes taxa based on molecular patterns.
- **Root architecture**: Branching density and cortical thickness create
  different colonization niches selecting for different microbial traits.
- **Host antimicrobials**: Phytoalexins, terpenes, and alkaloids act as
  chemical filters permitting only tolerant endophytes.

Critical prediction: **[[cannabis-rhizosphere-endorhiza-communities]] are more strongly shaped by
cultivar than by soil type**. Within a given soil, different genotypes maintain
significantly different endorhiza communities.

## Predicted Taxonomic Shifts

| Transition | Change | Rationale |
|---|---|---|
| Bulk → Rhizosphere | ↑ Proteobacteria | Copiotrophs thrive in carbon-rich zone |
| Bulk → Rhizosphere | ↓ Acidobacteria | Oligotrophs outcompeted |
| Rhizo → Endorhiza | ↑ Gamma/Alpha-proteobacteria | Contain many endophytic genera |
| Rhizo → Endorhiza | ↓↓ Acidobacteria | Lack endophytic colonization traits |

These shifts are consistent across Arabidopsis, rice, maize, and poplar.

## Evidence from Cannabis

### Experiment 1 (3 cultivars, 1 soil)

Endorhiza clustered significantly by type (ADONIS: R² = 0.26, p = 0.001).
Bulk soil also clustered (R² = 0.14, p = 0.001). Rhizosphere was intermediate
and not significant (R² = 0.07, p = 0.07). Strain-level differences were
significant only in the endorhiza (weighted R² = 0.59, p = 0.004).

### Experiment 2 (2 cultivars, 2 soils)

Community composition across all samples was determined by soil properties
(Tier 1), but within endorhiza, cultivar was primary (Tier 2).

*Methylophilus* drove cultivar differences (FDR: p = 0.012): 13% in Bookoo
Kush, 0.13% in Burmese, absent in Sour Diesel.

## Core Endorhiza Community

Despite cultivar differences, Cannabis maintained a consistent core community:

- **Pseudomonas** — PGPR endophytes producing siderophores and antibiotics
- **Cellvibrio** — aerobic cellulolytic bacteria
- **Oxalobacteraceae** — nitrogen-fixing associates
- **Xanthomonadaceae** — diverse plant-associated bacteria
- **Actinomycetales** — bioactive secondary metabolite producers
- **Sphingobacteriales** — common root colonizers

All except *Cellvibrio* are well-known endophytes within Gamma/Alphaproteobacteria.

## Terroir Connection

The model explains how regional soil microbiology contributes to unique crop
characteristics. Tier 1 establishes the microbial source pool, and rhizosphere
organisms can influence plant secondary metabolite production — providing a
mechanistic basis for terroir effects documented in wine and other crops.

## Applications

- **Biofertilizers**: Inoculants must survive Tier 1 and compete in Tier 2
- **Crop breeding**: Selecting cultivars that recruit beneficial microbiomes
- **Disease suppression**: Manipulating soil to favor protective communities

## Limitations

- Pseudoreplication in sampling (multiple roots per plant)
- Growth stage confounds cultivar vs. age effects
- Fungal assembly may follow different rules
- Cannabis cultivar designations are informal
- Non-additive soil × cultivar interactions

## See Also

- [[cannabis-endorniza-microbiome]]
- [[rhizosphere-microbial-communities]]
- [[cultivar-specificity-microbiome]]
