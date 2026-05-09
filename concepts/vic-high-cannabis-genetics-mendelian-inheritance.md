---
title: Cannabis Genetics and Mendelian Inheritance
created: 2026-04-26
updated: 2026-04-24
sources:
  - raw/papers/vic-high-creating-true-breeding-strains.md
type: concept
tags: [cannabis]
---

# Cannabis Genetics and Mendelian Inheritance

Vic High's foundational text on cannabis breeding uses Mendelian genetics as the conceptual framework for understanding how traits are inherited, how gene frequencies shift across generations, and how breeders can manipulate these processes to create true breeding strains. The text simplifies complex genetics by using single-gene (monogenic) models to illustrate principles that scale to more complex multi-gene (polygenic) realities.

As Vic High notes, breeding is not a black-and-white subject, and it would be too complex to put on paper in an easily understood form. Therefore, small fictional examples are used to reinforce various concepts before applying them to real breeding projects. The assumption that flavour is monogenic, for instance, is used purely for pedagogical simplicity.

## Gene Pairs and Alleles

In Vic High's framework, cannabis traits are controlled by gene pairs -- one gene inherited from each parent. For example, a flavour gene pair might consist of one gene coding for pine flavour and another coding for pineapple flavour. Either gene in the gene pair can code for either of the flavours.

There are two fundamental states a gene pair can occupy:

- **Homozygous**: Both genes in the pair code for the same trait. A plant homozygous for pineapple flavour has two pineapple genes. Such an individual is considered true breeding for that trait because all its gametes will carry the same genetic information. It can only pass on one type of gene to its offspring.

- **Heterozygous**: The two genes in the pair code for different traits (one pine, one pineapple). The plant will express only the dominant trait, but its gametes will carry either gene randomly. A heterozygous individual is not true breeding because its offspring can inherit either version of the gene.

A homozygous individual is considered true breeding and a heterozygous individual is not. This distinction is the foundation of all breeding strategy.

## Dominant and Recessive Traits

Vic High illustrates inheritance using dominant and recessive flavour traits. In his notation, capital letters (P) represent dominant alleles and lowercase letters (p) represent recessive alleles. Convention is that the capital letter signifies dominance.

Since each individual has two flavour genes paired up, the possible genotypes are PP, Pp, and pp. The phenotype (observable trait) depends on which genes are present and their dominance relationship.

### When Pineapple Flavour Is Dominant

- PP and Pp both express pineapple flavour (phenotypically identical).
- Only pp expresses pine flavour.
- A plant showing pineapple flavour could be either homozygous (PP) or heterozygous (Pp).
- Since pineapple is a new flavour in the population, the special individual is likely heterozygous (Pp).

### When Pineapple Flavour Is Recessive

- Only pp expresses pineapple flavour.
- PP and Pp both express pine flavour.
- Any plant showing pineapple flavour must be homozygous (pp).

This distinction has profound implications for breeding strategy. When a desirable trait is recessive, finding a single individual expressing it guarantees that individual is homozygous. When a trait is dominant, a plant expressing it could be either homozygous or heterozygous, making selection less straightforward.

## Punnett Squares and Genotypic Ratios

The text uses Punnett squares extensively to predict offspring ratios. The classic Mendelian cross of two heterozygous parents produces what Vic High calls the "typical Mendelian phenotypic 3:1 and genotypic 1:2:1 ratios":

- F2 cross = Pp x Pp = PP + Pp + Pp + pp
- 75% (3/4) express the dominant trait, 25% (1/4) express the recessive trait.
- 25% are homozygous dominant, 50% are heterozygous, 25% are homozygous recessive.

## Mathematical Shortcut for Punnett Squares

Vic High develops a mathematical shortcut for calculating Punnett square outcomes without drawing them. By expressing each parent's gene pool as a frequency (e.g., 3P2p x 3P5p), the offspring ratios can be computed algebraically by multiplying each combination:

- 3P2p x 3P5p = (3x3)PP + (3x5)Pp + (2x3)Pp + (2x5)pp
- = 9PP + 15Pp + 6Pp + 10pp
- = 9PP + 21Pp + 10pp

The total offspring count equals the product of the gene pool sizes:

(3+2) x (3+5) = 40, which matches the sum from the Punnett square.

This method becomes essential when tracking gene frequencies across multiple generations where literal Punnett squares become unwieldy. Vic High demonstrates this by calculating F4 and F5 generation outcomes that would require enormous Punnett grids but are straightforward with the algebraic method.

## Gene Frequency: The Central Metric

The most important concept in Vic High's framework is gene frequency -- the ratio or percentage of a population's total gene pool that carries a specific allele. This is the fundamental measure of breeding success.

Gene frequency is calculated as the number of a specific gene divided by the total genes in the gene pool. For example, in a population of 50 plants each with one gene pair for flavour, the gene pool contains 100 flavour genes. If 60 code for pineapple flavour, the gene frequency is 60%.

A trait is considered **fixed** when its gene frequency reaches 100%.

Vic High states this explicitly: "all you are really doing is manipulating gene frequencies. Therefore, to ever really understand what is happening in any breeding project, the breeder must pay attention to gene frequencies and assess how his selective pressures and models are influencing them. They are his measure of success."

## Gametes and Sexual Reproduction

Heterozygous individuals produce gametes (pollen or ovules) that can carry either allele. Homozygous individuals produce gametes carrying only one allele. This is the mechanism that creates variation in offspring and the raw material that breeders work with through selection.

The frequency of each gene in the gamete pool directly determines the genetic composition of the next generation. An F1 generation that is all Pp will generate pollen containing one P gene for every p gene -- a 50:50 ratio that directly shapes the next generation's genetic makeup.

## Gene Frequency in Decimal Form

For complex multi-generational calculations, Vic High switches from fractions to decimals. The conversion is straightforward: each genotype ratio becomes a decimal by dividing by the total. For example, a genepool of 1521PP + 2418Pp + 861pp (total 4800) becomes:

- 1521/4800 = 0.32 PP
- 2418/4800 = 0.50 Pp
- 861/4800 = 0.18 pp

The gene frequency for P in this genepool is (0.32 + 0.25) / 1 = 0.57, and since p = 1 - P, the frequency of p is 0.43. This decimal approach makes complex cross calculations manageable.

## The Heterozygous Individual as Starting Point

Vic High emphasises that when a new desirable trait appears in a population (such as pineapple flavour in a pine-flavoured population), the individual expressing it is likely heterozygous if the trait is dominant. This is because the trait is new and rare -- the probability of two copies coming together is low. This assumption underpins many of the breeding models in the text and explains why dominant traits are harder to stabilise than recessive ones.

For recessive traits, the situation reverses: any individual expressing the trait must be homozygous, which makes it immediately valuable as a breeding parent.

## From Monogenic to Polygenic Reality

While the models use single-gene assumptions for clarity, Vic High repeatedly emphasises that real cannabis traits are polygenic (controlled by multiple gene pairs). The principles demonstrated with single genes apply to multi-gene traits, but the math compounds:

- For a trait influenced by two recessive genes, each fixed individually at 87.5%: 87.5% x 87.5% = 76.6%.
- Adding a third gene (two recessive, one heterozygous dominant): 87.5% x 87.5% x 71.9% = 55%.
- Going from one to three genes drops the success rate from 87.5% to just 55%.

This compounding effect means that as genetic complexity increases, the probability of achieving desired outcomes decreases dramatically without deliberate selection pressure.

## Key Takeaways

- All cannabis breeding is fundamentally the manipulation of gene frequencies within a population.
- Homozygous individuals are true breeding; heterozygous individuals are not.
- Dominant traits can hide recessive genetic information, complicating selection.
- Single-gene Mendelian models illustrate principles that scale to polygenic reality, where probabilities multiply.
- Gene frequency is the breeder's primary metric for measuring progress toward any breeding goal.
- Mathematical shortcuts allow breeders to predict outcomes across multiple generations.
- The polygenic nature of real cannabis traits means breeding success rates compound negatively with each additional gene pair.
- Decimal notation simplifies complex multi-generational gene frequency calculations.
- [[cannabis-true-breeding-ibl-strains]]
- [[cannabis-phenotype-and-genotype-guide]]
- [[cannabis-chromosomes-and-mendelian-inheritance]]

- [[vic-high-cannabis-polyhybrid-crosses-and-f1-stability]]
- [[vic-high-selfing-and-regular-seed-production]]
