# Mycelial Network Nutrient Transport and Imaging

## Overview
Understanding how nutrients move through fungal [[decomposition]] in forest ecosystems.
These approaches have revealed that nutrient transport in mycelia involves pulsatile fluxes,
phase-synchronized oscillations, and adaptive network architectures that dynamically
reconfigure in response to resource discovery.

## The Vacuolar System as a Transport Organ
The vacuolar system in filamentous fungi has been proposed as an important organ for long-
distance translocation over millimetres or centimetres within individual hyphae. Vacuolar
morphology changes systematically along individual hyphae, creating distinct transport zones.
Near the hyphal tip, the vacuole appears as a complex reticulum of fine tubes interspersed with
small spherical vacuoles, forming a highly interconnected network well suited for distributing
materials to the growing apex. Progressing distally from the tip, this transitions through
larger, more spherical adherent vacuoles interconnected by fine tubes, to a series of discrete,
larger vacuoles near the hyphal base that act as storage compartments.
This morphological gradient from reticulate to discrete vacuoles has important implications for
transport capacity. The tubular reticulum near the tip provides a high-conductance pathway that
can rapidly supply materials to the extending apex, while the larger discrete vacuoles in sub-
apical regions serve as reservoirs that can buffer nutrient supply during periods of variable
external availability. The continuity of the vacuolar system across septal pores---facilitated
by narrow connecting tubes that traverse the septa---allows for long-distance movement of
solutes that would be prohibitively slow through the cytoplasm alone.

## FRAP Measurements of Oregon Green Diffusion
To quantify movement through the vacuolar system, researchers use fluorescence recovery after
photobleaching (FRAP) with the fluorescent dye Oregon Green (OG). The vacuole lumen is labelled
with carboxy-DFFDA, which is de-esterified within the vacuole and trapped there. Confocal laser
scanning microscopy then images individual septal compartments at high spatial and temporal
resolution. A brief, high-intensity illumination pulse photobleaches the fluorescent dye in a
defined region, and the rate of fluorescence recovery is monitored, providing a direct measure
of solute movement from adjacent parts of the vacuole into the bleached zone.
The vacuolar diffusion coefficient (Dv) of Oregon Green in vivo was estimated by FRAP of half a
large, isolated vacuole using rapid confocal imaging. Values obtained in vivo compared
favourably with theoretical and experimental values for fluorescein in pure water, suggesting
that OG was freely diffusible in a largely aqueous vacuole lumen. This established that the
vacuolar system offers relatively low resistance to molecular movement, at least for small,
uncharged solutes like amino acid analogues. With a known Dv, the functional tube diameter
between two connected vacuoles was estimated by FRAP, assuming diffusion-only transport through
the narrow connecting tube. Functional tube diameters determined in vivo ranged from 0.24 to
0.48 micrometres, consistent with EM estimates of approximately 0.3 micrometres.

## Monte Carlo Simulations of Diffusive Transport
To estimate transport characteristics of an entire septal compartment, the measured values of
Dv and median tube diameter were combined with measured distributions of vacuole length, width,
and separation to construct an in silico vacuole system. These computational models were run
with constant boundary conditions at the two ends of the filament, and the steady-state flux
recorded. This yielded an effective diffusion coefficient for the whole compartment via Fick's
first law, where a reduction factor measures the decrease in diffusion caused by including many
vacuoles and tubes of smaller diameter relative to a uniform vacuole.
One thousand Monte Carlo simulations were conducted for each compartment type. For the tubular
vacuole region near the hyphal tip, the data were well described by a model including a well-
connected tubular component and a smaller immobile vesicle phase. Diffusion alone was
sufficient to explain observed transport in all vacuolar regions. Preliminary analysis suggests
an unbranched hypha with a continuous tubular vacuole could sustain tip growth over
approximately 12 to 24 mm. Conversely, diffusion alone in a maximally branched system would
operate over only a few millimetres. The range of simulated effective diffusion coefficients
varied by orders of magnitude, raising the possibility that the vacuolar system could be
dynamically regulated to change its translocation capacity according to local nutrient
conditions.

## Radiolabelled Amino Acid Tracking with PCSI
To measure transport at the millimetre to centimetre scale across whole mycelial networks,
researchers developed photon-counting scintillation imaging (PCSI), a novel non-invasive
technique to track movement of 14C-labelled nitrogen compounds. [[phanerochaete-velutina]] networks of 300 to 500 main nodes, the average node degree stabilized
at around 3.5 after excluding degree-2 nodes left on the main connecting cords. Betweenness
centrality identifies nodes that act as critical bridges, whose removal would most disrupt
transport through the network.

## Resilience Testing via Node and Edge Removal
Network resilience was assessed in silico by measuring how network properties changed as
individual nodes or links were removed randomly or in a targeted manner. The same approach was
applied to model networks (Delaunay triangulation, relative neighbourhood graph, minimum
spanning tree) for comparison. The fungal network showed greater resilience than the minimum
spanning tree but less than the fully connected Delaunay triangulation. In real mycelial
networks, the probability of node or edge removal is unlikely to be random and may show
correlation between adjacent nodes, as grazing by soil invertebrates targets specific palatable
regions. Part of the resilience of such biological networks may not be just the architecture
prior to damage, but the ease and efficiency with which the network can reconnect itself
through growth, branching, and fusion---distinguishing biological networks from their abstract
mathematical analogues.

## See Also
- [[fungal-ecology-and-decomposition]]
- [[fungal-ecology-and-decomposition]]

## Source
- Gadd, Watkinson & Dyer (eds). *Fungi in the Environment*. Cambridge University Press, 2007.
