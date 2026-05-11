---
title: Two-Tier Selection Model
aliases:
  - Two tier selection
  - [[rhizosphere-microbiome-selection-model]]
  - Soil-plant selection
tags:
  - microbiology
  - rhizosphere
  - plant-microbe-interactions
  - ecology
  - soil-science
created: 2026-05-11
source: understanding-cultivar-specificity-cannabis-microbiome.md
---

# Two-Tier Selection Model

The two-tier selection model is a framework for understanding how plant-associated microbial communities are assembled. It describes a hierarchical process whereby edaphic (soil) factors primarily determine the composition of rhizosphere and root-inhabiting bacterial communities at the first tier, while plant genotype-dependent selection shapes the endorhiza (internal root) community at the second tier.

## Overview

The model was developed to explain the observation that while soil type strongly predicts which bacteria are present in the general soil and rhizosphere environment, the microbial communities living inside plant roots show a much stronger influence from the host plant's genotype. This creates two distinct filters that act sequentially on the available microbial pool.

Understanding this model is essential for anyone working with plant-microbiome interactions, as it provides a predictive framework for how microbial communities will respond to changes in soil management, cultivar selection, or growing conditions. The sequential nature of the two filters means that manipulating soil properties alone cannot fully control the endorhiza community, and conversely, breeding for beneficial root traits cannot overcome fundamentally unsuitable soil conditions.

## First Tier: Soil Determinism

The first tier of selection is driven by edaphic factors—physical and chemical properties of the soil that shape the local microbial reservoir. These factors establish the baseline community from which all subsequent selection occurs. Key soil determinants include:

- **pH**: Often the single strongest predictor of soil [[edaphic-factors-microbial-community-structure]]. Even small pH differences (0.5 units) can shift which taxa dominate, as different bacterial groups have distinct pH optima for growth and survival.
- **Total organic carbon**: Influences the energy available for microbial metabolism. Higher organic carbon generally supports more diverse communities with greater biomass.
- **Total nitrogen**: A limiting nutrient that affects community composition. The carbon-to-nitrogen ratio is particularly important in determining which microbial groups can thrive.
- **Salinity**: Affects osmotic stress tolerance of different microbial groups. Halotolerant and halophilic organisms are favored in saline soils.
- **Water content**: Determines oxygen availability and diffusion rates. Waterlogged soils favor anaerobic organisms, while well-drained soils support aerobic communities.
- **Physical composition**: Sand, silt, and clay ratios affect water retention, nutrient availability, and habitat structure. Clay-rich soils provide more surface area for microbial colonization.

The local soil microbiota serves as the source pool from which rhizosphere communities are drawn. When plants exude compounds into the rhizosphere, they create a nutrient-rich environment that shifts community composition from the bulk soil baseline, but the available taxa are fundamentally constrained by what the soil type can support. This means that two identical plants grown in different soils will develop different rhizosphere communities, even though their endorhiza communities may eventually converge if they share the same genotype.

### Edaphic Gradients and Community Thresholds

Research has shown that certain edaphic parameters exhibit threshold effects on microbial communities. For example, pH values below 5.5 tend to favor Acidobacteria and certain Firmicutes, while values above 7.0 shift the community toward Proteobacteria and Bacteroidetes. These thresholds create relatively discrete community types rather than continuous gradients, which is why soil type emerges as such a strong predictor in multivariate analyses.

BEST (Best Subset of Environmental Variables with Maximum Rank Correlation) analysis has been used to identify which edaphic factors explain the most variation in community structure. In Cannabis studies, pH and organic carbon content consistently ranked as the top predictors, followed by salinity and water content.

## Second Tier: Host Genotype Selection

The second tier operates when bacteria migrate from the rhizosphere into plant tissues (the endorhiza). At this stage, plant-specific factors become the dominant selective force, often overriding the soil-derived community structure established in tier one. The mechanisms include:

- **Root exudate chemistry**: Different cultivars produce different profiles of sugars, amino acids, organic acids, [[plant-defense-chemistry-and-secondary-metabolites]]. These compounds selectively feed or inhibit specific bacterial taxa, creating a genotype-specific chemical environment inside the root.
- **Root architecture**: Physical root structure determines which bacteria can physically access and colonize internal tissues. Root branching patterns, cortex cell wall composition, and the presence of aerenchyma all influence colonization pathways.
- **Immune responses**: [[plant-innate-immunity-pti-eti-defense]] selectively permits or rejects colonization by different bacterial groups. Pattern-triggered immunity and effector-triggered immunity act as gatekeepers at the root interface.
- **Secondary metabolites**: Compounds like terpenes, cannabinoids, and phenolics can have [[medicinal-mushroom-antimicrobial-properties]] that further filter the community, allowing only tolerant or resistant strains to persist inside root tissues.

This second-tier filtering results in endorhiza communities that are significantly more similar among plants of the same cultivar than among different cultivars, even when grown in the same soil. The strength of this filtering can be quantified using beta-diversity metrics such as weighted and [[weighted-vs-unweighted-unifrac-cannabis-strain-microbiome]] distances, tested for significance with PERMANOVA (ADONIS).

### Molecular Basis of Genotype Selection

At the molecular level, the second tier likely involves specific receptor-ligand interactions between plant cells and bacterial surface molecules. Plants can detect microbe-associated molecular patterns (MAMPs) such as flagellin, lipopolysaccharide, and peptidoglycan, and mount differential immune responses depending on the bacterial identity. Additionally, some endophytes produce effectors that actively suppress plant immunity, facilitating their own colonization. The specific complement of MAMP receptors and immune signaling components varies between cultivars, providing a mechanistic basis for genotype-dependent selection.

## Predictions of the Model

The two-tier selection model generates several testable predictions about microbial community structure:

1. **Phylum-level shifts**: Dramatic reduction in Acidobacteria abundance from soil to endorhiza, as these oligotrophic organisms are poorly adapted to the carbon-rich root interior.
2. **Cultivar-specific endorhiza**: Endorhiza communities should cluster by host genotype when soil type is controlled, showing statistically significant separation in ordination space.
3. **Soil-dependent rhizosphere**: Rhizosphere communities should cluster by soil type rather than by plant genotype, as the first-tier filter dominates at this compartment.
4. **Intermediate rhizosphere**: Rhizosphere communities represent a transitional state between bulk soil and endorhiza, showing influence from both tiers but not fully belonging to either compartment.
5. **Core microbiome persistence**: A set of broadly capable taxa should persist across all sample types, representing organisms adapted to both soil and root environments simultaneously.

## Evidence from Cannabis

The model has been tested in Cannabis using five distinct cultivars (Sour Diesel, Bookoo Kush, Burmese, White Widow, and Maui Wowie) across multiple growing locations in California. Two experiments were conducted: the first with minimal edaphic variation and the second with significant soil differences between sites. Key findings supporting the model include:

- Endorhiza communities showed significant cultivar-specificity (ADONIS R² = 0.59, p = 0.004 for weighted UniFrac), confirming strong second-tier selection even across different soil types.
- Rhizosphere communities did not cluster significantly by cultivar (p = 0.10), consistent with first-tier soil determinism dominating at this compartment.
- Bulk soil communities were determined primarily by edaphic factors, showing clear separation by soil type in PCoA ordination.
- A core endorhiza community of Pseudomonas, Cellvibrio, Oxalobacteraceae, Xanthomonadaceae, Actinomycetales, and Sphingobacteriales was maintained across all cultivars, representing taxa that passed both selection filters.

The genus Methylophilus was found to explain a significant portion of cultivar-level differences, comprising 13% of the Bookoo Kush endorhiza community but only 0.13% in Burmese and being absent entirely in Sour Diesel. This suggests specific metabolic compatibility between certain cultivars and particular bacterial taxa, possibly related to root exudate profiles.

## Comparison with Other Models

### Single-Filter Models
Earlier models proposed that either soil or plant genotype alone determined root-associated communities. Evidence for both positions existed in the literature, leading to conflicting conclusions. The two-tier model reconciles this apparent contradiction by assigning each factor to a different spatial compartment.

### Core Microbiome Concept
The concept of a core microbiome (consistently present taxa across samples) is compatible with but distinct from the two-tier model. The core community represents taxa capable of surviving both selection filters, while the model explains the variable fraction that differs between conditions.

### Habitat Filter Theory
General ecological habitat filter theory posits that environmental conditions filter species from a regional pool. The two-tier model is a specific application of this theory to the plant-microbiome context, with the added complexity of a biotic filter layered on top of the abiotic filter.

## Agricultural Implications

Understanding the two-tier selection process has practical applications for crop management and breeding programs:

- **Soil management**: Since the first tier depends on soil properties, managing soil health directly influences the pool of potential beneficial microbes available for root colonization.
- **Cultivar selection**: Breeding programs can indirectly select for beneficial microbiomes by selecting for root traits and exudate profiles that favor desirable microbial partners.
- **Inoculant design**: Effective microbial inoculants must be compatible with both the target soil type and the host cultivar's internal selection mechanisms for successful establishment.
- **Terroir effects**: The model provides a mechanistic explanation for how growing region and variety interact to produce unique microbial signatures that may influence crop quality characteristics.

## Limitations

- The model primarily describes bacterial communities; fungal selection mechanisms may follow different rules, particularly for mycorrhizal associations.
- Temporal dynamics such as seasonal changes and plant developmental stage add complexity not captured by the static two-tier framework.
- The relative strength of each tier likely varies across plant species and environmental conditions.
- Some studies have found minimal cultivar effects compared to edaphic factors, suggesting the second tier may be weaker in certain plant systems.
- The model does not explicitly address the role of horizontal gene transfer between root-associated bacteria, which could blur the boundaries between soil-selected and plant-selected communities.
- Interactions between the two tiers, such as plant-mediated soil conditioning (where root exudates alter soil chemistry over time), create feedback loops that the model treats as separate processes.

## References

- Winston ME et al. (2014) Understanding Cultivar-Specificity and Soil Determinants of the Cannabis Microbiome. PLoS ONE 9(6): e99641.

## See Also

- [[endorhiza-microbiome]]
- cannabis rhizosphere
- soil physicochemical factors and microbiome
- [[cannabis-cultivar-specificity]]
