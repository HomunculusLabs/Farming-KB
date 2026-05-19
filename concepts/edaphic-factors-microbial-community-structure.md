---
title: Edaphic Factors and Microbial Community Structure
source: understanding-cultivar-specificity-cannabis-microbiome.md
type: concept
---

## Edaphic Factors and Microbial Community Structure

Edaphic factors — the physical, chemical, and biological properties of soil — are the dominant determinants of microbial community composition in the [[cannabis-root-microbiome]], outweighing the effects of plant genotype and compartment ([[rhizosphere]] vs. endorhiza). Understanding these relationships is critical for managing soil health in agricultural systems.

## Hierarchy of Determinants

Research across multiple Cannabis cultivars and soil types established a clear hierarchy of factors influencing microbial communities:

1. **Soil type / edaphic properties** — strongest effect (690 significant weighted OTUs, 657 unweighted)
2. **Strain / cultivar** — secondary effect on abundances only (71 significant weighted OTUs, 0 unweighted)
3. **Sample type** (bulk soil, rhizosphere, endorhiza) — tertiary effect (51 significant weighted OTUs, 11 unweighted)

Soil properties determined both which organisms were **present** (unweighted analysis) and their **relative abundances** (weighted analysis), while strain only influenced abundances.

## The Five Key Edaphic Factors

### Nitrogen (Dominant Factor)

Nitrogen content had the strongest correlation with microbial community structure across all analyses:

- **Weighted UniFrac**: r-stat = 0.465, p = 0.001
- **Unweighted UniFrac**: r-stat = 0.630, p = 0.001

Nitrogen availability directly influences microbial metabolism, as it is essential for protein synthesis, nucleotide formation, and cellular growth. Different microbial taxa have varying nitrogen utilization strategies (ammonification, nitrification, nitrogen fixation), and nitrogen levels select for communities adapted to the prevailing form and concentration.

### Salinity

Salinity was the second most important factor:

- **Weighted**: r-stat = 0.437, p = 0.001
- **Unweighted**: r-stat = 0.620, p = 0.001

Soil salinity affects osmotic potential, limiting water availability to microorganisms. Halotolerant and halophilic taxa are favored in saline conditions, while sensitive organisms are excluded. The strong effect in both weighted and unweighted analyses indicates salinity influences both community membership and structure.

### Carbon

Organic carbon content ranked third:

- **Weighted**: r-stat = 0.330, p = 0.001
- **Unweighted**: r-stat = 0.512, p = 0.001

Carbon is the primary energy source for heterotrophic soil microorganisms. Carbon content determines the total metabolic capacity the soil can support and selects for taxa adapted to the quality and quantity of available organic matter.

### Water Content

Soil moisture ranked fourth:

- **Weighted**: r-stat = 0.281, p = 0.001
- **Unweighted**: r-stat = 0.466, p = 0.001

Water content governs diffusion of nutrients and gases, microbial motility, and substrate availability. Water-filled pore space affects aerobic vs. anaerobic conditions, selecting for metabolically appropriate communities.

### pH

[[soil-ph]] had the weakest but still highly significant effect:

- **Weighted**: r-stat = 0.221, p = 0.001
- **Unweighted**: r-stat = 0.292, p = 0.001

Soil pH influences [[nutrient-availability]] (through solubility effects), enzyme activity, and membrane transport. Most soil bacteria prefer near-neutral pH, while fungi tend to tolerate broader pH ranges.

## BEST Analysis

A Best Subset of Environmental Variables with Maximum (Rank) Correlation with Community Dissimilarities (BEST) analysis was used to identify the optimal combination of edaphic variables for predicting community structure. This multivariate approach confirmed that nitrogen and salinity together explained the largest portion of community variation, with carbon, water content, and pH providing additional predictive power.

## Soil Type Effects on Diversity

Alpha diversity showed consistent patterns related to soil type:

- **Mo-Bio (MB) soil**: Higher bulk soil diversity (Chao1: 5597) and rhizosphere diversity (Chao1: 4859)
- **Orange County (OC) soil**: Lower bulk soil diversity (Chao1: 4296) and rhizosphere diversity (Chao1: 3913)
- **Endorhiza diversity**: Not significantly different between soil types (MB: 3325, OC: comparable)

This suggests that while soil type determines the starting microbial pool, the host plant's filtering effect during endophyte colonization converges on a similar diversity level regardless of soil origin.

## Community Composition Shifts

Edaphic factors drive systematic shifts in taxonomic composition:

### Decreasing from Bulk Soil to Endorhiza
- **Acidobacteria**: Dramatic decrease, particularly order iii1-15 (Bonferroni-corrected ANOVA: p = 1.12e-7)
- Acidobacteria are typically oligotrophic and adapted to low-nutrient conditions; the carbon-rich rhizosphere environment favors copiotrophic taxa

### Increasing from Bulk Soil to Endorhiza
- **Proteobacteria**: Significant increase, particularly Rhizobiales
- **Actinobacteria**: Increased abundance in root-associated compartments
- **17 of 51 sample-type-differentiating OTUs** increased in the endorhiza, predominantly Proteobacteria

## Implications for Agricultural Management

### Soil as the Primary Lever

Since soil properties dominate microbial community structure, soil management is the most effective strategy for cultivating beneficial microbiomes:

1. **Nitrogen management** should be the top priority — both the form (ammonium vs. nitrate) and quantity significantly shape communities
2. **Salinity monitoring** is critical, especially in arid regions or with saline irrigation water
3. **Organic matter amendments** increase carbon availability, supporting diverse microbial populations
4. **Moisture management** through irrigation scheduling affects both water content and the aerobic/anaerobic balance
5. **pH adjustment** through liming or acidification can shift community composition toward desired taxa

### Cultivar Selection as a Secondary Lever

While strain effects are secondary to soil, they are biologically meaningful for the endorhiza compartment. This suggests:

- Probiotic inoculants may need strain-specific formulation
- Breeding programs could select for cultivars that recruit beneficial endophytes
- The interaction between soil and genotype offers opportunities for optimized pairing

## Analytical Framework

Edaphic-microbiome relationships were characterized using:

- **Mantel tests**: Correlating edaphic distance matrices with community dissimilarity matrices
- **ADONIS (PERMANOVA)**: Partitioning variance by soil type, strain, and sample type
- **RDA (Redundancy Analysis)**: Identifying which edaphic variables best explain community variation
- **BEST analysis**: Finding the optimal subset of environmental variables
- **UniFrac distances**: Both weighted (abundance-sensitive) and unweighted (presence/absence) metrics

## Key References

- Winston, M. E. et al. (2014). Understanding cultivar-specificity and soil determinants of the [[cannabis-microbiome]]. *PLoS ONE*, 9(6), e99641.
- Fierer, N. & Jackson, R. B. (2006). The diversity and biogeography of soil bacterial communities. *PNAS*, 103(3), 626-631.
- Lauber, C. L. et al. (2009). Pyrosequencing-based assessment of soil pH as a predictor of soil bacterial community structure. *ISME J.*, 3, 517-527.
