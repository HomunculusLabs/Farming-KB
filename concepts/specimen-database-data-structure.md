---
title: Specimen Database Core Data Structure
source: unknown-biodiversity-of-fungi.md
type: concept
---

# Specimen Database Core Data Structure

The core data structure for a mycological specimen database defines a standardized set of fields that capture every essential piece of information associated with a fungal specimen. This structure is designed to support biodiversity research, taxonomic revision, specimen tracking, and data exchange across herbaria and research institutions worldwide. The fields are organized into logical groups reflecting the stages of a specimen's lifecycle — from collection and identification to curation and storage.

## Taxonomic Name Fields

Taxonomic name fields form the backbone of specimen identification. Each specimen record must include the **genus** (a text field following the International Code of Nomenclature for algae, fungi, and plants), the **species epithet**, and the **infraspecific rank** (e.g., variety, form, subspecies). A **subspecific epithet** field accommodates names below the species level. The **author citation** field records the person(s) who validly published the name, formatted according to standard botanical conventions (e.g., "(Pers.) Hook."). The **determiner** field identifies the person who applied the current name to the specimen, while the **determination date** records when that identification was made — both critical for assessing the reliability and recency of the identification. A **verbatim name** field may also be included to preserve the original name as it appeared on the label, regardless of current taxonomic opinion.

## Locality and Geographic Data Fields

Geographic locality data enable researchers to map species distributions and analyze biogeographic patterns. The **country** field uses ISO 3166-1 two-letter or three-letter codes to ensure unambiguous identification of sovereign states. **Country subdivisions** (state, province, department) are recorded with standardized codes where available. The **place name** captures the nearest named geographic feature such as a town, mountain, or reserve. A free-text **locality description** provides detailed site-specific information — for example, "3 km north of the ranger station along the trail to Cerro Azul, in cloud forest."

**Elevation** is recorded in meters above sea level, optionally with minimum and maximum values to account for collecting ranges on slopes. **Latitude** and **longitude** are stored in decimal degrees (WGS 84 datum) along with a **coordinate source** field indicating how the coordinates were obtained (e.g., GPS device, georeferenced from place name, estimated from topographic map). An **uncertainty** field (in meters) quantifies the spatial accuracy of the coordinates, which is essential for downstream ecological analyses.

## Collector Information Fields

The **collector name** records the primary person who gathered the specimen, formatted as "Lastname, Firstname" to facilitate sorting and indexing. A **team collectors** field captures additional people who participated in the collecting event. The **collector number** is a unique identifier assigned by the collector to link specimens from the same foray or expedition. The **submitter** field identifies the person who deposited the specimen into the herbarium, which may differ from the collector when specimens change hands.

**Collection dates** are recorded with separate day, month, and year fields to handle partial dates (e.g., specimens collected with only month and year known). A **season** field may supplement date information, particularly for tropical regions where collecting events are described by rainy or dry seasons rather than calendar months.

## Substratum and Habitat Fields

Fungal ecology is intimately tied to substratum and habitat. The **substratum** field describes the material on which the fungus was found growing — wood (with host identity if possible), soil, leaf litter, dung, living plant tissue, or other organic matter. Standardized controlled vocabularies are recommended for this field to enable consistent querying. The **habitat** field provides broader ecological context, such as "tropical montane cloud forest," "mixed oak-pine woodland," or "disturbed agricultural field." Together, these fields support analyses of fungal niche specificity and ecological preferences.

## Host Organism Fields

When a fungus is associated with a specific host plant or animal, dedicated host fields capture that relationship. The **host genus** and **host species** fields follow the same nomenclatural conventions as the taxonomic name fields. An **host infraspecific rank** and **host subspecific epithet** accommodate named varieties or subspecies of the host. The **host common name** field records the vernacular name of the host organism, which aids communication with non-specialists and land managers. **Hybrid marker** fields (the multiplication sign ×) indicate whether the host is a hybrid taxon, following standard botanical practice. These host fields are particularly important for plant pathogenic fungi, mycorrhizal associates, and endophytes.

## Housekeeping and Herbarium Fields

Housekeeping fields support institutional specimen management. The **herbarium number** is the primary accession identifier, constructed by combining the institution's **Index Herbariorum code** (a globally unique 1–6 letter acronym registered with the New York Botanical Garden, e.g., NY, K, BPI) with a sequential specimen number. This combined code uniquely identifies any specimen in any herbarium worldwide. Additional housekeeping fields include the **accession date** (when the specimen was formally added to the collection), the **barcode** (machine-readable identifier), and **curation status** flags indicating whether the specimen has been mounted, frozen, or otherwise processed.

## Type Status and Culture Indicators

Specimens that serve as nomenclatural types carry special significance. The **type status** field records the role of the specimen — holotype, isotype, lectotype, neotype, epitype, paratype, or syntype — using controlled vocabulary from the botanical and mycological codes. These designations are essential for taxonomic stability, as types fix the application of scientific names.

A **culture indicator** field flags whether a living culture of the fungus has been preserved (e.g., in a culture collection such as ATCC, CBS, or a university repository). When present, the **culture accession number** links the physical specimen record to the corresponding living culture record. Culture data are particularly valuable for phylogenetic studies, bioactive compound screening, and functional ecology research.

## Additional Fields for Type Specimens and Culture Records

For type specimens, additional fields may capture the **protologue citation** (the publication in which the name was originally validly published), the **original name** if the specimen has been subsequently recombined, and any **designation details** explaining how and by whom a lectotype or neotype was designated. For culture records, supplementary fields include the **culture medium** used for isolation, the **storage method** (lyophilized, cryopreserved in liquid nitrogen, under mineral oil), the **viability test date**, and the **DNA sequence accession numbers** from public repositories such as GenBank or UNITE. These extensions bridge the gap between traditional voucher specimens and modern molecular mycology, ensuring that specimen databases serve as comprehensive reference systems for fungal biodiversity.

## Database Architecture and Implementation

Modern fungal specimen databases typically employ relational database management systems (RDBMS) such as PostgreSQL or MySQL, with standardized schemas that support both taxonomic and ecological queries. The database schema is organized around a central **specimen** table linked to subsidiary tables for **taxonomy**, **locality**, **collection-event**, and **genetic-data** records. This normalized structure minimizes data redundancy while enabling complex queries across multiple dimensions of specimen information.

For web-accessible databases, the **Darwin Core** standard (maintained by the Biodiversity Information Standards organization, TDWG) provides a standardized vocabulary for sharing biodiversity data. Darwin Core terms map directly to the specimen fields described above, facilitating data exchange through aggregator platforms such as the Global Biodiversity Information Facility (GBIF) and the MycoPortal. Implementation of Darwin Core ensures that institutional specimen databases are interoperable with global biodiversity networks.

Version control and audit trails are essential for maintaining data integrity in specimen databases. Each record modification should be logged with the modifier's identity, timestamp, and reason for change. This is particularly important for taxonomic revisions, where species names may change as systematic research advances, and for georeferencing updates that improve coordinate accuracy for older collections.

## Quality Assurance and Data Validation

Maintaining data quality in specimen databases requires systematic validation procedures. **Range checks** verify that numeric fields fall within plausible bounds — for example, elevation values between -500m and 8,848m, or latitude values between -90° and +90°. **Format checks** ensure that dates follow ISO 8601, coordinates use decimal degrees, and taxonomic names are properly formatted with correct capitalization and author citation syntax.

**Referential integrity constraints** prevent orphaned records — a specimen cannot reference a taxon that does not exist in the taxonomy table, and a collection event cannot reference a collector who is not in the personnel table. These constraints are enforced at the database level through foreign key relationships and trigger functions that validate data before committing changes.

Regular **data audits** compare specimen records against external authority files such as Index Fungorum, MycoBank, and GBIF to identify mismatches in taxonomic names, geographic coordinates, or collector information. Automated scripts can flag records that fail validation for manual review by curatorial staff, ensuring continuous improvement of database quality over time.

The integration of [[fungal-biodiversity-discovery]] approaches with specimen database systems has become increasingly important as environmental DNA (eDNA) methods generate biodiversity records that complement traditional vouchered specimens.

## Relevance to Cultivation Research

Well-structured specimen databases support [[mushroom-cultivation]] research by providing access to provenance data for commercially important strains. Cultivators can query specimen records to identify wild populations with desirable traits (cold tolerance, substrate preferences, fruiting body morphology) and use this information to guide strain selection for breeding programs. The connection between herbarium voucher data and living culture collections enables traceability from commercial spawn lots back to their original geographic and ecological origins.

## See Also

- [[mycology]]
- [[mycorrhiza]]
- [[basidiomycota]]
- [[ascomycota]]
- [[kingdom-fungi]]
- [[mushroom-cultivation]]
- [[specimen-database-design]]
- [[biodiversity-database-design-fields-tables]]
