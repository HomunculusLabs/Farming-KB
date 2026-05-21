---
title: Photon-Counting Scintillation Imaging (PCSI) for Mycelial Transport
source: geoffrey-gadd-sarah-c-watkinson-paul-s-dyer-fungi-in-the-environment.md
type: concept
---

## Photon-Counting Scintillation Imaging (PCSI) for Mycelial Nutrient Transport

## Overview

**Photon-Counting Scintillation Imaging (PCSI)** is a novel non-invasive technique developed to track the movement of radiolabelled compounds through fungal [[fungal-mycelial-networks-nutrient-translocation]]. It enables continuous, real-time visualization of nutrient translocation at the millimetre to centimetre scale in growing mycelia, providing unprecedented insight into how saprotrophic basidiomycetes distribute resources through their foraging networks.

## Principle of Operation

PCSI works by placing foraging mycelial networks in contact with an **inert scintillation screen**. When radiolabelled compounds (typically carbon-14 labelled) are introduced into the mycelium, the emitted beta particles interact with the scintillation screen to produce photons, which are detected and counted by a sensitive imaging system. This produces a spatial map of radiolabel distribution over time without requiring destructive harvesting of the fungal tissue.

The key advantage over traditional autoradiography and phosphor-imaging techniques is that PCSI provides **continuous, non-destructive time-series data**, allowing researchers to observe dynamic transport processes as they occur in living mycelia.

## Tracer Compound: 14C-AIB

The technique most commonly uses **[[alpha-amino-isobutyrate]] (14C-AIB)** as a tracer for nitrogen transport. AIB is a non-metabolized amino acid analogue, meaning it is taken up by the mycelium and translocated but is not incorporated into metabolic pathways. This makes it an ideal tracer because:

- It faithfully reports the transport dynamics of nitrogen-containing compounds
- It is not consumed or transformed during the experiment, providing a conservative tracer
- Its distribution pattern directly reflects the transport processes rather than metabolic processing

## Two Analytical Protocols

Two complementary analytical protocols have been developed:

### 1. Correlation Analysis (AIB Distribution vs. Growth)

This approach focuses on the correlation between local distribution patterns of AIB and local patterns of growth. It accommodates the marked asymmetry in colony development, particularly in the presence of additional resources that create a highly polarized resource environment.

The AIB distribution is characterized by three key parameters:

- **Centre of Mass Displacement (CMD):** The position of the centre of mass of AIB relative to the centre of the inoculum. Zero displacement represents symmetrical N distribution.
- **Angular Concentration (ConcD):** A measure of how evenly the AIB is spread around the colony versus concentrated in a particular area. Values of zero represent completely even distribution; values approaching 1 indicate very tightly focused distribution.
- **Alignment with Resource:** The degree to which the CMD vector aligns with the direction of a new resource. A value of zero represents perfect alignment toward the resource.

### 2. Pulsatile Component Analysis

This approach focuses on mapping the **pulsatile component** of transport that was observed superimposed on the net AIB translocation pattern. Pulsatile transport is particularly prominent through corded systems and reveals oscillatory behaviour in nutrient flux.

## Automated Colony Segmentation

Since PCSI precludes separate bright-field imaging (due to the white scintillation screen), colony growth must be estimated from the scintillation image itself. This is achieved through:

1. **Contrast-Limited Adaptive Histogram Equalization (CLAHE):** Enhances contrast in the scintillation image to distinguish mycelial areas from background
2. **Automated Grey-Scale Thresholding (Otsu"s method):** Segments the image into mycelial and background regions
3. **Validation:** The approach has been validated against bright-field images of colonies grown across Mylar film (1.5 mm thick) against a black background, showing very good correspondence

## Colony Growth Phases

The analysis reveals two distinct phases of colony development:

### First Phase: Symmetrical Growth
- Change in area and transport are almost symmetrical
- Duration depends on nutrient availability and developmental age of the colony
- Characterized by uniform expansion from the inoculum

### Second Phase: Asymmetric Growth
- Transition to sparser, more asymmetric growth
- Growth and resource allocation become focused toward specific directions or resources
- Canalized flow patterns in cords emerge with this transition
- Added resources induce marked N accumulation and asymmetric growth tightly focused on the new resource

The transition between phases can be described by **two superimposed logistic equations**, allowing normalization of all datasets to a common developmental stage.

## Statistical Analysis: Linear Mixed Effects Models

Time series data for CMD, ConcD, and area-based equivalents are fitted using **Linear Mixed Effects models** (Pinheiro and Bates, 2000). These models allow:

- Statistical comparison between control and treatment groups
- Normalization to the start of the second growth phase
- Quantification of the magnitude and directionality of resource allocation changes

## Response to Resource Addition

When a damp cellulosic resource (filter paper) is added to a growing colony:
- Internal nitrogen allocation changes, promoting marked N accumulation
- Asymmetric growth becomes tightly focused on the new resource
- Both transport and growth displacement vectors align strongly with the bait direction

A damp glass-fibre "resource" produces a more variable response, often with a transient perturbation response that is not sustained compared with filter-paper resources, reflecting the difference between a real nutrient source and a physical stimulus.

## Extended Microcosm Applications

The PCSI approach has been modified for more realistic microcosms using:
- **Wood-block inocula** instead of agar
- **Sand or soil substrata** overlaid with a translucent scintillation screen
- Extended imaging periods exceeding **6 weeks**

In these systems, complex sequences of shifts in nitrogen distribution and transport priority are observed throughout the network as it develops, revealing the sophisticated resource management strategies employed by cord-forming basidiomycetes.

## References

- Tlalka, M., Watkinson, S. C., Darrah, P. R. and Fricker, M. D. (2002). Continuous imaging of amino acid translocation in intact mycelia of *Phanerochaete velutina* reveals rapid, pulsatile fluxes. *New Phytologist* 153, 173-84.
- Tlalka, M., Hensman, D., Darrah, P. R., Watkinson, S. C. and Fricker, M. D. (2003). Noncircadian oscillations in amino acid transport have complementary profiles in assimilatory and foraging hyphae of *Phanerochaete velutina*. *New Phytologist* 158, 325-35.
- Otsu, N. (1979). A threshold selection method from gray-level histograms. *IEEE Trans. SMC* 9, 62-6.
- Pinheiro, J. and Bates, D. M. (2000). *Mixed Effects Models in S and S-PLUS*. New York: Springer-Verlag.

## See Also

- [[photon-counting-scintillation-imaging]]
- [[fungal-biology-fundamentals]]
- [[isotopic-tracers-mycorrhizal-research]]
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
