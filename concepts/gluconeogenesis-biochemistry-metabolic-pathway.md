---
title: "Gluconeogenesis"
created: 2026-04-28
updated: 2026-05-06
description: "Gluconeogenesis is the metabolic pathway by which glucose is synthesized from non-carbohydrate precursors such as lactate, glycerol, and glucogenic amino acids. It occurs primarily in the liver and renal cortex and is essential for maintaining blood glucose levels during fasting, starvation, and intense exercise."
tags:
  - biochemistry
  - metabolism
  - metabolic-pathway
  - glucose-homeostasis
  - endocrinology
  - clinical-biochemistry
related:
  - glycolysis
  - cori-cycle
  - glycogenolysis
  - glycogenesis
  - citric-acid-cycle
  - pyruvate-metabolism
  - insulin-signaling
  - glucagon-signaling
  - diabetes-mellitus
  - hypoglycemia
type: concept
sources:
  - "raw/papers/the-metabolic-pathway-of-psilocybin-production.md"
---

## Overview and Biological Significance

Gluconeogenesis (GNG) is the biosynthetic pathway that produces glucose from non-carbohydrate carbon substrates. It is not a simple reversal of glycolysis — although it shares seven reversible enzymatic steps, it bypasses three thermodynamically irreversible glycolytic reactions through four distinct enzymes. The pathway consumes 6 ATP equivalents (4 ATP + 2 GTP) per glucose synthesized, making it energetically expensive and tightly regulated.

GNG is indispensable for survival. The human brain consumes approximately 120 g of glucose per day and has minimal capacity to use alternative fuels under normal conditions. Hepatic glycogen stores (~70-100 g) are depleted within 12-18 hours of fasting, after which gluconeogenesis becomes the sole source of endogenous glucose. During prolonged starvation (>5 days), renal cortex gluconeogenesis can contribute up to 40% of total glucose production. The pathway also maintains glucose supply during intense exercise, when muscle glycogenolysis generates lactate that must be recycled.

## Pathway Steps and Key Enzymes

### 1. Pyruvate to Oxaloacetate (Pyruvate Carboxylase)

Pyruvate carboxylase (PC), a mitochondrial enzyme, carboxylates pyruvate to oxaloacetate (OAA) using ATP and bicarbonate. PC requires biotin as a covalently bound cofactor and acetyl-CoA as a potent allosteric activator. Acetyl-CoA signals a high-energy, low-carbohydrate state (e.g., beta-oxidation of [[adenosine-triphosphate-and-cellular-energy]] and suppressing GNG.
- **Fructose-2,6-bisphosphate (F2,6BP)** is the most potent regulator of the FBPase-1/PFK-1 pair: it activates PFK-1 and inhibits FBPase-1, strongly suppressing GNG.
- **ATP and citrate** activate FBPase-1, promoting GNG when energy is abundant.

### Hormonal Regulation

- **Glucagon** (fasting hormone): Stimulates GNG via cAMP-dependent protein kinase A (PKA) signaling. PKA phosphorylates and inactivates the bifunctional enzyme PFK-2/FBPase-2, reducing F2,6BP levels (de-repressing FBPase-1). Glucagon also induces transcription of PEPCK and G6Pase genes via CREB.
- **Insulin** (fed hormone): Suppresses GNG by promoting dephosphorylation of PFK-2/FBPase-2 (increasing F2,6BP), repressing PEPCK and G6Pase gene transcription via FOXO1 inhibition, and stimulating phosphofructokinase activity. Insulin's action is rapid (allosteric) and sustained (transcriptional).
- **Cortisol** (stress hormone): Enhances GNG during prolonged fasting and stress by inducing PEPCK and G6Pase gene expression. Cortisol also promotes muscle proteolysis, increasing amino acid supply for GNG. Its effects are permissive and synergistic with glucagon.
- **Epinephrine**: Activates GNG via beta-adrenergic/cAMP mechanisms similar to glucagon, particularly important during acute stress and exercise.

## Substrate Cycling and Futile Cycles with Glycolysis

Gluconeogenesis and glycolysis can operate simultaneously in hepatocytes, creating a substrate cycle (futile cycle) that hydrolyzes ATP and GTP without net flux. While this appears wasteful, controlled substrate cycling provides metabolic flexibility: it allows rapid switching between pathways in response to hormonal signals, generates heat (non-shivering thermogenesis), and fine-tunes metabolite concentrations. The primary site of futile cycling is at the F6P/F1,6BP interconversion (PFK-1 vs. FBPase-1). The magnitude of this cycle is controlled by F2,6BP — high F2,6BP suppresses the cycle by inhibiting FBPase-1.

## Tissue-Specific Aspects

### Liver

The liver is the primary site of gluconeogenesis, contributing approximately 80-90% of endogenous glucose production in the postabsorptive state. Hepatocytes express all four GNG-specific enzymes and possess the full enzymatic machinery. The liver's large size, high [[arbuscule-isolation-metabolic-activity-assays]], and direct portal blood supply (absorbing lactate and alanine from the intestine) make it ideally suited.

### Kidney Cortex

Renal gluconeogenesis becomes increasingly important during prolonged fasting and metabolic acidosis. The kidney contributes 15-20% of glucose production after an overnight fast and up to 40% after several days of starvation. Glutamine is the primary renal GNG precursor; its metabolism generates ammonium (NH4+), which is excreted in urine and helps buffer metabolic acidosis. The renal contribution is often underestimated clinically.

### Intestine

The small intestine contributes to GNG, particularly in the postprandial period. Enterocytes can convert glutamine and other amino acids to glucose. Intestinal GNG has been proposed to play a role in the portal glucose signal that regulates hepatic glucose production and food intake, though its quantitative significance in humans remains debated.

## Comparison with Glycolysis

| Feature | Glycolysis | Gluconeogenesis |
|---|---|---|
| Net ATP | +2 ATP (per glucose) | -6 ATP equivalents (4 ATP + 2 GTP) |
| Direction | Glucose to Pyruvate | Non-carb precursors to Glucose |
| Irreversible steps | 3 (HK, PFK-1, PK) | 4 bypass enzymes (G6Pase, FBPase-1, PC, PEPCK) |
| Primary tissues | All cells | Liver, kidney cortex |
| Hormonal driver | Insulin (stimulates) | Glucagon, cortisol (stimulate) |
| NADH/NAD+ | Produces NADH | Consumes NADH |
| Key regulator | F2,6BP activates PFK-1 | F2,6BP inhibits FBPase-1 |
| Physiological role | Energy production | Blood glucose maintenance |

## Clinical Significance

### Diabetes Mellitus

In type 2 diabetes, hepatic gluconeogenesis is inappropriately elevated despite hyperinsulinemia and hyperglycemia. Hepatic insulin resistance at the transcriptional level fails to suppress PEPCK and G6Pase expression, while increased circulating glucagon and free [[stable-carbon-isotope-signature-fatty-acids-mycorrhizal-carbon-tracking]] (providing acetyl-CoA and glycerol) further drive GNG. Metformin, the first-line oral antidiabetic, partially acts by inhibiting hepatic GNG through AMPK activation and mitochondrial complex I inhibition. The contribution of excessive GNG to fasting hyperglycemia in type 2 diabetes can exceed 60%.

### Fasting and Starvation

During the transition from the fed to the fasted state, a well-orchestrated hormonal shift (declining insulin, rising glucagon and cortisol) activates GNG. After glycogen depletion (~18 hours), GNG provides all endogenous glucose. By 3-5 days of starvation, GNG shifts toward glycerol and glutamine as the primary substrates, as muscle proteolysis decreases to conserve protein.

### Hypoglycemia

Impaired gluconeogenesis contributes to hypoglycemia in multiple clinical settings: hepatic failure (loss of GNG capacity), adrenal insufficiency (cortisol deficiency), sepsis, and inborn errors of metabolism (e.g., PEPCK deficiency, FBPase deficiency). Neonatal hypoglycemia can result from immature GNG enzyme systems, particularly in premature infants. Understanding GNG physiology guides treatment — glucagon is ineffective when GNG substrates are depleted (e.g., ethanol intoxication), necessitating IV glucose.

## Evolutionary Conservation

Gluconeogenesis is an ancient, evolutionarily conserved pathway present in virtually all life forms — bacteria, plants, fungi, [[diffusion-osmosis-and-active-transport-in-plants]], GNG is critical for [[glycolysis-embden-meyerhof-parnas-pathway]]
- [[psilocybin-biosynthetic-metabolic-pathway]]
