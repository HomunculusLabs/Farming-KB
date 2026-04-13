# Wiki Heartbeat

> Task queue for autonomous wiki building. A cron job reads this file,
> picks the first `pending` task, executes it, marks it `done`, and reports.
> Statuses: pending, in_progress, done
>
> RULES:
> - NO web research. Only process existing raw/ sources.
> - All new pages go in concepts/, entities/, comparisons/, or queries/ — NEVER the wiki root.
> - Frontmatter required: title, created, updated, type, tags (from SCHEMA taxonomy only), sources.
> - Every page needs 2+ [[wikilinks]] to other existing wiki pages.
> - Update index.md with any new pages.
> - Use execute_code with open() for all file writes.
> - After each task: verify no broken links, no orphans, index is complete.

## Queue

### done [2026-04-11] | Mine never-cited raw sources batch 1


### done [2026-04-12] | Deep re-mine once-cited sources batch 1 (large files)
These 422KB+ files were barely touched. Read deeply, create/update multiple wiki pages per source.
- magic-mushrooms-around-the-world-gartz (422KB) — species distribution data, regional guides, new species entities
- fungi-magazine-fungi-and-sustainability (42KB) — update fungal-sustainability, create pages for unique topics
- what-a-plant-knows-daniel-chamovitz (19KB) — create plant-senses-biology page, update plant-related pages

### done [2026-04-12] | Deep re-mine once-cited sources batch 2 (research papers)

### done [2026-04-12] | Deep re-mine once-cited sources batch 3 (more papers)
- the-metabolic-pathway-of-psilocybin-production (6KB) — already thoroughly captured in fungal-research-compound-reference; added source ref + biosynthetic context to psilocybin-mushroom-potency
- unknown-cultivation-of-fruitbodies-and-sclerotia (8KB) — created sclerotia-cultivation.md, updated mushroom-substrates with grass seed data, updated psilocybin-mushroom-cultivation with sclerotia section
- stuart-r-ayahuasca-tourism (10KB) — enriched entheogen-culture ayahuasca tourism section with detailed data (shaman authenticity, religious dynamics, safety, historical context)
- a-practitioners-guide-marijuana-magick (23KB) — already thoroughly captured in cannabis-spiritual-ritual-use; no new content needed
- unknown-exploring-the-rich-history-of-plant-scienc (6KB) — already thoroughly captured in plant-propagation history section; no new content needed

### done [2026-04-12] | Deep re-mine twice-cited sources batch 1

### done [2026-04-12] | Deep re-mine twice-cited sources batch 2
Updated 8 pages across 5 sources: Ramsbottom 1945 (mushroom poisoning, A. muscaria details, Inocybe/Etomaloma/Gyromitra species), cannabis microbiome (core endorhiza community, two-tier model, edaphic factors), McKenna tryptamines (DMT phenomenology, spore dispersal, shamanism). Gottlieb and Shulgin confirmed already well-covered.

### done [2026-04-12] | Mine raw/articles/ sources
All 4 files confirmed already thoroughly mined:
- jeff-lowenfels-teaming-with-fungi (268KB) — 14 citations, inoculum production already comprehensive
- nicole-faires-the-ultimate-guide-to-natural-farming-and (611KB) — 17 citations, well-mined
- permaculture-beginners-guide-graham-burnett (21KB) — 5 citations, small pamphlet, all topics covered by larger sources, nurseries already in seed-company-supplier-reference
- fungi-and-sustainability-fungi-magazine (42KB) — CONFIRMED DUPLICATE of fungi-magazine-fungi-and-sustainability (356/360 lines overlap)

### done [2026-04-12] | Build comparison pages from mined data
All 5 comparison pages already existed from previous session — verified indexed and frontmatter complete:
1. comparisons/mushroom-substrate-comparison.md (106 lines)
2. comparisons/hot-composting-vs-vermicompost-vs-bokashi.md (80 lines)
3. comparisons/cannabis-training-techniques.md (105 lines)
4. comparisons/cover-crop-species-comparison.md (98 lines)
5. comparisons/homesteading-livestock-comparison.md (103 lines)

### done [2026-04-12] | Build query/reference pages from mined data
All 5 query pages already existed from previous session — verified:
1. queries/cannabis-nutrient-deficiency-guide.md (104 lines)
2. queries/mushroom-toxicity-identification-warnings.md (106 lines)
3. queries/companion-planting-master-table.md (130 lines)
4. queries/seed-company-supplier-reference.md (105 lines)
5. queries/fungal-remediation-decision-tree.md (102 lines)

### done [2026-04-12] | Bulk up thin pages from raw sources
Enriched 3 remaining thin pages (<3KB) to 4KB+: psylocybe-fanaticus.md (2.9KB→6.1KB, +PF TEK technical details, perlite humidification, DCT, contamination control, Shroom source), max-winston.md (2.9KB→4.5KB, +study design, cultivar-specific findings, community composition details), knf-maltose-preparation.md (2.8KB→4.2KB, +cultural context, role in KNF system, additional wikilinks). All pages now >3KB. 0 broken links, 0 orphans, index complete.

### done [2026-04-12] | Cross-reference enrichment pass 2
Enriched 9 pages with <4 outbound wikilinks. fungal-cell-biology.md (0→8+ links), cannabis-breeding-basics.md (3→8+), cannabis-seed-germination.md (3→5+), fairy-rings-and-giant-mycelia.md (3→10+, fixed broken armillaria link), fungal-biology-fundamentals.md (3→10+), fungal-plant-pathogens.md (3→6+), fungal-sexual-reproduction.md (3→10+), urban-guerrilla-gardening.md (3→8+), water-catchment-urban-permaculture.md (3→8+). Fixed 3 nested-wikilink errors. Final state: 530 pages, 0 broken links, 0 orphans, all pages 4+ outbound wikilinks.

### done [2026-04-12] | Full wiki lint
Complete lint passed with all issues resolved:
- 0 broken links, 0 orphan pages, 0 missing index entries
- 0 frontmatter issues, 0 stale pages, 0 contradiction flags
- 5 pages trimmed from 201-202 lines to ≤200 lines
- 59 missing tags added to SCHEMA.md taxonomy (83→141 tags)
- Log: 97 entries (under 500 rotation threshold)
- Final state: 530 pages, all checks pass.

## Done

### done [2026-04-11] | Mine never-cited raw sources batch 2

<!-- Completed tasks move here with date -->
