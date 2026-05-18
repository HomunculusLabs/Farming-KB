---
title: Pulsatile Transport Fourier Analysis Fungi
source: geoffrey-gadd-sarah-c-watkinson-paul-s-dyer-fungi-in-the-environment.md
type: concept
---

# Pulsatile Nutrient Transport and Fourier Analysis in Fungal Mycelia

## Overview

A striking discovery in the study of fungal nutrient dynamics is the presence of **pulsatile (oscillatory) transport** of solutes through mycelial networks. Rather than moving at a constant rate, nutrients such as amino acids are transported in rhythmic pulses, particularly through corded (differentiated) hyphal systems. This pulsatile behaviour has been characterized using **Fourier analysis** techniques applied to time-series data from photon-counting [[pcsi-scintillation-imaging-mycelial-nutrient-transport-bebber]] (PCSI), revealing complex spatiotemporal patterns of coordination across the mycelial network.

## Discovery of Pulsatile Transport

Pulsatile transport was first observed in time-series PCSI data from *[[phanerochaete-velutina]]* mycelia. When the distribution of 14C-AIB was tracked over time, researchers noticed that the signal intensity at individual locations did not increase monotonically but oscillated in a regular, wave-like manner. This pulsatile component was particularly pronounced in corded systems, where differentiated, thick-walled hyphae serve as major transport conduits.

The oscillations are superimposed on the longer-term trend of net translocation, meaning that the overall movement of nutrients toward growing tips or newly discovered resources occurs through a series of pulses rather than as a steady flow.

## Phase Relationships Between Colony Regions

One of the most important findings from the Fourier analysis is that different regions of the colony exhibit **out-of-phase oscillations**:

- **Assimilatory hyphae** (on the inoculum and new resource) pulse in a pattern that is out of phase with
- **Foraging hyphae** (at the growing margin)

This complementary phasing suggests a coordinated, potentially pumping-like mechanism for nutrient distribution across the colony, rather than simple passive diffusion or bulk flow.

## Fourier Analysis Pipeline

The complete analytical pipeline for characterizing pulsatile transport involves several sequential steps:

### Step 1: Data Acquisition
Time-series PCSI data are collected, recording the distribution of 14C-AIB at each pixel over the duration of the experiment.

### Step 2: Spatial and Temporal Smoothing
- **Spatial averaging** using a 3x3 to 7x7 pixel kernel to reduce noise
- **Temporal averaging** using a 3-5 hour rolling average to identify trends

### Step 3: Detrending
The longer-term trend is estimated using a 12-24 hour rolling average and subtracted from the data to produce a stationary time-series suitable for Fourier analysis.

### Step 4: Time-of-Arrival Mapping
For each pixel, the time when the signal either reaches its maximum or exceeds the background by more than two standard deviations is extracted. This is pseudo-colour-coded as a concise summary of long-term translocation patterns.

### Step 5: Discrete Fast Fourier Transform (FFT)
The FFT is calculated **pixel by pixel** for the detrended oscillations, producing arrays of:
- **Magnitude values:** The amplitude of the oscillation at each frequency
- **Phase values:** The timing offset of the oscillation relative to a reference

### Step 6: Dominant Frequency Extraction
The maximum frequency component is identified for each pixel, and:
- Time of arrival is normalized to the total experimental duration
- The dominant frequency is normalized to the frequency range
- The magnitude is normalized to the maximum observed value
- The phase is normalized to plus or minus pi radians

### Step 7: Visualization as Colour-Coded Maps
The results are displayed as pseudo-colour-coded images (HSV to RGB conversion) showing:
- **Dominant Fourier frequency** (hue-coded): Reveals the periodicity of transport at each location
- **Amplitude** (brightness/intensity): Shows the strength of the oscillation
- **Phase shift** (hue-coded): Displays the timing relationships between different regions

Regions where the Fourier frequency varies from the dominant frequency by more than plus or minus 1 are masked to highlight coherent domains.

## Key Findings from Fourier Analysis

### Synchronized Phase Domains
The colour-coded phase maps reveal that signals from different parts of the colony form **distinct phase domains** that are locally synchronized. This means that neighbouring regions of the mycelium tend to oscillate in concert, creating coordinated waves of nutrient transport.

### Amplitude Shifts Toward Resources
In several colonies, the **amplitude of the pulsing centre** shifted towards newly added resources (baits). This indicates that the mycelial network dynamically reorganizes its transport activity to prioritize resource acquisition.

### Prolonged Oscillation Duration
In larger microcosms, the oscillations continue for approximately **5-7 days** after initial loading, indicating that pulsatile transport is not a transient phenomenon but a sustained feature of mycelial physiology.

## Route-Switching Behaviour

In extended microcosm experiments, an important phenomenon called **route-switching** was observed. Not all cords transported simultaneously. Some pre-existing cords showed no 14C-AIB movement initially, then began transporting at a similar rate to the primary cord, acting as a transport route only transiently before the signal declined.

Similarly, some subsidiary cords showed **two phases of transport**: one initiated almost synchronously with the main cord and a second starting much later (around 120-150 hours). This reveals that the mycelial network dynamically activates and deactivates different [[the-apoplastic-symplastic-and-transcellular-transport-pathways]] over time.

## Larger Microcosm Observations

When the PCSI approach was scaled up to more realistic microcosms (wood-block inocula on sand or soil substrata), several important observations emerged:

- **Rapid initial transport:** 14C-AIB travelled 250 mm along a major cord within 1 hour of loading
- **Broad distribution:** Within 4 hours, signal was present in most of the growing mycelium subtended by the active cord
- **Asynchronous cord activation:** Different cords became active at different times, with some showing transient activation (route-switching) and others showing sustained or multi-phase transport
- **Signal decay at the margin:** Overall signal levels decreased in cords as the growing mycelial margin advanced out of the region, reflecting resource depletion

## Significance

The pulsatile nature of fungal nutrient transport has several important implications:

1. **Active transport mechanism:** The regularity and coordination of the pulses suggest an active, regulated transport process rather than passive diffusion or simple bulk flow
2. **Network-level coordination:** The phase relationships between different colony regions indicate sophisticated [[plasmodesmata-and-intercellular-communication-in-plants]] and coordination
3. **Dynamic [[mycelial-foraging-resource-allocation]]:** Route-switching and amplitude shifting demonstrate that the network can rapidly reconfigure its transport priorities in response to environmental changes
4. **Efficiency:** Pulsatile transport may be more energy-efficient than continuous flow, allowing the mycelium to concentrate resources in waves that optimize delivery to growing tips

## References

- Tlalka, M., Watkinson, S. C., Darrah, P. R. and Fricker, M. D. (2002). Continuous imaging of amino acid translocation in intact mycelia of *Phanerochaete velutina* reveals rapid, pulsatile fluxes. *New Phytologist* 153, 173-84.
- Tlalka, M., Hensman, D., Darrah, P. R., Watkinson, S. C. and Fricker, M. D. (2003). Noncircadian oscillations in amino acid transport have complementary profiles in assimilatory and foraging hyphae of *Phanerochaete velutina*. *New Phytologist* 158, 325-35.

## See Also

- [[pulsatile-nutrient-transport-fungal-mycelia]]
- [[fungal-biology-fundamentals]]
- [[mycelial-network-structure]]
