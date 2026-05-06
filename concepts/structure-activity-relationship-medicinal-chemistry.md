---
title: Structure Activity Relationship Medicinal Chemistry
created: 2026-05-06
updated: 2026-05-06
type: concept
tags: []
sources: []
---

---
ti

Structure-activity relationship (SAR) is the systematic study of how the chemical
structure of a molecule determines its biological activity. The foundational
premise, articulated by Paul Ehrlich around 1900 (corpora non agunt nisi fixata
— substances do not act unless they are bound), holds that pharmacological
effects arise from molecular interactions between a drug and its biological
target, and the quality of that interaction is governed entirely by the drug's
three-dimensional structure and physicochemical properties. SAR analysis [[maps]]
the relationship between structural features and biological endpoints including
potency, selectivity, efficacy, toxicity, and pharmacokinetic behavior. Small
structural modifications — adding, removing, or repositioning a single atom or
functional group — can produce orders-of-magnitude changes in biological
activity, making SAR the central discipline of lead optimization in drug
discovery.

## Pharmacophore and Bioisosterism

A pharmacophore is the abstract three-dimensional arrangement of steric and
electronic features required for optimal interaction with a specific biological
target: hydrogen bond donors and acceptors, hydrophobic regions, aromatic ring
centroids, and ionizable groups. The pharmacophore concept separates the
essential binding features from the molecular scaffold that presents them,
enabling scaffold hopping — replacing the core framework while preserving the
geometry of key interactions.

Bioisosteres are substituents or groups with similar physicochemical properties
used to replace problematic moieties while maintaining activity. Classical
bioisosteric replacements include carboxylic acid to tetrazole (similar pKa,
improved membrane permeability), benzene to thiophene or pyridine (similar size
and aromaticity, different electronics), amide to oxadiazole (improved
metabolic stability), and hydroxyl to fluorine (small, blocks metabolic
oxidation). The -CH2- to -O- to -NH- to -S- series demonstrates bioisosterism
across a range of polarities while preserving approximate steric bulk. These
replacements are among the most powerful tools in the medicinal chemist's
arsenal for optimizing ADMET properties alongside potency.

## Physicochemical Dimensions of SAR

Three physicochemical dimensions drive SAR outcomes. Lipophilicity, measured by
LogP (octanol-water partition coefficient), determines membrane permeability and
binding to hydrophobic protein pockets. The optimal range for oral
bioavailability is typically LogP 1-5. Electronic effects, quantified by
Hammett sigma constants, influence ionization state (pKa), hydrogen bonding
capacity, electron density on aromatic rings (affecting pi-stacking), and
metabolic susceptibility. Steric effects govern whether a molecule fits into a
binding pocket; bulky groups can enhance selectivity by preventing off-target
binding or reduce activity by disrupting optimal geometry.

## Classical SAR Methodologies

The Hammett equation (1937), log(K/K0) = rho-sigma, provides the quantitative
foundation. Sigma (sigma) is the substituent constant measuring electronic
effect; rho (rho) is the reaction constant measuring sensitivity. Sigma-m
reflects primarily inductive effects; sigma-p includes resonance contributions.
Linear free energy relationships (LFERs) extend this principle: changes in
binding free energy correlate linearly with changes in molecular descriptors.

Corwin Hansch formalized QSAR in the 1960s by combining hydrophobic (pi),
electronic (sigma), and steric (Taft Es) parameters: log(1/C) = a-pi + b-sigma
+ c-Es + d-pi-squared + e. The quadratic lipophilicity term accounts for the
parabolic relationship between LogP and activity — too hydrophobic reduces
aqueous solubility, too hydrophilic impairs membrane permeability. Free-Wilson
analysis treats each substituent at each position as a binary variable, using
regression without explicit physicochemical parameters.

The Topliss decision tree (1972) provides a non-computational guide for
aromatic substituent exploration. Starting from an unsubstituted phenyl ring,
the first test substituent (typically 4-Cl) discriminates whether lipophilicity
or electronics dominates, directing subsequent synthesis toward the most
informative analogs. Craig plots graph substituents as points in sigma-pi space,
helping chemists select groups that vary primarily in one dimension while
holding the other constant.

## Modern Computational SAR

Molecular docking predicts ligand binding poses and affinities using scoring
functions based on van der Waals, electrostatic, and hydrogen bonding terms
(AutoDock, Glide, GOLD). Pharmacophore modeling generates three-dimensional
feature maps from known active compounds for virtual screening, applicable even
without a target structure. Molecular dynamics simulations reveal binding
pathways, conformational flexibility, and water-mediated interactions over
time.

Machine learning has transformed QSAR. Graph neural networks operate directly
on molecular structures; transformer models (ChemBERTa, MolBERT) learn
molecular representations from large datasets; generative models (VAEs, GANs,
diffusion models) design novel molecules within desired property spaces. Free
energy perturbation (FEP) calculations predict binding affinity differences
between related compounds with sub-kilocalorie-per-mole accuracy, enabling
prospective potency predictions that guide synthesis prioritization.

## Drug Design Constraints and ADMET

Lipinski's Rule of Five (1997) defines drug-like chemical space for oral
bioavailability: molecular weight under 500 Da, LogP under 5, fewer than 5
hydrogen bond donors, and fewer than 10 acceptors. Veber's criteria add
rotatable bonds under 10 and polar surface area under 140 square angstroms.
SAR optimization must navigate within these constraints — adding lipophilic
groups to improve potency often pushes LogP above 5, while adding polar groups
for target interactions can reduce permeability. This tension between potency
and drug-likeness is the central challenge of lead optimization.

ADMET considerations are increasingly integrated into SAR cycles. Absorption
depends on LogP, polar surface area, and pKa (determining ionization state at
physiological pH). Brain penetration requires LogP around 2, molecular weight
under 450, and polar surface area under 90 square angstroms. Metabolic stability
is addressed by bioisosteric replacement of metabolic soft spots (benzylic
positions, electron-rich heterocycles) and by introducing fluorine or deuterium
to block cytochrome P450 oxidation. Structural alerts for toxicity include
nitro groups, anilines, epoxides, and basic lipophilic amines (hERG liability).

## Historical Drug Design Examples

SAR has shaped major drug classes. The beta-blocker series evolved from
dichloroisoprenaline (an alpha antagonist) to propranolol by adding a naphthyl
group, revealing that the isopropylaminoethanol side chain is the essential
pharmacophore while the aryloxy group determines selectivity. Benzodiazepine
SAR showed that electron-withdrawing groups at position 7 (chloro in diazepam)
and ortho-halogens on the 5-phenyl ring dramatically enhance activity. Penicillin
SAR demonstrated that the beta-lactam ring is the essential pharmacophore while
the 6-acylamino side chain determines antibacterial spectrum. The opioid series
from morphine to fentanyl revealed that the basic nitrogen must remain within
approximately 5 angstroms of the aromatic ring, and N-phenethyl substitution
produces thousand-fold potency increases. In the statin class, SAR progression
from compactin to atorvastatin improved HMG-CoA reductase inhibition through
systematic side-chain optimization, culminating in a fluorophenyl group that
provided 2-3 fold potency gains.

## See Also

- [[bioisosteres]]

- [[medicinal-mushroom-properties]]

- [[tihkal-psilocin-psilocybin-chemistry]]

- [[cytochrome-p450-enzymes-drug-metabolism]]
- [[supramolecular-chemistry]]
