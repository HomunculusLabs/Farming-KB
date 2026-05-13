---
title: Weighted Vs Unweighted Unifrac Cannabis Strain Microbiome
source: understanding-cultivar-specificity-cannabis-microbiome.md
tags:
  - cannabis
  - microbiome
  - unifrac
  - beta-diversity
  - weighted
  - unweighted
  - strain-specificity
  - cultivar-specificity
  - composition
  - abundance
  - bioinformatics
  - qiime
---

## Overview

The Winston et al. (2014) [[cannabis-root-microbiome]]: it manifests primarily through [[cannabis-rhizosphere-microbial-communities]] based on the branch length of a phylogenetic tree that is unique to one community or the other. The metric comes in two principal variants:

- **Unweighted UniFrac** considers only the presence or absence of taxa. It measures the fraction of phylogenetic tree branch lengths that are unique to one community, treating all present taxa equally regardless of their relative abundance. This makes it sensitive to [[edaphic-determinants-cannabis-microbiome-community-structure]] — how abundant each taxon is.

- **Weighted UniFrac** incorporates taxon abundance by weighting each branch length by the relative abundance of the taxa descended from that branch. This makes it sensitive to both composition and structure, capturing differences in the proportional representation of shared taxa as well as the presence or absence of unique taxa.

The distinction between these metrics has profound implications for interpreting microbiome data. If two communities differ significantly by weighted but not unweighted UniFrac, it means they share most of the same taxa but differ in the relative abundance of those taxa. If they differ by both metrics, the differences include both compositional turnover and abundance shifts.

## Strain Effects: Weighted Sensitive, Unweighted Insensitive

In the first Cannabis microbiome experiment, the difference between metrics was dramatic. Division of [[two-tier-selection-model-plant-microbiome]], where soil determines which species are available (tier one) and plant genotype determines their relative success within the root (tier two).

The biological implication is that cultivar-specificity in the Cannabis microbiome is a matter of degree, not kind. A given bacterial taxon may be present in the endorhiza of all five cultivars tested but could be 100-fold more abundant in one cultivar than another. This abundance-based selection could be driven by genotype-dependent differences in root exudate profiles, immune recognition, root architecture, or any combination of host traits that differentially favour the growth of specific bacterial taxa.

## Soil Type: Strongest Signal in Both Metrics

In contrast to the strain effect, soil type was the dominant factor in both weighted and unweighted analyses, and by a large margin. For the pooled experiments, soil type explained R² = 0.323 for weighted UniFrac and R² = 0.196 for unweighted UniFrac. The number of significant OTUs differing between soil types was 690 (weighted) and 657 (unweighted), compared to 71 (weighted) and 0 (unweighted) for strain differences.

This dominance of soil type in both metrics indicates that soil determines [[leake-mycorrhizal-carbon-sequestration-plant-community-composition]] at the most fundamental level — which bacterial lineages are present in the local species pool. The fact that soil effects are strong in both metrics while strain effects are strong only in the weighted metric creates a clear hierarchy: soil determines presence/absence of taxa, while cultivar modulates their abundance within the root. This two-level hierarchy is exactly the pattern predicted by the two-tier selection model.

## Sample Type Effects: Intermediate Between Soil and Strain

Sample type (bulk soil, rhizosphere, endorhiza) showed an intermediate pattern between soil and strain in terms of metric sensitivity. For the pooled experiments, sample type explained R² = 0.229 for weighted UniFrac and R² = 0.086 for unweighted UniFrac. The number of significant OTUs differing between sample types was 51 (weighted) and 11 (unweighted). This indicates that the transition from bulk soil to rhizosphere to endorhiza involves both compositional filtering (certain taxa are excluded at each transition) and abundance restructuring (the relative proportions of surviving taxa shift).

The fact that some OTUs were significantly different between sample types in the unweighted analysis confirms that genuine compositional turnover occurs during root colonization — some soil taxa fail to colonize the rhizosphere, and some rhizosphere taxa fail to colonize the endorhiza interior. However, the much larger number of abundance-based differences (51 vs. 11) indicates that the primary effect of moving from soil to root interior is not wholesale exclusion but rather selective enrichment and suppression of taxa that are capable of colonizing both niches.

## Practical Implications for Microbiome Study Design

### Metric Selection

The Cannabis microbiome results demonstrate that the choice between weighted and unweighted UniFrac can determine whether biologically meaningful strain effects are detected. For studies focused on cultivar-specificity, genotype effects, or any hypothesis about differential selection from a shared species pool, weighted UniFrac or complementary abundance-based analyses (ANOVAs, LEfSe, DESeq2) should be used as primary metrics. Unweighted UniFrac alone will miss abundance-based effects and may lead to false negative conclusions about genotype-microbiome associations.

### Statistical Power Considerations

The asymmetry between metrics also has implications for statistical power and study design. Because abundance-based effects can be detected with smaller sample sizes than compositional effects (given the larger effect sizes typically observed), studies powered for unweighted UniFrac analysis may be overpowered for weighted analysis, while studies powered for weighted analysis may be underpowered for detecting compositional differences. The optimal approach is to include both metrics in the analysis plan and power the study for the metric most relevant to the primary hypothesis.

### Complementary Analyses

The Cannabis study used both permutational multivariate analysis of variance (ADONIS) and individual OTU-level tests (ANOVA for weighted, G-test for unweighted) to characterize community differences. This dual approach is recommended: multivariate tests provide an overall assessment of community-level differences, while OTU-level tests identify which specific taxa drive those differences. In the Cannabis data, the combination revealed that strain effects were driven by differential abundance of Proteobacterial taxa (particularly within Pseudomonadales, Burkholderiales, Sphingomonadales, and Rhizobiales orders) rather than by unique presence of specific taxa.

## Limitations of the UniFrac Approach

Both weighted and unweighted UniFrac have known limitations that should be considered when interpreting results. UniFrac is sensitive to tree construction methods and reference database choice, and the metric assumes that phylogenetic distance is a meaningful proxy for ecological distance — an assumption that may not hold for horizontally transferred genes or functionally convergent taxa. Additionally, UniFrac distances are compositional and sensitive to library size differences, making rarefaction an important preprocessing step.

### Compositional Data Challenges

Microbiome data generated by 16S rRNA amplicon sequencing is inherently compositional — the counts represent relative proportions within each sample rather than absolute abundances. This compositional nature can create spurious correlations and inflate apparent differences between samples, particularly for low-abundance taxa. While rarefaction (subsampling to equal depth) addresses some of these issues, it also discards valid data from deeper-sequenced samples. Alternative approaches such as centered log-ratio transformation or DESeq2's median-of-ratios normalization can complement rarefaction-based analyses.

The Cannabis study used rarefaction to 3,000 sequences (first experiment) and 45,000 sequences (second experiment) before computing UniFrac distances. The substantial difference in rarefaction depth between experiments reflects the different sequencing yields but also means that the two experiments had different effective resolutions of rare taxa, potentially affecting the comparability of unweighted UniFrac results (which are more sensitive to rare taxa than weighted results).

### Phylogenetic Resolution of the V4 Region

The V4 region of the 16S rRNA gene used in the Cannabis study provides limited phylogenetic resolution, particularly at the species and strain level. The 291 bp amplicon can reliably resolve genera and often species but cannot distinguish between closely related strains of the same species. Deeper taxonomic resolution through full-length 16S sequencing (PacBio, Nanopore) or whole-genome shotgun metagenomics might reveal compositional differences between cultivars that were undetectable with the V4 amplicon approach, potentially narrowing the gap between weighted and unweighted metric sensitivity.

If cultivar-specificity operates primarily at the strain level — for example, if different Cannabis cultivars select for different strains of *Pseudomonas* rather than different species — the V4 amplicon approach would classify these as the same OTU, making the difference detectable only through abundance shifts (weighted metric) rather than presence/absence (unweighted metric). This is a fundamental limitation of amplicon-based approaches that researchers should consider when designing studies of genotype-microbiome interactions.

## Broader Context: Metric Choice in Plant Microbiome Literature

## Overview

Weighted Vs Unweighted Unifrac Cannabis Strain Microbiome represents an important element within sustainable
design and ecological management systems. Its proper understanding
and integration contributes to the resilience and productivity of
designed ecosystems and agricultural systems.

## Key Characteristics

Several defining characteristics distinguish weighted vs unweighted unifrac cannabis strain microbiome
from related concepts in permaculture and ecological design.
Understanding these traits supports effective implementation
and management across diverse environmental conditions.

## Ecological Context

The ecological relationships involving weighted extend
across multiple trophic levels and functional groups.
Soil biology, water cycles, and energy flows all interact
with this element in complex and beneficial ways.

## Practical Applications

Weighted Vs Unweighted Unifrac Cannabis Strain Microbiome finds practical application in multiple design contexts.
Permaculture principles guide integration strategies that maximize
beneficial interactions while minimizing external inputs.
Site-specific adaptation ensures relevance to local conditions.

## Management and Implementation

Effective management requires attention to seasonal patterns
and environmental feedback loops. Monitoring outcomes supports
adaptive management strategies that improve results over time.
Integration with complementary elements enhances system function.

## Regional Considerations

Different geographic regions present unique challenges and
opportunities for weighted vs unweighted unifrac cannabis strain microbiome. Climate adaptation
strategies vary across cultivation zones and latitude ranges.
Local knowledge and site observation remain essential guides.

## Sustainability

Sustainable management practices ensure long-term viability.
Biodiversity considerations guide implementation decisions.
Responsible stewardship maintains ecological health over time.
Economic sustainability balances environmental and social needs.

## Research and Development

Ongoing research continues to expand understanding of
weighted vs unweighted unifrac cannabis strain microbiome and its applications. Active investigation
areas include ecological interactions and optimization.
Published findings contribute to an evolving evidence base.

## Historical Context

Weighted Vs Unweighted Unifrac Cannabis Strain Microbiome has been recognized across multiple knowledge traditions.
Indigenous and traditional practices have informed modern approaches.
The synthesis of historical and contemporary knowledge enriches
current understanding and implementation strategies.

## Integration Strategies

Successful integration of weighted vs unweighted unifrac cannabis strain microbiome into broader
systems requires careful planning and observation.
Design for multiple functions increases overall efficiency.
Monitoring integration outcomes supports adaptive management.

## Challenges and Solutions
