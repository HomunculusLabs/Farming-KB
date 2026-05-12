---
title: Cultivar Specificity Plant Microbiome
created: 2026-05-11
updated: 2026-05-11
type: concept
tags: [cannabis, microbes, soil, living-soil]
sources: [raw/papers/understanding-cultivar-specificity-cannabis-microbiome.md]
---

# Cultivar Specificity in Plant Microbiome Interactions

## Overview

Cultivar specificity refers to the phenomenon where different genetic varieties (cultivars) of the same plant species maintain distinct [[cannabis-rhizosphere-microbial-communities]], particularly within root tissues. The 2014 Winston et al. study on Cannabis provided strong evidence that this specificity is driven by abundance-based selection rather than compositional differences, fundamentally shaping our understanding of how plant genetics interact with the soil microbiome.

## Defining Cultivar Specificity

In plant microbiome research, "cultivar specificity" describes the reproducible differences in [[edaphic-factors-microbial-community-structure]] that correlate with plant genotype. This concept is distinct from:

- **Species specificity** — differences in microbiome between different plant species (e.g., Cannabis vs. tomato)
- **Soil specificity** — differences driven by soil properties regardless of plant genotype
- **Individual variation** — random differences between individual plants of the same cultivar

True cultivar specificity means that if you grow Cultivar A and Cultivar B in the same soil, their root microbiomes will be consistently and significantly different, even though both communities were drawn from the same soil reservoir.

## Evidence from Cannabis

The Cannabis study provided some of the most compelling evidence for cultivar-specific microbiome selection:

### Statistical Significance Across Multiple Analyses

Cultivar effects were significant across multiple statistical frameworks:

- **ADONIS (PERMANOVA)**: [[weighted-unifrac-strain-clustering-cannabis-endorhiza-community-structure]] showed significant strain differentiation in both experiments and pooled data (R² = 0.27-0.59, all p ≤ 0.008)
- **ANOSIM**: Provided complementary non-parametric confirmation of strain-level clustering
- **RDA (Redundancy Analysis)**: Identified strain as a significant predictor of community variation
- **Mantel tests**: Confirmed correlations between community structure and both strain identity and cannabinoid profiles

### Consistency Across Experimental Designs

The cultivar effect was robust across two independent experimental designs:

1. **Experiment 1**: Three cultivars (Burmese, Bookoo Kush, Sour Diesel) in one location with minimal edaphic variation
2. **Experiment 2**: Two cultivars (White Widow, Maui Wowie) across two locations with significant edaphic variation

This design allowed the researchers to separate cultivar effects from soil effects — the first experiment maximized cultivar signal by minimizing soil variation, while the second tested whether cultivar effects persist when soil differences are large.

### Pooled Analysis Confirms Robustness

When all data were combined (five cultivars, multiple soil types, 69 samples total), cultivar remained a highly significant predictor of community structure (weighted ADONIS: R² = 0.301, p = 0.001). This confirms that the effect is not an artifact of any single experimental condition.

## Abundance-Based vs. Compositional Selection

A critical insight from the study is the nature of cultivar-specific selection:

### What Changed (Abundance)

- **71 OTUs** showed significant abundance differences between strains (weighted ANOVA, FDR-corrected)
- These differences were concentrated in Proteobacteria (Pseudomonadales, Burkholderiales, Sphingomonadales, Rhizobiales) and Bacteroidetes (Sphingobacteriales, Flavobacteriales)
- Example: *Methylophilus* comprised 13% of Bookoo Kush endorhiza but was absent from Sour Diesel

### What Did NOT Change (Composition)

- **0 OTUs** showed significant presence/absence differences between strains (unweighted g-test)
- All cultivars shared the same set of core endorhiza taxa (Pseudomonas, Cellvibrio, Oxalobacteraceae, Xanthomonadaceae, Actinomycetales, Sphingobacteriales)
- The distinction is qualitative: cultivars don't host different bacteria, they host different proportions of the same bacteria

### Implications of This Distinction

This finding means that the plant's root chemistry acts as a dial, turning up or turning down specific microbial populations rather than acting as a filter that admits or excludes species. This has important practical consequences — it means that any soil with a reasonably diverse microbial community can support any cultivar, as the necessary taxa are likely present and simply need to be enriched through root exudate-mediated selection.

## Mechanisms of Cultivar-Specific Selection

### Root Exudate Profiles

The primary mechanism of cultivar-specific selection is likely differential root exudation:

- Different cultivars produce different profiles and concentrations of sugars, amino acids, organic acids, fatty acids, [[plant-defense-chemistry-and-secondary-metabolites]]
- These exudates selectively feed certain microbial populations, causing their enrichment in the rhizosphere and endorhiza
- In Cannabis specifically, variation in cannabinoid and [[clarke-marijuana-botany-terpene-biosynthesis-aromatic-profiles]] pathways may produce different exudate profiles between cultivars
- Studies in other species have shown that even single-gene mutations affecting root exudate composition can dramatically shift the root microbiome

### Immune Recognition

Plant immune systems differentially recognize microbial-associated molecular patterns (MAMPs):

- Cultivar-specific differences in pattern recognition receptor (PRR) repertoires could allow different microbial taxa to colonize different cultivars
- The plant immune system serves as a quality control mechanism, preventing overgrowth of any single taxon

### Root Architecture

Physical differences in root structure between cultivars create different ecological niches:

- Root branching patterns affect oxygen availability and nutrient diffusion gradients
- Root hair density influences the surface area available for microbial attachment
- Lateral root formation creates distinct microenvironments

## Cannabinoid-Microbiome Connection

The study revealed a provocative correlation between cannabinoid profiles and endorhiza community structure:

- Unweighted Mantel test: r-stat = 0.863, p = 0.001 (highly significant)
- This correlation suggests that cannabinoid-producing cultivars may shape their microbiome differently than non-producing or low-producing varieties
- However, confounding with soil type (one soil produced both higher THC and different edaphic conditions) prevents definitive causal claims
- This remains an open question with significant implications for understanding whether secondary metabolites in Cannabis directly influence microbial recruitment

## Broader Context in Plant Science

The Cannabis findings align with and extend observations from other crop species:

- **Rice**: Different rice cultivars maintain distinct rhizosphere communities, with differences driven by root exudate composition
- **Maize**: Inbred lines show reproducible microbiome differences that correlate with disease resistance traits
- **Arabidopsis**: Mutants affecting root exudate production show altered microbiome profiles
- **Wheat**: Modern cultivars have lost some of the microbial diversity found in landraces and wild relatives

The Cannabis study adds to this body of evidence by demonstrating cultivar specificity in a species with an exceptionally rich secondary metabolite profile, raising the question of whether these metabolites play a unique role in microbiome selection.

## Applications in Cultivation

### Inoculant Strategy

- Generic microbial inoculants may not perform equally well across all cultivars
- Cultivar-specific inoculant formulations could be developed based on the natural enrichment patterns observed in each cultivar's endorhiza
- Alternatively, broad-spectrum inoculants with diverse taxa allow the plant's own selection mechanisms to operate

### Breeding Considerations

- If specific endorhiza profiles correlate with desirable traits (yield, potency, disease resistance), microbiome composition could potentially be used as a selection criterion in breeding programs
- The correlation between cannabinoid profiles and microbiome structure (r = 0.863) is particularly intriguing in this context

### Living Soil Management

- Maintaining maximum soil microbial diversity ensures that the full pool of potential endorhiza colonizers is available for any cultivar's selection mechanisms
- This is a key argument for no-till, organic, living soil approaches over sterile or heavily amended conventional methods

## Related Concepts

- [[rhizosphere-ecology]]
- [[cannabis-endorhiza-bacterial-communities]]
- [[crimson-clover]]
- living soil microbial food web

## See Also

- Winston ME et al. (2014) "Understanding Cultivar-Specificity and Soil Determinants of the Cannabis Microbiome." PLoS ONE 9(6): e99641
