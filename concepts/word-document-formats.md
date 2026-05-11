---
title: Word Document Formats
created: 2026-04-28
tags:
  - microsoft-word
  - document-formats
  - file-formats
  - xml
  - interoperability
date: 2026-04-28
updated: 2026-04-28
sources:
  - /Users/t3rpz/wiki/raw/papers/administrator-microsoft-word-fukuoka-textdoc.md
type: concept
---

# Word Document Formats

[[microsoft-word]] has used several document formats throughout its history, each
reflecting the technological constraints and design philosophies of its era. The
evolution of these formats mirrors broader shifts in software architecture, from
proprietary binary formats to open, XML-based standards.

## Binary .doc Format

The classic .doc format was a proprietary binary format used from Word 2.0
through Word 2003. Internally, it used the OLE2 Compound Binary File Format (also
known as OLE Structured Storage), which allowed multiple data streams, such as
document text, formatting, embedded objects, and metadata, to be stored within a
single file. The binary format was efficient for its time but posed significant
challenges for interoperability. Reverse-engineering efforts by projects like
Apache POI and LibreOffice were necessary to enable third-party applications to
read and write .doc files reliably.

The binary format stored text as a sequence of characters with inline formatting
codes interleaved. A separate "Word Document" stream contained the main text,
while additional streams held formatting information (the "1Table" or "0Table"
stream), revision tracking data, and embedded OLE objects. The format evolved
through many versions (Word 2.0 through Word 97-2003), each adding features
that expanded the specification. The final binary format version, used by
Word 97 through Word 2003, became the most widely documented through
Microsoft's limited disclosure and reverse-engineering. Maximum file size for
.doc files was theoretically 512 MB, though practical limits were much lower
due to memory constraints of the applications. The format did not use Unicode
internally in early versions, which caused character encoding issues across
different language versions of Word.

## Office Open XML (.docx)

Word 2007 introduced the Office Open XML (OOXML) format, which became the
default save format. A .docx file is actually a ZIP archive containing multiple
XML files organized in a standard directory structure. The main document content
resides in word/document.xml, while styles, numbering, fonts, and settings each
have their own XML files. The format is documented in ISO/IEC 29500, making it
an open standard. This structure enables easier programmatic manipulation of
documents, as tools can work with individual XML components rather than parsing
a monolithic binary file.

Inside the ZIP archive, a .docx file follows a consistent directory layout.
The [Content_Types].xml file at the root [[maps]] file extensions to MIME types.
The _rels/ directory contains relationship files that define how parts
reference each other. The word/ directory contains the core document parts:
document.xml holds the main body text, styles.xml defines paragraph and
character styles, numbering.xml configures list numbering schemes, and
settings.xml stores application preferences. The word/media/ subdirectory
holds embedded images, while word/_rels/document.xml.rels maps content
references. Headers and footers are stored as separate XML files (header1.xml,
footer1.xml, etc.) in the word/ directory. The format also supports embedded
fonts, custom XML properties, and document parts for comments, revisions, and
bibliography data.

A .docm file uses the same structure as .docx but can contain VBA macros,
with the macro code stored in word/vbaProject.bin. The .dotx and .dotm
extensions serve as template formats corresponding to .docx and .docm
respectively. Strict Open XML documents (conforming to ISO/IEC 29500:2008
rather than the transitional variant) use a slightly different namespace
scheme and offer improved interoperability guarantees, though they are less
commonly produced by Word itself.

## Rich Text Format (.rtf)

Rich Text Format was developed by Microsoft in 1987 as a cross-platform
interchange format. RTF files use plain text with embedded formatting codes,
making them readable in any text editor while preserving basic formatting when
opened in a word processor. RTF served as a lingua franca for document exchange
before XML-based formats became prevalent. Although RTF support has been
maintained in Word and other applications, its capabilities are more limited
than .docx, particularly for complex layouts and embedded media.

## Other Supported Formats

## See Also
- [[microsoft-word-document-format-history]]
- [[microsoft-word-document-format]]
- [[fukuoka-document-processing-research]]
- [[document-automation-administration]]
- [[document-interoperability-standards]]
