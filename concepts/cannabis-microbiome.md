---
title: Cannabis Microbiome
source: understanding-cultivar-specificity-cannabis-microbiome.md
type: concept
---

## Cannabis Microbiome

The Cannabis microbiome — the community of microorganisms associated with [[cannabis-sativa]] roots and surrounding soil — exhibits distinct compartmentalization and is shaped by a hierarchy of factors led by soil edaphic properties, followed by plant cultivar (strain), and sample type (bulk soil, rhizosphere, or endorhiza). Research by Winston et al. (2014) provided the first comprehensive characterization of these communities across multiple Cannabis strains and soil types.

## Compartmentalization

The Cannabis root system supports three distinct microbial compartments with decreasing similarity:

### Bulk Soil
The soil not directly influenced by roots. Serves as the reservoir microbial community from which rhizosphere and endorhiza communities are recruited.

### Rhizosphere
Soil immediately adjacent to and influenced by [[root-exudates]]. Microbial communities are intermediate between bulk soil and endorhiza, showing:
- Decreased abundance of **Acidobacteria** compared to bulk soil
- Increased **Proteobacteria** and **Actinobacteria**
- Beta diversity distances significantly closer to bulk soil than to endorhiza

### Endorhiza (Endosphere)
Microbes living inside root tissue. The most distinct community, characterized by:
- Dramatic reduction in alpha diversity (Chao1: ~3321 vs. ~4947 in bulk soil)
- Core community dominated by well-known endophytic bacteria: **Pseudomonas, Cellvibrio, Oxalobacteraceae, Xanthomonadaceae, Actinomycetales, Sphingobacteriales**
- Predominantly **Gammaproteobacteria** and **Alphaproteobacteria**
- Enrichment of **Rhizobiales** relative to other compartments

The correlation of OTU abundances decreases progressively: bulk soil ↔ rhizosphere (ρ = 0.92) > rhizosphere ↔ endorhiza (ρ = 0.63) > bulk soil ↔ endorhiza (ρ = 0.42), demonstrating the stepwise selection process.

## Factors Structuring the Microbiome

### Soil Type (Strongest Factor)

Soil properties are the dominant determinant of community composition across all compartments:

| Edaphic Factor | Weighted UniFrac r-stat | Unweighted UniFrac r-stat |
|----------------|------------------------|--------------------------|
| Nitrogen | 0.465 | 0.630 |
| Salinity | 0.437 | 0.620 |
| Carbon | 0.330 | 0.512 |
| Water content | 0.281 | 0.466 |
| pH | 0.221 | 0.292 |

All edaphic factors were significantly correlated with community beta-diversity (p = 0.001 for all). Nitrogen was consistently the most important structuring factor, followed by salinity and carbon content.

### Strain / Cultivar (Secondary Factor)

Cannabis strain influences OTU **abundances** (weighted analysis) but has minimal effect on OTU **presence/absence** (unweighted analysis):

- **No significant unweighted OTU differences** between strains (0 significant OTUs)
- **71 significant weighted OTU differences** between strains
- Strain differences were predominantly in **Proteobacteria**: Pseudomonadales, Burkholderiales, Sphingomonadales, Rhizobiales
- **Bacteroidetes** (Sphingobacteriales, Flavobacteriales) also contributed to strain-level differentiation

Notable strain-specific associations:
- **Methylophilus** comprised 13% of Bookoo Kush endorhiza but only 0.13% in Burmese and was absent in [[sour-diesel]]
- **Sphingomonas wittichii** was prevalent in [[maui-wowie]], a bacterium that can metabolize phenazine-1-carboxylic acid and is associated with increased soil survival

### Sample Type (Tertiary Factor)

The transition from bulk soil through rhizosphere to endorhiza drives systematic changes:

- **51 OTUs significantly different** between sample types (weighted analysis)
- **Acidobacteria** (order iii1-15) showed the most significant decrease in endorhiza (Bonferroni-corrected ANOVA: p = 1.12e-7)
- **17 of 51 differentiating OTUs increased** in the endorhiza, predominantly Proteobacteria including Rhizobiales

## The Two-Step Colonization Model

The data support a two-step model of root microbiome assembly:

### Step 1: Rhizodeposition-Driven Recruitment
Root exudates (sugars, amino acids, organic acids) selectively enrich certain taxa from the bulk soil community, forming the rhizosphere. This step is primarily driven by **soil properties** and general plant metabolic processes.

### Step 2: Host Genotype Fine-Tuning
The plant's genotype (strain) further selects specific taxa for colonization of the internal root tissue (endorhiza). Evidence:

- Endorhiza communities share significantly more OTUs with their **own soil** than with a different soil growing the same strain (mean shared OTUs: 2934 vs. 2162, p = 1.2e-15)
- Strain-level differences in community structure were significant only within the endorhiza compartment
- Rhizosphere communities showed mixed strain-level significance, while bulk soil showed none

This confirms that soil provides the microbial pool, but host genotype determines which organisms successfully colonize the root interior.

## Cannabinoid-Microbiome Correlations

Mantel tests revealed significant correlations between cannabinoid profiles and endorhiza community structure (unweighted r-stat: 0.863, p = 0.001). However, this relationship is confounded by:

- THC concentration and composition were significantly higher in plants from one soil type
- THC variables were also significantly correlated with soil edaphic variables
- The cannabinoid-microbiome association cannot be disentangled from the soil physicochemical effect

This remains an open question requiring controlled experiments with standardized soil conditions.

## Bioinformatic Methods

The study employed standard 16S rRNA V4 amplicon sequencing analyzed with QIIME 1.7.0:

- **Reference database**: Greengenes pre-clustered at 97% identity
- **Alignment**: PyNAST against Greengenes core set
- **Phylogenetic tree**: FastTree
- **Taxonomy**: RDP classifier retrained on Greengenes
- **Rarefaction**: 3,000 sequences (Experiment 1), 45,000 sequences (Experiment 2)
- **Diversity metrics**: Weighted and unweighted UniFrac, alpha diversity (Chao1, observed species)
- **Statistical tests**: ADONIS, ANOSIM, Mantel tests, RDA, BEST analysis

## Agricultural Implications

Understanding the Cannabis microbiome has practical implications:

1. **Soil selection** is the most impactful decision for shaping beneficial microbial communities
2. **Strain-specific microbial associations** suggest that probiotic inoculants may need to be tailored to specific cultivars
3. **Endophytic communities** may influence plant health, nutrient uptake, and secondary metabolite production
4. **Nitrogen management** has the strongest influence on community structure and should be optimized for beneficial microbial associations

## Key References

- Winston, M. E. et al. (2014). Understanding cultivar-specificity and soil determinants of the Cannabis microbiome. *PLoS ONE*, 9(6), e99641.
- Lundberg, D. S. et al. (2012). Defining the core [[arabidopsis-thaliana]] root microbiome. *Nature*, 488, 86-90.
- Bulgarelli, D. et al. (2012). Revealing structure and assembly cues for Arabidopsis root-inhabiting bacterial microbiota. *Nature*, 488, 91-95.
