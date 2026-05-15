---
title: Core Specimen Data Structure for Mycological Databases
source: unknown-biodiversity-of-fungi.md
type: concept
---

# Core Specimen Data Structure for Mycological Databases

Standardized specimen data structures are essential for building interoperable mycological databases. A well-defined core data structure ensures that fungal collection records can be shared, compared, and aggregated across institutions, supporting both taxonomic research and biodiversity assessments.

Without such standardization, data from different herbaria and research groups remain siloed, hampering large-scale analyses of fungal distribution, ecology, and conservation status. The structure outlined below represents a comprehensive framework for capturing the critical information associated with each fungal specimen.

It balances completeness with practicality, defining a set of core fields that every mycological database should implement while leaving room for institution-specific extensions. This framework is particularly relevant in the context of digitizing historical fungal collections, where standardizing legacy data against a common schema is a prerequisite for meaningful data aggregation.

## Taxonomic Name Fields

Accurate taxonomic identification is the cornerstone of any specimen record. The core fields capture the full hierarchical name of the fungus, from genus through infraspecific epithet:

- **Genus** (size 26, required): The generic name of the fungus. This is a mandatory field — every specimen record must have a genus-level determination at minimum. The field size of 26 characters accommodates the vast majority of fungal generic names.

- **Species** (size 32): The specific epithet. May be left blank if the specimen has only been identified to genus level, though species-level identification is strongly encouraged. The 32-character limit handles most epithets including compound or lengthy descriptive names.

- **Rank**: Infraspecific rank designations such as *var.* (variety), *f.* (forma), *subsp.* (subspecies), and related terms. This field qualifies the relationship between the species epithet and the subspecific epithet, ensuring the full trinomial name can be reconstructed.

- **Subspecific Epithet** (size 32): The third-level name component when an infraspecific rank applies. Only used in conjunction with the Rank field; left empty for specimens identified only to species level.

- **Author** (size 100): The author citation for the name, following the Brummitt and Powell (1992) standard. Author citations are critical for disambiguating homonyms and tracking nomenclatural changes. When more than two authors are associated with a name, "et al." is used in accordance with the International Code of Botanical Nomenclature (ICBN).

- **Determiner**: The person who identified the specimen. Recording the determiner separately from the collector allows tracking of taxonomic expertise and facilitates verification of identifications.

- **Determine Date**: The date on which the determination was made. This is important for understanding the taxonomic framework in effect at the time of identification, especially for historically collected specimens that may have been redetermined as classification systems evolved.

## Locality Data Fields

Geographic provenance is critical for distribution studies, ecological modeling, and conservation assessments. Locality fields are structured hierarchically, moving from broad administrative units to precise site descriptions:

- **Country** (required): The country of collection. The value "unknown" is used when the country cannot be determined — this field should never be left blank. This requirement ensures that all records can be geographically referenced at a minimum level.

- **Country Subdivision1**: The first-level administrative division (e.g., state or province). For United States records, standard two-letter postal codes are recommended for consistency and ease of processing.

- **Country Subdivision2**: The second-level administrative division, typically county or parish. Together with the higher-level fields, this creates a three-tier administrative hierarchy suitable for mapping at regional scales.

- **Country Place Name**: The named geographic feature or settlement nearest to the collection site (e.g., "Yellowstone National Park" or "Springfield").

- **Locality** (size 250): A free-text description of the specific collection site, providing ecological and geographic context beyond the administrative hierarchy. This might include distance and direction from landmarks, trail names, or microhabitat descriptions.

- **Elevation1 / Elevation2**: Numeric elevation values representing a range (minimum and maximum). Zero represents sea level; negative values indicate elevations below sea level (e.g., coastal or subterranean collections).

- **Elevation Source**: The method or reference used to determine the elevation (e.g., altimeter, topographic map, GPS).

- **Elevation Unit**: Either feet (f) or meters (m). Standardizing on one unit across a database is recommended, with meters preferred for international interoperability.

- **Latitude / Longitude**: Expressed in decimal degrees, with north latitude and east longitude as positive values, and south latitude and west longitude as negative values. This signed-decimal convention avoids ambiguity inherent in degree-minute-second formats and N/S/E/W text labels.

- **LatLon Source**: The method used to obtain coordinates — options include GPS (most precise), map (interpolated from cartographic sources), estimate (approximate), or gazetteer (derived from named place databases).

## Collection Details

These fields document the circumstances and personnel involved in the collection event itself:

- **Collector**: Recorded in "Last, First" name format for consistent sorting and indexing. This format facilitates automated parsing and database searching by family name.

- **Team Collectors**: Additional collectors listed in semicolon-separated format. When more than three team members are present, "et al." is appended after the first three names (e.g., "Smith, J.; Jones, A.; Brown, K.; et al.").

- **Collector Number**: The unique field number assigned by the collector. This number links the physical specimen to the collector's field notes and is often the primary way collectors reference their collections in publications and correspondence.

- **Submitter**: The person who submitted the record to the database. This may differ from the collector when records are entered by herbarium staff, data managers, or citizen scientists.

- **Collector Date**: The date of collection, formatted as either YYYYMMDD or YYYY-MM-DD following the ANSI standard. Consistent date formatting is essential for chronological queries and phenological analyses of fruiting patterns.

- **Season**: The seasonal context of the collection (e.g., spring, summer, autumn, winter). Particularly useful for fungi, whose fruiting is often strongly seasonal and climate-dependent.

## Substratum and Habitat

Ecological context links the specimen to its environment and is vital for niche studies and ecological modeling:

- **Substratum** (required): The substrate on which the fungus was found (e.g., wood, soil, leaf litter, dung, living plant tissue). Like Country, this field uses "unknown" when information is unavailable rather than being left empty. Substratum data is especially important for saprotrophic and lignicolous fungi.

- **Habitat** (size 250): A descriptive characterization of the broader environment, including vegetation type, moisture conditions, and associated ecological features. For example: "mixed oak-pine forest on north-facing slope near stream."

## Host Information

For parasitic, pathogenic, or symbiotic fungi, host data is essential. The host fields mirror the taxonomic name structure, providing the same level of botanical precision for the host organism:

- **Host Genus**: The genus of the host organism.

- **Host Genus Hybrid**: Denoted with a lowercase × (multiplication sign) to indicate hybrid origin, following standard botanical conventions.

- **Host Species**: The species of the host.

- **Host Species Hybrid**: Hybrid notation at the species level, again using the lowercase × character.

- **Host Rank**: Infraspecific rank of the host (e.g., *var.*, *subsp.*).

- **Host Subspecific Epithet**: The infraspecific name of the host.

- **Host Common Name**: The vernacular name of the host organism, providing accessibility for non-specialist users and supporting cross-disciplinary research (e.g., plant pathology and forestry).

## Housekeeping Fields

Administrative fields ensure institutional accountability and record traceability across the global network of fungal collections:

- **Herbarium Number**: The accession number assigned to the specimen, incorporating Index Herbariorum codes to ensure uniqueness across institutions. Each herbarium's code (e.g., NY for New York Botanical Garden, K for Royal Botanic Gardens, Kew) is globally recognized. The combined code and number (e.g., "NY12345") constitutes a universally unique identifier for the specimen.

## Additional Fields

Supplementary fields capture specialized information that, while not universal to every record, is critical for certain research applications:

- **Type Status**: Indicates whether the specimen serves as a nomenclatural type, using standard abbreviations such as HO (holotype), IS (isotype), PT (paratype), and others. Type specimens carry special taxonomic significance under the codes of nomenclature and require careful documentation and long-term preservation.

- **Culture Status**: Whether a living culture of the fungus has been preserved. Living cultures are essential for phylogenetic studies (especially DNA sequencing), physiological experiments, and biochemical characterization.

For type status and culture data, a **relational table approach** is recommended rather than embedding multiple values in a single delimited field. This design allows a single specimen to be associated with multiple type designations or multiple culture accessions while maintaining database normalization and referential integrity.

## Importance for Fungal Biodiversity Research

The fungal kingdom is estimated to contain between 2.2 and 3.8 million species, yet only a fraction have been formally described. A standardized core data structure is fundamental to documenting and tracking this unknown biodiversity. When specimen records follow a common schema, researchers can:

- Aggregate distribution data across herbaria to map species ranges and identify biodiversity hotspots.

- Track taxonomic revisions over time by linking historical determinations to current classifications.

- Build ecological databases that correlate fungal occurrences with environmental variables and host distributions.

- Ensure that type specimens — the name-bearing specimens that anchor taxonomic concepts — are discoverable and accessible to the global mycological community.

## Design Principles

Several key principles underlie this data structure and guide its implementation:

1. **Required fields never blank**: Fields marked as required (Genus, Country, Substratum) use explicit placeholder values like "unknown" to prevent silent data gaps that could distort analyses.

2. **Standardized formats**: Author citations follow Brummitt and Powell; dates follow ANSI; coordinates follow decimal-degree conventions with signed values. These standards are chosen to maximize interoperability across institutions and software systems.

3. **Hierarchical geographic data**: Country → subdivision1 → subdivision2 → place name → locality provides scalable geographic precision, from country-level mapping to site-specific descriptions.

4. **Relational integrity**: Complex multi-valued attributes (type status, cultures) are handled through relational tables rather than delimited strings, supporting proper database normalization and preventing data anomalies.

5. **Extensibility**: The core structure provides a foundation that individual databases can extend with institution-specific fields while maintaining interoperability at the essential level. Local extensions should not redefine or conflict with core field semantics.

## See Also

- [[mycorrhiza]]
- [[basidiomycota]]
- [[ascomycota]]
- [[kingdom-fungi]]
- [[mushroom-identification]]
