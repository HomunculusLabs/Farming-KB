#!/usr/bin/env python3
"""
wiki_source_coverage.py — Report how many wiki pages were extracted from each source.

Usage:
  python3 wiki_source_coverage.py              # full report
  python3 wiki_source_coverage.py --top 20     # top 20 by remaining room
  python3 wiki_source_coverage.py --json       # machine-readable JSON
  python3 wiki_source_coverage.py --source cervantes  # single source detail

Uses two matching strategies:
  1. Filename prefix mapping (primary) — maps source filenames to page filename prefixes
  2. Frontmatter `sources:` field (supplementary) — catches pages with explicit citations
"""

import os
import re
import sys
import json
import argparse

WIKI_DIR = os.path.expanduser("~/wiki")
RAW_DIR = os.path.join(WIKI_DIR, "raw/papers")
PAGE_DIRS = ["concepts", "entities", "comparisons", "queries", "topics"]

# ── Prefix mapping: source filename → list of filename prefixes to match ──
# Each source file can produce pages with different prefixes.
# We map source filenames to the prefixes that pages from that source would use.
PREFIX_MAP = {
    # Permaculture & Farming
    "bill-mollison-permaculture-a-designers-manual.md": ["mollison"],
    "bill-mollison-permaculture-two-practical-design-for-to.md": ["mollison-two"],
    "bill-mollison-permaculture-design-course.md": ["mollison-pdc"],
    "david-holmgren-permaculture-principles-pathways-beyon.md": ["holmgren"],
    "gaias-garden-toby-hemenway.md": ["hemenway"],
    "a-guide-to-home-scale-permaculture-gaias-garden-a-guide-to-home-scale-permacultu.md": ["gaias"],
    "sepp-holzer-practical-guide-to-small-scale-integrative.md": ["holzer"],
    "sepp-holzer-practical-guide.md": ["sepp"],
    "holzer-desert-or-paradise.md": ["holzer-desert"],
    "masanobu-fukuoka-the-natural-way-of-farming-the-theory.md": ["fukuoka"],
    "masanobu-fukuoka-the-road-back-to-nature.md": ["fukuoka"],
    "masanobu-fukuoka-fukuoka.md": ["fukuoka"],
    "one-straw-revolution-masanobu-fukuoka.md": ["fukuoka"],
    "masanobu-fukuoka-sowing-seeds-in-the-desert.md": ["fukuoka"],
    "administrator-microsoft-word-fukuoka-textdoc.md": ["fukuoka"],
    "savory-holistic-resource-management.md": ["savory"],
    "jeavons-john-how-to-grow-more-vegetables.md": ["jeavons"],
    "gardening-when-it-counts-steve-solomon.md": ["solomon"],
    "eliot-coleman-winter-harvest-handbook.md": ["coleman"],
    "hamilton-geoffhamilton-nick_-organic-gardening.md": ["hamilton"],
    "william-ozier-williams-pdc_-a-permaculture-design-cours.md": ["pdc", "williams", "ozier"],
    "a-selection-permaculture-plants.md": ["permplant", "permaculture-plants"],
    "urban-permaculture-guerilla-gardening.md": ["urban-perm", "urban", "guerilla"],
    "permaculture-beginners-guide.md": ["permaculture-beginners"],
    "purdue-home-gardeners-guide.md": ["purdue"],

    # Cannabis
    "marijuana-horticulture-cervantes.md": ["cervantes"],
    "uwe-blesching-the-cannabis-health-index.md": ["blesching"],
    "greg-green-the-cannabis-grow-bible.md": ["greg-green", "greg", "green"],
    "robert-c-clarke-marijuana-botany-an-advanced-study.md": ["clarke"],
    "vic-high-creating-true-breeding-strains.md": ["vic"],
    "s-t-oner-the-rev-cannabis-sativa-volume-3_-the-essential-gu.md": ["oner"],
    "ben-lemon-cannabis-alchemy.md": ["lemon"],
    "a-practitioners-guide-marijuana-magick.md": ["practitioner"],
    "the-modern-farm-why-cannabis-grown-with-lab-might-produce.md": ["modern-farm"],
    "understanding-cultivar-specificity-cannabis-microbiome.md": ["cultivar"],

    # Mushroom Cultivation
    "unknown-growing-gourmet-and-medicinal-mushrooms-s.md": ["gourmet", "growing-gourmet", "growing"],
    "the-mushroom-cultivator-stamets.md": ["stamets", "cultivator"],
    "unknown-mycelium-running.md": ["mycelium"],
    "mycelium-running-stamets.md": ["mycelium"],
    "unknown-oyster-mushroom-cultivation.md": ["oyster"],
    "william-falconer-mushroom-how-to-grow-them.md": ["falconer"],
    "benjamin-minge-duggar-mushroom-growing.md": ["duggar"],
    "cotter-organic-mushroom-farming-mycoremediation.md": ["cotter"],
    "james-cuthill-a-treatise-on-the-cultivation-of-the-mushroom.md": ["cuthill"],
    "pf-tek-psilocybe-fanaticus.md": ["pf"],
    "fanaticus-pf-tek-psilocybe-fanaticus.md": ["pf"],
    "jarrold-indoor-mushroom-growing-technique-boil-a-bag.md": ["jarrold"],
    "peter-oei-5-pages-mushroom-cultivation.md": ["oei", "peter"],
    "laminar-flow-hood-construction-1.md": ["laminar"],
    "2-laminar-flow-hood-construction.md": ["laminar"],
    "working-with-agar.md": ["agar", "working"],
    "unknown-working-with-agar.md": ["agar", "working"],
    "unknown-a-practical-guide-to-synthetic-log-cultiva.md": ["synthetic-log"],
    "growing-the-woodlovers-outdoors.md": ["woodlovers"],
    "unknown-growing-the-woodlovers-outdoors.md": ["woodlovers"],
    "cultivation-of-panaeolus-cyanescens-and-panaeolus-tropicalis.md": ["panaeolus", "tropical"],
    "growing-psilocybe-azurescens.md": ["azurescens"],
    "unknown-cultivation-of-fruitbodies-and-sclerotia.md": ["fruitbodies"],
    "a-training-manual-mushroom-cultivation-by-people-with-disabi.md": ["training-manual"],
    "unknown-mushroom-culture-patent-2761246.md": ["mushroom-culture"],
    "carolina-mushrooms_08qxp.md": ["carolina"],

    # Fungal Biology
    "unknown-biodiversity-of-fungi.md": ["biodiversity"],
    "john-dighton-fungi-in-ecosystem-processes.md": ["dighton"],
    "geoffrey-gadd-sarah-c-watkinson-paul-s-dyer-fungi-in-the-environment.md": ["gadd"],
    "singh-harbhajan_-mycoremediation-_-fungal-bioremediation.md": ["singh"],
    "staycare-mngmt-fungi-in-bioremediation.md": ["staycare"],
    "symbiotic-fungi.md": ["symbiotic"],
    "fungi-magazine-fungi-and-sustainability.md": ["fungi-sustainability"],
    "fungi-and-sustainability-fungi-magazine.md": ["fungi-sustainability"],
    "tropisms-in-the-mushroom-psilocybe-cubensis.md": ["tropisms"],
    "unknown-tropisms-in-psilocybe-cubensis.md": ["tropisms"],
    "the-effect-of-light-upon-basidiocarp-initiation-in-psilocybe-cubensis.md": ["light-basidiocarp"],
    "unknown-effect-of-light-upon-basidiocarp-initiation-psilocybe-cubensis.md": ["light-basidiocarp"],
    "the-effect-of-the-interaction-of-various-spawn-grains-with-different-culture-med.md": ["spawn-grains"],
    "gartz-growth-promoting-effect-of-brassinosteroid-psilocybe-cubensis.md": ["brassinosteroid"],
    "growth-promoting-effect-of-a-brassinosteroid-in-mycelial-cultures-of-the-fungus-psilocybe-cubensis-gartz-adam-vorbrodt.md": ["brassinosteroid"],
    "the-metabolic-pathway-of-psilocybin-production.md": ["psilocybin-pathway"],
    "unknown-metabolic-pathway-of-psilocybin-production.md": ["psilocybin-pathway"],
    "tryptamine-cubensis-gartz.md": ["tryptamine-cubensis"],
    "nutrient-and-dynamic-accumulators.md": ["nutrient-accumulator", "dynamic"],
    "unknown-nutrient-and-dynamic-accumulators.md": ["nutrient-accumulator", "dynamic"],

    # Psychedelics
    "shulgin-a-pihkal.md": ["pihkal", "2c-b", "2c", "mda", "mdm", "dob", "dom", "doi", "aleph", "tma", "mmda"],
    "shulgin-a-tihkal.md": ["tihkal"],
    "hofmann-a-lsd-my-problem-child.md": ["hofmann", "lsd"],
    "mckenna_t-food_of-the-gods.md": ["mckenna"],
    "mckenna_t-tryptamines_consciousness.md": ["mckenna-trypt"],
    "harner-j-hallucinogens-and-shamanism.md": ["harner"],
    "the-road-to-eleusis.md": ["wasson", "eleusinian", "kykeon"],
    "turner-the-essential-psychedelics-guide-by-dm-turner.md": ["turner"],
    "the-essential-psychedelics-guide-by-dm-turner.md": ["turner"],
    "leary-t-the-psychedelic-experience.md": ["leary"],
    "metzner_r-hallucinogenic_drugs_in_psychotherapyshamanism.md": ["metzner"],
    "amaringo-p-ayahuasca-visions.md": ["amaringo"],
    "allegro-j-the-sacred-mushroomcross.md": ["allegro"],
    "magic-mushrooms-around-the-world-by-jochen-gartz.md": ["gartz"],
    "magic-mushrooms-around-the-world-gartz.md": ["gartz"],
    "world-wide-distribution-of-magic-mushrooms-guzman-allen-&-gartz.md": ["guzman"],
    "magic-mushrooms-of-australia-newzealand-by-john-w-allen.md": ["allen"],
    "the-psilocybin-solution-by-simon-g-powell.md": ["powell"],
    "plants-of-the-gods-schultes-hofmann.md": ["schultes"],
    "a-golden-guide-to-hallucinogenic-plants.md": ["golden-guide", "golden"],
    "halpern-m-hallucinogens-dissociative-agents-growing-in-us.md": ["halpern"],
    "arthur-j-mushrooms-and-mankind.md": ["arthur"],
    "amanita-muscaria-herb-of-immortality.md": ["amanita"],
    "psilocybin-mushrooms-of-the-world-stamets.md": ["stamets-psylo"],
    "shroom-a-cultural-history-of-the-magic-mushroom.md": ["shroom"],
    "magic-mushroom-growers-guide-ot-oss-on-oeric.md": ["gottlieb"],
    "bigwood-beug-variation-of-psilocybin-and-psilocin-levels-bigwood-beug.md": ["bigwood"],
    "unknown-sterilizing-surfaces-by-irradiation-with-microwaves.md": ["sterilizing"],
    "sterilizing-surfaces-by-irradiation-with-microwaves.md": ["sterilizing"],
    "gottlieb-a-the-psilocybin-producers-guide.md": ["gottlieb-producers"],
    "gottlieb-a-peyote-and-other-psychoactive-cacti.md": ["gottlieb"],
    "psilocybin-production-gottlieb.md": ["psilocybin-production"],
    "shirota-hakamata-goda-concise-large-scale-synthesis-of-psilocin-and-psilocybin.md": ["shirota"],
    "concise-large-scale-synthesis-of-psilocin-and-psilocybin-shirota-hakamata-goda.md": ["shirota"],
    "stuart-r-ayahuasca-tourism.md": ["ayahuasca-tourism", "stuart"],
    "the-psilocybin-mushroom-image-guide.md": ["stamets-image"],
    "unknown-psilocybin-mushroom-image-guide.md": ["stamets-image"],
    "field-guide-to-the-psilocybin-mushroom.md": ["field-guide"],
    "unknown-field-guide-to-the-psilocybin-mushroom.md": ["field-guide"],
    "unknown-nutrient-and-dynamic-accumulators.md": ["nutrient-accumulator"],

    # Soil & Microbiology
    "lowenfels-teaming-with-microbes.md": ["lowenfels", "teaming"],
    "teaming-with-microbes-lowenfels.md": ["lowenfels", "teaming"],
    "lowenfels-jeff-teaming-with-nutrients_-the-organic-garden.md": ["lowenfels-nutrients"],
    "teaming-with-fungi-lowenfels.md": ["lowenfels-fungi"],
    "elaine-ingham-phd_-the-field-guide-i-for-actively-aerated-com.md": ["ingham", "aact"],
    "what-a-plant-knows-daniel-chamovitz.md": ["chamovitz"],
    "grahamholmes-what-a-plant-knowsindd.md": ["plant-knows"],

    # Herbalism
    "cancer-treatments-medicinal-mushrooms.md": ["cancer", "medicinal"],

    # KNF/IMO
    "jadam-organic-farming-ultra-low-cost-agriculture.md": ["jadam"],
    "chos-global-natural-farming.md": ["knf", "chos"],
    "master-cho-knf-recipe-book.md": ["cho", "master"],
    "the-ultimate-guide-to-natural-farming-and-sustainable-living.md": ["natural-farm", "natfarm"],
    "the-way-to-ultra-low-cost-agriculture-untitled.md": ["ultra-low-cost", "ultra"],
    "bahay-kubo-indigenous-microorganisms_.md": ["bahay"],
    "beneficial-indigenous-microorganisms-bionutrients.md": ["bionutrients"],
    "unknown-natural-farming-poster.md": ["natural-farming-poster"],

    # History & Misc
    "ramsbottom-poisonous-fungi-ramsbottom.md": ["ramsbottom"],
    "mushrooms---poisionous-fungi-by-john-ramsbottom-1945.md": ["ramsbottom"],
    "julius-auboineau-palmer-about-mushrooms.md": ["palmer"],
    "about-mushrooms-1894.md": ["about-mushrooms"],
    "unknown-mr-bloomfields-orchard-mysterious-world-of-mushrooms.md": ["bloomfield", "bloomfields"],
    "mr-bloomfields-orchard---the-mysterious-world-of-mushrooms-molds-and-mycologists.md": ["bloomfield"],
    "unknown-exploring-the-rich-history-of-plant-scienc.md": ["plant-science"],
    "mushrooms-fungi-from-around-the-world.md": ["mushrooms-world"],
    "unknown-mushrooms-fungi-from-around-the-world.md": ["mushrooms-world"],
    "william-falconer-mushroom_-how-to-grow-them.md": ["falconer"],
    "shulgin-a-future-drugs.md": ["shulgin"],
    "mckenna_t-food_of_the_gods.md": ["mckenna"],
}


def get_raw_sources():
    """Get all raw source files with metadata."""
    sources = []
    for f in sorted(os.listdir(RAW_DIR)):
        if not f.endswith(".md"):
            continue
        path = os.path.join(RAW_DIR, f)
        size = os.path.getsize(path)
        with open(path) as fh:
            lines = sum(1 for _ in fh)
        sources.append({"filename": f, "size": size, "lines": lines})
    return sources


def get_all_pages():
    """Get all wiki page filenames (without .md)."""
    pages = []
    for d in PAGE_DIRS:
        dirpath = os.path.join(WIKI_DIR, d)
        if not os.path.exists(dirpath):
            continue
        for f in os.listdir(dirpath):
            if f.endswith(".md"):
                pages.append(f[:-3])
    return set(pages)


def count_pages_by_prefix(prefixes, all_pages):
    """Count pages matching any of the given prefixes."""
    count = 0
    matched = []
    for prefix in prefixes:
        for page in all_pages:
            if page.startswith(prefix + "-"):
                count += 1
                matched.append(page)
    # Deduplicate (page might match multiple prefixes from same source)
    return len(set(matched)), set(matched)


def count_pages_by_frontmatter(source_filename, candidate_pages, page_dirs=None):
    """Count pages that reference a source in their frontmatter. Only scans candidate_pages."""
    search_terms = [
        source_filename,
        source_filename.replace(".md", ""),
        source_filename.split("-")[0],
    ]
    # PITFALL: Do NOT scan all 8800+ wiki pages — scanning frontmatter on
    # the full page set times out (>15s). Only scan candidate_pages (typically
    # 0-50 files), which should be pre-filtered by prefix in build_report().
    count = 0
    matched = set()
    if page_dirs is None:
        page_dirs = PAGE_DIRS
    for d in page_dirs:
        dirpath = os.path.join(WIKI_DIR, d)
        if not os.path.exists(dirpath):
            continue
        for f in os.listdir(dirpath):
            if not f.endswith(".md"):
                continue
            page_name = f[:-3]
            if page_name not in candidate_pages:
                continue
            try:
                with open(os.path.join(dirpath, f)) as fh:
                    head = fh.read(1000)
            except:
                continue
            for term in search_terms:
                if term.lower() in head.lower():
                    count += 1
                    matched.add(page_name)
                    break
    return count, matched


def estimate_potential(lines, size):
    """Estimate how many extractable pages a source could yield."""
    # Rough: one page per 200-250 lines of source text
    # But small files (< 500 lines) are probably only 1-3 pages
    if lines < 500:
        return max(1, lines // 150)
    return max(1, lines // 200)


def get_display_name(filename):
    """Convert filename to a human-readable source name."""
    # Remove common prefixes
    name = filename
    for prefix in ["unknown-", "administrator-microsoft-word-"]:
        name = name.removeprefix(prefix)
    # Remove .md
    name = name.replace(".md", "")
    # Replace hyphens and underscores with spaces, capitalize
    name = name.replace("_", " ").replace("-", " ").title()
    # Clean up
    name = re.sub(r"\bPihkal\b", "PIHKAL", name)
    name = re.sub(r"\bTihkal\b", "TIHKAL", name)
    name = re.sub(r"\bLsd\b", "LSD", name)
    name = re.sub(r"\bDmt\b", "DMT", name)
    name = re.sub(r"\bKnf\b", "KNF", name)
    name = re.sub(r"\bJadam\b", "JADAM", name)
    name = re.sub(r"\bImo\b", "IMO", name)
    name = re.sub(r"\bAact\b", "AACT", name)
    name = re.sub(r"\bPdc\b", "PDC", name)
    name = re.sub(r"\bPf\b", "PF", name)
    return name


def build_report(top_n=None, source_filter=None, use_frontmatter=False):
    """Build the full coverage report."""
    raw_sources = get_raw_sources()
    all_pages = get_all_pages()

    report = []
    for src in raw_sources:
        fname = src["filename"]

        # Skip if filtering and doesn't match
        if source_filter and source_filter.lower() not in fname.lower():
            continue

        # Count by prefix (primary — fast)
        prefixes = PREFIX_MAP.get(fname, [fname.split("-")[0]])
        prefix_count, prefix_matched = count_pages_by_prefix(prefixes, all_pages)

        total_count = prefix_count

        if use_frontmatter:
            # Only scan pages whose first-word prefix matches (fast filter)
            source_first_word = fname.split("-")[0]
            candidates = set()
            for page in all_pages:
                if page.split("-")[0] == source_first_word or page.startswith(source_first_word[:6]):
                    candidates.add(page)
            candidates -= prefix_matched
            if candidates:
                fm_count, fm_matched = count_pages_by_frontmatter(fname, candidates)
                total_count = len(prefix_matched | fm_matched)

        potential = estimate_potential(src["lines"], src["size"])
        remaining = max(0, potential - total_count)
        pct = min(100, (total_count / potential * 100)) if potential > 0 else 0

        report.append({
            "filename": fname,
            "display_name": get_display_name(fname),
            "size": src["size"],
            "lines": src["lines"],
            "pages_extracted": total_count,
            "potential_pages": potential,
            "remaining_room": remaining,
            "yield_pct": pct,
            "prefix_count": prefix_count,
            "frontmatter_count": total_count - prefix_count,
        })

    # Sort by remaining room descending
    report.sort(key=lambda x: -x["remaining_room"])

    if top_n:
        report = report[:top_n]

    return report


def print_report(report, show_all=False):
    """Print the report in a nice table format."""
    # Filter out tiny sources unless show_all
    if not show_all:
        report = [r for r in report if r["size"] >= 5000]

    print(f"\n{'Room':>5}  {'Have':>5}  {'Pot.':>5}  {'Yield':>6}  {'Size':>8s}  "
          f"{'Lines':>7s}  {'Source'}")
    print("─" * 100)

    total_extracted = 0
    total_potential = 0
    total_size = 0

    for r in report:
        size_str = f"{r['size']/1024/1024:.1f}MB" if r['size'] >= 1048576 else f"{r['size']/1024:.0f}KB"
        yield_str = f"{r['yield_pct']:.0f}%"
        print(f"{r['remaining_room']:>5d}  {r['pages_extracted']:>5d}  {r['potential_pages']:>5d}  "
              f"{yield_str:>6s}  {size_str:>8s}  {r['lines']:>7d}  {r['display_name']}")
        total_extracted += r["pages_extracted"]
        total_potential += r["potential_pages"]
        total_size += r["size"]

    total_room = total_potential - total_extracted
    total_yield = (total_extracted / total_potential * 100) if total_potential > 0 else 0

    print("─" * 100)
    size_str = f"{total_size/1024/1024:.1f}MB"
    print(f"{total_room:>5d}  {total_extracted:>5d}  {total_potential:>5d}  "
          f"{total_yield:>5.0f}%  {size_str:>8s}  {'TOTAL':>7s}")
    print(f"\n  {total_extracted} pages extracted from {len(report)} sources "
          f"({total_size/1024/1024:.1f} MB raw text)")
    print(f"  {total_room} pages of remaining extraction capacity")


def print_source_detail(report, source_name):
    """Print detailed info about pages from a specific source."""
    matches = [r for r in report if source_name.lower() in r["filename"].lower()
               or source_name.lower() in r["display_name"].lower()]
    if not matches:
        print(f"No source matching '{source_name}' found.")
        return

    for r in matches:
        size_str = f"{r['size']/1024/1024:.1f}MB" if r['size'] >= 1048576 else f"{r['size']/1024:.0f}KB"
        print(f"\n{'='*60}")
        print(f"  {r['display_name']}")
        print(f"  File: {r['filename']}")
        print(f"  Size: {size_str} ({r['lines']:,} lines)")
        print(f"  Pages extracted: {r['pages_extracted']} (prefix: {r['prefix_count']}, "
              f"frontmatter: {r['frontmatter_count']})")
        print(f"  Estimated potential: ~{r['potential_pages']} pages")
        print(f"  Remaining room: ~{r['remaining_room']} pages")
        print(f"  Yield: {r['yield_pct']:.0f}%")
        print(f"{'='*60}")

        # List the actual extracted pages
        prefixes = PREFIX_MAP.get(r["filename"], [r["filename"].split("-")[0]])
        all_pages = get_all_pages()
        matched = set()
        for prefix in prefixes:
            for page in all_pages:
                if page.startswith(prefix + "-"):
                    matched.add(page)

        if matched:
            print(f"\n  Extracted pages ({len(matched)}):")
            for page in sorted(matched)[:50]:
                print(f"    - {page}")
            if len(matched) > 50:
                print(f"    ... and {len(matched) - 50} more")


def main():
    parser = argparse.ArgumentParser(description="Wiki source coverage report")
    parser.add_argument("--top", type=int, default=None, help="Show only top N sources")
    parser.add_argument("--json", action="store_true", help="Output as JSON")
    parser.add_argument("--all", action="store_true", help="Include tiny sources (< 5KB)")
    parser.add_argument("--source", type=str, default=None, help="Detail a specific source")
    args = parser.parse_args()

    report = build_report(top_n=args.top, use_frontmatter=bool(args.source))

    if args.json:
        print(json.dumps(report, indent=2))
    elif args.source:
        print_source_detail(report, args.source)
    else:
        print_report(report, show_all=args.all)


if __name__ == "__main__":
    main()
