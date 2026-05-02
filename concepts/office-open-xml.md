---
title: Office Open XML
tags: [file-format, xml, microsoft, standards, document-format]
date: 2026-04-28
updated: 2026-04-28
sources:
  - /Users/t3rpz/wiki/raw/papers/administrator-microsoft-word-fukuoka-textdoc.md
---

# Office Open XML

Office Open XML (OOXML) is a zipped, XML-based file format developed by
Microsoft for representing spreadsheets, charts, presentations, and word
processing documents. Standardized as ECMA-376 and later ISO/IEC 29500, OOXML
is the default format for Microsoft Office 2007 and later applications. Files
use the `.docx`, `.xlsx`, and `.pptx` extensions, where the trailing "x"
denotes the XML-based format replacing the legacy binary `.doc`, `.xls`, and
`.ppt` formats.

## Format Structure

An OOXML file is a ZIP archive containing a collection of XML parts organized
in a specific directory structure. The archive always includes a
`[Content_Types].xml` file at its root that maps file extensions to MIME types,
defining how each part should be interpreted. Relationships between parts are
described in `.rels` XML files that form a directed graph connecting the
document's components.

For a `.docx` Word document, the primary content resides in `word/document.xml`,
which uses a rich vocabulary of XML elements to represent paragraphs, runs of
formatted text, tables, images, and other document structures. Styles are
defined in `word/styles.xml`, and document properties such as author, title,
and revision history are stored in `docProps/core.xml` and `docProps/app.xml`.

The format supports embedded media (images, audio, video) stored directly in
the ZIP archive and referenced by relationships, as well as embedded OLE
objects and custom XML parts for application-specific data.

## Standardization History

Microsoft submitted OOXML to ECMA International for standardization in 2005,
resulting in ECMA-376 (published in December 2006). The subsequent submission
to ISO/IEC for fast-track approval became one of the most controversial
standardization processes in technology history. Critics argued that the
specification was incomplete, contained proprietary extensions, and overlapped
with the existing ISO 26300 standard for the OpenDocument Format (ODF).

After multiple ballot resolutions and extensive technical revisions, ISO/IEC
29500 was approved in April 2008. The standard exists in two variants: the
Transitional variant, which maintains backward compatibility with legacy
Microsoft Office features, and the Strict variant, which is a cleaner
specification without legacy baggage. Most implementations target the
Transitional variant.

## Technical Details

The XML markup in OOXML documents can be verbose, with simple formatting like
bold text requiring multiple nested XML elements. This verbosity, combined with
ZIP compression, means that OOXML files can sometimes be larger or smaller than
equivalent binary format files depending on the content type. Text-heavy
documents compress well, while documents with many embedded images see less
benefit.

A notable feature of OOXML is its support for custom XML markup parts, which
allow organizations to embed domain-specific structured data within documents.
This capability enables document-centric workflows where the same file serves as
both a human-readable document and a machine-readable data source, which is
valuable in legal, financial, and regulatory contexts.

## Interoperability and Compatibility

Multiple implementations of OOXML exist beyond Microsoft Office, including
LibreOffice, Google Docs, Apple iWork, and Apache POI (a Java library for
reading and writing OOXML files). However, perfect fidelity across
implementations remains challenging due to the specification's enormous size
(approximately 6,000 pages) and the many optional features and legacy
compatibility modes.

The Open Document Format (ODF), standardized as ISO 26300, remains the primary
alternative and is mandated by several governments as a document exchange
standard. The ongoing coexistence of OOXML and ODF has driven the development
of format conversion tools and the open standards movement in government IT
procurement.

## See Also

- [[docx]] — The Word-specific OOXML format
- open standards — The movement for open document standards
- xml — Extensible Markup Language fundamentals
- [[ole2-compound-binary-file-format]] — File format concepts and comparison
- [[microsoft-word]] — The primary application using OOXML
