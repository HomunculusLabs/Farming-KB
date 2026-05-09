---
title: cultivar-cannabis-microbiome-two-tier-selection-model Two-Tier two-tier-selection-model-plant-microbiome
source: raw/papers/understanding-cultivar-specificity-cannabis-microbiome.md
tags: [microbiome, cannabis, rhizosphere, endorhiza, plant-microbe-interactions]
created: 2026-05-09
---

# Cannabis Microbiome Two-Tier Selection Model

The two-tier selection model describes how plant-associated microbial
communities are assembled through two sequential filtering steps: first
by soil [[soil-edaphic-factors-microbial-communities]], then by host genotype. This model was tested
and supported by the first comprehensive characterization of the Cannabis
microbiome across five cultivars (Winston et al., 2014, PLOS ONE).

## Model Overview

### Tier 1: Soil Selection
Edaphic factors (soil type, pH, nitrogen, carbon, salinity, water
content) determine the composition of the local soil microbiota. This
soil community serves as the source pool for root colonization. The
key insight is that **soil type is the strongest predictor of which
microbes are present** across all sample types.

### Tier 2: Host Genotype Selection
As microbes migrate from the rhizosphere into root tissues (endorhiza),
the plant exerts genotype-dependent selection on community structure.
This second filter acts primarily on **microbial abundance** rather than
presence/absence, fine-tuning which soil-derived organisms thrive
inside the plant.

## Experimental Evidence from Cannabis

### Study Design
Two experiments examined the Cannabis microbiome:

**Experiment 1**: Three strains (Burmese, BooKoo Kush, Sour Diesel) in
similar soil, sampled 8 weeks post-harvest. 27 samples total.

**Experiment 2**: Two strains (White Widow, Maui Wowie) in two
distinctly different soil types, sampled 2 weeks pre-harvest. 42
samples. This experiment introduced significant edaphic variation
to test soil vs. genotype effects.

### Key PCoA Findings
- **Unweighted analysis** (presence/absence): PC1 dominated by soil
  type (32.06% variance), confirming soil as the primary compositional
  determinant
- **Weighted analysis** (abundance): PC1 dominated by [[blesching-cannabis-strain-selection-receptor-targeting]]
  (34.51% variance), showing cultivar drives community structure
- All sample types (bulk soil, rhizosphere, endorhiza) formed
  significantly differentiated clusters in weighted analyses

### OTU Analysis
- **690 significant OTUs** differed between soil types (weighted)
- **657 significant OTUs** differed between soil types (unweighted)
- **71 significant OTUs** differed between strains (weighted)
- **0 significant OTUs** differed between strains (unweighted)

This pattern confirms that soil determines who is present, while strain
determines their relative abundance within the plant.

## Edaphic Factor Importance

BEST analysis identified three edaphic factors optimally explaining
community variance (rho = 0.632):

1. **Nitrogen** — strongest individual correlate (weighted r = 0.465,
   unweighted r = 0.630)
2. **Salinity** — second strongest (weighted r = 0.437, unweighted
   r = 0.620)
3. **Carbon** — third (weighted r = 0.330, unweighted r = 0.512)
4. **Water content** — fourth (weighted r = 0.281, unweighted r = 0.466)
5. **pH** — fifth (weighted r = 0.221, unweighted r = 0.292)

All edaphic factors were significantly correlated with community
beta-diversity (p = 0.001) in both experiments.

## Community Shifts from Soil to Root

The transition from bulk soil to endorhiza involves predictable
taxonomic shifts:

- **Decrease**: Acidobacteria (especially order iii1-15), dramatic
  reduction in endorhiza (Bonferroni-corrected ANOVA: p = 1.12e-7)
- **Increase**: Proteobacteria and Actinobacteria within endorhiza
- **Core endorhiza community**: Pseudomonas, Cellvibrio, Oxalobacteraceae,
  Xanthomonadaceae, Actinomycetales, Sphingobacteriales — predominantly
  Gammaproteobacteria and Alphaproteobacteria

Of 51 OTUs significantly different between sample types, 17 increased
in abundance within the [[edaphic-factors-cannabis-endorhiza-microbiome-assembly]]. These were predominantly
Proteobacteria, including several from the Rhizobiales order.

## Alpha Diversity Gradient

Diversity peaks in bulk soil and declines toward the root interior:

| Sample Type | Chao1 (Exp. 2, MB soil) | Chao1 (Exp. 2, OC soil) |
|-------------|------------------------|------------------------|
| Bulk soil | 5597 | 4296 |
| Rhizosphere | 4859 | 3913 |
| Endorhiza | 3325 | 3311 |

This gradient reflects progressive filtering from a diverse soil
community to a smaller, more selected endophytic population. Despite
differences in bulk soil diversity between soil types, endorhiza
diversity converged, suggesting a bounded host-selected niche.

## Shared OTU Analysis

Endorhiza communities share significantly more OTUs with their own soil
than with a foreign soil (t = -10.05, p = 1.2e-15), confirming that
soil microbes are the source pool for root colonization. White Widow
grown in two different soils shared more OTUs with their respective
native soil (mean = 2934) than with the foreign soil (mean = 2162).

## Implications for Cannabis Cultivation

1. **Soil choice fundamentally shapes the available microbial pool** —
   select soils with favorable physicochemical properties
2. **Cultivar genetics fine-tune which microbes colonize roots** —
   different strains recruit distinct endorhiza communities
3. **Nitrogen management is critical** — it's the strongest edaphic
   driver of community structure
4. **Cannabinoid-microbiome links are confounded by soil** — THC
   correlates with community structure but also with edaphic variables,
   making causation difficult to establish

- [[cannabis-microbiome-otu-abundance-vs-presence-cannabis-strains]]
## See Also

- [[cannabis-rhizosphere-endorhiza-communities]] — detailed community
  composition data
- [[pf-tek-substrate-preparation]] — substrate [[singh-bioreactor-design-for-fungal-bioremediation]]
  cultivation

## References

- Winston ME et al. Understanding Cultivar-Specificity and Soil
  Determinants of the Cannabis Microbiome. PLOS ONE 9(6): e99641, 2014.
- Bulgarelli D et al. Structure and Functions of the Bacterial
  Microbiota of Plants. Annu Rev Plant Biol, 2013.
