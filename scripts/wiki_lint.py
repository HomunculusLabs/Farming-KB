#!/usr/bin/env python3
"""Wiki Link Linter — enforces link hygiene rules across the LLM Wiki.

Rules:
  1. NO SELF-LINKS: [[page-name]] inside page-name.md is a lint error
  2. NO BROKEN LINKS: every [[target]] must exist as a .md file
  3. NO ESCAPED HYPHENS: [[foo\-bar]] is invalid — use [[foo-bar]]
  4. NO MULTILINE LINKS: [[target\nalias]] spanning newlines
  5. NO EMPTY BRACKETS: [[]] with nothing inside
  6. NO SPACES IN LINKS: [[Foo Bar]] must be [[foo-bar]]
  7. MIN OUTGOING LINKS: every page should link to at least 3 others
  8. MIN PAGE SIZE: every page should be at least 80 lines

Usage:
  python3 wiki_lint.py              # check all, report errors
  python3 wiki_lint.py --fix        # auto-fix what we can (rules 1,3,4,5,6)
  python3 wiki_lint.py --fix --self # fix only self-links
  python3 wiki_lint.py --rule 1     # check only rule 1
  python3 wiki_lint.py --json       # machine-readable output
"""

import argparse
import json
import os
import re
import sys
from collections import Counter, defaultdict

WIKI_ROOT = os.path.expanduser("~/wiki")
DIRS = ["concepts", "entities", "comparisons", "queries"]
LINK_RE = re.compile(r'\[\[([^\]|#]+?)(?:\|([^\]]+))?\]\]')
MULTILINE_RE = re.compile(r'\[\[[^\]]*?\n[^\]]*?\]\]')
EMPTY_BRACKET_RE = re.compile(r'\[\[\s*\]\]')
ESCAPED_HYPHEN_RE = re.compile(r'\[\[([^\]]*?\\-[^\]]*?)\]\]')
SPACE_LINK_RE = re.compile(r'\[\[([a-zA-Z0-9][^\]]*?\s+[^\]]*?)\]\]')

RULES = {
    1: "NO SELF-LINKS",
    2: "NO BROKEN LINKS",
    3: "NO ESCAPED HYPHENS",
    4: "NO MULTILINE LINKS",
    5: "NO EMPTY BRACKETS",
    6: "NO SPACES IN LINKS",
    7: "MIN OUTGOING LINKS (3)",
    8: "MIN PAGE SIZE (80 lines)",
}

# --- Collectors ---

def collect_pages():
    """Build page set with dir, lines, and content."""
    pages = {}
    for d in DIRS:
        path = os.path.join(WIKI_ROOT, d)
        if not os.path.exists(path):
            continue
        for f in os.listdir(path):
            if not f.endswith(".md") or f.startswith("index-"):
                continue
            name = f[:-3]
            fp = os.path.join(path, f)
            with open(fp) as fh:
                content = fh.read()
            lines = len(content.split("\n"))
            pages[name] = {"dir": d, "path": fp, "lines": lines, "content": content}
    return pages

def check_self_links(pages):
    errors = []
    for name, info in pages.items():
        for m in LINK_RE.finditer(info["content"]):
            target = m.group(1).strip().replace("\\-", "-")
            if target == name:
                errors.append({
                    "rule": 1,
                    "page": name,
                    "path": info["path"],
                    "msg": f'Self-link: [[{name}]] in {name}.md',
                    "fixable": True,
                })
    return errors

def check_broken_links(pages, all_names):
    errors = []
    for name, info in pages.items():
        for m in LINK_RE.finditer(info["content"]):
            target = m.group(1).strip().replace("\\-", "-")
            if target.startswith("index-"):
                continue
            if target not in all_names:
                errors.append({
                    "rule": 2,
                    "page": name,
                    "path": info["path"],
                    "msg": f'Broken link: [[{target}]] does not exist',
                    "fixable": False,
                })
    return errors

def check_escaped_hyphens(pages):
    errors = []
    for name, info in pages.items():
        for m in ESCAPED_HYPHEN_RE.finditer(info["content"]):
            errors.append({
                "rule": 3,
                "page": name,
                "path": info["path"],
                "msg": f'Escaped hyphen in link: {m.group(0)[:60]}',
                "fixable": True,
            })
    return errors

def check_multiline_links(pages):
    errors = []
    for name, info in pages.items():
        for m in MULTILINE_RE.finditer(info["content"]):
            errors.append({
                "rule": 4,
                "page": name,
                "path": info["path"],
                "msg": f'Multiline wikilink in {name}.md',
                "fixable": True,
            })
    return errors

def check_empty_brackets(pages):
    errors = []
    for name, info in pages.items():
        for m in EMPTY_BRACKET_RE.finditer(info["content"]):
            errors.append({
                "rule": 5,
                "page": name,
                "path": info["path"],
                "msg": f'Empty brackets [[]] in {name}.md',
                "fixable": True,
            })
    return errors

def check_space_links(pages):
    errors = []
    for name, info in pages.items():
        for m in SPACE_LINK_RE.finditer(info["content"]):
            raw = m.group(1)
            # Only flag if it looks like a link target (not piped display text inside [[]])
            # Pipes split target|display, so check the part before |
            target_part = raw.split("|")[0].strip()
            if " " in target_part:
                errors.append({
                    "rule": 6,
                    "page": name,
                    "path": info["path"],
                    "msg": f'Spaces in link: [[{raw[:60]}]]',
                    "fixable": True,
                })
    return errors

def check_min_links(pages):
    errors = []
    for name, info in pages.items():
        outgoing = set()
        for m in LINK_RE.finditer(info["content"]):
            target = m.group(1).strip().replace("\\-", "-")
            if target != name and not target.startswith("index-"):
                outgoing.add(target)
        if len(outgoing) < 3:
            errors.append({
                "rule": 7,
                "page": name,
                "path": info["path"],
                "msg": f'Only {len(outgoing)} outgoing links (min 3)',
                "fixable": False,
            })
    return errors

def check_min_size(pages):
    errors = []
    for name, info in pages.items():
        if info["lines"] < 80:
            errors.append({
                "rule": 8,
                "page": name,
                "path": info["path"],
                "msg": f'Only {info["lines"]} lines (min 80)',
                "fixable": False,
            })
    return errors

# --- Fixers ---

def fix_self_links(pages):
    fixed_files = 0
    fixed_links = 0
    for name, info in pages.items():
        matches = list(LINK_RE.finditer(info["content"]))
        self_spans = []
        for m in matches:
            target = m.group(1).strip().replace("\\-", "-")
            if target == name:
                alias = m.group(2)
                if alias and alias.strip():
                    repl = alias.strip()
                else:
                    repl = name.replace("-", " ")
                self_spans.append((m.start(), m.end(), repl))
        if not self_spans:
            continue
        content = info["content"]
        for start, end, repl in reversed(self_spans):
            content = content[:start] + repl + content[end:]
            fixed_links += 1
        with open(info["path"], "w") as f:
            f.write(content)
        info["content"] = content
        fixed_files += 1
    return fixed_files, fixed_links

def fix_escaped_hyphens(pages):
    fixed_files = 0
    for name, info in pages.items():
        content = info["content"]
        new_content = MULTILINE_RE.sub("", content)  # nope, wrong regex
        new_content = ESCAPED_HYPHEN_RE.sub(
            lambda m: "[[" + m.group(1).replace("\\-", "-") + "]]",
            content
        )
        if new_content != content:
            with open(info["path"], "w") as f:
                f.write(new_content)
            info["content"] = new_content
            fixed_files += 1
    return fixed_files

def fix_multiline_links(pages):
    fixed_files = 0
    for name, info in pages.items():
        content = info["content"]
        # Replace multiline links by joining the lines and collapsing whitespace
        def fix_ml(m):
            text = m.group(0).replace("\n", " ").replace("  ", " ")
            return re.sub(r'\[\[\s+', "[[", text)
        new_content = MULTILINE_RE.sub(fix_ml, content)
        if new_content != content:
            with open(info["path"], "w") as f:
                f.write(new_content)
            info["content"] = new_content
            fixed_files += 1
    return fixed_files

def fix_empty_brackets(pages):
    fixed_files = 0
    for name, info in pages.items():
        content = info["content"]
        new_content = EMPTY_BRACKET_RE.sub("", content)
        if new_content != content:
            with open(info["path"], "w") as f:
                f.write(new_content)
            info["content"] = new_content
            fixed_files += 1
    return fixed_files

def fix_space_links(pages):
    fixed_files = 0
    for name, info in pages.items():
        content = info["content"]
        
        def fix_space(m):
            raw = m.group(1)
            # Convert "Foo Bar Baz" to "foo-bar-baz" for the target part
            # But preserve alias part after |
            if "|" in raw:
                target, alias = raw.split("|", 1)
                target = target.strip().lower().replace(" ", "-")
                return f"[[{target}|{alias}]]"
            else:
                return f"[[{raw.strip().lower().replace(' ', '-')}]]"
        
        new_content = SPACE_LINK_RE.sub(fix_space, content)
        if new_content != content:
            with open(info["path"], "w") as f:
                f.write(new_content)
            info["content"] = new_content
            fixed_files += 1
    return fixed_files

# --- Main ---

def main():
    parser = argparse.ArgumentParser(description="LLM Wiki Link Linter")
    parser.add_argument("--fix", action="store_true", help="Auto-fix fixable errors")
    parser.add_argument("--json", action="store_true", help="JSON output")
    parser.add_argument("--rule", type=int, help="Check only a specific rule (1-8)")
    parser.add_argument("--self", action="store_true", help="(with --fix) only fix self-links")
    args = parser.parse_args()

    pages = collect_pages()
    all_names = set(pages.keys())
    
    checkers = {
        1: lambda: check_self_links(pages),
        2: lambda: check_broken_links(pages, all_names),
        3: lambda: check_escaped_hyphens(pages),
        4: lambda: check_multiline_links(pages),
        5: lambda: check_empty_brackets(pages),
        6: lambda: check_space_links(pages),
        7: lambda: check_min_links(pages),
        8: lambda: check_min_size(pages),
    }

    fixers = {
        1: lambda: fix_self_links(pages),
        3: lambda: fix_escaped_hyphens(pages),
        4: lambda: fix_multiline_links(pages),
        5: lambda: fix_empty_brackets(pages),
        6: lambda: fix_space_links(pages),
    }

    # Determine which rules to check
    if args.rule:
        rules = {args.rule}
    else:
        rules = set(RULES.keys())

    # If --fix --self, only do rule 1
    if args.fix and args.self:
        rules = {1}

    # Run checks
    all_errors = []
    for rule in sorted(rules):
        errors = checkers[rule]()
        all_errors.extend(errors)

    # Auto-fix if requested
    if args.fix:
        for rule in sorted(rules):
            if rule in fixers:
                fixer = fixers[rule]
                result = fixer()
                if result:
                    if isinstance(result, tuple):
                        files_count, links_count = result
                        print(f"  Rule {rule} ({RULES[rule]}): fixed {files_count} files, {links_count} links")
                    else:
                        print(f"  Rule {rule} ({RULES[rule]}): fixed {result} files")
        
        # Re-check after fixes
        if not args.self:
            all_errors = []
            for rule in sorted(rules):
                errors = checkers[rule]()
                all_errors.extend(errors)

    # Output
    if args.json:
        print(json.dumps({
            "total_pages": len(pages),
            "errors": all_errors,
            "error_count": len(all_errors),
            "errors_by_rule": dict(Counter(e["rule"] for e in all_errors)),
        }, indent=2))
    else:
        # Summary
        by_rule = defaultdict(list)
        for e in all_errors:
            by_rule[e["rule"]].append(e)
        
        print(f"Wiki Link Lint — {len(pages)} pages checked\n")
        if not all_errors:
            print("All clean! No lint errors found.")
            return
        
        for rule in sorted(by_rule.keys()):
            errs = by_rule[rule]
            fixable = sum(1 for e in errs if e["fixable"])
            symbol = "!" if fixable else "?"
            print(f"  {symbol} Rule {rule}: {RULES[rule]} — {len(errs)} errors ({fixable} fixable)")
            
            # Show rule 2 broken links aggregated
            if rule == 2:
                broken_targets = Counter(e["msg"].split("[[")[1].split("]]")[0] for e in errs)
                for target, count in broken_targets.most_common(10):
                    print(f"      {count:3d}x -> [[{target}]]")
        
        print(f"\n  Total: {len(all_errors)} errors across {len(by_rule)} rules")
        if not args.fix:
            fixable_total = sum(1 for e in all_errors if e["fixable"])
            if fixable_total:
                print(f"  Run with --fix to auto-fix {fixable_total} errors")

    # Exit code
    sys.exit(1 if all_errors else 0)

if __name__ == "__main__":
    main()
