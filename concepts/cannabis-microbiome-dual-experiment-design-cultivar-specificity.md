---
title: Cannabis Microbiome Dual Experiment Design Cultivar Specificity
source: understanding-cultivar-specificity-cannabis-microbiome.md
type: concept
---

# Cannabis Microbiome Dual-Experiment Design for Cultivar Specificity

## Overview

Winston et al. (2014) employed a two-experiment research design to investigate the relative contributions of plant cultivar (genotype) and soil type ([[cannabinoid-microbiome-correlation-confounded-edaphic-factors]]) to the structure of Cannabis-associated microbial communities. This dual-experiment approach allowed the researchers to disentangle cultivar-specific effects from soil-driven effects across three sample compartments: endorhiza (root interior), rhizosphere, and bulk soil.

## Experimental Rationale

The study was motivated by the observation that microbial composition in soil depends on complex interactions between soil type, root zone location, and plant species. The two-tier selection model predicts that soil type determines the broad composition of rhizosphere and root-inhabiting communities, while plant genotype fine-tunes the endorhiza community through selective recruitment.

Testing this model requires experimental designs that can separate soil effects from cultivar effects. A single experiment with limited soil variation would be unable to distinguish between these two drivers. The dual-experiment design addressed this limitation.

## Experiment 1: Minimal Edaphic Variation

The first experiment focused on identifying variation in microbial communities between three Cannabis cultivars grown in similar soil conditions:

- **Cultivars:** [[sour-diesel]] (*C. sativa*, high THC:CBD ratio), Bookoo Kush (sativa-dominant hybrid, moderately high THC:CBD), and Burmese (balanced hybrid, moderate THC:CBD)
- **Location:** Vista, California (November 2011)
- **Soil:** Locally composted soil with minimal edaphic variation between plant sites
- **Samples:** 9 plants (3 per cultivar), triplicate endorhiza, rhizosphere, and bulk soil samples = 27 total
- **Soil characteristics:** [[sandy-loam-texture-cannabis-microbiome-assembly]], pH 6.63-6.94, salinity 5.12-7.44, total N 0.26-1.51%, total organic C 3.02-5.00%

The minimal edaphic variation in this experiment was intentional — by keeping soil conditions nearly constant, any observed microbial community differences could be more confidently attributed to cultivar effects. However, this design also meant that soil-type effects could not be robustly tested within this experiment alone.

## Experiment 2: Significant Edaphic Variation

The second experiment was designed specifically to understand the nature and strength of cultivar-specificity under conditions of greater soil variation:

- **Cultivars:** White Widow (balanced hybrid) and [[maui-wowie]] (*C. sativa*, high THC:CBD)
- **Locations:** Vista and Orange County, California (August 2012)
- **Soils:** Two distinct soil types with significant physicochemical differences (MB and OC soils)
- **Design:** 4 plants of each strain grown in same soil, plus 2 White Widow plants in a completely distinct soil type
- **Samples:** Triplicate endorhiza, rhizosphere, and bulk soil per plant = 42 total
- **Timing:** Samples taken 2 weeks prior to harvest (vs. 8 weeks post-harvest in Experiment 1)
- **Soil differences:** MB soil had higher salinity (5.12 vs 1.73), lower organic carbon (3.02 vs 20.0%), and lower water content (0.113 vs 0.371)

The key innovation was growing White Widow in two different soil types, which allowed direct comparison of the same cultivar's microbiome across edaphic gradients while controlling for genotype.

## Molecular Methods

Both experiments used identical [[genetic-improvement-agaricus-bisporus-molecular-approaches]]:

- **Sequencing:** Illumina MiSeq of the V4 region of the 16S rRNA gene (291 bp amplicon)
- **Primers:** 515F forward and 806R Golay-barcoded reverse (Earth Microbiome Project standard)
- **PCR:** 35 cycles, triplicate reactions pooled per sample
- **Bioinformatics:** QIIME 1.7.0, Greengenes database at 97% identity (open reference OTU picking)
- **Analysis:** Alpha and beta diversity (weighted and [[weighted-unweighted-unifrac-discrepancy-cannabis-cultivar]]), ADONIS, ANOSIM, ANOVA, RDA, BEST analysis
- **Rarefaction:** 3,000 sequences (Experiment 1), 45,000 sequences (Experiment 2)
- **DNA extraction:** PowerSoil DNA Isolation Kit with 65°C 10-minute pre-heating modification

## Cultivar Descriptions

The five cultivars used across both experiments represent a range of [[cannabis-chemotypes]] and genetic backgrounds:

- **Sour Diesel:** Pure *C. sativa*, high THC:CBD ratio, energizing effects
- **Bookoo Kush:** Sativa-dominant hybrid of *C. sativa* × *C. indica*, moderately high THC:CBD
- **Burmese:** Balanced hybrid of *C. sativa* × *C. indica*, moderate THC:CBD
- **Maui Wowie:** Pure *C. sativa*, high THC:CBD ratio, tropical Hawaiian landrace
- **White Widow:** Balanced hybrid, known for moderate THC:CBD ratio and widespread cultivation

## Sample Collection Protocol

The [[biodiversity-sampling-protocol-design]] was designed to capture three distinct microbial compartments:

1. **Bulk soil:** 50 g sample taken 10 cm from the stem at 20 cm depth, representing the background soil community
2. **Rhizosphere soil:** Soil remaining adhered to roots after removal from ground, shaken into whirlpak bags
3. **Endorhiza:** Root tissue samples from the root ball, surface-sterilized with alcohol and sterile water

All samples were immediately transferred to 4°C storage for transport (~4 hours to laboratory). Root samples were rinsed with alcohol and sterile water before DNA extraction. The protocol ensured clean separation between compartments while minimizing cross-contamination.

## Key Findings from the Dual Design

The two-experiment approach yielded several findings that would have been difficult to establish with a single study:

- **Soil type is the dominant driver** of community composition across all sample types (ADONIS R² = 0.196-0.323)
- **Cultivar specificity is significant but weaker** than soil effects, primarily detectable in endorhiza communities
- **Sample type (endorhiza vs rhizosphere vs bulk soil)** creates distinct community structures
- **Pooling both experiments** strengthened statistical power, with all three factors (soil, sample type, strain) highly significant

The combination of minimal-edaphic-variation (Experiment 1) and significant-edaphic-variation (Experiment 2) designs provided complementary evidence supporting the two-tier selection model.

## Limitations of the Design

Several methodological constraints affected the study:

- Pseudoreplication: triplicate samples from Experiment 2 were taken from different roots on the same plant
- Timing difference: Experiment 1 sampled 8 weeks post-harvest, Experiment 2 at 2 weeks pre-harvest
- Limited soil replication: Only two soil types in Experiment 2
- Single growing season: No temporal replication across years
- THC-soil confound: Higher THC in one soil type made it difficult to disassociate cannabinoid effects from soil physicochemical effects

## References

- Winston, M.E., et al. (2014). Understanding cultivar-specificity and soil determinants of the [[cannabis-microbiome]]. PLoS ONE, 9(6), e99641.
- Caporaso, J.G., et al. (2012). Ultra-high-throughput microbial community analysis on the Illumina HiSeq and MiSeq platforms. ISME J., 6, 1621-1624.
