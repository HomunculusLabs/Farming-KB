---
title: "Fungal Database and Specimen Data Management"
source: "[[biodiversity-of-fungi-biodiversity-patterns-ecosystems]] (Mueller, Bills, Foster)"
source_key: "unknown-biodiversity-of-fungi.md"
topics: [[mycology]], database-design, specimen-data, biodiversity-informatics, data-management]
aliases: [fungal databases, specimen management, [[fungal-biodiversity-data-analysis]], mycological informatics]
---

# Fungal Database and Specimen Data Management

## Overview

Effective management of [[biodiversity-fungal-biodiversity-estimation-methods]] data is essential for inventory,
monitoring, and comparative studies. Modern database software enables
researchers to design applications that serve both personal research needs and
the broader biodiversity community. A well-designed [[fungal-specimen-collection-herbarium-management]] database
supports data maintenance throughout a scientific career and facilitates data
exchange with institutional and international biodiversity resources.

## Database Design Principles

### Fields and Tables

Database design proceeds from the top down:

1. **Define the purpose** of the database
2. **Identify fields** (the smallest logical data units)
3. **Group fields into tables** that pertain to the same subject
4. **Establish relationships** between tables using shared data elements

**Rules for fields:**
- Data in each field should describe the subject of its table
- Break data into the smallest logical units (e.g., separate genus, species,
  author fields rather than one combined name field)
- Check field definitions against field notes and reports for completeness

**Rules for tables:**
- Include only fields pertaining to the same subject
- Tables should not contain fields left blank in many records — those belong in
  a separate table
- Different tables should not duplicate data except as needed to establish
  relationships
### Table Relationships

Two tables must share a data element of the same data type to be related.
Relational database software for personal computers is now widely available and
makes it straightforward to join tables and produce reports combining data from
multiple sources.

**Recursive relationships** are useful for nomenclatural databases where a table
relates to itself. A name table containing an ID, the name text, and a synonym
field (referencing another record in the same table) can list accepted names
alone, accepted names with synonyms, or only synonyms. A SynonymType field with
values such as "b" (basionym), "o" (obligate synonym), and "t" (taxonomic) can
control sorting in standard publication order.

### Authority Tables

Authority (lookup) tables verify data entry against standardized lists. A
geographic authority table listing all valid state or province names ensures
that only legitimate values are entered for locality fields. Generic names,
author names, and place names are obvious candidates for authority tables.

Authority tables can be obtained from colleagues or built from standard
references. On any long-term project, they significantly increase data entry
efficiency and consistency. It is difficult to overstate their importance.

## Core Data Structure for Fungal Specimens

The following field structure is recommended as a basic exchange format for
mycological specimen records:

### Taxonomic Name Fields
- **Genus** (26 chars, text, required) — Standard: Index of Fungi
- **Species** (32 chars, text) — Standard: Index of Fungi
- **Rank** (6 chars, text) — var., f., subsp., subsp., etc.
- **Subspecific Epithet** (32 chars, text)
- **Author** (100 chars, text) — Author at lowest rank; "et al." for multiple
  authors per International Code of Botanical Nomenclature

### Determiner Fields
- **Determiner** (55 chars, text) — Person who identified the specimen
- **Determine Date** (11 chars, text) — Date of identification

### Locality Fields
- **Country** (25 chars, text, required) — Use "unknown" if not known
- **Country Subdivision** (variable) — State, province, canton
- **Specific Locality** (text) — Detailed site description
- **Elevation** (numeric) — In meters; 0 = sea level; negative = below sea level
- **Elevation Source** (text) — How elevation was determined
- **Latitude/Longitude** — Decimal degrees or degrees-minutes-seconds
- **GPS Datum** — WGS84 or other reference

### Collector Fields
- **Collector** (55 chars, text) — Person or team who collected the specimen
- **Collector Number** (text) — Unique field number assigned by collector
- **Collection Date** (text) — Date of collection

### Substratum and Habitat
- **Substratum** (text) — Host species or substrate type
- **Habitat** (text) — Forest type, grassland, aquatic, etc.

### Specimen Details
- **Specimen Type** (text) — Holotype, isotype, voucher, etc.
- **Herbarium Code** (text) — Index Herbariorum abbreviation

## Standardization of Data

Failure to standardize format and content greatly reduces database value.
Key principles:

- **Enforce standardization at entry time** rather than relying on
  post-entry editing
- Use authority tables for controlled vocabularies
- Standardize date formats (e.g., YYYY-MM-DD)
- Standardize geographic names using recognized references (Times Atlas,
  ISO standards)
- Verify data using lookup tables before accepting entries

## Specimen Table Design

Two events are distinguished in specimen data: **collection** and
**identification**. Fields for each event are ideally assigned to separate
tables. The specimen table captures the collecting event (who, what, where,
when). A separate identification table includes the scientific name, determiner,
and date of determination. An intermediate table linking collection and
identification numbers allows one specimen to have multiple determinations over
time — a common occurrence in taxonomic work.

The specimen record serves as a voucher for observations that support
conclusions in biodiversity studies. Every specimen documented in publications
should have a corresponding database record accessible to other researchers.

## Practical Goals

A well-designed fungal specimen database should achieve:

1. Well-designed atomic fields and authority tables for validation
2. Relational links between taxonomic, geographic, and specimen data
3. Reusable data tables across applications (e.g., name table for both
   specimen labels and nomenclatural databases)
4. Reduced redundant data entry through table relationships
5. Consistent data facilitating exchange with institutional databases
   and international biodiversity networks

## See Also

- [[biodiversity-of-fungi-herbarium-specimen-curation-best-practices]]
- [[biodiversity-of-fungi-fungal-culture-preservation-techniques]]
- [[biodiversity-of-fungi-fungal-survey-design-baseline-monitoring]]
