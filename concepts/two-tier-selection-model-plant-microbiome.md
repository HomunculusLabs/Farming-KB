# Two-Tier Selection Model of Plant Microbiomes

## Overview

The two-tier selection model is a conceptual framework describing how microbial
communities are assembled in and around plant roots. It proposes that microbiome
composition is determined in two sequential stages: first by soil edaphic
factors, and second by host plant genotype. This model has been validated across
multiple plant systems and provides a predictive framework for understanding
rhizosphere and endorhiza microbiome structure in agricultural and ecological
contexts.

## The Two Tiers

### Tier 1: Soil-Determined Community

The first tier of selection is driven by edaphic (soil-related) factors. Soil
type, pH, salinity, organic carbon content, nitrogen availability, water
content, and physical composition (sand, silt, clay ratios) collectively
determine the baseline microbial community available in a given environment.
This is the "source pool" from which all plant-associated communities are drawn.

Soil pH is often the single strongest predictor of microbial community structure
across sample types. Soils with similar physicochemical properties tend to
harbor similar microbial communities regardless of the plant species growing in
them. This tier explains why bulk soil and rhizosphere communities from the
same location tend to cluster together in beta-diversity analyses, even when
different plant species are compared side by side.

The soil-derived microbiota serves as the recruitment pool for root-colonizing
bacteria. The transition from bulk soil to rhizosphere represents the first
major community shift, driven by the nutrient-rich environment created by root
exudates. Carbon compounds, amino acids, and organic acids secreted by roots
create a "rhizosphere effect" that enriches certain bacterial taxa relative to
bulk soil. This enrichment is relatively non-selective with respect to plant
genotype — any plant growing in that soil will produce a broadly similar
rhizosphere community because the source pool is the same.

### Tier 2: Host Genotype-Determined Community

The second tier of selection occurs when bacteria migrate from the rhizosphere
into plant tissues, specifically the endorhiza (root interior). At this stage,
host plant genotype becomes the dominant factor shaping community composition.
Different cultivars of the same species can maintain significantly different
endorhiza communities, even when grown in identical soil.

This genotype-dependent selection is mediated by several plant factors:

- **Root exudate profiles**: Different cultivars secrete different combinations
  of sugars, organic acids, and secondary metabolites, which selectively enrich
  or inhibit specific bacterial taxa.
- **Root cell wall composition**: Structural differences in cell wall
  polysaccharides influence which bacteria can attach and colonize internal
  root tissues.
- **Immune responses**: Plant innate immunity differentially tolerates or
  excludes bacterial taxa based on molecular pattern recognition receptors.
- **Secondary metabolites**: Compounds like terpenes, flavonoids, and
  alkaloids can have antimicrobial properties that filter the endorhiza
  community in a genotype-specific manner.

## Predictions of the Model

The two-tier model makes several testable predictions about microbial community
structure that have been examined across diverse plant systems:

1. **Bulk soil communities cluster primarily by soil type**, with minimal
   influence from plant species or cultivar identity. ADONIS and ANOSIM tests
   on bulk soil samples should show strong soil-type effects but weak or
   non-significant cultivar effects.
2. **Rhizosphere communities represent an intermediate state**, showing
   influence from both soil type and plant species, but are more strongly
   driven by edaphic factors. Statistical tests often show rhizosphere
   communities failing to separate significantly by cultivar.
3. **Endorhiza communities cluster primarily by host genotype**, with soil
   type playing a secondary role. This is the key prediction that distinguishes
   the two-tier model from simpler alternatives.
4. **Phylum-level abundance shifts** should be observable along the
   soil-rhizosphere-endorhiza gradient, with Acidobacteria typically declining
   sharply in the endosphere while Proteobacteria increase.
5. **Community diversity** typically decreases from bulk soil to rhizosphere to
   endorhiza, as each selection step filters the available taxa.

## Evidence from Cannabis Microbiome Studies

Research on the Cannabis microbiome has provided strong support for the
two-tier selection model. In studies examining five distinct Cannabis cultivars
— Sour Diesel, Bookoo Kush, Burmese, White Widow, and Maui Wowie — grown
across multiple California locations:

- **Endorhiza communities showed significant cultivar-specificity** using both
  weighted and unweighted UniFrac metrics. Beta-diversity analyses confirmed
  that different strains maintained distinct microbial communities within their
  root tissues, with ADONIS R² values of 0.59 (weighted) and 0.39 (unweighted)
  for strain-level separation.
- **Rhizosphere communities did not show significant strain-level differences**
  (p = 0.07-0.10), clustering instead by soil type, consistent with Tier 1
  dominance.
- **Bulk soil communities were strongly differentiated by edaphic properties**,
  particularly pH (ranging from 6.63 to 6.94) and organic carbon content
  (ranging from 3.02% to 20.0%).
- A core endorhiza community was identified across all cultivars, including
  Pseudomonas, Cellvibrio, Oxalobacteraceae, Xanthomonadaceae,
  Actinomycetales, and Sphingobacteriales — all well-known endophytic bacteria
  primarily within the Gammaproteobacteria and Alphaproteobacteria.

Notably, the genus Methylophilus explained a significant portion of
cultivar-level endorhiza differences (FDR p = 0.012), comprising 13% of the
Bookoo Kush endorhiza community while being virtually absent in Sour Diesel and
present at only 0.13% in Burmese. This striking cultivar-specific enrichment
exemplifies the Tier 2 genotype-dependent selection process.

## Sample Types in Microbiome Research

The model operates across three principal sample compartments that form a
gradient from soil to plant interior:

### Bulk Soil

Bulk soil samples are collected at a distance from the plant (typically 10-20
cm from the stem, at depth) and represent the background microbial community
not directly influenced by root activity. Bulk soil communities are the most
diverse and serve as the reference point for understanding how plant roots
modify their surroundings. In the Cannabis studies, bulk soil was collected at
a depth of 20 cm and 10 cm from the stem.

### Rhizosphere Soil

Rhizosphere soil consists of particles that remain adhered to roots after
gentle shaking. This narrow zone of soil directly influenced by root exudates
is home to communities enriched for fast-growing copiotrophic bacteria that can
capitalize on the carbon resources secreted by roots. The rhizosphere effect
increases microbial biomass by 2-10x compared to bulk soil. Rhizosphere samples
are obtained by shaking roots into a sterile bag and collecting the dislodged
soil.

### Endorhiza (Root Endosphere)

The endorhiza comprises the internal root tissues colonized by endophytic
bacteria. These bacteria have crossed the root epidermis and established
themselves within the root cortex, vascular tissue, or intercellular spaces.
Endorhiza communities are the least diverse of the three compartments but the
most strongly shaped by host genotype. Before DNA extraction, root samples must
be surface-sterilized to eliminate rhizosphere contamination.

## Broader Applicability Across Plant Systems

The two-tier selection model has been observed in numerous plant systems beyond
Cannabis:

- **Grapevines (Vitis vinifera)**: Soil type determines the available microbial
  pool, while cultivar shapes the endorhiza, contributing to terroir effects
  in wine production. Regional microbial signatures persist even after vines
  are transplanted.
- **Arabidopsis thaliana**: Accession-level genetic differences drive distinct
  root microbiome compositions, with the core root microbiome representing a
  subset of the soil community.
- **Maize (Zea mays)**: Different hybrid lines maintain distinct endorhiza
  communities, and the rhizosphere microbiome is more heritable than previously
  appreciated.
- **Barley (Hordeum vulgare)**: Cultivar effects on root microbiome have been
  documented across multiple soil types, with some bacterial taxa showing
  consistent cultivar associations.

## Methodological Considerations

Studies testing the two-tier model typically employ 16S rRNA gene amplicon
sequencing (particularly the V4 region) analyzed with bioinformatic pipelines
such as QIIME. Key methodological points include:

- **Surface sterilization**: Root samples must be thoroughly sterilized
  (alcohol and sterile water rinses) before DNA extraction to distinguish
  endorhiza from rhizosphere communities.
- **Rarification**: Samples must be rarified to even sequencing depth before
  alpha and beta-diversity analyses to avoid artifacts from unequal sampling.
- **Pseudoreplication**: Taking triplicate samples from different roots on the
  same plant provides technical replication but does not constitute biological
  replication for statistical purposes.
- **Phylogenetic metrics**: Both weighted and unweighted UniFrac distances
  should be examined, as they capture different aspects of community structure
  (abundance-weighted vs. presence-absence).
- **DNA extraction**: Kits such as the PowerSoil DNA Isolation Kit are standard,
  with modifications like a 65°C heating step to improve lysis efficiency.

## Agricultural Implications

Understanding the two-tier selection model has practical implications for crop
management and microbiome engineering:

1. **Soil management directly influences the microbial recruitment pool**.
   Practices that maintain soil health — organic amendments, reduced tillage,
   cover cropping, and appropriate irrigation — expand the diversity of
   beneficial microbes available for root colonization.
2. **Breeding for beneficial microbiome interactions is feasible**, as
   cultivar genotype determines endorhiza community structure. Selecting for
   cultivars that naturally recruit growth-promoting or disease-suppressive
   endophytes could reduce fertilizer and pesticide inputs.
3. **Transplanting microbiomes across environments may be limited** by Tier 1
   soil constraints. Inoculants must be compatible with the local soil
   chemistry and competitive with the resident community to establish
   persistently.
4. **The model predicts that soil-type effects can be partially overcome**
   through aggressive inoculation strategies, but genotype-matched inoculants
   are more likely to establish in the endorhiza.

## Limitations and Open Questions

- The relative strength of each tier varies by plant species, growth stage,
  and environmental conditions. Some studies find stronger soil effects even
  in the endorhiza than the model predicts.
- Fungal communities, including arbuscular mycorrhizal partners, may not
  follow the same two-tier pattern as bacterial communities and require
  separate modeling frameworks.
- Temporal dynamics are not fully captured by the static two-tier model.
  Microbial communities shift throughout the plant lifecycle, and the
  strength of selection at each tier may change with phenological stage.
- The model does not fully account for stochastic colonization events,
  dispersal limitations, or priority effects that can influence community
  assembly independently of soil type or host genotype.
