---
title: Database Design for Fungal Specimen Collections
source: unknown-biodiversity-of-fungi.md
type: concept
---

## Introduction

Database design for fungal specimen collections requires careful planning and builds on the foundations described in [[specimen-database-design]]. A well-designed database ensures data integrity, supports research, and facilitates data sharing among institutions.

## Top-Down Design Approach

Effective database design begins with a **top-down approach** — starting from broad purpose and narrowing to specific data elements.

### Define the Purpose

The first step is to clearly articulate what the database must accomplish:

- What types of queries will users run?
- Who are the primary users?
- Will it serve taxonomic research, collection management, or both?

These answers shape every subsequent design decision.

### Identify the Subjects

Next, identify the major **subjects** the database tracks. For fungal collections, these typically include:

- **Specimens** — the physical fungal material
- **Taxa** — names and classifications
- **Collectors** — people who gathered specimens
- **Locations** — geographic origin of specimens
- **Literature** — publications referenced by the collection

Each subject becomes one or more database tables. For each, determine every data element needed — it is far easier to design a field in from the start than to retrofit it later.

## Field-Level Design Principles

Every field should satisfy several quality criteria.

### Relevance and Atomicity

Only include fields that serve a clear purpose. Ask: *Will anyone need to search, sort, or report on this value?*

Each field should store a **single, indivisible** piece of information:

- Split names into `family_name` and `given_name`
- Decompose locations into `country`, `state`, `county`, `locality`
- Store date ranges as `start_date` and `end_date`

### Completeness and Consistency

Every record should have enough information to be scientifically useful. Distinguish between **mandatory** and **optional** fields.

Values within a field must follow a uniform format:

- Dates should all use one format (e.g., ISO 8601: `YYYY-MM-DD`)
- Country names should come from a standard list
- Collector names should follow a consistent authority format

## Table Design Principles

Tables are the structural backbone of the relational database. Each table should describe **one and only one** subject. When a table stores information about two subjects, it should be split.

A field that is empty for the majority of records signals a design problem — it may belong in a separate, related table. Data should appear in **exactly one place** in the database. The only acceptable repetition is **foreign key fields** that establish relationships between tables.

## Table Relationships

Tables are connected through **shared data elements** — fields appearing in two or more tables. A linking field (foreign key) in one table references the primary key of another, and both must have **identical data types**.

Common relationship types include:

1. **One-to-many** — one collector has many specimens.
2. **Many-to-many** — specimens in multiple publications (requires a junction table).
3. **One-to-one** — a specimen with one molecular sequence record (optional).

## Relational Design in Systematics

Fungal systematics imposes specific demands on database structure. Several specialized tables are typically needed.

### Specimen and Morphological Tables

The specimen table is the core of the collection database, as detailed in [[core-specimen-data-structure-mycology]]. Key fields include **accession number**, **collector name**, **collection number**, **date of collection**, **geographic location**, **substrate/host**, **habitat**, and **preservation status**.

Morphological characters are best stored in a separate linked table covering spore measurements, microscopic features (hyphal structure, cystidia), macroscopic features (cap size, color, odor), and chemical reactions (KOH, Melzer's, etc.). Separating morphological data allows for flexible querying and easier updates.

### Nomenclature and Bibliographic Tables

Fungal nomenclature is governed by the **ICN** and follows [[fungal-phylogeny-classification]] standards. A nomenclature table tracks the currently accepted name, all synonyms and their types, basionyms, nomenclatural status (valid, illegitimate, invalid), and author citations.

A bibliography table stores all cited literature: full author list, publication year, title, journal or book name, volume, issue, page numbers, and DOI or other persistent identifier.

## Recursive Relationships: Synonymy

Synonymy in fungal taxonomy creates **recursive relationships** — a taxon table that references itself.

### Synonym Tables and Types

A synonym table records the relationship between a synonym and its accepted name. Each row contains the synonym name, accepted name, and a **SynonymType** field.

The SynonymType field is critical. It distinguishes among several categories:

1. **Basionym** — the name-bearing synonym; the original published name.
2. **Obligate synonym** — based on the same type specimen; automatically synonymized.
3. **Taxonomic synonym** — subjective judgment that two names refer to the same taxon.

### Literature Citation Links

Every synonymy decision should link to a **literature citation**, so users can see *why* a name was synonymized and by *whom*.

## Data Standardization

Standardization is essential for data quality and interoperability.

### Format vs. Content

**Format standardization** controls how data is entered (date format, coordinate format). **Content standardization** controls what values are permitted (controlled country lists, herbarium codes). Both are necessary.

### Entry-Time vs. Post-Entry

**Entry-time** standardization enforces rules as data is input using dropdown lists and validation rules. **Post-entry** standardization cleans data after input using batch scripts. The best approach uses both.

### Authority Tables and Lookup Tables

**Authority tables** (lookup tables) store the valid values for a field. A `countries` table provides official names and ISO codes; a `herbaria` table stores recognized acronyms (per Index Herbariorum); a `specimen_preservation` table lists valid preservation methods. Lookup tables ensure consistency — updating a country name requires changing only one row.

## Application Software Considerations

A **single integrated product** offers simplicity but may lack flexibility. **Multiple specialized products** offer power but require integration effort. Most collections benefit from starting with one system and adding tools as needs grow.

Common integration methods include shared database back-ends, import/export routines (CSV, Darwin Core), and API connections. Modern databases should be **web-compatible** and follow [[mycology|mycological]] data standards — exporting in standard formats and serving records to aggregators like GBIF or MycoBank.

## Practical Implementation

Start with the **minimum viable database** that meets the collection's core needs. Prioritize specimen records, taxonomic names, and collector data. Defer complex features (molecular data, image management) to later phases.

### Incremental Growth

Build in phases, each delivering a **working system**:

1. **Phase 1** — Core specimen table with basic fields.
2. **Phase 2** — Taxonomic tables with synonym tracking.
3. **Phase 3** — Bibliographic links and authority tables.
4. **Phase 4** — Advanced features (GIS, molecular data, web interface).

### User Interface and Documentation

A complex schema does not require a complex user interface. Data entry screens should be clean, guided by dropdown lists, and organized logically.

Every standard should be documented in a **data dictionary** specifying the definition and purpose of every field, accepted values and formats, mandatory versus optional status, and relationships between tables and fields. The data dictionary is the single most important reference for maintaining data quality over time.

## Conclusion

Database design for fungal specimen collections requires both mycological expertise and sound relational design principles. By following a top-down approach, enforcing field and table design rules, managing synonymy through recursive relationships, and standardizing data through authority tables, curators can build databases that serve their collections for decades.

Start small, document everything, and let the database grow with the collection.

## See Also

- [[specimen-database-design]]
- [[biodiversity-database-design-fields-tables]]
- [[fungal-phylogeny-classification]]
