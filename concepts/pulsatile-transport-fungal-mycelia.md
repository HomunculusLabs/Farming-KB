---
title: Pulsatile Transport Fungal Mycelia
source: geoffrey-gadd-sarah-c-watkinson-paul-s-dyer-fungi-in-the-environment.md
type: concept
---

# Pulsatile Transport in Fungal Mycelia

## Overview

In addition to steady-state diffusive and bulk-flow transport, fungal mycelia exhibit a pronounced **pulsatile component** associated with rapid [[nutrient-movement-plant-roots]], particularly through corded (differentiated) transport systems. This oscillatory behaviour was discovered using photon-counting [[pcsi-scintillation-imaging-mycelial-nutrient-transport-bebber]] (PCSI) of 14C-labelled [[alpha-amino-isobutyrate]] (14C-AIB) and represents one of the most striking features of mycelial nutrient dynamics. The pulsatile transport creates coordinated waves of nutrient flux that move through different regions of the colony with distinct phase relationships.

## Discovery and Initial Characterization

Pulsatile transport was first observed in *[[phanerochaete-velutina]]* when time-series PCSI data revealed that 14C-AIB movement was not a smooth, continuous process but rather exhibited strong oscillations superimposed on the longer-term translocation trend. Initial Fourier analysis of discrete regions of interest showed that:

- The **assimilatory mycelium** at the inoculum site pulsates
- The **foraging mycelium** at the colony margin also pulsates
- These two regions pulse **out of phase** with each other

This phase difference between assimilatory and foraging compartments suggests that pulsatile transport may reflect a pumping or pressure-driven mechanism that alternately fills and drains different regions of the mycelial network.

## Fourier Analysis Pipeline

To systematically map the pulsatile component across entire colonies, researchers developed a pixel-by-pixel Fourier analysis pipeline:

### Step 1: Preprocessing
1. **Spatial averaging**: Apply a 3x3 to 7x7 (x,y) kernel to smooth pixel-level noise
2. **Temporal averaging**: Use a 3-5 hour rolling average to establish the baseline trend
3. **Trend subtraction**: Calculate 2nd differences or subtract the trend data (12-24 hour rolling average) to obtain a stationary time series
4. **Zero-padding**: Pad the time series with zeros to the nearest power of 2 for efficient FFT computation

### Step 2: Time-of-Arrival Mapping
- Calculate when the signal reaches maximum intensity or exceeds the background threshold (mean_background + 2 x SD_background)
- Normalize to total experimental time and encode as a hue layer in HSV colour space
- Produces a concise pseudo-colour summary of long-term translocation patterns

### Step 3: Discrete Fourier Transform
- Compute the **Fast Fourier Transform (FFT)** at each pixel
- Extract three key parameters from the dominant frequency:
  - **Frequency**: The dominant oscillation frequency
  - **Amplitude (magnitude)**: The strength of the pulsatile signal at the dominant frequency
  - **Phase**: The timing offset of the oscillation relative to a reference

### Step 4: Visualization
- Frequency is normalized to the observed range and coded as the **hue (H)** layer
- Amplitude is normalized to the maximum magnitude
- Phase is normalized to +/-pi radians
- These are combined in HSV colour space and converted to RGB for display

## Phase Domain Organization

The pixel-by-pixel Fourier maps revealed that pulsatile signals are organized into distinct **phase domains** within the colony:

- Signals from **assimilatory hyphae** in the inoculum and at new resources oscillate with one phase
- Signals from **foraging hyphae** at the colony margin oscillate with a different phase
- Within each domain, oscillations are **locally synchronized**
- The phase differences became established as the colony developed

In several colonies, the **amplitude centre** of the pulsation also shifted towards newly added resources, suggesting that the pulsatile mechanism can be redirected to prioritize nutrient delivery to regions of high demand.

## Pulsatile Behaviour in Larger Microcosms

When the PCSI approach was extended to more realistic microcosms (wood-block inocula, sand substrata, translucent scintillation screens), pulsatile behaviour was observed over extended periods (up to 6+ weeks). Key observations include:

### Rapid Initial Transport
- Within **1 hour** of loading 14C-AIB at the wood inoculum, the radiolabel had travelled **250 mm** along a major cord
- Within **4 hours**, signal was present in most growing mycelium subtended by this cord

### Sustained Oscillations
- Pronounced oscillations continued for approximately **5-7 days** following initial loading
- The overall signal level in cords decreased as the growing mycelial margin advanced out of the region

### Route Switching
Not all cords transported simultaneously, revealing a dynamic **route-switching** mechanism:
- Pre-existing cords that showed no initial AIB movement began transporting after approximately 12 hours
- Some cords functioned as transport routes only **transiently**, with signal declining after around 30 hours
- Other subsidiary cords showed **multiple phases** of transport, with one phase initiated synchronously with the main cord and additional phases starting around 120-150 hours

## Mechanistic Implications

The pulsatile transport phenomenon raises important questions about the underlying mechanism:

1. **Pressure-driven flow**: The oscillatory nature is consistent with periodic pressure fluctuations, possibly driven by protoplasmic streaming or osmotic gradients
2. **Coordination across domains**: The establishment of synchronized phase domains suggests [[plasmodesmata-and-intercellular-communication-in-plants]] coordinating the timing of pulsations
3. **Resource-directed modulation**: The shift in amplitude centre towards new resources indicates that the pulsatile mechanism is responsive to source-sink relationships
4. **Route switching**: The transient activation and deactivation of different cord pathways suggests a dynamic allocation system that can redirect transport capacity

## Non-Circadian Nature

Importantly, the oscillations observed in amino acid transport are **non-circadian** -- they do not follow a 24-hour cycle and are not entrained by light-dark conditions. The complementary profiles observed in assimilatory and foraging hyphae (Tlalka et al., 2003) suggest an intrinsic biological rhythm rather than an environmental response.

## See Also

- [[photon-counting-scintillation-imaging]] - The PCSI technique used to detect pulsatile transport
- [[vacuolar-transport-fungal-hyphae]] - Intracellular diffusion-based transport
- [[fungal-mycelial-network-analysis]] - [[mycelial-network-architecture]] governing transport routes

## References

- Tlalka, M., Watkinson, S. C., Darrah, P. R. & Fricker, M. D. (2002). Continuous imaging of amino acid translocation in intact mycelia of *Phanerochaete velutina* reveals rapid, pulsatile fluxes. *New Phytologist* 153, 173-84.
- Tlalka, M., Hensman, D., Darrah, P. R., Watkinson, S. C. & Fricker, M. D. (2003). Noncircadian oscillations in amino acid transport have complementary profiles in assimilatory and foraging hyphae of *Phanerochaete velutina*. *New Phytologist* 158, 325-35.
## Practical Applications
The principles discussed here have direct applications in agricultural systems, ecological restoration, and sustainable resource management.
Practitioners have demonstrated successful implementation across diverse climates and soil conditions.
Adaptation to local conditions and careful observation remain central to effective application.

## Research Directions
Current research explores the intersections between traditional knowledge and modern scientific understanding.
Comparative studies across different bioregions provide valuable insights into generalizable principles.
Long-term monitoring and documentation continue to build the evidence base for these approaches.
Collaborative research networks facilitate knowledge exchange and accelerate innovation.

## Key Considerations
Context-specific implementation requires attention to local ecology, climate patterns, and community needs.
Integration with existing systems often yields better results than complete replacement strategies.
Monitoring and adaptive management are essential for long-term success and continuous improvement.
## Further Considerations
Ongoing research and field trials continue to expand our understanding of this subject.
Practical experience combined with systematic observation yields the most reliable insights.

## Future Directions
Emerging approaches and technologies offer new opportunities for advancement.
Collaborative knowledge sharing accelerates progress across related domains.
