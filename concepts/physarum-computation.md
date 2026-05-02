---
title: Physarum Computation
tags: [biology, computing, slime-mold, optimization, unconventional-computing]
date: 2026-04-28
updated: 2026-04-28
sources: [/Users/t3rpz/wiki/raw/papers/unknown-mycelium-running.md]
---

# Physarum Computation

Physarum computation uses the slime mold *Physarum polycephalum* as a biological
computing substrate. Despite being a single-celled organism (a plasmodial slime
mold), *Physarum* exhibits remarkable problem-solving abilities that have made it
a model organism in [[unconventional-computing]] research. Its ability to solve
complex spatial problems through simple physical processes has attracted
attention from mathematicians, computer scientists, and biologists alike.

## Biology of Physarum

*Physarum polycephalum* exists in its vegetative phase as a large, single,
multinucleate cell called a plasmodium. It spans up to several square meters in
the wild and consists of a branching network of vein-like tubes that shuttle
cytoplasm back and forth via rhythmic contractions (peristalsis). Key biological
features relevant to computation include:

- **Cytoplasmic streaming**: Shuttle streaming of cytoplasm at ~1 mm/s
  distributes nutrients and signals across the organism. The streaming is
  driven by rhythmic contractions of the tube walls at intervals of
  approximately 1-2 minutes.
- **Tubular network**: The vein network dynamically remodels, thickening
  productive routes and thinning unused ones. This self-optimization is driven
  by positive feedback: higher flow increases tube diameter, which increases
  flow further.
- **Chemotaxis**: The plasmodium moves toward food sources (attracted to
  sugars, amino acids) following chemical gradients with impressive precision.
- **Phototaxis**: It avoids light (specifically blue and UV wavelengths),
  allowing optical signals to steer growth and network remodeling.
- **Thermotaxis**: Temperature gradients also influence migration and growth
  direction, providing another input channel.

## Classic Experiment: Tokyo Rail Network

In a celebrated 2010 study by Toshiyuki Nakagaki and colleagues, *Physarum* was
placed on a map of the greater Tokyo area with oat flakes at the locations of
36 major cities. Over 26 hours, the slime mold restructured its body into a
network that closely matched the existing Tokyo rail infrastructure — achieving
comparable efficiency to the human-engineered system at a cost of roughly 1.5×
the theoretical minimum transport cost.

The match was not exact but was strikingly close, particularly in the retention
of key connections and the elimination of redundant routes. This experiment has
been replicated for other cities including Barcelona, London, and Canadian
highway networks.

## Computational Capabilities

### Maze Solving
*Physarum* can find the shortest path through a maze by filling it entirely,
then pruning dead-end tubes as cytoplasm concentrates on the shortest route.
This was first demonstrated by Nakagaki et al. in 2000, when the organism
solved an 8×8 maze connecting two food sources through the shortest path.

### Network Design
Beyond the Tokyo experiment, *Physarum* has approximated optimal designs for
highway networks in the Iberian Peninsula, Canada, and the United Kingdom. The
algorithm used by the organism naturally minimizes total transport cost while
maintaining robustness against link failures — a multi-objective optimization
problem that is computationally expensive to solve conventionally.

### Logical Operations
Researchers have constructed AND, OR, NOT, and XOR gates using combinations of
food sources and light stimuli. Cascading these gates enables basic Boolean
circuits. The inputs are typically oat flakes (representing TRUE) and their
absence (representing FALSE), with light barriers as control signals.

### Memory
The organism exhibits habituation: repeated exposure to a harmless stimulus
(like light) causes a decreasing response, and this "memory" persists for
hours. This has been proposed as a form of [[biological-memory-non-neural]].
Critically, the habituation can be "refreshed" by a gap between stimulations,
paralleling the spacing effect in human learning.

## Mathematical Models

The behavior of *Physarum* can be described by the **Physarum solver**, a
mathematical model that simulates the organism's adaptive network dynamics:

1. Each tube has a conductivity that changes based on flow rate.
2. Flow follows a pressure gradient (analogous to Kirchhoff's laws for
   electrical circuits).
3. Tubes carrying more flow increase in conductivity (positive feedback).
4. Tubes carrying less flow shrink (negative feedback / decay).

This model has been applied to solve minimum spanning tree problems,
steiner tree problems, and network flow optimization. The solver
converges to near-optimal solutions without any explicit optimization objective
— the behavior emerges from local interaction rules.

## Limitations

- Results are probabilistic — repeated runs produce varying solutions.
- No native arithmetic or symbolic processing capability.
- Environmental sensitivity makes reproducibility challenging.
- Scaling to arbitrarily large problems is constrained by physical size.
- The organism requires constant moisture and nutrient supply.
- Computation speed is limited by biological growth rates.

## See Also

- [[mycelial-network-computation]]
- biological computing
- [[unconventional-computing]]
- minimum spanning tree
- [[bio-electronic-interfaces]]
