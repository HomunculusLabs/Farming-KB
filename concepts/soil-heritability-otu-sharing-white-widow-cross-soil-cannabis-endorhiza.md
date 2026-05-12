---
title: Soil Heritability of OTU Sharing in Cannabis Endorhiza
topic: cannabis microbiome
related: [[two-tier-selection-model]], cannabis microbiome, [[white-widow-cannabis]], bulk soil rhizosphere recruitment, [[cultivar-specificity-microbiome]], endorhiza microbiome, otu sharing analysis
tags: [microbiome, cannabis, endorhiza, soil, otu, heritability, winston-2014]
---

# Soil Heritability of OTU Sharing in Cannabis Endorhiza

**Soil heritability of OTU sharing** refers to the empirical observation that the [[cannabis-core-endorhiza-microbiome|endorhiza]] microbial communities of [[cannabis-microbiome-best-analysis-edaphic-factor-ranking]] plants are significantly more similar to the [[rhizosphere-vs-bulk-soil-microbiome|bulk soil]] in which they grow than to alternative soils, demonstrating that the surrounding soil serves as the primary source pool for root-colonizing microbes. This concept was directly tested and validated by Winston et al. (2014) in their landmark study of cultivar-specificity and soil determinants of the Cannabis microbiome.

## Background and Hypothesis

A central question in [[cultivar-specificity-plant-microbiomes|plant microbiome]] research is the degree to which root-associated microbial communities are inherited from the surrounding environment versus selected by host plant genetics. The [[two-tier-selection-model]] proposes a two-step process: first, bulk soil microbes serve as the available source pool, and second, host plant factors selectively filter and enrich specific taxa from that pool into the [[rhizosphere-ecology|rhizosphere]] and [[cannabis-core-endorhiza-microbiome|endorhiza]].

Prior to the work of Winston et al. (2014), this two-tier model had been proposed and supported in several other plant systems, including studies of maize, barley, Arabidopsis, and various crop species. However, the Cannabis microbiome had not yet been systematically examined for evidence of soil-derived microbial inheritance. Given the increasing commercial and scientific interest in Cannabis cultivation, understanding the relative contributions of soil versus genotype to the root microbiome carried both academic significance and practical relevance for growers seeking to optimize plant health and [[fungal-elicitors-enhanced-secondary-metabolite-production]] through microbial management.

## Experimental Design

Winston et al. (2014) designed a cross-soil experiment using the [[white-widow-cannabis|White Widow]] cultivar to directly test whether endorhiza microbes are inherited from the surrounding soil. White Widow plants were grown in two distinct soil types under controlled conditions:

- **MB soil** — a mineral-based growing medium
- **OC soil** — an organic compost-based growing medium

By growing the same cultivar in two different soils, the experiment held host genetics constant while varying the soil environment. This controlled design allowed the researchers to isolate the soil effect on endorhiza community composition and assess the degree to which OTU sharing between endorhiza and bulk soil was driven by soil proximity rather than plant genotype alone.

Root endorhiza samples and corresponding bulk soil samples were collected from each plant, and microbial communities were profiled using high-throughput 16S rRNA gene sequencing. Operational taxonomic units (OTUs) were clustered at 97% sequence similarity, and pairwise OTU sharing was calculated between each endorhiza sample and both soil types.

## Statistical Analysis

The key statistical test involved pairwise OTU sharing comparisons between endorhiza and bulk soil samples. For each endorhiza sample, researchers calculated the number of OTUs shared with:

1. The **home soil** — the soil in which that plant was actually grown
2. The **away soil** — the alternative soil type not associated with that plant

This produced a paired comparison for each of **n = 45 paired samples**. A paired t-test was used to determine whether endorhiza communities shared significantly more OTUs with their home soil than with the away soil.

The paired design is a methodological strength, as it controls for plant-level variation in microbial community richness and composition. Each plant serves as its own control, isolating the soil-type effect from other sources of variation such as plant age, root architecture, and microenvironmental conditions.

## Results

The results provided strong statistical support for soil-derived microbial inheritance in the Cannabis endorhiza:

| Comparison | Mean Shared OTUs | Statistic |
|---|---|---|
| Endorhiza vs. home soil | 2,934 | — |
| Endorhiza vs. away soil | 2,162 | — |
| Paired t-test | — | t = −10.05, p = 1.209 × 10⁻¹⁵ |

The highly significant difference (p = 1.209e-15) demonstrates that Cannabis endorhiza communities are far more similar to the soil they grew in than to a different soil type. The magnitude of the effect — a difference of approximately 772 shared OTUs on average between home and away soil comparisons — underscores the practical importance of soil type in shaping the root microbiome.

This pattern held consistently across the 45 paired samples, indicating a robust and reproducible effect. The enormous t-statistic (−10.05) and near-zero p-value leave essentially no statistical doubt that the observed OTU sharing asymmetry reflects a genuine biological phenomenon rather than sampling artifact.

Notably, the mean of 2,162 shared OTUs with the away soil indicates that some overlap exists between the two soil microbial communities, as expected. The MB and OC soils are not completely dissimilar, and both contain cosmopolitan taxa capable of colonizing roots. The key finding is not the absence of away-soil sharing but the significantly elevated sharing with the home soil.

## Interpretation Within the Two-Tier Selection Model

These findings validate the **first tier** of the [[two-tier-selection-model]]: bulk soil microbes constitute the primary source pool from which rhizosphere and endorhiza communities are drawn. Without a soil-derived inoculum source, the endorhiza cannot assemble a community reflective of the local soil environment.

However, the results do not imply that the endorhiza is a passive reflection of soil composition. Winston et al. (2014) also demonstrated [[cultivar-specificity-microbiome|cultivar-specific selection]] effects, showing that different Cannabis cultivars grown in the same soil developed distinct endorhiza communities. This confirms that the **second tier** of the model — host-driven selective filtering — operates concurrently with soil-derived sourcing.

In essence, the soil provides the raw microbial material, and the plant selectively shapes which taxa from that pool successfully colonize the root interior. Both processes are necessary and neither alone fully explains [[weighted-unifrac-strain-clustering-cannabis-endorhiza-community-structure]].

## Comparison to Other Plant Systems

The Cannabis findings align closely with observations in other well-studied plant-microbiome systems. Across these systems, a consistent pattern emerges: soil type is the dominant predictor of root microbiome composition, while host genotype modulates community structure within the constraints imposed by the available soil microbial pool.

- **Maize**: Peiffer et al. (2013) showed that soil type was the strongest predictor of rhizosphere community composition across diverse field sites, while host genotype exerted a weaker but significant effect. This hierarchical ordering of soil over genotype mirrors the Cannabis results.
- **Barley**: Bulgarelli et al. (2015) demonstrated that the barley root microbiome is recruited primarily from the surrounding soil, with host genotype acting as a secondary filter. Their work explicitly framed soil as the "reservoir" from which root communities are drawn.
- **Arabidopsis**: Lundberg et al. (2012) found that Arabidopsis root microbiota were largely derived from the soil, with endophytic communities representing a subset of the broader rhizosphere pool. The nested subset relationship between soil, rhizosphere, and endorhiza is analogous to the pattern observed in Cannabis.
- **Wheat**: Donn et al. (2015) reported similar soil-driven recruitment patterns in wheat, with soil type explaining the largest proportion of variance in root-associated communities. Inoculation experiments further confirmed that soil amendments shifted the root microbiome in predictable directions.

The Winston et al. (2014) Cannabis results are consistent with this broader pattern, reinforcing the generality of soil-derived microbial inheritance across diverse plant taxa. The study adds to this literature by using a cross-soil experimental design with a single cultivar, which provides a particularly clean test of the soil effect free from genotype confounds.

## Implications for Cannabis Cultivation

The finding that soil type strongly determines the available microbial pool has direct practical implications for Cannabis cultivation:

- **Soil selection matters**: Changing the soil type fundamentally alters the microbial inoculum available for root colonization, even when using the same cultivar. Growers seeking specific microbial associations must consider soil composition as a primary variable.
- **Microbial pool is a constraint**: Cultivar-specific selection can only act on the microbes present in the soil. A cultivar may preferentially enrich certain taxa, but it cannot recruit microbes absent from the source pool. This means soil management and [[ingham-compost-tea-recipe-ratios|compost tea]] applications can expand the range of taxa available for selection.
- **Reproducibility across grows**: Consistent soil media across growing cycles promotes reproducible microbial communities in the endorhiza, which may contribute to more predictable plant health and secondary metabolite production.
- **Breeding considerations**: When evaluating cultivar-specific microbiome interactions, the soil environment must be controlled and reported, as soil effects can easily confound genotype-level conclusions.
- **Indoor vs. outdoor cultivation**: Outdoor Cannabis grown in native soils will recruit regionally characteristic microbiomes, while indoor operations using manufactured or amended substrates have greater control over the initial microbial pool. The OTU sharing data suggest that indoor growers who standardize their soil mix can achieve more consistent endorhiza communities across harvests.
- **Soil health as plant health**: Because the endorhiza microbiome is inherited from the soil, practices that degrade soil microbial diversity — such as excessive sterilization, monoculture without rotation, or heavy chemical inputs — may narrow the functional potential of the root microbiome.

## Concept of Microbial Inheritance

The term **microbial inheritance** in the context of the plant microbiome refers to the process by which plants acquire their root-associated microbial communities from the surrounding environment, particularly the soil. Unlike genetic inheritance, microbial inheritance is an ecological process mediated by proximity, diffusion, root exudation, and selective colonization. The [[cannabis-endorhiza-otu-pooling-and-strain-core-microbiome]] sharing results provide quantitative evidence for this form of inheritance, showing that the soil environment contributes a substantially larger share of endorhiza OTUs than a non-associated soil.

This concept is distinct from vertical transmission of microbiota (e.g., seed-associated microbes) and refers specifically to the horizontal acquisition of microbes from the growth substrate. In most agricultural and ecological settings, soil-derived horizontal acquisition is the dominant pathway for root microbiome assembly.
