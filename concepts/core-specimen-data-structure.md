---
title: Core Specimen Data Structure
source: unknown-biodiversity-of-fungi.md
type: concept
---

# Core Specimen Data Structure

A standardized data structure for fungal specimen databases, designed to capture
taxonomic identification, geographic provenance, collection metadata, and
housekeeping information. The design separates concerns into discrete field
groups and distinguishes between **identification events** and **collecting
events**, since a specimen may be re-identified multiple times by different
determiners over its lifetime.

## Design Philosophy: Event-Based Tables

The core table design is built around the concept of **events**:

- **Identification events** — each time a specimen is examined and a name
  applied (or revised), a new identification-event row is created. This
  preserves the full history of taxonomic opinions attached to a single
  physical specimen.
- **Collecting events** — the single act of field collection that produced the
  specimen. One collecting event can yield multiple specimens (e.g., duplicate
  sheets, cultures, DNA extractions).

Separating these events prevents data redundancy and correctly models the
many-to-one relationship between determinations and a collected specimen.

## Taxonomic Name Fields

| Field | Size / Format | Standard / Notes |
|---|---|---|
| **Genus** | 255 chars, text | Latin name, first letter capitalised; follows ICN |
| **Species** | 255 chars, text | Specific epithet, all lowercase; may include
"sp.", "spp.", or "cf." |
| **Rank** | 50 chars, controlled vocabulary | e.g., species, subspecies, variety, form, `×` (hybrid);
governs interpretation of Subspecific Epithet |
| **Subspecific Epithet** | 255 chars, text | Infraspecific epithet; used only when Rank ≠ species |
| **Author** | 255 chars, text | Basionym author citation (e.g., "(Fr.) P. Karst.");
standardised per **Authors of Fungal Names** ( Kirk & Ansell 2008) |

## Determiner Fields

| Field | Size / Format | Standard / Notes |
|---|---|---|
| **Determiner** | 255 chars, text | Name of the person who identified the specimen;
standardised format: `Surname, Initials` |
| **Determination Date** | Date (ISO 8601) | Date the identification was made; `YYYY-MM-DD` or
partial (year, year-month) |

A specimen may have multiple determiner records (see identification events above).
Each record links to the specimen's primary key, enabling a full annotation
history.

## Locality Data Fields

| Field | Size / Format | Standard / Notes |
|---|---|---|
| **Country** | 255 chars, text | Full country name; preferably ISO 3166-1 country
name (not the 2-letter code) |
| **Country Subdivision 1** | 255 chars, text | First-level administrative division (state, province,
prefecture); ISO 3166-2 code recommended |
| **Country Subdivision 2** | 255 chars, text | Second-level subdivision (county, district,
municipality) |
| **Country Place Name** | 255 chars, text | Named locality on a map (town, reserve, mountain);
verbatim from label |
| **Locality** | Text (unlimited) | Free-text description of the specific collection site;
as precise as possible |
| **Elevation1** | Numeric (float) | Lower elevation boundary in metres (or selected unit) |
| **Elevation2** | Numeric (float) | Upper elevation boundary; when equal to Elevation1,
indicates a point estimate |
| **Elevation Source** | 100 chars, text | Method of determination: `GPS`, `map`, `altimeter`,
`estimated` |
| **Elevation Unit** | 20 chars, controlled vocabulary | `m` (metres), `ft` (feet) |
| **Latitude** | Decimal degrees (float) | WGS 84 datum; negative for Southern Hemisphere |
| **Longitude** | Decimal degrees (float) | WGS 84 datum; negative for Western Hemisphere |
| **Lat-Long Source** | 100 chars, text | Provenance of coordinates: `GPS`, `georeferenced`,
`estimated`, `unknown` |

## Collector Data Fields

| Field | Size / Format | Standard / Notes |
|---|---|---|
| **Collector** | 255 chars, text | Primary collector name; format: `Surname, Initials` |
| **Team Collectors** | Text (unlimited) | Additional collectors in the field party; one name
per line or semicolon-delimited |
| **Collector Number** | 100 chars, text | Unique number assigned by the collector in the field |
| **Submitter** | 255 chars, text | Person who submitted the specimen to the herbarium
(if different from collector) |
| **Collector Date1** | Date (ISO 8601) | Start date of collection; supports partial dates |
| **Collector Date2** | Date (ISO 8601) | End date (for multi-day forays); null if single-day |
| **Season** | 50 chars, text | Season of collection where exact date is unavailable
(e.g., `autumn`, `wet season`) |

## Collection Details

| Field | Size / Format | Standard / Notes |
|---|---|---|
| **Substratum** | Text (unlimited) | Material the fungus was growing on (e.g., `soil`,
`decaying wood of Quercus robur`, `leaf litter`) |
| **Habitat** | Text (unlimited) | Broader ecological context (e.g., `temperate
rainforest`, `mixed woodland`, `alpine meadow`) |
| **Host Genus** | 255 chars, text | Genus of the host organism (if parasitic or
symbiotic) |
| **Host Species** | 255 chars, text | Species of the host |
| **Host Rank** | 50 chars, controlled vocabulary | Taxonomic rank of the host identification |
| **Host Subspecific Epithet** | 255 chars, text | Infraspecific epithet of the host, if applicable |
| **Host Common Name** | 255 chars, text | Vernacular name of the host |
| **Hybrid Notation** | 20 chars, controlled vocabulary | Indicates host is a hybrid: `×` or `notho-` prefix
(× is the standard hybrid sign) |

## Housekeeping Fields

| Field | Size / Format | Standard / Notes |
|---|---|---|
| **Herbarium Number** | 100 chars, text | Composite identifier: `INDEX-HOLONYMUS-CODE +
accession number` (e.g., `BPI 123456`); codes follow
**Index Herbariorum** (Thiers, continuously updated) |

The Index Herbariorum code is the internationally recognised abbreviation for
the herbarium holding the specimen. Every herbarium should be registered in
Index Herbariorum, and the code ensures unambiguous global identification of the
custodial institution.

## Additional Fields

| Field | Size / Format | Standard / Notes |
|---|---|---|
| **Type Status** | 100 chars, controlled vocabulary | Indicates nomenclatural type designation:
`holotype`, `isotype`, `paratype`, `lectotype`,
`neotype`, `epitype`, `syntype`, `not a type` |
| **Culture** | Boolean / 20 chars | Whether a living culture was derived from the
specimen: `yes` / `no`; if yes, cross-reference to
the culture collection accession number |

## Key References

- **Authors of Fungal Names** — Kirk, P.M. & Ansell, A.E. (2008). Authors of
  Fungal Names. CABI.
- **Index Herbariorum** — Thiers, B. (continuously updated). New York Botanical
  Garden. http://sweetgum.nybg.org/ih/
## See Also

- [[mycorrhiza]]
- [[basidiomycota]]
- [[ascomycota]]
- [[kingdom-fungi]]
- [[mushroom-identification]]
