---
title: Mycological Specimen Data Standards
source: unknown-biodiversity-of-fungi.md
type: concept
---

# Mycological Specimen Data Standards

Mycological specimen data standards define the structure and formatting of information recorded when collecting, preserving, and cataloging fungal specimens. These standards ensure consistency, interoperability, and discoverability across herbaria and biodiversity databases worldwide.

## Core Data Structure

Every fungal specimen record is built around four fundamental questions: **what** was collected, **who** collected it, **when** it was collected, and **where** it was found. These pillars correspond to taxonomic, agent, temporal, and spatial data domains.

A well-structured specimen record ties each of these domains to controlled vocabularies and standardized field formats wherever possible. This reduces ambiguity and enables machine-readable data exchange.

The following sections detail the specific fields within each domain, including their accepted sizes, formats, and whether they are required or optional.

## Taxonomic Name Fields

Taxonomic identification is the central element of any specimen record. The following fields capture the full taxonomic context of the specimen:

- **Genus** — up to 26 characters, text format
- **Species** — up to 32 characters, text format
- **Rank** — up to 6 characters (e.g., "sp.", "var.", "f.")
- **Subspecific Epithet** — up to 32 characters, text format
- **Author** — up to 100 characters (taxonomic author citation)

These fields collectively form the full scientific name of the fungal specimen. The Genus and Species fields are generally **required**, while Rank and Subspecific Epithet are optional.

## Determiner and Determine Date

The **Determiner** field records the name of the person who provided the current taxonomic identification. This may differ from the original collector.

The **Determine Date** captures when the identification was made. It is essential for tracking the currency and authority of a taxonomic assignment.

Multiple determinations may exist for a single specimen over time. Best practice is to retain historical determinations while flagging the current accepted one.

## Locality Data

Precise locality information is critical for biogeographic and ecological analyses. Locality fields follow a hierarchical structure from broad to specific:

1. **Country** — standardized country name or ISO 3166 code
2. **Country Subdivision 1** — state, province, or equivalent
3. **Country Subdivision 2** — county, district, or equivalent
4. **Country Place Name** — nearest named populated place
5. **Locality** — free-text description of the specific collection site

The Country field is **required** in all standards-compliant records. Country Place Name and Locality are strongly recommended to enable precise georeferencing.

## Elevation Fields

Elevation data provides important ecological context for fungal collections. The standard fields are:

- **Elev1** — minimum elevation at the collection site
- **Elev2** — maximum elevation (used for elevation ranges)
- **Elevation Source** — method or instrument used (e.g., "GPS," "topo map," "altimeter")
- **Elevation Unit** — meters above sea level (MASL) is the default standard

Elev1 and Elev2 should be recorded as numeric values. When only a single elevation is known, both fields may contain the same value.

## Coordinate Fields

Geographic coordinates anchor a specimen record to a precise point on the Earth's surface. The primary coordinate fields are:

- **Latitude** — decimal degrees, positive north of the equator
- **Longitude** — decimal degrees, positive east of the Prime Meridian
- **Lat-Long Source** — origin of the coordinate data (e.g., "GPS," "georeferenced from locality description")

Coordinates should be reported in **decimal degrees (WGS 84 datum)** to maximize interoperability with mapping tools and biodiversity platforms. Degrees-minutes-seconds formats should be converted prior to submission.

Coordinate precision and uncertainty should be documented when available. This allows downstream users to assess the reliability of spatial analyses.

## Collection Details

Collection agent and event data answer the "who" and "when" of specimen acquisition. These fields include:

- **Collector** — primary person who collected the specimen
- **Team Collectors** — additional team members involved in the collection event
- **Collector Number** — unique identifier assigned by the collector in the field
- **Submitter** — person or institution submitting the record to a database
- **Collector Date1** — start date of the collection event
- **Collector Date2** — end date (for multi-day collecting trips)
- **Season** — general seasonal descriptor (e.g., "autumn," "monsoon")

The Collector and Collector Date1 fields are **required**. Collector Number is highly recommended as it links field notes and physical specimens.

Dates should follow the **ISO 8601 standard** (YYYY-MM-DD) for unambiguous international use.

## Substratum and Habitat

Fungal ecology is closely tied to the substrate on which a specimen was found and the broader habitat type. Two fields capture this information:

- **Substratum** — the specific material the fungus was growing on (e.g., "decaying hardwood," "soil," "living leaf")
- **Habitat** — the broader ecological context (e.g., "tropical montane forest," "grassland")

Both fields use free text but are ideally drawn from **controlled vocabularies** to facilitate search and analysis. Substratum is particularly important for saprotrophic and pathogenic fungi.

## Host Fields

For fungi associated with a host organism (pathogens, parasites, and some mutualists), detailed host data is recorded:

- **Host Genus** — genus of the host organism
- **Host Species** — species of the host organism
- **Host Rank** — taxonomic rank of the host identification
- **Host Subspecific Epithet** — infraspecific epithet of the host
- **Host Common Name** — vernacular name of the host
- **Hybrid Indicator** — flags whether the host is a known hybrid

Host fields follow the same character limits as the corresponding fungal taxonomic fields. These data are essential for plant pathology and host-specificity studies.

## Herbarium Number

The **Herbarium Number** links a specimen record to its physical voucher in a herbarium collection. It follows the **Index Herbariorium** coding system, which assigns internationally recognized abbreviations to registered herbaria.

The format typically combines the herbarium code with a unique accession number (e.g., "NY 01234567" for the New York Botanical Garden). Index Herbariorium codes are maintained by the International Association for Plant Taxonomy (IAPT).

This field is **required** for any specimen deposited in a registered herbarium. It enables unambiguous cross-referencing between digital records and physical collections.

## Type Status and Culture Indicators

Two additional flags provide important metadata about the significance and availability of a specimen:

- **Type Status** — indicates whether the specimen serves as a nomenclatural type (e.g., "holotype," "isotype," "paratype," "neotype," "epitype")
- **Culture** — indicates whether a living culture of the fungus has been preserved (e.g., in a culture collection such as ATCC or CBS)

Type specimens carry special nomenclatural significance under the **International Code of Nomenclature for algae, fungi, and plants (ICN)**. They must be designated from physical specimens deposited in a registered herbarium.

Living cultures are critical for genetic and physiological studies. When available, the culture accession number should also be recorded.

## Standards References

Mycological specimen data standards draw from and align with several major international frameworks:

1. **Darwin Core** — a biodiversity informatics standard maintained by Biodiversity Information Standards (TDWG)
2. **ABCD Schema** — Access to Biological Collection Data, an XML-based schema
3. **Index Herbariorum** — the global registry of herbaria and their codes
4. **ICN (Melbourne Code)** — the governing nomenclatural code for fungi
5. **ISO 8601** — date and time representation standard
6. **ISO 3166** — country and subdivision codes

Darwin Core terms map directly to many of the fields described above, facilitating data exchange through platforms like GBIF, iDigBio, and MycoPortal.

## See Also

- [[mycology]]
- [[fungal-taxonomy]]
- [[biodiversity-database-design-fields-tables]]
- [[database-design-fungal-specimens]]
- [[spore]]
