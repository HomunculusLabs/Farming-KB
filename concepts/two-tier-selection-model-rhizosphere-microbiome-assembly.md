---
title: Two-Tier Selection Model of Rhizosphere Microbiome Assembly
created: 2026-05-11
source: understanding-cultivar-specificity-cannabis-microbiome.md
tags: [microbiome, rhizosphere, two-tier-selection, plant-microbe-interactions, soil-ecology, endorhiza]
aliases: [Two-Tier Model Root Microbiome, Rhizosphere Selection Model]
---

# Two-Tier Selection Model of Rhizosphere Microbiome Assembly

The two-tier selection model describes how root-associated [[cannabis-endorhiza-bacterial-communities]]
are assembled through two sequential selective filters: first by soil (edaphic)
properties at the rhizosphere level, and then by plant genotype at the endorhiza
level. This model, supported by the [[winston-cannabis-microbiome-study-design]] of Winston et al.
(2014), provides a framework for understanding the relative contributions of
environment and host genetics to plant microbiome composition.

## The Model Explained

### Tier 1: Soil Type Determines Rhizosphere Composition

The first selective filter operates at the transition from bulk soil to
rhizosphere. [[soil-physicochemical-properties-microbial-communities]] — particularly pH, but also
salinity, organic carbon content, nitrogen availability, water content, and
physical composition (sand/silt/clay ratios) — determine the structure of the
local soil microbiota. This bulk soil community then serves as the source pool
from which rhizosphere communities are drawn.

Root exudates (sugars, amino acids, organic acids) create a nutrient-rich
environment that shifts community composition away from bulk soil, but the
available taxa are constrained by what was already present in the soil. A plant
growing in acidic sandy soil will recruit from a fundamentally different
bacterial pool than the same cultivar growing in alkaline clay, regardless of
the plant's genotype.

**Key prediction:** Soil type is the dominant factor explaining beta-diversity
at the rhizosphere level. Rhizosphere communities from the same soil but
different plant species should be more similar to each other than rhizosphere
communities from the same plant species in different soils.

### Tier 2: Plant Genotype Determines Endorhiza Composition

The second selective filter operates at the transition from rhizosphere to
endorhiza (root interior). Having passed through the soil filter, bacteria
must now navigate the plant's immune system, compete for niche space within
root tissues, and survive in the fundamentally different biochemical environment
of the root interior. This second filter is genotype-dependent: different
cultivars of the same species maintain significantly different endorhiza
communities.

**Key prediction:** Cultivar identity is the dominant factor explaining
beta-diversity at the endorhiza level. Endorhiza communities from different
cultivars in the same soil should be more different from each other than from
the same cultivar in different soils.

## Evidence from Cannabis

The Winston et al. study provided strong support for both tiers:

### Tier 1 Evidence

- Bulk soil samples clustered significantly apart from all other sample types
  (ADONIS R² = 0.14, p = 0.001)
- Rhizosphere communities were not significantly differentiated by cultivar
  (ADONIS R² = 0.07, p = 0.07), confirming that soil, not genotype, drives
  rhizosphere composition
- BEST analysis identified soil physicochemical factors as the primary
  drivers of community variation at the rhizosphere level

### Tier 2 Evidence

- Endorhiza communities showed highly significant cultivar differentiation
  (ADONIS R² = 0.59, p = 0.004 for [[weighted-unifrac-strain-clustering-cannabis-endorhiza-community-structure]])
- This cultivar effect was observed even when controlling for soil type in
  Experiment 2 (two locations, two soil types)
- The genus Methylophilus varied 100-fold between cultivars in the same soil

### Diminishing Cultivar Effect

The strength of cultivar-specificity diminishes from endorhiza to rhizosphere
to bulk soil, exactly as the model predicts. Cultivar effects are significant
only in the endorhiza compartment, not in the rhizosphere or bulk soil.

## Predicted Phylum-Level Changes

The two-tier model predicts characteristic shifts in phylum-level abundance as
communities move through the tiers:

| Change | Mechanism |
|--------|-----------|
| Acidobacteria decrease | Shift from oligotrophic bulk soil to copiotrophic root zone |
| Proteobacteria increase | Fast-growing taxa favored by root exudate enrichment |
| Actinobacteria moderate | Some strains are competitive endophytes; others are soil specialists |
| Firmicutes variable | Some endospore-formers persist across compartments |

The dramatic reduction in Acidobacteria within the endorhiza is particularly
notable and has been observed across multiple plant species, suggesting it is
a general feature of tier 2 selection rather than a Cannabis-specific phenomenon.

## Broader Applicability

While originally developed from studies on Arabidopsis and other model plants,
the two-tier model has been validated across diverse plant species:

- **[[arabidopsis-thaliana]]** — Bodenhausen et al. (2013) demonstrated soil
  effects on rhizosphere and genotype effects on endorhiza
- **Maize (Zea mays)** — Peiffer et al. (2013) showed soil was the primary
  determinant of rhizosphere communities across genotypes
- **Rice (Oryza sativa)** — Edwards et al. (2015) found genotype-specific
  root microbiomes despite strong soil effects
- **Cannabis** — Winston et al. (2014) confirmed the pattern in a
  previously uncharacterized crop

## Limitations and Refinements

The two-tier model is a useful simplification but has known limitations:

1. **Plant age matters** — seedling communities are less differentiated than
   mature plants; composition shifts throughout the life cycle.
2. **Soil-plant interactions** — plants modify soil chemistry over time,
   creating feedback loops between tiers.
3. **Fungal communities** — the model was developed for bacteria; AMF show
   different patterns with stronger cannabis cultivar specificity.
4. **Stress responses** — drought, salinity, and pathogens can override both
   tiers by inducing defensive root exudate changes.
5. **Transient vs. core** — the model better predicts core members than
   transient taxa from stochastic colonization events.

## Agricultural Applications

The two-tier model has practical implications for microbiome management:

- **Soil management** (tier 1) is the highest-leverage intervention for
  rhizosphere health — composting, cover cropping, and pH adjustment shape
  the available microbial pool.
- **Breeding** (tier 2) can select for favorable endorhiza recruitment traits,
  effectively breeding for better microbial partnerships.
- **Inoculant strategy** should match the tier: soil amendments for broad
  rhizosphere effects, genotype-matched endophytes for targeted benefits.

## See Also

- cannabis rhizosphere microbiome zonation — zonation in Cannabis
- cannabis cultivar specificity endorhiza microbiome — cultivar effects
- [[endorhiza-endophyte-bacteria-plant-roots]] — endophyte biology
