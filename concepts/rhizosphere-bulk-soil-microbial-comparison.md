---
title: Rhizosphere vs Bulk Soil [[soil-edaphic-factors-microbial-communities]]
source: understanding-cultivar-specificity-cannabis-microbiome.md
tags:
  - microbiology
  - rhizosphere
  - soil-ecology
  - microbial-ecology
  - cannabis
created: 2026-05-09
---

## Overview

Understanding the distinction between rhizosphere and bulk soil microbial
communities is fundamental to plant microbiome ecology. Winston et al.
(2014) characterized both compartments in Cannabis sativa, providing
quantitative evidence for how root proximity reshapes microbial community
composition. Their analysis demonstrated that the rhizosphere represents an
intermediate zone between bulk soil and the [[cannabis-endorhiza-microbiome|endorhiza]], shaped primarily by plant-driven rhizodeposition.

## Definitions

### Bulk Soil

Bulk soil refers to soil not directly influenced by plant roots. It serves
as the baseline reference community in plant microbiome studies, representing
the indigenous soil microbiome unaffected by root exudates. In Winston et al.
(2014), bulk soil samples were collected at distance from plant roots to
ensure they were outside the zone of rhizosphere influence.

### Rhizosphere

The rhizosphere is the narrow zone of soil directly influenced by plant roots,
typically extending only a few millimeters from the root surface. It is often
defined as the soil adhering to roots after gentle shaking. The rhizosphere
is distinguished from bulk soil by elevated microbial activity and altered
composition driven by rhizodeposition — the release of organic compounds
including exudates, mucilage, and secretions.

## Beta-Diversity: Compartment Relationships

Winston et al. (2014) used beta-diversity analyses to quantify how microbial
communities differ across compartments. Rhizosphere communities were more
similar to bulk soil than to [[cannabis-rhizosphere-endorhiza-communities]], consistent with the
[[two-tier-selection-model-plant-microbiome]].

### OTU Abundance Correlations

Pearson correlation of OTU abundances between compartments:

| Comparison                    | Pearson rho |
|-------------------------------|-------------|
| Bulk soil vs Rhizosphere      | 0.92        |
| Rhizosphere vs Endorhiza      | 0.63        |
| Bulk soil vs Endorhiza        | 0.42        |

The high correlation (rho = 0.92) between bulk soil and rhizosphere confirms
the rhizosphere draws its inhabitants predominantly from the surrounding soil
pool. The moderate rhizosphere-endorhiza correlation (rho = 0.63) reflects
additional filtering at the root surface. The lowest bulk soil-endorhiza
correlation (rho = 0.42) demonstrates the cumulative effect of both selection
tiers.

## Rhizosphere as Intermediate Zone

The rhizosphere functions as an ecological transition zone shaped by two
forces:

1. **Soil influence**: The resident soil microbial community provides the
   source pool from which rhizosphere inhabitants are recruited. Soil
   properties (pH, texture, organic matter) constrain available taxa.
2. **Plant influence**: Rhizodeposition selectively stimulates growth of
   certain taxa while suppressing others, creating the rhizosphere effect —
   increased microbial biomass and altered composition relative to bulk soil.

This dual influence positions the rhizosphere as intermediate, sharing most
taxa with bulk soil but showing the beginnings of plant-driven selection that
intensifies in the endorhiza.

## Rhizodeposition and Community Shaping

Rhizodeposition encompasses several processes that shape rhizosphere communities:

- **Exudates**: Low-molecular-weight compounds (sugars, amino acids, organic
  acids) secreted by root cells, enriching copiotrophic microorganisms.
- **Mucilage**: Polysaccharide material from root cap cells creating hydrated
  microenvironments and carbon substrates.
- **Secretions**: Enzymes, antimicrobials, and signaling molecules that
  modulate microbial growth and [[edaphic-determinants-cannabis-microbiome-community-structure]].
- **Cell lysates**: From root cell turnover, providing organic substrates.

## Dynamic Nature of Rhizosphere Communities

Rhizosphere communities change dynamically:

- **Seasonal changes**: Communities shift over [[query-how-to-protect-plants-from-frost-and-extend-the-growing-season]] as plant
  developmental stage changes exudate composition and quantity.
- **Diel cycles**: Exudation rates fluctuate on daily cycles driven by
  photosynthate availability, shifting microbial activity.
- **Spatial heterogeneity**: Composition varies along the root axis and
  between root types, reflecting developmental gradients in exudation.

## Sequencing and Analytical Methodology

Winston et al. (2014) employed 16S rRNA gene amplicon sequencing:

- **Gene region**: V4 hypervariable region of the 16S rRNA gene.
- **Platform**: Illumina MiSeq for high-throughput community-level reads.
- **Bioinformatics**: QIIME 1.7.0 for sequence processing, OTU clustering,
  and taxonomic assignment.
- **Reference database**: Greengenes database for taxonomic classification.

### Distance Metrics

- **Weighted UniFrac**: Incorporates phylogenetic relationships and OTU
  abundances, sensitive to changes in dominant taxa. [[cannabis-cultivar-effects-soil-microbiome]] were
  detected using weighted but not unweighted distances.
- **[[weighted-vs-unweighted-unifrac-cannabis-strain-microbiome]]**: Considers only phylogeny and presence/absence,
  detecting compartment differences but not within-compartment cultivar
  effects.

## Edaphic Factors Ranking

Winston et al. (2014) ranked edaphic factors by influence on community
composition across all compartments:

1. **Nitrogen**: Strongest predictor, reflecting nitrogen's fundamental
   role in soil microbial ecology.
2. **Salinity**: Second strongest, affecting osmotic conditions and stress.
3. **Carbon**: Organic carbon availability shapes the heterotrophic energy
   landscape.
4. **Water content**: Moisture levels affect microbial activity and solute
   diffusion.
5. **pH**: Soil acidity influences physiology, but ranked lowest among the
   five measured factors.

## Alpha Diversity Patterns

Alpha diversity consistently peaked in bulk soil and declined through the
rhizosphere to the endorhiza. This reflects increasing selectivity of the
plant-driven filtering: bulk soil harbors the full soil microbiome diversity,
the rhizosphere enriches for root-exudate-adapted taxa, and the endorhiza
further selects for taxa capable of root interior colonization. See
[[cannabis-endorhiza-microbiome]] for specific Chao1 richness values.
## See Also
- [[two-tier-selection-model-plant-microbiome]] — Two-tier selection framework
- [[cannabis-endorhiza-microbiome]] — Root interior communities
- [[cannabis-cultivar-microbial-community-effects]] — Cultivar-specific effects
