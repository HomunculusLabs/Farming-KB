---
title: Fungal Biodiversity Similarity Indices Beta Diversity
source: unknown-biodiversity-of-fungi.md
tags: [fungi,  biodiversity,  beta-diversity,  similarity-indices,  ecology,
community]
created: 2026-05-11
---

# Fungal Biodiversity: Similarity Indices and Beta Diversity

Quantifying how fungal communities differ from one another — across [[fungal-adaptations-environmental-gradients]],
between habitat types,
or among geographic regions — requires appropriate measures of community similarity and dissimilarity.
These measures,  collectively referred to as beta diversity metrics,
are fundamental tools in fungal ecology.
They allow researchers to test hypotheses about the [[duggar-mushroom-environmental-factors-temperature-moisture-light]] that shape fungal communities,
to compare the effects of different management practices on fungal diversity,
and to track changes in fungal communities over time.

## Alpha, Beta, and Gamma Diversity

Before examining specific similarity indices,
it is important to distinguish between the three levels of diversity that ecologists measure.
Alpha diversity refers to the diversity within a single sampling unit or habitat — the number of species (richness) and their relative abundances (evenness) at a single site.
Gamma diversity is the total diversity across all sampling units combined — the total number of species in a landscape or region.
Beta diversity connects alpha and gamma diversity: it measures the variation in species composition among sampling units.

Formally,
beta diversity can be defined as the ratio of gamma diversity to alpha diversity (Whittaker's multiplicative definition) or as the difference between gamma and mean alpha diversity (additive definition).
In practice,
beta diversity is most commonly measured using pairwise similarity or dissimilarity indices that compare the species composition of two communities,
or through multivariate methods that analyze the complete set of pairwise comparisons among all communities in a study.

## Why Beta Diversity Matters for Fungi

Fungal beta diversity is particularly important because fungal communities are often highly heterogeneous across space,
even at relatively small scales.
A soil sample taken from one square meter may harbor a completely different fungal community than a sample taken from an adjacent square meter.
This fine-scale spatial heterogeneity reflects the complex interactions between fungal life history strategies,
dispersal limitations,  microhabitat variation,
and competitive dynamics that structure fungal communities.

Understanding the patterns and drivers of fungal beta diversity has practical implications for agriculture,
forestry,  conservation,  and ecosystem management.
The degree to which fungal communities differ between managed and unmanaged habitats can indicate the ecological impacts of land use practices.
The similarity between fungal communities in different geographic regions can reveal biogeographic patterns and dispersal barriers.
And changes in beta diversity over time can signal shifts in [[dighton-mycorrhizal-diversity-ecosystem-function]] or stability.

## Binary (Presence-Absence) Similarity Indices

### Jaccard Index

The Jaccard index is one of the oldest and most widely used similarity coefficients in ecology.
For two communities A and B,
it is calculated as the number of species shared between them (the intersection) divided by the total number of species present in either community (the union): J = a / (a + b + c),
where a is the number of species shared,
b is the number of species unique to community A,
and c is the number of species unique to community B.

The Jaccard index ranges from 0 (no species in common) to 1 (identical species composition).
It considers only presence or absence of species,  not their abundances,
making it appropriate for studies where abundance data are unreliable or unavailable — a common situation in fungal studies where species detection frequencies may be influenced more by sampling effort and detection probability than by true abundance differences.

### Sørensen-Dice Index

The Sørensen (or Dice) index is closely related to Jaccard but gives greater weight to shared species: S = 2a / (2a + b + c).
Compared to the Jaccard index,
the Sørensen index produces higher similarity values for the same pair of communities because the shared species count is effectively doubled in the numerator.
The choice between Jaccard and Sørensen is often a matter of convention within particular research traditions,
and both are widely used in fungal ecology.

### Other Binary Indices

Several other binary similarity indices exist,
each with slightly different weighting of shared and unique species.
The Simpson index gives more weight to dominant (widely distributed) species.
The Ochiai index uses a geometric mean approach.
The Kulczyński index incorporates abundance information in a asymmetric form.
The choice among these indices should be guided by the specific ecological questions being asked and the characteristics of the data.

## Quantitative (Abundance-Based) Indices

### Bray-Curtis Dissimilarity

The Bray-Curtis dissimilarity coefficient is the most widely used quantitative measure of community dissimilarity in fungal ecology and in ecology generally.
Unlike the binary indices,
Bray-Curtis incorporates information about species abundances (or surrogate measures such as colony counts,
DNA sequence read counts,
or [[growing-gourmet-mushrooms-species-sequencing-substrate-utilization]] scores): BC = 1 - (2W / (A + B)),
where W is the sum of the lesser abundances for each species,
and A and B are the total abundances in each community.

Bray-Curtis dissimilarity ranges from 0 (identical communities with identical abundances) to 1 (no species in common).
It is particularly popular in fungal ecology because it is intuitive to interpret,
robust to sampling variation,
and performs well in ordination analyses such as non-metric multidimensional scaling (NMDS) and principal coordinates analysis (PCoA).

### Morisita-Horn Index

The Morisita-Horn index is another abundance-based similarity measure that is particularly sensitive to the most abundant species in the communities being compared.
It is calculated based on the probability that two individuals randomly selected from the combined communities will belong to the same species.
The Morisita-Horn index is useful when the dominant species in fungal communities are of particular ecological interest,
but it can be sensitive to sample size effects.

## Distance-Based Measures

In addition to similarity and dissimilarity indices,
several distance-based measures are used to quantify differences between fungal communities.
Euclidean distance,  Manhattan distance,
and chi-square distance can all be applied to [[core-endorhiza-bacterial-community-composition-cannabis]] data,
though each makes different assumptions about the nature of the data and the appropriate way to weight rare versus common species.

The choice of distance measure can significantly affect the results of multivariate analyses.
Euclidean distance,  for example,
is sensitive to the absolute abundance of species and may be dominated by a few highly abundant species.
Chi-square distance,  used in correspondence analysis,
gives more weight to rare species.
Researchers should carefully consider which distance measure is most appropriate for their data and questions.

## Ordination and Visualization

Similarity and dissimilarity matrices generated by these indices are typically analyzed using ordination techniques that reduce the multidimensional community data to a small number of axes that capture the major patterns of variation.
Non-metric multidimensional scaling (NMDS) is the most widely used ordination method in fungal community ecology because it makes minimal assumptions about the distribution of the data and works well with both binary and quantitative dissimilarity measures.

Principal coordinates analysis (PCoA,
also called metric multidimensional scaling) is another common approach that preserves the metric properties of the dissimilarity matrix.
Canonical correspondence analysis (CCA) and redundancy analysis (RDA) are constrained ordination methods that relate community composition to environmental variables,
allowing researchers to test hypotheses about the drivers of fungal community variation.

## Challenges Specific to Fungal Studies

Fungal biodiversity studies face several challenges that complicate the application of standard beta diversity methods.
Detection probability varies dramatically among fungal species depending on their life history,
growth form,  and detectability by the chosen sampling method.
Molecular methods detect DNA from dead or dormant organisms as well as active ones,
potentially inflating diversity estimates.
And the lack of comprehensive species inventories for most fungal groups means that many detected sequences cannot be reliably assigned to known species,
forcing researchers to work with operational taxonomic units (OTUs) or amplicon sequence variants (ASVs) rather than named taxa.

## See Also

- [[fungal-molecular-methods-apcr-rdna-biodiversity]]
- [[fungal-kingdom-phylogeny-classification-overview]]
- [[environmental-dna-metabarcoding-fungi]]
- [[fungal-diversity-indices-community-analysis]]
