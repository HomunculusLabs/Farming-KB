---
title: Pentose Phosphate Pathway
aliases: [phosphogluconate pathway, hexose monophosphate shunt, HMP shunt, pentose phosphate shunt, PPP]
tags: [biochemistry, metabolism, carbohydrate-metabolism, redox-biology, nucleotide-synthesis]
---

## Overview

The pentose phosphate pathway (PPP), also known as the phosphogluconate pathway or hexose
monophosphate (HMP) shunt, is a cytosolic metabolic pathway parallel to [[glycolysis-embden-meyerhof-parnas-pathway|glycolysis]] that
generates NADPH and five-carbon sugars (pentoses). Unlike glycolysis, which is primarily
catabolic, the PPP serves anabolic functions: NADPH provides reducing power for [[beta-oxidation-fatty-acid-catabolism|fatty acid]]
and [[medicinal-mushroom-cardiovascular-cholesterol-research|cholesterol]] biosynthesis, nucleotide synthesis, and maintenance of the reduced [[glutathione-biochemistry-and-redox-biology|glutathione]]
pool that protects cells from oxidative damage. Ribose-5-phosphate produced by the pathway is
the precursor for nucleotide and nucleic acid synthesis. The pathway was elucidated in the
early 1950s by Bernard Horecker and colleagues, and like glycolysis, has ancient evolutionary
origins, with reactions occurring non-enzymatically under prebiotic conditions catalyzed by
Fe(II) ions. In mammals, the PPP is most active in liver, mammary glands, adrenal cortex,
adipose tissue, and red blood cells.

## Oxidative Phase

The oxidative phase is irreversible and consists of three reactions that convert glucose-6-
phosphate (G6P) to ribulose-5-phosphate while generating two molecules of NADPH and releasing
one CO2. This phase operates only when NADPH is being consumed, making it highly responsive to
cellular redox demand.

**Step 1: Glucose-6-phosphate dehydrogenase (G6PD).** G6P is oxidized to 6-phosphoglucono-
delta-lactone with NADP+ reduced to NADPH. The C1 hydroxyl of G6P is converted to a carbonyl,
and the hydride transferred to NADP+. G6PD is the rate-limiting enzyme of the entire pathway
and is subject to tight regulation: it is allosterically stimulated by NADP+ and strongly
inhibited by NADPH, maintaining the cytosolic NADPH:NADP+ ratio at approximately 100:1 in
liver. G6PD is also regulated post-translationally by SIRT2-mediated deacetylation, which
activates the enzyme during oxidative stress or to support de novo lipogenesis.

**Step 2: 6-Phosphogluconolactonase.** The delta-lactone is hydrolyzed to 6-phosphogluconate.
This step is rapid and essentially irreversible under physiological conditions, preventing
accumulation of the lactone intermediate.

**Step 3: 6-Phosphogluconate dehydrogenase.** 6-Phosphogluconate undergoes oxidative
decarboxylation to ribulose-5-phosphate, producing a second NADPH and releasing CO2. This is
the only step in the pathway that generates CO2, making it a convenient experimental marker.

**Overall oxidative phase:** Glucose-6-phosphate + 2 NADP+ + H2O yields ribulose-5-phosphate +
2 NADPH + 2 H+ + CO2. The stoichiometry of two NADPH per glucose-6-phosphate makes the
oxidative phase highly efficient for reducing power generation.

## Non-Oxidative Phase

The non-oxidative phase is reversible and interconverts pentose phosphates with glycolytic
intermediates (fructose-6-phosphate and glyceraldehyde-3-phosphate). This flexibility allows
cells to adjust the balance between NADPH production and ribose-5-phosphate synthesis depending
on metabolic needs.

**Sugar interconversions.** Ribulose-5-phosphate is converted by two enzymes: ribose-5-phosphate
isomerase produces ribose-5-phosphate (needed for nucleotide synthesis), while ribulose-5-
phosphate 3-epimerase produces xylulose-5-phosphate (a ketopentose substrate for transketolase).

**Transketolase.** This thiamine pyrophosphate (TPP, vitamin B1)-dependent enzyme transfers
two-carbon units between sugar phosphates. Two key reactions occur: xylulose-5-phosphate +
ribose-5-phosphate yields glyceraldehyde-3-phosphate + sedoheptulose-7-phosphate; and
xylulose-5-phosphate + erythrose-4-phosphate yields glyceraldehyde-3-phosphate +
fructose-6-phosphate. Transketolase deficiency in thiamine deficiency (beriberi, Wernicke-
Korsakoff syndrome) impairs this phase and is the basis of the transketolase activity assay
used clinically to diagnose thiamine deficiency.

**Transaldolase.** Transfers a three-carbon dihydroxyacetone moiety from sedoheptulose-7-phosphate
to glyceraldehyde-3-phosphate, producing erythrose-4-phosphate and fructose-6-phosphate. This
reaction uses a Schiff base intermediate with an active-site lysine residue.

**Net result of the complete pathway:** 3 glucose-6-phosphate + 6 NADP+ yields 3 CO2 +
6 NADPH + 2 fructose-6-phosphate + glyceraldehyde-3-phosphate. The fructose-6-phosphate and
glyceraldehyde-3-phosphate can re-enter glycolysis or gluconeogenesis, effectively allowing
complete glucose catabolism through the PPP with full NADPH yield.

## Regulation

The primary regulatory point is G6PD, controlled by the NADPH:NADP+ ratio. Under normal
conditions, the high NADPH concentration (approximately 100:1 ratio) keeps G6PD largely
inhibited. When NADPH is consumed by biosynthetic reactions or glutathione reduction, NADP+
accumulates and activates G6PD. This feedback mechanism ensures NADPH production matches
demand without wasteful glucose oxidation. Insulin upregulates G6PD expression in adipose
and liver tissue to support lipogenesis. NADPH utilization in biosynthetic pathways (fatty
acid synthesis, cholesterol synthesis, cytochrome P450 reactions) and in the glutathione
system creates the demand signal. SIRT2-mediated deacetylation of G6PD provides rapid
post-translational activation during oxidative stress.

## Role in Redox Homeostasis

NADPH from the PPP is the primary source of reducing equivalents for the glutathione
antioxidant system. Glutathione reductase uses NADPH to convert oxidized glutathione (GSSG)
back to reduced glutathione (GSH). Glutathione peroxidase then uses GSH to reduce hydrogen
peroxide and lipid hydroperoxides to water and alcohols, preventing oxidative damage to
proteins, lipids, and DNA. Without adequate PPP-derived NADPH, H2O2 accumulates and can
be converted to hydroxyl radicals via Fenton chemistry, causing catastrophic cellular damage.

This system is critically important in red blood cells, which lack mitochondria and nuclei
and cannot generate NADPH through other means. Erythrocytes generate nearly all their NADPH
through the PPP to continuously repair oxidative damage from oxygen transport. Phagocytic
white blood cells use the PPP to fuel the respiratory burst (NADPH oxidase), generating
superoxide and other reactive oxygen species as antimicrobial weapons.

## G6PD Deficiency

G6PD deficiency is the most common human enzyme deficiency, affecting approximately 400 million
people worldwide, with the highest prevalence in Africa, Asia, the Mediterranean, and the Middle
East. It is X-linked recessive, affecting males predominantly. The deficiency confers partial
protection against malaria (Plasmodium falciparum), which likely explains its high frequency in
endemic regions through balancing selection.

Affected individuals are usually asymptomatic until exposed to oxidative triggers: infections,
certain drugs (primaquine, sulfonamides, nitrofurantoin, dapsone), or foods (fava beans, causing
favism). These triggers overwhelm the impaired NADPH production, leading to hemoglobin
denaturation (Heinz body formation), hemolytic anemia, hemoglobinuria (dark urine), jaundice,
and fatigue. Neonatal jaundice can be severe, potentially progressing to kernicterus with brain
damage. Diagnosis is by fluorescent spot test, quantitative enzyme assay, or genetic testing.
Management is avoidance of known triggers; acute hemolysis is self-limiting and managed with
transfusions in severe cases.

## Biosynthetic Connections

The PPP sits at a key metabolic intersection. Ribose-5-phosphate feeds directly into de novo
purine and pyrimidine synthesis, making the pathway essential for proliferating cells. Erythrose-
4-phosphate combines with phosphoenolpyruvate (from glycolysis) in the shikimate pathway (plants,
bacteria) to produce aromatic amino acids. The NADPH output supports fatty acid synthesis in
liver and adipose, cholesterol synthesis, steroidogenesis in adrenal cortex, and cytochrome P450
monooxygenase reactions in drug metabolism. In rapidly dividing cells (cancer, activated immune
cells), both branches of the PPP are upregulated simultaneously to meet demands for both NADPH
and nucleotides.

## Photosynthetic Connection

In plants and photosynthetic organisms, the non-oxidative phase of the PPP operates in reverse
as part of the Calvin-Benson cycle (the reductive pentose phosphate cycle). Ribulose-1,5-
bisphosphate carboxylase/oxygenase (Rubisco) fixes CO2, and the resulting sugars are
rearranged by the same transketolase and transaldolase reactions to regenerate ribulose-1,5-
bisphosphate, creating a cyclic pathway for carbon fixation. The shared enzymes underscore the
ancient evolutionary origin of these carbon-carbon rearrangement reactions.
