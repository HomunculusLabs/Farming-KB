---
title: Rhizosphere Microbiome Two-Tier Selection Model
created: 2026-05-11
updated: 2026-05-11
type: concept
tags: [soil, microbes, cannabis, mycorrhizae]
sources: [raw/papers/understanding-cultivar-specificity-cannabis-microbiome.md]
---

# Rhizosphere Microbiome Two-Tier Selection Model

## Overview

The two-tier selection model describes how microbial communities associated with plant roots are structured through two sequential filtering processes. First, soil type ([[cannabinoid-microbiome-correlation-confounded-edaphic-factors]]) determines the composition of the local soil microbiota and the initial shift into the nutrient-rich rhizosphere. Second, host plant genotype selects for specific microorganisms that colonize the endorhiza (root interior). This model was validated in the landmark 2014 study by Winston et al. examining five Cannabis cultivars and remains a foundational framework for understanding plant-microbiome interactions in agricultural systems.

## Historical Development

The concept of a two-step root colonization process emerged from earlier work by Bulgarelli et al. (2012, 2013) and Lundberg et al. (2012), who independently proposed that root-associated microbiota are first recruited from the surrounding soil environment through rhizodeposition (the release of exudates, mucilage, and sloughed cells from roots), and then fine-tuned by host genotype-dependent selection. The [[winston-cannabis-microbiome-study-design]] by Winston et al. (2014) provided some of the earliest experimental validation of this model in a commercially important crop species, using controlled experiments across multiple cultivars and soil types.

Prior to this model, microbial ecologists debated whether soil properties or plant genotype was the primary determinant of root-associated communities. The two-tier model resolved this debate by showing that both factors operate, but at different spatial scales — soil at the ecosystem level and genotype at the tissue level.

## Tier 1: Soil-Derived Community Selection

The first tier of selection is driven entirely by abiotic soil properties. The bulk soil microbiome serves as the reservoir from which rhizosphere communities are drawn. Key [[edaphic-determinants-cannabis-microbiome-community-structure]] include:

- **Nitrogen concentration** — the single strongest predictor of community structure (Mantel r-stat: 0.465 weighted, 0.630 unweighted)
- **Salinity** — second strongest factor (r-stat: 0.437 weighted, 0.620 unweighted)
- **Total organic carbon** — (r-stat: 0.330 weighted, 0.512 unweighted)
- **Water content** — (r-stat: 0.281 weighted, 0.466 unweighted)
- **pH** — weakest of the tested factors (r-stat: 0.221 weighted, 0.292 unweighted)

When Cannabis plants were grown in different soil types, the resulting rhizosphere communities were significantly more similar to their respective bulk soils than to each other, confirming that soil properties are the primary determinant at this stage. This was demonstrated when White Widow plants grown in two different soils showed endorhiza communities that shared significantly more OTUs with their own soil (mean = 2934) than with the alternate soil (mean = 2162, t = 10.05, p = 1.2e-15).

The relative ranking of edaphic factors remained consistent across both weighted and unweighted analyses, suggesting that these factors influence both which taxa are present and their relative abundances. Nitrogen's dominance as a community structuring factor aligns with its fundamental role in microbial metabolism and growth.

## Tier 2: Host Genotype-Dependent Selection

The second tier operates as microorganisms migrate from the rhizosphere into plant tissues. At this stage, host plant genotype (cultivar) becomes the dominant factor in structuring the endorhiza community. This was clearly demonstrated in the Cannabis microbiome study:

- Endorhiza communities clustered significantly by strain when using [[weighted-unifrac-strain-clustering-cannabis-endorhiza-community-structure]] (ADONIS: R² = 0.59, p = 0.004)
- Rhizosphere and bulk soil communities did not show significant strain-level differentiation
- Strain effects were observed in OTU **abundances** (weighted analysis) but not in OTU **presence/absence** (unweighted analysis), meaning cultivar selection primarily alters the relative proportions of already-present taxa rather than introducing entirely new ones

This finding has profound implications: the plant does not create new microbial species in its roots, but rather selectively enriches or depletes populations from the soil-derived community based on root chemistry, immune responses, and exudate profiles that vary between cultivars.

## Mechanism of Genotype-Based Selection

The mechanism by which host genotype selects endorhiza communities involves several plant-mediated processes:

1. **Root exudates** — different cultivars produce different profiles of sugars, amino acids, organic acids, [[plant-defense-mechanisms]] that selectively feed certain microbial populations
2. **Immune signaling** — plant innate immune responses recognize and limit colonization by certain microbial taxa while permitting others
3. **Root architecture** — differences in root branching patterns, root hair density, and tissue structure create different ecological niches
4. **Secondary metabolites** — in Cannabis specifically, cannabinoid and terpene production may influence the root microbiome through antimicrobial or signaling properties
5. **Oxygen gradients** — root anatomy creates micro-oxic to aerobic zones that differentially favor different microbial functional groups

## Phylum-Level Shifts Across Compartments

The transition from bulk soil through the rhizosphere to the endorhiza produces predictable changes in microbial composition:

| Compartment | Acidobacteria | Proteobacteria | Actinobacteria |
|---|---|---|---|
| Bulk soil | High | Moderate | Moderate |
| Rhizosphere | Decreasing | Increasing | Increasing |
| Endorhiza | Dramatically reduced | Dominant | Enriched |

The most significant individual change was the decrease in Acidobacteria from order iii1-15 in endorhiza samples (Bonferroni-corrected ANOVA: p = 1.12e-7). Acidobacteria are typically oligotrophic organisms adapted to low-nutrient conditions, so their reduction in the carbon-rich rhizosphere and endorhiza environments is consistent with known ecological preferences. Of 51 OTUs significantly differentiating between sample types, 17 that increased in abundance within the Cannabis endorhiza were predominantly Proteobacteria, including several from the Rhizobiales order — many of which are known endophytic colonizers.

## Alpha Diversity Gradient

Biodiversity decreases progressively from bulk soil to the endorhiza interior:

- **Bulk soil**: highest diversity (chao1: m = 4947)
- **Rhizosphere**: slight reduction (chao1: m = 4525)
- **Endorhiza**: dramatic reduction (chao1: m = 3321)

This pattern is consistent with the two-tier model — each filtering step reduces community complexity as the environment becomes more selective. The relatively modest drop from bulk soil to rhizosphere suggests that the rhizosphere is broadly permissive, while the sharp decline into the endorhiza reflects the stronger selective pressure of the plant host.

## Beta Diversity Relationships

Distances between microbial communities follow a clear hierarchy:

- Rhizosphere-to-bulk-soil distances are significantly lower than rhizosphere-to-endorhiza distances (both weighted and unweighted, p < 0.001)
- Rhizosphere-to-endorhiza distances were not significantly different from bulk-soil-to-endorhiza distances
- This indicates that the endorhiza represents a distinct community regardless of which soil compartment it is compared against

The high correlation between bulk soil and rhizosphere OTU abundances (Pearson's rho: 0.92) compared to the lower correlation between rhizosphere and endorhiza (rho: 0.63) and bulk soil and endorhiza (rho: 0.42) quantitatively confirms the progressive divergence predicted by the model.

## Evidence from Cannabis Cultivars

The two-tier model was tested across five Cannabis cultivars (Burmese, BooKoo Kush, Sour Diesel, White Widow, Maui Wowie) in two experiments. Key findings supporting the model:

1. Soil type had the strongest effect on both OTU presence/absence (657 significant OTUs) and abundance (690 significant OTUs)
2. Strain had no significant unweighted OTU differences (0 significant OTUs) but strong weighted differences (71 significant OTUs), confirming abundance-based rather than compositional selection
3. Core endorhiza community members (Pseudomonas, Cellvibrio, Oxalobacteraceae, Xanthomonadaceae, Actinomycetales, Sphingobacteriales) were maintained across all cultivars despite strain-specific differences in relative abundance
4. Methylophilus explained significant strain-level differentiation, comprising 13% of the Bookoo Kush endorhiza but only 0.13% of Burmese and was absent from Sour Diesel

## Implications for Cultivation

Understanding the two-tier selection model has direct applications for cannabis and other crop cultivation:

- **Soil management is foundational** — because tier 1 selection is soil-driven, building healthy, diverse soil biology provides the raw material from which beneficial root communities are drawn
- **Living soil approaches align naturally** — maintaining diverse microbial populations in the soil maximizes the pool from which genotype-specific selection can draw
- **Cultivar-microbe specificity matters** — different cultivars will select different microbial partners from the same soil, suggesting that inoculant strategies may need to be cultivar-specific
- **Edaphic testing informs practice** — nitrogen, salinity, carbon, and water content all significantly shape the foundation microbial community that interacts with plant roots

## Limitations and Open Questions

Several questions remain about the two-tier model that warrant further investigation:

- The relative strength of tier 1 vs. tier 2 selection likely varies with plant age, growth stage, and environmental stressors, but these dynamics have not been fully characterized
- The model has been primarily validated in agricultural settings; whether it applies equally to wild plant-microbiome systems is less clear
- Fungal communities, including mycorrhizal partners, may follow different selection rules than [[cannabis-rhizosphere-bacterial-communities]], as the Cannabis study focused exclusively on 16S rRNA bacterial sequencing
- The interaction between the two tiers — whether specific soil communities predispose plants toward particular endorhiza profiles — remains an area of active research
- Temporal dynamics, such as how the model operates during seedling establishment versus mature plant maintenance, need more detailed study

## Related Concepts

- [[cannabis-endorhiza-bacterial-communities]]
- 
- [[cultivar-specificity-plant-microbiome]]
- living soil microbial food web

## See Also

- Winston ME et al. (2014) "Understanding Cultivar-Specificity and Soil Determinants of the Cannabis Microbiome." PLoS ONE 9(6): e99641
