---
title: Stereochemistry and Chirality
aliases: [stereochemistry, chirality, enantiomers,
optical isomerism, molecular asymmetry]
tags: [chemistry, organic-chemistry, biochemistry,
pharmacology, stereochemistry]
created: 2026-05-02
updated: 2026-05-06
type: concept
sources: []
---
Stereochemistry is the branch of chemistry concerned with the three-
dimensional arrangement of atoms in molecules and how this affects
chemical and biological properties. Chirality -- from the Greek cheir
(hand) -- is the property of an object being non-superimposable on its
mirror image. Louis Pasteur first demonstrated molecular chirality in
1848 by manually separating mirror-image crystals of sodium ammonium
tartrate, showing one rotated light right and the other left. In 1874,
Jacobus van't Hoff and Joseph Le Bel independently proposed the
tetrahedral carbon model, explaining how a carbon with four different
substituents produces two enantiomers. Van't Hoff received the first
Nobel Prize in Chemistry in 1901. The thalidomide tragedy (1957-1961),
causing ~10,000-20,000 birth defects, became the watershed event
transforming chiral chemistry into a regulatory and pharmaceutical
imperative.
## Fundamental Concepts
A stereocenter is any atom where swapping two substituents produces a
stereoisomer. A chiral center produces a non-superimposable molecule,
most commonly a carbon with four different substituents. With n chiral
centers, the maximum number of stereoisomers is 2^n, reduced when meso
forms exist. The Cahn-Ingold-Prelog (CIP) priority rules (1951) assign
absolute configurations as R (rectus) or S (sinister). Priorities
follow atomic number (I > Br > Cl > F > O > N > C > H) with ties
broken recursively. The lowest-priority group is oriented away;
tracing 1-2-3 clockwise gives R, counterclockwise gives S. R/S does
not correlate with optical rotation direction.
Enantiomers are non-superimposable mirror images sharing all physical
properties except optical rotation direction. Diastereomers are
stereoisomers that are not mirror images and have different physical
properties. Meso compounds contain stereocenters but are achiral due
to an internal plane of symmetry (e.g., meso-tartaric acid, 2R,3S). A
racemic mixture (racemate) is a 1:1 enantiomer mix, denoted (+/-) or
rac; it is optically inactive with a typically lower melting point
than either pure enantiomer.
## Notation Systems
Wedge-dash notation uses solid wedges (toward viewer), dashed wedges
(away), and plain lines (in-plane). Fischer projections (Emil Fischer,
1891) place the carbon chain vertically with horizontal bonds
projecting out; rotating 90 degrees inverts the configuration while
180 degrees preserves it. Haworth projections (Walter Haworth, 1929)
depict cyclic sugars as flat rings; for D-sugars, right-side
substituents go down, and alpha-anomers have the anomeric OH down
(trans to CH2OH). The E/Z system (1964) assigns alkene geometry using
CIP priorities: same side = Z (zusammen), opposite = E (entgegen),
unambiguously handling all alkenes.
Optical activity is measured by polarimetry. Specific rotation [alpha]
= alpha_obs / (l * c), with l in dm and c in g/mL, typically at the
sodium D line (589 nm). Enantiomeric excess ee = |%R - %S|;
enantiomeric ratio er relates by ee = (er-1)/(er+1). Pharmaceutical
specifications typically require ee > 98%.
## Conformational Analysis
Newman projections (Melvin Newman, 1952) view conformations along a
C-C bond. Ethane's eclipsed conformation is 3.0 kcal/mol above
staggered due to torsional strain. Butane ranks: anti (180 deg,
reference) < gauche (+/-60 deg, +0.9 kcal/mol) < eclipsed methyl-H
(+/-120 deg, +3.6 kcal/mol) < eclipsed methyl-methyl (0 deg, +6.0
kcal/mol). Cyclohexane adopts chair conformations with ~109.5 degree
bond angles and zero angle strain. Chair flips (barrier ~10.8
kcal/mol) interconvert axial and equatorial positions. A-values
(kcal/mol, equatorial preference): methyl 1.74, ethyl 1.75, isopropyl
2.21, tert-butyl >4.5 (locks chair), phenyl ~3.0, Cl 0.52, Br 0.48, OH
~0.87. These arise from 1,3-diaxial gauche interactions.
## Stereochemistry in Drug Action
Biological systems are homochiral (L-amino acids, D-sugars), so drug
enantiomers interact differently with chiral receptors. (S)-ibuprofen
is the active COX inhibitor; (R)-ibuprofen undergoes ~60% in vivo
inversion to (S) via the acyl-CoA pathway. (S)-citalopram
(escitalopram) is the active SSRI at half the racemic dose. The
thalidomide tragedy: (R)-thalidomide was sedative while
(S)-thalidomide was teratogenic via cereblon binding, causing
phocomelia. The enantiomers racemize in vivo (t1/2 ~2.5-10 hours),
making single-enantiomer formulation unsafe. This led to the 1962
Kefauver-Harris Amendment. Other examples: (S)-warfarin is 3-5x more
potent and is CYP2C9-metabolized; (R)-albuterol is the active
bronchodilator while (S) is pro-inflammatory; naproxen is pure (S)
because (R) is hepatotoxic; levodopa is active while D-DOPA is
inactive.
## Resolution Methods
Classical resolution (Pasteur, 1853) converts racemates to
diastereomeric salts with chiral resolving agents (tartaric acid,
brucine, quinine); fractional crystallization gives max 50% yield.
Chiral HPLC uses chiral stationary phases (polysaccharide derivatives,
cyclodextrins, Pirkle phases) for analytical and preparative
separation. SFC with supercritical CO2 is preferred for large-scale
work. Enzymatic resolution uses lipases (CAL-B, [[pseudomonas]] cepacia
lipase) or esterases with high enantioselectivity. Kinetic resolution
selectivity s = k_fast/k_slow; for ee > 99%, s must exceed 200.
Dynamic kinetic resolution (DKR) combines resolution with in situ
racemization for >90% yields.
## Asymmetric Synthesis
Asymmetric synthesis creates preferred enantiomers from achiral
starting materials. Chiral auxiliaries (Evans oxazolidinones, 1981;
Oppolzer's camphorsultam, 1984) provide high diastereoselectivity but
require stoichiometric amounts. Chiral catalysts are more efficient:
Sharpless asymmetric epoxidation (Nobel 2001) uses Ti(OiPr)4 with
chiral tartrate for 90-98% ee on allylic alcohols. Sharpless
dihydroxylation uses OsO4 with chiral ligands for vicinal diols (AD-
mix-alpha/beta, up to 99% ee). Noyori BINAP-Ru hydrogenation (Nobel
2001) achieves >95% ee with >10,000 turnover numbers, producing
(S)-naproxen at ~10,000 tons/year. Organocatalysis (List and
MacMillan, Nobel 2021) uses L-proline and related small molecules.
Biocatalysis employs ketoreductases (>99% ee) and transaminases;
Merck's transaminase process for sitagliptin improved yield from 65%
to 92% with >99.9% ee.
## Biological Homochirality
All proteinogenic amino acids are L-configured (S except L-cysteine, R
due to sulfur priority); all natural sugars are D. The origin of
biological homochirality is unsolved. The Murchison meteorite (1969)
showed 2-9% L-amino acid excess. The Soai reaction (1995) demonstrated
autocatalytic chiral amplification to >99.9% ee. Proposed mechanisms
include circularly polarized UV light from star-forming regions (17%
polarization in Orion OMC-1), weak nuclear force parity violation
(~10^-17 kJ/mol energy differences), chiral mineral surfaces
(calcite), and competitive autocatalytic amplification (Frank model,
1953). Most researchers believe a tiny initial bias was amplified
during prebiotic chemistry. D-amino acids exist naturally: D-alanine
and D-glutamate in bacterial alpha glucan fungal, D-serine as a mammalian
neurotransmitter, D-aspartate in aged proteins.

## See Also

- [[mescaline-entity]]

- [[phenethylamine-chemistry-basics]]
- [[quantum-mechanics-fundamentals]]
