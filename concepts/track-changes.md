---
title: Track Changes
tags: [collaboration, word-processing, document-review, microsoft-word]
date: 2026-04-28
updated: 2026-04-28
sources:
  - /Users/t3rpz/wiki/raw/papers/administrator-microsoft-word-fukuoka-textdoc.md
---

# Track Changes

Track Changes (also called "Revision Tracking" or "Redlining") is a
collaborative editing feature in word processing applications, most
prominently [[microsoft-word]], that records modifications to a document so
that reviewers and editors can see what has been altered, by whom, and when.
It is a standard workflow in publishing, legal document review, academic peer
review, and business document collaboration.

## How It Works

When Track Changes is enabled in microsoft word document, the application begins
recording every insertion, deletion, formatting change, and comment as
revisions. Insertions are typically displayed with underlined text in a
designated color, deletions are shown as strikethrough text or in balloons in
the margin, and formatting changes appear in the margin or as highlighted
text. Each revision is tagged with the author's name and a timestamp.

Word stores revision data as annotation markup within the DOCX XML. The
`w:ins` element wraps inserted text, `w:del` wraps deleted text, and
`w:rPrChange` and `w:pPrChange` elements record formatting modifications. Each
revision element includes an `w:author` attribute and an `w:date` attribute.
This means the revision history is embedded directly in the document file and
persists across saves and file transfers.

## Review Workflow

The standard Track Changes workflow involves an author enabling the feature and
circulating the document to one or more reviewers. Each reviewer edits the
document with their changes recorded, optionally adding comments (annotations
not tied to specific text changes). The document author then reviews each
change, accepting or rejecting individual revisions to produce the final
document.

Word provides tools for navigating between revisions, filtering changes by
author or type, and comparing two versions of a document to generate a revision
history even when Track Changes was not originally enabled. The "Compare
Documents" feature creates a legal blackline or redline document showing all
differences between two files, which is essential in contract negotiation and
legal proceedings.

## Security and Privacy Concerns

Track Changes data embedded in DOCX files has been the source of numerous
embarrassing data leaks. Documents shared without accepting or rejecting all
revisions may contain deleted text, author information, and editing timestamps
that are invisible in the default reading view but recoverable by opening the
document with Track Changes visible or by inspecting the raw XML.

Notable incidents include leaked government reports, corporate filings, and
legal documents that revealed earlier drafts, deleted passages, and contributor
identities. In response, organizations have developed document sanitization
procedures that include running Microsoft's Document Inspector, converting to
plain text and back, or using specialized tools to strip revision data before
distribution.

## Beyond Microsoft Word

Track Changes functionality exists in Google Docs, LibreOffice Writer, Apple
Pages, and other word processors, though implementations differ in granularity
and presentation. Google Docs stores revision history server-side and provides
a version history browser, while Word embeds revisions in the document file.
The server-side approach provides a more complete audit trail but requires
network connectivity, whereas the embedded approach works offline but depends
on users managing revision state.

In version control systems like Git, the concept of tracking changes is handled
through diffs and commit history, providing similar functionality for
plain-text and code documents. Tools like `diff` and `patch` serve the same
fundamental purpose for text files that Track Changes serves for rich documents.

## See Also

- [[mollison-designers-access-roads-pathways-and-track-design]]

- [[microsoft-word]] — Primary application with Track Changes
- word processing — Word processor history and comparison
- [[docx]] — Document format storing revision data
- version control — Change tracking in software development
- collaborative editing — Broader topic of real-time document collaboration
