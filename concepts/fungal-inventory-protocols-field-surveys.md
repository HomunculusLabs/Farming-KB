---
title: Fungal Inventory Protocols for Field Surveys
aliases: [mycological survey, [[fungal-sampling-methods]], [[fungal-ecological-operational-groups-biodiversity-inventory]], mushroom survey protocol]
tags: [mycology, field-methods, survey-protocol, biodiversity, inventory, ecology]
source: biodiversity-of-fungi.md
created: 2026-05-11
---

# Fungal Inventory Protocols for Field Surveys

## Overview

Standardized fungal inventory protocols are essential for making meaningful comparisons between sites and tracking changes in fungal biodiversity over time. As emphasized in *[[biodiversity-of-fungi-biodiversity-patterns-ecosystems]]* (Mueller, Bills, and Foster), the absence of broadly accepted standard methods has been one of the greatest obstacles to progress in fungal ecology and conservation. Different fungal groups require fundamentally different sampling approaches, which is why the volume is organized by methodology rather than taxonomy.

## Planning a Fungal Inventory

### Site Selection and Delineation

Define the inventory area using ecologically meaningful boundaries (watershed, vegetation type, elevation band) rather than arbitrary political boundaries. Document the following site characteristics:

- **Location**: GPS coordinates, elevation, aspect, slope
- **Climate**: Mean annual temperature and precipitation, seasonal patterns
- **Vegetation**: Dominant plant species, community type, successional stage, canopy cover
- **Soil**: Type, pH, texture, organic matter content, moisture regime
- **Disturbance history**: Logging, fire, grazing, agriculture, pollution

### Temporal Design

No single visit can capture the full fungal diversity of a site. The minimum survey design recommended in the volume includes:

- **Multiple years**: At least 3–5 years to account for inter-annual variation in fruiting patterns. Some species may not appear every year.
- **Seasonal coverage**: In [[oyster-mushroom-log-cultivation-temperate-regions-short-log-method]], sample at least during spring (April–June), summer (July–September), and fall (October–November). Winter sampling detects cold-weather specialists.
- **Weather-dependent scheduling**: The most productive surveys occur 3–10 days after significant rainfall during warm weather. Schedule flexibly to capture these windows.
- **Repeated visits**: A minimum of 4–6 visits per year, timed to follow rain events during the growing season.

## Macrofungal Survey Methods

### Plot-Based Surveys

Systematic surveys within permanent plots provide quantitative, comparable data:

**Plot design**:
- Circular or rectangular plots, typically 100–1,000 m² depending on forest type and expected fungal density
- A minimum of 5–10 plots per site, stratified by habitat type (elevation, vegetation, moisture)
- Permanent markers allow resurvey of the same plots over time
- Record all fungal fruiting bodies within the plot boundary

**Collection protocol**:
1. Search the plot systematically, working from one edge to the other in parallel transects spaced 1–2 meters apart
2. Record each collection with a unique field number, GPS coordinates, substrate, and associated plant species
3. Photograph each specimen in situ before collection, including scale reference
4. Collect the entire fruiting body if possible, including the base/stipe base (critical for identification)
5. For large specimens, collect a cross-section including cap, gills/pores, stipe, and base
6. Wrap specimens individually in wax paper or aluminum foil (never plastic bags, which promote decay and condensation)
7. Label immediately with collection number, date, collector, and location

### Transect Surveys

Walking transects of defined length through representative habitat complement plot-based surveys. Standardize effort (person-hours per km), record all species observed, and use time-constrained searches (e.g., 60 minutes per transect) to compare species accumulation rates. Particularly useful for rapid biodiversity assessments and detecting rare species outside permanent plots.

### All-Species Lists

Maintain a cumulative species list for the inventory area combining all methods and seasons. Track over time to document new additions and estimate total richness using accumulation curves.

## Microfungal Sampling Methods

### Soil Fungi

Soil harbors the greatest fungal diversity. Methods include: composite soil cores (5–10 cores per sample, 2.5 cm × 10 cm depth), soil sieving (250 μm sieve with sucrose flotation for propagules), baiting with selective substrates (sterilized seeds, cellulose filters), and root washing to isolate mycorrhizal and endophytic fungi.

### Foliar Fungi

Methods for leaf surface (phyllosphere) and leaf interior (endophyte) fungi: leaf washing with surfactant and plating dilutions, [[challenge-microorganisms-microwave-surface-sterilization]] with ethanol/hypochlorite followed by tissue plating for endophytes, leaf imprint directly onto agar, and direct microscopy of cleared leaf tissue.

### Wood-Inhabiting Fungi

Moist chamber incubation of wood samples (4–12 weeks), baiting with sterilized wood strips placed in the field for 2–6 months, and direct field examination of dead wood and stumps for ascomycete and basidiomycete fruiting bodies. Record substrate species, decay stage, and orientation.

## Specimen Processing and Preservation

### Drying

Rapid drying is critical to preserve specimens for DNA extraction and morphological study:

- Use a food dehydrator set to 35–40°C (never above 45°C, which destroys DNA and alters morphology)
- Alternatively, use silica gel desiccant in sealed containers for small specimens
- Drying should be completed within 24–48 hours of collection
- Target moisture content: <10% of fresh weight

### Voucher Specimens

Every collection should produce a voucher specimen deposited in a recognized herbarium:

- Label with complete collection data: species name (if determined), collector, collection number, date, location (GPS), habitat, substrate, associated organisms, descriptive notes
- Include duplicates for exchange with other herbaria
- For DNA work, subsample before or immediately after drying, placing tissue in CTAB buffer or directly into 95% ethanol
- Photograph the dried specimen as a supplement to the field photo

## Data Management

### Field Data Standards

Record the following for every collection:

- Unique collection number (sequential, never reused)
- Date and time of collection
- Collector name(s)
- GPS coordinates (datum specified)
- Elevation, aspect, slope
- Habitat description (vegetation type, dominant plants)
- Substrate (soil, wood species, leaf species, dung, etc.)
- Decay stage (for wood-inhabiting fungi)
- Abundance estimate (number of fruiting bodies, area covered)
- Associated organisms (insects on fungi, parasitic fungi, etc.)
- Weather conditions at time of collection

### Database Management

Use a relational database designed for biological collections (Specify, Symbiota, or similar) to manage collection data. Key principles:

- Follow Darwin Core standards for data fields to ensure interoperability
- Back up data regularly in at least two separate locations
- Link specimen records to DNA sequence data (GenBank accession numbers)
- Link to photographs for visual reference
- Make data publicly accessible through online portals (MyCoPortal, iNaturalist, MushroomObserver)

## Quality Assurance

### Identification Verification

- Have all identifications reviewed by a specialist for the relevant fungal group
- Deposit problematic specimens in a reference herbarium for future re-examination
- Sequence the ITS barcode region for all specimens to provide a molecular reference independent of morphological identification
- Compare sequences against curated reference databases (UNITE for fungi) to verify identifications

### Estimating Completeness

Use species accumulation curves to estimate how complete the inventory is:

- Plot cumulative species count against sampling effort (number of visits, person-hours, number of plots)
- If the curve is still rising steeply, the inventory is incomplete and more sampling is needed
- If the curve approaches an asymptote, the inventory has captured the majority of species present
- Use non-parametric estimators (Chao1, ACE, Jackknife) to extrapolate total species richness from the observed data

## See Also

- estimating fungal biodiversity methods — Overview of diversity estimation approaches
- mycorrhizal fungi ecosystem function — Belowground fungal inventory challenges
- [[endophytic-fungi-plant-interactions]] — Specialized protocols for [[bacterial-endophyte-isolation-detection-plant-roots]]
