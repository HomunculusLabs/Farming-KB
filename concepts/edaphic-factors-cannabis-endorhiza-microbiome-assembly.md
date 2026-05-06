---
title: Edaphic Factors in Cannabis Endorhiza Microbiome Assembly
created: 2026-04-28
tags:
  - cannabis
  - microbiome
  - edaphic
  - endorhiza
  - soil-science
  - rhizosphere
  - beta-diversity
  - community-assembly
date: 2026-04-28
updated: 2026-04-28
sources:
  - Winston ME et al. (2014) "Understanding Cultivar-Specificity and Soil Determinants of the Cannabis Microbiome." PLoS ONE 9(6): e99641.
type: concept
---

# Edaphic Factors in Cannabis Endorhiza Microbiome Assembly

The assembly of microbial communities in and around Cannabis roots is governed by a hierarchy of factors in which soil physicochemical properties (edaphic factors) are the primary determinant of overall community composition, while cultivar genotype fine-tunes the endorhiza community structure. This two-tier model, supported by the landmark Winston et al. (2014) study, has significant implications for understanding plant-microbe interactions in this commercially and medicinally important crop.

## Dominance of Soil Type Over Community Composition

Across two independent experiments involving five Cannabis cultivars (Sour Diesel, Bookoo Kush, Burmese, White Widow, and Maui Wowie) grown in sandy loam soils, soil type was overwhelmingly the strongest predictor of microbial community composition. In the second experiment, which featured significant edaphic variation between two soil types (Mo-Bio soil and Orange County soil), unweighted UniFrac analysis showed soil type accounted for 32% of community variation (ADONIS: R² = 0.32, p = 0.001). When both experiments were pooled, soil type remained highly significant (ADONIS: R² = 0.196, p = 0.001 for unweighted; R² = 0.323, p = 0.001 for weighted UniFrac).

The number of significant OTU differences attributable to soil type was far greater than for any other factor: 690 significant OTUs by weighted ANOVA and 657 by unweighted g-test with FDR correction. This dwarfs the 51 significant OTUs for sample type and 71 for strain in weighted analysis. The overwhelming dominance of soil in determining which organisms are present underscores the importance of soil management in Cannabis cultivation.

## Soil Physical and Chemical Profiles

The five soil types across both experiments shared a sandy loam texture but varied substantially in chemical properties:

- **Mo-Bio soils (Experiment 1)**: pH 6.80-6.94, salinity 7.10-7.44, total nitrogen 1.30-1.51%, total organic carbon 3.31-5.00%, water content 0.101-0.178. These were relatively nitrogen-rich, moderately saline soils with low to moderate organic matter.
- **Mo-Bio soil (Experiment 2)**: pH 6.63, salinity 5.12, total nitrogen 0.26%, total organic carbon 3.02%, water content 0.113. This soil had notably lower nitrogen than the first-experiment Mo-Bio soils.
- **Orange County soil (Experiment 2)**: pH 6.77, salinity 1.73, total nitrogen 0.53%, total organic carbon 20.0%, water content 0.371. This soil was dramatically different, with far lower salinity, moderate nitrogen, extremely high organic carbon, and substantially higher water retention.

These edaphic differences provided the variation necessary to test the two-tier selection model with statistical power. The Orange County soil, with its extraordinarily high organic carbon content (20% versus 3-5% in Mo-Bio soils), represented a fundamentally different soil environment despite the shared sandy loam texture classification.

## Hierarchy of Edaphic Influences

Mantel tests correlating edaphic variables with community beta-diversity revealed a consistent ranking of importance across both weighted and unweighted analyses:

1. **Nitrogen** was the strongest structuring factor (weighted: r = 0.465, p = 0.001; unweighted: r = 0.630, p = 0.001). Total nitrogen concentration in the soil was the single most powerful edaphic predictor of which microbes would be present and in what abundance.
2. **Salinity** was the second most important factor (weighted: r = 0.437; unweighted: r = 0.620). Electrical conductivity measurements showed significant variation between the two soil types in the second experiment (7.15 vs 1.73).
3. **Total organic carbon** ranked third (weighted: r = 0.330; unweighted: r = 0.512). The Orange County soil contained dramatically more organic carbon (20.0%) than the Mo-Bio soils (3.0 to 5.0%).
4. **Water content** was fourth (weighted: r = 0.281; unweighted: r = 0.466), with Orange County soil showing substantially higher moisture retention (0.371 vs 0.101 to 0.178).
5. **pH** was the weakest but still highly significant factor (weighted: r = 0.221; unweighted: r = 0.292). All soils were mildly acidic (pH 6.63 to 6.94), with the relatively narrow pH range possibly limiting its discriminatory power in this dataset.

A BEST (Bio-Env) analysis determined that the optimal combination of just three edaphic variables, Nitrogen, Carbon, and Water content, explained the maximum variance in community data (rho = 0.632). This parsimonious three-factor model captured the majority of edaphic influence without requiring pH or salinity.

## Edaphic Effects on Alpha Diversity

Edaphic factors also influenced the richness of microbial communities. The Mo-Bio soil supported higher alpha diversity in both bulk soil (chao1: mean = 5597) and rhizosphere (chao1: mean = 4859) compared to Orange County soil (bulk: chao1 = 4296; rhizosphere: chao1 = 3913). However, endorhiza diversity converged between soil types (Mo-Bio: chao1 = 3325; Orange County: chao1 = 3311), suggesting that host genotype-mediated selection imposes a ceiling on endophyte diversity regardless of soil conditions.

The consistent pattern of declining alpha diversity from bulk soil to rhizosphere to endorhiza was observed across all soil types: bulk soil was richest, rhizosphere showed a slight reduction, and the endorhiza showed a dramatic drop. This filtering pattern supports the two-tier selection model in which the rhizosphere acts as a transitional zone where edaphically determined communities are progressively filtered by root exudates and host immune responses.

## Cultivar Effects Within Edaphic Context

While soil type determined the presence or absence of OTUs (unweighted analysis showed zero significant OTU differences between cultivars), Cannabis strain significantly structured community abundance (weighted analysis: 71 significant OTUs). This means that cultivars select for the same general groups of bacteria from the available soil pool, but modulate their relative abundances differently.

In the second experiment with White Widow and Maui Wowie, strain effects on endorhiza communities were highly significant (weighted ADONIS: R² = 0.59, p = 0.004). The PCoA plots were particularly revealing: in unweighted analysis, PC1 (32.06% variance) was dominated by soil type, while in weighted analysis, PC1 (34.51% variance) was dominated by strain. This demonstrates that composition (who is there) is edaphically determined, while structure (how abundant each member is) is cultivar-dependent.

Key strain-specific OTU differences included the prevalence of Methylophilus, which comprised 13% of the Bookoo Kush endorhiza community but only 0.13% in Burmese and was entirely absent from Sour Diesel. In the second experiment, Sphingomonas wittichii was prevalent in Maui Wowie but not White Widow; this organism can metabolize phenazine-1-carboxylic acid and has been implicated in increased survival in soil environments.

## OTU Sharing and the Two-Step Selection Model

A critical test of the two-tier model involved comparing OTU overlap between endorhiza communities and their own versus foreign soils. White Widow was grown in two different soil types, and the endorhiza shared significantly more OTUs with the soil it was grown in (mean = 2934 shared OTUs) than with the other soil (mean = 2162 shared OTUs, t = -10.05, p = 1.209e-15). This confirmed that endophytic microbes are primarily recruited from the local soil pool, with cultivar-dependent selection acting as a secondary filter.

## Cannabinoid-Edaphic Confound

A notable finding was that THC concentration and composition were significantly correlated with endorhiza community structure (Mantel test: r = 0.863, p = 0.001). However, because THC levels were themselves strongly correlated with edaphic variables (particularly the nitrogen-rich Orange County soil producing higher THC plants), it was not possible to disentangle the direct effects of cannabinoid production on the microbiome from indirect effects mediated through soil chemistry. This confound represents an important methodological challenge for future studies.

## Post-Harvest Effects on Microbiome Interpretation

A comparison between the two experiments revealed an important methodological consideration. Samples in the first experiment were taken 8 weeks post-harvest, while second-experiment samples were taken from actively growing plants 2 weeks before harvest. The post-harvest samples showed dramatically higher Cellvibrio abundance (16.9% vs 0.095%), a known cellulytic bacterium, consistent with early root decay rather than genuine endophytic colonization. This finding cautions against interpreting post-harvest root microbiome data as representative of living plant associations.

## Core Endorhiza Community Across Cultivars

Despite significant cultivar-specific differences in OTU abundance, all Cannabis endorhiza samples maintained a core community of consistent members. This core included Pseudomonas, Cellvibrio, Oxalobacteraceae, Xanthomonadaceae, Actinomycetales, and Sphingobacteriales. With the exception of the aerobic cellulytic bacterium Cellvibrio (now understood to be a decay artifact), all prevalent core members were well-known endophytic bacteria, primarily within the orders Gammaproteobacteria and Alphaproteobacteria.

This observation is consistent with patterns reported from other plant systems, where a relatively small set of generalist endophytes colonizes diverse host species. The stability of this core community across five Cannabis cultivars and three soil types suggests strong selection for these particular taxa within the root interior environment, possibly driven by their ability to metabolize root exudates, evade plant immune responses, or provide benefits to the host.

## Taxonomic Shifts Across Compartments

The transition from bulk soil through rhizosphere to endorhiza was characterized by predictable taxonomic shifts consistent with the two-tier selection model. The most significant change was a dramatic reduction in Acidobacteria from the order iii1-15 within endorhiza samples (Bonferroni-corrected ANOVA: p = 1.12e-7). Acidobacteria, which are often oligotrophic and adapted to low-nutrient conditions in bulk soil, appear to be selected against in the carbon-rich root environment.

Conversely, Proteobacteria and Actinobacteria increased in relative abundance within the endorhiza. Of the 51 OTUs significantly differentiating between sample types, the 17 that increased in abundance within the Cannabis endorhiza were predominantly Proteobacteria, including several from the Rhizobiales order. Strain-level OTU differences were also composed mostly of Proteobacteria, notably from the orders Pseudomonadales, Burkholderiales, Sphingomonadales, and Rhizobiales, with additional contributions from Bacteroidetes (Sphingobacteriales and Flavobacteriales).

## OTU Correlation Between Compartments

The mean abundance of the 51 sample-type-differentiating OTUs was highly correlated between bulk soil and rhizosphere samples (Pearson's rho: 0.92), indicating that the rhizosphere largely preserves the relative abundance structure of the bulk soil community. However, the correlation dropped substantially between rhizosphere and Cannabis endorhiza (rho: 0.63), and was lowest between bulk soil and endorhiza (rho: 0.42). This gradient of decreasing correlation quantifies the progressive reshaping of the microbial community as it transitions from soil to root surface to root interior.

## Cultivar Descriptions and Chemotype Context

The five Cannabis cultivars used in the study represented a range of chemotypes and genetic backgrounds:

- **Sour Diesel**: Cannabis sativa, high THC to CBD ratio
- **Bookoo Kush**: Sativa-dominant hybrid, moderately high THC to CBD ratio
- **Burmese**: Balanced hybrid of C. sativa and C. indica, moderate THC to CBD ratio
- **Maui Wowie**: Cannabis sativa, high THC to CBD ratio
- **White Widow**: Balanced hybrid of C. sativa and C. indica, moderate THC to CBD ratio

The consistent finding of cultivar-specific microbiome structuring across this diverse panel suggests that the phenomenon is generalizable across Cannabis genetic diversity rather than being specific to particular chemotypes or subspecies classifications.

## Future Directions Suggested by the Study

The authors identified several areas requiring further investigation. These include elucidating the role of cultivar on rhizosphere (where the first experiment showed ambiguous results likely due to post-harvest decay artifacts), determining which aspects of host genotype produce the observed microbiome structure across strains, and increased testing of cannabinoids with better experimental designs to decouple cannabinoid effects from edaphic confounds. Time-series sampling of endorhiza communities across the reproductive cycle was also recommended to understand natural variation during plant development.

## Methodological Contributions

The Winston et al. study contributed several methodological advances to the study of Cannabis microbiomes. Their use of 16S rRNA amplicon sequencing with both V3-V5 and V6-V8 primer sets provided a more comprehensive picture of community composition than either primer set alone. Their experimental design, which separated the effects of soil type, cultivar, and sample compartment, established a framework for disentangling the multiple factors that shape the Cannabis root microbiome. The comparison between two independent experiments, while initially intended as replication, became an important methodological lesson about post-harvest sampling artifacts.

## See Also

- [[core-endorhiza-microbiome-proteobacteria-enrichment-cannabis]]

- [[cannabis-microbiome-cultivar-specificity]]
- [[two-tier-selection-model-root-microbiome-assembly]]
- [[cannabis-endorhiza-microbiome]]
- [[rhizosphere-microbiome-selection-model]]
- [[proteobacteria-dominance-cannabis-endorhiza]]
- [[acidobacteria-decline-rhizosphere-endorhiza-transition]]
- [[beta-diversity-root-soil-compartments-cannabis]]
- [[cannabinoid-microbiome-correlation-cannabis]]
- [[cellvibrio-and-root-decay-microbiome]]
