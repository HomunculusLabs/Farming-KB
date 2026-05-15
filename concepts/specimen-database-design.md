---
title: Specimen Database Design
source: unknown-biodiversity-of-fungi.md
type: concept
---

# Specimen Database Design

Specimen database design encompasses the principles, structures, and practices for building relational databases that document the occurrence of organisms in a given place at a given time. A well-designed personal database can serve both the needs of the researcher and provide valuable data for comprehensive biodiversity studies.

## Database Design Philosophy

Designing a database is best done from the **top down**: first determine the purpose, then identify the subjects (entities) the database must track, and finally create a separate table for each subject. The goals of individual scientists and consumers of biodiversity information are inherently compatible — a well-thought-out database management application serves both audiences.

## Fields and Tables

Once subjects are identified, data elements are assigned to each table. Key principles for field design:

1. **Fields should describe the subject** of their table.
2. **Break data into the smallest logical units** — e.g., place each element of a taxonomic name (genus, specific epithet, family) in a separate field rather than a single combined field.
3. **It is difficult to parse data into too many fields** — err on the side of granularity.
4. **Check designated fields against field notes and reports** to ensure all necessary information is covered.

Key principles for table design:

1. Tables should **only include fields pertaining to the same subject**.
2. Tables should **not contain fields intentionally left blank** in many records — this often signals those fields belong in a different table.
3. Different tables should **not duplicate data** except as needed to establish relationships.

## Table Relationships

Relational databases store different data sets in separate tables, define relationships among them, and use those relationships to retrieve data across tables. Two tables must **share a data element** (field) of the same data type to be related. The shared field in one table typically references a unique identifier in another table.

- A **primary key** uniquely identifies each record in a table (e.g., an arbitrary ID number or a natural key like a roll number).
- A **foreign key** in one table references the primary key of another table, establishing the relationship.

When two tables lack a common data element, an additional linking field can be added (e.g., adding a `SpecimenName` number field to one table to reference the `ID` field of a name table).

## Relational Tables in Systematics

The relational methodology applies naturally to systematic biology:

- **Specimen tables** should be restricted to information about the collecting event: who, what, where, and when. Morphological data belongs in a separate table.
- **Nomenclature databases** track names and their associated literature citations. Citations are best placed in a separate bibliographic table to facilitate reusability — a single publication describing multiple taxa need only be entered once.
- **Bibliographic databases** maintain full literature citations that can be linked to name tables and other applications. This avoids redundant citation entry.
- **Taxonomic classification tables** can be used to determine class and order for names in the specimen table.

A primary goal of relational design is **reducing redundant keyboarding** and enabling **data reusability**. A name table, for example, is entered once but can be used in specimen label tables, nomenclature tables, and other applications, ensuring consistent use across all of them.

## Recursive Relationships

A **recursive relationship** occurs when a table is related to itself. This is particularly useful in nomenclature databases. Consider a name table with three fields:

- **NameId** — a unique identifier (primary key)
- **Name** — the taxonomic name (text)
- **Synonym** — a reference to another record's NameId (foreign key pointing to the same table)

The synonym field is numeric, pointing to an existing record in the same table. By relating the table to itself, you can display the actual synonym name rather than just its ID. This design allows listing accepted names only, accepted names with their synonyms, or synonyms only.

A **SynonymType** field can further classify relationships with values such as:

- **b** — basionym
- **o** — obligate synonym
- **t** — taxonomic synonym

Sorting by SynonymType arranges synonyms in standard publication order. Adding a fourth field linking to a literature citation table enables full nomenclatural tracking. The resulting name table can then be used to update names in the specimen table, embodying the theme of reusability.

## Data Standardization

Field structure may be the most important aspect of database design, but failure to standardize **both format and content** of entered data greatly reduces the database's value. Standardization is especially critical when converting data between applications — inconsistency causes the most trouble during such migrations.

**Key standardization practices:**

- **Enforce standardization at the time of entry**, not through post-entry editing. Good intentions for later cleanup almost always fail.
- **Standardize format** through the software application (e.g., enforcing dates as YYYY MM DD).
- **Standardize content** so that querying for a particular piece of information returns all matching records — inconsistent spelling of names or places will cause records to be missed.
- Well-standardized data makes it feasible to include records in larger datasets or to combine datasets from different sources.

## Authority and Lookup Tables

Related tables serve a major role in **verifying data** as it is entered. Tables used for this purpose are called **lookup tables** or **authority tables**. Common examples include:

- **Geographic names** — standardized lists of states, provinces, cantons, districts, etc. A state table linked to the specimen table restricts entry to valid values, ensuring consistency without post-entry editing.
- **Taxon names** — generic names, author names, and other nomenclatural elements are obvious candidates for authority tables.

Authority tables can be obtained from colleagues or institutions that have built them for external use, or they can be constructed by entering items from standard references. On any project of significant size with long-term continuity, authority tables **significantly increase data entry efficiency** — their importance is difficult to overstate.

## Application Software

A single database product can handle many data manipulation needs. However, practitioners often use different tools for different purposes: bibliographic software for citations, databases for specimen labels, and spreadsheets for morphological data. The downside is difficulty integrating and reusing data across products.

The advantage of a single software package is that electronic publication and real-time Internet display become extensions of existing procedures without reformatting. Relational databases provide the flexibility to build an application **table by table over time** as needs arise.

## User Interface Design

The user interface controls how data are edited, added, and displayed. Most modern database packages simplify the creation of data-entry screens and reports. Data managers should **start simple and add capabilities as needed** — overzealous beginnings are a common cause of project stalls.

## Practical Considerations

Although the theoretical aspects of table design are interesting, practical aspects must also be considered. Simply put, the more complicated the table design, the more difficult it becomes to construct a usable interface between the user and the tables. Current software is helpful in this area but has limited resolving power.

Authority tables can be incorporated easily into table design. However, adding intermediate tables (e.g., linking specimen records to multiple identification events) requires increased knowledge of the more esoteric parts of database software. A well-designed database should, at minimum, achieve two things: well-designed fields and incorporation of authority tables.

An alternative approach to handling taxonomic names is to have fields for all components of the name (genus, species, author, etc.), each related to a separate table with standardized names for that component. While this design includes several tables, the individual components can be reused across applications, promoting consistency in nomenclatural data entry.

## Project Goals

Goals should be **realistic**, focusing on what is truly needed for research rather than what would be "nice." The biggest impediment to progress is typically the effort required to collate and enter information. Even with data entry assistance, time demands for prescreening can be high. A small, well-defined database can be integrated into a work routine, and understanding how it supports data maintenance helps guide expansion into other activities.

## Core Data Structure for Exchange

A core specimen-data record includes the fundamental elements: **what, who, when, and where**. A proposed core data structure serves as a model framework fulfilling several functions:

1. **Basic exchange format** — a flat file structure with field names, definitions, and maximum field lengths, requiring awareness from both data donor and recipient.
2. **Point of departure for communication** — donors can describe how their data differ from the basic exchange format, enabling structured interoperability.
3. **File structure for specimen information** — suitable for collecting and storing specimen data for various purposes beyond exchange.

This framework draws on work from many ongoing projects and institutions, including the Natural Science Collections Alliance and the Common Data Structure for European Floristic Databases, adapting their principles to mycological specimens.

## Conclusions

Modern database software greatly increases the ease with which applications can be developed by end users. If fields are delimited carefully, applications can be developed that meet the researcher's needs yet provide data that are generally useful and easily transferable to the wider community involved in biodiversity studies. Although the software has improved and is easier to use, it will not immediately meet all data management needs. If expectations are reasonable, chances of successful implementation are improved greatly. If designed properly, database tools will be useful throughout a career — they are worth an investment of time and patience.

## See Also

- [[mycorrhiza]]
- [[basidiomycota]]
- [[ascomycota]]
- [[kingdom-fungi]]
- [[mushroom-identification]]
