---
title: Cannabis Microbiome Experimental Design
created: 2026-04-28
tags: [microbiome, methods, cannabis, experimental-design]
date: 2026-04-28
updated: 2026-04-28
sources:
  - /Users/t3rpz/wiki/raw/papers/understanding-cultivar-specificity-cannabis-microbiome.md
type: concept
---

# Cannabis Microbiome Experimental Design

## Overview

Winston et al. (2014) employed a two-experiment design to characterize the
bacterial microbiome of Cannabis across the root-soil continuum. The first
experiment explored broad variation across three cultivars in a single soil
type, while the second focused on cultivar-specificity with greater edaphic
variation using two cultivars across two soil types. This design provided
both breadth (five total cultivars) and depth (controlled soil comparisons),
though different sampling timings introduced an important confound.

## Experiment 1: Post-Harvest Sampling

### Objective

Identify variation in microbial communities between roots and soil across
three Cannabis cultivars grown in the same soil environment.

### Cultivars

Three cultivars representing different chemotypes and genetic backgrounds:

- **Sour Diesel**: Cannabis sativa, high THC to CBD ratio
- **Bookoo Kush**: Sativa-dominant hybrid (sativa x indica), moderately
  high THC to CBD ratio
- **Burmese**: Balanced hybrid (sativa x indica), moderate THC to CBD
  ratio

### Growing Conditions and Sampling

Nine organically-grown plants (three per cultivar) in locally composted
soil in Vista, California. Samples were collected in November 2011, eight
weeks after harvesting flowering bud and foliage. For each plant:

1. **Bulk soil**: 50 g sample at 10 cm from stem, 20 cm depth
2. **Rhizosphere soil**: Adhered soil shaken into a whirlpak bag
3. **Endorhiza**: Root ball samples rinsed with alcohol and sterile water

A larger bulk soil sample was collected for edaphic testing (pH, salinity,
N, C, water content). All samples stored at 4 degrees C for approximately
4 hours during shipping. Triplicate extracts yielded single representative
samples per compartment per plant. Total: 27 samples.

### Key Limitation

Post-harvest timing introduced root decay effects, particularly
proliferation of cellulolytic Cellvibrio (see
[[cellvibrio-and-root-decay-microbiome]]), confounding the true endorhiza
community with early successional decay communities.

## Experiment 2: Pre-Harvest Sampling

### Objective

Understand the nature and strength of cultivar-specificity with greater
edaphic variation, using a controlled cross-soil design.

### Cultivars and Growing Conditions

- **White Widow**: Balanced hybrid (sativa x indica), moderate THC to CBD
- **Maui Wowie**: Cannabis sativa, high THC to CBD ratio

Four plants (two per cultivar) grown in Mo-Bio soil (Vista, CA); two
White Widow plants grown in Orange County soil. This created significant
edaphic variation (see [[soil-edaphic-factors-microbial-communities]]).

### Sampling Protocol

Collected in August 2012, two weeks prior to harvest. For each of six
plants: triplicate endorhiza samples from different roots (pseudoreplicates),
triplicate rhizosphere samples, and triplicate bulk soil samples. Total: 42
samples (18 endorhiza, 18 rhizosphere, 6 bulk soil). One discarded for
insufficient coverage, leaving 41.

### Cannabinoid Testing

Cannabinoid data collected from buds of three White Widow and one Maui
Wowie plant, including delta-9-tetrahydrocannabinol, processed at
Delta-9-Technologies, LLC (Santa Ana, CA).

## Critical Differences Between Experiments

| Aspect           | Experiment 1         | Experiment 2           |
|-----------------|----------------------|------------------------|
| Cultivars       | 3 (SD, BK, B)       | 2 (WW, MW)             |
| Soil types      | 1 (shared)           | 2 (MB, OC)             |
| Sampling timing | 8 weeks post-harvest | 2 weeks pre-harvest    |
| Total samples   | 27                   | 42                     |
| Rarefaction     | 3,000 sequences      | 45,000 sequences       |
| Cannabinoid data| No                   | Yes                    |
| Pseudoreplicates| No                   | Yes (different roots)  |

The rarefaction depth difference means alpha diversity cannot be directly
compared between experiments. Different sampling timings confound
experiment with plant growth stage.

## DNA Extraction

DNA was isolated from 0.25 g of soil or root using the PowerSoil DNA
Isolation Kit (MO BIO, USA) with a key modification: heating at 65
degrees C for 10 minutes prior to the initial vortex step, improving
lysis of tough Gram-positive endophytes. Root samples were surface-
sterilized with alcohol and sterile water to isolate true endorhiza
bacteria. See [[16s-rrna-sequencing-microbiome-analysis]] for complete
sequencing and bioinformatics details.

## Design Implications

The complementary design addressed different questions: experiment 1
tested whether any cultivar variation exists, while experiment 2 measured
cultivar-specificity strength with controlled soil comparisons. The
post-harvest timing of experiment 1 proved useful for studying root decay,
though not originally intended. Future studies would benefit from unified
design with consistent sampling across all cultivars and soil types.

## See Also

- [[cannabinoid-microbiome-correlation-cannabis]]

- [[16s-rrna-sequencing-microbiome-analysis]] for sequencing methodology
- [[cannabis-cultivar-microbiome-specificity]] for results overview
- [[cellvibrio-and-root-decay-microbiome]] for post-harvest effects
- [[soil-edaphic-factors-microbial-communities]] for soil differences
- [[cannabis-microbiome-research]] for the complete study overview
