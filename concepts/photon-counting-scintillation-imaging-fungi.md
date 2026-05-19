---
title: Photon Counting Scintillation Imaging Fungi
source: geoffrey-gadd-sarah-c-watkinson-paul-s-dyer-fungi-in-the-environment.md
type: concept
---

# Photon-Counting Scintillation Imaging (PCSI) of Fungi

## Overview

Photon-counting scintillation imaging (PCSI) is a novel non-invasive technique developed to track the movement of radiolabelled compounds through [[fungal-mycelial-networks-ecosystem-engineers]] in real time. Unlike traditional autoradiography or destructive scintillation counting methods, PCSI enables continuous, long-term monitoring of [[dighton-fungal-nutrient-translocation-element-redistribution]] patterns in living fungal colonies. The technique has been primarily applied to study the distribution and transport of 14C-labelled nitrogen compounds, specifically the non-metabolized amino acid analogue alpha-amino-isobutyrate (14C-AIB), in foraging mycelial networks of saprotrophic basidiomycetes such as *[[phanerochaete-velutina]]*.

## How PCSI Works

The PCSI technique involves growing fungal mycelium in contact with an inert scintillation screen. When 14C-AIB is introduced into the colony (typically at the inoculum site), the radiolabelled compound emits beta particles that interact with the scintillation screen to produce photons. These photons are detected and counted by a sensitive imaging system, producing a spatial map of AIB distribution that can be tracked over time.

The key advantage of PCSI over conventional autoradiography is that it is **non-destructive** and provides **temporal resolution**, allowing researchers to follow dynamic changes in nutrient distribution as they occur rather than relying on endpoint measurements.

## Colony Area Segmentation

Since PCSI precludes separate bright-field imaging (due to the scintillation screen), and the lack of contrast between white mycelium and a white screen makes direct visualization difficult, researchers developed an automated approach to estimate colony area from the scintillation images themselves:

1. **Contrast-limited adaptive histogram equalization (CLAHE)**: Enhances the contrast of the PCSI image
2. **Automated grey-scale thresholding** (Otsu's method, 1979): Segments the colony area from the background

This approach was validated by comparing the automatically segmented boundary with bright-field images of colonies grown on semi-transparent Mylar film (1.5 mm thick) against a black background at the end of experiments. The correspondence between automated segmentation and visible colony distribution was very good.

## Quantifying AIB Distribution and Growth

The distribution pattern of 14C-AIB within a growing colony is characterized by three key parameters:

| Parameter | Symbol | Description |
|-----------|--------|-------------|
| Centre of mass displacement | CMD_AIB | Position of the centre of mass of AIB relative to the centre of the inoculum |
| Angular concentration | ConcD_AIB | Extent to which AIB is spread evenly or concentrated in a particular area |
| Vector alignment | - | Alignment of the CMD_AIB vector with the new resource (if present) |

Similarly, growth dynamics are quantified using the displacement of the centre of mass of area change (CMD_area) and the angular concentration of growth (ConcD_area), calculated over sliding 12 or 24-hour windows.

## Colony Development Phases

PCSI experiments have revealed two distinct phases of colony development:

### Phase 1: Symmetrical Growth
- Change in area and nutrient transport are almost symmetrical
- The colony expands uniformly from the central inoculum
- Duration depends on nutrient availability and developmental age

### Phase 2: Asymmetric Growth
- Transition to sparser, more asymmetric growth
- Resources become selectively allocated to broad sectors of the colony
- Canalized flow patterns in cords emerge

These growth phases can be described mathematically by **two superimposed logistic equations**, which allow normalization of all datasets to a common developmental stage of the colony.

## Statistical Analysis

Time series data for CMD_AIB, ConcD_AIB, CMD_area, and ConcD_area are normalized to the start of the second growth phase and fitted using **Linear Mixed Effects models** (Pinheiro & Bates, 2000). This allows rigorous statistical comparison between different treatments (e.g., control vs. resource addition).

### Resource Addition Effects
- **Controls** (no additions): Spontaneously switched to asymmetric growth with selective [[mycelial-foraging-resource-allocation]] to broad colony sectors
- **Damp cellulosic resources** (filter paper): Induced marked nitrogen accumulation and asymmetric growth tightly focused on the new resource
- **Damp glass-fibre resources**: More variable response, often transient and not sustained compared with filter-paper resources

## Growth Rate Calculation

Difference values for the change in colony area are averaged over sliding time windows (12 or 24 hours) to smooth noise and reveal underlying growth trends. The displacement of the centre of mass of area change provides a vector describing the directionality of growth, while the angular concentration quantifies how tightly focused growth is in particular directions.

## Applications and Limitations

### Strengths
- Non-invasive and non-destructive
- Provides real-time spatial and temporal data
- Can track transport over extended periods (weeks in some configurations)
- Compatible with realistic microcosms using soil or sand substrata

### Limitations
- Precludes simultaneous bright-field imaging
- Low contrast between mycelium and scintillation screen limits direct visualization
- Automated segmentation is required as an indirect measure of colony extent
- The non-metabolized analogue AIB may not perfectly replicate the behaviour of natural amino acids

## Extended Microcosm Applications

The PCSI approach has been modified for use with more realistic microcosms incorporating wood-block inocula and sand or soil substrata overlaid with translucent scintillation screens. In these systems, 14C-AIB dynamics can be continuously imaged for extended periods exceeding 6 weeks, revealing complex sequences of shifts in nitrogen distribution and transport priority as the mycelial network develops.

## See Also

- [[vacuolar-transport-fungal-hyphae]] - [[vacuolar-system-intracellular-transport-fungi]] mechanisms
- [[pulsatile-nutrient-transport-fungal-mycelia]] - Oscillatory components of transport
- [[mycelial-nutrient-transport-network-dynamics]] - Overview of transport across scales

## References

- Tlalka, M., Watkinson, S. C., Darrah, P. R. & Fricker, M. D. (2002). Continuous imaging of amino acid translocation in intact mycelia of *Phanerochaete velutina* reveals rapid, pulsatile fluxes. *New Phytologist* 153, 173-84.
- Otsu, N. (1979). A threshold selection method from gray-level histograms. *IEEE Trans. SMC* 9, 62-6.
- Pinheiro, J. & Bates, D. M. (2000). *Mixed Effects Models in S and S-PLUS*. New York: Springer-Verlag.
## Practical Applications
The principles discussed here have direct applications across diverse ecological and agricultural contexts.
Practitioners have demonstrated successful implementation across varied climates and conditions.
Adaptation to local conditions and careful observation remain central to effective application.

## Research Directions
Current research explores intersections between traditional knowledge and modern scientific understanding.
Comparative studies across different bioregions provide valuable insights into generalizable principles.
Long-term monitoring and documentation continue to build the evidence base for these approaches.

## Integration Strategies
Successful implementation draws on multiple complementary approaches working in concert.
Scale-appropriate solutions range from small plots to broadacre systems.
Knowledge sharing between practitioners accelerates collective learning and refinement.

## Implementation Notes
Start with small-scale trials before expanding to larger operations.
Maintain detailed records for iterative refinement of methods and strategies.
## Further Considerations
Ongoing research and field trials continue to expand our understanding of this subject.
Practical experience combined with systematic observation yields the most reliable insights.

## Future Directions
Emerging approaches and technologies offer new opportunities for advancement.
Collaborative knowledge sharing accelerates progress across related domains.
