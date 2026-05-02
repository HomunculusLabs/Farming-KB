---
title: Fungal Species Estimation — Methods for Assessing Total Diversity
created: 2026-04-21
updated: 2026-04-21
type: concept
tags: [mycology, fungi]
sources: []
---

# Fungal Species Estimation — Methods for Assessing Total Diversity

Estimating how many fungal species exist — globally, regionally, or locally — is one of the most challenging problems in mycology. Fungi are vastly under-described, with current estimates ranging from 500,000 to nearly 10 million species. This page reviews the methods and assumptions underlying species estimation.

## The Scale of the Problem

### Known vs. Estimated
- Approximately **150,000 described species** of fungi
- Hawksworth (1991): ~1.5 million species total (10:1 ratio of estimated to described)
- Various subsequent estimates: 500,000 to 9.9 million
- Only about **5% of fungal species are described** (vs. 60-80% of lichens)
- New species continue to be described at ~1,000-1,500 per year

### Why Fungi Are Undercounted
- Most are microscopic and inconspicuous
- Many do not produce visible fruiting structures
- Fruiting is often ephemeral and seasonal
- Tropical regions are severely undercollected
- Many species are known only from a single collection
- Cryptic species (morphologically identical but genetically distinct) are common
- Host specificity patterns are poorly understood

## Methods of Estimation

### Ratio-Based Methods (Hawksworth 1991)

The classic 1.5 million estimate was based on:
1. Ratio of fungal to plant species in well-studied regions (e.g., UK: ~6:1 fungi:plants)
2. Apply ratio to global vascular plant diversity (~270,000 species)
3. Result: ~1.5 million fungal species

**Assumptions:**
- Fungal:host ratios are consistent across regions and habitats
- Ratios from temperate regions apply to tropics
- All plant-associated niches are filled proportionally

**Limitations:**
- Ratios vary dramatically by region and habitat type
- Tropical fungal:plant ratios likely much higher
- Non-plant-associated fungi (soil, aquatic, animal-associated) not well captured

### Extrapolation from Well-Studied Sites

Using intensive local inventories:
- Tropical tree plots: 20% of collected fungal species were new to science
- Single 40-hectare neotropical tract yielded many undescribed species
- One-third of plant species had their own rust species

### Species Accumulation Curves

- Plot cumulative species count against sampling effort (area, time, specimens)
- Extrapolate to asymptote for estimated total
- Rarely reaches asymptote for fungi — undersampling is the rule
- 21-year macrofungal study: estimators still had not stabilized

### Nonparametric Estimators

#### Jackknife Estimators
- First-order jackknife: S + (n-1)/n * m1
- Second-order jackknife: S + (2n-3)/n * m1 - (n-2)^2/n(n-1) * m2
- Where S = observed species, n = number of samples, m1 = species in 1 sample, m2 = species in exactly 2 samples

#### Bootstrap Estimator
- S + sigma(1 - pi^n)
- Where pi = proportion of sample i occupied by species i

#### Chao Estimator (Most Widely Used)
- Chao1: S + F1^2 / (2 * F2)
- Where F1 = number of singletons (species found once), F2 = number of doubletons
- Provides lower-bound estimate of true richness
- Modified versions account for unseen species

### Incidence-Based Coverage Estimator (ICE) and Chao2
- Use species incidence (presence/absence in samples) rather than abundance
- ICE accounts for variable sampling intensity
- Chao2: S + Q1^2 / (2 * Q2) where Q1 = species in 1 sample, Q2 = species in 2 samples

## Power Analysis

Used to determine if sampling is sufficient to detect differences between sites:
- Requires specification of effect size, alpha level, and desired power
- Determines minimum sample size needed
- Critical for comparative studies
- Often reveals that fungal studies are underpowered

## Challenges Specific to Fungi

### Fruiting Phenology
- Species may fruit only 1 year out of 4 or more
- Some species are reliably detected only during specific seasons
- Weather-dependent fruiting creates temporal gaps

### Detection Probability
- Cryptic species may be present but not detected
- Sequestrate fungi require raking to detect
- Microfungi require microscopy
- Molecular methods reveal many species invisible to traditional surveys

### Patchy Distributions
- High spatial autocorrelation
- Clumped sporocarp distributions
- Adjacent plots more similar than distant ones

### Incomplete Taxonomic Knowledge
- Many specimens identifiable only to genus
- Expertise bottleneck: few taxonomists for most groups
- Tropical regions especially understaffed

## Molecular Approaches

### Metabarcoding Revelations
- Soil DNA reveals far more species than cultivation or fruiting surveys
- Ectomycorrhizal root analysis shows many species that rarely or never fruit
- 192 morphological types from 0.45 m^2 of soil cores vs. 43 sequestrate + ~100 mushroom species from 27,000 m^2 of sporocarp plots

### Limitations
- DNA does not confirm species are alive or active
- Copy number variation complicates quantification
- Reference databases incomplete
- Voucher specimens still essential

## Practical Recommendations

1. **Use multiple estimators** (Chao, Jackknife, ICE) and report range
2. **Combine methods:** Sporocarp surveys + soil cores + molecular analysis
3. **Long-term sampling:** Minimum 5 years, preferably 10+
4. **Pilot studies:** Determine required sampling intensity before committing
5. **Report confidence intervals:** Single point estimates are misleading
6. **Deposit vouchers:** All estimates should be tied to physical specimens
7. **Acknowledge limitations:** All fungal richness estimates are underestimates

## See Also

- [[fungal-diversity-indices-community-analysis]]
- [[beta-glucan-receptor-binding]]
- [[dna-barcoding-fungal-identification]]
- [[macrofungal-sampling-design-plots-transects]]
- [[fungal-species-richness-and-diversity-indices]]
- [[tropical-vs-temperate-fungal-diversity-patterns]]
- [[soil-fungal-diversity-wisconsin-survey-global-patterns]]
