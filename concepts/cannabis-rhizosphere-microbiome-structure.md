---
title: Cannabis Rhizosphere Microbiome Structure
source: understanding-cultivar-specificity-cannabis-microbiome.md
type: concept
---

# Cannabis Rhizosphere Microbiome Structure

## Overview

The rhizosphere and endorhiza microbiome of *Cannabis sativa* was first comprehensively described by Winston et al. (2014) in a landmark PLOS ONE study. This work established foundational knowledge about how cannabis cultivars shape and are shaped by their associated bacterial communities, introducing a two-tier selection model that has since informed understanding of plant–microbe interactions in this crop. The study profiled bacterial communities across three root-associated compartments—bulk soil, rhizosphere soil, and endorhiza (internal root tissue)—for five distinct cannabis cultivars grown under controlled conditions.

## Experimental Design

The study comprised two complementary experiments designed to disentangle the effects of host genotype (cultivar) and soil environment on microbiome composition.

**Experiment 1:** Three cannabis strains—Burmese, Bookoo Kush, and Sour Diesel—were grown in a single, homogenized soil. This controlled-soil design isolated the effect of host genotype by holding the edaphic environment constant. Any microbiome differences observed among the three cultivars could therefore be attributed to plant-driven selection rather than soil heterogeneity.

**Experiment 2:** Two additional strains—White Widow and Maui Wowie—were each grown in two different soil types. This two-soil design introduced an environmental variable, enabling the researchers to evaluate how soil type and cultivar identity interact in shaping [[edaphic-factors-microbial-community-structure]]. By crossing cultivar with soil type, the experiment provided the statistical power to partition variance attributable to each factor.

Across both experiments, samples were collected from three compartments: bulk soil (distant from root influence), rhizosphere soil (soil tightly adhering to roots), and endorhiza (surface-sterilized root tissue containing internally colonized microbes). This spatial gradient from exterior to interior was critical for characterizing how plant host filtering intensifies along the soil-to-root continuum.

DNA was extracted from all samples and the bacterial 16S rRNA gene V4 region was sequenced using Illumina technology. Bioinformatic processing was performed with the QIIME pipeline, including quality filtering, OTU clustering, and taxonomic assignment.

## Two-Tier Selection Model

A central finding of Winston et al. was strong support for a **two-tier selection model** governing cannabis root-associated microbiome assembly:

1. **Tier 1 — Soil type** determines the overall baseline microbial composition across all sample types. The resident soil microbial pool serves as the source community from which rhizosphere and endorhiza members are drawn. Different soils provide different species pools, and this edaphic influence persists even after plant-driven filtering.

2. **Tier 2 — Host cultivar** acts as a selective filter that is most pronounced in the endorhiza. While soil type sets the available diversity, the plant genotype determines which subset of that pool successfully colonizes root interior tissues. This second tier of selection was statistically significant and cultivar-dependent.

This hierarchical model explains why both soil type and cultivar identity were significant factors in PERMANOVA and related multivariate analyses, but their effects operated at different spatial scales and through different mechanisms.

## Cultivar Specificity

Cultivar-specific differences in [[core-endorhiza-bacterial-community-composition-cannabis]] were a hallmark finding. However, this specificity was **restricted to the endorhiza compartment** and was not observed in the rhizosphere or bulk soil. In other words, while all three compartments differed from one another in overall community structure, only the internal root microbiome carried a signature of host genotype.

This pattern is consistent with the hypothesis that cultivar-specific root exudate profiles, immune responses, or tissue-level biochemical environments selectively recruit or permit colonization by specific bacterial taxa. The rhizosphere, by contrast, reflects a broader and more generalized response to root presence that is less genotype-dependent.

A striking example of cultivar specificity was the [[otu-differential-abundance-cannabis-microbiome]] of *Methylophilus*:

| Cultivar | *Methylophilus* (relative abundance) |
|----------|--------------------------------------|
| Bookoo Kush | ~13% of endorhiza community |
| Burmese | ~0.13% of endorhiza community |
| Sour Diesel | Absent from endorhiza |

This 100-fold difference between Bookoo Kush and Burmese—and complete absence in Sour Diesel—illustrates how strongly host genotype can shape endorhiza community membership, even among plants grown in identical soil.

## Core Endorhiza Community

Despite cultivar-specific differences, a set of bacterial taxa consistently colonized the endorhiza across all five cultivars studied. This **core endorhiza community** represents the taxa most tightly associated with cannabis root interiors:

- **Pseudomonas** — Among the most frequently reported root-associated bacteria; known for plant growth-promoting and biocontrol activities.
- **Cellvibrio** — A genus of cellulolytic bacteria that may contribute to root cell wall modification or carbon cycling at the root–soil interface.
- **Oxalobacteraceae** — A family that includes plant-associated taxa often linked to nitrogen cycling and organic acid metabolism.
- **Xanthomonadaceae** — A diverse family with known plant-associated members; some are phytopathogens while others may be commensal or beneficial.
- **Actinomycetales** — An order of Gram-positive bacteria that includes many species known for producing bioactive compounds and contributing to soil suppressiveness.
- **Sphingobacteriales** — An order commonly recovered from rhizosphere environments and associated with organic matter decomposition.

The consistent presence of these taxa across diverse cultivars and soil conditions suggests they fulfill functional roles that are either specifically selected for by cannabis or are broadly competitive in root endosphere niches.

## Phylum-Level Shifts Along the Soil-to-Root Gradient

Winston et al. documented clear directional shifts in phylum-level composition moving from bulk soil through the rhizosphere to the endorhiza:

- **Acidobacteria decreased** in relative abundance from bulk soil to endorhiza. Acidobacteria are often characterized as oligotrophic taxa adapted to low-nutrient conditions; their decline is consistent with the enriched carbon environment near roots.
- **Proteobacteria increased** along the gradient. Proteobacteria are typically copiotrophic, fast-growing organisms that thrive in carbon-rich zones such as the rhizosphere and root interior.
- **Actinobacteria increased** from soil to endorhiza, consistent with their known roles in root colonization and production of bioactive secondary metabolites that may facilitate endophytic persistence.

These shifts mirror patterns observed in many other plant species, reinforcing the idea that cannabis follows broadly conserved principles of root microbiome assembly while also exhibiting distinctive cultivar-level specificity.

## OTU-Level Differences Between Cultivars

At the OTU level, the bacterial taxa driving community differences between cannabis cultivars belonged predominantly to the phylum **Proteobacteria**, specifically within four orders:

- **Pseudomonadales** — Including *Pseudomonas* and related genera; these organisms are among the most studied plant growth-promoting rhizobacteria.
- **Burkholderiales** — A metabolically versatile order that includes both beneficial and pathogenic plant-associated species.
- **Sphingomonadales** — Known for their ability to degrade complex [[plant-volatile-organic-compounds-and-chemical-ecology]] their prevalence in rhizosphere environments.
- **Rhizobiales** — An order that includes nitrogen-fixing symbionts and diverse root-associated bacteria, though classical legume nodulation is not expected in cannabis.

The concentration of cultivar-differentiating taxa within Proteobacteria underscores the ecological importance of this phylum in the [[cannabis-root-microbiome]] and suggests that functional traits encoded by Proteobacterial genomes (e.g., root colonization factors, hormone production, stress tolerance) may be key determinants of host-specificity.

## Alpha and Beta Diversity Patterns

### Alpha Diversity

Bacterial alpha diversity followed a consistent pattern across the soil-to-root gradient:

**Bulk soil > Rhizosphere > Endorhiza**

The highest diversity was found in bulk soil, which represents the unfiltered reservoir of soil microbial life. Diversity declined progressively through the rhizosphere—where root exudates selectively enrich certain taxa—reaching its lowest point in the endorhiza, where only a subset of rhizosphere-competent organisms gain entry to root tissues and survive host immune surveillance.

This pattern of decreasing alpha diversity from soil to root interior is well-established across many plant species and is consistent with the concept of a nested selection process in which each compartment imposes additional filtering on the available community.

### Beta Diversity

Beta diversity analyses revealed that microbial community composition was significantly influenced by three factors:

1. **Sample type** (bulk soil, rhizosphere, endorhiza) — the strongest source of variation
2. **Soil type** — a significant factor in Experiment 2, affecting communities across all compartments
3. **Plant cultivar** — a significant factor, but primarily in the endorhiza compartment

The interaction between soil type and sample type was also significant, indicating that the magnitude and direction of plant-driven filtering may depend on the starting soil community composition.

## Methodological Notes

- Sequencing platform: Illumina (16S rRNA gene V4 region)
- [[qiime-bioinformatics-pipeline-16s-rrna-microbiome]]: QIIME (quality filtering, OTU clustering, taxonomic assignment)
- Experimental system: Controlled growth conditions with replicated samples across cultivars and soil types
- Statistical approaches: Multivariate community analyses (e.g., PERMANOVA) to partition variance among soil type, cultivar, and compartment factors

## Summary of Key Findings

| Aspect | Finding |
|--------|---------|
| Cultivar specificity | Significant in endorhiza only, not in rhizosphere or bulk soil |
| Soil influence | Determines baseline community composition across all compartments |
| Core endorhiza taxa | Pseudomonas, Cellvibrio, Oxalobacteraceae, Xanthomonadaceae, Actinomycetales, Sphingobacteriales |
| Phylum shifts | Acidobacteria ↓, Proteobacteria ↑, Actinobacteria ↑ from soil to root |
| Alpha diversity | Bulk soil > Rhizosphere > Endorhiza |
| Key differentiating taxa | Proteobacteria (Pseudomonadales, Burkholderiales, Sphingomonadales, Rhizobiales) |

## Significance

Winston et al. (2014) established the foundational framework for understanding cannabis–microbiome interactions by demonstrating that: (1) cannabis hosts a distinct and cultivar-selective endorhiza microbiome; (2) community assembly follows a two-tier selection model with soil and host genotype acting at different spatial scales; and (3) the core endorhiza community is dominated by Proteobacteria and Actinobacteria with plant-associated functional potential. These findings have implications for understanding cannabis health, optimizing cultivation practices, and developing microbiome-informed strategies for this agriculturally important crop.

## Related Concepts

- **[[cannabis-cultivar-specificity]]** — The degree to which different cannabis genotypes harbor distinct microbial communities, particularly in root-associated compartments.
- **Endorhiza microbiome** — The community of microorganisms colonizing the interior of plant roots, subject to the strongest host filtering effects.
- **Two-tier selection model** — A hierarchical framework in which soil determines the available microbial species pool while host genotype filters which taxa colonize internal root tissues.
- **Rhizosphere effect** — The general enrichment and compositional shift of microbial communities in soil adjacent to plant roots relative to bulk soil, driven by root exudates.

## See Also
- [[nitrogen-strongest-edaphic-factor-cannabis-microbiome-structuring]]
