---
title: Beta Diversity Distances Bulk Soil Rhizosphere Cannabis Endorhiza
source: understanding-cultivar-specificity-cannabis-microbiome.md
tags:
  - cannabis
  - microbiome
  - beta-diversity
  - rhizosphere
  - endorhiza
  - bulk-soil
  - community-similarity
  - unifrac
  - two-tier-selection
  - niche-differentiation
---

## Overview

The Winston et al. (2014) [[winston-cannabis-microbiome-study-design]] provided quantitative measurements of community dissimilarity between three root-associated compartments — bulk soil, rhizosphere soil, and endorhiza (root interior) — using both weighted and [[weighted-vs-unweighted-unifrac-cannabis-strain-microbiome]] distances. These inter-compartment distance comparisons revealed a key pattern: rhizosphere and bulk soil communities are significantly more similar to each other than either is to the [[proteobacteria-dominance-cannabis-endorhiza-community]]. This finding has implications for understanding how root colonization progresses and whether the two-tier selection model's predicted intermediate step between soil and endorhiza is detectable as a distinct community state.

## The Three Compartments

The Cannabis microbiome study sampled three distinct microbial habitats associated with the root system:

- **Bulk soil**: Soil collected 10 cm from the stem at 20 cm depth, representing the general soil [[edaphic-factors-microbial-community-structure]] uninfluenced by direct root interaction. This is the source pool from which rhizosphere and endorhiza communities are drawn.

- **Rhizosphere soil**: Soil remaining adhered to roots after gentle shaking, representing the zone of direct root influence where exudates, mucilage, and sloughed root cells alter the microbial environment. This is the first tier of selection in the two-tier model.

- **Endorhiza**: The root interior after [[challenge-organisms-nasa-microwave-surface-sterilization-testing]] (alcohol and sterile water rinsing), representing bacteria that have colonized root tissue itself. This is the second tier of selection where host genotype effects become dominant.

## Distance Comparisons: Rhizosphere-Bulk Soil vs. Rhizosphere-Endorhiza

The study compared beta-diversity distances between all pairs of compartments using both weighted and unweighted UniFrac. The key finding was that rhizosphere-to-bulk-soil distances were significantly lower than rhizosphere-to-endorhiza distances, and this pattern held for both distance metrics:

- **Unweighted**: Mean rhizosphere-bulk soil distance was significantly lower than rhizosphere-endorhiza distance (t = 24.59, p < 0.001)
- **Weighted**: Mean rhizosphere-bulk soil distance was significantly lower than rhizosphere-endorhiza distance (t = 211.82, p < 0.001)

The extremely high t-statistic for the weighted comparison (211.82) reflects the large effect size — the abundance-weighted [[edaphic-determinants-cannabis-microbiome-community-structure]] of the rhizosphere is far more similar to bulk soil than to the endorhiza interior. This makes intuitive sense: the rhizosphere is essentially modified soil, while the endorhiza represents a fundamentally different ecological niche.

## Bulk Soil-Endorhiza vs. Rhizosphere-Endorhiza Distances

A second comparison tested whether bulk soil and endorhiza communities were more different from each other than rhizosphere and endorhiza communities. In the two-tier model, the rhizosphere represents an intermediate step between soil and root interior, so one might expect the rhizosphere-endorhiza distance to be smaller than the bulk soil-endorhiza distance (the rhizosphere being "closer" to the endorhiza than bulk soil is).

The results were:

- **Unweighted**: Rhizosphere-endorhiza distance was not significantly different from bulk soil-endorhiza distance (t = 22.10, p = 0.109)
- **Weighted**: Rhizosphere-endorhiza distance was not significantly different from bulk soil-endorhiza distance (t = 22.23, p = 0.078)

Both comparisons showed a trend toward the rhizosphere being intermediate, but neither reached statistical significance. This is a notable finding because it suggests that the rhizosphere may not represent a strongly differentiated intermediate community state between bulk soil and endorhiza, at least as measured by these distance metrics.

## Implications for the Two-Tier Selection Model

The two-tier selection model predicts a stepwise filtering process: bulk soil communities are filtered by rhizodeposition to create a rhizosphere community (tier one), and then rhizosphere communities are further filtered by host genotype to create an endorhiza community (tier two). This model predicts that community distances should follow the pattern: bulk soil-endorhiza > rhizosphere-endorhiza > bulk soil-rhizosphere.

The Cannabis data partially support this prediction. The bulk soil-rhizosphere distance is indeed the smallest (both metrics), confirming that the rhizosphere represents a modest modification of the soil community rather than a wholesale transformation. However, the failure to find a significant difference between bulk soil-endorhiza and rhizosphere-endorhiza distances is problematic for the model's predicted intermediate step.

The authors acknowledge this discrepancy, noting that the rhizosphere and endorhiza distances from bulk soil "were not significantly different and thus provides little evidence for the first differentiation step of the two-step selection model." This does not invalidate the two-tier model but suggests that the rhizosphere-to-endorhiza transition may be more abrupt than gradual — the endorhiza community may diverge dramatically from the rhizosphere in a single selection step rather than through a series of incremental changes.

## Alternative Interpretations

### Rhizosphere as a Gradient Rather Than a Discrete Compartment

One explanation for the lack of significant distance differences between bulk soil-endorhiza and rhizosphere-endorhiza pairs is that the rhizosphere is not a discrete compartment but a gradient of decreasing soil influence and increasing root influence. The operational definition of rhizosphere as "soil remaining after shaking" creates an arbitrary boundary that may not correspond to a biologically meaningful community transition. The true rhizosphere effect may be distributed across a spatial gradient, and the sampling method may capture a mixture of soil-like and root-influenced communities that averages out to an intermediate position.

### Strong Endorhiza Filtering Overwhelming Rhizosphere Signal

Another interpretation is that the endorhiza filtering step is so strong that it essentially erases the rhizosphere signal. If host genotype imposes a very selective filter on which bacteria can colonize root tissue — allowing only a narrow subset of rhizosphere taxa to enter — then the endorhiza community will be dramatically different from both the rhizosphere and bulk soil, making it difficult to detect a significant intermediate step. Under this interpretation, the two-tier model is still correct, but the second tier is the dominant driver of community differentiation.

### Sampling Methodology Effects

The rhizosphere sampling method — shaking roots into a whirlpak bag — may include some loosely attached soil particles that dilute the true rhizosphere signal, making rhizosphere communities appear more soil-like than they biologically are. Conversely, the endorhiza sterilization protocol (alcohol and sterile water rinsing) may not perfectly remove all [[lowenfels-rhizosphere-bacteria-plant-interaction]] from the root surface, potentially contaminating endorhiza samples with rhizosphere taxa. Both sampling artifacts would act to reduce the apparent distance between compartments, potentially masking genuine differentiation steps.

## Comparison with Alpha-Diversity Patterns

The beta-diversity distance results can be compared with the alpha-diversity gradient observed in the same study. Alpha diversity (chao1) showed a stepwise decline: bulk soil (m = 4947) > rhizosphere (m = 4525) > endorhiza (m = 3321) in the second experiment. The modest bulk soil-to-rhizosphere reduction (8.5%) and the much larger rhizosphere-to-endorhiza reduction (26.6%) parallel the beta-diversity pattern: the rhizosphere is a modestly impoverished version of the soil community, while the endorhiza represents a dramatic filtering event.

The consistency between alpha and beta diversity patterns strengthens the conclusion that the rhizosphere represents a relatively minor modification of the bulk soil community, while the transition to the endorhiza involves a major community restructuring driven primarily by host genotype.

## Taxonomic Composition of the Transition

The taxonomic shifts associated with the soil-to-rhizosphere-to-endorhiza transition were characterized by a predictable pattern of phylum-level changes. As predicted by the two-tier model, Acidobacteria showed a dramatic decrease in abundance from bulk soil to endorhiza (the most significant OTU difference between sample types was Acidobacteria from order iii1-15, Bonferroni-corrected ANOVA: p = 1.12e-7). Conversely, Proteobacteria (particularly Gammaproteobacteria and Alphaproteobacteria) and Actinobacteria increased in relative abundance within the endorhiza.

Of the 51 OTUs significantly different between sample types in the weighted analysis, 17 increased in abundance within the Cannabis endorhiza relative to the rhizosphere, and these were predominantly Proteobacteria from the Rhizobiales order. The mean abundance of these 51 differentially abundant OTUs was highly correlated between bulk soil and rhizosphere (Pearson's rho: 0.92), less correlated between rhizosphere and endorhiza (rho: 0.63), and least correlated between bulk soil and endorhiza (rho: 0.42). This gradient of decreasing correlation mirrors the beta-diversity distance pattern.

## Methodological Details

Beta-diversity distances were computed using QIIME 1.7.0 with both weighted and unweighted UniFrac metrics. The phylogenetic tree was built using FastTree from PyNAST-aligned sequences against the Greengenes core set. Significance of distance comparisons was assessed using pairwise t-tests between distance matrices, with all samples from both experiments included in the analysis. Samples were rarified to an even depth of 3,000 sequences (first experiment) or 45,000 sequences (second experiment) before distance computation.

The use of triplicate samples per plant (three separate root samples per plant) in the second experiment provided within-plant replication that allowed estimation of within-plant heterogeneity, though these pseudoreplicates do not represent true biological independence. The PCoA visualization of community distances showed clear clustering patterns, with PC1 dominated by soil type (32.06% variance in [[unifrac-weighted-unweighted-analysis-cannabis-microbiome]]) and PC2 dominated by sample type differentiation (11.34% variance).
