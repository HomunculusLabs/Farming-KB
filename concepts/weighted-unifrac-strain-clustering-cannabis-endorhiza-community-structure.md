---
title: Weighted Unifrac Strain Clustering Cannabis Endorhiza Community Structure
wiki: "LLM Wiki"
category: "[[fukuoka-microbial-ecology-decomposition]]"
tags:
  - cannabis
  - microbiome
  - unifrac
  - endorhiza
  - community-structure
  - beta-diversity
  - cultivar-specificity
related:
  - "[[cannabis-microbiome-agricultural-implications-and-future-directions]]"
  - "weighted unifrac"
  - "unweighted unifrac"
  - "[[alpha-beta-diversity-cannabis-root-microbiomes]]"
  - "pcoa"
  - "adonis"
  - "anosim"
  - "otu analysis"
  - "fdr correction"
  - "endorhiza"
  - "soil microbiome"
created: "2026-05-10"
---

# Weighted vs Unweighted UniFrac in Cannabis Endorhiza Community Structure

**Weighted vs unweighted UniFrac analysis** of the [[cannabis-endorhiza-microbiome]] reveals a critical distinction in how cultivar selection and [[mycorrhizal-fungi-soil-carbon-sequestration-by-type]] shape [[cannabis-rhizosphere-microbial-communities]]. This insight, drawn from Winston et al. (2014), demonstrates that cannabis cultivars influence the *relative abundance* of microbial taxa rather than determining which taxa are present—a nuance that is frequently overlooked in studies relying on a single beta-diversity metric.

## Background

[[unifrac-weighted-unweighted-analysis-cannabis-microbiome]] is a beta diversity measure that quantifies differences between [[cultivar-specific-root-microbial-communities]] based on phylogenetic distances of observed organisms on a reference tree. Two principal variants exist:

- **[[weighted-vs-unweighted-unifrac-cannabis-strain-microbiome]]** considers only the *presence or absence* of taxa on a phylogenetic tree. It measures differences in community *composition*—which lineages are found in a given sample, regardless of how abundant each lineage is.
- **weighted unifrac strain clustering cannabis endorhiza community structure** incorporates taxon *abundances* into the distance calculation, measuring differences in community *structure*—not only which lineages are present, but how abundant each one is relative to others.

The distinction is biologically meaningful. When two communities share the same set of taxa but differ in the dominance relationships among them, unweighted UniFrac will report them as highly similar, while weighted UniFrac will capture the divergence. Conversely, when communities contain entirely different taxa, both metrics will register large distances.

## Key Findings from Winston et al. (2014)

### OTU-Level Significance Testing

Winston et al. (2014) applied both weighted and unweighted UniFrac distance matrices to the endorhiza (root interior) microbiome of multiple cannabis cultivars grown across different soil types. The results were starkly asymmetric:

| Factor | Weighted UniFrac Significant OTUs | Unweighted UniFrac Significant OTUs |
|--------|----------------------------------|-------------------------------------|
| Strain (cultivar) | 71 | 0 |
| Soil type | 690 | 657 |

For **strain** (cultivar), unweighted UniFrac detected *zero* significant OTUs, while weighted UniFrac identified 71. This pattern indicates that cannabis cultivars do not act as filters that permit or exclude particular microbial taxa from colonizing the root interior. Instead, cultivar identity reshapes the *relative abundances* of a shared pool of endorhiza colonizers.

For **soil type**, both metrics returned large numbers of significant OTUs (690 weighted; 657 unweighted), confirming that soil is the primary determinant of *which taxa can enter* the root endosphere at all. The near-parity between weighted and unweighted counts for soil indicates that soil differences affect both composition and abundance simultaneously.

### Principal Coordinates Analysis (PCoA)

The second experiment in the study reinforced these findings through [[PCoA]] ordination of the two distance matrices:

- **Unweighted UniFrac**: PC1 explained 32.06% of variance and was dominated by **soil type** as the primary clustering factor.
- **Weighted UniFrac**: PC1 explained 34.51% of variance and was dominated by **strain** (cultivar) as the primary clustering factor.

This cross-validation is powerful. When the analysis is tuned to presence/absence (unweighted), soil type is the dominant structuring force. When the analysis is tuned to abundance (weighted), cultivar identity emerges as the dominant signal. The two metrics are not contradictory—they capture different biological axes of community variation operating simultaneously.

## Interpretation

### Cultivar Acts on Abundance, Not Composition

The fundamental conclusion is that cannabis cultivar selection operates on the *relative abundances* of endorhiza microbes, not on compositional filtering. All cultivars sampled shared essentially the same species pool within a given soil environment. What differed was the degree to which particular taxa were favored or suppressed by each cultivar's root exudate profile, immune responses, or other host-mediated factors.

This has practical implications for [[cannabis-core-endorhiza-microbiome]]. If cultivars filtered taxa at the species level, breeding for a desirable microbiome would require introducing novel taxa to the system. Because the effect is on abundances, [[weed-management-strategies]] such as inoculation, soil amendments, and crop rotation can shift the existing community toward favorable configurations without needing to introduce entirely new species.

### Soil as the Compositional Gatekeeper

Soil type determined *composition*—the identity of taxa available for root colonization. This aligns with decades of research showing that [[cannabis-rhizosphere-bulk-soil-microbial-comparison]] communities serve as the primary source pool for rhizosphere and endorhiza inhabitants. In this study, soil was the dominant factor in [[unifrac-weighted-unweighted-analysis-cannabis-microbiome]], confirming its role as the compositional gatekeeper that establishes the boundaries within which host effects operate.

## Statistical Methods

Winston et al. employed a suite of complementary statistical approaches to ensure robustness:

- **[[ADONIS]]** (PERMANOVA): Partitioned variance in UniFrac distance matrices by factor (strain, soil). Confirmed that both strain and soil significantly explain community variation when tested independently.
- **[[ANOSIM]]**: Non-parametric test of group differences based on rank dissimilarities. Provided an independent confirmation of ADONIS results without distributional assumptions.
- **[[ANOVA]] with [[fdr-correction]]**: Applied at the individual [[OTU]] level to identify which specific taxa differed significantly between treatment groups. The [[false-discovery-rate]] correction controlled for multiple comparisons across hundreds of OTUs, reducing the risk of false positives inherent in high-dimensional microbiome data.

The combination of multivariate community-level tests (ADONIS, ANOSIM) with univariate OTU-level tests (ANOVA + FDR) provides a robust statistical framework that has become standard in microbiome ecology.

## Broader Significance

This study highlights a common pitfall in plant [[cannabis-microbiome-research]]: relying on a single beta-diversity metric can obscure meaningful biological patterns. Many published studies report only unweighted UniFrac (or only Bray-Curtis), potentially missing abundance-driven effects of host genotype that weighted UniFrac would reveal.
