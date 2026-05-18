---
title: Database Design for Biodiversity Information
source: unknown-biodiversity-of-fungi.md
type: concept
---

# Database Design for Biodiversity Information

## Overview

Effective biodiversity databases are essential infrastructure for mycological and biological inventory work. Two fundamental approaches exist for managing biodiversity data: **centralized** systems, where a single authoritative repository holds all data under one schema, and **distributed** systems, where data reside across multiple institutions or projects and are linked through shared standards and protocols.

Centralized databases simplify querying and consistency enforcement but require significant governance overhead, including agreed-upon data models, access policies, and long-term maintenance commitments. They work well for large institutional collections or national inventories where a single authority can enforce standards.

Distributed approaches—increasingly common in [[fungal-biodiversity]] work—allow individual researchers or collections to maintain local control while enabling data exchange through common formats and identifiers (e.g., UUID, Life Science Identifiers, or DOIs for datasets). This model reflects the reality that fungal specimens, cultures, and sequence data are often scattered across herbaria, culture collections, and sequence repositories worldwide.

Regardless of architecture, sound database design principles apply to both. The decisions made at the schema level ripple through every downstream activity—data entry, querying, reporting, analysis, and data sharing.

## Top-Down Design Approach

Biodiversity databases should be designed top-down, starting from the **purpose** of the system, then identifying the **subjects** (real-world entities) to be represented, and finally defining the **data elements** (fields) that describe each subject.

For example, a herbarium specimen tracking system's purpose is to manage voucher information. Its subjects include specimens, taxa, collectors, localities, and collecting events. Its data elements are attributes like collection date, latitude, collector name, and species epithet. Each step narrows the focus and makes the next step more tractable.

This disciplined approach prevents scope creep and ensures every field in the database serves a documented need. It also produces natural documentation: the purpose statement becomes the project charter; the subject list becomes the entity-relationship diagram; the field definitions become the data dictionary.

## Fields: The Smallest Logical Units

Fields represent the atomic units of data. Breaking information into its smallest meaningful components is critical for flexibility and query power. For instance:

- A collector's full name should be split into `given_name` and `family_name` rather than stored as a single string—this enables sorting, searching, and formatting variations (e.g., "Smith, J.K." vs. "J.K. Smith").
- Geographic coordinates are best stored as separate numeric `latitude` and `longitude` values rather than a free-text location description, enabling spatial queries and mapping.
- A full taxonomic name should be decomposed into `genus`, `specific_epithet`, `infraspecific_rank`, `infraspecific_epithet`, and `author_citation`.

When defining fields, designers should systematically check against existing **field notes** and collection forms to ensure all routinely recorded information has a home in the schema. However, fields that are rarely populated should be questioned—every field adds maintenance burden.

## Tables: Grouping Related Fields

Tables group fields that share a common subject or entity. A well-designed `specimens` table holds all attributes pertaining to a single voucher specimen (collector, date, elevation, substrate), while a `taxa` table stores nomenclatural details and a `localities` table stores geographic information.

Key design rules include:

- **Avoid blank fields**: If a table has many fields that are null for most records, those fields likely belong in a separate, related table. For example, not every specimen has an associated DNA barcode, so barcode-related fields belong in a linked `sequences` table.
- **Avoid data duplication**: If the same piece of information (e.g., a collector's full address) is repeated across many records, it should be moved to its own table and referenced by a foreign key. This is the foundational principle of database normalization.

## Table Relationships

Tables communicate through **shared data elements**—typically primary and foreign keys. A `specimens` table might reference a `collectors` table via a `collector_id` field, ensuring each collector's information is stored exactly once. Data types must be consistent across related tables: if `collector_id` is an integer in one table, it must be an integer in every table that references it.

Relationship cardinality should be explicitly modeled:

- **One-to-one**: A specimen has one accession number; an accession number refers to one specimen.
- **One-to-many**: A collector may have made many collections; a roll of film contains many negatives.
- **Many-to-many**: A specimen may be identified by multiple taxonomists; a taxonomist may identify many specimens (typically resolved through a junction/link table).

These constraints enforce real-world logic and prevent orphaned or contradictory records.

## Relational Databases for Biodiversity Work

Relational database management systems (RDBMS) running on personal computers have long been the backbone of small-to-medium biodiversity projects. A classic mycological example involves three linked tables:

- **Negatives** table: photographic records of fungal specimens (negative number, frame, date, subject description).
- **Names** table: taxonomic identifications linked to each negative (species name, identifier, date of determination).
- **Roll** table: photographic film metadata (roll number, film type, date loaded, camera body, lens).

Each negative belongs to a specific roll; each negative may carry one or more names. By relating these tables through foreign keys rather than embedding roll information in every negative record, the database avoids massive redundancy and keeps the schema clean.

## Redundancy Reduction Through Separate Tables

The roll table example illustrates a core principle: enter information **once**, then reference it. A single roll record (film type, date loaded, camera) is linked to dozens of negatives, eliminating the need to repeat that data for every image.

This not only saves storage but, more importantly, ensures **consistency**—if the film type needs correction, it is changed in one place and all related negatives automatically reflect the update. Without this separation, correcting a single error across hundreds of records is error-prone and time-consuming.

In biodiversity contexts, the same principle applies to collectors, localities, taxa, and preparation methods. Each deserves its own table with a unique identifier that other tables reference.

## Data Reusability

A well-designed name or taxon table is reusable across multiple contexts. The same `taxa` table can serve specimen labels, nomenclatural databases, checklists, and ecological observations. By centralizing taxonomic information, changes to a name (e.g., a new combination following taxonomic revision) propagate to every record that references it.

This reusability is a major efficiency gain and reduces the risk of inconsistent nomenclature across project outputs. When a species is reclassified, updating one record in the `taxa` table automatically corrects all specimen labels, reports, and checklists that draw from it.

## Recursive Relationships in Nomenclature

Nomenclatural databases frequently require **recursive relationships**, where a table references itself. Synonyms, for example, point to the same `taxa` table: both the accepted name and its synonyms exist as rows, with synonym records carrying a foreign key to their accepted-name counterpart.

A `SynonymType` field classifies the relationship:

| SynonymType | Meaning |
|---|---|
| **Basionym** | The original published name on which a new combination is based |
| **Obligate synonym** | A nomenclaturally necessary synonym (homotypic) |
| **Taxonomic synonym** | A taxonomic judgment synonym (heterotypic) |

This design allows queries that traverse synonymy chains and supports automatic display of current accepted names alongside historical combinations. It also enables analysis of nomenclatural history—tracking how many times a species has been recombined, by whom, and in which publication.

## Standardization of Data: Format and Content

Data standardization operates at two levels:

**Format standardization** ensures uniform data entry—dates in ISO 8601 format (YYYY-MM-DD), coordinates in decimal degrees (WGS 84 datum), measurements in metric units, and text in consistent case conventions. Without format standards, even simple queries (e.g., "all specimens collected in 2023") may fail because dates were entered as "Jan 15, 2023", "15/01/2023", and "2023-01-15".

**Content standardization** uses **authority tables** (also called lookup or reference tables) to constrain values:

- Geographic names should reference a gazetteer table with standardized country, state/province, and county names.
- Generic names should validate against an approved list (e.g., Index Fungorum or MycoBank).
- Substrate, habitat, and host terms should draw from controlled vocabularies.

Authority tables prevent spelling variants, enforce controlled vocabularies, and make queries more reliable. They can be enforced at the database level (foreign key constraints) or at the application level (drop-down lists in the user interface).

## Application Software Considerations

Project leads must decide between using a **single integrated database product** (e.g., FileMaker, Microsoft Access, or a web-based platform like Symbiota) versus **multiple specialized tools** that interoperate.

Single-product solutions simplify deployment and user training but may lack depth in any one domain. Multi-product architectures (e.g., a RDBMS for specimen data coupled with a GIS application for mapping and a separate taxonomic name server) offer best-of-breed capabilities but demand expertise in data exchange formats and integration.

Key considerations include cost, available technical support, data export capabilities, and alignment with community standards such as Darwin Core or ABCD (Access to Biological Collection Data).

## User Interface Design Principles

The best database schema is useless if users cannot interact with it effectively. Interface design principles for biodiversity databases include:

- **Minimize keystrokes** through auto-population, default values, and pick lists drawn from authority tables.
- **Validate at entry**—reject invalid dates, out-of-range coordinates, or unapproved names before they reach the database.
- **Support batch operations** for importing field data or bulk-updating records (e.g., updating all specimens in a genus after a taxonomic revision).
- **Provide clear feedback** when errors occur, with guidance on correction.
- **Design for the actual users**—typically field mycologists and collection managers, not database administrators. The interface should reflect their workflow, not the underlying table structure.

## Project Goals: Start Small, Focus on Realistic Needs

The most common pitfall in biodiversity database projects is over-ambition. A successful project begins with a **narrow, realistic scope**—for example, tracking specimens from a single expedition or managing a single genus. Core functionality (data entry, searching, reporting) should be solid before adding features like web publishing, image management, or GIS integration.

Incremental growth allows the team to learn from real usage patterns and adapt the schema accordingly. A small, working database that people actually use is infinitely more valuable than a comprehensive design that was never implemented. Each successful increment builds trust, demonstrates value, and creates momentum for the next expansion.

## Key Takeaways

- Design top-down: purpose → subjects → fields.
- Break data into atomic fields; group fields into subject-based tables.
- Relate tables through shared keys; maintain data type consistency.
- Eliminate redundancy by separating entities into their own tables.
- Use authority tables to standardize content and format.
- Plan for recursive relationships in nomenclatural data.
- Choose software that matches team capacity and project scale.
- Start small, deliver working systems, and grow iteratively.

## See Also

- [[mycology]]
- [[database-design-fungal-specimens]]
- [[mycological-specimen-data-standards]]
- [[fungal-taxonomy]]
