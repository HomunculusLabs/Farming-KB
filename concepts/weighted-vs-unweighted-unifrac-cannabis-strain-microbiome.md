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

The Winston et al. (2014) [[cultivar-cannabis-microbiome-two-tier-selection-model]] study revealed a striking asymmetry between weighted and unweighted UniFrac distance metrics in their sensitivity to cultivar-specific microbiome effects. While both metrics detected significant clustering by sample type and soil type, only weighted UniFrac consistently identified significant strain-level effects. This pattern provides important insight into the nature of cultivar-specificity in the [[cannabis-root-microbiome]]: it manifests primarily through [[otu-differential-abundance-cannabis-microbiome]] of shared taxa rather than through the presence or absence of strain-unique taxa. Understanding this distinction is critical for experimental design, statistical analysis, and biological interpretation of plant microbiome studies.

## UniFrac Metrics: Composition vs. Abundance

UniFrac (Unique Fraction) is a phylogenetic distance metric that measures the dissimilarity between [[cannabis-rhizosphere-microbial-communities]] based on the branch length of a phylogenetic tree that is unique to one community or the other. The metric comes in two principal variants:

- **Unweighted UniFrac** considers only the presence or absence of taxa. It measures the fraction of phylogenetic tree branch lengths that are unique to one community, treating all present taxa equally regardless of their relative abundance. This makes it sensitive to [[core-endorhiza-bacterial-community-composition-cannabis]] — which taxa are present — but insensitive to [[edaphic-determinants-cannabis-microbiome-community-structure]] — how abundant each taxon is.

- **Weighted UniFrac** incorporates taxon abundance by weighting each branch length by the relative abundance of the taxa descended from that branch. This makes it sensitive to both composition and structure, capturing differences in the proportional representation of shared taxa as well as the presence or absence of unique taxa.

The distinction between these metrics has profound implications for interpreting microbiome data. If two communities differ significantly by weighted but not unweighted UniFrac, it means they share most of the same taxa but differ in the relative abundance of those taxa. If they differ by both metrics, the differences include both compositional turnover and abundance shifts.

## Strain Effects: Weighted Sensitive, Unweighted Insensitive

In the first Cannabis microbiome experiment, the difference between metrics was dramatic. Division of [[cannabis-rhizosphere-endorhiza-communities]] by strain was significant for both weighted (ADONIS: R² = 0.59, p = 0.004) and unweighted (ADONIS: R² = 0.39, p = 0.003) analyses, suggesting detectable compositional differences between strains. However, across all sample types combined, strain-level differences were not significant for either weighted (ADONIS: R² = 0.11, p = 0.25) or unweighted (ADONIS: R² = 0.11, p = 0.15) analyses, indicating that strain effects were confined to the endorhiza niche.

In the second experiment, the pattern became clearer. Division of all communities by strain was significant for weighted UniFrac (ADONIS: R² = 0.27, p = 0.001) but not for unweighted UniFrac in the individual sample type analysis. Critically, there were zero significantly segregating OTUs based on unweighted analysis between cultivars in endorhiza and rhizosphere samples, while there were 71 significantly different OTUs when abundance was accounted for through weighted analysis.

When both experiments were pooled, the asymmetry was fully apparent. Using weighted UniFrac, strain was a highly significant factor (ADONIS: R² = 0.301, p = 0.001). Using unweighted UniFrac, strain remained significant (ADONIS: R² = 0.178, p = 0.001), but the effect size was substantially smaller, and the individual OTU analysis confirmed that no single taxon was uniquely present or absent between strains — all differences were in abundance.

## Interpretation: Abundance-Based Selection, Not Compositional Turnover

The consistent pattern — weighted metrics more sensitive to strain effects, zero strain-unique OTUs in unweighted analysis — indicates that Cannabis cultivars do not harbour fundamentally different bacterial species in their endorhiza communities. Instead, all cultivars draw from the same soil-derived species pool and select from it by modulating the relative abundance of specific taxa. This is consistent with the two-tier [[two-tier-selection-model-plant-microbiome]], where soil determines which species are available (tier one) and plant genotype determines their relative success within the root (tier two).

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
