---
title: Glycolysis and the Embden-Meyerhof-Parnas Pathway
type: concept
aliases: [glycolysis, EMP pathway, Embden-Meyerhof-Parnas, glycolytic pathway, glucose catabolism, glycolytic flux]
tags: [biochemistry, metabolism, cellular-respiration, enzyme-kinetics, carbohydrate-metabolism, energy-metabolism]
created: 2026-05-02
updated: 2026-05-06
type: concept
sources: []
---

Glycolysis (from Greek glykys, sweet, and lysis, splitting) is the universal
metabolic pathway that converts one molecule of glucose (C6) into two molecules
of pyruvate (C3) in the cytoplasm of virtually all living organisms. The pathway
consists of ten enzyme-catalyzed steps, requires no oxygen, [[mollison-designers-resources-classification-and-yields]] a net
gain of 2 [[electron-transport-chain-mitochondrial-respiration]] and 2 [[glutathione-biochemistry-and-redox-biology]] per glucose. Also called the Embden-Meyerhof-Parnas
(EMP) pathway after the three researchers who elucidated it, glycolysis is one
of the most ancient metabolic pathways, believed to have evolved before the
Great Oxidation Event approximately 2.4 billion years ago in an anaerobic world.

Overall reaction: Glucose + 2 NAD+ + 2 ADP + 2 Pi yields 2 Pyruvate + 2 NADH +
2 H+ + 2 ATP + 2 H2O.

## Energy Investment Phase (Steps 1-5)

The first five steps consume 2 ATP to phosphorylate and rearrange glucose into
two molecules of glyceraldehyde-3-phosphate (G3P).

**Step 1 — Hexokinase**: Glucose to glucose-6-phosphate (G6P), consuming ATP.
Mg2+ is required as a cofactor. Hexokinase (HK I-III) has low Km (~0.1 mM) and
is inhibited by its product G6P. The liver isoform glucokinase (HK IV, Km ~10 mM)
is not product-inhibited, allowing the liver to phosphorylate glucose even after
a meal when G6P is abundant. Glucokinase is regulated by glucokinase regulatory
protein (GKRP), which sequesters it in the nucleus; fructose-1-phosphate
releases it. This step is irreversible.

**Step 2 — Phosphoglucose isomerase**: G6P to fructose-6-phosphate (F6P), a
reversible aldose-to-ketose isomerization. The ring opens, the carbonyl shifts
from C1 to C2, and the ring recloses as a furanose.

**Step 3 — Phosphofructokinase-1 (PFK-1)**: F6P to fructose-1,6-bisphosphate
(F1,6BP), consuming ATP. This is the rate-limiting step of glycolysis and the
primary point of regulation. PFK-1 is allosterically activated by AMP and ADP
(signaling low energy) and by fructose-2,6-bisphosphate (F2,6BP, the most
potent activator). It is inhibited by ATP (high energy), citrate (abundant TCA
intermediates), and low pH (H+, preventing excessive lactic acid accumulation).

**Step 4 — Aldolase**: F1,6BP splits into glyceraldehyde-3-phosphate (G3P) and
dihydroxyacetone phosphate (DHAP). This reversible aldol cleavage produces two trioses from one hexose.

**Step 5 — Triose phosphate isomerase (TPI)**: DHAP isomerizes to G3P. This
near-perfect enzyme (catalytic perfection, diffusion-limited) ensures both
trioses proceed through the payoff phase. From this point, all subsequent steps
occur twice per glucose molecule.

## Energy Payoff Phase (Steps 6-10)

The payoff phase generates 4 ATP and 2 NADH, yielding a net gain of 2 ATP and 2
NADH per glucose molecule.

**Step 6 — Glyceraldehyde-3-phosphate dehydrogenase (GAPDH)**: G3P to
1,3-bisphosphoglycerate (1,3BPG). Inorganic phosphate is incorporated, and NAD+
is reduced to NADH. This step captures the oxidative energy of the aldehyde as a
high-energy acyl phosphate bond. The thiol group of a cysteine residue in the
active site forms a covalent thiohemiacetal intermediate with G3P.

**Step 7 — Phosphoglycerate kinase (PGK)**: 1,3BPG to 3-phosphoglycerate (3PG),
producing ATP by substrate-level phosphorylation. This step recovers the ATP
invested in step 1.

**Step 8 — Phosphoglycerate mutase**: 3PG to 2-phosphoglycerate (2PG) by
shifting the phosphate group from C3 to C2. The enzyme uses a phospho-histidine
intermediate.

**Step 9 — Enolase**: 2PG to phosphoenolpyruvate (PEP) with elimination of water.
Mg2+ is required to stabilize the carbanion intermediate. PEP has the highest
phosphoryl transfer potential of any common metabolic intermediate.

**Step 10 — Pyruvate kinase (PK)**: PEP to pyruvate, producing ATP by
substrate-level phosphorylation. This irreversible step is regulated by
feedforward activation from F1,6BP and allosteric inhibition by ATP and alanine.
Hormonal regulation via glucagon activates PKA, which phosphorylates and
inactivates liver PK (PK-L), suppressing glycolysis during fasting. Insulin
promotes dephosphorylation and activation. The PK-M2 isoform in proliferating
cells can exist as a less active dimer (shunting carbon to biosynthesis) or an
active tetramer, a key metabolic switch in cancer cells.

## Regulation and Hormonal Control

Glycolytic flux is primarily controlled at PFK-1, the committed step. The
bifunctional enzyme PFK-2/FBPase-2 synthesizes and degrades F2,6BP. Insulin
promotes dephosphorylation of PFK-2/FBPase-2, activating the PFK-2 kinase domain
and raising F2,6BP levels, which activates PFK-1 and stimulates glycolysis.
Glucagon triggers phosphorylation via PKA, activating the FBPase-2 domain,
lowering F2,6BP, and inhibiting PFK-1 to conserve glucose during fasting.

The Pasteur effect describes the inhibition of glycolysis by oxygen: aerobic
conditions produce more ATP via oxidative phosphorylation, raising ATP levels
and allosterically inhibiting PFK-1. The Crabtree effect, observed in yeast and
some cancer cells, is the opposite — preferential fermentation despite aerobic
conditions when glucose is abundant.

## Fate of Pyruvate

Under aerobic conditions, pyruvate enters mitochondria via the mitochondrial
pyruvate carrier (MPC) and is converted to acetyl-CoA by the pyruvate
dehydrogenase complex (PDHC), feeding into the [[citric-acid-cycle-tca-krebs-cycle]] and ultimately
oxidative phosphorylation for a total yield of approximately 30-32 ATP per
glucose. Under anaerobic conditions, lactate dehydrogenase (LDH) converts
pyruvate to lactate, regenerating NAD+ to keep glycolysis running. Erythrocytes,
which lack mitochondria, rely exclusively on anaerobic glycolysis. In yeast,
pyruvate decarboxylase converts pyruvate to acetaldehyde, then alcohol
dehydrogenase produces ethanol, also regenerating NAD+. The Cori cycle shuttles
lactate from muscle to liver where gluconeogenesis converts it back to glucose
at a cost of 6 ATP per glucose molecule.

## Connections to Other Metabolic Pathways

Glycolysis interfaces with multiple metabolic networks: G6P branches into glycogen synthesis (via G1P) and the [[pentose-phosphate-pathway]] phosphate pathway, which produces
NADPH for biosynthesis and ribose-5-phosphate for nucleotide synthesis. DHAP
feeds glycerol-3-phosphate for triglyceride backbone formation. Pyruvate provides carbon for alanine transamination and oxaloacetate via
pyruvate carboxylase (anaplerosis). [[diffusion-osmosis-and-active-transport-in-plants]] and microorganisms, PEP and erythrose-
4-phosphate enter [[primary-metabolic-precursors-to-the-shikimate-pathway]] for aromatic amino acid biosynthesis,
the precursor to tryptophan, phenylalanine, and tyrosine, as well as numerous
[[singh-ergot-alkaloid-fungal-secondary-metabolites]] including alkaloids and flavonoids.

## Historical Discovery

Eduard Buchner demonstrated in 1897 that cell-free yeast extracts could ferment
glucose to ethanol and CO2, proving fermentation did not require intact living
cells and establishing the concept of enzymatic catalysis (Nobel Prize, 1907).
Arthur Harden and William Young identified inorganic phosphate as essential and
discovered fructose-1,6-bisphosphate as the first intermediate (Nobel Prize,
1929). Gustav Embden, Otto Meyerhof (Nobel Prize, 1922), and Jakub Karol Parnas
elucidated the complete pathway through the 1930s-1940s. Carl and Gerty Cori discovered the Cori cycle and glucose-1-
phosphate (Nobel Prize, 1947). Fritz Lipmann discovered coenzyme A and ATP's
role as energy currency (Nobel Prize, 1953).

## Clinical Significance

The Warburg effect — aerobic glycolysis in cancer cells even in the presence of
oxygen — was discovered by Otto Warburg (Nobel Prize, 1931). Tumors
overexpress GLUT1 and hexokinase II, and the PK-M2 dimer shunts carbon to biosynthetic pathways. Fluorodeoxyglucose positron emission tomography
(18F-FDG PET) exploits elevated tumor glucose uptake for cancer detection.

Inherited glycolytic enzyme deficiencies include pyruvate kinase deficiency
(the most common, causing hereditary nonspherocytic hemolytic anemia
with over 500 known PKLR mutations), phosphofructokinase deficiency (Tarui disease, GSD
type VII), triose phosphate isomerase deficiency (progressive neuromuscular
degeneration), and aldolase A deficiency (GSD type XII). Diabetes disrupts
glycolytic regulation: Type 1 reduces glucokinase expression and increases
