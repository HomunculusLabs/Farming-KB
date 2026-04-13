# Wiki Schema

## Domain
Regenerative homesteading — biodynamic farming, animal husbandry (ducks, goats), cannabis cultivation (indoor living soil beds), soil biology and food web, Korean Natural Farming (KNF), JADAM, fermented plant extracts, homemade fertilizers, vermicompost, bokashi, effective microorganisms (EM), light spectrums for indoor LED grow lights, and utilization of animal byproducts (feathers, hides).

## Conventions
- File names: lowercase, hyphens, no spaces (e.g., `knf-lab-preparations.md`)
- Every wiki page starts with YAML frontmatter (see below)
- Use `[[wikilinks]]` to link between pages (minimum 2 outbound links per page)
- When updating a page, always bump the `updated` date
- Every new page must be added to `index.md` under the correct section
- Every action must be appended to `log.md`
- Raw sources in `raw/` are immutable — corrections go in wiki pages only

## Frontmatter
```yaml
---
title: Page Title
created: YYYY-MM-DD
updated: YYYY-MM-DD
type: entity | concept | comparison | query | summary
tags: [from taxonomy below]
sources: [raw/articles/source-name.md]
---
```

## Tag Taxonomy

### Growing Methods
- `regenerative` — regenerative agriculture principles and practices
- `biodynamic` — biodynamic farming methods, preparations, calendar
- `knf` — Korean Natural Farming techniques and preparations
- `jadam` — JADAM methods and formulations
- `living-soil` — living soil bed approach, no-till, soil biology focus
- `indoor` — indoor growing techniques, environments, equipment

### Cannabis
- `cannabis` — cannabis cultivation broadly
- `lighting` — grow lights, spectrums, photoperiods, PAR/PPFD
- `flowering` — flowering stage specific techniques
- `vegetative` — vegetative stage specific techniques
- `germination` — seed starting, cloning, early growth

### Soil & Biology
- `soil` — soil composition, mineral balancing, testing
- `microbes` — beneficial bacteria, fungi, effective microorganisms (EM)
- `mycorrhizae` — mycorrhizal fungi and fungal networks
- `compost` — composting, vermicompost, bokashi, thermophilic compost
- `fertilizer` — homemade fertilizers, nutrient sources, amendments

### Fermented Preparations
- `fpe` — fermented plant extracts
- `fermentation` — fermentation processes broadly (LAB, IMO, FPJ, etc.)

### Animals & Byproducts
- `ducks` — duck keeping, breeds, forage, health
- `goats` — goat keeping, breeds, dairy, health
- `animal-husbandry` — general animal care topics
- `byproducts` — utilization of feathers, hides, bones, manure, blood

### Plants & Crops
- `plant-systems` — integrated plant systems and polycultures
- `cover-crop` — cover cropping, green manure, companion planting
- `food-forest` — food forest design, perennial polycultures
- `forage` — forage systems for animals, pasture management


### Equipment & Infrastructure
- `greywater` — greywater recycling, treatment, and reuse systems
- `equipment` — grow equipment, tools, infrastructure
- `lighting-hardware` — specific light fixtures (e.g., Think Grow Model H Plus)

### People & Organizations
- `person` — individual people (farmers, researchers, authors, innovators)
- `organization` — organizations, companies, research institutions


### Meta
- `comparison` — side-by-side analyses
- `timeline` — chronological processes, seasonal schedules
- `recipe` — specific formulations, step-by-step preparations
- `troubleshooting` — problem-solving guides, pest/disease management
- `homestead-crafts` — value-added products from homestead outputs (soap, candles, textiles)

Rule: every tag on a page must appear in this taxonomy. If a new tag is needed,
add it here first, then use it.


### Additional Tags
- `permaculture` — Permaculture principles, design, zones, guilds
- `fertility` — Soil fertility, nutrient management, base saturation
- `minerals` — Mineral amendments, rock dusts, trace elements
- `biology` — Soil biology, microbiology, ecology
- `ecology` — Ecological systems, food webs, ecosystems
- `fungi` — Fungal biology, cultivation, identification
- `mushrooms` — Mushroom cultivation, foraging, species
- `cultivation` — Growing methods, crop cultivation broadly
- `gardening` — Home gardening, vegetable growing
- `medicine` — Herbal medicine, natural remedies, health
- `vinegar` — Vinegar production, BRV, acetic acid
- `homesteading` — Homesteading broadly, rural living skills
- `pesticide` — Natural pesticides, organic pest control products
- `theory` — Theoretical frameworks, scientific theory
- `plant-growth` — Plant growth stages, development, physiology


- `microbiome` — Microbiome, microbial communities, gut and soil microbiomes
- `design` — Design principles, systems design
- `ethics` — Ethical frameworks, land ethics, care ethics
- `principles` — Foundational principles, guiding rules
- `npk` — Nitrogen-Phosphorus-Potassium, macronutrients
- `ph` — Soil pH, acidity, alkalinity, liming
- `phosphorus` — Phosphorus, bone meal, rock phosphate
- `calcium` — Calcium amendments, eggshells, gypsum, lime
- `pollution` — Environmental contaminants, bioremediation, water quality
- `water` — Water systems, filtration, irrigation, sourcing
- `health` — Health, wellness, therapeutic applications, medical conditions
- `processing` — Post-harvest processing, extraction, preservation methods
- `psychopharmacology` — Psychoactive compound pharmacology, brain effects, receptor interactions
- `ethnobotany` — Study of people-plant relationships, indigenous plant knowledge, traditional plant use
- `psychology` — Psychology, consciousness studies, therapeutic frameworks
- `therapy` — Therapy, counseling, psychedelic-assisted therapy, healing practices
- `mycology` — Mycology broadly, fungal science, mushroom study
- `ethnomycology` — Cultural use of fungi, mushroom traditions, sacred mushroom practices
- `religion` — Religion, spiritual traditions, sacred practices
- `philology` — Philology, linguistic analysis, ancient texts
- `psychiatry` — Psychiatry, clinical mental health, psychopharmacology practice
- `academia` — Academic research, institutions, scholarship
- `consciousness` — Consciousness studies, altered states, phenomenology
- `philosophy` — Philosophy, philosophical frameworks, worldviews
- `counterculture` — Counterculture movements, underground culture, subcultures
- `lab-technique` — Laboratory techniques, scientific methods, protocols
- `symbiosis` — Symbiotic relationships, mutualism, commensalism
- `culture` — Cultural studies, cultural history, traditions
- `folklore` — Folklore, traditional knowledge, oral traditions
- `methods` — Methods, approaches, techniques broadly
- `patterns` — Natural patterns, pattern language, design patterns
- `plants` — Plants broadly, botany, plant science
- `nutrients` — Nutrients, plant nutrition, dietary nutrition
- `cacti` — Cacti, succulents, desert plants

- `africa` — African geography, African species, African traditions
- `agriculture` — Agriculture broadly, farming systems
- `amazon` — Amazon region, Amazonian ecosystems, Amazonian cultures
- `annual-calendar` — Annual schedules, seasonal planning
- `anthropology` — Anthropology, human societies, cultural studies
- `archaeology` — Archaeology, ancient sites, historical artifacts
- `asia` — Asian geography, Asian species, Asian traditions
- `author` — Authors, writers, content creators
- `beginner` — Beginner-friendly guides, introductory material
- `biochemistry` — Biochemistry, molecular biology, metabolic pathways
- `chemistry` — Chemistry broadly, chemical compounds, reactions
- `climate` — Climate, weather patterns, climate zones
- `composting` — Composting processes, compost systems
- `construction` — Building, construction techniques, infrastructure
- `distribution` — Geographic distribution, species range
- `drying` — Drying techniques, dehydration, preservation
- `ecological-design` — Ecological design, systems thinking
- `engineering` — Engineering, technical systems, mechanical design
- `entheogen` — Entheogenic substances, psychoactive plants/fungi
- `entheogen-research` — Entheogen research, clinical studies
- `europe` — European geography, European species, European traditions
- `fruit-tree` — Fruit trees, orchard fruits, tree fruit cultivation
- `fruiting` — Fruiting stage, mushroom fruiting, crop fruiting
- `grain` — Grains, cereals, grain crops
- `harvesting` — Harvest techniques, harvest timing, post-harvest
- `history` — Historical topics, historical events, historical figures
- `humidity` — Humidity control, moisture management
- `livestock-health` — Livestock health, veterinary care, animal medicine
- `mesoamerica` — Mesoamerican region, Mesoamerican cultures
- `new-world` — New World, Americas broadly
- `no-till` — No-till agriculture, minimal soil disturbance
- `old-world` — Old World, Eurasia/Africa broadly
- `orchard` — Orchards, fruit tree management
- `organic` — Organic farming, organic certification, organic methods
- `pest-control` — Pest control methods, pest management products
- `pest-management` — Integrated pest management, pest strategy
- `pharmacology` — Pharmacology, drug effects, receptor interactions
- `plant-catalog` — Plant catalogs, species listings, plant databases
- `potassium` — Potassium nutrient, K fertilization
- `potency` — Potency, strength, concentration of active compounds
- `preparation` — Preparations, formulations, processing methods
- `preservation` — Food preservation, storage techniques
- `pruning` — Pruning, plant training, canopy management
- `rice` — Rice cultivation, paddy systems, rice varieties
- `safety` — Safety, harm reduction, risk management
- `soil-amendment` — Soil amendments, mineral additions, conditioners
- `south-america` — South American geography, South American species
- `species` — Species identification, species profiles
- `species-profiles` — Detailed species profiles, taxonomic descriptions
- `storage` — Storage methods, shelf life, preservation
- `survey` — Surveys, field surveys, geographic surveys
- `sustainability` — Sustainability, sustainable practices, resilience
- `taxonomy` — Taxonomy, classification systems, nomenclature
- `teacher` — Teachers, educators, knowledge transmitters
- `underground-press` — Underground publishing, counterculture literature
- `vegetables` — Vegetables, vegetable gardening, vegetable crops
- `water-management` — Water management, irrigation, drainage
- `workflow` — Workflows, processes, procedural guides
### Additional Tags (added during lint)
- `earthworks` — Earthworks, land shaping, swales, berms, terraces
- `recipes` — Collections of recipes, formulation compilations
- `season-extension` — Season extension techniques, structures, methods
- `economics` — Economic analysis, cost-benefit, market considerations




### Additional Tags (added during lint 2026-04-12)
- `energy` — Energy systems, renewable energy, off-grid power
- `immunology` — Immunology, immune system, immune responses
- `microscopy` — Microscopy techniques, microscopic observation
- `off-grid` — Off-grid living, self-sufficiency, independent systems
- `windbreak` — Windbreaks, shelterbelts, wind protection

## Page Thresholds
- **Create a page** when an entity/concept appears in 2+ sources OR is central to one source
- **Add to existing page** when a source mentions something already covered
- **DON'T create a page** for passing mentions, minor details, or things outside the domain
- **Split a page** when it exceeds ~200 lines — break into sub-topics with cross-links
- **Archive a page** when its content is fully superseded — move to `_archive/`, remove from index

## Entity Pages
One page per notable entity (animal breed, equipment model, microbe species, plant variety). Include:
- Overview / what it is
- Key facts and characteristics
- Relationships to other entities ([[wikilinks]])
- Source references

## Concept Pages
One page per concept or technique. Include:
- Definition / explanation
- How it works (mechanism)
- When and why to use it
- Related concepts ([[wikilinks]])
- If applicable: recipe, formulation, or step-by-step process

## Comparison Pages
Side-by-side analyses. Include:
- What is being compared and why
- Dimensions of comparison (table format preferred)
- Verdict or synthesis
- Sources

## Update Policy
When new information conflicts with existing content:
1. Check the dates — newer sources generally supersede older ones
2. If genuinely contradictory, note both positions with dates and sources
3. Mark the contradiction in frontmatter: `contradictions: [page-name]`
4. Flag for user review in the lint report

### Growing Methods

- `farming` — general farming practices and systems
- `urban` — urban agriculture, city farming, guerrilla gardening
- `agroforestry` — integrating trees with crops/livestock
- `forestry` — forest management, timber, tree farming

### Soil & Biology

- `remediation` — environmental remediation broadly (soil, water, land)
- `mycoremediation` — fungal-based environmental cleanup and bioremediation
- `mycorestoration` — using fungi for ecological restoration
- `restoration` — ecological restoration of degraded land
- `decomposition` — organic matter breakdown processes
- `nutrient-cycling` — nutrient flow through ecosystems
- `bacteria` — bacterial biology, beneficial and pathogenic bacteria
- `pathogens` — disease-causing organisms (fungal, bacterial, viral)
- `succession` — ecological succession, pioneer species, climax communities
- `carbon-sequestration` — carbon capture and storage in soil/plants

### Plants & Crops
- `plant-systems` — integrated plant systems and polycultures

- `companion-planting` — companion planting strategies and guilds
- `guild` — plant guilds, polyculture groupings
- `cover-crop-termination` — methods for ending cover crop growth
- `trees` — tree care, planting, pruning, orchard management
- `multi-function` — multi-functional plants serving multiple purposes

### Animals & Byproducts

- `livestock` — general livestock management and care
- `insects` — insect biology, beneficial insects, pest insects
- `wildlife` — wildlife habitat, native species, biodiversity on the homestead
- `entomopathogenic` — insect-pathogenic fungi (e.g., Beauveria, Metarhizium)

### Equipment & Infrastructure
- `greywater` — greywater recycling, treatment, and reuse systems

- `filtration` — water/air filtration systems and techniques
- `deployment` — field deployment of fungal/plant treatments
- `swales` — swale design and construction for water management

### People & Organizations

- `shamanism` — shamanic practices, plant teachers, indigenous healing
- `spirituality` — spiritual and ceremonial plant use broadly
- `activism` — environmental activism, drug policy reform
- `community` — community organizing, shared resources, cooperative efforts

### Cannabis

- `pests` — cannabis pest identification and management

### Cultivation Techniques

- `techniques` — general cultivation techniques and methods
- `spawn` — mushroom spawn production, grain spawn, liquid culture
- `inoculation` — inoculation methods for substrates, plants, soil
- `foraging` — wild mushroom and plant foraging

### Environment & Ecology
- `conservation` — conservation of water, soil, biodiversity, and resources

- `environment` — environmental conditions, climate, ecology broadly
- `erosion` — soil erosion, erosion control, land degradation
- `silt` — silt soil type, sediment management

### Food & Nutrition

- `food` — food production, cooking, preservation from homestead

### Science & Research

- `genetics` — genetic principles, breeding, heredity
- `genomics` — genomic analysis, DNA sequencing, genetic mapping
- `neuroscience` — brain science, neurochemistry, psychoactive compounds
- `psychedelics` — psychedelic compounds, effects, research

### Materials & Chemistry

- `NPK` — nitrogen-phosphorus-potassium values and ratios
- `pH` — pH management, soil and water acidity/alkalinity

### Law & Policy

- `law` — legal frameworks, regulations, legislation
- `reform` — drug policy reform, legal reform efforts
- `patents` — patents, intellectual property, licensing
- `intellectual-property` — IP law, patents, trade secrets

### Media & Culture

- `music` — music related to plants, fungi, or homesteading

### Reference & Documentation

- `reference` — reference tables, lookup pages, master lists
- `networks` — networks (mycelial, social, ecological)
- `carbon` — carbon in soil, biomass, climate impact
- `soil-building` — techniques for building and improving soil



### Fungal Ecology & Biodiversity Tags (auto-added 2026-04-12)

Fungal ecology and decomposition:
- `biodiversity` — biodiversity
- `biodiversity-assessment` — biodiversity assessment
- `carbon-cycling` — carbon cycling
- `decomposers` — decomposers
- `forest-ecology` — forest ecology
- `fungal-biodiversity` — fungal biodiversity
- `fungal-diversity` — fungal diversity
- `fungal-ecology` — fungal ecology
- `leaf-litter` — leaf litter
- `microbial-ecology` — microbial ecology
- `saprotrophs` — saprotrophs
- `wood-rot` — wood rot

Marine and aquatic fungi:
- `aquatic-fungi` — aquatic fungi
- `coastal` — coastal
- `estuarine` — estuarine
- `freshwater` — freshwater
- `mangrove` — mangrove
- `marine-fungi` — marine fungi

Taxonomy, biogeography, and field methods:
- `biodiversity-assessment` — biodiversity assessment
- `biogeography` — biogeography
- `classification` — classification
- `endemism` — endemism
- `field-methods` — field methods
- `fungal-distribution` — fungal distribution
- `inventory` — inventory
- `molecular-systematics` — molecular systematics
- `phytogeography` — phytogeography
- `sampling` — sampling
- `speciation` — speciation
- `species-estimates` — species estimates

Specialized fungal groups and interactions:
- `anaerobic-fungi` — anaerobic fungi
- `biocontrol` — biocontrol
- `chytrids` — chytrids
- `dictyostelids` — dictyostelids
- `fungal-interactions` — fungal interactions
- `fungicolous` — fungicolous
- `gut-microbiome` — gut microbiome
- `hyperparasites` — hyperparasites
- `microbial-ecology` — microbial ecology
- `mycetozoans` — mycetozoans
- `mycoparasites` — mycoparasites
- `myxomycetes` — myxomycetes
- `oomycetes` — oomycetes
- `protostelids` — protostelids
- `rumen` — rumen
- `slime-molds` — slime molds
- `soil-fungi` — soil fungi
- `soil-health` — soil health

General:
- `botany` — botany
- `business` — business
- `culture-media` — culture media
- `dung-fungi` — dung fungi
- `herbivore` — herbivore
- `isolation` — isolation
- `laboratory-methods` — laboratory methods
- `nutrition` — nutrition
- `seeds` — seeds
- `soil-food-web` — soil food web
- `substrate` — substrate

- `tools` — tools, equipment, workshop tools

- `education` — education, learning, teaching resources

### Additional Tags (added during lint 2026-04-12 evening)
- `outdoor` — Outdoor growing, outdoor cultivation, field production
- `pollinators` — Pollinators, pollination, bee and insect pollinator support
- `regulation` — Regulation, regulatory compliance, legal requirements
- `ventilation` — Ventilation, air circulation, airflow management for indoor growing

- `cooking` — Cooking techniques, food preparation, culinary methods
- `research` — Scientific research, academic studies, field research
- `resilience` — Resilience, adaptation, community resilience, climate resilience

- `aquaponics` — Aquaponics, integrated fish and plant systems, aquaculture
