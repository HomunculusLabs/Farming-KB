---
title: mixed-microbial-challenge-organisms-surface-sterilization-testing in NASA microwave-surface-sterilization Testing
aliases: [bacillus pumilus [[microwave-sterilization]], NASA sterilization test organisms, microwave microbial kill validation]
tags: [sterilization, microwave, NASA, microbiology, bacillus-pumilus, escherichia-coli, pseudomonas-cepacia, biological-indicators]
created: 2026-05-08
source: sterilizing-surfaces-by-irradiation-with-microwaves.md
---

# Challenge Organisms in NASA Microwave Surface Sterilization Testing

## Overview

The NASA microwave surface sterilization study (MSC-22484) employed a carefully selected panel of three microbial challenge organisms to validate the efficacy of the [[dry-microwave-irradiation-spore-resistance]] protocol. The mixed population included *Bacillus pumilus*, *Escherichia coli*, and *Pseudomonas cepacia*, representing three distinct categories of microbial resistance: bacterial spores, gram-negative vegetative cells with high radiation sensitivity, and gram-negative vegetative cells with moderate environmental resistance. Together, these organisms span the range of resistance profiles likely to be encountered in contamination control applications.

## The Three Challenge Organisms

### Bacillus pumilus

*Bacillus pumilus* is a gram-positive, spore-forming bacterium and the most resistant organism in the test panel. Its inclusion as a challenge organism reflects its status as a standard biological indicator in sterilization validation.

**Key characteristics relevant to sterilization testing:**

- **Spore formation** — Under stress conditions, *B. pumilus* produces endospores that are among the most resistant known biological structures, surviving extremes of heat, radiation, desiccation, and chemical exposure
- **[[bacillus-pumilus-radiation-resistance-surface-decontamination]]** — *B. pumilus* spores are notably resistant to ionizing radiation (gamma rays, X-rays) and UV radiation, making them a standard challenge organism for radiation-based [[conventional-surface-sterilization-methods-limitations-comparison]]
- **Environmental persistence** — Spores can persist in the environment for years without losing viability, making them a realistic contamination threat
- **Spacecraft relevance** — *B. pumilus* has been isolated from spacecraft assembly clean rooms and has been detected on spacecraft surfaces, making it directly relevant to NASA's contamination control concerns
- **Recovery and culturing** — Grows readily on standard microbiological media (nutrient agar, tryptic soy agar), facilitating post-treatment viability assessment

In the [[rotational-transition-water-dipole-microwave-sterilization-physics]] study, *B. pumilus* was the last organism to be eliminated, requiring the full 13.1 W-hr exposure for complete kill. This confirmed that the protocol was effective against the most resistant organism in the panel, providing confidence that it would also eliminate less resistant contaminants.

### Escherichia coli

*Escherichia coli* is a gram-negative, non-spore-forming bacterium and the most sensitive organism in the test panel. Its inclusion provides a lower bound on the sterilization dose-response curve.

**Key characteristics relevant to sterilization testing:**

- **Vegetative cells only** — Does not form spores, making it inherently more vulnerable to heat, radiation, and chemical agents than spore-formers
- **High water content** — Vegetative *E. coli* cells contain approximately 70-80% water, providing ample target for microwave energy coupling
- **Radiation sensitivity** — Relatively sensitive to both ionizing and non-ionizing radiation compared to spore-formers and some other vegetative bacteria
- **Rapid growth** — Fast generation time (20-30 minutes under optimal conditions) allows quick assessment of post-treatment viability
- **Universal laboratory organism** — Well-characterized genetics, physiology, and culture requirements; inexpensive and reliable to work with

In the microwave study, *E. coli* was the first organism to be eliminated at low microwave exposures, showing approximately 10⁴ reduction at minimal exposure levels. This early elimination demonstrates that the microwave protocol is effective even against the most sensitive organisms, and that the full 13.1 W-hr protocol provides a large margin of safety for vegetative organisms.

### Pseudomonas cepacia (Burkholderia cepacia)

*Pseudomonas cepacia* (reclassified as *Burkholderia cepacia*) is a gram-negative, non-spore-forming bacterium with moderate environmental resistance, occupying an intermediate position in the test panel between the radiation-sensitive *E. coli* and the spore-forming *B. pumilus*.

**Key characteristics relevant to sterilization testing:**

- **Environmental resilience** — *B. cepacia* is naturally resistant to many disinfectants and antiseptics, surviving exposure to quaternary ammonium compounds, chlorhexidine, and some alcohol-based disinfectants
- **Biofilm formation** — Can form biofilms on surfaces, which provide additional protection against antimicrobial agents
- **Nutritional versatility** — Can metabolize a wide range of organic compounds, allowing it to persist in diverse environments including water systems, soil, and clinical settings
- **Clinical significance** — An opportunistic pathogen, particularly dangerous for patients with cystic fibrosis; its inclusion in sterilization testing reflects clinical relevance
- **Gram-negative cell wall** — The outer membrane of gram-negative bacteria provides additional barrier protection compared to gram-positive organisms

In the microwave study, *B. cepacia* showed intermediate sensitivity, requiring moderate microwave exposure for significant population reduction and being eliminated before *B. pumilus* spores but after *E. coli*. This intermediate position validates the graduated response of the microwave protocol across organisms of varying resistance.

## Rationale for the Mixed Population Approach

The use of a mixed population rather than individual organism challenges serves several important validation purposes:

1. **Realism** — Real-world contamination involves mixed populations, not single-species challenges
2. **Competitive interactions** — Mixed populations may exhibit different survival dynamics than pure cultures due to competition for resources or protective interactions
3. **Dose-response characterization** — The different resistance levels of the three organisms create a natural dose-response gradient within a single experiment
4. **Worst-case demonstration** — If the protocol eliminates the most resistant organism (*B. pumilus* spores), it by definition eliminates the less resistant ones
5. **Efficiency** — Testing three organisms simultaneously is more efficient than running three separate experiments

## Initial Population and Kill Criteria

The study used an initial surface population of approximately 2 × 10⁵ Colony Forming Units (CFU). This population level represents a realistic worst-case contamination scenario — higher than would typically be encountered in a well-maintained clean room but plausible in field conditions or after a contamination event.

The kill criterion was complete sterilization: reduction from the initial population to zero detectable CFU. This is a more stringent criterion than the "6-log reduction" (99.9999% kill) commonly used in industrial sterilization validation, as it requires elimination of every single organism rather than a proportional reduction.

## Kill Curve Analysis

The microbial kill curves presented in the NASA Tech Brief (Figure 2) reveal distinct phases in the sterilization process at 3.6 W/cm²:

**Phase 1 (0-2 W-hr): Rapid vegetative kill**
- *E. coli* population drops by approximately 4-5 orders of magnitude
- *B. cepacia* shows moderate reduction (1-2 orders of magnitude)
- *B. pumilus* spores show minimal effect
- Dominant mechanism: Direct microwave heating of intracellular water in vegetative cells

**Phase 2 (2-8 W-hr): Progressive elimination**
- *E. coli* is completely eliminated
- *B. cepacia* population drops to near-zero
- *B. pumilus* spores begin significant reduction
- Dominant mechanism: Combination of residual microwave heating and steam effects

**Phase 3 (8-13.1 W-hr): Spore elimination**
- *B. cepacia* is completely eliminated
- *B. pumilus* spores progressively reduced to zero
- Dominant mechanism: Flash steam from trace water penetrating spore coats

## Relevance to Spacecraft Contamination Control

The choice of these particular organisms reflects NASA's specific contamination control concerns:

- **Planetary protection** — Preventing forward contamination of other celestial bodies requires elimination of hardy terrestrial organisms, including spore-formers like *B. pumilus*
- **Crew health** — Eliminating opportunistic pathogens like *B. cepacia* from closed spacecraft environments protects immunocompromised crew members
- **ECLSS integrity** — Preventing microbial contamination of [[eclss-environmental-control-life-support]] and Life Support System water supplies requires inactivation of waterborne organisms including *E. coli*
- **Experimental validity** — Space biology experiments require truly sterile conditions to prevent confounding results from contaminant organisms

## See Also

- [[bacillus-pumilus-radiation-resistance-surface-decontamination]] — *B. pumilus* radiation resistance profile
- [[microwave-sterilization-dose-response-microbial-kill-curves]] — Detailed kill curve analysis
- [[spore-vs-vegetative-cell-resistance-microwave-sterilization]] — Spore vs. vegetative cell comparison
- [[microwave-sterilizable-access-port-nasa-space-biology]] — MSAP system overview

## References

- Atwater JE, Streech ND, Garmon FC. Sterilizing Surfaces by Irradiation with Microwaves. NASA Tech Briefs MSC-22484.
- La Duc MT, Nicholson W, Kern R, Venkateswaran K (2003). Microbial characterization of the Mars Odyssey spacecraft and its assembly facility. *Environmental Microbiology* 5(12):977-985.
- Nicholson WL, Munakata N, Horneck G et al. (2000). Resistance of *Bacillus* endospores to extreme terrestrial and extraterrestrial environments. *Microbiology and Molecular Biology Reviews* 64(3):548-572.

## Comparison with Standard Biological Indicators

In industrial sterilization validation, specific biological indicators are standardized for different sterilization methods. The organisms chosen for the NASA microwave study can be compared to these standards:

| Sterilization Method | Standard Biological Indicator | NASA Study Equivalent |
|---|---|---|
| Autoclave (steam) | *Geobacillus stearothermophilus* spores | *Bacillus pumilus* spores (similar spore resistance) |
| Ethylene oxide | *Bacillus atrophaeus* spores | *B. pumilus* spores |
| Gamma irradiation | *B. pumilus* spores (most radiation-resistant) | *B. pumilus* spores (same organism) |
| Dry heat | *B. atrophaeus* spores | *B. pumilus* spores |
| UV irradiation | *[[bacillus-subtilis]]* spores | *B. pumilus* spores (higher resistance) |

Notably, *B. pumilus* is itself the standard biological indicator for gamma irradiation sterilization, one of the most challenging sterilization methods. Its inclusion in the microwave study as the most resistant challenge organism establishes a high bar for validating the microwave protocol — if it can kill radiation-resistant *B. pumilus* spores, it can likely handle any organism encountered in practice.
