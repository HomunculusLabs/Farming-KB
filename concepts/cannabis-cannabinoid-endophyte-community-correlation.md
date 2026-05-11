---
title: Cannabis Cannabinoid-Endophyte Community Correlation
source: Winston et al. 2014
tags:
  - cannabis
  - microbiome
  - cannabinoid
  - THC
  - CBD
  - endorhiza
  - terroir
  - mantel-test
---

# Cannabis Cannabinoid-Endophyte Community Correlation

## Overview

Winston et al. (2014) investigated whether cannabinoid concentrations,
particularly THC (delta-9-tetrahydrocannabinol) and CBD (cannabidiol), were
correlated with endorhiza bacterial community structure across five Cannabis
cultivars. The study found statistically significant correlations between
cannabinoid profiles and endorhiza community composition using Mantel tests,
but also revealed that these correlations were substantially confounded by
underlying soil edaphic variables. Disassociating the direct effects of
cannabinoid production on endophyte recruitment from the indirect effects of
soil chemistry proved to be the central analytical challenge of this
investigation.

## Cannabinoid Profiles Across Cultivars

The five Cannabis cultivars examined (Burmese, Bookoo Kush, Sour Diesel, White
Widow, Maui Wowie) exhibited varying THC and CBD concentrations consistent
with their chemotype classifications. High-THC cultivars such as Sour Diesel
and White Widow showed elevated THC-to-CBD ratios, while other cultivars
displayed more balanced cannabinoid profiles. These chemical differences among
cultivars provided the natural variation necessary to test for
cannabinoid-microbiome associations. Importantly, cannabinoid concentration is
a genetically determined trait, meaning that cultivar identity and cannabinoid
profile are intrinsically linked.

## Mantel Test Results

Mantel tests comparing cannabinoid concentration distance matrices with
community dissimilarity matrices revealed significant but moderate correlations
between cannabinoid profiles and endorhiza community structure. The correlation
was stronger when using weighted
[[unifrac-weighted-unweighted-analysis-cannabis-microbiome|UniFrac]] distances
(incorporating taxon abundance) compared to unweighted UniFrac (presence-absence
only), suggesting that cannabinoid concentrations affect the relative abundance
of endorhiza taxa rather than fundamentally determining which taxa are present.

However, when partial Mantel tests were performed controlling for soil edaphic
variables, the cannabinoid-community correlation was substantially reduced. This
indicated that a significant portion of the observed cannabinoid-microbiome
relationship was mediated through shared edaphic influences rather than direct
plant-microbe signaling involving cannabinoid compounds.

## Confounding with Soil Edaphic Variables

### The Confounding Problem

The fundamental analytical challenge identified by Winston et al. was the
entanglement of three factors: cultivar identity, cannabinoid concentration,
and soil chemistry. Cultivar determines cannabinoid profile (genetic basis),
cultivar also influences root exudate chemistry (affecting microbiome), and
cultivar response to soil conditions creates genotype-by-environment
interactions. Additionally, soil chemistry independently shapes the microbiome
and may influence cannabinoid biosynthesis through nutrient availability.

[[nitrogen-edaphic-factor-cannabis-microbiome|Nitrogen availability]] was the
strongest edaphic predictor of community structure, and nitrogen is also known
to influence cannabinoid biosynthesis rates. This dual role of nitrogen creates
a statistical confound: the observed cannabinoid-microbiome correlation could
reflect nitrogen's independent effects on both variables rather than a direct
cannabinoid-microbe interaction.

### Partial Correlation Analysis

Partial Mantel tests and distance-based redundancy analysis (dbRDA) were
employed to partition the variance in community composition attributable to
cannabinoid concentration versus edaphic factors. After controlling for soil
chemistry, the unique contribution of cannabinoid concentration to community
variation was small but detectable. This residual signal suggests that some
direct interaction between cannabinoid-producing root tissues and the
endorhiza microbiome may exist, but it is dwarfed by the overwhelming influence
of soil physicochemical properties.

## Mechanisms of Cannabinoid-Microbiome Interaction

Despite the confounding challenges, several plausible mechanisms could underlie
direct cannabinoid-endophyte interactions. Cannabinoid compounds possess
antimicrobial properties that could selectively inhibit or promote specific
bacterial taxa in the root interior. THC and CBD have documented antibacterial
activity against Gram-positive bacteria, which could shape the relative
abundance of Actinomycetales and other Gram-positive endorhiza members.

Root exudates may also contain cannabinoid biosynthetic intermediates or
degradation products that serve as carbon sources for specialized endophytes.
The [[cannabis-endorhiza-core-microbiome-pseudomonas-rhizobiales|core
microbiome]] taxa consistently detected across cultivars may be those capable
of tolerating or metabolizing low levels of cannabinoid compounds in root
tissues. Conversely, [[cannabis-cultivar-specificity-microbial-selection-mechanisms|cultivar-specific
enrichments]] like [[methylophilus|Methylophilus]] and
[[sphingomonas-wittichii|Sphingomonas wittichii]] may reflect differential
tolerance to cannabinoid concentrations.

## Implications for Terroir

The cannabis terroir concept posits that growing environment, including soil
chemistry, climate, and microbial ecology, influences the chemical profile of
harvested Cannabis flowers. The Winston et al. findings support a bidirectional
terroir model: soil conditions shape the endorhiza microbiome, which may in
turn influence plant metabolism and cannabinoid production, while soil chemistry
also directly affects cannabinoid biosynthesis through nutrient availability.

This creates a feedback loop in which soil, microbiome, and plant secondary
metabolism are interconnected. The strong edaphic effect on community structure
means that the same Cannabis cultivar grown in different soils will harbor
distinct endorhiza communities, potentially leading to subtle differences in
cannabinoid profiles even when genotype is held constant.

## Limitations and Future Directions

The correlational nature of the Mantel test approach limits causal inference.
Experimental manipulations of cannabinoid biosynthesis (e.g., using genetic
knockouts or biosynthetic inhibitors) in controlled soil environments would be
necessary to isolate direct cannabinoid-microbiome effects. Gnotobiotic
experiments inoculating sterile Cannabis roots with defined microbial
communities under varying cannabinoid production conditions could establish
causality and identify specific cannabinoid-responsive taxa.

## See Also

- [[two-tier-selection-model]]
- [[cannabis-endorhiza-core-microbiome-pseudomonas-rhizobiales]]
- [[cannabis-cultivar-specificity-microbial-selection-mechanisms]]
- [[nitrogen-edaphic-factor-cannabis-microbiome]]
- [[methylophilus]]
- [[sphingomonas-wittichii]]
- [[unifrac-weighted-unweighted-analysis-cannabis-microbiome]]
- [[cannabis-rhizosphere-community-structure-edaphic-factors]]
