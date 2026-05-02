---
title: Backcrossing and Inbreeding Techniques
created: 2026-04-26
updated: 2026-04-24
sources:
  - raw/papers/vic-high-creating-true-breeding-strains.md
type: concept
tags: [reference]
---

# Backcrossing and Inbreeding Techniques

Vic High provides detailed analysis of two major inbreeding strategies used in cannabis breeding: backcrossing (also called cubing) and generational (filial) inbreeding. Each technique manipulates gene frequencies differently and produces distinct outcomes that breeders must understand to choose the right approach for their goals.

## Backcrossing (Cubing) Defined

Backcrossing involves breeding an individual with its own progeny. In cannabis breeding culture, successive backcrosses to the same parent have specific names:

- **First backcross (B1)**: Offspring crossed back to the original P1 parent.
- **Second backcross (B2) / Squaring**: Progeny from B1 crossed back to the same P1 parent (now a grandparent).
- **Third backcross (B3) / Cubing**: Progeny from B2 crossed back to the same P1 parent (now a great-grandparent).

"Cubing" specifically refers to three backcrosses -- the term derives from the number three, not from any mathematical cubing operation. Further backcrosses beyond three continue to increase gene frequency but are simply called backcrossing.

## Gene Frequency Math in Backcrossing

The gene pool composition after each backcross follows a predictable mathematical pattern based on averaging the gene frequencies of both parents. Starting with a P1 mom (100% of target genes) crossed with an unrelated male (0% of target genes):

- F1 generation: (100% + 0%) / 2 = 50% of P1 genes
- First backcross (B1): (100% + 50%) / 2 = 75%
- Second backcross / Squaring (B2): (100% + 75%) / 2 = 87.5%
- Third backcross / Cubing (B3): (100% + 87.5%) / 2 = 93.75%

This same probability math applies to specific genes and traits, with dramatic effects on methodology and selection. The more males used with each cross, the better the chance that reality matches the theory.

## Cubing a Dominant Heterozygous Trait

When the desired trait is dominant and the P1 mom is heterozygous (Pp), cubing with random male selection produces limited results. Since the P1 is Pp and the male is unrelated (assumed PP for the dominant pine flavour), the F1 cross yields:

- F1 = Pp x PP = Pp + Pp + Pp + Pp (all heterozygous)

Wait -- in Vic High's model, the male is from the general population and is homozygous for the common pine flavour. If pineapple is dominant, the male is pp (homozygous recessive for the dominant trait means it lacks the dominant allele). The F1 cross is:

- F1 = Pp x pp = Pp + Pp + pp + pp
- 50% express pineapple flavour, P gene frequency is 25%.

Since males cannot be phenotyped for flavour, they are selected randomly. From the F1 males, only 25% of pollen grains carry the P gene. The first backcross (B1) produces:

- B1 = Pp x (random F1 males) yields roughly 56.25% pineapple phenotype.
- Second backcross (B2/Squaring): 68.75% pineapple, P gene frequency 43.75%.
- Third backcross (B3/Cubing): 71.875% pineapple, only 22% true breeding (PP), P gene frequency approximately 47%.

### The Critical Limitation

If backcrossing continued indefinitely with random male selection and large populations, the P gene frequency would max out at 50%. This means:

- Best case: 25% true breeding for pineapple flavour.
- Best case: 75% display pineapple flavour.
- You would never be rid of the 25% that maintain the pine flavour.

This model holds true when trying to cube any heterozygous trait. No amount of additional backcrossing can break through this ceiling without deliberate selection.

## Improving Cubing With Selection

Vic High demonstrates the impact of applying selective pressure. If homozygous recessive (pp) individuals are removed before each backcross (removing the pine-flavoured plants that can be identified), but heterozygous (Pp) individuals cannot be distinguished from homozygous dominant (PP) ones:

- After F1 with selection: breeding pool becomes Pp x Pp (only pineapple-flavoured F1 individuals used).
- First backcross with selection: P gene frequency rises from 37.5% to 66.7%.
- Second backcross with selection: P gene frequency rises to 58%.
- Third backcross (cubing) with selection: 95% express pineapple, 35% true breeding, P gene frequency 60%.

Selection nearly doubles the true breeding rate (from 22% to 35%) and dramatically improves the phenotypic outcome (from 72% to 95%).

## Cubing a Recessive Homozygous Trait

When the desired trait is recessive and the P1 mom is homozygous (pp), the outcome is dramatically better because the P1 can only contribute the desired allele:

- F1 = pp x PP = Pp + Pp + Pp + Pp (all identical, 0% express pineapple, but p gene frequency is 50%).
- B1 = pp x Pp = Pp + Pp + pp + pp (50% pineapple, p gene frequency 75%).
- B2/Squaring: 75% pineapple, p gene frequency approximately 88%.
- B3/Cubing: approximately 88% pineapple AND true breeding, p gene frequency approximately 94%.

If backcrossing continued indefinitely, the gene frequency would approach but never quite reach 100%.

## Generational (Filial) Inbreeding

Generational inbreeding involves crossing individuals from the same generation rather than backcrossing to a parent. The P1 parents produce F1 offspring, F1 crossed together produces F2, F2 produces F3, and so on.

### Full-Sib Cross (Both Parents Selected)

Both male and female parents are selected for the desired phenotype, providing maximum selection pressure.

For a dominant trait (starting with Pp x pp):

- F2 = Pp x Pp = PP + Pp + Pp + pp (75% pineapple, 50% P gene frequency).
- F5 (with continued full-sib selection): 96% pineapple, 80% P gene frequency.

For a recessive trait (starting with pp x PP):

- F2 = Pp x Pp = PP + Pp + Pp + pp (25% pineapple, 50% p gene frequency).
- F3 = pp x pp = pp + pp + pp + pp (100% true breeding, complete fixation in 3 generations).

### Half-Sib Cross (Only Females Selected)

Only females are selected; males are used randomly because desirable traits like flavour cannot be assessed in male plants.

For a dominant trait:

- F2: 62.5% pineapple, 37.5% P gene frequency.
- F5: 87% pineapple, 63.5% P gene frequency.

For a recessive trait:

- F3: 50% pineapple, 75% p gene frequency.
- F5: 87.5% pineapple, 93.75% p gene frequency.

## Comparing the Strategies

| Scenario | Cubing (3 BC) | Full-Sib F5 | Half-Sib F5 |
|----------|--------------|-------------|-------------|
| Recessive homozygous source | 88% true breeding | 100% (by F3) | 87.5% true breeding |
| Dominant heterozygous (no selection) | 22% true breeding | -- | -- |
| Dominant heterozygous (with selection) | 35% true breeding | 96% phenotype | 87% phenotype |

## Population Size and Selection Pressure

The models assume large population sizes and random matings. In practice:

- Smaller populations increase unintended selective pressure through genetic drift.
- Fewer males used per cross means less predictable outcomes.
- More males per cross increases the chance that reality matches theoretical predictions.
- The significance of population size is greatest when cubing heterozygous traits.
- The examples only account for single gene pairs; real traits involve multiple genes where probabilities multiply.

## Key Takeaways

- Cubing progressively increases P1 gene contribution: 50% to 75% to 87.5% to 93.75%.
- Cubing cannot create a true breeding strain from a heterozygous dominant source -- gene frequency caps at 50%.
- Cubing a homozygous recessive source is highly effective, producing 88% true breeding offspring.
- Selection against identifiable undesired individuals nearly doubles cubing effectiveness.
- Full-sib generational inbreeding achieves faster and more complete stabilization than half-sib.
- Full-sib inbreeding can achieve 100% fixation for recessive traits by F3.
- Male selection is the single largest factor determining generational inbreeding success.
- Population size directly affects how closely real outcomes match theoretical predictions.
- All models assume single gene traits; real polygenic traits compound the probabilities.
- [[vic-high-true-breeding-strain-development-stabilization]]
- [[vic-high-cannabis-phenotype-selection-criteria]]
- [[green-cannabis-grow-bible-strain-selection-genetics]]
- [[cannabis-phenotype-selection]]
