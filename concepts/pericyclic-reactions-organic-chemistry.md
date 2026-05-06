---
title: Pericyclic Reactions
created: 2026-04-28
updated: 2026-05-06
aliases: [electrocyclic reactions, cycloaddition, sigmatropic rearrangement, woodward-hoffmann rules, orbital symmetry]
tags: [chemistry, organic-chemistry, reaction-mechanism, orbital-theory, synthesis]
type: concept
sources: []
---

## Overview

Pericyclic reactions are a fundamental class of organic reactions that proceed through a single
concerted cyclic transition state, meaning all bond-breaking and bond-forming events occur
simultaneously through a continuous cyclic overlap of orbitals. They involve no discrete
intermediates, no charged species, and no catalysts. The defining characteristic is a cyclic
array of interacting molecular orbitals connecting the reacting centers. Pericyclic reactions
are among the most stereospecific transformations in organic chemistry and are governed by the
principle of orbital symmetry conservation.

## Classification

Pericyclic reactions fall into four main categories based on the topology of bond reorganization:

**Electrocyclic reactions** are intramolecular processes where a sigma bond forms or cleaves at
the termini of a conjugated pi system, changing ring size by one. The number of pi electrons
(4n or 4n+2) determines whether ring closure proceeds via conrotatory or disrotatory motion.

**Cycloadditions** involve two or more pi systems combining to form a new ring, with two new
sigma bonds forming simultaneously. They are described by component electron counts in brackets
notation, such as [4+2] for the Diels-Alder reaction or [2+2] for photocycloadditions.

**Sigmatropic rearrangements** involve migration of a sigma bond across a conjugated pi system,
where one sigma bond breaks and another forms simultaneously, described using [i,j] notation.

**Group transfer reactions** involve concerted transfer of a group between molecules in a cyclic
fashion. These are rare and often subsumed under cycloaddition frameworks. Cheletropic reactions,
a subtype where two bonds are made or broken to a single atom, are sometimes classified separately.

## Woodward-Hoffmann Rules and Orbital Symmetry

The Woodward-Hoffmann rules (1965-1969), developed by Robert B. Woodward and Roald Hoffmann,
establish the theoretical foundation through the conservation of orbital symmetry. The symmetry
properties of molecular orbitals must be conserved as reactants transform into products along
the reaction coordinate.

A pericyclic reaction is thermally allowed if the total number of (4q+2)s + (4r)a components is
odd, where s denotes suprafacial (same face) and a denotes antarafacial (opposite face) components.
Systems with 4n pi electrons require antarafacial overlap thermally but suprafacial photochemically.
Systems with 4n+2 pi electrons require suprafacial overlap thermally but antarafacial photochemically.

Dewar and Zimmerman's aromatic transition state theory provides an equivalent formulation. Allowed
reactions proceed through aromatic transition states: Huckel aromatic for 4n+2 electrons with all
suprafacial components, and Mobius aromatic for 4n electrons with one antarafacial component.

## Frontier Molecular Orbital Theory

Kenichi Fukui's frontier molecular orbital theory (1952) focuses on the interaction between the
HOMO of one reactant and the LUMO of another. For pericyclic reactions, the symmetry of the
HOMO dictates stereochemical outcomes under thermal conditions, while photochemical excitation
inverts frontier orbital symmetry and reverses selection rules. In electrocyclic reactions, the
phase relationship of terminal HOMO lobes determines whether conrotatory or disrotatory motion
is required. Same-phase termini favor disrotation; opposite-phase termini favor conrotation.

## Thermal and Photochemical Selectivity

UV excitation promotes an electron from HOMO to LUMO, inverting frontier orbital symmetry and
reversing all selection rules. The same starting material can yield completely different
stereoisomeric products depending on whether it is heated or irradiated with UV light. For
electrocyclic reactions, 4n systems undergo conrotatory closure thermally and disrotatory
photochemically, while 4n+2 systems undergo disrotatory closure thermally and conrotatory
photochemically. The butadiene-cyclobutene (4 pi) and hexatriene-cyclohexadiene (6 pi)
interconversions are the classic illustrative examples.

## Electrocyclic Reactions in Detail

The butadiene to cyclobutene conversion (4 pi electrons) illustrates the principles. Thermally,
the HOMO of butadiene (psi-2) has opposite-phase lobes at C1 and C4, requiring conrotation.
From trans,trans-2,4-hexadiene, thermal ring closure yields trans-3,4-dimethylcyclobutene.
Photochemically, the excited-state HOMO (psi-3) has same-phase termini, enabling disrotation
and producing the cis-dimethyl isomer. The hexatriene to cyclohexadiene conversion (6 pi
electrons) reverses the pattern: thermal disrotatory closure, photochemical conrotatory closure.
These reactions are completely stereospecific.

## Cycloadditions

The Diels-Alder reaction, discovered by Diels and Alder (Nobel Prize 1950), combines a conjugated
diene (4 pi electrons) with a dienophile (2 pi electrons) to form a six-membered ring in a
concerted suprafacial-suprafacial [4+2] cycloaddition. Stereospecificity is complete: cis-
dienophiles yield cis-substituted cyclohexenes, and trans-dienophiles yield trans-substituted
products. Endo selectivity arises from secondary orbital interactions between dienophile
substituent pi orbitals and the diene pi system, making the endo transition state kinetically
favored despite the exo product being thermodynamically more stable. Regioselectivity follows
frontier orbital coefficient magnitudes: the largest HOMO coefficient on the diene pairs with
the largest LUMO coefficient on the dienophile under normal electron demand.

Thermal [2+2] cycloadditions are symmetry-forbidden, but photochemical [2+2] cycloadditions are
allowed and widely used. UV-induced thymine dimer formation in DNA is a biologically significant
example. 1,3-Dipolar cycloadditions are thermally allowed [4+2] processes including the Huisgen
cycloaddition of azides and alkynes to form triazoles, and nitrone cycloadditions producing
isoxazolidines reducible to amino alcohols.

## Sigmatropic Rearrangements

The Cope rearrangement is a [3,3]-sigmatropic reaction of 1,5-dienes thermally allowed through
a chair-like cyclic transition state strongly preferred over the boat alternative. The oxy-Cope
rearrangement, with a hydroxyl group at the 3-position, is accelerated by 10^10 to 10^17 due to
enolate formation in the transition state. The Claisen rearrangement converts allyl vinyl ethers
to gamma,delta-unsaturated carbonyl compounds through a chair-like transition state with complete
transfer of allylic stereochemistry. Major variants include the Ireland-Claisen (ester enolates),
Johnson-Claisen (triethyl orthoacetate), and Eschenmoser-Claisen (dimethylacetamide dimethyl
acetal), each providing stereocontrolled C-C bond formation. [1,5]-Hydride shifts are thermally
allowed suprafacial migrations in pentadienyl systems, while [1,3]-hydride shifts are thermally
forbidden due to geometrically impossible antarafacial hydrogen migration requirements.

## Applications in Natural Product Synthesis

Pericyclic reactions are indispensable in total synthesis. Nicolaou's biomimetic endiandric
acids synthesis (1982) featured a cascade of electrocyclic ring openings, [1,7]-hydride shifts,
and an intramolecular Diels-Alder from a single polyunsaturated precursor. Corey employed
Diels-Alder reactions to construct the prostaglandin bicyclic core. Woodward's cholesterol and
cortisone syntheses used Diels-Alder methodology before the theoretical framework existed. Both
Holton and Nicolaou used Diels-Alder reactions in their taxol syntheses. Claisen rearrangements
install chiral quaternary centers in alkaloid and terpene synthesis.

## Historical Development

Fukui published frontier orbital theory in 1952, initially underappreciated outside Japan. In
1965, Woodward and Hoffmann published their seminal JACS paper on electrocyclic stereospecificity,
motivated by unexplained outcomes in Woodward's vitamin B12 synthesis. The Conservation of
Orbital Symmetry monograph appeared in 1969. Dewar and Zimmerman developed the aromatic transition
state formulation in 1969-1971. The 1981 Nobel Prize was awarded jointly to Hoffmann and Fukui;
Woodward had died in 1979. The Diels-Alder reaction dates to 1928, Cope to 1940, Claisen to 1912.

## Modern Computational Validation

DFT calculations (B3LYP/6-31G(d)) routinely locate transition states predicted by Woodward-
Hoffmann rules. Activation barriers for allowed reactions are 15-30 kcal/mol, while forbidden
counterparts exceed 50 kcal/mol. Dynamic studies by Singleton revealed hidden stepwise
intermediates on ultra-short timescales, though orbital symmetry rules still predict observed
stereospecificity. Houk identified ambimodal transition states leading to two product distributions
from a single TS. Machine learning models now predict pericyclic outcomes with high accuracy.

## See Also

- [[bioremediation-fenton-chemistry-brown-rot-fungi]]
- [[cervantes-compost-tea-organic-brewing]]
- [[hamilton-organic-seed-saving-propagation]]

- molecular orbital theory — Quantum mechanical foundation for orbital symmetry analysis
- aromaticity huckel rule — Hückel's 4n+2 rule applied to transition state aromaticity
- heterocyclic chemistry — Related nitrogen-containing heterocycle ring chemistry
- named organic reactions — Broader catalog of named organic chemistry transformations
- retrosynthetic analysis — Strategic use of pericyclic reactions in synthesis planning
