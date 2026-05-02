#!/usr/bin/env python3
"""Build all 14 navigation indexes for the LLM Wiki."""
import os, re
from collections import defaultdict, Counter

wiki = os.path.expanduser("~/wiki")

# Collect all pages
all_pages = []
page_dir = {}
for d in ["concepts", "entities", "comparisons", "queries"]:
    path = os.path.join(wiki, d)
    if not os.path.exists(path): continue
    for f in sorted(os.listdir(path)):
        if f.endswith(".md") and not f.startswith("index-"):
            name = f[:-3]
            all_pages.append(name)
            page_dir[name] = d

print(f"Total pages: {len(all_pages)}")

# Directory-based assignment
page_topics = {}
for name in all_pages:
    d = page_dir.get(name)
    if d == "entities":
        page_topics[name] = "species"; continue
    if d in ("comparisons", "queries"):
        page_topics[name] = "comparisons-queries"; continue

# Topic keywords (substring match, priority order matters)
topic_keywords = {
    "fungal-ecology": [
        "fungal", "fungi", "myco", "mycel", "spore", "hypha", "lichen", "endophy",
        "saprob", "decompos", "humus", "glomal", "mycorrhiz", "ascomyc", "basidiomyc",
        "ergot", "cordyceps", "trichoderma", "laccase", "peroxidase", "mycotoxin",
        "aflatoxin", "rhizobia", "rhizosphere", "nematode", "collembola", "glomalin",
        "pgpr", "suillus", "russula", "trametes", "phellinus", "amanita", "conocybe",
        "inocybe", "pluteus", "boletus", "coprophilous", "fungicolous", "neurotropic",
        "keratinophilic", "dermatophyte", "sequestrate", "cortinarius", "truffle",
        "chanterelle", "morel", "lactarius", "cantharellus", "matsutake",
        "biodiversity-of-fungi", "fungal-evolution", "fungal-sexual", "fungal-culture",
        "fungal-photobiology", "fungal-parasit", "spore-dispersal",
        "symbiotic-fungi", "ectomycorrhizal", "arbuscular", "ericoid",
        "teaming-with-fungi", "teaming-with-microbes",
        "palmer-about-mushrooms", "ramsbottom", "bloomfields-orchard",
        "actinorhizal", "frankia", "nitrogen-fix", "legume", "rhizobium",
        "biotroph", "necrotroph", "pathogenic", "bioprotect",
        "chitin", "chitosan", "beta-glucan", "glycoprotein",
        "gilled", "pored", "polypor", "agaric", "bracket",
        "myxomycete", "slime-mold", "oomycete", "zygomycete",
        "mycetozoan", "laboulbeniales", "neurospora", "fairy-ring",
        "stropharia", "gymnopilus", "light-initiation", "pinhead-initiation",
        "claviceps-paspali", "cryptococcus", "root-exudate", "amf-biocontrol",
        "hemicellulase", "geosiphon", "piriformospora", "guttation",
        "magnaporthe", "mold-identification",
        "symbiosis-bryo", "symbiosis-art", "tryptophan",
        "photosynthesis", "transport-pathway", "nutritive-cycle",
        "palmer", "phallus", "stinkhorn", "puff-ball", "lycoperdaceae",
    ],
    "mushroom-cultivation": [
        "mushroom", "oyster", "shiitake", "reishi", "substrate", "spawn", "fruiting",
        "inocul", "pasteuriz", "steriliz", "agar", "monotub", "casing", "primordia",
        "contamination", "log-cultiv", "gourmet", "truffle-cult", "wood-loving",
        "woodlover", "copelandia", "panaeolus", "jarrold", "pf-tek", "falconer",
        "cuthill", "gottlieb", "azurescens", "working-with-agar",
        "synthetic-log", "laminar-flow", "desiccant",
        "mushroom-cultiv", "mushroom-market", "mushroom-grain",
        "mushroom-substrate", "mushroom-spore",
        "psilocybe-cubensis-cultiv", "psilocybin-production",
        "fungal-culture-preserv", "hepa-filter",
        "stamets-grow", "stamets-invention", "stamets-maitake",
        "stamets-outdoor", "stamets-sterile", "stamets-growing",
        "enoki", "nameko", "shimeji", "straw-cultiv", "stem-butt",
        "strain-isolation", "strain-selection", "deep-bed", "coprinus",
        "porcini", "pleurotus", "maitake", "sclerotia",
        "pda-and-tissue", "tissue-culture", "wild-specimen",
        "fmc-application", "phase-ii-room", "pinhead-init",
        "water-soluble-phosphoric",
        "ganoderma", "enriched-sawdust",
    ],
    "psychedelics": [
        "psychedel", "psychoactive", "entheogen", "dmt", "lsd", "mescaline", "salvia",
        "iboga", "ayahuasca", "peyote", "mdma", "ketamine", "psilocybin",
        "mckenna", "pihkal", "tihkal", "wasson", "hofmann", "shulgin",
        "hallucinogen", "muscimol", "leary", "castaneda", "huxley", "entheogenic",
        "shamanic", "ceremony", "microdose", "sacred", "ritual",
        "shroom-cultural", "turner-essential", "turner-multiple", "hancock-supernatural",
        "metzner", "weil-the-natural-mind", "weil-drug-use", "weil-intoxic",
        "weil-psychedelic", "weil-cultural", "weil-the-mind",
        "powell-psilocybin", "leary-harvard", "timothy-leary",
        "maria-sabina", "harner-cross", "amaringo",
        "marijuana-magick", "plant-teachers",
        "golden-guide-hallucinogenic",
        "dob-pihkal", "2c-b", "dob-compound", "dob-entity",
        "magic-mushrooms-around", "magic-mushrooms-of",
        "neotropical-psilocybin", "psilocybin-image",
        "gartz-magic", "guzman-allen",
        "lsd-entity", "psilocybin-entity", "dmt-entity", "mescaline-entity",
        "tryptamine", "pianka-psychoactive", "arthur-mushrooms-and-mankind",
        "mckenna-food-of-the-gods", "amanita-muscaria-herb",
        "mystery-cult", "ancient-greek-mystery", "eleusinian",
        "soma-hypothesis", "kykeon",
        "blue-lotus", "belladonna", "nightshade", "datura",
        "betacarboline", "beta-carboline", "harmala", "yage",
        "visionary", "vegetalista", "amazonian", "shipibo",
        "archaic-revival", "bicycle-day",
        "5-meo", "5-methoxy", "aleph-", "dpt-", "dipt-",
        "altered-state", "set-and-setting", "integration",
        "mushrooms-and-mankind", "ethnomycology",
        "liberty-cap", "sandoz", "dutch-smart", "good-friday",
        "harm-reduction", "phenethylamine", "essential-amphetamine",
        "salvinorin", "dm-reference",
        "snuff", "ethnobotany", "pituri", "narcotic", "ololiuqui",
        "soma", "haoma", "teonanacatl", "rigveda", "yopo", "virola", "cohoba",
        "cebil", "cashinahua", "mescal-bean", "kanna", "turkestan",
        "dionysian", "pelanos", "hecatonkephalos", "persephone", "zoroaster",
        "sachamama", "yakuruna", "susto", "mandrake",
        "consciousness", "informational", "computational", "natural-intelligence",
        "default-mode", "complexity", "deep-relaxation", "mind-body",
        "2c-c", "2c-d", "2c-e", "2c-family", "2c-i", "2c-p", "2c-t",
        "md-", "mda-", "mde-", "mdo-", "doi-", "dom-", "dmmda-", "mmda-",
        "tma-", "doc-", "doet-", "mdoi-",
        "cactus", "san-pedro", "dominator-culture", "consumer-versus-conserver",
    ],
    "permaculture": [
        "permaculture", "mollison", "holmgren", "holzer", "hemenway", "swale",
        "guild", "polyculture", "food-forest", "chinampa", "keyline", "earthwork",
        "hugelkultur", "biodynamic", "resilience", "demeter",
        "zone-and-sector", "edge-effect", "aquaculture",
        "permaculture-plant", "permaculture-design", "permaculture-adj",
        "allegro", "pdc", "sheet-mulch", "herb-spiral", "mandala-garden",
        "banana-circle", "chicken-tractor", "greywater", "vermifiltration",
        "water-harvest", "dam-and-pond", "chinampa", "forest-garden",
        "gaia-garden", "biodigester", "bioregional",
        "biointensive", "carbon-farming", "diet-design", "bed-preparation",
        "pattern-language", "zone-analysis",
        "broadscale", "patterns-in-nature",
        "windbreak", "shelterbelt", "zone-5",
        "community-finance", "community-land", "community-supported",
        "ethical-investment", "local-currenc", "zeri",
        "farming-with-air", "human-settlement",
        "permitted-vs", "energy-descent",
    ],
    "natural-farming": [
        "fukuoka", "knf", "cho", "jadam", "natural-farming", "imo", "fpj",
        "fish-amino", "fermented-plant", "ohn", "ws-ca", "ws-k",
        "effective-microorganism", "clay-ball-seed", "natural-way-of-farming",
        "one-straw", "master-cho", "chos-global", "indigenous-microorganism",
        "fermented-fruit", "oriental-herb", "straw-mulch", "no-plow",
        "fukuoka-living", "fukuoka-straw", "fukuoka-weed", "fukuoka-pest",
        "fukuoka-natural", "fukuoka-dandelion", "fukuoka-barley",
        "fukuoka-rice", "fukuoka-acacia", "fukuoka-clover",
    ],
    "cannabis": [
        "cannabis", "cannabinoid", "thc", "cbd", "terpen", "trichome", "hashish",
        "hemp", "marijuana", "cervantes", "blesching", "rosenthal",
        "green-cannabis", "cannabis-alchemy", "cannabis-health",
        "clarke-marijuana", "sinsemilla", "scrog", "sog",
        "cannabis-genetic", "cannabis-seed", "cannabis-pest",
        "cannabis-pruning", "cannabis-harvest", "cannabis-organic",
        "cannabis-outdoor", "cannabis-indoor", "cannabis-medium",
        "cannabis-clone", "cannabis-autoflower", "autoflower",
        "lemon-cannabis", "cannabidiol", "endocannabinoid",
        "fimming", "lollipopping", "main-lining", "re-vegging",
        "screen-of-green", "sea-of-green", "cmh-grow", "hps-grow",
        "led-grow", "guerilla-grow", "low-stress", "cal-mag",
        "foliar-feed", "cultivation-facility", "live-resin",
        "vic-high", "phase-ii",
    ],
    "soil-and-compost": [
        "soil", "compost", "vermicompost", "worm", "teaming", "nutrient",
        "nitrogen", "phosphorus", "potassium", "mulch", "biochar",
        "fertilizer", "manure", "amendment", "till", "cover-crop", "humic",
        "bacterial", "protozoa", "dynamic-accumulator", "regenerative",
        "compost-tea", "biochar-solution", "terra-preta", "pyrolysis",
        "ingham-field-guide", "actively-aerated", "aact",
        "carbon-negative", "soil-food-web", "no-till-garden",
        "soil-ecology", "soil-amendment", "earthworm",
        "trace-mineral", "micronutrient",
        "rock-dust", "mineral-supplement", "organic-matter", "cation-exchange",
        "lactic-acid-bacteria-lab", "ingham-moss", "ingham-root", "ingham-vineyard",
    ],
    "gardening": [
        "garden", "vegetable", "plant", "crop", "weed", "greenhouse", "trellis",
        "pruning", "grafting", "companion", "beekeep", "pollinator", "insect",
        "seed", "nursery", "pasture", "orchard", "fruit", "grain", "aquaponic",
        "hydroponic", "aerobic", "season-extension", "integrated-pest",
        "raised-bed", "seed-saving", "heirloom", "natural-farming-guide",
        "faires-garden", "faires-vegetable", "faires-fruit",
        "duggar", "bahay-kubo", "bloomfield-orchard",
        "urban-permaculture", "urban-farming", "urban-guerilla",
        "allium", "apple-tree", "bamboo-grow",
        "bean-grow", "berry-grow", "blueberry", "citrus", "grape",
        "stone-fruit", "brassica", "tomato", "pepper-grow",
        "bat-conserv", "bird-habitat", "amphibian",
        "cold-frame", "row-cover", "frost-protect",
        "harvest", "propagation", "cutting", "division",
        "transplant", "hardening-off",
        "faires-", "hamilton-", "solomon-",
        "growing-guide", "growing-", "growing-by",
        "bee-forage", "bee-product", "swarm-capture", "top-bar-hive", "queen-rearing",
        "bamboo-species", "berry-species", "palm-tree", "multi-purpose-tree",
        "coleman", "bunya", "chestnut", "hazelnut", "persimmon",
        "jujube", "macadamia", "wattle", "willow", "figs-ficus",
        "aeroponics", "bubbleponics", "deep-water-culture", "ebb-and-flow",
        "keyhole-bed", "grow-tunnel", "hoop-house", "extending-growing",
        "potato-growing", "sweet-potato", "okra-growing", "ginger-growing",
        "turmeric-growing", "garlic-growing", "onion-growing", "carrot-growing",
        "cucumber-growing", "lettuce-and-leafy", "chicories", "fodder-growing",
        "hay-and-forage", "grass-fed", "winter-squash", "chamomile-growing",
        "holy-basil", "lemon-balm", "valerian-growing", "passionflower",
        "parsley-celery", "hawthorn", "respiratory-herbs", "dried-herb",
        "xeriscaping", "edible-landscape", "green-roof", "living-wall",
        "wildlife-habitat", "prairie-ecology", "forest-ecology", "wild-foraging",
        "xeriscape", "ornamental-grass", "lawn-care", "organic-lawn",
        "organic-pest", "specific-pest",
        "invasive-species", "leatherjacket", "powdery-mildew", "clubroot",
        "slugs-and-snails", "voles-control", "natural-pest",
        "irrigation", "drip-irrig", "watershed", "constructed-wetland",
        "desalination", "well-drilling", "passive-irrig", "graywater",
        "pond-maint", "water-management", "water-storage", "water-tank",
        "water-source", "water-diversion", "water-purif",
        "climate-and-microclimate", "low-fire", "salt-tolerant",
        "white-clover", "ground-cover", "geoff-hamilton",
        "farmers-market", "selling-farm", "seasonal-planning",
        "edible-landscaping", "growing-lettuce", "growing-potato",
        "growing-sweet-corn", "growing-by-chunking",
    ],
    "bioremediation": [
        "bioremediation", "mycoremediation", "phytoremediation", "remediation",
        "singh", "pollutant", "hydrocarbon", "pcb", "heavy-metal",
        "hyperaccumul", "phytomining", "bioaugment", "bioslurry", "pah",
        "contaminant", "toxicity", "detoxif", "degradat",
        "acid-mine", "azo-dye", "biosorption", "biostimul",
        "biofilter", "bioaccumul", "biotransform",
        "restoration", "reclamation", "riparian", "wetland",
        "phytoextraction", "phytostab", "phytovolatil", "rhizofiltr",
        "desertification", "pulp-paper", "effluent",
        "tahuya-forest", "ohana-watershed",
    ],
    "herbalism": [
        "herbal", "medicinal", "tincture", "salve", "remedy", "adaptogenic",
        "ashwagandha", "echinacea", "gotu-kola", "nootropic",
        "cardiovascular-herbs", "digestive-herbs", "nervine-herbs",
        "antimicrobial-herbs", "cancer-treatment", "medicinal-mushroom",
        "medicinal-plant", "plant-medicine",
        "ahcc", "turkey-tail", "lions-mane", "reishi",
        "chaga", "immune-modul", "anti-inflamm",
        "atp", "cellular-energy", "receptor-binding",
        "lentinan", "psk-", "psp-", "schizophyllan",
        "maitake-cancer", "maitake-d-fraction", "antitumour",
        "ganoderic", "polysaccharide", "womens-health",
        "oral-polysaccharide", "mandrake",
        "herb-drug", "herb-growing", "macrobiotics",
    ],
    "homesteading": [
        "homestead", "chicken", "poultry", "livestock", "cattle", "sheep", "goat",
        "pig", "rabbit", "dairy", "butcher", "smoke", "curing", "canning",
        "preserv", "dehydrat", "off-grid", "solar", "fencing", "building",
        "construction", "cob", "earthbag", "rocket-stove", "masonry", "cordwood",
        "adobe", "root-cellar", "barn", "duck", "goose", "quail", "turkey",
        "animal-harvest", "animal-tract", "animal-byproduct",
        "black-soldier-fly", "biodiesel", "biogas",
        "small-scale", "appropriate-technology", "woodlot",
        "candle-making", "soap-making", "cheese-making", "leather",
        "granola-making", "ghee", "nut-butter", "jam-and-jelly",
        "pickle-making", "jerky-making", "hot-sauce-making",
        "preparedness", "earthquake", "hurricane", "wildfire", "extreme-heat",
        "winter-storm", "emergency",
        "solar", "wind-power", "rocket-mass", "radiant-floor", "pellet-stove",
        "micro-hydro", "photovoltaic", "energy-",
        "earth-plaster", "rammed-earth", "timber-frame", "tiny-house",
        "skoolie", "reciprocal-roof", "mud-oven", "ice-house", "earth-berm",
        "firewood", "wood-fired", "raw-milk", "maple-syrup",
        "smoking-meat", "fermented-hot-sauce", "honey-extraction",
        "honey-varieties", "strawyard", "charcoal-production",
        "bokashi", "food-in-hard-times",
    ],
    "brewing": [
        "brew", "wine", "beer", "mead", "cider", "vinegar", "koji", "miso",
        "tempeh", "sourdough", "kefir", "kimchi", "sauerkraut", "lacto-ferment",
        "probiotic", "distill", "fermentation", "kombucha", "natto", "hops",
        "malt", "yeast",
    ],
}

# Keyword assignment
for name in all_pages:
    if name in page_topics: continue
    for topic, keywords in topic_keywords.items():
        for kw in keywords:
            if kw in name:
                page_topics[name] = topic
                break
        if name in page_topics: break

# Manual fallback assignments
manual = {
    "consumer-versus-conserver-society": "permaculture",
    "csa-farm-share-model": "permaculture",
    "lactic-acid-bacteria-lab": "soil-and-compost",
    "magnaporthe-grisea-functional-genomics-rice-blast": "fungal-ecology",
    "mandrake-mandragora-officinarum-in-european-folklore": "herbalism",
    "maple-syrup-production": "homesteading",
    "mdoi-compound-profile": "psychedelics",
    "mold-identification-guide": "fungal-ecology",
    "patterns-in-nature": "permaculture",
    "pda-and-tissue-culture": "mushroom-cultivation",
    "smoking-meat-and-fish": "homesteading",
    "tissue-culture-cloning": "mushroom-cultivation",
    "wild-specimen-isolation": "mushroom-cultivation",
    "water-soluble-phosphoric-acid-wpa": "mushroom-cultivation",
    "fmc-application-and-troubleshooting": "mushroom-cultivation",
    "dighton-wood-decay-ecosystem-carbon": "fungal-ecology",
    "landscape-fabric-alternatives": "gardening",
    "microdosing-guide": "psychedelics",
    "microdosing-theory-and-practice": "psychedelics",
    "outdoor-wood-lover-cultivation": "mushroom-cultivation",
    "psilocybe-bohemica-central-european": "fungal-ecology",
    "psilocybe-cubensis-potency-variation-by-flush": "fungal-ecology",
    "psilocybe-cubensis-profile": "fungal-ecology",
    "psilocybe-cyanescens-profile": "fungal-ecology",
    "psilocybe-genus-classification": "fungal-ecology",
    "psilocybe-global-biogeography": "fungal-ecology",
    "psilocybe-mexicana-profile": "fungal-ecology",
    "psilocybe-natalensis-african-species": "fungal-ecology",
    "psilocybe-section-classification": "fungal-ecology",
    "psilocybe-semilanceata-eight-indole-compounds": "fungal-ecology",
    "psilocybe-semilanceata-profile": "fungal-ecology",
    "psilocybe-stuntzii-profile": "fungal-ecology",
    "psilocybe-tampanensis-profile": "fungal-ecology",
    "psilocybian-species-cultivation-parameters": "mushroom-cultivation",
    "think-grow-model-h-plus": "fungal-ecology",
    "trees-and-the-water-cycle": "gardening",
    "triptolemus-eumolpus-and-the-founding-families-of-eleusis": "psychedelics",
    "tropisms-psilocybe-cubensis-gravitropism": "fungal-ecology",
    "tropisms-psilocybe-cubensis-phototropism": "fungal-ecology",
    "water-soluble-calcium-phosphate-wcp": "mushroom-cultivation",
    "water-soluble-calcium-wca": "mushroom-cultivation",
    "zone-sector-analysis-guide": "permaculture",
    # Coleman (Eliot Coleman, four-season farming)
    "coleman-cold-hardiness-testing-ratings": "gardening",
    "coleman-cold-hardy-varieties": "gardening",
    "coleman-deep-organic-farming": "gardening",
    "coleman-four-season-farm": "gardening",
    "coleman-french-intensive-bed-method": "gardening",
    "coleman-marketing-economics": "gardening",
    "coleman-pest-management": "gardening",
    "coleman-protected-cultivation": "gardening",
    "coleman-tools-small-farm": "gardening",
    "coleman-winter-greens": "gardening",
    "coleman-winter-greens-variety-selection": "gardening",
    "coleman-year-round-marketing-calendar": "gardening",
    # Savory (Allan Savory, holistic management)
    "savory-animal-days-and-forage-measurement": "natural-farming",
    "savory-animal-impact-and-herd-effect": "natural-farming",
    "savory-brittle-environments": "natural-farming",
    "savory-brittleness-scale": "natural-farming",
    "savory-cause-and-effect-guideline": "natural-farming",
    "savory-drought-planning-and-reserves": "natural-farming",
    "savory-ecosystem-foundation-blocks": "natural-farming",
    "savory-erosion-and-land-deterioration": "natural-farming",
    "savory-fire-as-management-tool": "natural-farming",
    "savory-flexibility-in-management": "natural-farming",
    "savory-holistic-decision-making": "natural-farming",
    "savory-holistic-goal-definition": "natural-farming",
    "savory-holistic-management-overview": "natural-farming",
    "savory-land-monitoring": "natural-farming",
    "savory-land-planning-and-grazing-cell-design": "natural-farming",
    "savory-mineral-cycle-management": "natural-farming",
    "savory-non-brittle-environments": "natural-farming",
    "savory-overgrazing-vs-overrest": "natural-farming",
    "savory-predator-prey-and-herding-behavior": "natural-farming",
    "savory-ranch-financial-planning": "natural-farming",
    "savory-recovery-and-grazing-periods": "natural-farming",
    "savory-reductionist-vs-holistic-science": "natural-farming",
    "savory-rest-as-management-tool": "natural-farming",
    "savory-society-and-culture-guideline": "natural-farming",
    "savory-stock-density-vs-stocking-rate": "natural-farming",
    "savory-testing-and-management-guidelines": "natural-farming",
    "savory-water-cycle-management": "natural-farming",
    "savory-weak-link-analysis": "natural-farming",
    # Shroom cultural history
    "shroom-counterculture": "psychedelics",
    "shroom-european-folklore": "psychedelics",
    "shroom-mazatec-tradition": "psychedelics",
    "shroom-mesoamerican-civilization": "psychedelics",
    "shroom-prohibition": "psychedelics",
    "shroom-scientific-study": "psychedelics",
    # Tompkins (Peter Tompkins, alternative agriculture)
    "tompkins-albert-abrams-electronic-diagnosis": "permaculture",
    "tompkins-hieronymus-eloptic-energy": "permaculture",
    "tompkins-lakhovsky-multi-wave-oscillator": "permaculture",
    "tompkins-luther-burbank-intuitive-breeding": "permaculture",
    "tompkins-radionic-agriculture-pesticides": "permaculture",
    # Jeavons (John Jeavons, Grow Biointensive)
    "jeavons-beneficial-herbs-nutrition": "gardening",
    "jeavons-calorie-farming": "gardening",
    "jeavons-master-planning-mini-farms": "gardening",
    "jeavons-surface-cultivation-technique": "gardening",
    "jeavons-watering-technique": "gardening",
    # Fungal ecology misc
    "aspergillus-fumigatus-population-genetics": "fungal-ecology",
    "candida-albicans-molecular-epidemiology": "fungal-ecology",
    "coccidioides-species-complex-biogeography": "fungal-ecology",
    "compartmented-in-vitro-systems-am-transport": "fungal-ecology",
    "dighton-aquatic-hyphomycete-conidia-community-dynamics": "fungal-ecology",
    "dighton-fungus-cultivation-ants-termites-bark-beetles": "fungal-ecology",
    "downy-mildew-biology-diversity-peronosporales": "fungal-ecology",
    "helotiales-inoperculate-discomycete-diversity-ecology": "fungal-ecology",
    "proteomics-early-am-symbiosis-stages": "fungal-ecology",
    "psilocybe-cubensis-strains-names-and-marketing": "psychedelics",
    "psilocybe-subaeruginosa-australia": "fungal-ecology",
    "arbuscule-isolation-metabolic-activity-assays": "fungal-ecology",
    "ingham-leaf-surface-biology-exudates": "fungal-ecology",
    # Psychedelics misc
    "eleusis-mysteries-overview": "psychedelics",
    "harner-cashaahua-banisteriopsis": "psychedelics",
    "sam-stein-psilocybe-cubensis-bad-trip-1961": "psychedelics",
    "schultes-henbane-hyoscyamus-oracle-delphi": "psychedelics",
    "schultes-psilocybe-little-flowers-gods": "psychedelics",
    # Mushroom cultivation misc
    "cotter-cultivation-troubleshooting": "mushroom-cultivation",
    "cotter-culture-storage-senescence": "mushroom-cultivation",
    "cotter-laboratory-setup": "mushroom-cultivation",
    "cotter-log-stump-cultivation": "mushroom-cultivation",
    "cotter-wood-chip-cultivation-outdoor-beds": "mushroom-cultivation",
    # Gardening misc
    "reading-the-landscape": "permaculture",
    "green-grow-room-environment": "cannabis",
    # Ultra-low-cost farming
    "ultra-low-cost-farming-overview": "natural-farming",
    "ultra-low-cost-integrated-farming": "natural-farming",
    "ultra-low-cost-pest-control": "natural-farming",
    "ultra-low-cost-tools-equipment": "natural-farming",
    # 2026-04-27 new pages
    "arid-landscape-scarp-wadi-desert-settlement": "permaculture",
    "coleman-direct-marketing-and-csa-models": "gardening",
    "coleman-small-farm-equipment-and-tools": "gardening",
    "greg-green-container-and-pot-sizing": "cannabis",
    "greg-green-hermaphrodites-and-sex-problems": "cannabis",
    "greg-green-odor-control-and-air-filtration": "cannabis",
    "greg-green-spider-mites-and-common-pests": "cannabis",
    "greg-green-temperature-and-humidity-control": "cannabis",
    "greg-green-water-quality-and-hard-water": "cannabis",
    "honey-locust-pod-fodder-timber-production": "gardening",
    "psilocybe-ovoideocystidiata-species-profile": "fungal-ecology",
    "psilocybe-weilii-species-profile": "fungal-ecology",
    "savory-belief-systems-and-paradigm-shifts": "natural-farming",
    "savory-community-organization-and-shared-grazing": "natural-farming",
    "savory-conventional-vs-holistic-range-management": "natural-farming",
    "savory-four-missing-keys": "natural-farming",
    "savory-grazing-mechanics-and-root-sacrifice": "natural-farming",
    "savory-herd-composition-and-culling-strategies": "natural-farming",
    "savory-human-creativity-in-resource-management": "natural-farming",
    "savory-living-organisms-as-tools": "natural-farming",
    "savory-partial-rest-and-algal-crusts": "natural-farming",
    "savory-poor-land-syndrome": "natural-farming",
    "savory-replanning-and-monitoring-feedback": "natural-farming",
    "savory-short-duration-grazing-and-cell-systems": "natural-farming",
    "savory-supplemental-feeding-and-winter-management": "natural-farming",
    "savory-technology-as-management-tool": "natural-farming",
    "savory-time-and-timing-guideline": "natural-farming",
    "stamets-pinning-initiation-stages-environmental-control": "mushroom-cultivation",
    "urban-water-catchment-cistern-thermal-mass": "permaculture",
    # 2026-04-27第二批新页面
    "bloomfield-gasteromycetes-puffballs-earthstars": "fungal-ecology",
    "stamets-psi-galerina-deadly-look-alikes-safety": "mushroom-cultivation",
    "stamets-psi-psilocybe-baeocystis-knobby-tops": "fungal-ecology",
    "stamets-psi-psilocybe-cubensis-species-guide": "fungal-ecology",
    "stamets-psi-psilocybe-cyanescens-species-guide": "fungal-ecology",
    "stamets-psi-psilocybe-mexicana-species-guide": "fungal-ecology",
    "stamets-psi-psilocybe-stuntzii-blue-ringers": "fungal-ecology",
    "tompkins-cleve-backster-primary-perception": "permaculture",
    "ultra-low-cost-foliar-application-methods": "natural-farming",
    "ultra-low-cost-mineral-leaching-and-sea-salt-replenishment": "natural-farming",
    "urban-rooftop-farming-guide": "gardening",
    # 2026-04-27 new pages (third batch)
    "gadd-mineral-transformations-biogeochemistry": "fungal-ecology",
    "savory-biological-pest-control-and-succession": "natural-farming",
    "savory-elephant-culling-and-wildlife-population-policy": "natural-farming",
    "savory-enterprise-overhead-and-gross-profit-analysis": "natural-farming",
    "savory-game-ranching-and-wildlife-conversion": "natural-farming",
    "turner-2cb-erotic-empathogen": "psychedelics",
    # 2026-04-28 new pages
    "bloomfield-potato-blight-phytophthora-infestans": "fungal-ecology",
    "bloomfield-rice-blast-appressorium-mechanics": "fungal-ecology",
    "desert-varnish-and-microbial-metal-oxidation": "bioremediation",
    "lysergic-acid-amide-discovery-in-ololiuhqui": "psychedelics",
    "pholiotina-filaris-profile": "fungal-ecology",
    "powell-omega-point-and-cosmic-evolution": "permaculture",
    "powell-sleeping-dreams-and-waking-dreams": "permaculture",
    "powell-the-other-and-sentient-presence": "permaculture",
    "psilocybe-aztecorum-profile": "fungal-ecology",
    "psilocybe-caerulescens-profile": "fungal-ecology",
    "psilocybe-pelliculosa-profile": "fungal-ecology",
    "psilocybe-quebecensis-profile": "fungal-ecology",
    "savory-holistic-resource-management-animal-impact": "natural-farming",
    "savory-holistic-resource-management-biological-monitoring": "natural-farming",
    "savory-holistic-resource-management-brittle-vs-nonbrittle-environments": "natural-farming",
    "savory-holistic-resource-management-decision-framework": "natural-farming",
    "savory-holistic-resource-management-ecological-succession": "natural-farming",
    "savory-holistic-resource-management-fire-as-tool": "natural-farming",
    "savory-holistic-resource-management-mineral-cycle": "natural-farming",
    "savory-holistic-resource-management-overgrazing": "natural-farming",
    "savory-holistic-resource-management-water-cycle": "natural-farming",
    "tompkins-lawrence-biological-interstellar-communication": "permaculture",
    "volvariella-volvacea-cultivation-guide": "mushroom-cultivation",
    # 2026-04-29 new pages
    "16s-rrna-sequencing-microbiome-analysis": "fungal-ecology",
    "allen-australian-psilocybe-species-comprehensive-guide": "fungal-ecology",
    "allen-pans-cyanescens-australia-distribution": "fungal-ecology",
    "allen-subtropical-australia-hunting-techniques": "mushroom-cultivation",
    "biodiversity-sampling-protocol-design": "permaculture",
    "calcium-accumulators-and-oak-leaves": "soil-and-compost",
    "cellvibrio-and-root-decay-microbiome": "fungal-ecology",
    "dual-chambered-terrarium-design": "mushroom-cultivation",
    "harner-sharanahua-visions-and-cures": "psychedelics",
    "incubation-and-colonization": "mushroom-cultivation",
    "light-basidiocarp-initiation-psilocybe-cubensis-research": "fungal-ecology",
    "oss-oeric-dosage-guidelines-and-potency": "mushroom-cultivation",
    "oss-oeric-equipment-and-materials-list": "mushroom-cultivation",
    "oss-oeric-history-and-impact-underground-classic": "mushroom-cultivation",
    "oss-oeric-legal-disclaimer-and-context": "mushroom-cultivation",
    "oss-oeric-psilocybe-cubensis-strain-guide": "mushroom-cultivation",
    "oss-oeric-rice-cake-tek-methodology": "mushroom-cultivation",
    "oss-oeric-terrarium-design-and-humidity": "mushroom-cultivation",
    "psilocybe-baeocystis-profile": "fungal-ecology",
    "psilocybe-coprophila-profile": "fungal-ecology",
    "psilocybe-genus-overview": "fungal-ecology",
    "psilocybe-samuiensis-profile": "fungal-ecology",
    "psilocybe-southeast-asia-pacific": "fungal-ecology",
    "psilocybe-species-europe": "fungal-ecology",
    "psilocybe-subcubensis-profile": "fungal-ecology",
    "stamets-cultivator-humidity-management-fogging-systems": "mushroom-cultivation",
    "stamets-cultivator-paddy-straw-volvariella-volvacea-cultivation": "mushroom-cultivation",
    "stamets-psylo-dangers-mistaken-identification": "mushroom-cultivation",
    "stamets-psylo-field-collection-techniques": "mushroom-cultivation",
    "stamets-psylo-global-distribution-ecology": "fungal-ecology",
    "stamets-psylo-good-tips-great-trips": "mushroom-cultivation",
    "stamets-psylo-historical-perspective": "mushroom-cultivation",
    "stamets-psylo-identification-macroscopic-microscopic": "fungal-ecology",
    "stamets-psylo-psilocybe-cubensis": "fungal-ecology",
    "stamets-psylo-psilocybe-cyanescens": "fungal-ecology",
    "stamets-psylo-psilocybe-semilanceata": "fungal-ecology",
    "stamets-psylo-six-classic-habitats": "fungal-ecology",
    "ultra-low-water-softening-for-pesticide-efficacy": "natural-farming",
    "stamets-psylo-psilocybe-stuntzii": "fungal-ecology",
    # 2026-04-29 new pages (batch 2)
    "22s-23s-homobrassinolide-chemistry-and-synthesis": "fungal-ecology",
    "catalytic-hydrogenolysis-palladium-carbon-debenzylation": "fungal-ecology",
    "gadd-aspergillus-fumigatus-glucan-virulence": "fungal-ecology",
    "gadd-penicillium-marneffei-population-genetics": "fungal-ecology",
    "light-wavelength-basidiocarp-initiation-psilocybe-cubensis-badham": "fungal-ecology",
    "primary-metabolic-precursors-to-the-shikimate-pathway": "fungal-ecology",
    "psilocin-synthesis-4-hydroxyindole-to-psilocin": "mushroom-cultivation",
    "psilocybe-mexicana-cultivation": "mushroom-cultivation",
    "psilocybe-tampanensis-cultivation": "mushroom-cultivation",
    "zwitterionic-n-o-dibenzyl-phosphate-intermediate": "fungal-ecology",
    # 2026-04-30 new pages
    "banco-sumiruna-muraya": "psychedelics",
    "culebra-borrachera-methysticodendron-amesianum": "psychedelics",
    "ghouled-field-guide-historical-context": "psychedelics",
    "icaros-power-songs": "psychedelics",
    "mariri-phantom-sorcery": "psychedelics",
    "taique-desfontainia-hookeri-andean-shrub": "psychedelics",
    "creatively-use-and-respond-to-change": "permaculture",
    "design-from-patterns-to-details": "permaculture",
    "integrate-rather-than-segregate": "permaculture",
    "use-and-value-renewable-resources": "permaculture",
    "use-edges-and-value-the-marginal": "permaculture",
    "use-small-and-slow-solutions": "permaculture",
    "natives-vs-exotics": "permaculture",
    "zone-system": "permaculture",
    "water-conservation": "permaculture",
    "ingham-dissolved-oxygen-management": "fungal-ecology",
    "ingham-single-species-vs-whole-community": "fungal-ecology",
    "ingham-sticker-spreader-surfactants": "fungal-ecology",
    "motivational-sessions-trainees": "natural-farming",
}
for name, topic in manual.items():
    if name in page_topics: continue
    page_topics[name] = topic

unassigned = [n for n in all_pages if n not in page_topics]
if unassigned:
    print(f"WARNING: {len(unassigned)} unassigned pages:")
    for u in sorted(unassigned):
        print(f"  {u}")

# Topic titles and descriptions
topic_meta = {
    "fungal-ecology": ("Fungal Ecology & Biology", "Mycology, fungal biology, symbiosis, ecology, soil food web, and fungal diversity"),
    "mushroom-cultivation": ("Mushroom Cultivation", "Growing mushrooms, substrates, sterile technique, species-specific guides, and commercial production"),
    "psychedelics": ("Psychedelics & Entheogens", "Psychedelic compounds, consciousness research, ethnobotany, cultural history, and therapeutic applications"),
    "permaculture": ("Permaculture & Ecological Design", "Permaculture principles, ecological design, water management, community resilience, and bioregional organization"),
    "natural-farming": ("Natural Farming", "Fukuoka's natural farming, Korean Natural Farming (KNF), JADAM, and no-till methods"),
    "cannabis": ("Cannabis", "Cannabis cultivation, genetics, breeding, processing, and medical applications"),
    "soil-and-compost": ("Soil & Compost", "Soil science, composting, compost tea, mineral management, and the soil food web"),
    "gardening": ("Gardening & Growing", "Vegetable gardening, orcharding, food preservation, irrigation, season extension, and homesteading skills"),
    "bioremediation": ("Bioremediation & Restoration", "Environmental cleanup, mycoremediation, phytoremediation, land restoration, and pollution treatment"),
    "herbalism": ("Herbalism & Plant Medicine", "Medicinal plants, herbal preparations, functional mushrooms, and traditional plant medicine"),
    "homesteading": ("Homesteading & Self-Reliance", "Animal husbandry, food preservation, natural building, energy systems, and emergency preparedness"),
    "brewing": ("Brewing & Fermentation", "Fermented foods, beverages, probiotics, and traditional fermentation methods"),
    "species": ("Species Profiles", "Individual species entries from PIHKAL, TIHKAL, and taxonomic references"),
    "comparisons-queries": ("Comparisons & Queries", "Side-by-side comparisons and query-based analysis pages"),
}

# Group pages by topic
topic_pages = defaultdict(list)
for name, topic in page_topics.items():
    topic_pages[topic].append(name)

# Print counts
print("\nTopic distribution:")
for topic in sorted(topic_pages.keys()):
    print(f"  {topic}: {len(topic_pages[topic])}")

# Write index files
index_dir = wiki
os.makedirs(index_dir, exist_ok=True)

for topic, pages in topic_pages.items():
    pages.sort()
    alpha_groups = defaultdict(list)
    for p in pages:
        letter = p[0].upper() if p[0].isalpha() else "#"
        alpha_groups[letter].append(p)

    title, desc = topic_meta.get(topic, (topic.title(), ""))
    lines = [f"# {title}", "", f"> {desc}", "", f"**{len(pages)} pages**", ""]
    for letter in sorted(alpha_groups.keys()):
        lines.append(f"## {letter}")
        lines.append("")
        for p in alpha_groups[letter]:
            lines.append(f"- [[{p}]]")
        lines.append("")

    filepath = os.path.join(index_dir, f"index-{topic}.md")
    with open(filepath, "w") as f:
        f.write("\n".join(lines))
    print(f"  Wrote {filepath} ({len(pages)} pages)")

# Build index-all.md
alpha_all = defaultdict(list)
for p in sorted(all_pages):
    letter = p[0].upper() if p[0].isalpha() else "#"
    alpha_all[letter].append(p)

lines = ["# Complete Page Index", "", f"> All {len(all_pages)} pages in the wiki, alphabetically.", ""]
for letter in sorted(alpha_all.keys()):
    lines.append(f"## {letter}")
    lines.append("")
    for p in alpha_all[letter]:
        lines.append(f"- [[{p}]]")
    lines.append("")

with open(os.path.join(wiki, "index-all.md"), "w") as f:
    f.write("\n".join(lines))
print(f"  Wrote index-all.md ({len(all_pages)} pages)")

# Build index.md (hub)
tc = Counter(page_topics.values())
lines = ["# LLM Wiki", "", "> A comprehensive knowledge base covering mycology, mushroom cultivation, psychedelics, permaculture, natural farming, cannabis, soil science, herbalism, bioremediation, and homesteading.", "", f"**{len(all_pages)} pages** across {len(topic_pages)} categories", ""]
lines.append("## Categories")
lines.append("")
for topic in ["fungal-ecology", "mushroom-cultivation", "psychedelics", "permaculture", "natural-farming", "cannabis", "soil-and-compost", "gardening", "bioremediation", "herbalism", "homesteading", "brewing", "species", "comparisons-queries"]:
    title, _ = topic_meta[topic]
    count = tc.get(topic, 0)
    lines.append(f"- [[index-{topic}|{title}]] ({count} pages)")
lines.append("")
lines.append("## Complete Index")
lines.append("")
lines.append("- [[index-all|All Pages A-Z]]")
lines.append("")

with open(os.path.join(wiki, "index.md"), "w") as f:
    f.write("\n".join(lines))
print("  Wrote index.md")

print(f"\nDone! {len(all_pages)} pages indexed into {len(topic_pages)} categories.")
if unassigned:
    print(f"WARNING: {len(unassigned)} pages remain unassigned!")
