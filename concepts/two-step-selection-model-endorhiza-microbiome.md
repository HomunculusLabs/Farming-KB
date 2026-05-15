---
title: Two-Step Selection Model for Endorhiza Microbiome Assembly
source: understanding-cultivar-specificity-cannabis-microbiome.md
type: concept
---

## Overview

The two-step selection model is a widely accepted framework describing how root endophytic (endorhiza) microbial communities are assembled. The model proposes that bulk soil microbial communities first undergo filtering by plant-derived rhizodeposits in the rhizosphere, followed by convergent host genotype-dependent selection on endophytic communities within the root interior. This model has been validated across multiple plant species, including [[cannabis-sativa]], [[arabidopsis-thaliana]], and Populus deltoides.

## Step 1: Rhizosphere Filtering

The first selection step occurs at the root-soil interface. Plants release a rich mixture of exudates, mucilage, and lysates — collectively termed rhizodeposits — into the surrounding soil. These compounds selectively enrich certain microbial taxa while depleting others from the broader bulk soil community. Key characteristics of this step include:

- **Soil type is the primary determinant** of microbial community composition in the rhizosphere. In studies on Cannabis, soil type explained the largest proportion of variance along principal coordinate axis PC1 (32.06% in unweighted analysis).
- **Niche filtering** reduces taxonomic diversity from bulk soil to rhizosphere. Alpha diversity consistently decreases from bulk soil to rhizosphere to endorhiza compartments.
- **Edaphic factors** — particularly nitrogen, carbon, and water availability — strongly structure rhizosphere communities. In one study, these three factors optimally explained variance in community data (rho = 0.632).
- The rhizosphere acts as a **bridge** between the bulk soil reservoir and the root interior, with shared OTUs between rhizosphere and endorhiza significantly exceeding those between bulk soil and endorhiza directly.

## Step 2: Host Genotype-Dependent Selection

The second step involves the host plant's genotype exerting selective pressure on which microbes successfully colonize the root interior (endorhiza). This step is characterized by:

- **Convergent selection**: Different host genotypes (cultivars) select for distinct endophytic communities, even when grown in the same soil.
- **Abundance-driven differentiation**: In Cannabis, cultivar was the main determinant of community structure when abundance was weighted (PC1 = 34.51%), but not in unweighted (composition-only) analysis. This suggests host selection primarily acts by modulating relative abundances of taxa rather than strict presence/absence filtering.
- **Cultivar-specific OTUs**: In Cannabis studies, 71 OTUs significantly differed between cultivars in the endorhiza when accounting for abundance, compared to 657 OTUs differing between soil types — showing soil remains dominant but cultivar effects are substantial.
- **Persistence of signal post-harvest**: Remarkably, cultivar-specificity was still detectable in endorhiza samples taken 8 weeks post-harvest, suggesting the host genotype imprints a lasting community structure.

## Evidence from Cannabis Microbiome Studies

### Alpha Diversity Patterns

Diversity follows a consistent gradient across root compartments:

| Compartment | Chao1 (Exp. 1, MB soil) | Chao1 (Exp. 2, MB soil) | Chao1 (Exp. 2, OC soil) |
|-------------|------------------------|------------------------|------------------------|
| Bulk soil | 2,010.7 | 2,319.1 | 2,004.8 |
| Rhizosphere | — | — | — |
| Endorhiza | 916.1 | 1,413 | 1,374 |

The reduced endorhiza diversity in the first experiment (post-harvest sampling) was attributed to early stages of root decay rather than true biological differences, as confirmed by elevated Cellvibrio (a cellulolytic bacterium) abundance.

### Beta Diversity and Community Structure

- **Unweighted analysis**: Soil type dominated community differentiation; rhizosphere and endorhiza samples formed significantly differentiated clusters from bulk soil along PC2 (11.34%).
- **Weighted analysis**: Cannabis strain became the dominant factor (PC1 = 34.51%), indicating host genotype controls community structure (abundance) more than composition alone.
- **OTU overlap**: Significantly more OTUs were shared between endorhiza and their own bulk soil than between endorhiza and foreign bulk soil, supporting soil inheritance.

### The Cellvibrio Anomaly

The first experiment revealed unusually high Cellvibrio abundance in the endorhiza (16.9% vs. 0.095% in the second experiment). Cellvibrio is a known cellulolytic bacterium, and its elevated presence was traced to root decay processes occurring during the 8-week post-harvest interval before sampling. This finding has important methodological implications:

- Post-harvest sampling can confound endophyte community analysis
- Cellulolytic taxa may serve as indicators of tissue degradation rather than true endophytes
- Active-growth sampling is essential for accurate characterization

## Limitations and Unresolved Questions

Despite strong support for the two-step model, several expectations remain unvalidated:

1. **Rhizosphere intermediacy**: While mean beta-diversity distances show rhizosphere communities are intermediate between bulk soil and endorhiza, this difference was not statistically significant in Cannabis studies, providing weak evidence for the predicted first differentiation step.
2. **Cannabinoid influence**: The specific role of cannabinoid production in structuring endorhiza communities remains unclear and requires decoupling from edaphic factors.
3. **Temporal dynamics**: How endorhiza communities vary across the reproductive cycle and between growth stages is not well understood.
4. **Mechanistic basis**: Which specific aspects of host genotype (root architecture, exudate profile, immune responses) drive the observed selection patterns?

## Applications and Future Directions

Understanding the two-step selection model has practical implications for agriculture and biotechnology:

- **Microbial inoculants**: Identifying cultivar-specific core microbiome members could enable targeted probiotic development
- **Plant fitness**: Manipulating rhizosphere communities to suppress disease or increase stress tolerance
- **Metabolite augmentation**: Leveraging microbiome-host interactions to enhance production of desired secondary metabolites
- **Breeding programs**: Selecting cultivars that recruit beneficial microbial communities

Future research priorities include sampling endorhiza communities across time series, testing across more cultivars, and performing mechanistic studies on how specific host traits shape microbial assembly.

## Key References

- Bulgarelli et al. (2012) — Revealing structure and assembly cues for Arabidopsis root-inhabiting bacterial microbiota. *Nature*, 488, 91–95.
- Garbeva et al. (2004) — Microbial diversity in soil: selection by plant and soil type. *Annu. Rev. Phytopathol.*, 42, 243–270.
- Berg & Smalla (2009) — Plant species and soil type cooperatively shape microbial communities in the rhizosphere. *FEMS Microbiol. Ecol.*, 68, 1–13.
- Winston et al. (2014) — The Cannabis Microbiome. *PLOS ONE*, 9(6), e99641.

## See Also
- [[weighted-unifrac-strain-clustering-cannabis-endorhiza-community-structure]]
- [[strain-otu-presence-absence-vs-abundance-cannabis-microbiome]]
- [[otu-abundance-vs-presence-absence-cannabis-strain-microbiome]]
