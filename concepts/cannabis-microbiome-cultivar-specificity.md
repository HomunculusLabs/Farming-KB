---
title: Cannabis Microbiome Cultivar Specificity
source: understanding-cultivar-specificity-cannabis-microbiome.md
type: concept
---

# Cannabis Microbiome Cultivar Specificity

**Source:** Winston et al. 2014, *PLoS ONE* 9(6):e99641

## Overview

Cannabis presents a compelling model for studying plant–microbiome interactions due to its rich profile of secondary metabolic compounds. Despite the crop's economic importance, remarkably little was known about its soil-based microbial associations prior to this study. Winston et al. (2014) provided the first comprehensive description of the endorhiza-, rhizosphere-, and bulk soil-associated bacterial microbiomes across five distinct Cannabis cultivars, demonstrating that bacterial communities within the endorhiza (root interior) exhibit significant cultivar-specificity.

## Background: The Role of Soil Microbes in Plant Health

Soil microbes underpin several critical plant-supporting processes:

- **Nitrogen fixation** — converting atmospheric N₂ into bioavailable forms
- **Growth stimulation** — producing phytohormones and low-molecular-weight compounds
- **Improved water retention** — enhancing soil aggregate structure
- **Root disease suppression** — via competitive exclusion and antimicrobial compounds

These functions occur predominantly in the rhizosphere and rhizoplane, where microbial activity is further modulated by fungal saprotrophs and [[mycorrhizal-fungi]]. Microbial community composition is known to depend on soil type, root zone location, and plant species, with rhizosphere communities being highly dynamic — fluctuating in response to temperature, moisture, pH, CO₂, and O₂ levels.

## The Two-Tier Selection Model

The study proposed a **two-tier selection model** to explain how root-associated bacterial communities are assembled in Cannabis:

1. **First shift (soil-driven):** Soil physicochemical properties — including pH, salinity, organic carbon, and nitrogen content — define the composition of the rhizosphere and root-inhabiting bacterial pool. This is the broader, edaphic filter that determines which taxa are available to colonize the root environment.

2. **Second shift (genotype-driven):** Migration of bacteria from the rhizosphere into plant root tissues is governed by plant genotype-dependent selection. The host plant actively shapes its endorhiza community through the production of [[root-exudates]], secondary metabolites, and immune signaling molecules. This tier predicts a dramatic reduction in certain taxa — most notably Acidobacteria — within the endosphere.

This model reconciles the competing influences of edaphic factors and host genetics, positioning them as sequential rather than mutually exclusive filters.

## Experimental Design

### Experiment 1 — Minimally Variable Soil

- **Cultivars:** Burmese (balanced hybrid), Bookoo Kush (sativa-dominant hybrid), [[sour-diesel]] (C. sativa)
- **Location:** Vista, California (November 2011)
- **Design:** 9 plants total (3 per cultivar), 27 samples collected as triplicate endorhiza / rhizosphere / bulk soil per plant
- **Soil conditions:** Sandy loam, minimally variable edaphic parameters (pH 6.63–6.94, salinity 1.73–7.44, total N 0.26–1.51%, total organic C 3.02–20.0%, water content 0.101–0.371)
- **Sequencing:** Illumina 16S rRNA V4 region, analyzed with QIIME 1.7.0

### Experiment 2 — Contrasting Soil Types

- **Cultivars:** White Widow (balanced hybrid), Maui Wowie (C. sativa)
- **Locations:** Vista and Orange County, California (August 2012)
- **Design:** 42 samples with triplicate pseudoreplicates from different roots; included cannabinoid profiling from buds
- **Purpose:** To test whether cultivar-specificity persists under significant edaphic variation

## Cultivar-Specific Endorhiza Communities

### Statistical Evidence for Specificity

In Experiment 1, cultivar-dependent differences were **observed exclusively in the endorhiza**, with no significant strain-level differences detected in the rhizosphere or bulk soil:

- Weighted UniFrac PERMANOVA (ADONIS): R² = 0.59, p = 0.004
- Unweighted UniFrac PERMANOVA (ADONIS): R² = 0.39, p = 0.003

The genus *Methylophilus* was a key taxon driving cultivar differentiation — comprising 13% of the endorhiza community in Bookoo Kush but only 0.13% in Burmese and was entirely absent from Sour Diesel. This stark disparity highlights how closely bacterial enrichment within root tissue tracks with host genotype.

Community composition across all sample types was determined predominantly by soil properties; however, within the endorhiza specifically, differences in community structure were driven by cultivar identity.

### Core Endorhiza Community

Despite inter-cultivar variation, a consistent core bacterial community was identified across all five cultivars in the endorhiza:

- *Pseudomonas*
- *Cellvibrio*
- Oxalobacteraceae
- Xanthomonadaceae
- Actinomycetales
- Sphingobacteriales

These taxa represent recurring root colonizers that may play shared functional roles in plant growth promotion and disease suppression across Cannabis genotypes.

## Phylum-Level Shifts from Soil to Root

Transitioning from bulk soil and rhizosphere into the endorhiza was accompanied by pronounced phylum-level compositional changes:

| Phylum | Direction in Endorhiza |
|---|---|
| Acidobacteria | Decreased dramatically |
| Proteobacteria | Increased |
| Actinobacteria | Increased |

The most significant single OTU shift was the depletion of Acidobacteria order iii1-15 in the endorhiza (Bonferroni-corrected p = 1.12 × 10⁻⁷). Of the 51 sample-type-differentiating OTUs identified, 17 that increased in the endorhiza were predominantly Proteobacteria — including members of the Rhizobiales, an order associated with nitrogen fixation and plant-beneficial functions.

### Correlation of OTU Abundance Across Compartments

Pearson correlation coefficients for OTU abundance between sample types revealed the progressive filtering effect of each compartment:

- Bulk soil vs. rhizosphere: ρ = 0.92 (very similar)
- Rhizosphere vs. endorhiza: ρ = 0.63 (moderate similarity)
- Bulk soil vs. endorhiza: ρ = 0.42 (substantial divergence)

The declining correlation from soil → rhizosphere → endorhiza quantitatively supports the two-tier selection model: the first soil-driven filter modestly reshapes the community, while the genotype-dependent second filter exerts a much stronger selective pressure.

## Significance for Cannabis Agriculture

The discovery of cultivar-specific endorhiza communities has several practical implications:

1. **Tailored inoculants:** Microbial biofertilizers and biocontrol agents could be matched to specific Cannabis cultivars to maximize efficacy, rather than applying generic products across all strains.

2. **Breeding for microbiome compatibility:** Cultivar selection could incorporate microbiome profiling as an additional trait, favoring genotypes that recruit beneficial endorhiza communities.

3. **Terroir and product quality:** Endophytes and epiphytes may contribute to localized "flavor" or terroir effects in Cannabis — analogous to the well-documented microbial contributions to wine characteristics — suggesting that microbial management could influence cannabinoid and terpene profiles.

4. **Sustainable production:** Leveraging naturally occurring plant-microbe partnerships could reduce dependence on synthetic fertilizers and pesticides, supporting more sustainable cultivation practices.

5. **Disease resilience:** Understanding which endorhiza taxa are cultivar-enriched enables targeted strategies to bolster plant defenses against soil-borne pathogens through microbiome engineering.

## Key Limitations and Future Directions

The study was limited to bacterial communities (16S rRNA); fungal and archaeal contributions to cultivar-specificity remain unexplored. Additionally, functional characterization of the identified taxa — particularly their roles in secondary metabolism and cannabinoid biosynthesis — would further clarify the practical value of these microbial partnerships for Cannabis agriculture.

## See Also

- [[cannabis-microbiome]] general concepts
- Rhizosphere ecology
- Plant endophyte biology
- Two-tier selection model in plant microbiomes
