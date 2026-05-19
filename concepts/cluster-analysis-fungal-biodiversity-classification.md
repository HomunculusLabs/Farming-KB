---
title: Cluster Analysis for Fungal Biodiversity Classification
source: unknown-biodiversity-of-fungi.md, Chunk 21
type: concept
---

## Cluster Analysis for Fungal Biodiversity Classification

## Overview

Cluster analysis is a multivariate statistical technique whose fundamental objective is to group objects into subgroups (clusters) such that objects within a subgroup are more similar to each other than to objects in other subgroups. In [[fungal-biodiversity]] studies, these "objects" are typically sampling sites, plots, or fungal taxa described by ecological, morphological, or molecular characters. The method provides a structured, data-driven means of revealing patterns of similarity among fungal assemblages that may not be apparent from raw species-abundance data alone.

As an exploratory technique, cluster analysis generates a descriptive summary of data structure rather than hypothesis tests, making it well suited to pilot studies and situations where prior ecological knowledge is limited. The technique has been widely applied in mycological surveys to identify fungal community types associated with particular habitat conditions, host species, or disturbance regimes (Sneath and Sokal 1973; Gauch 1982).

## Dissimilarity Matrices: The Foundation of Clustering

All hierarchical clustering procedures begin with a dissimilarity (or distance) matrix — a square, symmetric table in which each entry quantifies the pairwise ecological distance between two objects. The diagonal is zero (each object is identical to itself), and off-diagonal entries range from small values (high similarity) to large values (low similarity). The full set of pairwise values captures the multivariate [[acidifying-pollutants-mycorrhizal-community-structure]] in a compact representation.

This matrix serves as the sole input to most clustering algorithms; once it is computed, the original species-by-sites data matrix is no longer used directly by the clustering routine. The quality of the dissimilarity matrix therefore determines the quality of the resulting clusters.

### Choosing the Right Resemblance Function

The choice of resemblance function used to construct the [[bray-curtis-dissimilarity]] is of paramount importance, as it fundamentally shapes the clustering outcome. Different resemblance measures emphasise different aspects of [[mycorrhizal-effects-on-plant-community-composition]], and the selection of an inappropriate measure can lead to misleading or biologically meaningless results (van Tongeren 1995).

Presence/absence-based coefficients such as the Jaccard similarity index treat all species equally regardless of abundance. Two sites sharing the same species set are considered maximally similar even if one is dominated by a single species and the other has an even distribution. By contrast, [[fungal-biodiversity-quantitative-indices]] such as the Morisita Horn index place greater weight on dominant species and are more sensitive to [[species-abundance-distribution]] structure differences.

As illustrated in reference figures (Fig. 5.3), applying Jaccard versus Morisita-Horn to the same fungal community dataset can produce markedly different dendrogram topologies, leading to different ecological interpretations. The Jaccard-based dendrogram might group sites primarily by species composition, while Morisita-Horn might group them by dominance patterns. Selecting a resemblance measure appropriate for the data type (binary vs. quantitative) and the ecological question is therefore a critical first step that should be guided by both statistical properties and ecological reasoning.

## Data Preparation Considerations

Before constructing a dissimilarity matrix, researchers must make several decisions about data preparation that can influence clustering results. These include whether to transform [[species-abundance-distribution]] data (e.g., square-root or log transformations to downweight dominant species), whether to standardise sampling units by total abundance or area, and how to handle rare species that occur in only one or two samples.

Rare species can contribute noise to the dissimilarity matrix and may cause spurious cluster separation; some analysts prefer to remove species occurring in fewer than a threshold number of samples before analysis. However, this must be balanced against the risk of discarding ecologically informative rare taxa that may characterise particular habitat types. Data transformations can also have a substantial effect on the resulting dissimilarity values and should be chosen carefully.

## Dendrogram Interpretation

The output of hierarchical cluster analysis is a dendrogram — a branching tree diagram representing the sequence in which objects are fused into clusters. Dendrograms are the primary tool for communicating cluster analysis results in mycological and ecological publications, and correct interpretation is essential.

### Branch Length and Similarity

In a dendrogram, the length of branches connecting two objects or clusters is inversely proportional to their similarity: short branches indicate high similarity (early fusion at low dissimilarity), while long branches indicate low similarity (late fusion near the top of the tree). The height at which two branches meet is the dissimilarity value at which those clusters were joined.

Reading a dendrogram from bottom to top reveals the progressive aggregation of increasingly dissimilar groups. A well-structured dendrogram for fungal community data typically shows clear groupings of ecologically similar sites separated by long branches from other groups.

### Information Loss in One-Dimensional Representation

Because the dendrogram compresses all pairwise dissimilarities into a single hierarchical ordering, some information is inevitably lost when complex multidimensional relationships are forced into a tree structure. Two objects equidistant from a third in multidimensional space may appear at very different positions in the dendrogram, depending on the constellation of other objects in the analysis.

This information loss is an inherent limitation of cluster analysis and underscores the value of complementing clustering with ordination techniques, which preserve more continuous variation in the data and do not force discrete group boundaries. Researchers should be cautious about over-interpreting the apparent discreteness of clusters shown in a dendrogram.

## The Wide Variety of Clustering Methods

Cluster analysis encompasses a wide variety of methods, classifiable along several independent axes (Sneath and Sokal 1973). Understanding these distinctions is important for selecting an appropriate algorithm and interpreting resulting dendrograms correctly.

### Agglomerative vs. Divisive

Agglomerative (bottom-up) methods begin with each object as its own cluster and progressively fuse the most similar pairs until all objects are united in a single cluster. Divisive (top-down) methods start with one cluster containing all objects and successively partition it. Most ecological applications use agglomerative methods for computational simplicity; divisive methods require a criterion for choosing partitions at each step, which is less straightforward for ecological data.

### Hierarchic vs. Nonhierarchic

Hierarchic methods produce nested partitions (the dendrogram), where each cluster is contained within a larger cluster at the next higher level. Nonhierarchic methods (e.g., k-means) assign objects to a predetermined number of clusters without implying nesting. Nonhierarchic methods are useful when group number is known a priori but lack the visual summary dendrograms provide.

### Overlapping vs. Nonoverlapping

Most methods produce nonoverlapping (hard) clusters where each object belongs to exactly one group. Overlapping (fuzzy) clustering allows shared membership among multiple clusters, reflecting the reality that many fungal communities represent gradients rather than discrete types. This distinction is particularly relevant in [[fungal-ecology]], where community composition often changes gradually across [[fungal-adaptations-environmental-gradients]].

### Sequential vs. Simultaneous

Sequential algorithms build the solution one fusion at a time, each step depending on the previous. Simultaneous algorithms optimise the entire cluster configuration at once, which can yield more globally optimal but computationally demanding solutions. Agglomerative methods are inherently sequential, while some optimisation-based approaches are simultaneous.

### Weighted vs. Unweighted

Weighted methods allow clusters of unequal size to contribute equally to subsequent fusions. Unweighted methods weight clusters in proportion to their object count. This choice can significantly affect results when cluster sizes are unequal — a common situation in fungal surveys where some habitats support many more species than others.

### Adaptive vs. Nonadaptive

Adaptive methods adjust their strategy based on data structure encountered during analysis (e.g., switching fusion rules in different dendrogram regions). Nonadaptive methods apply a fixed rule throughout — simpler but potentially less effective for heterogeneous data. Adaptive methods are less commonly used in standard ecological software but offer theoretical advantages for complex community datasets.

## UPGMA: The Most Common Approach

Among agglomerative hierarchic methods, UPGMA (Unweighted Pair Group Method using Arithmetic Averages) is by far the most widely used in fungal ecology and biodiversity studies (Gauch 1982). UPGMA iteratively merges the two most similar clusters and recomputes average dissimilarity to all remaining clusters using an arithmetic mean. It treats all clusters equally regardless of size — the average is unweighted by cluster size.

UPGMA is computationally straightforward, easy to interpret, and produces an ultrametric dendrogram — branch lengths are additive and tips are aligned at the same level. This ultrametric property suits it to ecological [[distance-coefficients-fungal-community-comparison]] that approximately satisfy the ultrametric condition.

However, UPGMA assumes a constant rate of divergence among all lineages; when this assumption is violated, branch lengths may not accurately reflect true dissimilarities. Users should be aware of this limitation, particularly when community turnover rates vary substantially across the study area.

## Assessing Dendrogram Accuracy: The Cophenetic Correlation Coefficient

Because cluster analysis involves successive approximation, evaluating how faithfully the dendrogram represents the original dissimilarity matrix is essential. The cophenetic correlation coefficient (Sokal and Rohlf 1962) provides a quantitative measure of this fidelity.

The cophenetic distance between two objects is defined as the dissimilarity level at which they first join the same cluster in the dendrogram. The cophenetic correlation is the Pearson product-moment correlation between original dissimilarity values and the cophenetic distances. A high value (typically > 0.80) indicates the dendrogram preserves dissimilarity structure well; a low value suggests substantial distortion and the clusters should be interpreted with caution.

The coefficient is especially useful for comparing different clustering algorithms on the same dataset, allowing the researcher to select the method that best represents the data.

## Cluster Analysis and Ordination: Complementary Techniques

Cluster analysis and ordination are the two principal multivariate families for exploring community composition, best regarded as complementary rather than competing approaches (Gauch 1982). Ordination techniques (PCA, NMDS, DCA) reduce dimensionality and display objects as points in continuous space, preserving gradients and continuous variation. Cluster analysis imposes discrete group boundaries via a one-dimensional dendrogram that cannot fully capture multidimensional gradient structure.

When strong gradients exist, ordination may reveal patterns that clustering obscures — for example, smooth fungal species turnover along an environmental gradient may be forced into discrete clusters that do not reflect the underlying continuity. Conversely, cluster analysis can identify discrete community types (e.g., distinct fungal associations on different host tree species) that ordination may not clearly delineate.

The most robust community analyses typically employ both approaches; consistent results strengthen confidence, while discrepancies themselves provide valuable ecological insight.

## Practical Recommendations

Based on the considerations outlined above, the following practical recommendations can guide the application of cluster analysis to [[fungal-biodiversity-data-analysis]]. First, always compare the results of multiple resemblance functions before committing to a single clustering solution. Second, use the cophenetic correlation coefficient to assess dendrogram fidelity and to compare alternative clustering methods. Third, complement cluster analysis with ordination to evaluate whether the identified groups are robust or artefacts of the one-dimensional representation. Fourth, document all methodological choices — resemblance function, clustering algorithm, data transformations — to ensure reproducibility and to allow readers to evaluate the appropriateness of the analytical decisions.

## Cautions and Limitations

Several important cautions should guide the application of cluster analysis to fungal biodiversity data (van Tongeren 1995):

1. **Data quality**: Cluster analysis is sensitive to sampling effort, species identification errors, and treatment of rare species. Noise can produce spurious clusters or obscure genuine ones. Standardised [[lichen-biodiversity-sampling-protocols-data-analysis]] and careful taxonomic work are prerequisites.
2. **Choice of method**: Different algorithms can yield different dendrograms from the same data. No single "correct" method exists; the choice should be guided by data structure and research objectives. Comparing multiple methods is good practice.
3. **Choice of resemblance function**: The distance coefficient used can dramatically alter results. It must be matched to the data type and ecological question.
4. **Information loss**: The one-dimensional dendrogram loses multidimensional community variation. Apparent cluster discreteness should not be over-interpreted.
5. **Arbitrariness of boundaries**: Deciding how many clusters to recognise (where to "cut" the dendrogram) involves subjectivity. Objective criteria (Mantel statistic, silhouette width) can assist but biological judgement remains essential.
6. **Limited statistical testing**: Cluster analysis does not yield p-values or confidence intervals. Robustness assessment relies on resampling procedures or the cophenetic correlation coefficient.

## References

- Gauch, H.G. (1982). *Multivariate Analysis in Community Ecology*. Cambridge University Press.
- Sokal, R.R. and Rohlf, F.J. (1962). The comparison of dendrograms by objective methods. *Taxon*, 11(2), 33–40.
- Sneath, P.H.A. and Sokal, R.R. (1973). *Numerical Taxonomy: The [[biodynamic-farming-principles-and-practice]] of Numerical Classification*. W.H. Freeman.
- van Tongeren, O. (1995). Cluster analysis. In: Jongman, R.H.G., ter Braak, C.J.F. and van Tongeren, O.F.R. (eds.), *Data Analysis in Community and Landscape Ecology*. Cambridge University Press, pp. 174–212.
