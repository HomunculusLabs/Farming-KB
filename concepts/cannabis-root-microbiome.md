---

title: Cannabis Root Microbiome
created: 2026-04-12
updated: 2026-04-12
type: concept

tags:
- cannabis
- microbiome
- microbes
- soil
- living-soil
- biology
- symbiosis
- vegetables
- processing
- ph

sources:
- raw/papers/understanding-cultivar-specificity-cannabis-microbiome.md
---

## Cannabis Root Microbiome

The cannabis root microbiome is the community of microorganisms associated with cannabis roots, spanning three compartments: bulk soil (surrounding soil), rhizosphere (soil adhering to roots), and endorhiza (microbes colonized inside root tissue). Research by Winston et al. (2014) provides the foundational characterization of this system and reveals how cannabis assembles its microbial partners through a two-tier selection process.

## The Three Compartments

### Bulk Soil
The general soil environment surrounding the root zone. Microbial communities here are shaped almost entirely by edaphic (soil) factors — not by the plant. This is the "reservoir" from which cannabis recruits its root associates.

### Rhizosphere
The thin layer of soil (1-2mm) directly adhering to root surfaces. [[root-exudates]] (sugars, amino acids, organic acids) create a nutrient-rich zone that shifts microbial community composition from bulk soil. However, the rhizosphere is still primarily shaped by soil type rather than plant genotype.

### Endorhiza (Root Interior)
Microbes that have colonized inside root tissue. This is where cultivar-specificity becomes dominant. The plant's immune system selectively allows certain microbes inside, and different cannabis varieties recruit different endorhiza communities. Endorhiza bacteria provide phytohormones, enzymes for regulating growth and metabolism, and help plants tolerate environmental stressors.

## The Two-Tier Selection Model

Winston et al. confirmed a model first proposed by Bulgarelli et al. (2013) for Arabidopsis, now validated for cannabis:

### Tier 1: Soil-Driven Selection
Soil type determines the composition of rhizosphere and root-inhabiting communities. [[cannabinoid-microbiome-correlation-confounded-edaphic-factors]] ranked by influence (most to least):

1. **Nitrogen** — strongest predictor (r-stat: 0.465 weighted, 0.630 unweighted)
2. **Salinity** — high salt reduces microbial diversity (r-stat: 0.437/0.620)
3. **Total organic carbon** — drives microbial biomass (r-stat: 0.330/0.512)
4. **Water content** — shapes [[aact-aerobic-vs-anaerobic-brew-comparison-ingham]] communities (r-stat: 0.281/0.466)
5. **pH** — moderate influence (r-stat: 0.221/0.292)

BEST analysis showed the optimal combination of three factors — Nitrogen, Carbon, and Water — explains community variance with rho = 0.632.

Phosphorus and potassium had surprisingly little influence on microbial community composition, despite their importance for plant nutrition.

### Tier 2: Plant-Driven Selection
Within the endorhiza, cannabis cultivar (genotype) becomes the dominant factor structuring community abundance. Key findings:

- **Strain differences**: 71 significant OTU abundance differences between strains (weighted ANOVA, FDR-corrected)
- **No presence/absence differences**: Zero significant OTU differences by strain in unweighted analysis — cultivar affects *abundance* of microbes, not *which* microbes are present
- **Soil still matters more for composition**: 657 significant OTU differences between soil types vs 71 between strains

## Community Composition Changes (Bulk Soil to Endorhiza)

As microbes transition from bulk soil into the root interior, dramatic taxonomic shifts occur:

### Decreasing
- **Acidobacteria** — most dramatic decrease, especially order iii1-15 (Bonferroni-corrected p = 1.12e-7)
- These are typically oligotrophic soil bacteria adapted to low-nutrient conditions

### Increasing
- **Proteobacteria** — dominant group in endorhiza, especially:
  - Pseudomonadales
  - Burkholderiales
  - Sphingomonadales
  - Rhizobiales
- **Actinobacteria** — especially Actinomycetales
- **Bacteroidetes** — Sphingobacteriales and Flavobacteriales

The shift from Acidobacteria to Proteobacteria/Actinobacteria reflects the transition from nutrient-poor bulk soil to the carbon-rich root interior.

## Core Cannabis Endorhiza Community

A consistent set of microbial taxa found inside cannabis roots across cultivars and growing conditions:

| Taxon | Role |
|-------|------|
| **Pseudomonas** | PGPR, phosphate solubilization, disease suppression, phytohormone production |
| **Cellvibrio** | Aerobic cellulolytic bacterium — degrades cellulose, recycles carbon |
| **Oxalobacteraceae** | Organic acid metabolism, nutrient cycling |
| **Xanthomonadaceae** | Diverse metabolic capabilities |
| **Rhizobiales** | Nitrogen fixation potential |
| **Burkholderiaceae** | [[pseudomonas-endophyte-cannabis-endorhiza-plant-growth-promotion]], biocontrol |
| **Actinomycetales** | Filamentous bacteria, decompose complex organic matter, produce antibiotics |
| **Sphingobacteriales** | Organic matter degradation |
| **Mortierellaceae** | Early successional fungi, plant growth promotion, pathogen suppression |

All prevalent members except Cellvibrio are well-known [[endorhiza-endophytic-bacteria]], primarily within Gammaproteobacteria and Alphaproteobacteria — consistent with observations from other plant systems.

## Cultivar-Specific Differences

### Bookoo Kush
- High abundance of Methylophilus (13% of endorhiza community)
- Methylophilus is a methylotrophic bacterium — consumes methanol, a byproduct of plant cell wall metabolism

### Maui Wowie
- Prevalence of [[sphingomonas-wittichii-cannabis-endorhiza-strain-specificity]]
- This species can metabolize phenazine-1-carboxylic acid and has been implicated in increased survival in soil environments

### Sour Diesel and Burmese
- Methylophilus nearly absent (0.13% in Burmese, 0% in Sour Diesel)
- Demonstrates that cultivar chemistry selects for different microbial partners

## Cannabinoid-Microbiome Connection

Winston et al. found a significant correlation between [[weighted-unifrac-strain-clustering-cannabis-endorhiza-community-structure]] and cannabinoid composition (Mantel test r-stat: 0.863, p = 0.001). However, this correlation is confounded — THC levels were also significantly correlated to soil edaphic variables, making it difficult to disentangle the cannabinoid-microbiome relationship from the soil-cannabinoid relationship. The authors note this requires further research with controlled experiments.

## Alpha Diversity Pattern

Diversity decreases moving from soil into the root:

| Compartment | Chao1 (mean) | Pattern |
|-------------|-------------|---------|
| Bulk soil | ~4,296-5,597 | Highest diversity |
| Rhizosphere | ~3,913-4,859 | Slight reduction |
| Endorhiza | ~3,311-3,325 | Dramatic reduction (~33% less than bulk soil) |

Notably, endorhiza diversity was NOT significantly different between soil types, even though bulk soil diversity differed substantially. This suggests the plant's immune system imposes a diversity ceiling on internal communities regardless of soil richness.

## Root Decay Signal

Samples taken 8 weeks post-harvest (experiment 1) showed dramatically elevated Cellvibrio (16.9% of endorhiza reads vs 0.095% in live plants). This indicates root tissue decomposition rather than true endophytic colonization. The cultivar-specificity signal persisted despite decay, suggesting the community structure is robust.

## Practical Implications for Living Soil Cultivation

### Build Tier 1 Diversity
Since soil type determines the available microbial pool, focus on:
- High organic matter content (carbon)
- Adequate but not excessive nitrogen
- Low salinity
- Proper moisture
- Diverse compost and inoculant sources (see [[indigenous-microorganisms-imo]], [[effective-microorganisms-em]])

### Don't Try to Engineer Tier 2
You cannot force specific endorhiza communities. Different cannabis cultivars will recruit different internal partners from the available soil pool. This means:
- Start seeds/clones in the same living soil they will flower in
- Avoid sterile media for seedling stage (resets microbial recruitment)
- Maintain undisturbed root zones (no-till approach, see [[no-till-gardening-method]])
- The longer soil has been active, the richer the microbial pool for selection
