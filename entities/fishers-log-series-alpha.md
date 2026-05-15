---
title: Fisher's Log-Series Alpha
source: unknown-biodiversity-of-fungi.md
type: entity
---

## Description

Fisher's log-series alpha is a diversity index derived from the logarithmic series model first described by Fisher, Corbet, and Williams in 1943. It was the first mathematical model to describe the relationship between the number of species and the number of individuals. The parameter alpha from this distribution serves as a measure of diversity widely used in ecological studies including assessments of [[fungal-biodiversity]].

## Classification

- **Category**: Diversity index
- **Mathematical basis**: Logarithmic series distribution
- **Historical origin**: Fisher et al. (1943)
- **Data requirement**: Number of species (S) and total number of individuals (N)
- **Related models**: Geometric series, lognormal distribution, broken-stick model

## Historical Context (Fisher, Corbet & Williams 1943)

Ronald A. Fisher, along with entomologist A.S. Corbet and botanist C.B. Williams, introduced the logarithmic series model in their landmark 1943 paper published in the *Journal of Animal Ecology*. The work originated from the study of Malayan butterfly collections and moth trap data, where Fisher observed that the number of species represented by different numbers of individuals followed a predictable mathematical pattern. Fisher, already renowned for his contributions to statistics and population genetics, applied the log-series distribution — originally developed for other statistical purposes — to describe species-abundance relationships. Williams subsequently applied the model extensively to a wide range of taxa, demonstrating its broad applicability. The parameter alpha (α) emerged from this work as a single-number summary of diversity that could be compared across communities differing in sample size and total abundance, a breakthrough at a time when ecologists lacked standardized diversity metrics.

## Mathematical Derivation

The log-series distribution predicts that the number of species represented by exactly *n* individuals is:

$$a_n = \frac{\alpha \, x^n}{n}$$

where:
- $\alpha$ is Fisher's alpha (the diversity parameter)
- $x$ is a constant between 0 and 1, related to sample size
- $n = 1, 2, 3, \ldots$ is the number of individuals per species

The total number of species *S* and total number of individuals *N* are related to the parameters by:

$$S = -\alpha \ln(1 - x)$$

$$N = \frac{\alpha \, x}{1 - x}$$

Combining these to eliminate *x* yields the fundamental relationship:

$$S = \alpha \ln\!\left(1 + \frac{N}{\alpha}\right)$$

This equation is solved iteratively for $\alpha$ given observed values of *S* and *N*, as no closed-form solution exists. The parameter $\alpha$ represents the theoretical number of species in a community of infinite size and thus serves as a sample-size-independent measure of diversity.

## Relationship to the Log-Series Model

Fisher's alpha is not an independent metric but is intrinsically tied to the log-series species-abundance model. The log-series predicts that the species-abundance distribution follows a specific shape: a large number of rare species (singletons) and a long tail of increasingly uncommon abundant species. When a community's species-abundance distribution conforms to the log-series, alpha is the natural diversity summary parameter. If the community does not follow a log-series pattern — for instance, if it follows a lognormal distribution — the biological interpretation of alpha becomes less straightforward, though it remains a useful comparative index. The log-series model arises theoretically when a few dominant factors control community structure and propagules arrive at random, producing communities where most species are represented by very few individuals.

## Properties and Assumptions

**Properties:**
- Alpha is dimensionless and depends only on *S* and *N*, not on the full abundance distribution
- It is relatively insensitive to sample size, making it robust for comparisons across studies
- Less influenced by the abundances of dominant species than shannon index or simpson index
- Increases monotonically with species richness at constant sample size

**Assumptions:**
- The underlying community follows a log-series species-abundance distribution
- Species arrive and establish independently (no strong biological interactions structuring abundance)
- The community is sampled sufficiently to capture the rare-species tail
- Alpha does not capture evenness — communities with identical *S* and *N* but very different evenness patterns receive the same alpha value
- Best suited for nonequilibrial or early-successional communities where a few factors dominate

## Applications in Ecological Studies

Fisher's log-series alpha has been widely applied across ecological subdisciplines:

- **Entomology**: Originally developed from butterfly and moth data, it remains common in insect community assessments
- **Mycology**: Zak (1988, 1992) found that geometric and log-series models described rhizoplane fungal assemblages well; fungal communities often show nonequilibrial characteristics that align with the log-series model
- **Microbial ecology**: Used to compare soil microbial and fungal diversity across land-use types and treatments
- **Plant ecology**: Applied to herbaceous understory communities and tropical forest plots
- **Marine ecology**: Used in benthic invertebrate and plankton community surveys
- **Conservation biology**: Serves as a standardized metric for comparing biodiversity across fragmented habitats with unequal sampling effort

For cultivators and mycologists, whether a fungal community follows a log-series or lognormal distribution provides diagnostic insight: log-series patterns may indicate early successional or stressed communities, while lognormal patterns suggest established, diverse, and stable communities.

## Comparison with Other Diversity Indices

| Index | Sensitivity to Sample Size | Sensitivity to Dominants | Captures Evenness | Primary Use |
|---|---|---|---|---|
| **Fisher's alpha** | Low | Low | No | Nonequilibrial communities |
| shannon index | Moderate | Moderate | Yes | General diversity |
| simpson index | Low | High | Partial | Dominance-weighted comparisons |
| [[species-richness-diversity-indices-fungi]] | High | None | No | Simple species counts |
| [[fungal-species-accumulation-rarefaction-estimators]] curves | Explicitly controlled | — | — | Sample-standardized comparisons |

Fisher's alpha is generally preferred over raw species richness when comparing communities with very different sample sizes. However, its inability to reflect evenness means that two communities with the same *S* and *N* but radically different abundance distributions will receive identical alpha values, which may be a critical limitation in studies where evenness is ecologically meaningful. Taylor (1978) strongly supported log-series alpha for its discriminant ability and insensitivity to sample size, and Rosenzweig (1995) recommended it as the preferred diversity index for many purposes.

## Estimation Methods

1. **Iterative numerical solution**: The standard method solves $S = \alpha \ln(1 + N/\alpha)$ iteratively using Newton-Raphson or bisection. Starting with an initial guess (e.g., $\alpha_0 = S$), the algorithm refines the estimate until convergence.

2. **Maximum likelihood estimation (MLE)**: Provides estimates of both $\alpha$ and $x$ simultaneously by maximizing the log-likelihood of the observed frequency counts under the log-series model. MLE yields confidence intervals via the Fisher information matrix.

3. **Approximation for large samples**: When *N* is very large relative to *S*, $\alpha \approx S / \ln(N)$ provides a rough but fast approximation.

4. **Software implementations**: Available in R packages such as `vegan` (function `fisher.alpha()`), `biodiversityR`, and Python libraries including `scikit-bio` and `pycogent`. Most implementations handle the iterative solving internally and return $\alpha$ with optional confidence intervals.

## Key Facts

- Fisher's logarithmic series was the first model to mathematically describe species-individual relationships
- Taylor (1978) strongly supported log-series alpha due to good discriminant ability and insensitivity to sample size
- Less affected by abundances of common species than Shannon or Simpson indices
- Less sensitive to sample size than many alternative indices
- Major disadvantage: unaffected by evenness of species distribution
- Assumes species adhere to a log-series distribution
- Rosenzweig (1995) recommended it as the preferred diversity index
- The log-series model arises when few factors control species dominance and propagules arrive randomly
- Characteristic of nonequilibrial assemblages and small species sets

## Relevance to Cultivation and Mycology

Fisher's log-series alpha is particularly relevant for assessing fungal diversity because fungal communities often display nonequilibrial characteristics. Zak (1988, 1992) found geometric and log-series models described rhizoplane fungal assemblages. For cultivators, whether communities follow log-series or lognormal distributions provides insight into community stability. Log-series patterns may indicate early successional or stressed communities, while lognormal patterns suggest established, diverse communities. The index's insensitivity to sample size makes it practical for comparing studies with different sampling intensities.

## See Also

- [[species-abundance-distribution]]
- [[whittaker-beta-diversity]]
- [[bray-curtis-dissimilarity]]
- [[alpha-beta-gamma-diversity-fungi]]
- [[species-richness-diversity-indices-fungi]]
- [[fungal-diversity-indices-community-analysis]]
- [[fungal-molecular-community-analysis]]
