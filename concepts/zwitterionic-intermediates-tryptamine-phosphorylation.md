---
title: Zwitterionic Intermediates in Tryptamine Phosphorylation
created: 2026-05-08
updated: 2026-05-08
sources:
  - "Shirota O, Hakamata W, Goda Y - Concise Large-Scale Synthesis of Psilocin and Psilocybin (J. Nat. Prod. 2003)"
type: concept
tags: [zwitterion, phosphorylation, psilocybin, organic-chemistry, nmr, benzyl-migration]
---

# Zwitterionic Intermediates in Tryptamine Phosphorylation

## Overview

The synthesis of psilocybin from psilocin requires phosphorylation of the
4-hydroxy group — converting 4-hydroxy-N,N-dimethyltryptamine into its
4-phosphoryloxy derivative. This seemingly straightforward transformation proved
technically challenging, with multiple phosphorylation methods failing to
consume the starting material. The key breakthrough by Shirota, Hakamata, and
Goda (2003) was the discovery and exploitation of a zwitterionic
N,O-dibenzyl phosphate intermediate that enabled gram-scale synthesis without
chromatographic purification.

## The Phosphorylation Challenge

Converting psilocin to psilocybin requires introducing a phosphate group at
the 4-position of the indole ring. The challenge is threefold:

1. **Selectivity**: The 4-hydroxy group must be phosphorylated without
   affecting the indole nitrogen or the tertiary amine.
2. **Purification**: Psilocybin is highly polar, making isolation from
   reaction mixtures difficult without chromatography.
3. **Yield**: Previous methods gave poor yields (20–47%) and required
   anion-exchange resin purification.

Several phosphorylation methodologies were screened. Most failed to consume
psilocin entirely. Two approaches showed partial success: the phosphoryl iodide
method (using tribenzyl phosphite, I₂, and DMAP) and the pyrophosphate method
(using tetrabenzylpyrophosphate and n-BuLi). The pyrophosphate method was
selected for scale-up due to easier handling and reagent stability.

## The Unexpected Intramolecular Rearrangement

The pyrophosphate method was expected to produce the neutral O,O-dibenzyl
phosphate intermediate (7). After the standard aqueous workup to remove excess
reagents, the ¹H NMR spectrum in CDCl₃ showed complicated signals. TLC revealed
an additional spot at the origin, and the whitish material no longer dissolved
in CH₂Cl₂ — behavior inconsistent with the expected neutral compound.

Nichols and Frescas had previously reported similar observations, concluding
that "hydrolytic cleavage of one of the O-benzyl groups rapidly occurred and
the resulting zwitterionic O-monobenzyl phosphate was obtained as a mixture."
Shirota's team isolated a single compound (8) by preparative reversed-phase HPLC
and subjected it to comprehensive 2D NMR analysis.

## Structural Elucidation by NMR

The zwitterion was not simply an O-monobenzyl phosphate as previously assumed.
Full structural characterization revealed a more complex intramolecular
rearrangement:

### ¹H and ¹³C NMR (CD₃OD)
- Two sets of benzyl groups present in the molecule
- Psilocin core signals intact
- N-benzyl methylene shifted to high field: δ 4.56 (2H, s) — characteristic
  of a benzyl group attached to a quaternary ammonium ion
- O-benzyl methylenes at δ 4.98 (1H, s) and 4.96 (1H, s) — diastereotopic
  protons on a chiral phosphate center
- N,N-dimethyl and methylene protons on the psilocin core shifted to low
  field compared to free psilocin — consistent with the positive charge

### HMBC (Heteronuclear Multiple Bond Correlation)
The key HMBC experiment showed that one benzyl group was directly linked at
the nitrogen of the N,N-dimethyl group, forming a quaternary ammonium ion.
This confirmed that the benzyl group did not simply hydrolyze off — it
migrated from oxygen to nitrogen.

### NOESY (Nuclear Overhauser Effect Spectroscopy)
NOESY correlations supported the assigned linkages, confirming the spatial
proximity relationships expected for the zwitterionic structure.

### ³¹P NMR
Confirmed the presence of the phosphate moiety with a characteristic
chemical shift consistent with a monoanionic phosphate.

## Proposed Rearrangement Mechanism

The transformation proceeds as follows:
1. Psilocin reacts with tetrabenzylpyrophosphate to form the neutral
   O,O-dibenzyl phosphate (7).
2. During aqueous workup, one O-benzyl group is hydrolytically cleaved,
   generating a monoanionic phosphate.
3. The free benzyl cation (or equivalent electrophile) is captured by the
   tertiary amine nitrogen of the N,N-dimethyltryptamine side chain.
4. The result is a zwitterion: a positively charged quaternary ammonium
   (N-benzyl-N,N-dimethyl) and a negatively charged phosphate
   (O-benzyl phosphate) on the same molecule.

## Practical Significance of Zwitterion Formation

The zwitterionic nature of intermediate 8 is what makes the entire synthesis
practical at scale:

**Solubility switch**: Unlike neutral compound 7, zwitterion 8 is insoluble
in CH₂Cl₂. This allows isolation by simple filtration rather than
chromatography.

**Purification by washing**: After suspending the worked-up reaction mixture
in CH₂Cl₂ overnight (to allow complete conversion to the zwitterion), the
precipitated white solid is collected by filtration. Excess dibenzyl phosphate
(the byproduct) is removed by washing with CH₂Cl₂, in which it is soluble
but the zwitterion is not.

**High yield**: The zwitterion is isolated in over 85% yield — remarkably
clean for a reaction that previously gave complex mixtures.

## Final Hydrogenolysis

Catalytic hydrogenolysis (H₂, Pd/C catalyst, methanol, room temperature)
cleaves both benzyl groups simultaneously from the zwitterion:
- The N-benzyl group is removed, regenerating the tertiary amine
- The O-benzyl group is removed, yielding the free phosphoric acid (psilocybin)

The product crystallizes directly from the reaction mixture as white needles.
Overall isolated yield from psilocin exceeds 72%.

## Broader Implications for Phosphorylation Chemistry

The Shirota zwitterion illustrates an important principle in phosphorylation
chemistry: reactions involving benzyl-protected phosphates and tertiary amine
substrates can undergo unexpected intramolecular benzyl migration from oxygen
to nitrogen during aqueous workup. This rearrangement, rather than being a
complication to avoid, can be exploited as a purification strategy — the
zwitterion's contrasting solubility properties enable isolation without
chromatography.

This approach may be applicable to the synthesis of other phosphorylated
tryptamines or phosphorylated indole alkaloids where similar purification
challenges exist.

## See Also

- [[pihkal-introduction-and-methodology]]

- [[dmt-phenomenology-and-tryptamine-hypercontinuum]]

See also: [[intramolecular-benzyl-migration-zwitterionic-phosphate-psilocybin-synthesis]]
