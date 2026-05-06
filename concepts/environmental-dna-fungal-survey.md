---
title: Environmental DNA Fungal Survey
created: 2026-04-28
tags: [mycology, metabarcoding, genomics, biodiversity, methodology]
date: 2026-04-28
updated: 2026-04-28
sources: [/Users/t3rpz/wiki/raw/papers/unknown-biodiversity-of-fungi.md]
type: concept
---

# Environmental DNA Fungal Survey

## Overview

Environmental DNA (eDNA) metabarcoding has transformed fungal biodiversity
assessment by enabling detection of species that never produce visible
fruiting structures or that are too rare to find through conventional
collecting. This approach extracts DNA directly from environmental samples
such as soil, water, air, leaf litter, and plant tissue, then amplifies and
sequences marker regions to identify the fungi present.

## The ITS Marker Region

The internal transcribed spacer (ITS) region between ribosomal RNA genes is
the universally accepted DNA barcode for fungi. ITS1 and ITS2 sub-regions
offer the best balance of amplification reliability and taxonomic resolution
across the fungal kingdom. The UNITE database provides curated reference
sequences for ITS-based identification, though coverage remains incomplete,
especially for tropical and asexual taxa.

## Sample Collection Methods

### Soil Core Sampling

Soil is the most commonly surveyed substrate for fungal eDNA. Standard
protocols involve collecting soil cores to a depth of 5 to 10 centimeters,
preserving in CTAB buffer or freezing immediately. Spatial pooling strategies
and composite sampling help capture landscape-scale diversity while managing
sequencing costs.

### Air Spore Monitoring

Airborne fungal DNA provides a window into the spore-producing community and
is increasingly used for allergen monitoring and plant pathogen surveillance.
High-volume air samplers equipped with filters capture spores over hours to
days, revealing temporal patterns in fungal dispersal.

### Leaf and Root Tissue

Surface-sterilized leaf and root tissues allow targeted surveys of endophytic
and mycorrhizal fungi. Root-tip sorting under a microscope enables selective
analysis of mycorrhizal colonization types, separating arbuscular from
ectomycorrhizal communities.

### Water and Sediment

Aquatic fungal communities are surveyed by filtering water samples or
extracting DNA from sediment. Freshwater habitats harbor significant
undescribed fungal diversity, particularly among Chytridiomycota and early-
diverging fungal lineages that are rarely encountered above ground.

## Laboratory Workflow

The typical metabarcoding pipeline involves DNA extraction from the
environmental matrix, PCR amplification of the ITS region using fungal-specific
primers (such as ITS1F/ITS2), addition of sample-specific barcodes and
sequencing adapters, high-throughput sequencing on Illumina platforms, and
bioinformatic processing to cluster sequences into OTUs or amplicon sequence
variants (ASVs). The shift from OTUs to ASVs has improved reproducibility and
resolution.

## Bioinformatic Challenges

### Reference Database Gaps

A major limitation is that many environmental sequences cannot be confidently
assigned to described species because reference databases cover only a fraction
of known fungal diversity. Tropical taxa, asexual fungi, and early-diverging
lineages are particularly underrepresented in curated databases like UNITE and
GenBank.

### Primer Bias

No single primer pair amplifies all fungal groups equally. Some commonly used
primer combinations preferentially amplify certain lineages while missing
others. Basal fungal lineages, such as Rozellomycota and Chytridiomycota, are
often underrepresented in ITS-based surveys. Multiplexed primer approaches
partially address this bias.

### Contamination and False Positives

Laboratory contamination from reagents, equipment, and previous samples is a
persistent concern in eDNA work. Negative controls, blank extractions, and
mock community standards are essential for distinguishing genuine environmental
signals from contaminants. Sequencing depth thresholds and rarity filters help
but can also discard authentic rare detections.

## Ecological Insights from eDNA

Metabarcoding has revealed that fungal communities are far more diverse than
fruiting-body surveys suggest, with many species detected only as DNA. Seasonal
patterns in community composition are now trackable across entire years,
revealing previously invisible phenological dynamics. Spatial patterns show
strong habitat partitioning at very fine scales, with distinct communities in
soil horizons separated by centimeters.

## Limitations

eDNA detects presence but not abundance in a straightforward way, because
spore counts and mycelial biomass contribute differently to DNA signal. The
approach cannot distinguish active from dormant organisms or living biomass
from dead material. Linking environmental sequences to described species
remains the central bottleneck, as most sequences are "dark taxa" without
reference matches.

## Emerging Applications

Beyond biodiversity surveys, fungal eDNA is increasingly applied to practical questions in agriculture and environmental monitoring. Soil health assessments use fungal community composition as a bioindicator, tracking shifts toward saprotrophic or pathogenic dominance that signal soil degradation. Plant pathogen surveillance networks deploy air and soil eDNA sampling to detect crop-threatening fungi such as *Puccinia graminis* (wheat stem rust) and *Fusarium* species before visible symptoms appear. In restoration ecology, eDNA monitoring tracks the recovery of mycorrhizal communities after disturbance, providing a metric of below-ground ecosystem recovery that is invisible to surface surveys.

Metabarcoding data is also being integrated with functional gene profiling (metagenomics and metatranscriptomics) to move beyond species lists toward understanding what fungal communities are actually doing — which enzymes they express, what nutrients they cycle, and how they respond to environmental change. This functional approach bridges the gap between [[fungal-enzyme-activity-nutrient-availability]] measurements and community-level ecology.

## See Also

- environmental dna fungal survey

- [[fungal-species-estimates]]
- [[biodiversity-fungi-tropical-fungal-diversity]]
- [[cryptic-fungal-species]]
- [[fungal-taxonomic-impediment]]
