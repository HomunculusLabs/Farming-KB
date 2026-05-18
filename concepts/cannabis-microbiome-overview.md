---
title: Cannabis Microbiome Overview
source: understanding-cultivar-specificity-cannabis-microbiome.md
type: concept
---

# Cannabis Microbiome Overview

## Introduction

Winston et al. (2014) published the first comprehensive description of the microbial communities associated with Cannabis roots and surrounding soil across five distinct cultivars. This landmark study in *PLoS ONE* established foundational knowledge about how Cannabis cultivar genotype shapes its root-associated microbiome and introduced a two-tier selection model for understanding plant–microbe interactions in this previously understudied crop.

The study examined three distinct microbial habitats — the **endorhiza** (internal root tissue), the **rhizosphere** (soil tightly adhering to roots), and **bulk soil** (soil distant from roots) — to understand how microbial communities change as proximity to the plant root increases and how those changes are influenced by host genotype.

## Study Design

The research was structured as two complementary experiments, each designed to isolate different variables driving microbiome composition.

### Experiment 1: Controlling for Soil Type

- **Objective:** Isolate the effect of cultivar genotype by minimizing edaphic (soil) variation.
- **Cultivars:** Burmese, BooKoo Kush, and Sour Diesel.
- **Location:** Vista, CA (single soil type).
- **Sample count:** 27 total samples.
- **Rationale:** By growing all three strains in the same soil, any differences in microbial communities could be more confidently attributed to the plant genotype rather than environmental variability.

### Experiment 2: Introducing Soil Variation

- **Objective:** Examine how different soil types interact with cultivar genotype to shape microbiomes.
- **Cultivars:** White Widow and Maui Wowie.
- **Locations:** Vista, CA and Orange County, CA (two distinct soil types).
- **Sample count:** 42 total samples.
- **Rationale:** This experiment tested whether the genotype effects observed in Experiment 1 persist across different edaphic conditions, and how soil type versus plant genotype contribute to community structure.

## Cultivar Descriptions

Each cultivar represented a different chemotype and genetic background within *Cannabis*:

| Cultivar | Type | THC:CBD Profile |
|----------|------|-----------------|
| Sour Diesel | *C. sativa* | High THC:CBD ratio |
| BooKoo Kush | Sativa-dominant hybrid | Moderately high THC:CBD |
| Burmese | Balanced hybrid | Moderate THC:CBD |
| Maui Wowie | *C. sativa* | High THC:CBD ratio |
| White Widow | Balanced hybrid | Moderate THC:CBD |

The diversity of chemotypes allowed the researchers to explore whether cannabinoid profile or overall genetic background influenced microbial community assembly.

## Sampling Strategy

Three sample types were collected from each plant to capture the full soil-to-root microbial gradient:

1. **Endorhiza:** Root tissue samples, representing the internal root microbiome. These are organisms that have colonized the root interior, potentially forming intimate symbiotic or pathogenic relationships with the plant.

2. **Rhizosphere:** Soil particles that remain adhered to the root surface after gentle shaking. This zone is directly influenced by root exudates and represents the interface where plants actively recruit and shape microbial communities.

3. **Bulk Soil:** Soil collected 10 cm from the stem at a depth of 20 cm. This serves as a baseline reference for the native [[edaphic-factors-soil-microbial-community-structure]], minimally influenced by the plant.

This three-compartment approach is standard in plant microbiome studies and enables researchers to track how microbial diversity and composition shift across the root-soil interface.

## Laboratory Methods

### DNA Extraction and Sequencing

DNA was isolated using the **MoBio PowerSoil DNA Isolation Kit** with a **65°C heating modification** to lyse tough cell walls (particularly Gram-positive bacteria), improving yield from recalcitrant taxa. Sequencing targeted the **16S rRNA gene V4 region** using Illumina technology with **515F/806R primers**, providing broad taxonomic coverage with genus-level resolution.

### Bioinformatic Pipeline

- **QIIME 1.7.0** for sequence processing and analysis.
- **Greengenes 97%** reference database for OTU clustering and taxonomic assignment.
- **UniFrac distances:** Both unweighted (community membership) and weighted (abundance-weighted).
- **Ordination:** PCoA for visualization, RDA for constrained ordination.
- **Statistical testing:** BEST analysis and ADONIS (PERMANOVA) for group comparisons.

## Key Results from Experiment 1

### Sample Type Effects

- The **endorhiza** and **bulk soil** communities were significantly distinct from all other sample types (ADONIS p = 0.001), confirming that plant roots exert a strong filtering effect on the soil microbiome.
- Surprisingly, the **rhizosphere** was NOT significantly different from other sample types by itself (ADONIS p = 0.07 unweighted, p = 0.10 weighted). This may reflect the transitional nature of the rhizosphere — it occupies a gradient between bulk soil and root interior, making it harder to distinguish statistically when sample sizes are limited.

### Cultivar Effects Are Endorhiza-Specific

- Strain-level differences in microbial communities were **only significant within the endorhiza** ([[cannabis-weighted-unifrac-strain-abundance-vs-presence-absence]] R² = 0.59, p = 0.004). This is a remarkably high R² value, indicating that nearly 60% of the variation in [[weighted-unifrac-strain-clustering-cannabis-endorhiza-community-structure]] was explained by cultivar identity alone.
- No significant cultivar effects were observed in the rhizosphere or bulk soil, underscoring that the plant's genotype-dependent selection operates primarily at the root interior.

### Methylophilus as a Discriminant Taxon

The genus *Methylophilus* (a methylotrophic bacterium capable of metabolizing single-carbon compounds) showed dramatic cultivar-specific enrichment:

- **BooKoo Kush:** 13% relative abundance
- **Burmese:** 0.13% relative abundance (100-fold lower)
- **Sour Diesel:** Completely absent

This striking [[otu-differential-abundance-cannabis-microbiome]] pattern made *Methylophilus* a key contributor to the observed strain-level differences and raised interesting questions about whether root exudate chemistry varies systematically among cultivars.

### Core Endorhiza Community

Despite cultivar-specific differences, a set of taxa were consistently found across all endorhiza samples, forming the "core" [[cannabis-root-microbiome]]:

- **Pseudomonas** — a ubiquitous genus including plant growth-promoting rhizobacteria (PGPR) and some opportunistic pathogens.
- **Cellvibrio** — cellulolytic bacteria that may assist in organic matter decomposition around roots.
- **Oxalobacteraceae** — a family commonly associated with the rhizosphere of diverse plant species.
- **Xanthomonadaceae** — a family with both plant-associated and free-living members.
- **Actinomycetales** — an order of high-GC Gram-positive bacteria known for producing bioactive [[antifungal-secondary-metabolites-coprophilous-fungi]].
- **Sphingobacteriales** — an order of environmental bacteria found in soil and root environments.

## The Two-Tier Selection Model

Perhaps the most significant conceptual contribution of this study is the evidence supporting a **two-tier selection model** for Cannabis root microbiome assembly:

```
Tier 1 (Edaphic Selection):
  Soil type and environmental conditions determine the pool of
  available microorganisms in bulk soil and rhizosphere.

Tier 2 (Genotype-Dependent Selection):
  The plant host's genotype selectively filters and enriches
  specific taxa from the available pool during endorhiza colonization.
```

This model predicts that while the starting microbial pool is set by abiotic soil factors, the final composition of the root interior is primarily shaped by the plant's genetics. The study's results are consistent with this framework: bulk soil communities were shaped mainly by soil type, while endorhiza communities were shaped mainly by cultivar identity.

## Significance and Broader Implications

This study established several foundational principles for Cannabis microbiome science:

1. **Cultivar specificity is real:** Different Cannabis strains harbor distinct endorhiza microbiomes, confirming that breeding and selection for specific chemotypes may inadvertently or deliberately shape the plant's microbial partners.

2. **The endorhiza is the key compartment:** Genotype effects are strongest inside the root, where plant immune responses, exudate chemistry, and tissue architecture create a highly selective environment.

3. **Soil matters, but genotype matters more at the root level:** While edaphic factors determine what organisms are available, the plant ultimately selects its root microbial partners.

4. **Potential for microbiome-informed cultivation:** Understanding cultivar-specific microbiome associations could eventually lead to targeted inoculant development for specific Cannabis strains, improving plant health, yield, or cannabinoid production.

5. **Foundation for future research:** This study provided the methodological and conceptual baseline that subsequent Cannabis microbiome investigations have built upon, including work on fungal communities, temporal dynamics, and the functional roles of specific root-associated taxa.

## Limitations and Considerations

- The study focused exclusively on bacterial communities via 16S rRNA gene sequencing; fungal and archaeal components of the Cannabis microbiome were not characterized.
- Sample sizes were modest (27 and 42 samples), which may have limited statistical power for detecting subtle effects, particularly in the rhizosphere.
- The cultivation environment was outdoor field soil; controlled environment studies would be needed to further isolate genetic from environmental effects.
- Functional characterization of the microbiome (metagenomics, metatranscriptomics) was not included, leaving open questions about what these microbial communities actually *do* for the plant.

## See Also

- [[cannabis-microbiome-cultivar-specificity]] — Detailed results and Experiment 2 findings
- endorhiza vs rhizosphere — Comparison of root-associated microbial compartments
- [[two-tier-selection-model]] — Theoretical framework for [[two-tier-selection-model-plant-microbiome-assembly]]
- methylophilus cannabis — Role of methylotrophic bacteria in Cannabis roots
