---
title: UniFrac
source: understanding-cultivar-specificity-cannabis-microbiome.md
type: entity
---

## Description

**UniFrac** is a phylogenetic distance metric used to compare microbial communities based on the evolutionary divergence of their constituent organisms. Developed by Catherine Lozupone and Rob Knight, it measures the fraction of branch length in a phylogenetic tree that is unique to one community or shared between two communities. UniFrac was used extensively in the [[winston-cannabis-microbiome-study-design]] to assess beta diversity between sample types. It is one of the core beta-diversity metrics calculated by the [[qiime]] pipeline alongside alpha-diversity measures like the [[chao1-index]].

## Classification

- **Category:** Phylogenetic beta-diversity metric
- **Type:** Distance measure for microbial community comparison
- **Variants:** [[weighted-unweighted-unifrac-discrepancy-cannabis-cultivar]] (presence/absence), Weighted UniFrac (abundance-aware)
- **Named after:** Unique Fraction metric
- **Published:** 2005, Applied and Environmental Microbiology

## Key Facts

- Unweighted UniFrac considers only the presence or absence of lineages, capturing differences in community membership (which taxa are present).
- Weighted UniFrac incorporates taxon abundances, capturing differences in community structure (how abundant each taxon is).
- In the Cannabis microbiome study, both weighted and unweighted UniFrac analyses were performed to characterize community differences.
- Key finding: Cannabis strain was the main determinant of PC1 (34.51%) for the weighted analysis of all samples in the second experiment, suggesting that convergent host genotype-dependent selection acts through controlling community structure (abundance) more than composition.
- There were no significant segregating OTUs based on unweighted analysis between cultivars in endorhiza and rhizosphere samples, but 71 segregating OTUs when abundance was accounted for (weighted).
- The 71 cultivar-differentiating OTUs (weighted) contrasts sharply with the 657 OTUs that significantly differ between soil types, showing soil is the dominant factor.

## Mathematical Foundation

### Core Concept
UniFrac measures the phylogenetic distance between two microbial communities as the fraction of the total branch length in a phylogenetic tree that is unique to one community (not shared). The calculation depends on a phylogenetic tree constructed from aligned sequences (typically 16S rRNA gene sequences).

### Unweighted UniFrac Formula
**UniFrac_U = (unique branch length) / (total branch length)**

For two communities A and B:
1. Construct a phylogenetic tree containing all sequences from both communities
2. For each branch, determine if its descendant sequences come from community A only, community B only, or both
3. Sum the branch lengths unique to each community (not shared)
4. Divide by the total branch length of the tree
5. Result ranges from 0 (identical communities) to 1 (completely disjoint communities)

### Weighted UniFrac Formula
**UniFrac_W = Σᵢ (bᵢ × |Aᵢ - Bᵢ|) / Σᵢ (bᵢ × max(Aᵢ, Bᵢ))**

Where bᵢ is the branch length for branch i, and Aᵢ and Bᵢ are the total abundances of descendants of branch i in communities A and B respectively. This formulation accounts for both phylogenetic distance and relative abundance, making it sensitive to changes in the proportions of lineages.

## Unweighted vs. Weighted UniFrac

### When to Use Unweighted UniFrac
- To detect differences in **which taxa are present** (community membership)
- When rare taxa are of particular interest
- For detecting presence/absence patterns driven by environmental filtering
- Best for comparing communities with very different compositions

### When to Use Weighted UniFrac
- To detect differences in **how abundant taxa are** (community structure)
- When changes in dominant taxa are more relevant than presence/absence of rare taxa
- For detecting abundance shifts driven by host selection or environmental conditions
- More robust to uneven sampling depth in some cases

### Interpreting Discrepancies
When unweighted and weighted UniFrac tell different stories, the discrepancy itself is informative:
- **Significant unweighted, non-significant weighted:** Communities differ in membership but the abundant taxa are similar. Rare taxa drive the difference.
- **Non-significant unweighted, significant weighted:** Communities share the same taxa but differ in their relative proportions. Abundance shifts are the key signal.
- **Both significant:** Communities differ in both membership and structure — the strongest differentiation.

In the Cannabis study, the discrepancy was key to understanding that cultivar genotype shapes community **abundance** more than **membership**. See weighted vs unweighted unifrac [[otu-abundance-vs-presence-absence-cannabis-strain-microbiome]] for detailed interpretation of this finding.

## Application in Cannabis Microbiome Research

### Experimental Design
The Cannabis microbiome study analyzed bacterial communities using [[16s-rrna-sequencing-microbiome-analysis]] processed through [[qiime]]. UniFrac distances were calculated for all pairwise sample comparisons and visualized through Principal Coordinate Analysis (PCoA).

### Key UniFrac Findings

#### Soil Type Dominance
Both weighted and unweighted UniFrac confirmed that soil type is the dominant factor structuring Cannabis microbial communities. The 657 OTUs significantly different between soil types dwarf the 71 OTUs differing between cultivars, demonstrating that the soil environment overwhelms host genotype effects on community composition.

#### Cultivar Genotype Effects
The weighted UniFrac analysis revealed that Cannabis strain was the main determinant of PC1 (34.51% of variation), indicating that host genotype-dependent selection primarily operates through controlling community **structure** (abundance) rather than **composition** (presence/absence). See weighted [[weighted-unifrac-strain-clustering-cannabis-endorhiza-community-structure]] [[proteobacteria-dominance-cannabis-endorhiza-community]] structure for the strain-level analysis.

#### Niche Filtering
UniFrac analysis revealed progressive niche-filtering of microbes:
1. **Bulk soil to rhizosphere:** Moderate filtering — some soil taxa are excluded from the root zone
2. **Rhizosphere to endorhiza:** Strong filtering — only a subset of rhizosphere taxa colonize the root interior

This supports the two-step selection model for endophyte colonization from the soil reservoir.

## Integration with Other Analyses

UniFrac results are typically integrated with:
- **Alpha diversity ([[chao1-index]]):** To contextualize between-community differences with within-community richness
- **Taxonomic bar plots:** To identify which specific taxa drive UniFrac distance patterns
- **Environmental metadata:** To correlate community distances with soil properties (pH, nitrogen, carbon, water content)
- **Mantel tests:** To test the statistical significance of correlations between community distance matrices and environmental distance matrices

All of these analyses are supported within the [[qiime]] pipeline.

## Relevance to Cultivation and Mycology

- **Community comparison:** UniFrac enables quantitative comparison of microbial communities between different growth substrates, cultivation conditions, or plant compartments, essential for optimizing cultivation practices.
- **Host genotype effects:** By distinguishing between membership (unweighted) and structure (weighted) effects, UniFrac can reveal whether host genotype influences which microbes are present or their relative abundance — critical for understanding cultivar-microbiome interactions.
- **Soil vs. cultivar effects:** The Cannabis study demonstrated that soil type dominates community membership while cultivar genotype shapes community abundance, providing actionable insights for growers managing soil and cultivar selection.
- **Niche filtering:** UniFrac analysis revealed niche-filtering of microbes in rhizosphere and endorhiza samples from bulk soil, supporting the two-step selection model for endophyte colonization.

## See Also

- [[qiime]] — The [[qiime-bioinformatics-pipeline-16s-rrna-microbiome]] that calculates UniFrac
- [[chao1-index]] — Alpha diversity metric used alongside UniFrac
- [[16s-rrna-sequencing-microbiome-analysis]] — The sequencing technology underlying UniFrac analysis
- unifrac weighted unweighted analysis cannabis microbiome — Detailed UniFrac analysis in Cannabis research
- weighted vs unweighted unifrac cannabis strain microbiome — Interpreting weighted vs. unweighted discrepancies
- [[fungal-ecology-and-environmental-biology]] — Fungal ecology context for community analysis

## Sources

- Understanding cultivar-specificity in the Cannabis microbiome (PLOS ONE, 2014)
- Lozupone C, Knight R (2005) UniFrac: a New Phylogenetic Method for Comparing Microbial Communities. Appl Environ Microbiol, 71(12):8228.
