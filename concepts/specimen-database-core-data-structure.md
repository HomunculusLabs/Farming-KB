---
title: Core Data Structure for a Fungal Specimen Database
source: unknown-biodiversity-of-fungi.md
type: concept
---

## Core Data Structure for a Fungal Specimen Database

## Overview

A fungal specimen database is built around a **core specimen data record** that captures the essential "what, who, when, and where" information for each biodiversity observation. This record serves as a **voucher** — a verifiable, physically preserved reference specimen deposited in a recognized collection.

The core data structure fulfills three critical functions:

1. **Exchange Format** — Enables standardized data sharing between institutions, databases, and research networks via a common schema.
2. **Communication Framework** — Establishes a shared vocabulary and field structure so mycologists and curators can unambiguously transmit specimen information.
3. **Storage Structure** — Defines the logical organization of data, ensuring consistency, queryability, and long-term integrity.

---

## Taxonomic Name Fields

| Field | Max Size | Description |
|---|---|---|
| **Genus** | 26 chars | Generic name of the fungus |
| **Species** | 32 chars | Specific epithet |
| **Rank** | 6 chars | Infraspecific rank (e.g., var., f., subsp.) |
| **Subspecific Epithet** | 32 chars | Infraspecific epithet |
| **Author** | 100 chars | Author(s) who validly published the name |

### Name Standards

Scientific names should follow established references: **Farr et al. (1979, 1986)**, the **Index of Fungi**, **Greuter et al. (1993, 2000)** (ICBN editions), and **Brummitt and Powell (1992)** (author abbreviations).

### Author Field Conventions

Per the **International Code of Botanical Nomenclature**, when a name has more than two authors, use **"et al."** after the first author. For one or two authors, list all using standardized abbreviations.

---

## Determiner Fields

| Field | Max Size | Description |
|---|---|---|
| **Determiner Name** | 55 chars | Person who identified the specimen |
| **Determination Date** | 11 chars | Date of determination (YYYY-MM-DD) |

---

## Locality Data

| Field | Required | Description |
|---|---|---|
| **Country** | **Yes** | Full country name (ISO preferred) |
| **Country Subdivision 1** | No | First-level division (state, province) |
| **Country Subdivision 2** | No | Second-level division (county, district) |
| **Country Place Name** | No | Nearest named place on a map |
| **Locality** | No | Free-text, up to **250 chars**, with site-specific details |

The **Locality** field is the primary narrative description and should allow relocation of the general collection area.

---

## Elevation

Elevation is recorded as a range: **Elevation 1** (lower bound) and **Elevation 2** (upper bound). **Elevation Source** records how it was determined (GPS, topographic map). **Elevation Unit** is **f** (feet) or **m** (meters).

---

## Geographic Coordinates

- **Latitude** and **Longitude** in **decimal degrees**.
- **Sign convention**: N positive / S negative for latitude; E positive / W negative for longitude.
- **Coordinate Source** indicates how coordinates were obtained (GPS, georeferencing, map interpolation).

---

## Collector Fields

| Field | Description |
|---|---|
| **Collector Name** | Primary collector, formatted as **Last, First** |
| **Team Collectors** | Additional team members |
| **Collector Number** | Unique field number assigned by the collector |
| **Submitter** | Person who submitted the record to the database |

The Collector Number + collector name uniquely identifies the field collection event.

---

## Collector Dates

- **Collection Date** in **YYYYMMDD** or **YYYY-MM-DD** format.
- **Date Range** for multi-day collections (start and end dates).
- **Season** — seasonal descriptor (spring, summer, autumn, winter, rainy season).

---

## Details of Collection

### Substratum

**Required field.** If unknown, enter **"unknown"** explicitly — never leave blank. Describes the material the fungus was collected from (soil, wood, leaf litter, dung, living tissue).

### Habitat

Free-text, up to **250 characters**. Describes the broader ecological context: forest type, wetland, grassland, disturbance regime, etc.

### Host Fields

For host-associated fungi: **Host Genus**, **Host Species**, **Host Rank**, **Host Subspecific Epithet**, **Host Common Name**, and **Hybrid Notation** (e.g., × for hybrid hosts).

---

## Housekeeping Fields

| Field | Description |
|---|---|
| **Herbarium Number** | Accession number using **Index Herbariorum** codes (e.g., BPI, NY, K) |
| **Type Status** | Nomenclatural type: **HO** (holotype), **IS** (isotype), or others (paratype, neotype, lectotype, epitype) |
| **Culture Indicator** | Flag for living culture maintenance |

The Herbarium Number links the digital record to the physical voucher specimen.

---

## Additional Fields: Type and Culture Data

A key design decision is whether type and culture data reside in the main specimen table or in **separate relational tables**.

**Separate tables are recommended** for institution-level databases because:
- A specimen may have multiple cultures across different collections.
- Type status may be revised, requiring an audit trail.
- One-to-many relationships (one specimen → many cultures/annotations) are better normalized.
- The core table retains summary flags (Type Status, Culture Indicator) for quick filtering, while detail tables hold full records.

---

## Summary

The core data structure provides a standardized framework for recording fungal voucher specimens. By capturing taxonomic identity, geographic origin, collecting event details, host associations, and curatorial metadata in well-defined fields with consistent formatting, it enables reliable data exchange, supports biodiversity research, and ensures each record serves as a trustworthy reference for mycological science.

## See Also

- [[mycology]]
- [[mycorrhiza]]
- [[basidiomycota]]
- [[ascomycota]]
- [[kingdom-fungi]]
