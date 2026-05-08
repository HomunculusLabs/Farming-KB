#!/usr/bin/env python3
"""
Wiki Source Processor — Watches ~/wiki/raw/staging/ for new files,
extracts text, and moves them to ~/wiki/raw/papers/ as markdown.

Supports:
  - PDF (text-based via pymupdf, scanned via marker-pdf)
  - EPUB (via ebooklib)
  - DOCX (via python-docx)
  - Markdown (copied directly)

Usage:
  python3 process_staging.py              # Process all files in staging
  python3 process_staging.py --watch      # Watch mode (poll every 30s)
  python3 process_staging.py --dry-run    # Show what would be processed

Drop files in ~/wiki/raw/staging/ and they'll be auto-processed.
Processed files move to ~/wiki/raw/staging/processed/
Failed files move to ~/wiki/raw/staging/failed/
"""

import os
import sys
import shutil
import subprocess
import time
import re
from pathlib import Path

STAGING = Path(os.path.expanduser("~/wiki/raw/staging"))
PROCESSED = STAGING / "processed"
FAILED = STAGING / "failed"
OUTPUT = Path(os.path.expanduser("~/wiki/raw/papers"))
MARKER_BIN = os.path.expanduser("~/Library/Python/3.9/bin/marker_single")

# Extensions we handle
PDF_EXT = {'.pdf'}
EPUB_EXT = {'.epub'}
DOCX_EXT = {'.docx', '.doc'}
MD_EXT = {'.md', '.markdown', '.txt'}
ALL_EXT = PDF_EXT | EPUB_EXT | DOCX_EXT | MD_EXT


def slugify(name: str) -> str:
    """Convert filename to wiki-safe slug."""
    name = name.lower()
    name = re.sub(r'[^a-z0-9]+', '-', name)
    name = re.sub(r'-+', '-', name)
    name = name.strip('-')
    return name[:200]


def sanitize_frontmatter(text: str) -> str:
    """Remove any YAML frontmatter from extracted text."""
    lines = text.split('\n')
    if lines and lines[0].strip() == '---':
        # Find closing ---
        for i, line in enumerate(lines[1:], 1):
            if line.strip() == '---':
                return '\n'.join(lines[i+1:])
    return text


def process_pdf_text(filepath: Path) -> str:
    """Extract text from text-based PDF using pymupdf."""
    import pymupdf4llm
    md_text = pymupdf4llm.to_markdown(str(filepath), page_chunks=True)
    return md_text if md_text else ""


def process_pdf_scanned(filepath: Path) -> str:
    """Extract text from scanned PDF using marker-pdf (OCR)."""
    import tempfile
    with tempfile.TemporaryDirectory() as tmpdir:
        result = subprocess.run(
            [sys.executable, MARKER_BIN, str(filepath), "--output_dir", tmpdir],
            capture_output=True, text=True, timeout=600
        )
        if result.returncode != 0:
            # Try with the marker module directly
            try:
                from marker.convert import convert_single_pdf
                from marker.models import load_all_models
                md_text = convert_single_pdf(str(filepath), model_list=load_all_models())
                return md_text.text if hasattr(md_text, 'text') else str(md_text)
            except Exception as e:
                raise RuntimeError(f"marker failed: {result.stderr[:500]}\nModule error: {e}")
        
        # Find the output markdown file
        for f in Path(tmpdir).rglob("*.md"):
            return f.read_text(encoding='utf-8', errors='replace')
    
    raise RuntimeError("marker produced no output")


def process_pdf(filepath: Path) -> str:
    """Try pymupdf first, fall back to marker if output is too short."""
    # Try pymupdf first (fast)
    text = process_pdf_text(filepath)
    
    # If we got reasonable content, use it
    if len(text.strip()) > 500:
        return text
    
    # Short output = probably scanned PDF, use marker OCR
    print(f"  Short text output ({len(text)} chars), trying OCR with marker-pdf...")
    try:
        ocr_text = process_pdf_scanned(filepath)
        if len(ocr_text.strip()) > 100:
            return ocr_text
    except Exception as e:
        print(f"  OCR failed: {e}")
    
    # Return whatever pymupdf gave us
    return text


def process_epub(filepath: Path) -> str:
    """Extract text from EPUB."""
    import ebooklib
    from ebooklib import epub
    from html.parser import HTMLParser
    
    class HTMLStripper(HTMLParser):
        def __init__(self):
            super().__init__()
            self.text = []
        def handle_data(self, data):
            self.text.append(data)
        def get_text(self):
            return '\n'.join(self.text)
    
    book = epub.read_epub(str(filepath))
    chapters = []
    for item in book.get_items_of_type(ebooklib.ITEM_DOCUMENT):
        content = item.get_content().decode('utf-8', errors='replace')
        stripper = HTMLStripper()
        stripper.feed(content)
        text = stripper.get_text().strip()
        if text:
            chapters.append(text)
    
    return '\n\n---\n\n'.join(chapters)


def process_docx(filepath: Path) -> str:
    """Extract text from DOCX."""
    from docx import Document
    doc = Document(str(filepath))
    paragraphs = [p.text for p in doc.paragraphs if p.text.strip()]
    return '\n\n'.join(paragraphs)


def process_markdown(filepath: Path) -> str:
    """Just read and return markdown/txt files."""
    return filepath.read_text(encoding='utf-8', errors='replace')


def process_file(filepath: Path) -> tuple[bool, str]:
    """Process a single file. Returns (success, message)."""
    ext = filepath.suffix.lower()
    
    try:
        if ext in MD_EXT:
            text = process_markdown(filepath)
        elif ext in DOCX_EXT:
            print(f"  Extracting DOCX...")
            text = process_docx(filepath)
        elif ext in EPUB_EXT:
            print(f"  Extracting EPUB...")
            text = process_epub(filepath)
        elif ext in PDF_EXT:
            print(f"  Extracting PDF...")
            text = process_pdf(filepath)
        else:
            return False, f"Unsupported extension: {ext}"
        
        if not text or len(text.strip()) < 50:
            return False, f"Extraction too short: {len(text)} chars"
        
        # Clean up
        text = sanitize_frontmatter(text)
        text = text.strip()
        
        # Generate output filename
        stem = filepath.stem
        slug = slugify(stem)
        out_path = OUTPUT / f"{slug}.md"
        
        # Handle collisions
        counter = 1
        while out_path.exists():
            out_path = OUTPUT / f"{slug}-{counter}.md"
            counter += 1
        
        # Write
        out_path.write_text(text, encoding='utf-8')
        size_kb = len(text) / 1024
        
        return True, f"OK -> {out_path.name} ({size_kb:.0f}KB, {text.count(chr(10))} lines)"
    
    except Exception as e:
        return False, f"Error: {e}"


def main():
    dry_run = '--dry-run' in sys.argv
    watch_mode = '--watch' in sys.argv
    
    if watch_mode:
        print(f"Watching {STAGING}/ for new files (poll every 30s)...")
        print(f"Drop PDFs, EPUBs, DOCX, or MD files in {STAGING}/")
        print(f"Output goes to {OUTPUT}/")
        print(f"Press Ctrl+C to stop\n")
    
    while True:
        # Find files to process
        files = []
        for f in STAGING.iterdir():
            if f.is_file() and f.suffix.lower() in ALL_EXT:
                files.append(f)
        
        if not files:
            if watch_mode:
                time.sleep(30)
                continue
            else:
                print("No files to process in staging.")
                return
        
        files.sort(key=lambda f: f.name.lower())
        print(f"\nFound {len(files)} file(s) to process:")
        
        for f in files:
            ext = f.suffix.lower()
            size_mb = f.stat().st_size / (1024 * 1024)
            print(f"\n  [{ext.upper()}] {f.name} ({size_mb:.1f}MB)")
            
            if dry_run:
                print(f"  (dry-run: would process)")
                continue
            
            success, msg = process_file(f)
            print(f"  {msg}")
            
            # Move to processed or failed
            dest = PROCESSED if success else FAILED
            shutil.move(str(f), dest / f.name)
            print(f"  Moved to {dest.name}/")
        
        if not watch_mode:
            print(f"\nDone. Processed {len(files)} file(s).")
            return


if __name__ == '__main__':
    main()
