---
title: Relational Databases in Fungal Systematics
source: unknown-biodiversity-of-fungi.md
type: concept
---

# Relational Databases in Fungal Systematics

Relational databases have become indispensable tools for managing the complex data associated with fungal biodiversity research. Modern database software greatly increases the ease with which applications can be developed by end users. When fields are delimited carefully, applications can be developed that meet the researcher's specific needs while producing data that are generally useful and easily transferable to the wider community involved in biodiversity-related studies.

## Table Design Principles

Three fundamental principles guide relational table design in systematics:

1. **Subject cohesion** — Tables should include only fields pertaining to the same subject.
2. **Non-sparsity** — Tables should not contain fields intentionally left blank in many records; such fields belong in a separate table.
3. **No redundancy** — Different tables should not duplicate data except as needed to establish relationships.

A primary goal of table design is reducing redundant keyboarding. The same principle of reusability means that a name table, for example, can be used across multiple applications — specimen labels, nomenclatural databases, and taxonomic checklists — with the name entered only once but used in many places.

## Relational Tables in Systematics

A **specimen table** should be restricted to information relating to the collecting event: *who*, *what*, *where*, and *when*. This includes the identity of the specimen, the collector, the date, and the place — the essential data that enable a specimen to serve as a voucher for observations supporting conclusions in biodiversity studies.

Information dealing with morphological features is best placed in a **separate table**, keeping the specimen record lean and focused on the collecting event. This separation also facilitates the reusability of morphological data across different analyses and publications.

Two distinct events can be recognized in specimen management: **identification** and **collecting**. Fields associated with each event can be assigned to separate tables. When field collecting involves many collections from a few localities, locality data entered once can be referenced easily by each specimen record, assuring consistency.

### Table Relationships

To relate two tables, they must share a data element (field) of the same data type (e.g., numeric or text). Modern relational database software has improved greatly the ease with which tables can be linked to produce reports combining data from multiple sources. What once required significant programming can now be accomplished with essentially no effort.

## Nomenclature and Bibliographic Tables

An obvious component of nomenclature information is the original citation. Although every name will have a literature citation, the citation should be stored in a **separate bibliographic table** rather than embedded in the name table to facilitate reusability.

Literature citations are often maintained in a bibliographic database. By establishing a relationship between the bibliographic table and the name table, a record from the bibliographic database can be used directly in the name table. This design is particularly valuable because multiple taxa are frequently described in a single publication — a full citation need only be entered once and then linked to all appropriate name tables.

A separate table can also be used to determine the **class** and **order** for the names in the specimen table, maintaining taxonomic classification independently.

## Recursive Relationships for Synonymy

A nomenclature database is often of particular interest to systematists. A **recursive relationship** — in which a table is related to itself — is a powerful tool for managing synonymy.

Consider a table with three fields:

- **NameId** — an ID number (numeric)
- **Name** — the scientific name (text)
- **Synonym** — a numeric field referring to another record in the same table

The synonym field points to an already-existing record in this same table. To display the actual name in the synonym field, the table must be related to itself. With this design you can list only accepted names, accepted names with their synonyms, or only the synonyms.

### SynonymType Field

An additional field, **SynonymType**, controls the sorting of synonyms into the standard order used in publications. Three text designations are employed:

| Code | Synonym Type | Description |
|------|-------------|-------------|
| **b** | Basionym | The original name on which a new combination is based |
| **o** | Obligate synonym | A nomenclaturally required synonym |
| **t** | Taxonomic synonym | A synonym based on taxonomic judgment |

By sorting on the SynonymType field, synonyms are automatically arranged in the standard publication order. Adding a fourth field containing the link to a literature citation table makes it possible to maintain a full nomenclatural application.

### Updating Specimen Names

Recalling the theme of data reusability, the name table in the nomenclature database can be used to **update names in the specimen table**. When taxonomic revisions occur, changes to the nomenclatural database propagate to linked specimen records, maintaining consistency across the entire data set.

## Data Standardization

Although field structure may be the most important aspect of a database project, failure to standardize both the format and content of entered data can greatly reduce the value of the database. When converting data between applications, a lack of standardization causes the most trouble. The act of entering data into a database does not confer higher precision than the data actually possess.

### Format Enforcement

The software application controls format standardization, checking that data are entered consistently. Dates, for example, should always use the **YYYYMMDD** format (American National Standards Institute standard). This prevents variations like "1/5/03," "Jan 5, 2003," and "2003-01-05" from coexisting in the same field.

### Content Standardization

When a database is queried for a particular piece of information, it should produce all records containing those data. This fails if the item name has not been spelled the same way in all records. Well-standardized data make feasible the inclusion of records in larger datasets or combinations of datasets.

## Authority (Lookup) Tables

Another major use of related tables is to **verify data being entered** into the main table. Tables of this type are called "lookup tables" or **authority tables**.

### How Authority Tables Work

A common example is a table of standardized geographic or political names — states, provinces, cantons, districts. If a relationship is set up between the state field in a specimen database and a table listing all states, most software will only allow values that appear in the authority table. This ensures consistent data entry without post-entry editing.

Many fields in a specimen database benefit from authority tables. Obvious candidates include:

- **States and provinces** — standardized political subdivisions
- **Generic names** — validated against accepted fungal generic names
- **Author names** — standardized according to Brummitt and Powell (1992)
- **Place names** — verified geographic locations

### Building vs. Obtaining Authority Tables

Authority tables can be **obtained** from a colleague or institution that has already built such a table and made it available for outside use. The alternative is to **build the lookup table yourself** by entering items from a standard reference, either all at once or incrementally as data are entered. With the latter approach, procedures for adding new values to the authority table must be established during the early stages of the project.

### Long-Term Efficiency Benefits

On a project of any size involving a continuing long-term effort, authority tables **significantly increase the efficiency of data entry**. It is difficult to overstate their importance. The initial investment in creating or obtaining authority tables pays dividends throughout the lifetime of the database.

## Application Software Considerations

### Single vs. Specialized Products

A single database product can handle many data manipulation needs. However, in practice, literature citations may reside in bibliographic software, specimen-label data in a database, and morphological data in a spreadsheet.

The **downside of using different products** is the difficulty of reusing data for different purposes. For example, integrating literature citations in a specialized bibliographic database with a nomenclatural database can be challenging. The **downside of a single package** is that individual applications may not be as sophisticated as purpose-built tools.

### Incremental Development

Relational databases provide logical procedures for **building an application table by table over time** as needs arise. This incremental approach allows researchers to start with a small, well-defined database that integrates into daily work routines, then expand it to include additional activities as understanding of how the database supports data maintenance grows. Project goals should be realistic, focusing on what is truly needed rather than what would be "nice" — many projects stall after overzealous beginnings.

## Appendix: Core Specimen-Data Record

A core data structure for mycological specimens provides a model framework serving several functions:

1. **Exchange format** — A flat-file structure with field names, definitions, and maximum field lengths, understood by both data donors and recipients.
2. **Communication standard** — A reference point for describing how transferred data differ from the basic format.
3. **Storage framework** — A file structure for collecting and storing specimen information for various purposes.

The core record captures the essential **what, who, when, and where** information:

- **What**: Taxonomic name (genus, species, author, infraspecific epithet, rank)
- **Who**: Collector, team collectors, determiner, submitter
- **When**: Collection date(s), season, determination date(s)
- **Where**: Country, political subdivisions, place name, locality, latitude/longitude, elevation

Additional fields for host information (substratum, habitat, host genus/species), type status, and culture data extend the core record for specialized applications while maintaining compatibility with the basic exchange format.

## References

- Farr, D.F. and Farr, E.R. Electronic Information Resources (Chapter 4). In: *Biodiversity of Fungi*.
- Brummitt, R.K. and Powell, C.E. 1992. *Authors of Plant Names*. Royal Botanic Gardens, Kew.
- Bisby, F.A. 1994. Data standards. In: *Biodiversity Information Standards (TDWG)*.
- Greuter, W. et al. 2000. *International Code of Botanical Nomenclature* (St. Louis Code).
- Federal Geographic Data Committee. 1998. *Content Standard for Digital Geospatial Metadata*.

## See Also

- [[mycology]]
- [[mycorrhiza]]
- [[basidiomycota]]
- [[ascomycota]]
- [[kingdom-fungi]]
