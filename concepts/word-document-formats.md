---
title: word document formats
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
---

# Word Document Formats

Microsoft Word has used several document formats throughout its history, each
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
The [Content_Types].xml file at the root maps file extensions to MIME types.
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

Word supports importing and exporting a variety of formats including HTML,
plain text (.txt), OpenDocument Format (.odt used by LibreOffice), PDF, and
XPS. PDF export was natively added in Word 2007 with a downloadable plugin and
became built-in from Word 2010 onward. The ability to save directly to PDF
significantly reduced the reliance on separate PDF creation tools. Word also
supports the older WordPerfect format (.wpd) and various international text
encoding standards.

## Format Compatibility Challenges

Despite the move to open standards, format compatibility remains a concern. The
OOXML specification is extensive (over 6,000 pages), and Microsoft's
implementation has at times included features not fully documented in the
standard. This has led to formatting discrepancies when opening .docx files
in non-Microsoft applications. Page layout, font rendering, and complex
features like tracked changes and conditional formatting can differ between
Word and competing applications. The OpenDocument Format (ODF), standardized
as ISO/IEC 26300, offers an alternative open standard that some governments
and organizations have adopted by policy.

Compatibility mode in Word deserves special attention. When a .doc file is
opened in Word 2007 or later, Word enters "Compatibility Mode," which
disables features introduced after Word 2003 and displays the mode in the
document title bar. Documents created in Compatibility Mode use the older
layout engine, which can produce different line breaks, pagination, and
spacing compared to native .docx mode. Key differences include the handling
of paragraph spacing, table layout algorithms, font fallback behavior, and
the rendering of floating objects and text wrapping. Converting a document
from Compatibility Mode to full .docx mode can cause reflow that changes
page count, particularly in long documents with complex formatting.

Format conversion between .docx and other formats is handled by built-in
converters in Word and by third-party libraries. Word's built-in PDF export
uses a high-fidelity rendering engine that maps OOXML formatting to PDF
structures, though complex layouts involving floating objects and automatic
numbering can sometimes produce unexpected results. Converting to ODF
(.odt) loses some features that lack ODF equivalents, such as certain
content controls, XML mapping panes, and SmartArt graphics. The reverse
conversion (ODF to OOXML) also involves compromises where formatting models
differ. Online conversion services and libraries like Pandoc provide
additional conversion pathways, particularly for round-tripping between
document formats and lightweight markup languages like Markdown.

## See Also

- [[microsoft-word-document-format]]
- [[microsoft-word-document-format-history]]
- [[document-format-conversion-fidelity]]
- [[japanese-document-processing]]
- [[word-ribbon-interface]]

- [[microsoft-word-history]]
- [[binary-document-format-reverse-engineering]]
- rich text format
- pdf
