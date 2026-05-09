# UniFrac Beta-Diversity Analysis in Cannabis Microbiome Studies

## Overview

UniFrac is a phylogenetic distance metric used to compare microbial communities based on the branch lengths of a phylogenetic tree that are unique to each community. In the landmark 2014 study by Winston et al. on the Cannabis microbiome, both unweighted and weighted UniFrac analyses were applied to 16S rRNA gene sequence data from endorhiza, rhizosphere, and bulk soil samples across five Cannabis cultivars. The dual application of these metrics revealed complementary aspects of microbial community structure: unweighted UniFrac captured differences in taxonomic composition (presence/absence of lineages), while weighted UniFrac captured differences in community structure (relative abundance of lineages).

The UniFrac approach was developed by Lozupone and Knight (2005) and has become the standard metric for comparing microbial communities in ecological studies. Unlike simple taxonomic distance measures (such as Bray-Curtis dissimilarity), UniFrac incorporates the evolutionary relationships between organisms, providing a more biologically meaningful measure of community similarity. Two variants exist: unweighted UniFrac considers only the presence or absence of lineages, while weighted UniFrac additionally accounts for the relative abundance of each lineage. The use of both variants in the Cannabis microbiome study allowed the researchers to distinguish between effects on community composition versus community structure — a distinction that proved critical for understanding how soil and cultivar interact to shape the Cannabis root microbiome.

## Weighted vs. Unweighted UniFrac: Complementary Signals

The study demonstrated that the two metrics produce fundamentally different clustering patterns when applied to the same dataset. In the second experiment (White Widow and Maui Wowie across two soil types), unweighted UniFrac showed that soil type dominated PC1 (32.06% variance), confirming that edaphic factors are the primary determinant of which microbial lineages are present. Weighted UniFrac, however, showed that Cannabis strain dominated PC1 (34.51% variance), revealing that host genotype primarily controls the relative abundance of those lineages within the plant.

This divergence between weighted and unweighted results is biologically significant. It supports the two-tier selection model where soil type acts as the first filter (determining community composition), while cultivar acts as the second filter (determining community structure through abundance modulation). The 690 weighted OTUs differing between soil types versus zero unweighted OTUs differing between strains in the endorhiza underscores this finding: cultivars don't change which bacteria are present, but they do change how abundant those bacteria become.

The practical implication is that a grower cannot overcome soil-driven microbiome limitations simply by choosing a particular cultivar. The soil provides the pool of available microbes, and the plant's genotype only selects from that pool. Changing soil type (or amending the soil) has a far greater impact on which microbial lineages are available for root colonization than switching from one strain to another.

## Statistical Framework: ADONIS, ANOSIM, and RDA

The study employed multiple complementary statistical tests to assess community differentiation. Each test has different assumptions and sensitivities, and their combined use provides a more robust picture of community dynamics than any single test alone.

- **ADONIS (PERMANOVA)**: Partitioned variance in community distance matrices by factors including soil type, sample type, and strain. Endorhiza communities showed the strongest differentiation (ADONIS R² = 0.26 unweighted, 0.59 weighted in experiment 1; R² = 0.26 unweighted, 0.215 weighted in pooled analysis). The high R² values for endorhiza in weighted analyses indicate that cultivar identity explains a large proportion of the variance in community structure within the root.

- **ANOSIM**: Provided rank-based non-parametric testing, which yielded mixed results for rhizosphere and bulk soil samples. In experiment 2, bulk soil showed non-significant ANOSIM (R = 0.012, p = 0.459) but significant ADONIS (R² = 0.06, p = 0.054), suggesting that the PERMANOVA results may be partially driven by dispersion differences between groups rather than purely by centroid differences. ANOSIM is known to be sensitive to differences in within-group dispersion, which can produce false negatives when groups have unequal variances.

- **RDA (Redundancy Analysis)**: Ordinated communities constrained by edaphic variables, confirming significant soil-microbiome associations even when ANOSIM was non-significant. In experiment 2 bulk soil, RDA showed F = 2.41, p = 0.045, confirming real effects despite the ANOSIM failure to detect them. RDA is a constrained ordination technique that directly models the relationship between community composition and environmental variables, making it particularly useful for identifying which specific edaphic factors drive community differences.

When ANOSIM and ADONIS disagree (as they did for rhizosphere samples in several analyses), the ADONIS result is generally preferred because PERMANOVA has greater statistical power and can detect effects even when within-group dispersions differ. The RDA results serve as an independent line of evidence. Researchers analyzing microbiome data should be aware that relying on a single test can produce misleading conclusions, and that the combination of ADONIS with RDA provides the most robust assessment of community-level effects.

## PCoA Ordination and Variance Partitioning

Principal Coordinates Analysis (PCoA) based on UniFrac distances was the primary visualization tool used in the study. The PCoA plots revealed distinct clustering patterns that varied depending on the UniFrac variant used:

**Unweighted UniFrac (composition-based):**
- Experiment 1: PC1 = 26.46% variance, PC2 = 7.36% variance. Sample type was the dominant structuring factor along PC1.
- Experiment 2: PC1 = 32.06% variance (soil type), PC2 = 11.34% variance (sample type), PC3 = 5.67% variance.
- Pooled: PC1 = 13.27% (soil type), PC2 = 10.15% (sample type), PC3 = 6.15% (strain).

**Weighted UniFrac (abundance-based):**
- Experiment 1: PC1 = 62.98% variance, PC2 = 15.43% variance. The much higher variance captured by PC1 in weighted analysis reflects the strong abundance-driven signal in endorhiza communities.
- Experiment 2: PC1 = 34.51% (strain), PC2 = 25.41% (sample type), PC3 = 19.31% (soil type).
- Pooled: PC1 = 37.69% (soil type), PC2 = 13.95% (sample type), PC3 = 11.07% (strain).

The striking difference between experiment 1 weighted PC1 (62.98%) and experiment 2 weighted PC1 (34.51%) reflects the confounding effect of post-harvest root decay in experiment 1. The decay-related Cellvibrio signal dominated the community structure in experiment 1, inflating the apparent sample-type effect. When experiments were pooled, this signal was diluted and the soil-type effect reasserted itself as the primary structuring factor.

## Pairwise Beta-Distance Comparisons

A key finding from the beta-diversity analysis was the hierarchical similarity structure among sample types. Rhizosphere and bulk soil communities were significantly more similar to each other than either was to endorhiza communities. This hierarchical structure was tested with pairwise t-tests on the beta-diversity distances:

- Rhizosphere-bulk soil distances were significantly lower than rhizosphere-endorhiza distances (unweighted: t = 24.59, p < 0.001; weighted: t = 211.82, p < 0.001)
- Rhizosphere-bulk soil distances were significantly lower than bulk soil-endorhiza distances (unweighted: t = 25.15, p < 0.001; weighted: t = 211.56, p < 0.001)
- Rhizosphere-endorhiza distances were NOT significantly different from bulk soil-endorhiza distances (unweighted: t = -2.10, p = 0.109; weighted: t = -2.23, p = 0.078)

The enormous t-statistics for the significant comparisons (211.82 for weighted) indicate extremely strong effects with essentially no overlap between the distance distributions. The non-significant finding for the third comparison is particularly notable because it fails to support the first step of the two-tier selection model, which predicts a gradual community shift from bulk soil through rhizosphere to endorhiza. The absence of a significant rhizosphere intermediary effect suggests that in Cannabis, the rhizosphere may not serve as a distinct filtering step, or that the filtering is too subtle to detect with the sample sizes used (18 rhizosphere samples in experiment 2).

This finding contrasts with studies in other plant systems (such as Arabidopsis and Populus) where the rhizosphere community is clearly intermediate between bulk soil and endorhiza. The Cannabis-specific result may reflect the unique chemistry of Cannabis root exudates, which include cannabinoids and terpenes that could directly recruit endophytes from soil without an intermediate rhizosphere enrichment step.

## Edaphic Factors and Community Structuring

Mantel tests correlating UniFrac distances with edaphic variables showed that all tested factors were significantly correlated with community beta-diversity (p = 0.001 for all). The ranking by importance was consistent across weighted and unweighted analyses:

1. **Nitrogen**: Strongest effect (weighted r = 0.465, unweighted r = 0.630)
2. **Salinity**: Second strongest (weighted r = 0.437, unweighted r = 0.620)
3. **Total Organic Carbon**: Third (weighted r = 0.330, unweighted r = 0.512)
4. **Water content**: Fourth (weighted r = 0.281, unweighted r = 0.466)
5. **pH**: Weakest but still significant (weighted r = 0.221, unweighted r = 0.292)

The BEST (Bioenv) analysis, which identifies the optimal subset of environmental variables for explaining community variation, determined that three edaphic factors together — Nitrogen, Carbon, and Water — optimally explained community beta-diversity (rho = 0.632). Adding salinity and pH did not improve the correlation, suggesting that these three factors capture the primary edaphic signal.

The dominance of nitrogen as the strongest edaphic correlate is consistent with the known importance of nitrogen availability in structuring soil microbial communities. Nitrogen availability affects microbial growth rates directly and indirectly influences community composition through competitive dynamics. For Cannabis cultivation, this means that nitrogen management in growing media has the largest potential to influence the root microbiome, followed by salinity management (which connects to fertilizer EC management and the risk of salt stress on beneficial microbes).

## Pooled Experiment Analysis: Increased Statistical Power

When experiments 1 and 2 were pooled and rarified to the shallower sequencing depth of experiment 1, all three factors (soil type, sample type, strain) became highly significant for both weighted and unweighted UniFrac (all p = 0.001). The pooling increased sample size from 27 or 42 to 69 samples and broadened the range of cultivars and soil types represented.

The pooled analysis revealed cultivar effects on rhizosphere communities that were not detectable in experiment 1 alone. In experiment 1, rhizosphere communities did not cluster significantly by strain (ADONIS: R² = 0.07, p = 0.07 unweighted; R² = 0.09, p = 0.10 weighted). In the pooled analysis, strain became significant for rhizosphere (ADONIS: R² = 0.034, p = 0.004 weighted). This demonstrates that the genotype effect on the rhizosphere is real but requires adequate statistical power to detect.

However, the pooling also revealed a confound: Cellvibrio abundance in experiment 1 was dramatically higher (16.9% mean) than in experiment 2 (0.095% mean), likely due to root decay occurring in the 8-week post-harvest samples of experiment 1 versus the actively growing plants in experiment 2. Despite this confound, cultivar-specificity was still detectable in the endorhiza of experiment 1, suggesting that the host genotype signal persists even during early stages of root decomposition.

## OTU-Level Analysis: Presence vs. Abundance

A critical insight from the UniFrac analysis was reinforced by the individual OTU-level statistical testing. Both unweighted (g-test) and weighted (ANOVA) analyses of individual OTUs showed that soil type had the strongest influence over significant OTU differences, with 690 weighted and 657 unweighted significant OTUs. Sample type produced 51 weighted and 11 unweighted significant OTUs. Strain produced 71 weighted but zero unweighted significant OTUs.

This pattern — where strain differences appear only in weighted analysis — confirms that Cannabis cultivars shape their microbiome through abundance modulation rather than through selective exclusion of specific taxa. All bacterial lineages found in any cultivar's endorhiza were also potentially present in other cultivars; what differed was how dominant each lineage became. This has important implications for microbiome engineering: rather than trying to introduce novel taxa, cultivation practices should focus on creating conditions that favor the proliferation of already-present beneficial organisms.

The 51 OTUs that significantly differed between sample types (endorhiza, rhizosphere, bulk soil) were predominantly characterized by a decrease in Acidobacteria (particularly the order iii1-15) and an increase in Proteobacteria within the endorhiza. The Bonferroni-corrected ANOVA for the Acidobacteria decrease yielded p = 1.12e-7, one of the strongest statistical signals in the entire study. This pattern of Proteobacteria enrichment and Acidobacteria depletion in the root endosphere is consistent with observations across many plant species and may reflect the general adaptation of Proteobacteria to the nutrient-rich, low-pH, low-oxygen microenvironment of the root interior.

## Implications for Cannabis Cultivation

The beta-diversity findings suggest several practical principles for cultivators:
1. Soil selection is the single most impactful decision for determining root microbiome composition
2. Cultivar selection primarily affects the abundance balance of endophytic bacteria, not their presence
3. The conserved Proteobacteria-enriched endorhiza core community suggests functional redundancy and resilience
4. Manipulating soil nitrogen content offers the most direct lever for shaping the root microbiome
5. The rhizosphere may not serve as a strong intermediary filter in Cannabis as it does in other crops
6. Super-soil or living soil approaches that maintain diverse bacterial communities are likely more effective than inoculant-only strategies, since the plant selects from the available soil pool rather than requiring specific introduced strains
7. Monitoring soil nitrogen, carbon, and water content provides a practical framework for maintaining favorable root microbiome conditions without expensive sequencing-based diagnostics

## Limitations and Future Directions

The UniFrac-based approach in this study has several limitations that should be acknowledged. First, the study used 16S rRNA gene amplicon sequencing of the V4 region, which provides genus-level but rarely species-level taxonomic resolution. Many functionally important differences between microbial strains are invisible to this approach. Second, the study characterized only the bacterial community; the fungal and archaeal components of the Cannabis microbiome remain uncharacterized and may play equally important roles in plant health.

Third, the two experiments differed in their sampling timing (post-harvest versus pre-harvest), which introduced the Cellvibrio confound. Future studies should sample across multiple time points during the growing cycle to distinguish between growth-stage effects and cultivar effects. Fourth, the study examined only five cultivars; the full diversity of Cannabis chemotypes and their associated microbiomes remains to be explored. Finally, the correlative nature of the beta-diversity analysis cannot establish causation — experiments that manipulate specific microbial taxa and measure plant fitness outcomes are needed to move from description to application.

## See Also

- [[cannabis-microbiome-two-tier-selection]] — The two-tier selection model framework
- [[edaphic-determinants-cannabis-microbiome-community-structure]] — Edaphic factor analysis
- [[core-endorhiza-bacterial-community-composition-cannabis]] — Core endorhiza community
- [[proteobacteria-dominance-cannabis-endorhiza-community]] — Proteobacteria enrichment patterns
- [[cellvibrio-root-decay-indicator-cannabis-endorhiza]] — Post-harvest root decay signal

## Source

Winston ME, Hampton-Marcell J, Zarraonaindia I, et al. (2014) Understanding Cultivar-Specificity and Soil Determinants of the Cannabis Microbiome. PLoS ONE 9(6): e99641.
