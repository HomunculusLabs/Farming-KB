---
title: WYSIWYG Editor
tags: [text-editor, user-interface, document-authoring, web-development]
date: 2026-04-28
updated: 2026-04-28
sources:
  - /Users/t3rpz/wiki/raw/papers/administrator-microsoft-word-fukuoka-textdoc.md
---

# WYSIWYG Editor

WYSIWYG (pronounced "wiz-ee-wig") stands for "What You See Is What You Get." A
WYSIWYG editor is a document or content editing interface that presents users
with a rendering of the final output during the editing process, allowing them
to manipulate content visually rather than through markup or code. WYSIWYG
editors are central to word processing applications like [[microsoft-word]],
web content management systems, email clients, and design tools.

## Origins and History

The concept of on-screen document preview dates to the early 1970s. The Bravo
editor developed at Xerox PARC (1974) is widely considered the first WYSIWYG
text editor, displaying formatted text on a bitmap display that closely matched
the output of a Xerox laser printer. Charles Simonyi, one of Bravo's creators,
later brought the WYSIWYG paradigm to Microsoft, where it became a defining
feature of Word.

The Apple Macintosh (1984) popularized WYSIWYG editing for personal computing,
with MacWrite and MacPaint demonstrating that visual editing could be intuitive
for non-technical users. Microsoft Word for Macintosh (1985) and later Word for
Windows (1989) brought WYSIWYG word processing to the broader PC market,
contributing significantly to Word's eventual dominance over markup-based
competitors like WordPerfect.

## Implementation Approaches

WYSIWYG editors use several underlying rendering strategies. Desktop
applications like Word maintain an internal document model (a tree of elements
representing paragraphs, runs, tables, etc.) that is rendered to screen using
platform graphics APIs. The rendering engine handles layout calculations
including text wrapping, pagination, column flow, and floating element
positioning.

Web-based WYSIWYG editors typically work by making a `contenteditable` HTML
element editable and manipulating the DOM directly in response to user actions.
Libraries like TinyMCE, CKEditor, Quill, and ProseMirror provide abstraction
layers over `contenteditable` that handle cross-browser inconsistencies and
provide richer editing models. A fundamental challenge of web WYSIWYG editors
is the mismatch between the flat HTML model and the structured content models
that applications require.

## The "Lies" Problem

A well-known critique of WYSIWYG editors is that they are never truly WYSIWYG.
The output medium (printed page, web browser, mobile device, PDF) inevitably
differs from the editing viewport in resolution, font availability, color
space, layout engine, and rendering behavior. This gap between the editing
experience and the final output has been humorously described by the acronym
WYSIAYG ("What You See Is All You Get") or WYSIWYGMOF ("What You See Is What
You Get — Maybe On a Good Day").

The rise of responsive web design exacerbated this problem, as a single HTML
document renders differently across screen sizes. Modern editors address this
with preview modes, device-frame simulations, and adaptive editing interfaces
that show content in multiple viewport configurations simultaneously.

## WYSIWYG vs. Markup Editing

The tension between WYSIWYG and markup-based editing (e.g., markdown,
latex, HTML source editing) is a persistent debate in document authoring.
WYSIWYG proponents argue that visual editing lowers barriers to entry and
enables non-technical users to produce formatted content. Markup proponents
argue that direct access to source provides precision, reproducibility, version
control friendliness, and separation of content from presentation.

Hybrid approaches have emerged as a practical compromise. Many modern editors
provide both WYSIWYG and source modes, split-pane views, or "block editors"
that combine visual manipulation with structured content models. Notion,
Ghost, and craft are examples of editors that blend WYSIWYG editing with
structured, non-HTML content models.

## See Also

- [[williams-pdc-electricity-in-permaculture]]
- [[query-how-do-i-make-jadam-natural-pesticide-jnp]]
- [[homestead-scale-assessment]]
- [[geoff-hamilton-organic-techniques]]
- [[luther-burbank-plant-breeding-methods]]

- word processing — History of word processors and WYSIWYG evolution
- [[microsoft-word]] — The most widely used WYSIWYG word processor
- markdown — Lightweight markup language alternative to WYSIWYG
- latex — Markup-based academic document preparation
- rich text editor — Web-based rich text editing libraries and approaches
