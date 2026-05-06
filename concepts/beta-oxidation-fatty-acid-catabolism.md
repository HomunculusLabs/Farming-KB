---
title: Beta Oxidation Fatty Acid Catabolism
created: 2026-05-06
updated: 2026-05-06
type: concept
tags: []
sources: []
---

---
ti

## Overview

Beta-oxidation is the core catabolic pathway by which fatty acid molecules are broken down to
generate acetyl-CoA, which enters the citric acid cycle to produce reducing equivalents for
the [[electron-transport-chain-mitochondrial-respiration|electron transport chain]]. The process is named for the oxidation of the beta carbon (C3)
of the fatty acyl chain, which is converted to a carbonyl group before cleavage. In eukaryotes,
beta-oxidation occurs primarily in the mitochondrial matrix, with very long-chain [[carbon-isotope-labelling-mycorrhizal-fatty-acids|fatty acids]]
(C22+) handled by peroxisomes first. The pathway is especially active in heart, liver, and
skeletal muscle. Red blood cells and neurons cannot oxidize fatty acids directly, relying on
glucose and ketone bodies respectively. The overall reaction for one cycle is: Cn-acyl-CoA +
FAD + NAD+ + H2O + CoA yields Cn-2-acyl-CoA + FADH2 + NADH + H+ + acetyl-CoA.

## Fatty Acid Activation and Transport

Free fatty acids enter cells via SLC27 family [[plant-cell-membrane-transport-proteins-channels-carriers-and-pumps|transport proteins]] (FATPs). In the cytosol, they
are activated to acyl-CoA by acyl-CoA synthetase, which consumes ATP (forming AMP + PPi) to
create the thioester bond. The PPi is rapidly hydrolyzed by inorganic pyrophosphatase, making
activation effectively irreversible at a cost of two high-energy phosphate bonds.

Long-chain acyl-CoA cannot cross the inner mitochondrial membrane directly and requires the
carnitine shuttle, a three-protein transport system:

1. **CPT I** (carnitine palmitoyltransferase I, outer membrane) transfers the acyl group to
   carnitine, forming acylcarnitine. CPT I is the rate-limiting step of the entire pathway and
   is potently inhibited by malonyl-CoA, the first committed intermediate of fatty acid
   synthesis. This reciprocal regulation ensures synthesis and oxidation never co-occur.

2. **CACT** (carnitine-acylcarnitine translocase) exchanges acylcarnitine inward for free
   carnitine outward across the inner membrane via an antiport mechanism.

3. **CPT II** (inner membrane, matrix face) regenerates acyl-CoA and free carnitine in the
   matrix. Short- and medium-chain fatty acids (C8 and below) diffuse across without the shuttle,
   which is why MCT oil bypasses CPT I regulation in metabolic disorders.

## The Four Steps of the Beta-Oxidation Cycle

Each cycle shortens the acyl-CoA by two carbons, producing one FADH2, one NADH, and one
acetyl-CoA. The cycle repeats until the entire chain is consumed.

**Step 1: Oxidation (acyl-CoA dehydrogenase).** Introduces a trans double bond between C2 and
C3, producing trans-Delta2-enoyl-CoA. FAD is reduced to FADH2, which transfers electrons to the
electron transport chain via ETF (electron-transferring flavoprotein) and ETF-QO, ultimately
contributing to the CoQ pool. Isoforms include VLCAD (C14-C20, bound to inner membrane), MCAD
(C6-C12), and SCAD (C4-C6), each specific to acyl chain length.

**Step 2: Hydration (enoyl-CoA hydratase).** Adds water stereospecifically across the trans
double bond to form L-3-hydroxyacyl-CoA. Only the L-isomer is produced, which is essential for
the stereochemical recognition by the next enzyme.

**Step 3: Oxidation (L-3-hydroxyacyl-CoA dehydrogenase).** Oxidizes the L-3-hydroxyl group to a
ketone, forming 3-ketoacyl-CoA with NAD+ reduced to NADH. This NADH enters the ETC at complex I.
In the mitochondrial trifunctional protein (MTP), steps 2-4 are combined in a single large
enzyme complex associated with the inner mitochondrial membrane.

**Step 4: Thiolysis (beta-ketothiolase).** A second molecule of CoA performs a nucleophilic attack
on the carbonyl carbon of the 3-keto group, cleaving between C2 and C3 to release acetyl-CoA and
an acyl-CoA two carbons shorter, which re-enters the cycle.

## Odd-Chain and Unsaturated Fatty Acids

**Odd-chain fatty acids** yield propionyl-CoA instead of the final acetyl-CoA. Propionyl-CoA is
converted to succinyl-CoA in three steps: propionyl-CoA carboxylase (biotin-dependent,
ATP-consuming) produces D-methylmalonyl-CoA; methylmalonyl-CoA epimerase converts this to the
L-isomer; and methylmalonyl-CoA mutase (cobalamin/B12-dependent) rearranges it to succinyl-CoA
via an intramolecular radical mechanism. Since succinyl-CoA is a TCA intermediate, odd-chain
oxidation is anaplerotic and can support gluconeogenesis, unlike even-chain fatty acids.

**Unsaturated fatty acids** require auxiliary enzymes because cis double bonds block formation
of the trans-Delta2 intermediate needed for normal beta-oxidation. Enoyl-CoA isomerase converts
cis-Delta3-enoyl-CoA to trans-Delta2-enoyl-CoA, handling monounsaturated fatty acids like oleic
acid. For polyunsaturated fatty acids like linoleic acid (18:2), 2,4-dienoyl-CoA reductase
reduces trans-Delta2,cis-Delta4-dienoyl-CoA intermediates to trans-Delta3-enoyl-CoA using NADPH,
after which isomerase completes the conversion.

## Peroxisomal Beta-Oxidation

Very long-chain (C22+), branched-chain, bile acid intermediates, and certain eicosanoids undergo
initial oxidation in peroxisomes. The process uses the same four-step cycle but with distinct
isoforms: acyl-CoA oxidase replaces acyl-CoA dehydrogenase, transferring electrons directly to
O2 to form H2O2, which is detoxified by catalase. This pathway is not coupled to ATP synthesis.
Once chains are shortened to approximately C8, they are exported as acylcarnitines to
mitochondria for complete oxidation. Peroxisomal beta-oxidation is upregulated by PPAR-alpha
activation in response to high-fat diets and fibrates like clofibrate.

## Energy Yield

Each beta-oxidation cycle produces approximately 14 ATP: 1.5 from FADH2 (via ETF/CoQ/complex
II), 2.5 from NADH (via complex I), and 10 from acetyl-CoA oxidation through the TCA cycle.
Two ATP equivalents are consumed in the initial activation step. For palmitoyl-CoA (C16), seven
cycles produce 7 FADH2, 7 NADH, and 8 acetyl-CoA molecules:

| Source               | ATP Yield |
|----------------------|-----------|
| 7 FADH2 x 1.5        | 10.5      |
| 7 NADH x 2.5         | 17.5      |
| 8 Acetyl-CoA x 10    | 80.0      |
| Activation (-2 ATP)  | -2.0      |
| **Total**            | **106**   |

The general formula is approximately 7n - 6 ATP for even-chain saturated fatty acids of n
carbons. For odd-chain fatty acids, the propionyl-CoA to succinyl-CoA conversion yields a net
of approximately 4 additional ATP (5 from succinyl-CoA minus 1 for carboxylation), giving a
formula of approximately 7n - 19 ATP.

## Regulation

Malonyl-CoA inhibition of CPT I is the primary control point. Malonyl-CoA, produced by
acetyl-CoA carboxylase (ACC), rises when energy is abundant (high insulin, low glucagon),
blocking fatty acid entry into mitochondria. During fasting, ACC is phosphorylated and
inactivated, malonyl-CoA levels fall, CPT I is disinhibited, and oxidation proceeds.
PPAR-alpha transcriptionally upregulates the full complement of beta-oxidation enzymes during
prolonged fasting. High acetyl-CoA and ATP ratios provide additional allosteric feedback,
signaling sufficient energy supply.

## Clinical Significance

At least 25 enzymes and transport proteins participate in beta-oxidation; 18 are associated
with human inborn errors of metabolism, typically manifesting during fasting or metabolic stress.

**MCAD deficiency** (1 in 10,000-20,000 births) is the most common, impairing C6-C12 oxidation.
It presents with hypoketotic hypoglycemia, vomiting, lethargy, and potentially sudden infant
death. Newborn screening has dramatically improved outcomes. Treatment centers on avoiding
fasting, frequent carbohydrate feedings, and carnitine supplementation.

**VLCAD deficiency** affects C14-C20 oxidation. Severe forms present neonatally with
cardiomyopathy, hepatomegaly, and hypoglycemia. Milder forms cause exercise-induced
rhabdomyolysis. Management includes a low-fat diet with MCT supplementation.

**LCHAD deficiency** impairs the dehydrogenation step of long-chain oxidation and is notably
associated with maternal acute fatty liver of pregnancy when the fetus is affected. Symptoms
include hypoketotic hypoglycemia, cardiomyopathy, retinopathy, and peripheral neuropathy.

## Ketogenesis Connection

During prolonged fasting, hepatic acetyl-CoA from beta-oxidation exceeds TCA cycle capacity
because oxaloacetate is diverted to gluconeogenesis. Excess acetyl-CoA is converted to ketone
bodies (acetoacetate, beta-hydroxybutyrate, acetone) by HMG-CoA synthase and HMG-CoA lyase in
hepatic mitochondria. These water-soluble fuels supply the brain, heart, and skeletal muscle
during glucose scarcity. Ketogenesis is governed by the same malonyl-CoA/CPT I gate that
controls beta-oxidation flux, linking the two pathways at their regulatory nexus.

## See Also
- [[cancer-beta-glucan-pharmacology]]
- [[beta-glucan-receptor-binding]]
- [[beta-d-entity-pihkal]]
