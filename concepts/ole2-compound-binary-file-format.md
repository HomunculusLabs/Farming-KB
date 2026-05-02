---
title: OLE2 Compound Binary File Format
tags: [file-formats, microsoft, binary-formats, data-storage,
      document-architecture]
date: 2026-04-28
updated: 2026-04-28
sources: [/Users/t3rpz/wiki/raw/papers/administrator-[[microsoft-word]]-fukuoka-textdoc.md]
---

# OLE2 Compound Binary File Format

## Overview

The OLE2 Compound Binary File Format (also called CFBF or "Structured Storage")
is a container format developed by Microsoft for storing multiple data streams
within a single physical file. Originally designed for Object Linking and
Embedding (OLE) in the early 1990s, it became the default container for all
Microsoft Office binary formats through version 2003, including `.doc`, `.xls`,
and `.ppt` files.

## Structure

An OLE2 file begins with a 512-byte header containing a magic number
(`0xD0CF11E0A1B11AE1`), version information, and pointers to internal
filesystem structures. The remainder of the file is divided into sectors of
fixed size (typically 512 bytes), organized similarly to a simple filesystem.

### Key Components

**Sector Allocation Table (SAT):** A bitmap-like structure that tracks which
sectors are in use and which are free. The SAT itself can span multiple sectors
for large files, with a dual-SAT (DIFAT) mechanism handling the indirection.

**Directory Entries:** A tree structure stored in directory sectors that
functions like a filesystem directory. Each entry has a name, type (storage,
stream, or root), creation and modification timestamps, and a starting sector
pointer. Storage entries act as directories, and stream entries act as files.

**Streams:** Named sequences of sectors containing the actual data. A Word
document, for example, stores its main text in the "WordDocument" stream and
its formatting tables in a separate "1Table" or "0Table" stream.

### Mini Stream

For small data streams (under 4096 bytes by default), OLE2 uses a "mini
stream" within the root storage entry's data, managed by a separate Mini
Sector Allocation Table (MSAT). This optimization avoids wasting an entire
512-byte sector for data that might be only a few dozen bytes.

## Usage in Microsoft Office

Microsoft Word `.doc` files use OLE2 as their container, with the actual
Word Binary File Format living inside the "WordDocument" stream. Supporting
streams hold tables for text formatting, the piece table (which maps logical
document positions to physical stream positions), and embedded OLE objects.

Excel `.xls` files similarly store workbook data, sheet metadata, and shared
string tables as named streams within an OLE2 container.

## Limitations and Decline

The OLE2 format has several limitations that drove its replacement by OOXML's
ZIP-based approach. Maximum file sizes are constrained by the sector-based
addressing scheme. The format lacks built-in compression, resulting in larger
files than modern alternatives. Recovery from corruption is difficult because
damage to the SAT or directory sectors can make the entire file unreadable.

## Parsing and Tools

The `olefile` Python library provides read-only access to OLE2 files. Microsoft's
own structured storage APIs (available through COM/OLE) offer full read-write
access. The format is documented in Microsoft's Open Specification Promise,
making it one of the better-documented legacy binary formats.

## Security and Forensic Relevance
OLE2 files have been a persistent vector for malware delivery because the
complex binary structure makes targeted inspection difficult. Macro viruses
embedded in Word `.doc` files exploited the OLE2 container's support for
executable code streams throughout the 1990s and 2000s. In digital forensics,
OLE2 metadata — including creation timestamps, author fields stored in
directory entries, and embedded object relationships — provides valuable
evidence even when document content has been modified or deleted. Forensic
tools such as `oleid` and `OleFileIO_PL` are commonly used to extract this
metadata for investigation.

## See Also

- [[microsoft-word-document-format-history]]
- [[office-open-xml]]
- [[binary-document-format-reverse-engineering]]
