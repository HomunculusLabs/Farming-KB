# UniFrac Beta-Diversity Analysis in Cannabis Microbiome Studies

## Overview

UniFrac is a phylogenetic distance metric used to compare microbial communities based on the branch lengths of a phylogenetic tree that are unique to each community. In the landmark 2014 study by Winston et al. on the Cannabis microbiome, both unweighted and [[edaphic-factors-microbial-community-structure]]: [[edaphic-determinants-cannabis-microbiome-community-structure]] (relative abundance of lineages).

The UniFrac approach was developed by Lozupone and Knight (2005) and has become the standard metric for comparing microbial communities in [[winston-cannabis-microbiome-study-design]] allowed the researchers to distinguish between effects on [[cannabis-root-microbiome]].

## Weighted vs. Unweighted UniFrac: Complementary Signals

The study demonstrated that the two metrics produce fundamentally different clustering patterns when applied to the same dataset. In the second experiment (White Widow and Maui Wowie across two soil types), unweighted UniFrac showed that soil type dominated PC1 (32.06% variance), confirming that [[dighton-aquatic-hyphomycete-conidia-community-dynamics]] than any single test alone.

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

The dominance of nitrogen as the strongest edaphic correlate is consistent with the known importance of [[core-endorhiza-microbiome-proteobacteria-enrichment-cannabis]] and Acidobacteria depletion in the root endosphere is consistent with observations across many plant species and may reflect the general adaptation of Proteobacteria to the nutrient-rich, low-pH, low-oxygen microenvironment of the root interior.

## Implications for Cannabis Cultivation

The beta-diversity findings suggest several practical principles for cultivators:
1. Soil selection is the single most impactful decision for determining root microbiome composition

## Practical Applications

The principles and techniques discussed here have wide-ranging applications
across multiple disciplines and contexts. Practitioners and researchers
continue to explore new ways to integrate these concepts into modern practice,
adapting traditional knowledge to contemporary challenges and opportunities.

## Key Considerations

Several important factors influence the effectiveness and outcomes described
in this topic. Understanding these considerations helps practitioners make
informed decisions and avoid common pitfalls. Environmental conditions,
timing, and material selection all play critical roles.

## Historical Context

The historical development of this subject reflects centuries of accumulated
knowledge and practical experience. From traditional methods passed down
through generations to modern scientific approaches, the evolution continues
to inform current best practices and research directions.

## Common Challenges

Practitioners frequently encounter several challenges when working with
these concepts. Climate variability, resource limitations, and knowledge
gaps can all affect outcomes. Addressing these challenges requires patience,
observation, and a willingness to adapt approaches based on results.

## See Also
- [[det]]
- [[root-exudates]]
- [[decomposition]]
## Practical Applications
The principles discussed here have direct applications across diverse ecological and agricultural contexts.
Practitioners have demonstrated successful implementation across varied climates and conditions.
Adaptation to local conditions and careful observation remain central to effective application.

## Research Directions
Current research explores intersections between traditional knowledge and modern scientific understanding.
Comparative studies across different bioregions provide valuable insights into generalizable principles.
Long-term monitoring and documentation continue to build the evidence base for these approaches.

## Integration Strategies
Successful implementation draws on multiple complementary approaches working in concert.
Scale-appropriate solutions range from small plots to broadacre systems.
Knowledge sharing between practitioners accelerates collective learning and refinement.

## Implementation Notes
Start with small-scale trials before expanding to larger operations.
Maintain detailed records for iterative refinement of methods and strategies.
## Further Considerations
Ongoing research and field trials continue to expand our understanding of this subject.
Practical experience combined with systematic observation yields the most reliable insights.

## Future Directions
Emerging approaches and technologies offer new opportunities for advancement.
Collaborative knowledge sharing accelerates progress across related domains.
