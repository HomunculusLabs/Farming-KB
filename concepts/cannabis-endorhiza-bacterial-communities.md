---
title: Cannabis Endorhiza Bacterial Communities
created: 2026-05-11
updated: 2026-05-11
type: concept
tags: [cannabis, microbes, soil, mycorrhizae]
sources: [raw/papers/understanding-cultivar-specificity-cannabis-microbiome.md]
---

# Cannabis Endorhiza Bacterial Communities

## Overview

The endorhiza — the community of bacteria colonizing root tissue — represents the most intimate and plant-selective compartment of the root microbiome. The 2014 Winston et al. study provided the first comprehensive description of Cannabis endorhiza bacterial communities across five distinct cultivars, revealing a core microbiome shared across all strains alongside significant cultivar-specific differences in microbial abundance.

## Core Endorhiza Community

Despite cultivar-specific variation, all five Cannabis strains maintained a conserved core bacterial community within the endorhiza:

- **Pseudomonas** — ubiquitous genus within the Gammaproteobacteria, well-known for plant growth-promoting properties including siderophore production, phosphate solubilization, and pathogen suppression
- **Cellvibrio** — an aerobic cellulolytic bacterium, notable as the only non-typical endophyte in the core community; its presence reflects the decomposition of plant cell wall material in the root zone
- **Oxalobacteraceae** — a family within the Betaproteobacteria associated with nitrogen cycling and organic acid metabolism
- **Xanthomonadaceae** — a family of Gammaproteobacteria that includes both plant pathogenic and beneficial species; their consistent presence in healthy Cannabis roots suggests a non-pathogenic functional role
- **Actinomycetales** — an order of Actinobacteria known for producing antibiotics and antifungal compounds; they may contribute to root disease resistance
- **Sphingobacteriales** — an order of Bacteroidetes involved in complex carbohydrate degradation

With the exception of Cellvibrio, all prevalent core members are well-established endophytic bacteria primarily within the orders Gammaproteobacteria and Alphaproteobacteria. This taxonomic profile aligns with observations from other plant systems, suggesting conserved evolutionary mechanisms of [[fungal-endophyte-colonization-patterns]] across diverse plant species.

## Cultivar-Specific Abundance Differences

While the core community was conserved, the relative abundances of specific OTUs varied significantly between Cannabis cultivars. This pattern was evident in weighted (abundance-based) but not unweighted (presence/absence) UniFrac analyses:

- **Experiment 1** (Burmese, BooKoo Kush, Sour Diesel): Endorhiza communities clustered significantly by strain (weighted ADONIS: R² = 0.59, p = 0.004; unweighted ADONIS: R² = 0.39, p = 0.003)
- **Experiment 2** (White Widow, Maui Wowie): Strain differentiation was also significant (weighted ADONIS: R² = 0.27, p = 0.001)
- **Pooled experiments**: Strain remained significant across all data combined (weighted ADONIS: R² = 0.301, p = 0.001)

The absence of unweighted strain effects (0 significant OTUs in Experiment 1) confirms that cultivar selection reshapes community structure by adjusting relative abundances of shared taxa, not by introducing cultivar-specific species.

## Key Strain-Differentiating Taxa

### Methylophilus in Bookoo Kush

The most dramatic strain-specific finding was the enrichment of *Methylophilus* in the Bookoo Kush endorhiza:

- Comprised 13% of the Bookoo Kush endorhiza microbial community
- Only 0.13% in Burmese endorhiza
- Completely absent from Sour Diesel endorhiza
- This difference explained a significant portion of the strain-level variation (FDR: p = 0.012)

*Methylophilus* species are methylotrophic bacteria that can utilize one-carbon compounds such as methanol as their sole carbon and energy source. Their enrichment in Bookoo Kush may reflect differences in root exudate profiles, particularly methanol production from pectin demethylation in cell wall metabolism.

### Sphingomonas wittichii in Maui Wowie

In the second experiment, *Sphingomonas wittichii* was prevalent in the Maui Wowie endorhiza. This species has been documented to metabolize phenazine-1-carboxylic acid and has been implicated in increased survival in soil environments. Its presence may contribute to pathogen suppression or niche competition within the root interior.

### Proteobacteria Dominance in Strain Differentiation

The majority of OTUs showing significant abundance differences between Cannabis strains belonged to the Proteobacteria phylum, specifically the orders:

- **Pseudomonadales** — includes many plant growth-promoting rhizobacteria (PGPR)
- **Burkholderiales** — contains both beneficial and pathogenic species; some fix nitrogen
- **Sphingomonadales** — known for degrading aromatic compounds and [[singh-fungal-biodegradation-of-polycyclic-aromatic-hydrocarbons]]
- **Rhizobiales** — best known for nitrogen fixation in legume root nodules; also includes non-nodulating endophytes

Additionally, Bacteroidetes orders Sphingobacteriales and Flavobacteriales contributed to strain-level differences.

## Functional Implications

The cultivar-specific microbial profiles suggest functional consequences for plant health:

### Plant Growth Promotion
Endorhiza bacteria support plant growth through phytohormone production (auxins, cytokinins, gibberellins), low molecular weight compounds, and enzymes that regulate growth and metabolism. The varying abundance of Pseudomonadales and Rhizobiales across cultivars implies differential access to these growth-promoting functions.

### Disease Suppression
Several core community members (Pseudomonas, Actinomycetales) are known biocontrol agents. The enrichment of *Sphingomonas wittichii* in Maui Wowie, with its ability to metabolize phenazine compounds, may indicate enhanced competitive exclusion of pathogens in that cultivar's root zone.

### Phytotoxicant Tolerance
Endorhiza bacteria can assist host plants in tolerating phytotoxic effects of environmental contaminants. This function may be particularly relevant for Cannabis, which can accumulate heavy metals and other soil contaminants in its tissues.

### Terroir Effects
Endorhiza communities may contribute to localized "terroir" — the characteristic sensory profile associated with cannabis grown in specific regions. This has been demonstrated for wine grapes, where microbial communities influence flavor and aroma compounds. The interaction between cannabinoid/terpene production and endorhiza composition in Cannabis remains an open area of investigation.

## Cannabinoid-Microbiome Correlations

The second experiment included cannabinoid profiling of plants, revealing significant correlations between cannabinoid profiles and [[weighted-unifrac-strain-clustering-cannabis-endorhiza-community-structure]] (unweighted Mantel r-stat: 0.863, p = 0.001). However, interpretation is complicated by the confounding effect of soil type — plants from one soil type had both higher THC concentrations and different [[soil-physicochemical-properties-cannabis-microbiome-assembly-winston]], making it difficult to disassociate microbiome-cannabinoid associations from soil-cannabinoid relationships.

## Sampling and Methodology

Understanding the methodology is critical for interpreting these findings:

- Samples were collected from organically-grown plants in Vista and Orange County, California
- Roots were surface-sterilized with alcohol and sterile water before DNA extraction
- DNA was isolated using the PowerSoil DNA Isolation Kit with a modified heating step (65°C for 10 minutes)
- The V4 region of 16S rRNA was sequenced on Illumina MiSeq using Earth Microbiome Project standard protocols
- Experiment 1 samples were rarified to 3,000 sequences; Experiment 2 to 45,000 sequences
- Taxonomy was assigned using the RDP classifier trained on Greengenes database

## Cultivars Studied

| Cultivar | Type | THC:CBD Ratio |
|---|---|---|
| Sour Diesel | C. sativa | High |
| Bookoo Kush | Sativa-dominant hybrid | Moderately high |
| Burmese | Balanced hybrid | Moderate |
| Maui Wowie | C. sativa | High |
| White Widow | Balanced hybrid | Moderate |

## Significance for the Cannabis Industry

As the legal cannabis industry continues to mature, understanding the endorhiza microbiome has commercial implications:

- **Consistency and quality control** — cultivar-specific microbiome profiles could serve as biomarkers for authentication and quality assurance, distinguishing genuine cultivar products from counterfeits
- **Inoculant development** — understanding which endorhiza taxa are naturally enriched in high-performing cultivars could guide the development of targeted biological amendments
- **Living soil product formulation** — compost teas and biological inoculants could be optimized for specific cultivar-microbe partnerships rather than using generic microbial mixes
- **[[medicinal-mushroom-cancer-regulatory-frameworks]]** — microbial testing requirements for cannabis products may eventually need to account for the distinction between pathogenic organisms and beneficial endorhiza residents

## Related Concepts

- [[rhizosphere-microbiome-two-tier-selection-model]]
- [[edaphic-factors-microbiome-structuring]]
- [[cultivar-specificity-plant-microbiome]]
- [[16s-rrna-sequencing-microbiome-analysis-cannabis]]

## See Also

- Winston ME et al. (2014) "Understanding Cultivar-Specificity and Soil Determinants of the Cannabis Microbiome." PLoS ONE 9(6): e99641
