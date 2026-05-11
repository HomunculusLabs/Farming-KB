---
title: Psilocybin Biosynthesis Pathway And Enzymology
concept_type: biochemistry
topic: mycology
related: ["tryptophan-biosynthesis-from-chorismate", "tryptophan-decarboxylase", "baeocystin-and-norbaeocystin-in-psilocybin-biosynthesis", "acetyl-protection-route-psilocin-psilocybin-synthesis"]
created: 2026-05-09
---

# Psilocybin Biosynthesis Pathway and Enzymology

## Introduction

Psilocybin (O-phosphoryl-4-hydroxy-N,N-dimethyltryptamine) and its dephosphorylated counterpart psilocin (4-hydroxy-N,N-dimethyltryptamine) are the principal psychoactive indole alkaloids produced by mushrooms in the genera *Psilocybe*, *Panaeolus*, *Copelandia*, *Gymnopilus*, *Inocybe*, and *Pluteus*. The elucidation of the psilocybin biosynthesis pathway has been a landmark achievement in fungal natural product biochemistry, revealing a four-enzyme cascade that converts the [[cho-fish-amino-acid-preparation]] L-tryptophan into psilocybin in a series of regio- and chemoselective transformations.

## Historical Discovery

The pathway was largely elucidated through the work of Janis Fricke, Dirk Hoffmeister, and colleagues at the Hans Knöll Institute (Leibniz Institute for Natural Product Research and Infection Biology) in Jena, Germany. Their 2017 publication in *Angewandte Chemie* identified the four core biosynthetic enzymes by combining transcriptomic analysis of *[[basidiocarp-four-stage-development-classification-psilocybe-cubensis-badham-1982]]* [[bloomfield-asterophora-and-mycoparasites-of-fruiting-bodies]] with heterologous expression in *E. coli* and *Aspergillus nidulans*.

Key insights from the discovery:

- The entire pathway is encoded in a compact biosynthetic gene cluster spanning approximately 7.5 kb of genomic DNA.
- All four enzymes are co-regulated, being expressed specifically during [[fungal-fruiting-body-formation-environmental-triggers]] when psilocybin accumulates.
- The pathway represents a convergence of [[primary-metabolic-precursors-to-the-shikimate-pathway]] pathways ([[tryptophan-biosynthesis-from-chorismate]], SAM-dependent methylation) with specialized enzymology unique to psilocybin-producing fungi.

## The Four-Enzyme Pathway

### Step 1: L-Tryptophan Decarboxylation (PsiD)

**Enzyme**: PsiD — L-tryptophan decarboxylase  
**Reaction**: L-tryptophan → tryptamine + CO₂  
**Cofactor**: Pyridoxal-5'-phosphate (PLP)

PsiD is a cytosolic PLP-dependent decarboxylase that removes the α-carboxyl group from L-tryptophan to produce tryptamine. This reaction is analogous to the first step in plant serotonin and indole alkaloid biosynthesis, and PsiD shows sequence homology to plant aromatic amino acid decarboxylases.

Key properties of PsiD:

- **Km for L-tryptophan**: ~0.3 mM, indicating moderate substrate affinity.
- **Specificity**: Highly specific for L-tryptophan; shows minimal activity on other aromatic amino acids (L-tyrosine, L-phenylalanine).
- **Kinetic parameters**: kcat ~2.5 s⁻¹.
- **Subcellular localization**: Cytosolic.

The decarboxylation mechanism follows the classic PLP-dependent pathway: the amino acid substrate forms an external aldimine with PLP, followed by decarboxylation and protonation to release the amine product and regenerate the enzyme-PLP internal aldimine.

### Step 2: Hydroxylation at C-4 (PsiH)

**Enzyme**: PsiH — monoxygenase  
**Reaction**: tryptamine → 4-hydroxytryptamine (norbaeocystin)  
**Cofactors**: NADPH, O₂, heme

PsiH is a cytochrome P450 monoxygenase that catalyzes the regioselective hydroxylation of tryptamine at the C-4 position of the indole ring. This is the key regiochemical step that distinguishes psilocybin from other tryptamine derivatives. The C-4 position is normally one of the least reactive positions on the indole ring, making this a chemically challenging transformation.

Key properties of PsiH:

- **Regioselectivity**: Exclusive hydroxylation at C-4; no detectable 5-, 6-, or 7-hydroxy products.
- **Cofactor dependence**: Requires both NADPH as an electron donor and molecular oxygen.
- **Membrane association**: As a P450 enzyme, PsiH is associated with the endoplasmic reticulum membrane.
- **Substrate scope**: Accepts tryptamine and N-methyltryptamine as substrates but shows reduced activity on N,N-dimethyltryptamine (DMT), suggesting the pathway proceeds via stepwise methylation.

The mechanistic significance of C-4 hydroxylation cannot be overstated. In medicinal chemistry, direct hydroxylation of tryptamine at C-4 is extremely difficult to achieve chemically — it typically requires multistep syntheses involving protection/deprotection strategies. PsiH accomplishes this transformation in a single enzymatic step under mild physiological conditions.

### Step 3: Stepwise N-Methylation (PsiK)

**Enzyme**: PsiK — SAM-dependent N-methyltransferase  
**Reaction 1**: 4-hydroxytryptamine → 4-hydroxy-N-methyltryptamine (baeocystin)  
**Reaction 2**: 4-hydroxy-N-methyltryptamine → 4-hydroxy-N,N-dimethyltryptamine (psilocin)  
**Cofactor**: S-adenosyl-L-methionine (SAM)

PsiK is a SAM-dependent methyltransferase that catalyzes two sequential N-methylations of the amino group on the 4-hydroxytryptamine [[shirota-glyoxalylamide-side-chain-construction-psilocin-synthesis]]. The stepwise mechanism is significant: PsiK methylates the primary amine to a secondary amine (baeocystin), then methylates the secondary amine to the tertiary amine (psilocin).

Key properties of PsiK:

- **Sequential mechanism**: Each methylation is a separate catalytic event; the enzyme releases baeocystin as an intermediate.
- **Km values**: Higher affinity for the first methylation (4-hydroxytryptamine) than the second (baeocystin).
- **SAM specificity**: Requires SAM as the methyl donor; S-adenosylhomocysteine (SAH) is the product.
- **Regulation**: Activity is inhibited by SAH, providing product-feedback regulation.

The intermediate **baeocystin** (4-hydroxy-N-methyltryptamine) is itself found [[cap-versus-stem-alkaloid-distribution-in-psilocybin-mushrooms]] at concentrations of 0.1–0.5% dry weight (compared to 0.5–2.0% for psilocybin). Its pharmacological activity is less well characterized but it appears to be a weak 5-HT2A agonist.

### Step 4: O-Phosphorylation (PsiM)

**Enzyme**: PsiM — SAM-dependent 4-hydroxyindole O-methyltransferase  
**Reaction**: psilocin → psilocybin (O-phosphorylation using a unique mechanism)  
**Cofactor**: The enzyme uses a phospho-transfer mechanism distinct from classical kinases.

The final step involves phosphorylation of the 4-hydroxy group of psilocin to produce psilocybin. Unlike typical kinases that use ATP as a phosphate donor, the enzymology of this step has been the subject of some revision. Current understanding indicates that PsiM is actually an O-methyltransferase that may be involved in an alternative branch of the pathway, while the phosphorylation step may involve a distinct phosphotransferase.

The phosphorylation serves as a metabolic protection mechanism: the phosphate group increases water solubility, reduces oxidative degradation, and serves as a pharmacologically inactive prodrug form. After ingestion, alkaline phosphatases in the gut and liver cleave the phosphate to generate the active compound psilocin.

## The Biosynthetic Gene Cluster
