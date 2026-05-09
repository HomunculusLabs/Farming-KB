---
title: Two-Tier Selection Model of Plant Microbiome Assembly
created: 2026-04-28
tags: [microbiome, cannabis, rhizosphere, endorhiza, soil-science, plant-microbe-interactions, cultivar-specificity]
date: 2026-04-28
updated: 2026-04-28
sources:
  - understanding-cultivar-specificity-cannabis-microbiome.md
type: concept
---

# Two-Tier Selection Model of Plant Microbiome Assembly

The two-tier selection model is a conceptual framework describing how microbial communities are assembled in and around plant roots. It proposes that plant-associated microbiomes are structured by two sequential filters: first, soil type determines the pool of available microorganisms in the rhizosphere, and second, host plant genotype selectively filters which of those organisms colonize the internal root tissues (endorhiza). This model was developed through studies of plant-microbiome interactions and has been validated across multiple plant species, including Cannabis.

## The Two Tiers

### Tier 1: Soil Determines the Rhizosphere Pool

The first tier posits that edaphic factors — soil chemistry, texture, pH, salinity, organic carbon content, nitrogen levels, and water content — are the primary determinants of the microbial community composition in the bulk soil and rhizosphere. The rhizosphere is the narrow zone of soil directly influenced by root secretions (rhizodeposits), which include exudates, mucilage, and lysates. These compounds create a nutrient-rich environment that shifts the microbial community away from the bulk soil composition, but the available organisms are drawn from the soil-born pool.

Edaphic factors such as nitrogen, salinity, carbon, and water content have been shown through Mantel tests to be strongly correlated with beta-diversity across all sample types. In studies of Cannabis microbiomes, nitrogen had the strongest effect on community structure (weighted UniFrac r-stat: 0.465, p = 0.001), followed by salinity (r-stat: 0.437), carbon (r-stat: 0.330), water content (r-stat: 0.281), and pH (r-stat: 0.221). For unweighted analyses, the relative importance of edaphic factors remained the same, with nitrogen as the most important (r-stat: 0.630), followed by salinity (r-stat: 0.620), carbon (r-stat: 0.512), water content (r-stat: 0.466), and pH (r-stat: 0.292). These findings are consistent across multiple plant systems and demonstrate that you cannot separate soil health from microbiome health.

The relative importance of soil versus cultivar can be quantified by examining the number of significant OTUs (operational taxonomic units) attributable to each factor. In pooled Cannabis studies, soil type produced 690 significant weighted OTU differences and 657 unweighted differences, compared to only 71 weighted and zero unweighted differences for strain. This dramatic asymmetry underscores that soil is the dominant factor determining which organisms are even available for plant selection.

### Tier 2: Host Genotype Selects the Endorhiza Community

The second tier involves genotype-dependent selection of endorhiza (endophytic root) colonizers. Once microorganisms have been recruited to the rhizosphere, the plant exerts selective pressure on which species actually enter root tissues. This selection is mediated by root architecture, immune responses, and the specific chemical composition of root exudates, which vary between cultivars and species.

In Cannabis, this second tier has been demonstrated clearly. While rhizosphere communities showed minimal strain-level differentiation, endorhiza communities clustered significantly by cultivar (weighted UniFrac ADONIS: R2 = 0.59, p = 0.004). Different Cannabis strains maintained distinct endorhiza microbiomes even when grown in the same soil, proving that host genotype is the dominant factor shaping the internal root microbiome.

The distinction between the tiers becomes clear when examining what type of differences each produces. Soil type affects both OTU presence/absence (unweighted differences) and OTU abundance (weighted differences), meaning soil determines which species are present at all. Cultivar, by contrast, affects only OTU abundance (71 weighted differences, zero unweighted differences), meaning all cultivars draw from essentially the same species pool but select for different population sizes of each species within their roots.

## Predicted Phylum-Level Changes

The two-tier model makes specific predictions about how microbial phyla change in abundance as organisms transition from soil to rhizosphere to endorhiza:

- **Acidobacteria** decrease dramatically in the endorhiza relative to the rhizosphere and bulk soil. These are oligotrophic organisms adapted to low-nutrient conditions, and the nutrient-rich root interior is unfavorable for them. The most significant single OTU abundance difference between sample types was the decrease in Acidobacteria from order iii1-15 in endorhiza samples (Bonferroni-corrected ANOVA: p = 1.12e-7).
- **Proteobacteria** increase in the endorhiza, particularly from the orders Rhizobiales, Pseudomonadales, Burkholderiales, and Sphingomonadales. Many of these are known endophytes capable of forming mutualistic relationships with plants. Of 51 OTUs that increased in abundance within the Cannabis endorhiza relative to the rhizosphere, 17 were predominantly Proteobacteria, including several from the Rhizobiales order.
- **Actinobacteria** also increase in endorhiza samples, consistent with their known roles as endophytic colonizers and producers of bioactive compounds that may help protect the host plant.
- **Bacteroidetes** from the orders Sphingobacteriales and Flavobacteriales also contribute to several significant OTU differences between Cannabis strains in the endorhiza.

## OTU Sharing Between Soils Supports the Model

A key prediction of the two-tier model is that endorhiza communities should share more operational taxonomic units (OTUs) with the soil they are grown in than with a different soil in which the same strain is grown. This was tested using White Widow plants grown in two distinct soil types: the Mo-Bio soil (MB) and an Orange County soil (OC), which differed significantly in clay content, nitrogen, carbon, salinity, and water content.

Endorhiza samples shared significantly more OTUs with their native soil (n = 45, mean = 2934) than with the alternate soil (n = 45, mean = 2162), with a t-statistic of -10.05 and p = 1.209e-15. This result confirms that soil provides the microbial source pool from which the plant selects its endophytes, consistent with the first tier of the model. The magnitude of the difference — over 770 additional shared OTUs with the native soil — underscores the importance of local soil ecology in determining endorhiza composition.

## Cultivar-Specific Endorhiza Signatures

Different Cannabis cultivars develop distinctive endorhiza signatures even when grown in identical soil:

- **Methylophilus** explained a significant portion of the inter-strain difference (FDR: p = 0.012), comprising 13% of the endorhiza community in Bookoo Kush but only 0.13% in Burmese and was completely absent in Sour Diesel. Methylophilus species are methylotrophic bacteria that utilize one-carbon compounds, suggesting possible metabolic interactions with root exudates.
- **Sphingomonas wittichii** was prevalent in Maui Wowie but not in White Widow. In some contexts this organism can metabolize phenazine-1-carboxylic acid, suggesting a possible role in plant defense through degradation of toxic compounds.
- A core community of Pseudomonas, Cellvibrio, Oxalobacteraceae, Xanthomonadaceae, Actinomycetales, and Sphingobacteriales was shared across all cultivars. With the exception of the aerobic cellulolytic Cellvibrio, all prevalent members of this core endorhiza community are well-known endophytic bacteria primarily within the orders Gammaproteobacteria and Alphaproteobacteria, consistent with observations from other plant systems.

## Alpha Diversity Gradient

The transition from bulk soil to endorhiza follows a consistent pattern of decreasing alpha diversity, representing a funneling effect as each tier of selection reduces the community:

- **Bulk soil** shows the highest diversity (Chao1: mean ~4947, SD ~717)
- **Rhizosphere** shows moderate diversity (Chao1: mean ~4525, SD ~542)
- **Endorhiza** shows the lowest diversity (Chao1: mean ~3321, SD ~420)

The reduction from bulk soil to rhizosphere is modest, while the reduction from rhizosphere to endorhiza is dramatic. This pattern is consistent with both tiers of selection operating sequentially: first, rhizodeposition shifts the community composition, and then host immune responses and chemical defenses further filter which organisms successfully colonize root tissues.

Soil type also influenced alpha diversity within the rhizosphere and bulk soil compartments. The Mo-Bio soil supported higher diversity in bulk soil (Chao1: 5597) and rhizosphere (4859) compared to the Orange County soil (4296 and 3911 respectively), but endorhiza diversity was not significantly different between soils (3325 vs. OC endophytes), suggesting that cultivar selection converges on a similar level of endorhiza complexity regardless of initial soil diversity.

## Beta Diversity Relationships

Beta distances between sample types reveal the hierarchical structure of the microbiome. Rhizosphere and bulk soil communities were significantly more similar to each other than either was to endorhiza communities. Distances between rhizosphere and bulk soil were significantly lower than distances between rhizosphere and endorhiza for both unweighted (t = 24.59, p < 0.001) and weighted analyses (t = 211.82, p < 0.001). However, the distance from rhizosphere to endorhiza was not significantly different from the distance from bulk soil to endorhiza (unweighted: t = -2.10, p = 0.109; weighted: t = -2.23, p = 0.078), indicating that the transition from either soil compartment to the endorhiza represents a similarly large community shift.

## Cannabinoid Correlations

Cannabinoid concentration and composition showed significant correlation with endorhiza community structure (unweighted Mantel r-stat: 0.863, p = 0.001). However, higher THC composition in plants from one soil type was confounded with edaphic variables, making it difficult to disassociate microbiome-cannabinoid associations from soil physicochemical effects. This confounding represents an important methodological consideration for future studies aiming to understand how root microbiomes might influence secondary metabolite production.

## Experimental Design Considerations

The two-tier model was tested using two separate experiments with complementary designs. The first experiment used three Cannabis strains (Burmese, Bookoo Kush, and Sour Diesel) grown in similar soils with minimal edaphic variation, producing 27 samples. The second experiment used two strains (White Widow and Maui Wowie) grown in two distinct soil types with significant differences in clay content, nitrogen, carbon, salinity, and water content, producing 42 samples. All sampling used Illumina 16S rRNA sequencing of the V4 region, analyzed through QIIME 1.7.0 with both open and closed reference OTU-picking against the Greengenes database.

Triplicate samples were taken from each plant for both rhizosphere and endorhiza compartments. In the second experiment, triplicates were taken from different roots on the same plant (pseudoreplicates), allowing assessment of within-plant microbial variation. Samples were taken two weeks prior to harvest to capture mature root-microbiome associations. DNA was isolated using the PowerSoil DNA Isolation Kit with a 65 degree C heating modification.

## Limitations and Open Questions

While well-supported by empirical data, the two-tier model has several limitations:

- **Edaphic confounding**: The relative importance of soil type versus cultivar can vary depending on the degree of edaphic difference between growing locations. In the Cannabis studies, the first experiment with minimal soil variation showed weaker strain effects than the second experiment with significant soil differences.
- **Temporal dynamics**: The model is largely based on point-in-time sampling (two weeks before harvest) and does not fully account for how microbiome communities change across the growing season or across plant developmental stages.
- **Cannabinoid confounding**: The relationship between cannabinoid profiles and endorhiza community structure is difficult to disentangle from soil physicochemical variables, as THC concentration was confounded with soil type.
- **Fungal partners**: The model focuses on bacterial communities and does not fully account for the role of fungal partners such as mycorrhizae in mediating bacterial recruitment or in directly contributing to plant health.
- **Mechanistic detail**: The model describes what happens (soil then genotype filtering) but does not fully specify the molecular mechanisms by which host genotype selects particular endophytes. Root exudate chemistry, immune receptor diversity, and root architecture likely all play roles, but their relative contributions remain to be quantified.
- **Functional significance**: The model describes community composition without fully addressing the functional consequences of different endorhiza communities for plant fitness, yield, or secondary metabolite production.

## Relevance to Other Plant Systems

While validated most thoroughly in Cannabis, the two-tier selection model has been supported by studies in other plant species. The decrease in Acidobacteria and increase in Proteobacteria from soil to endorhiza has been observed across numerous plant families including Poaceae (grasses), Fabaceae (legumes), and Solanaceae (nightshades). The core endorhiza community shared across all Cannabis cultivars — dominated by Pseudomonas, Oxalobacteraceae, and Xanthomonadaceae — overlaps substantially with endophyte communities reported in other crops, particularly the Gammaproteobacteria and Alphaproteobacteria dominance pattern.

The model provides a useful framework for understanding how breeding programs implicitly shape plant-microbiome associations and how soil management practices cascade through to influence internal plant microbial communities. It also suggests that transplanting a cultivar to a new soil environment will fundamentally alter its endorhiza microbiome, with potential consequences for plant health, nutrient uptake, and secondary metabolite production that may not be immediately visible.

The distinction between OTU presence/absence (driven by soil) versus OTU abundance (driven by cultivar) has practical implications. Soil management determines which microbial species are available to interact with the plant at all, while cultivar genetics determines the relative population sizes of those species within root tissues. This means that even the best cultivar selection cannot compensate for a depleted soil microbiome.

## Implications for Agriculture

The two-tier model has practical implications for crop cultivation:

1. **Soil management is foundational**: Because soil determines the available microbial pool, building healthy, diverse soils is prerequisite to developing beneficial plant-microbiome partnerships. Soil management practices directly influence which endophytes a plant can recruit.
2. **Cultivar selection matters**: Different cultivars will recruit different endorhiza communities from the same soil, meaning that breeding programs implicitly select for microbiome associations alongside other agronomic traits.
3. **Inoculant design**: Effective microbial inoculants must be compatible with both the target soil environment and the specific host cultivar's selection criteria. A one-size-fits-all approach to bioinoculants is unlikely to succeed.
5. **Terroir effects**: Both endophytes and epiphytes may contribute to localized terroir for crop plants, as has been demonstrated for wine grapes. The interaction between soil-derived microorganisms and cultivar-specific selection creates unique microbial signatures for each growing location and variety combination. This terroir effect has been documented for wines through microbial source tracking studies showing that regional microbial communities contribute to the sensory characteristics of the final product.

## Future Research Directions

The two-tier model suggests several productive avenues for future investigation. Manipulating soil microbial communities through composting, cover cropping, or targeted inoculation could allow farmers to influence the pool from which cultivars select their endorhiza partners. Understanding the specific root exudate compounds that mediate cultivar-specific selection could enable breeding programs to explicitly select for desirable microbiome associations. Longitudinal studies tracking microbiome development across the full growing season would clarify temporal dynamics that the current point-in-time sampling approach cannot capture.

## See Also

- [[cannabis-endorhiza-microbiome]] for details on endophytic root colonization
- [[cannabis-microbiome-research]] for the broader context of Cannabis-microbe studies
- [[serpentine-soil-ecology]] for the ecology of oligotrophic soil bacteria that decline in endorhiza
- [[pseudomonas-tolaasii-entity-the-mushroom-cultivator]] for the role of Pseudomonas species as core endorhiza colonizers
