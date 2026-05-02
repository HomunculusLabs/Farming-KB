---
title: Slime Mold Computation and Biological Problem Solving
tags: [mycology, computational-biology, emergent-behavior, protistology]
date: 2026-04-28
updated: 2026-04-28
sources: [/Users/t3rpz/wiki/raw/papers/unknown-mycelium-running.md]
---

# Slime Mold Computation and Biological Problem Solving

Slime molds, particularly the plasmodial slime mold [[physarum-polycephalum]],
have emerged as powerful unconventional computing substrates. Despite lacking a
brain, nervous system, or any centralized control, these single-celled organisms
solve spatial optimization problems that challenge algorithmic approaches. Their
ability to find efficient paths, construct robust networks, and make adaptive
decisions has attracted interest from fields ranging from computer science to
urban planning.

## Physarum Polycephalum Biology

Physarum polycephalum is a large, multinucleate amoeboid organism that exists
in two main life stages. The plasmodial stage -- a single giant cell
containing millions of nuclei -- is the active, foraging form. It ranges from
a few millimeters to over a meter in diameter, forming an intricate network
of vein-like tubes that distribute nutrients and shuttle protoplasmic fluid.

The organism moves by extending frontal pseudopods at its leading edge while
retracting tubes at the rear. Cytoplasmic streaming within the tubes creates
alternating flow patterns driven by oscillatory contractions of the tube
walls. These contractions occur at approximately 1 to 2 minute intervals and
propagate as peristaltic waves, creating a decentralized pump that circulates
nutrients throughout the plasmodium without any central coordination.

## Network Optimization

The most celebrated demonstration of slime mold computation involves the
Tokyo rail network experiment. In 2010, researchers at Hokkaido University
placed oat flakes representing major Tokyo stations on a wet surface and
introduced a Physarum plasmodium. Over 26 hours, the organism reorganized
its tubular network into a pattern strikingly similar to the existing Tokyo
rail system, including many of the same shortcuts and efficiency optimizations
that human engineers had designed over decades.

The slime mold's algorithm is elegantly simple: tubes carrying more nutrients
grow thicker, while underutilized tubes shrink and eventually disappear. This
positive feedback loop -- reinforced by the organism's tendency to pump fluid
through wider tubes at higher rates -- naturally amplifies efficient routes
and prunes redundant ones. The result is a minimum-cost network that balances
transport efficiency against the metabolic cost of maintaining tube volume.

## Shortest Path Computation

Physarum consistently finds the shortest path between two food sources in
labyrinth mazes. When placed in a maze with food at the entrance and exit,
the plasmodium initially explores all corridors. Once both food sources are
connected, the organism concentrates cytoplasmic flow along the shortest
path and withdraws from dead-end corridors.

This behavior can be modeled mathematically. The Physarum solver, formalized
by Tero, Kobayashi, and Nakagaki in 2007, represents tube conductivity as a
variable that increases with flux and decreases with a decay term. Iterating
this model converges on the shortest path in polynomial time, providing a
biologically inspired algorithm for graph optimization problems.

## Steiner Tree Problem

The Steiner tree problem -- finding the minimum-length network connecting a
set of points with the option to add intermediate (Steiner) points -- is
NP-hard for classical algorithms. Physarum approximates solutions
efficiently. When presented with three or more food sources arranged in a
triangle or polygon, the organism constructs a network with Steiner-like
junctions that minimize total tube length while maintaining connectivity.

The quality of these biological solutions is remarkable. For simple
configurations, Physarum finds exact Steiner tree solutions. For complex
arrangements, its solutions are typically within a few percent of the known
optimal, comparable to the best heuristic algorithms. This has inspired
"Physarum-inspired" optimization algorithms applied to network design, VLSI
routing, and supply chain logistics.

## Decision Making and Habituation

Beyond spatial problems, Physarum demonstrates basic forms of decision making
and learning. When presented with a choice between food sources of different
quality, the organism allocates proportional biomass -- favoring richer
sources but maintaining connections to poorer ones as backup options. This
risk-spreading behavior mirrors portfolio optimization strategies in finance.

Physarum also exhibits habituation, a simple form of learning. When
repeatedly exposed to an aversive stimulus (such as a bitter compound or
light), the organism's avoidance response diminishes over time. If the
stimulus is removed and then reintroduced after a rest period, the
habituated response recovers. Remarkably, fusion experiments show that
habituated individuals can "teach" naive individuals -- when a habituated
plasmodium fuses with an untrained one, the combined organism displays the
habituated response.

## Hybrid Bio-Computing Systems

Researchers have developed hybrid systems that use living Physarum as a
computational component. One approach interfaces the organism with electronic
sensors: the organism's electrical resistance changes as it grows and
contracts, providing a measurable output signal. By encoding problem
parameters in the spatial arrangement of food or repellents, the organism's
growth pattern becomes the computed solution.

Another approach uses Physarum to route electrical circuits. The organism
grows preferentially along conductive paths, effectively solving maze
problems in hardware. After growth, the biological template is replaced with
metal traces, creating physical circuits whose layout was "designed" by the
slime mold. These bio-fabricated circuits have been used to create simple
logic gates and memory elements.

## Theoretical Implications

Slime mold computation challenges conventional definitions of intelligence.
The organism's problem-solving abilities emerge from local interactions
between simple components -- tube contractions, fluid dynamics, and chemical
gradients -- without any global representation of the problem. This is
embodied computation: the computation is not separate from the organism but
is the organism.

The field intersects with research on [[fungal-intelligence]], ant colony
optimization, and cellular automata. Together, these systems demonstrate that
complex computation does not require complex architectures. Decentralized,
embodied systems can solve problems that centralized systems struggle with,
particularly in noisy, dynamic environments. See also [[mycelial-network-communication]] and biological computation.

## See Also

- [[biological-slime-mold-computing]]
- [[myxomycete-mycetozoan-slime-mold-diversity-ecology]]
- [[oyster-mushroom-green-mold-disease]]
- [[trichoderma-forest-green-mold-guide]]
- [[ultra-low-leaf-mold-as-ideal-soil-model]]
