---
title: Photon Counting Scintillation Imaging Mycelial Transport
source: geoffrey-gadd-sarah-c-watkinson-paul-s-dyer-fungi-in-the-environment.md
type: concept
---

## Overview

Photon-counting scintillation imaging (PCSI) is a non-invasive radiotracer technique developed to visualize and quantify real-time nutrient translocation in [[fungal-mycelial-networks-ecosystem-engineers]]. By tracking the movement of ¹⁴C-labelled compounds across growing colonies, PCSI reveals spatial and temporal patterns of resource allocation that are invisible to conventional microscopy. The technique has been particularly valuable for studying how saprotrophic basidiomycetes such as *[[phanerochaete-velutina]]* distribute nitrogen and carbon through corded mycelial networks spanning centimetre to metre scales, and has revealed phenomena including pulsatile transport, route-switching, and resource-directed foraging.

## Principles of PCSI

PCSI works by growing fungal mycelium in contact with an inert scintillation screen. When a radiolabelled compound (typically ¹⁴C-labelled α-amino-isobutyrate, or ¹⁴C-AIB) is introduced at a specific location in the mycelium, radioactive decay events produce photons where the tracer accumulates. These photons are detected by a sensitive camera system, generating a time-series of images that map the spatial distribution of the tracer with high temporal resolution.

The key advantages of PCSI over conventional autoradiography include:

- **Non-destructive**: colonies remain intact and viable throughout imaging
- **Continuous temporal resolution**: transport dynamics can be followed in real time rather than requiring destructive harvest at discrete time points
- **Quantitative**: photon counts provide a measure of tracer concentration
- **Extended duration**: experiments can run for weeks, capturing long-term developmental changes

## The ¹⁴C-AIB Tracer System

α-amino-isobutyrate (AIB) is a non-metabolized amino acid analogue that is taken up by fungal amino acid transporters but not incorporated into proteins or further metabolized. This makes it an ideal tracer for studying translocation patterns, as its distribution reflects transport processes rather than metabolic transformation. The ¹⁴C radioisotope provides detectable decay events suitable for scintillation imaging.

## Quantitative Analysis of Distribution Patterns

The spatial distribution of ¹⁴C-AIB within a colony is characterized by several quantitative parameters:

- **Centre of Mass Displacement (CMDAIB)**: the position of the centre of mass of tracer relative to the inoculum centre, measuring directional bias in nutrient allocation
- **Angular Concentration (ConcDAIB)**: a measure of how tightly focused the tracer distribution is, ranging from 0 (completely uniform) to ~1 (highly concentrated in one sector)
- **Alignment with Resources**: the angular alignment between the CMDAIB displacement vector and the vector pointing toward an added resource, quantifying how specifically nutrient allocation targets a particular resource

## Colony Growth Quantification

Since PCSI precludes simultaneous bright-field imaging (the mycelium and scintillation screen are both white), colony growth is estimated from the scintillation images themselves using automated image processing:

1. **Contrast-Limited Adaptive Histogram Equalization (CLAHE)**: enhances contrast in the scintillation images
2. **Automated Grey-Scale Thresholding** (Otsu method): segments the mycelial area from the background
3. **Time-Differencing**: changes in segmented area over 12–24 hour windows quantify growth rates and directions

This automated approach has been validated against bright-field images of colonies grown on semi-transparent substrates, showing very good correspondence between the segmented boundary and the visible colony margin.

## Growth Phase Dynamics

Colonies of *P. velutina* display two distinct growth phases that can be described by superimposed logistic equations:

1. **Phase 1 — Symmetric Growth**: initial uniform radial expansion with approximately even tracer distribution
2. **Phase 2 — Asymmetric Foraging**: transition to sparser, more directional growth with focused nutrient allocation

The duration of Phase 1 depends on nutrient availability and colony developmental age. By normalizing time-series data to the start of Phase 2 using bi-logistic fitting, data from different experimental conditions can be compared at equivalent developmental stages. Linear Mixed Effects models are then fitted to the normalized CMDAIB, ConcDAIB, CMDarea, and ConcDarea data for statistical comparison between treatments.

## Resource-Directed Nutrient Allocation

When damp cellulosic resources (filter paper baits) are added to colonies, PCSI reveals dramatic changes in nitrogen allocation:

- Marked accumulation of ¹⁴C-AIB at the resource site
- Tight focusing of growth toward the new resource
- Strong alignment between the nutrient displacement vector and the resource direction
- These effects are sustained and pronounced with real cellulosic resources

Damp glass-fibre "resources" produce more variable and often transient responses, suggesting that the nutrient content of the resource drives the allocation response.

## Pulsatile Transport Phenomena

Superimposed on the longer-term translocation trends, PCSI reveals a strong pulsatile component in solute transport, particularly through corded systems. Fourier analysis of time-series data from individual pixels or regions of interest reveals oscillatory behaviour with distinct frequency, amplitude, and phase characteristics. These pulsatile signals can continue for 5–7 days after tracer loading.

## Extended Microcosm Studies

Modified PCSI protocols allow measurements from more realistic microcosms with wood-block inocula and sand or soil substrata overlaid with translucent scintillation screens. In these systems, ¹⁴C-AIB dynamics have been continuously imaged for periods exceeding 6 weeks, revealing complex sequences of shifts in nitrogen distribution and transport priority as the network develops.

Key findings from extended microcosm studies include:

- **Rapid long-distance transport**: ¹⁴C-AIB can travel 250 mm along major cords within 1 hour of loading
- **Asynchronous cord activation**: not all cords transport simultaneously; some show delayed activation ("route-switching")
- **Transient transport routes**: some cords function as transport pathways only temporarily, with signal declining after 30 hours
- **Multi-phase filling**: subsidiary cords may show two distinct phases of transport activity

## Route-Switching and Transport Prioritization

One of the most striking observations from extended PCSI studies is the phenomenon of "route-switching," where a pre-existing cord that initially showed no tracer movement later becomes transiently labelled and active. This suggests that the mycelial network dynamically reconfigures its transport pathways, potentially redirecting nutrient flows toward regions of highest demand or away from depleted sources. The ability to switch between alternative routes may represent an important adaptation for optimizing resource distribution in heterogeneous soil environments.

## Ecological and Agricultural Significance

The transport phenomena revealed by PCSI have important implications for understanding fungal ecology in agricultural and natural systems:

- **Wood decomposition dynamics**: the ability to rapidly channel nutrients over centimetre-to-metre distances explains how cord-forming fungi dominate wood decomposition in forest soils
- **Soil nutrient redistribution**: fungal networks serve as major conduits for moving nitrogen and other nutrients between spatially separated organic resources
- **Foraging efficiency**: the shift from symmetric to asymmetric growth, combined with resource-directed allocation, maximizes the efficiency of resource capture
- **Network resilience**: route-switching and multi-pathway transport provide redundancy that maintains nutrient distribution even when parts of the network are damaged
- **Compost and soil management**: understanding fungal transport mechanisms can inform practices that promote beneficial saprotrophic networks for organic matter decomposition [[mollison-designers-fish-pond-fertiliser-and-nutrient-cycling]]

## Technical Considerations and Limitations

Several technical challenges are inherent to PCSI methodology:

- **Imaging constraints**: PCSI precludes simultaneous bright-field imaging because the white mycelium lacks contrast against the white scintillation screen, necessitating automated image processing algorithms for colony delineation
- **Substrate limitations**: early experiments used simple agar substrata; extension to soil and sand microcosms required translucent scintillation screens that introduce some optical attenuation
- **Tracer specificity**: while AIB is non-metabolized, it only tracks amino acid transport pathways; other nutrients (sugars, minerals, phosphates) may follow different translocation routes
- **Spatial resolution**: the technique resolves transport at the colony and cord level but cannot resolve subcellular transport within individual hyphae
- **Quantitative calibration**: converting photon counts to absolute tracer concentrations requires careful attenuation correction and background subtraction

Despite these limitations, PCSI has provided unprecedented insights into fungal nutrient dynamics that were previously inaccessible, and continues to be refined for more ecologically realistic experimental conditions.

## Future Directions

Ongoing work is extending PCSI approaches to study a broader range of fungal species beyond *P. velutina*, including ectomycorrhizal and pathogenic fungi. Integration with complementary techniques — such as confocal microscopy for subcellular transport, and network graph analysis for colony-level organization — promises to bridge the gap between cellular and ecosystem scales of fungal nutrient dynamics.

## See Also

- [[vacuolar-nutrient-transport-in-fungi]]
- [[pulsatile-nutrient-transport-fungal-mycelia]] in Fungal Mycelia
- Fungal [[fungal-mycelial-network-analysis]]

## See Also

- [[photon-counting-scintillation-imaging]]
- [[isotopic-tracers-mycorrhizal-research]]
- [[fungal-biology-fundamentals]]
