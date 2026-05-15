---
title: Database Design for Biodiversity Information
source: unknown-biodiversity-of-fungi.md
type: concept
---

# Database Design for Biodiversity Information

Electronic information resources are essential tools for managing the vast amounts of data generated in biodiversity research. Whether tracking fungal specimens, cataloging species, or managing taxonomic nomenclature, well-designed databases enable researchers to store, retrieve, and analyze data efficiently. This page covers the fundamentals of database design as applied to biodiversity and systematics data.

## Database Design Fundamentals

At the heart of every database lies the concept of **fields** and **tables**. A field is the smallest unit of data — a single attribute such as a specimen number, a species name, or a collection date. Fields are grouped into tables (also called files or relations), where each row represents a single record and each column represents a field. For example, a specimen table might contain fields for accession number, scientific name, collector, date, and locality.

Database design follows a **top-down approach**: first identify the scope and purpose of the database, then define the major entities (tables) and their attributes (fields), and finally establish the relationships between tables. This structured methodology ensures that the database faithfully models the real-world domain it serves.

## Relational Databases and Table Relationships

Relational database management systems (RDBMS) organize data into multiple linked tables. Each table has a **primary key** — a unique identifier for every record (e.g., an accession number). Tables are connected through **foreign keys**, which are fields in one table that reference the primary key of another table.

Three fundamental types of relationships exist:

- **One-to-one**: Each record in Table A links to exactly one record in Table B (e.g., a specimen and its detailed molecular analysis record).
- **One-to-many**: One record in Table A links to many records in Table B (e.g., a species name links to many specimen records).
- **Many-to-many**: Records in Table A link to multiple records in Table B and vice versa (e.g., specimens linked to multiple habitat types). These are resolved using **junction tables**.

These relationships eliminate data redundancy, enforce referential integrity, and allow complex queries across related datasets.

## Relational Tables in Systematics

Biodiversity and systematics databases present unique modeling challenges. Taxonomic hierarchies — kingdom, phylum, class, order, family, genus, species — naturally lend themselves to relational structures. Each taxonomic rank can occupy its own table or be represented as fields within a single taxon table linked by parent-child relationships.

Specimen databases link taxonomic names to collection events, which in turn link to locality records, collector information, and ecological observations. This modular design allows a single locality record to be referenced by many specimens, and a single collector to be associated with many collection events.

## Recursive Relationships

A particularly powerful design pattern in biodiversity informatics is the **recursive relationship**, where a table relates to itself. This is indispensable for nomenclature databases, where taxonomic names may have synonyms, basionyms, or replaced names. A single "names" table can include a foreign key that points to its own primary key, allowing each name to reference another name in the same table.

For example, a current accepted name may reference a basionym (the original published name), and synonym records may reference the accepted name. This self-referencing structure elegantly captures the complex history and reclassification of taxa without duplicating tables or creating cumbersome data architectures.

## Standardization of Data

Data standardization operates at two levels: **format** and **content**.

**Format standardization** ensures that data values follow consistent conventions. Dates should use a single format (e.g., ISO 8601: YYYY-MM-DD). Geographic coordinates should use a consistent datum and decimal degree format. Specimen numbers should follow a defined pattern.

**Content standardization** ensures that the same concept is always represented the same way. A genus name should be spelled consistently; country names should follow a recognized standard (e.g., ISO 3166); ecological terms should come from an agreed-upon vocabulary.

Without standardization, data retrieval becomes unreliable — queries may miss records because of trivial spelling differences or formatting inconsistencies.

## Authority Tables and Lookup Lists

To enforce content standardization, databases employ **authority tables** (also called lookup tables, controlled vocabularies, or pick lists). These are auxiliary tables that store all valid values for a particular field. Instead of allowing free-text entry, the database constrains the user to choose from the pre-approved list.

For example, an authority table for countries ensures that every locality record references the same canonical country name. Similarly, a habitat-type authority table guarantees that ecological descriptions use a consistent terminology. Authority tables also simplify data entry, reduce errors, and enable more efficient querying and reporting.

## Application Software Choices

Selecting the right database software depends on project scale, budget, and technical expertise. Options range from simple flat-file solutions and desktop RDBMS (e.g., Microsoft Access, FileMaker) for small collections, to enterprise-grade systems (e.g., PostgreSQL, MySQL, Oracle) for institutional databases with many concurrent users and large datasets.

Open-source platforms such as Symbiota, Specify, and Brahms are purpose-built for biodiversity collections and offer pre-configured schemas for specimen data. The choice of software should align with the project's long-term goals for data sharing, interoperability, and sustainability.

## User Interface Considerations

The user interface is the bridge between the database engine and the people who enter and retrieve data. A well-designed interface should:

- Present data entry forms that mirror the structure of the underlying tables.
- Use dropdown lists linked to authority tables to enforce controlled vocabularies.
- Provide search and query interfaces that accommodate both simple and complex queries.
- Include validation rules to catch errors at the point of entry (e.g., latitude must fall between -90 and 90).
- Support batch import and export of data for interoperability with other systems.

A database that is technically robust but difficult to use will suffer from poor data quality and low adoption.

## Defining Project Goals

Before designing a database, it is critical to define clear **project goals**. Key questions include:

- What is the primary purpose — research, curation, education, or public outreach?
- Who are the users, and what are their technical skills?
- What types of data will be stored (specimens, observations, sequences, images)?
- Will the data need to be shared or published to aggregators (e.g., GBIF, iDigBio)?
- What are the long-term maintenance and migration plans?

Answering these questions shapes every subsequent design decision, from table structure to software selection.

## Core Specimen Data Structure

The backbone of most biodiversity databases is the specimen record. A well-designed core data structure typically includes the following categories of fields:

### Taxonomic Name Fields

- **Kingdom, Phylum, Class, Order, Family** — higher classification.
- **Genus** and **specific epithet** — the binomial components.
- **Infraspecific rank and epithet** — for subspecies, varieties, or forms.
- **Author/citation** — the authority who published the name.
- **Name according to** — the taxonomic reference or treatment followed.
- **Identification qualifier** — e.g., "cf.," "aff.," "s. lat.," indicating uncertainty.
- **Identifier name and date** — who identified the specimen and when.

### Locality Data

- **Country** and **state/province** — political geography.
- **County/district** — administrative subdivision.
- **Locality description** — free-text description of the site (e.g., "3 km north of town on riverbank").
- **Latitude, longitude, datum** — geographic coordinates with coordinate reference system.
- **Elevation** — altitude in meters.
- **Georeference source and uncertainty** — how coordinates were derived and their precision.

### Collector Data

- **Primary collector** — the person who collected the specimen.
- **Additional collectors** — other participants in the field.
- **Collection number** — the collector's field number.
- **Collection date** — when the specimen was gathered.

### Habitat and Substratum Fields

- **Habitat** — the broader ecological context (e.g., "temperate rainforest," "grassland").
- **Substratum** — the immediate substrate on which the organism was found (e.g., "decaying wood of Quercus robur," "soil under Pinus").
- **Associated organisms** — other species observed in association.
- **Host** — for parasitic or symbiotic fungi, the host species.

This core structure provides a solid foundation that can be extended with additional fields for molecular data, morphology, images, or project-specific attributes as needed.

## See Also

- [[mycology]]
- [[mycorrhiza]]
- [[basidiomycota]]
- [[ascomycota]]
- [[kingdom-fungi]]
