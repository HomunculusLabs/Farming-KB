---
title: "Cannabis Endorhiza Microbiome"
created: 2026-05-11
source: Winston et al. (2014) "Understanding Cultivar-Specificity and Soil Determinants of the Cannabis Microbiome" PLoS ONE
tags: [microbiology, cannabis, endophytes, rhizosphere, plant-microbe-interactions]
---

# Cannabis Endorhiza Microbiome

The endorhiza microbiome refers to the community of bacteria that colonize the internal tissues of plant roots. In Cannabis, this community exhibits significant cultivar-specificity, meaning that different genetic strains of Cannabis host distinct microbial assemblages within their root systems. This was first systematically characterized by Winston et al. (2014), who provided the foundational description of endorhiza-, rhizosphere-, and bulk soil-associated bacterial communities across five distinct Cannabis cultivars, establishing Cannabis as an important model for studying plant-microbiome interactions in a crop that produces numerous secondary metabolic compounds.

## Definition and Scope

The endorhiza is distinguished from the rhizosphere (soil adhering to root surfaces) and bulk soil (soil distant from root influence). Bacteria within the endorhiza are true endophytes — they have crossed the root epidermis and colonized internal root tissues. These communities are typically less diverse than rhizosphere or bulk soil communities but are more tightly coupled to host plant physiology.

In Cannabis, the core endorhiza community across all studied cultivars includes genera from several well-known endophytic lineages: **Pseudomonas**, **Cellvibrio**, members of **Oxalobacteraceae**, **Xanthomonadaceae**, **Actinomycetales**, and **Sphingobacteriales**. With the exception of the aerobic cellulolytic bacterium Cellvibrio, all prevalent members of the core [[weighted-unifrac-strain-clustering-cannabis-endorhiza-community-structure]] are recognized endophytic bacteria primarily within the orders Gammaproteobacteria and Alphaproteobacteria, consistent with observations from other plant systems such as Populus deltoides and [[arabidopsis-thaliana]].

Understanding these endorhiza communities has practical importance because soil microbes play major roles in plant ecology by providing nitrogen fixation, production of growth stimulants, improved water retention, and suppression of root diseases. These vital microbial processes occur predominantly within the rhizosphere and rhizoplane, and are heavily influenced by fungal saprotrophs and plant-mutualists such as endomycorrhizal and ectomycorrhizal fungi. Despite the economic and medicinal importance of Cannabis, relatively little was known about its soil-based microbial associations prior to this work. The study by Winston et al. represented the first comprehensive 16S rRNA gene survey of Cannabis-associated bacterial communities.

Rhizosphere microbiota are highly dynamic, and the composition of bacterial communities can fluctuate in response to seasonal and diel temperature changes, water content, pH, CO₂ concentration, and O₂ levels. Microbial composition in soil depends on complex interactions between the soil type, root zone location, and plant species. While evidence has been found for significant effects of plant cultivar on rhizosphere communities and endomycorrhizal fungal communities, some work suggests that these effects are minimal compared to edaphic factors (particularly pH) or plant growth stage.

## Cultivar-Specificity

Winston et al. demonstrated that when controlling for soil type and sample location, the [[edaphic-factors-microbial-community-structure]] within Cannabis endorhiza was significantly different between plant cultivars. This cultivar effect was detectable using both weighted and unweighted UniFrac distance metrics, though it was more pronounced in weighted analyses, suggesting that cultivar primarily influences the relative abundance of taxa rather than their presence or absence.

Notable cultivar-specific differences included:
- **Methylophilus** comprised 13% of the endorhiza community in Bookoo Kush, 0.13% in Burmese, and was absent entirely in Sour Diesel
- **Sphingomonas wittichii** was prevalent in Maui Wowie endorhiza samples, a species that can metabolize phenazine-1-carboxylic acid and has been implicated in increased survival in soil environments

The significance of strain-level differences was confirmed through ADONIS permutation tests. In the second experiment comparing White Widow and Maui Wowie across two distinct soil types, strain significantly structured endorhiza communities for both weighted (R² = 0.59, p = 0.004) and unweighted (R² = 0.39, p = 0.003) UniFrac analyses. When both experiments were pooled, the strain effect remained highly significant across all samples (weighted R² = 0.301, p = 0.001; unweighted R² = 0.178, p = 0.001).

Interestingly, no significant OTU presence/absence differences were found between cultivars in unweighted analyses of the second experiment (0 significant OTUs by g-test), while 71 OTUs showed significant abundance differences in weighted analyses (ANOVA with FDR correction). This indicates that cultivar selection operates primarily on community structure — the relative proportions of taxa — rather than on which taxa are present.

## Soil Influence on Endorhiza Communities

Despite the strong cultivar signal, soil type remains the dominant factor shaping microbial community composition across all sample types. In pooled analyses, soil type explained the largest proportion of variation in both weighted (R² = 0.323) and unweighted (R² = 0.196) UniFrac analyses. This primacy of soil over host genotype is consistent with findings across many plant systems.

Edaphic factors most strongly correlated with community structure were:
1. **Nitrogen** (r-stat: 0.465 weighted, 0.630 unweighted)
2. **Salinity** (r-stat: 0.437 weighted, 0.620 unweighted)
3. **Total organic carbon** (r-stat: 0.330 weighted, 0.512 unweighted)
4. **Water content** (r-stat: 0.281 weighted, 0.466 unweighted)
5. **pH** (r-stat: 0.221 weighted, 0.292 unweighted)

A BEST (Best Subset of Environmental Variables) analysis determined that the optimal combination of three edaphic factors — Nitrogen, Carbon, and Water — explained the maximum variance in community data (rho = 0.632). All five tested edaphic factors were significantly correlated with community beta-diversity at p = 0.001 for both weighted and unweighted analyses.

Endorhiza communities shared significantly more OTUs with their own soil than with a different soil in which the same strain was grown (mean shared OTUs: 2934 vs 2162, p = 1.2×10⁻¹⁵). This was tested by growing White Widow in two different soil types and comparing OTU overlap between endorhiza and their native versus foreign soil. This result supports the model that endophytic microbes are primarily soil-derived.

## Taxonomic Shifts from Soil to Root

Transitioning from bulk soil through the rhizosphere to the endorhiza, predictable taxonomic shifts occur. The most dramatic change is the decrease in **Acidobacteria** (particularly the order iii1-15) within endorhiza samples, accompanied by an increase in **Proteobacteria** and **Actinobacteria**. Of 51 OTUs significantly differentiating between sample types, 17 increased in abundance within the Cannabis endorhiza relative to the rhizosphere, and these were predominantly Proteobacteria including several from the Rhizobiales order.

Significant OTU abundance differences between strains were composed mostly of differences in Proteobacteria, notably from the orders Pseudomonadales, Burkholderiales, Sphingomonadales, and Rhizobiales. Apart from Proteobacteria, Bacteroidetes orders Sphingobacteriales and Flavobacteriales were also responsible for several significant OTU differences between Cannabis strains.

The mean abundance of differentiating OTUs was highly correlated between bulk soil and rhizosphere (Pearson's rho: 0.92), indicating strong continuity. The correlation dropped substantially between rhizosphere and endorhiza (rho: 0.63), and even further between bulk soil and endorhiza (rho: 0.42). This gradient of decreasing correlation reflects the progressive filtering and selection that occurs as microbes transition from soil to root interior.

## Alpha Diversity Patterns

Alpha diversity follows a consistent pattern across all experiments: highest in bulk soil, slightly reduced in the rhizosphere, and dramatically reduced in the endorhiza. In the second experiment, Chao1 diversity estimates were:
- Bulk soil: mean = 4947 (SD = 717)
- Rhizosphere: mean = 4525 (SD = 542)
- Endorhiza: mean = 3321 (SD = 420)

Notably, while bulk soil and rhizosphere diversity differed significantly between the two soil types tested (MB vs OC), endorhiza diversity was not significantly different between soils (MB: chao1 = 3325, SD = 517 vs OC: chao1 = 3311, SD = 112). This convergence suggests that host plant selection constrains endorhiza diversity to a similar level regardless of the starting soil community richness.

## Beta Diversity Between Sample Types

Beta diversity distances between rhizosphere and bulk soil communities were significantly lower than distances between rhizosphere and endorhiza communities for both unweighted (t = 24.59, p < 0.001) and weighted (t = 211.82, p < 0.001) analyses. Similarly, rhizosphere-to-bulk-soil distances were significantly lower than bulk-soil-to-endorhiza distances (unweighted: t = 25.15, p < 0.001; weighted: t = 211.56, p < 0.001). However, the distances between rhizosphere-endorhiza and bulk-soil-endorhiza were not significantly different from each other, providing limited evidence for a distinct rhizosphere filtering step separate from the overall soil-to-root transition.

## Functional Significance

Endorhiza bacteria support plant growth and suppress disease through multiple mechanisms:
- Production of **phytohormones** (auxins, cytokinins, gibberellins) that modulate plant development
- Secretion of **low molecular weight compounds** and **enzymes** involved in regulating growth and metabolism
- Assistance in tolerating phytotoxic effects of environmental toxicants including heavy metals and organic pollutants
- Suppression of root diseases through competitive exclusion and antibiosis
- Potential contributions to localized terroir effects analogous to those documented in wine grape microbiomes

The terroir concept — that microbial communities contribute to the unique sensory qualities of agricultural products — has been well-established for wine. Both endophytes and epiphytes may play a role in localized flavor for crop plants, and [[cannabis-terpene-and-aroma-chemistry-clarke]] cannabinoid profiles could potentially be influenced by the resident root microbiome.

## Cannabinoid Correlations

Mantel tests revealed significant correlations between cannabinoid profiles and endorhiza community structure (unweighted r-stat: 0.863, p = 0.001). This finding is particularly intriguing because it raises the possibility of a bidirectional relationship: not only might the plant's chemistry shape its microbiome, but the microbiome might also influence cannabinoid biosynthesis. However, because THC composition and concentration were also significantly correlated with soil edaphic variables, disentangling the direct effects of cannabinoid production from soil-mediated effects remains an open challenge. Higher THC plants were found predominantly in one of the two soil types, confounding the cannabinoid-microbiome relationship with the soil-microbiome relationship.

Each plant in the second experiment was tested for a variety of cannabinoids including delta-9-tetrahydrocannabinol (THC). The cannabinoid data was processed at Delta-9-Technologies, LLC. Future studies with controlled cannabinoid profiles grown in identical soils will be needed to isolate the direct effect of plant secondary metabolites on root microbiome assembly.

## Sampling Considerations

Post-harvest sampling introduces significant artifacts. In the Winston et al. study, the first experiment sampled roots 8 weeks after harvest, revealing high Cellvibrio abundances (16.9%, SD = 13.0%) indicative of root decay rather than healthy endophytic colonization. The second experiment sampled from actively growing plants two weeks before harvest, yielding much lower Cellvibrio (0.095%, SD = 2.7%) and more biologically meaningful endorhiza profiles. This comparison underscores the critical importance of sampling timing and plant growth stage in plant microbiome studies. It also highlights the extensive work demonstrating the importance of plant growth stage on the microbiota, as well as the plant-soil feedbacks identified in structuring below-ground microbial communities. The fact that cultivar-specificity could still be detected in post-harvest endorhiza samples, despite the confounding effects of root senescence and decay, suggests that cultivar-specific microbial associations may be remarkably persistent.

## Cultivars Studied

The five Cannabis cultivars examined across two experiments were:
1. **Sour Diesel** — Cannabis sativa, high THC:CBD ratio
2. **Bookoo Kush** — sativa-dominant hybrid, moderately high THC:CBD ratio
3. **Burmese** — balanced sativa/indica hybrid, moderate THC:CBD ratio
4. **Maui Wowie** — Cannabis sativa, high THC:CBD ratio
5. **White Widow** — balanced sativa/indica hybrid, moderate THC:CBD ratio

The first experiment examined Burmese, Bookoo Kush, and Sour Diesel grown in a single sandy loam soil in Vista, California (November 2011). The second experiment examined White Widow and Maui Wowie grown in two distinct soil types at two locations: Vista and Orange County, California (August 2012). The two soil types differed significantly in their physicochemical properties, with the Orange County soil having notably higher total organic carbon (20.0% vs 3.0-5.0%) and water content (0.371 vs 0.101-0.178), creating substantial edaphic variation for testing soil-type effects.

## Methodology

Samples were processed using Illumina 16S rRNA sequencing targeting the V4 region (515F/806R primers), following the Earth Microbiome Project standard pipeline. DNA was extracted from 0.25g of soil or root per extraction using the PowerSoil DNA Isolation Kit with a modified heating step (65°C for 10 minutes prior to vortex). Bioinformatic analysis was performed in QIIME 1.7.0 with both open and closed reference OTU-picking against the Greengenes database pre-clustered at 97% identity. Statistical analyses included ADONIS, ANOSIM, ANOVA, RDA, and Mantel tests for community-level comparisons.

For the first experiment, samples were rarified to 3,000 sequences per sample (4 samples discarded for insufficient coverage). For the second experiment, samples were rarified to 45,000 sequences per sample (1 sample discarded). Phylogenetic trees were built using FastTree, and taxonomy was assigned using the RDP classifier retrained on Greengenes. Relationships between samples were evaluated using redundancy analysis (RDA) and principal coordinate analyses (PCoA) calculated from pairwise sample distances using both weighted and unweighted UniFrac metrics. The study generated a total of 69 samples across both experiments.

## Future Directions

Several important questions remain open for [[cannabis-microbiome-research]]. Understanding which aspects of host genotype produce the observed structuring effects across Cannabis strains is a priority. Increased testing of cannabinoids with careful decoupling from edaphic factors will improve understanding of the importance of cannabinoid production in shaping endorhiza communities. Sampling a time series of endorhiza communities across several plants may help characterize natural variation during the reproductive cycles of Cannabis, which is essential for directing future mechanistic studies.

The practical applications of this research are substantial. Understanding the Cannabis microbiome could lead to microbial inoculants that increase plant fitness, suppress disease, or augment desired metabolite production. Given the growing commercial importance of Cannabis and the trend toward organic cultivation methods, leveraging the plant's native microbial partnerships represents a promising avenue for agricultural optimization.

## See Also

- [[two-tier-selection-model]]
- [[cannabinoid]]
- [[Rhizosphere]]
- [[fungi-in-the-environment-fungal-endophytes-plant-communities]]

The Cannabis endorhiza microbiome represents a frontier in plant-microbiome science with direct implications for one of the world's most commercially significant medicinal crops.
