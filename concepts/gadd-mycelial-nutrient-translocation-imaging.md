---
title: Mycelial dighton-fungal-nutrient-translocation-element-redistribution Imaging
tags:
  - mycology
  - nutrient-translocation
  - imaging
  - basidiomycetes
  - mycelial-networks
  - scintillation-imaging
  - network-analysis
  - cord-forming-fungi
date: 2026-04-28
updated: 2026-04-28
sources:
  - Gadd, G.M., Watkinson, S.C. & Dyer, P.S. (2007) Fungi in the Environment. Cambridge University Press. Chapter 1 by Bebber, Tlalka, Hynes, Darrah, Ashford, Watkinson, Boddy & Fricker, pp. 3-21.
created: 2026-05-07
type: concept
---

# Mycelial Nutrient Translocation Imaging

## Overview

Basidiomycete mycelia form extensive networks that scavenge, sequester, and redistribute nutrients across metres of soil. Understanding how nutrients move through these networks requires techniques spanning micrometre to metre length scales. Research on [[gadd-mathematical-modelling-fungal-mycelia|mathematical modelling of fungal mycelia]] has been advanced by innovative imaging approaches that track nutrient translocation in real time, revealing complex pulsatile transport, route-switching, and emergent network-level coordination.

## The Challenge of Scale

[[mycelial-network-nutrient-transport-imaging-gadd]] in fungal mycelia occurs across an enormous range of length scales: from uptake by individual transporter proteins in hyphal membranes, through translocation within septal compartments via the [[gadd-colony-morphogenesis-hyphal-growth|Phanerochaete velutina]]:
- **Distal compartments**: Large, discrete vacuoles connected by fine tubes
- **Intermediate compartments**: Mix of vacuoles and tubular elements
- **Tip compartments**: Dense tubular reticulum with small vesicles

### Modelling Diffusive Capacity

By combining measured diffusion coefficients with distributions of vacuole size and separation, in silico models of entire septal compartments were constructed. Monte Carlo simulations yielded effective diffusion coefficients for each compartment type. Applying Fick's first law with estimates of nitrogen demand at the tip and vacuolar nitrogen concentration revealed that an unbranched hypha with a continuous tubular vacuole could sustain growth over 12 to 24 mm, while a maximally branched system would support transport over only a few millimetres. This poise suggests the vacuolar system coordinates [[gadd-hyphal-tip-growth-and-branching-mechanisms]] and branching by regulating its translocation capacity in response to local nutrient conditions.

## Photon-Counting Scintillation Imaging (PCSI)

At the millimetre to centimetre scale, researchers developed a novel non-invasive technique to track radiolabelled 14C-amino-isobutyrate (14C-AIB) movement in [[fungal-mycelial-networks-nutrient-translocation]] growing over inert scintillation screens. PCSI provides continuous, real-time imaging of [[mollison-designers-legume-tree-inoculation-and-nitrogen-distribution]] without [[fungal-destructive-sampling-herbarium-dna-extraction]].

### Colony Development Phases

Analysis of 14C-AIB distribution and colony growth revealed two developmental phases:
- **Phase 1**: Symmetrical growth with near-uniform nitrogen distribution
- **Phase 2**: Transition to sparser, asymmetric growth with selective nutrient allocation

The transition between phases depends on [[ph-and-nutrient-availability-garden-soils]] and colony age. Added cellulosic resources induce a rapid shift to focused nitrogen accumulation and asymmetric growth directed toward the new resource.

### Pulsatile Transport

Superimposed on the net translocation pattern, a pronounced pulsatile component was discovered, particularly in corded systems. Fourier analysis of pixel-by-pixel time series produced colour-coded maps of frequency, amplitude, and phase that revealed distinct phase domains: signals from assimilatory hyphae at the inoculum, foraging hyphae, and hyphae at new resources all oscillated but were out of phase with each other, forming locally synchronized regions.

### Route-Switching

In larger sand microcosms, not all cords transported simultaneously. Some cords showed delayed activation—a phenomenon termed "route-switching"—where previously inactive cords became transient [[the-apoplastic-symplastic-and-transcellular-transport-pathways]] before signal declined again. Other cords exhibited multiple filling phases at different times. This dynamic routing behaviour suggests sophisticated regulation of transport pathway selection.

## Network Analysis at the Centimetre to Metre Scale

To understand how the architecture of corded networks supports [[ingham-mycorrhizal-fungi-nutrient-transport-colonization]], graph-theoretic network analysis was applied. Cords were represented as links connecting nodes at branch points and anastomoses, and wood resources served as hub nodes with many connections.

### Network Measures

Key metrics included minimum path length, network diameter, degree distribution, clustering coefficient, and topological indices (alpha, beta, gamma). Fungal networks were compared against model networks generated by Delaunay triangulation (highly connected), relative neighbourhood graphs, and minimum spanning trees (least connected).

### Resilience Assessment

In silico removal of nodes and links revealed that fungal networks show intermediate resilience compared to model networks. The capacity for self-repair through hyphal regrowth may confer advantages over random networks in the cost and efficiency of reconnection after damage.

### Dynamic Network Evolution

[[mycelial-network-architecture]] is not static: initial proliferation produces many links, followed by selection and reinforcement of a subset into strong cords, and eventual regression of the remainder to leave a sparser, more efficient network. The average node degree stabilizes at approximately 3.5 after excluding residual degree-2 nodes on main connecting cords.

## Current Limitations and Future Directions

A complete anatomical description of how transport pathways map onto individual hyphae within differentiating cords remains elusive, even with confocal microscopy, when structures are in their natural dry state. Serial EM sectioning with 3D reconstruction may address this gap. The immense plasticity of [[fungal-pulsatile-nutrient-transport-mycelial-networks]] also makes quantitative comparisons between experiments challenging, requiring sophisticated analytical approaches to accommodate colony-level variability.

## See Also

- [[gadd-mathematical-modelling-fungal-mycelia|Mathematical Modelling of Fungal Mycelia]]
- [[gadd-colony-morphogenesis-hyphal-growth|Colony Morphogenesis and Hyphal Growth]]
- [[gadd-fungal-ecology-saprotrophs|Fungal Ecology: Saprotrophs]]
