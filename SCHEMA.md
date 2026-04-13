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


### Chemistry & Pharmacology
- `chemistry` — chemical compounds, molecular structures, reactions
- `pharmacology` — drug actions, mechanisms, pharmacokinetics
- `psychopharmacology` — psychoactive compound effects on mind and behavior
- `psychedelics` — psychedelic compounds and their effects
- `neuroscience` — brain function, neural systems, cognition
- `phenethylamine` — phenethylamine class compounds
- `amphetamine` — amphetamine derivatives and related compounds
- `serotonin` — serotonin receptors and serotonergic systems
- `dopamine` — dopamine receptors and dopaminergic systems
- `receptor-biology` — receptor binding, affinity, selectivity
- `structure-activity-relationship` — molecular structure vs biological activity
- `dosage` — dosing guidelines, threshold effects, dose-response
- `effects` — subjective and objective effects of compounds
- `synthesis` — chemical synthesis methods and procedures
- `timing` — duration, onset, and temporal aspects of compound effects
- `harm-reduction` — safety practices, risk mitigation, responsible use
- `legal` — legal status, regulations, scheduling
- `therapeutic-potential` — therapeutic applications and clinical research
- `compound-profile` — detailed compound-specific reference pages
- `psilocybin` — psilocybin and psilocin containing compounds

### Mushroom Cultivation
- `mushroom-cultivation` — mushroom growing techniques and methods
- `mushroom-foraging` — wild mushroom identification and foraging
- `gourmet-mushrooms` — edible/culinary mushroom species
- `medicinal-mushrooms` — mushrooms with therapeutic properties
- `sterile-technique` — aseptic procedures, contamination prevention
- `agar` — agar media preparation and use
- `grain-spawn` — grain-based spawn production
- `bulk-substrate` — bulk substrate preparation and use
- `fruiting-chamber` — fruiting environment setup and management
- `laminar-flow` — laminar flow hood use and design
- `glove-box` — still air box / glove box sterile technique
- `monotub` — monotub cultivation method
- `pf-tek` — PF TEK beginner cultivation method
- `log-cultivation` — log-based outdoor mushroom cultivation
- `cloning` — mushroom tissue cloning and isolation
- `strain-isolation` — isolating specific mushroom strains
- `tissue-culture` — tissue culture techniques
- `spore-print` — spore print collection and use
- `species-identification` — mushroom species identification methods
- `species-guide` — species-specific cultivation or reference guides
- `grain-to-bulk` — grain spawn to bulk substrate transition
- `contamination` — contamination identification and prevention
- `laboratory` — lab equipment and procedures
- `hygiene` — sanitation and hygiene practices
- `fae` — fresh air exchange for fruiting
- `co2` — carbon dioxide management in cultivation

### Mushroom Species & Materials
- `shiitake` — shiitake mushroom (Lentinula edodes)
- `lions-mane` — lion's mane mushroom (Hericium erinaceus)
- `oyster-mushroom` — oyster mushroom (Pleurotus species)
- `reishi` — reishi mushroom (Ganoderma lucidum)
- `lion's-mane` — lion's mane mushroom (Hericium erinaceus)
- `turkey-tail` — turkey tail mushroom (Trametes versicolor)
- `maitake` — maitake mushroom (Grifola frondosa)
- `chaga` — chaga mushroom (Inonotus obliquus)
- `pleurotus` — Pleurotus genus oyster mushrooms
- `stropharia` — Stropharia genus mushrooms
- `lentinula-edodes` — Lentinula edodes species
- `beta-glucans` — beta-glucan compounds in fungi
- `mycelium` — mycelial growth and networks
- `deadly-mushrooms` — toxic and deadly mushroom species
- `lookalikes` — mushroom species that resemble edible ones

### Mycoremediation & Applied Mycology
- `mycoforestry` — use of fungi in forestry and reforestation
- `mycofiltration` — fungal filtration for water treatment
- `mycopesticides` — fungi as biological pest control agents
- `forest-restoration` — forest ecosystem restoration
- `forest-floor` — forest floor ecology and decomposition
- `mycorrhizal` — mycorrhizal fungal associations
- `heavy-metals` — heavy metal contamination and remediation
- `petroleum` — petroleum and hydrocarbon contamination
- `pesticides` — pesticide contamination and remediation
- `pcb` — PCB contamination and remediation
- `dioxin` — dioxin contamination and remediation
- `water-treatment` — water purification and treatment systems
- `ecosystem` — ecosystem-level processes and dynamics

### Cultivation Materials & Methods
- `straw` — straw as substrate or mulch material
- `sawdust` — sawdust as substrate material
- `wood-chips` — wood chips as substrate or mulch
- `composites` — composite materials from biological sources
- `biomaterials` — biomaterials and bio-based materials
- `building-materials` — natural and alternative building materials
- `packaging` — sustainable packaging materials
- `outdoor-beds` — outdoor growing bed techniques
- `totem-method` — totem method for outdoor mushroom cultivation
- `wood-cultivation` — wood-based cultivation methods

### Permaculture & Land Management
- `mulch` — mulching materials and techniques
- `weed-management` — weed control and management strategies
- `weeds` — weed species and their management
- `rainwater` — rainwater collection and harvesting
- `water-harvesting` — water harvesting techniques and systems
- `mapping` — land mapping and survey techniques
- `topography` — topographical analysis and contour mapping
- `contour` — contour-based land design
- `landscape-analysis` — landscape reading and analysis
- `site-design` — permaculture site design

### Research & Methods
- `research-methods` — research methodologies and approaches


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


### Entheogens & Ethnobotany
- `ceremony` — ceremonial use, ritual contexts, sacred practices
- `amanita-muscaria` — Amanita muscaria (fly agaric) mushroom
- `fly-agaric` — fly agaric, Amanita muscaria
- `bicycle-day` — Bicycle Day (April 19, LSD discovery anniversary)
- `mk-ultra` — MK-Ultra CIA program, mind control research
- `discovery` — historical discoveries of compounds or species
- `mazatec` — Mazatec people, Mazatec mushroom traditions
- `soma` — Soma, Vedic ritual drink, identity debates
- `eleusinian` — Eleusinian Mysteries, kykeon
- `christianity` — Christian contexts, biblical mushroom theories
- `controversy` — controversial topics, debated claims
- `cross-cultural` — cross-cultural comparisons, shared practices
- `ayahuasca` — ayahuasca brew, DMT-containing preparations
- `bardo` — bardo states, Tibetan death/rebirth cosmology
- `bufonid-toad` — bufonid toad venom, 5-MeO-DMT sources
- `ego-death` — ego dissolution, mystical experiences
- `harmala` — harmala alkaloids, beta-carbolines, MAOIs
- `iboga` — iboga plant, ibogaine
- `peyote` — peyote cactus, mescaline
- `set-and-setting` — set and setting, context of psychedelic experiences
- `shamanism` — shamanic practices, indigenous healing traditions
- `smoked-compound` — compounds administered via smoking/vaporization
- `snuff` — snuff preparations, nasal administration
- `virola` — Virola genus, DMT snuff sources
- `comedown` — post-experience comedown, integration period
- `session-guide` — session preparation and facilitation guides
- `experience-guide` — experiential guidance, navigation aids
- `trip-sitting` — trip sitting, psychedelic sitting, safety monitoring
- `integration` — post-experience integration, processing insights
- `aftercare` — aftercare, post-session support and grounding
- `tibetan-book-of-the-dead` — Tibetan Book of the Dead, Bardo Thodol
- `mysticism` — mystical experiences, spiritual states
- `spirituality` — spiritual practices, beliefs, traditions

### Geography & Ecology
- `siberia` — Siberian regions, boreal environments
- `tropics` — tropical regions, tropical ecosystems
- `temperate` — temperate climate zones
- `habitat` — natural habitats, ecological niches
- `geography` — geographic features, regional characteristics
- `corridor` — wildlife corridors, ecological connectivity
- `forest-garden` — forest gardens, edible landscapes
- `predators` — predator species, predator-prey dynamics
- `voles` — vole species, small mammal management
- `hominid` — hominid species, human evolution
- `evolution` — evolutionary processes, adaptation
- `ancient` — ancient history, historical contexts
- `wind` — wind patterns, wind effects on growing
- `frost` — frost protection, freeze events
- `nature` — natural systems, wilderness
- `animals` — animal biology, wildlife
- `coastal` — coastal environments, marine-terrestrial interfaces
- `freshwater` — freshwater systems, ponds, streams
- `microclimate` — microclimate management, local weather modification
- `wildlife` — wildlife management, habitat creation
- `zones` — growing zones, hardiness zones, climate zones
- `1960s` — 1960s counterculture, psychedelic era

### Chemistry & Pharmacology (additional)
- `lsd` — lysergic acid diethylamide (LSD)
- `dmt` — N,N-dimethyltryptamine (DMT)
- `muscimol` — muscimol, GABAergic compound from Amanita
- `ibotenic-acid` — ibotenic acid, prodrug to muscimol
- `5-ht2a` — 5-HT2A serotonin receptor
- `ssri` — selective serotonin reuptake inhibitors
- `ergot` — ergot fungus, ergotamine, ergoline alkaloids
- `maoi` — monoamine oxidase inhibitors
- `maoi-interaction` — MAOI drug interactions, dietary restrictions
- `tryptamine` — tryptamine class compounds
- `beta-carboline` — beta-carboline class compounds
- `beta-glucan` — beta-glucan polysaccharides, immune modulators
- `betulin` — betulin, betulinic acid from birch bark
- `betulinic-acid` — betulinic acid, anti-tumor compound
- `ganoderic-acid` — ganoderic acids, triterpenoids from Reishi
- `grifolan` — grifolan, beta-glucan from Maitake
- `polysaccharide-k` — PSK, polysaccharide-K from Turkey Tail
- `polysaccharide-peptide` — PSP, polysaccharide-peptide
- `superoxide-dismutase` — superoxide dismutase (SOD), antioxidant enzyme
- `triterpenoid` — triterpenoid compounds
- `phosphate-ester` — phosphate ester linkages, psilocybin chemistry
- `mushroom-alkaloid` — alkaloids found in mushrooms
- `endogenous-compound` — endogenous compounds, naturally occurring in body
- `dose-response-curve` — dose-response relationships, pharmacodynamics
- `pharmacokinetics` — drug metabolism, absorption, half-life
- `phenomenology` — subjective experience, phenomenological descriptions
- `oral-active` — orally active compounds, bioavailability
- `threshold` — threshold doses, minimum effective doses
- `onset` — onset of effects, time to peak
- `peak` — peak effects, duration
- `adaptogen` — adaptogenic compounds, stress modulation
- `anti-inflammatory` — anti-inflammatory compounds, mechanisms
- `antioxidant` — antioxidant compounds, oxidative stress
- `anxiety` — anxiety, anxiolytic effects
- `ptsd` — PTSD, trauma treatment
- `depression` — depression, antidepressant effects
- `addiction` — addiction, substance dependence, recovery
- `contraindications` — medical contraindications, risk factors
- `clinical-research` — clinical studies, human trials
- `clinical-trial` — clinical trial design, methodology
- `pain-management` — pain management, analgesic properties
- `cancer` — cancer research, anti-tumor properties
- `cardiovascular` — cardiovascular effects, heart health
- `sleep` — sleep effects, sleep quality
- `inflammation` — inflammatory processes, anti-inflammatory
- `anatomy` — anatomical structures, morphology
- `glandular` — glandular systems, endocrine function
- `default-mode-network` — default mode network, brain connectivity
- `neuroplasticity` — neuroplasticity, brain adaptation
- `genomics` — genomics, genome studies
- `genotype` — genotype, genetic variation
- `phenotype` — phenotype, expressed characteristics
- `melanin` — melanin, fungal pigmentation
- `enzymes` — enzymatic processes, enzyme function

### People & Organizations (additional)
- `mckenna` — Terence McKenna, Dennis McKenna
- `hofmann` — Albert Hofmann, LSD discoverer
- `maria-sabina` — Maria Sabina, Mazatec curandera
- `wasson` — R. Gordon Wasson, ethnomycologist
- `sandoz` — Sandoz pharmaceutical company
- `holzer` — Sepp Holzer, permaculture farmer
- `allegro` — John Allegro, sacred mushroom theory
- `harvard` — Harvard University, Harvard research
- `leary` — Timothy Leary, psychedelic research
- `fukuoka` — Masanobu Fukuoka, natural farming pioneer

### Homesteading & Community (additional)
- `local-economy` — local economic systems, community economics
- `trade` — trade, barter, exchange systems
- `biological-control` — biological pest control, natural enemies
- `foundations` — building foundations, earthworks
- `geometry` — geometric design, sacred geometry
- `field-guide` — field guides, identification resources
- `drug-policy` — drug policy, legal frameworks
- `scheduling` — scheduling, timing, seasonal planning
- `testing` — soil testing, quality testing
- `journaling` — journaling, record keeping
- `meditation` — meditation, mindfulness practices
- `etymology` — etymology, word origins
- `integrated-pest-management` — integrated pest management (IPM)
- `trapping` — trapping, pest control methods
- `activism` — activism, advocacy, social movements
- `education` — education, teaching, learning
- `community` — community building, social organization
- `self-reliance` — self-reliance, independence
- `self-sufficiency` — self-sufficiency, homesteading skills
- `law` — legal frameworks, regulations
- `business` — business, enterprise, marketing
- `reform` — policy reform, social change
- `regulation` — regulatory frameworks, compliance
- `intellectual-property` — patents, IP, open-source licensing
- `patents` — patent systems, patent law
- `observation` — observation skills, nature observation
- `tools` — tools, equipment, implements
- `reference` — reference materials, data compilations
- `resources` — resource management, resource lists

### Growing Methods (additional)
- `farming` — farming practices, agricultural methods
- `natural-farming` — natural farming, minimal intervention
- `sustainable-agriculture` — sustainable agriculture, long-term farming
- `agroforestry` — agroforestry, tree-crop integration
- `aquaculture` — aquaculture, fish farming
- `aquaponics` — aquaponics, fish-plant systems
- `foraging` — wild foraging, harvesting wild plants
- `growing-guide` — species-specific growing guides
- `indoor-cultivation` — indoor growing environments
- `outdoor` — outdoor growing, field cultivation
- `intensive-gardening` — intensive gardening, biointensive methods
- `urban-gardening` — urban gardening, city growing
- `tropical-gardening` — tropical gardening techniques
- `container-garden` — container gardening, raised beds
- `balcony` — balcony gardening, small-space growing
- `difficult-sites` — challenging growing conditions
- `direct-seeding` — direct seeding, field planting
- `intercropping` — intercropping, multiple crop systems
- `companion-planting` — companion planting combinations
- `polyculture` — polyculture systems, multiple species
- `green-manure` — green manure crops, soil building
- `clover-cover` — clover cover crops, nitrogen fixation
- `straw-mulch` — straw mulching, weed suppression
- `guild` — plant guilds, functional groupings
- `guilds` — guild systems, permaculture guilds
- `coppicing` — coppicing, woodland management
- `irrigation` — irrigation systems, water delivery
- `ventilation` — ventilation, air circulation
- `temperature` — temperature management, climate control
- `propagation` — plant propagation, multiplication
- `seeds` — seed saving, seed management
- `seed-production` — seed production, seed crops
- `planting` — planting techniques, timing
- `plant-spacing` — plant spacing, density management
- `training` — plant training, pruning, shaping
- `stacking` — stacking functions, vertical space use
- `succession` — ecological succession, progressive planting
- `swales` — swales, water-harvesting earthworks
- `fire` — fire management, controlled burns
- `pasture` — pasture management, grazing systems
- `livestock` — livestock management, animal husbandry
- `pollinators` — pollinator support, bee keeping
- `insects` — insect management, beneficial insects
- `pests` — pest identification, pest management
- `pathogens` — plant pathogens, disease management
- `plant-disease` — plant diseases, diagnostics
- `trees` — tree care, orchard management
- `timber` — timber production, forestry
- `roundwood` — roundwood construction, natural building
- `shelter` — shelter construction, housing
- `building` — building techniques, construction
- `natural-building` — natural building materials and methods
- `ponds` — pond construction, aquaculture ponds

### Soil & Biology (additional)
- `soil-biology` — soil biological processes, soil life
- `soil-building` — soil building techniques, improvement
- `soil-health` — soil health assessment, indicators
- `soil-science` — soil science, pedology
- `organic-matter` — organic matter, humus, soil organic carbon
- `nitrogen` — nitrogen cycle, nitrogen management
- `carbon` — carbon in soil, carbon management
- `carbon-cycling` — carbon cycling, decomposition pathways
- `carbon-sequestration` — carbon sequestration, climate mitigation
- `nutrient-cycling` — nutrient cycling, mineral flows
- `decomposition` — decomposition processes, breakdown
- `decomposers` — decomposer organisms, detritivores
- `earthworm` — earthworms, vermicomposting
- `vermicompost` — vermicomposting, worm castings
- `rhizosphere` — rhizosphere ecology, root-zone interactions
- `bacteria` — bacterial biology, soil bacteria
- `ectomycorrhiza` — ectomycorrhizal fungi associations
- `saprotrophs` — saprotrophic organisms, decay fungi
- `entomopathogenic` — entomopathogenic fungi, insect-killing fungi
- `biocontrol` — biological control agents
- `mycoremediation` — mycoremediation, fungal cleanup
- `mycorestoration` — mycorestoration, ecological repair
- `remediation` — environmental remediation, cleanup
- `restoration` — ecological restoration, rehabilitation
- `conservation` — conservation, preservation
- `biodiversity` — biodiversity, species diversity
- `fungal-biodiversity` — fungal biodiversity, species richness
- `fungal-ecology` — fungal ecology, environmental roles
- `forest-ecology` — forest ecology, woodland ecosystems
- `environment` — environmental factors, context
- `resilience` — ecological resilience, system stability
- `erosion` — soil erosion, erosion control
- `silt` — silt, soil texture, sediment
- `trace-elements` — trace elements, micronutrients
- `filtration` — water filtration, soil filtering
- `recycling` — nutrient recycling, waste recycling

### Plants & Crops (additional)
- `botany` — botanical science, plant biology
- `plant-biology` — plant biology, physiology
- `herbs` — herbs, herbaceous plants
- `herbalism` — herbalism, herbal medicine
- `traditional-medicine` — traditional medicine systems
- `traditional-chinese-medicine` — TCM, Chinese herbal medicine
- `indigenous-medicine` — indigenous healing practices
- `plant-medicine` — plant-based medicine, herbal remedies
- `natural-remedies` — natural remedies, home treatments
- `calendula` — calendula, pot marigold
- `thyme` — thyme, Thymus species
- `barley` — barley, Hordeum vulgare
- `kiwi` — kiwi, Actinidia species
- `vine` — vine crops, climbing plants
- `vegetables` — vegetable crops, food gardens
- `crops` — crop production, agronomic crops
- `food` — food production, food systems
- `food-production` — food production methods
- `nutrition` — nutritional content, dietary value
- `cooking` — cooking, food preparation
- `tea` — tea, herbal teas, fermented teas
- `essential-oil` — essential oils, aromatic compounds

### Cannabis (additional)
- `indica` — Cannabis indica, indica-type varieties
- `sativa` — Cannabis sativa, sativa-type varieties
- `ruderalis` — Cannabis ruderalis, autoflowering genetics
- `landrace` — landrace varieties, heritage strains
- `trichome` — trichomes, resin glands
- `hashish` — hashish, resin products
- `kief` — kief, dry-sift resin
- `breeding` — cannabis breeding, strain development
- `hybridization` — hybridization, cross-breeding
- `selection` — phenotypic selection, breeding selection
- `genetics` — cannabis genetics, inheritance
- `classification` — cannabis classification, taxonomy debates
- `morphology` — plant morphology, structural features
- `identification` — plant identification, species determination
- `substrate` — growing substrates, media
- `clay-pellets` — clay pellets, LECA, hydroton
- `inoculation` — inoculation, microbial inoculants

### Mushroom Cultivation (additional)
- `mushroom` — mushrooms broadly, general mushroom topics
- `gourmet-mushroom` — gourmet/edible mushroom species
- `medicinal-mushroom` — medicinal mushroom species
- `oyster` — oyster mushrooms, Pleurotus species
- `truffle` — truffles, Tuber species
- `spawn` — mushroom spawn, inoculum
- `inoculation` — inoculation techniques
- `deployment` — spawn deployment, field inoculation
- `tree-inoculation` — tree inoculation, log inoculation
- `materials` — cultivation materials, supplies
- `application` — substrate application, colonization
- `techniques` — cultivation techniques, methods
- `extraction` — extraction methods, processing
- `solvent` — solvent extraction, solvents
- `grifola-frondosa` — Grifola frondosa, Maitake
- `d-fraction` — D-fraction, Maitake extract
- `molecular-systematics` — molecular systematics, DNA analysis
- `field-methods` — field collection methods, sampling
- `survey` — biodiversity surveys, monitoring

### Meta (additional)
- `reference` — reference materials, data compilations
- `growing-guide` — species-specific growing guides
- `science` — scientific research, methodology
- `research` — research activities, investigations
- `systems` — systems thinking, integrated systems
- `networks` — networks, connections, relationships
- `multi-function` — multifunctional elements, stacked functions
- `synergy` — synergistic relationships, mutual benefits
- `geology` — geological factors, rock, minerals
- `fish` — fish species, aquaculture
- `music` — music in ceremonial/cultural contexts
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

### Additional Tags (added during lint 2026-04-13)
- `application` — application
- `balcony` — balcony
- `building` — building
- `calendula` — calendula
- `container-garden` — container-garden
- `crops` — crops
- `difficult-sites` — difficult-sites
- `diversity` — diversity
- `earthworm` — earthworm
- `green-manure` — green-manure
- `growing-guide` — growing-guide
- `guilds` — guilds
- `herbalism` — herbalism
- `herbs` — herbs
- `intensive-gardening` — intensive-gardening
- `intercropping` — intercropping
- `irrigation` — irrigation
- `kiwi` — kiwi
- `mushroom` — mushroom
- `natural-building` — natural-building
- `natural-remedies` — natural-remedies
- `nitrogen` — nitrogen
- `nutritive-cycle` — nutritive-cycle
- `observation` — observation
- `plant-disease` — plant-disease
- `plant-spacing` — plant-spacing
- `planting` — planting
- `polyculture` — polyculture
- `propagation` — propagation
- `recycling` — recycling
- `resources` — resources
- `rhizosphere` — rhizosphere
- `roundwood` — roundwood
- `self-reliance` — self-reliance
- `self-sufficiency` — self-sufficiency
- `shelter` — shelter
- `soil-biology` — soil-biology
- `systems` — systems
- `tea` — tea
- `temperature` — temperature
- `thyme` — thyme
- `timber` — timber
- `trace-elements` — trace-elements
- `urban-gardening` — urban-gardening
- `vermicompost` — vermicompost
- `vine` — vine

### Additional Tags (added during lint 2026-04-13 batch 2)
- `aquaculture` — aquaculture
- `coppicing` — coppicing
- `fish` — fish
- `food-production` — food-production
- `microclimate` — microclimate
- `ponds` — ponds

### Additional Tags (added during lint 2026-04-13 maintenance)
- `adaptogen` — Adaptogenic compounds and herbs
- `anatomy` — Biological anatomy, organ systems
- `anti-inflammatory` — Anti-inflammatory compounds and effects
- `antioxidant` — Antioxidant compounds and effects
- `ayahuasca` — Ayahuasca, psychedelic brew
- `bardo` — Bardo, intermediate states in Tibetan Buddhism
- `barley` — Barley cultivation and uses
- `beta-carboline` — Beta-carboline class compounds
- `beta-glucan` — Beta-glucan polysaccharides in fungi
- `betulin` — Betulin compound from birch bark
- `betulinic-acid` — Betulinic acid compound
- `breeding` — Plant breeding and genetics
- `bufonid-toad` — Bufonid toads, bufo venom compounds
- `cancer` — Cancer, oncology, anti-tumor research
- `cardiovascular` — Cardiovascular system, heart health
- `clay-pellets` — Clay pellets for cultivation substrates
- `clinical-trial` — Clinical trials, clinical research
- `clover-cover` — Clover as cover crop
- `co2` — Carbon dioxide management
- `comedown` — Comedown, after-effects
- `d-fraction` — D-fraction, maitake extract compound
- `direct-seeding` — Direct seeding, no-transplant methods
- `dose-response-curve` — Dose-response relationships and curves
- `ectomycorrhiza` — Ectomycorrhizal fungal associations
- `ego-death` — Ego death, ego dissolution experiences
- `endogenous-compound` — Endogenous compounds, naturally occurring
- `enzymes` — Enzymes, enzymatic processes
- `essential-oil` — Essential oils, aromatic compounds
- `experience-guide` — Experience guides, trip reports
- `extraction` — Extraction methods and techniques
- `fae` — Fresh air exchange for cultivation
- `fire` — Fire ecology, controlled burns, fire management
- `fukuoka` — Masanobu Fukuoka, natural farming pioneer
- `ganoderic-acid` — Ganoderic acid from reishi mushroom
- `genotype` — Genotype, genetic makeup
- `geology` — geology
- `glandular` — Glandular structures, secretory tissues
- `gourmet-mushroom` — Gourmet and culinary mushrooms
- `grifola-frondosa` — Grifola frondosa (maitake) species
- `grifolan` — Grifolan beta-glucan from maitake
- `harmala` — Harmala alkaloids (harmine, harmaline)
- `hashish` — Hashish, concentrated cannabis resin
- `hybridization` — Hybridization, cross-breeding
- `identification` — Identification methods, species ID
- `indica` — Cannabis indica subspecies
- `indigenous-medicine` — Indigenous healing practices and plant medicine
- `indoor-cultivation` — Indoor cultivation techniques
- `inflammation` — Inflammation, inflammatory response
- `integration` — Integration of experiences, psychological integration
- `kief` — Kief, dry-sieved cannabis trichomes
- `landrace` — Landrace varieties, heirloom strains
- `leary` — Timothy Leary, psychedelic research
- `lentinula-edodes` — Lentinula edodes (shiitake) species
- `lion's-mane` — Lion's mane mushroom (Hericium erinaceus)
- `maoi` — Monoamine oxidase inhibitors
- `maoi-interaction` — MAOI interactions and contraindications
- `materials` — Materials, construction materials
- `medicinal-mushroom` — Medicinal mushrooms, therapeutic fungi
- `melanin` — Melanin pigmentation
- `morphology` — Morphology, physical form and structure
- `mushroom-alkaloid` — Alkaloid compounds from mushrooms
- `mysticism` — Mysticism, mystical experiences
- `natural-farming` — Natural farming broadly, Masanobu Fukuoka methods
- `onset` — Onset time of compound effects
- `oral-active` — Orally active compounds
- `oyster` — Oyster mushroom broadly
- `pain-management` — Pain management, analgesia
- `pasture` — Pasture management, rotational grazing
- `peak` — Peak effects of compounds
- `pf-tek` — PF TEK beginner mushroom cultivation
- `pharmacokinetics` — Pharmacokinetics, drug metabolism
- `phenomenology` — Phenomenology, subjective experience
- `phenotype` — Phenotype, expressed traits
- `phosphate-ester` — Phosphate ester chemistry
- `plant-biology` — Plant biology broadly
- `plant-medicine` — Plant medicine broadly, herbal medicine
- `polysaccharide-k` — Polysaccharide-K (PSK) from turkey tail
- `polysaccharide-peptide` — Polysaccharide peptides from fungi
- `ruderalis` — Cannabis ruderalis subspecies
- `sativa` — Cannabis sativa subspecies
- `science` — Science broadly
- `seed-production` — Seed production and saving
- `selection` — Selection, plant or strain selection
- `session-guide` — Session guides for therapeutic experiences
- `set-and-setting` — Set and setting in psychedelic experiences
- `sleep` — Sleep, sleep disorders, sleep science
- `smoked-compound` — Smokable plant compounds
- `snuff` — Nasal snuff preparations
- `soil-science` — Soil science, pedology
- `solvent` — Solvents for extraction and chemistry
- `stacking` — Function stacking in permaculture
- `straw-mulch` — Straw as mulching material
- `superoxide-dismutase` — Superoxide dismutase (SOD) enzyme
- `sustainable-agriculture` — Sustainable agriculture practices
- `synergy` — Synergistic effects between compounds
- `synthetic-log` — Synthetic log substrates for mushroom growing
- `threshold` — Threshold effects, minimum effective doses
- `tibetan-book-of-the-dead` — Tibetan Book of the Dead (Bardo Thodol)
- `traditional-chinese-medicine` — Traditional Chinese Medicine (TCM)
- `traditional-medicine` — Traditional medicine systems, ethnomedicine
- `training` — Plant training techniques (LST, HST)
- `tree-inoculation` — Tree inoculation with fungi or microbes
- `trichome` — Trichomes, plant glandular structures
- `triterpenoid` — Triterpenoid compounds in fungi
- `tropical-gardening` — Tropical gardening techniques
- `truffle` — Truffles, hypogeous fungi
- `tryptamine` — Tryptamine class compounds and chemistry
- `virola` — Virola tree genus, DMT sources
- `zones` — Zoning, permaculture zones
