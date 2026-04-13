---

title: Cannabis Breeding Strategies
created: 2026-04-11
updated: 2026-04-12
type: concept

tags:
- cannabis
- regenerative
- indoor
- lighting
- genetics
- species
- classification
- lighting-hardware

sources:
- raw/papers/greg-green-the-cannabis-grow-bible.md
- raw/papers/robert-c-clarke-marijuana-botany-an-advanced-study.md
- raw/papers/vic-high-creating-true-breeding-strains.md
---

# Cannabis Breeding Strategies

Advanced breeding strategies from Vic High's guide to creating true-breeding strains, plus cannabis species classification, chemotypes, and practical breeding tips. See [[cannabis-genetics-and-breeding]] for foundational genetics terminology, test crosses, IBL creation, backcrossing, and cubing basics.

## Detailed Breeding Strategies (Vic High)

### Gene Frequency: The Core Concept

All breeding is fundamentally about **manipulating gene frequencies** in a population. Gene frequency is the percentage of a population that carries a specific gene. A "fixed" trait means 100% gene frequency — every individual is homozygous for it. A true breeding strain (IBL) is a population where the key target traits are all or nearly fixed.

### Cubing Explained in Detail

**Backcrossing** = breeding offspring back to the original parent. The naming convention:
- **BX1** (1st backcross): 75% of genepool matches the P1 parent
- **BX2** ("squaring"): 87.5% matches P1
- **BX3** ("cubing"): 93.75% matches P1
- Continue: each additional backcross halves the remaining distance to 100%

Formula: take the average of the two parents' gene frequencies. P1 mom = 100%, F1 dad = 0% → BX1 = (100+0)/2 = 50%. Then BX2 = (100+50)/2 = 75%. Wait — Vic High counts from the initial cross differently. The key math: **BX(n) gene frequency = 100% - (100% / 2^n)**.

**Critical caveat — cubing a heterozygous trait plateaus at 50%:**
- If the P1 mom is heterozygous (Pp) for a dominant trait, random male selection means the maximum achievable P gene frequency approaches only 50%
- This means at best 25% of cubed offspring will be true breeding — cubing alone cannot fix a heterozygous trait
- **Cubing a homozygous recessive trait is much more effective** — achieves ~88% true breeding after BX3 with 94% gene frequency

**Polygenic traits compound the difficulty:**
- If a trait involves 2 recessive genes: 87.5% × 87.5% = 76.6% success
- 2 recessive + 1 heterozygous dominant: 87.5% × 87.5% × 71.9% = 55% success
- As gene count increases, success drops dramatically without selective pressure

### Applying Selective Pressure

**The most important breeding tool is intentional selection:**
- Remove individuals showing unwanted recessive traits BEFORE each backcross
- For dominant traits: removing homozygous recessives (pp) before each backcross improves true-breeding rate from 22% to 35% and overall trait expression from 72% to 95%
- Select males carefully — males carry hidden genes you cannot observe in flowers
- Use **progeny testing**: grow out male offspring to evaluate which males pass on desired traits
- Never select based on superficial traits unrelated to your target (linked genes travel together on chromosomes)

**Gene linkage matters:** Cannabis has ~several thousand genes on only 10 chromosome pairs. Selecting for one trait may inadvertently select for or against hundreds of other genes on the same chromosome. Work on **one or two traits at a time**.

### Generational Inbreeding (F2, F3, F4, F5...)

An alternative to backcrossing: cross individuals within the same generation.

**Full-sib cross** (selecting both male and female parents):
- F2 from heterozygous dominant P1: 75% show trait, 50% gene frequency
- F5 with selection: 96% show trait, 80% gene frequency
- If selecting for a recessive trait where both parents can be identified: can achieve 100% true breeding by F3 (cross two pp individuals)

**Half-sib cross** (can only select females, males chosen randomly):
- Significantly slower — F5 with half-sib selection achieves only 87% trait expression vs. 96% full-sib
- Gene frequency reaches only 63.5% vs. 80% (dominant trait case)
- For recessive traits: half-sib F5 achieves 87.5% — same as cubing, but without the parent clone dependency

### Cubing vs. Generational Inbreeding: When to Use Which

| Factor | Cubing (Backcrossing) | Generational Inbreeding |
|--------|----------------------|------------------------|
| Best for | Preserving a clone's traits | Creating new combinations |
| Parent preservation | Need to keep P1 alive as clone | No parent needed after P1 |
| Speed (homozygous recessive) | ~88% true breeding in BX3 | 100% by F3 (full-sib) |
| Speed (heterozygous dominant) | Plateaus at 25% true breeding | Can reach higher with selection |
| Genetic diversity | Narrowing (bottleneck risk) | Some reassortment each generation |
| Risk | Inbreeding depression, clonal degradation | Inbreeding depression at F5+ |
| Male selection | Critical (can't observe flower traits) | Same challenge |

### Key Breeding Rules (Vic High)

1. **Cubing cannot fix heterozygous dominant traits** — use generational inbreeding instead
2. **Work on one trait at a time** — linked genes complicate multi-trait selection
3. **Recessive traits are easier to fix** — once visible, you know the genotype (pp)
4. **Male selection is the hardest part** — use progeny testing when traits can't be observed in males
5. **Population size matters** — small populations increase random genetic drift
6. **A true IBL takes many generations** — commercial "IBLs" in 1-2 years started with mostly stable genetics
7. **Document everything** — parent genotypes, gene frequencies, selection criteria, offspring ratios

## Cannabis Species and Chemotypes

### Species
- **Cannabis sativa** — tall, narrow leaflets, long flowering, uplifting effect
- **Cannabis indica** — short, broad leaflets, short flowering, relaxing effect
- **Cannabis ruderalis** — small, autoflowering, low THC, cold-tolerant

### Chemotype (Clarke)
- **Drug strain**: Genetically capable of converting CBDA to THCA — produces significant THC
- **Fiber strain**: Cannot convert CBDA to THCA — produces CBD but negligible THC
- The THC-to-CBD ratio is genetically determined; environment only modulates the expression

### Strain Selection for Indoor Growing (from S.T. Oner)
- Indicas: 6-9 week flowering, compact, ideal for indoor spaces
- Indica-dominant hybrids: 7-10 week flowering, good balance of yield and potency
- Sativa-dominant hybrids: 9-12+ week flowering, may need height management
- Pure sativas: 14-16+ week flowering, very difficult indoors, best in organic soil grows
- Autoflowers (ruderalis crosses): automatic flowering regardless of photoperiod

## Photoperiod and Genetics

Cannabis flowering is triggered by photoperiod — specifically the length of continuous darkness:
- Most strains flower when the dark period exceeds 12 hours
- Strains from equatorial regions (20 degrees latitude) are less photoperiod-sensitive and may flower based on age
- Strains from higher latitudes are more responsive to photoperiod change
- Cannabis measures darkness through phytochrome in the leaves, not at the shoot tip (see [[plant-perception]])

## Practical Breeding Tips

- Keep parent plants alive as clones — exact genetic material is preserved
- Work on one or two traits at a time rather than trying to lock down everything simultaneously
- Document every cross with parent info, date, and offspring observations
- When selecting males, consider pollen potency and similarity to the mother's traits
- The most important factor in THC production is the genotype — after that, provide adequate nutrients, light, and time for maturation


## See Also

- [[cannabis-genetics-and-breeding]] — Genetics fundamentals, test crosses, IBL, cubing
- [[cannabis-vegetative-stage]] — Vegetative growth management
- [[cannabis-flowering-stage]] — Flowering and sex expression
- [[seed-saving]] — Seed saving and storage
- [[cannabis-plant-nutrition]] — Nutrition for breeding stock
