# Fungal Species Recognition and Population Genetics

## Overview
Understanding fungal species delimitation and population structure is essential for
addressing ecological questions about dispersal, gene flow, adaptation, and the spatial
organization of [[biodiversity-of-fungi-soil-fungal-communities-agriculture|soil fungalcommunities]]. These insights have practical implications for plant pathology,
[[fungal-conservation-biology]], and the management of fungal bioresources. The challenge of
recognizing fungal species is complicated by the fact that only approximately 11% of
described fungal species have been cultivated, and roughly 20% of those do not
reproduce sexually in laboratory conditions, precluding straightforward mating tests.

## The Species Concept Problem in Fungi

### Morphological Species Recognition (MSR)
Historically, all fungal species were recognized by morphology. Where morphological
species were broad and the need to distinguish species was great, mycologists employed
additional phenotypes such as substrate utilization patterns and growth rates on
different media at various temperatures. However, multiple genetically isolated species
frequently share identical morphologies (cryptic species), while single genetic species
may display remarkable phenotypic plasticity across [[fungal-adaptations-environmental-gradients]]. The
morphological approach therefore severely underestimates true fungal diversity.

### Biological Species Recognition (BSR)
The biological species concept defines species as groups of interbreeding individuals
reproductively isolated from other such groups. This approach has been applied
productively to fungi that can be mated in laboratory conditions, particularly among
Agaricales. However, BSR is not broadly applicable given the prevalence of asexual
reproduction and the difficulty of cultivating many fungi. Additionally, many
genetically and geographically distinct species are not reproductively isolated,
meaning BSR and genetic approaches can yield conflicting results.

### Phylogenetic Species Recognition (PSR)
Phylogenetic species recognition has emerged as the most widely applicable solution.
PSR uses the concordance of gene genealogies across multiple loci to identify
genetically isolated lineages. The approach relies on a fundamental transition: within
a species, recombination maintains concordance among gene trees, while between species,
lineage-specific loss of ancestral variation following genetic isolation produces
congruent phylogenetic patterns across independent loci. PSR has had a dramatic impact
on fungal taxonomy, particularly for medically and agriculturally important species.

## Multilocus Sequence Typing (MLST)

MLST characterizes fungal isolates by sequencing fragments of multiple housekeeping
genes, typically five to seven loci. Each unique allelic profile at these loci defines
a sequence type (ST) that can be compared across studies and laboratories. A critical
advantage of MLST over fingerprinting approaches like RAPD is that DNA sequences are
"portable" — sequences determined in different laboratories can be combined into unified
databases, avoiding the ascertainment bias that plagues approaches where polymorphic
loci discovered for one population may prove fixed and uninformative in another.

Web-based MLST schemes have been established for several socially important fungi,
including Coccidioides species. The first application of genealogical concordance in
mycology was with [[coccidioides-immitis]], where comparison of five genes sequenced from
17 individuals revealed two phylogenetic species within what had been considered a
single morphological species. It seems likely that each medically important fungus will
eventually have its own MLST scheme, enabling truly global studies of fungal species
diversity.

## Multilocus Microsatellite Typing (MLMT)

MLMT exploits the high variability of microsatellite loci — short tandem repeat
sequences that mutate rapidly through replication slippage — for high-resolution
fungal genotyping. Microsatellites are portable like DNA sequences and can be used to
discover population structure through either phylogenetic analysis or Bayesian
assignment methods.

MLMT provides finer-scale discrimination than MLST, making it ideal for studying
recent transmission events, local population structure, and epidemiological outbreaks.
In Coccidioides, nine microsatellite loci applied to nearly 170 individuals confirmed
the two species proposed by MLST and further revealed at least two populations within
Coccidioides immitis and three within Coccidioides posadasii.

### The Homoplasy Problem
An important finding from comparative studies is that single microsatellites can be
misleading owing to hypervariability and attendant homoplasy — identical allele sizes
may arise independently through convergent mutations rather than shared ancestry. This
conclusion was reached independently in studies of both Coccidioides and Neurospora.
The practical implication is that many microsatellite loci should be used
simultaneously; for example, Fisher and colleagues used 20 microsatellites in their
study of [[gadd-penicillium-marneffei-population-genetics]] to accomplish species recognition and population
characterization in a single analysis.

## Histoplasma: A Case Study in Cryptic Diversity

The fungus [[histoplasma-capsulatum]] provides a compelling illustration of how
phylogenetic methods reveal hidden diversity. This species was known to be
phenotypically complex and was divided into three varieties based on host, geographic
range, and disease symptoms. When sequences from four loci were obtained from more
than 130 individuals assigned to the three varieties, they formed at least seven
genetically isolated clades showing strong correlation with geography but not with host
or symptoms: North America 1 and 2, Latin America A (including a Eurasian subclade)
and Latin America B, Africa, Australia, and Indonesia. The morphological varieties
proved to be neither monophyletic nor phylogenetically meaningful.

## Species Divergence and Geologic Time

Molecular clock analyses have revealed that morphological species typically harbour
two or more cryptic species with divergences on the order of 3–10 million years ago,
while the nearest morphologically distinct species have diverged approximately 30–100
million years ago. This disparity suggests that it is far easier to form a new species
than to maintain one — most genetically isolated clades do not persist long enough to
accumulate morphological differences.

In Coccidioides, the two recognized species diverged between 10 and 12 million years
ago. For Histoplasma, the radiation of seven clades was estimated at 3.2 to 13 million
years ago, with tropical clades showing much greater genotypic diversity than
temperate ones — likely because temperate populations endured genetic bottlenecks
during ice age glaciation cycles while tropical populations escaped these
contractions.

## Reproductive Mode and Geographic Range

Reproductive mode profoundly influences population structure and biogeography. A
strictly clonal species would need periodic global sweeps of a single genotype to
avoid fragmentation into endemic clades, while a recombining species requires
long-distance dispersal of individuals capable of mating. Many socially important
fungi that are morphologically mitosporic, including [[aspergillus-fumigatus]], show
genetic evidence of recombination in their population structures.

A. fumigatus presents a striking contrast to most other studied fungi: it maintains
a truly global geographic range with no hint of endemism, unlike the geographically
structured species seen in Coccidioides, Histoplasma, and Fusarium. The presence of
both mating types in equal proportion at single locations, combined with high local
genotypic diversity, suggests that almost any individual of A. fumigatus is capable
of very long-distance dispersal.

## Sources
- Taylor, J.W., Turner, E., Pringle, A., Dettman, J. & Johannesson, H. (2006).
  "Fungal species: thoughts on their recognition, maintenance and selection." In Gadd,
  G.M., Watkinson, S.C. & Dyer, P.S. (Eds.), *Fungi in the Environment*, pp. 313–339.
  Cambridge University Press.
- Koufopanou, V. et al. (1997). "Evidence for parasexual recombination in
  Coccidioides immitis." *PNAS* 94: 5478–5482.
- Kasuga, T. et al. (2003). "Extensive polymorphism in Coccidioides." *Fungal Genet.
  Biol.* 39: 224–235.

## See Also

- [[gadd-fungal-species-recognition]]
- [[gadd-fungal-mlst-population-genetics]]
- [[fungal-genetics]]
