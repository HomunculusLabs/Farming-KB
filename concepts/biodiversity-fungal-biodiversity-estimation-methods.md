---
title: "Biodiversity Fungal Biodiversity Estimation Methods"
created: 2026-04-28
tags:
  - biodiversity-estimation
  - species-richness
  - statistical-methods
  - extrapolation
  - sampling-theory
date: 2026-04-28
updated: 2026-04-28
sources:
  - "/Users/t3rpz/wiki/raw/papers/unknown-biodiversity-of-fungi.md"
type: concept
---

# Fungal Biodiversity Estimation Methods

[[estimating-fungal-biodiversity-methods]] methods from limited sampling presents significant
challenges because fungi are diverse, patchily distributed, and often
ephemeral in their fruiting. Large numbers of species inhabit small
areas, and studies of fungal-communities-succession without sustained,
long-term sampling effort.

## Complementarity Analysis

Complementarity is an empirical measure of the degree of species
uniqueness between different samples or sites. It is expressed as the
proportion of total species encountered that is unique to one sample or
the other, calculated as Cjk = Ujk/Sjk, where Cjk is the complementarity
between samples j and k, Ujk is the number of taxa found at only one
site, and Sjk is the total richness of both sites combined.

When all species are found at both sites, complementarity equals zero;
when no species are shared, it equals one. Sampling for richness is most
efficient when complementarity among samples is approximately 0.5. High
complementarity (fewer species in common) indicates that many taxa
probably are being overlooked and sampling intensity should be increased.
Low complementarity suggests that some samples are redundant. This
measure has been used effectively to determine efficient sampling
strategies for litter agarics in [[fungal-biodiversity-tropical-ecosystems]].

## Jackknife Estimators

The jackknife is a resampling-based statistical procedure for estimating
total richness from sample data. The first-order jackknife formula is
S* = Sobs + L[(n-1)/n], where S* is estimated total richness, Sobs is
the total number of species observed in all samples, L is the number of
species observed in only one sample (singletons), and n is the number of
samples.

The first-order jackknife considers only the rarest taxa. The
second-order jackknife extends the approach to include species observed
at exactly two sites (doubletons). These estimators are based on the
principle that the greater the proportion of rarely encountered taxa, the
more a diversity estimate should be revised upward. The jackknife is
particularly useful because it provides a relatively straightforward
calculation from standard inventory data.

## Chao's Estimators

Chao's second estimator, known as "Chao 2," is one of the simplest and
most reliable richness estimators when the number of samples is small.
The formula is S* = Sobs + (L2/2M), where the variables are the same as
in the jackknife and M is the number of species observed in exactly two
samples. This algorithm performed particularly well on data with a
preponderance of rare taxa, a situation frequently encountered with
fungi.

A notable limitation of Chao 2 is that when the number of taxa in
exactly two plots is zero, estimated total richness becomes infinite.
This artifact underscores the importance of obtaining adequate sample
sizes before applying extrapolation methods. Despite this limitation,
Chao 2 is widely recommended as a robust starting point for richness
estimation in fungal biodiversity studies.

## Performance of Estimators

Schmit and colleagues examined the utility of the jackknife, Chao 2,
and other estimators applied to macrofungal inventory data. They found
that none of the currently used extrapolation techniques was robust when
applied to their data from a northwest Indiana fungal-biodiversity-inventory-design that measured diversity of both
macrofungi and trees examined 25 studies involving 184 plots across
[[psilocybin-north-america-pacific-northwest]], Europe, China, and Costa Rica. The analysis determined
that although plots contained more macrofungi than trees, the
macrofungi were neither more nor less widely distributed than tree
species. Sampling effort had a major impact on macrofungal diversity
discovered, but habitat type and tree diversity played larger roles in
explaining differences between studies than sampling effort alone.
Differences in [[lichen-biodiversity-sampling-protocols-data-analysis]] also interfered with direct comparisons
