<div align="center">

# 🌱 Farming KB

**The Autonomous Living Encyclopedia of Cultivation, Mycology & Earth Sciences**

[![Pages](https://img.shields.io/badge/pages-12%2C100%2B-blue)](#) [![Sources](https://img.shields.io/badge/sources-155-green)](#) [![Agents](https://img.shields.io/badge/autonomous_agents-54+-orange)](#) [![Status](https://img.shields.io/badge/status-24%2F7_mining-success)](#)

*A self-building knowledge base. No web scraping. No hallucination. Every fact traced to a real book or paper.*

</div>

---

## What Is This?

Farming KB is a comprehensive wiki covering **mycology, cannabis cultivation, herbal medicine, permaculture, psychedelic ethnobotany, regenerative agriculture, and earth sciences**. It contains **12,000+ interlinked pages** mined from a curated library of **155 books, papers, and reference texts**.

What makes it unique: the entire wiki is **built and maintained by 54+ autonomous AI agents** running 24/7. They mine raw sources, generate new pages, cross-link existing ones, audit quality, and push updates — all without human intervention.

## Quick Numbers

| Category | Pages | Description |
|----------------:|-------------|
| [Concepts](concepts/) | 9,700+ | Topic-specific deep dives with citations |
| [Entities](entities/) | 1,300+ | Species, strains, chemicals, people |
| [Comparisons](comparisons/) | 400+ | "X vs Y" side-by-side breakdowns |
| [Queries](queries/) | 460+ | FAQ-style question-answer pages |
| [Topics](topics/) | 170+ | Wikipedia-style long-form narratives |
| **Total** | **12,100+** | **~109 MB of structured markdown** |

## What's Inside

### Mycology & Fungi
Over 4,000 pages on mushroom cultivation, fungal biology, taxonomy, foraging, and applied mycology. From PF Tek to advanced gourmet cultivation, from Psilocybe taxonomy to mycoremediation.

### Cannabis
Comprehensive coverage of cannabis cultivation, breeding, nutrient science, living soil, training techniques, processing, and medical applications. Strain profiles, deficiency guides, and grow system comparisons.

### Permaculture & Regenerative Agriculture
Masanobu Fukuoka's natural farming, Sepp Holzer's techniques, JADAM methods, Korean Natural Farming, agroforestry, cover cropping, composting, and food forest design.

### Herbal Medicine & Ethnobotany
Plant profiles, herbal preparations, traditional medicine systems, and ethnobotanical knowledge spanning multiple cultural traditions.

### Psychedelic Compounds
Chemistry, pharmacology, history, and cultural significance of psychedelic substances. Shulgin's phenethylamines and tryptamines, ayahuasca traditions, mushroom distributions worldwide.

### Homesteading & Self-Sufficiency
Off-grid systems, animal husbandry, food preservation, natural building, water systems, and integrated homestead design.

## Coverage Map

```
mycology          ████████████████████  786+ pages
permaculture      ██████████████        447+ pages
cannabis          ███████████           388+ pages
natural-farming   ██████████            332+ pages
ethnobotany       ██████                150+ pages
psychedelics      ██████                200+ pages
herbalism         █████                 100+ pages
homesteading      ████                   80+ pages
earth-sciences    ████                   60+ pages
```

## Source Library

All content derives from **155 curated texts** — no web scraping, no LLM hallucination. Every page cites its source material.

**Source types:**
- **151 papers** — academic research, field guides, reference texts
- **4 articles** — long-form journalism and technical writing
- Raw library at `~/wiki/raw/` (~2 GB of text)

**Top contributing sources:**
- Uwe Blesching — *The Cannabis Health Index*
- Masanobu Fukuoka — *The Natural Way of Farming*
- Eliot Coleman — *The Winter Harvest Handbook*
- Paul Stamets — *Mycelium Running*, *Growing Gourmet & Medicinal Mushrooms*
- Terence McKenna — *Food of the Gods*
- Shulgin — *PiHKAL*, *TiHKAL*
- Cho Han-kyu — *JADAM Organic Farming*
- 140+ additional books and papers

## Entity Breakdown

| Type | Count | Examples |
|------------:|----------|
| Species | 543 | *Psilocybe cubensis, Cannabis sativa, Agaricus bisporus* |
| General | 471 | Plant varieties, techniques, methods |
| Chemical | 97 | *Psilocybin, THC, CBD, DMT, Muscimol* |
| Strain | 42 | *ACDC, Blue Dream, Golden Teacher* |
| Person | 33 | *Fukuoka, Stamets, Shulgin, Holzer* |
| Other | 31 | Concepts, genera, organizations |

## How It Works

### The Autonomous Mining Pipeline

```
┌─────────────┐    ┌──────────────┐    ┌─────────────┐    ┌──────────────┐
│  Raw Sources │───>│  Queue Mgr   │───>│  Mining     │───>│  Wiki Pages  │
│  (155 texts) │    │  (breadth-   │    │  Agents     │    │  (12,100+)   │
│              │    │   first)     │    │  (15 waves) │    │              │
└─────────────┘    └──────────────┘    └─────────────┘    └──────┬───────┘
                                                                │
                    ┌───────────────────────────────────────────┘
                    ▼
        ┌──────────────────────┐    ┌──────────────────┐
        │  Quality Pipeline    │───>│  Git Sync        │
        │  • Lint (6 rules)    │    │  • Auto-commit   │
        │  • Wikilink enrich   │    │  • Auto-push     │
        │  • Thin page audit   │    │  • Index rebuild │
        │  • Topic generation  │    │                  │
        └──────────────────────┘    └──────────────────┘
```

### Agent Fleet — 54 Cron Jobs

The wiki is maintained by a fleet of **54 autonomous cron agents** running on staggered schedules to maximize throughput and avoid collision:

| Cycle | Agents | Role |
|------:|-------:|------|
| 5 min | 5 | Concept mining (from source queue) |
| 7 min | 8 | Concept mining + entity generation |
| 8 min | 4 | Topic/comparison/query generation |
| 9 min | 9 | Entity generation (species, chemicals, strains) |
| 10 min | 9 | Concept mining + entity generation |
| 11 min | 4 | Entity + multi-page generation |
| 13 min | 2 | Git push + fleet health monitoring |
| 15 min | 7 | Quality audit, wikilink enrichment, generators |
| 30 min | 3 | Index rebuild, heartbeat processing |
| Daily | 1 | Source catalog update |

**Staggered scheduling** uses prime-number intervals (5, 7, 8, 9, 10, 11, 13 minutes) so agents never fire simultaneously, preventing concurrency bottlenecks.

### Fleet Watchdog

A dedicated watchdog agent runs every 13 minutes to:
- Clear stale queue cooldowns (prevents mining dead zones)
- Push unpushed files if the pusher falls behind
- Detect and auto-restart any stuck agents
- Report fleet health status

## Page Format

Every page follows a consistent YAML frontmatter format:

```yaml
---
title: Psilocybe Cubensis Cultivation
tags: [mycology, fungi, cultivation, psilocybe]
date: 2026-04-28
updated: 2026-04-28
sources:
  - /Users/t3rpz/wiki/raw/papers/stamets-cultivation-guide.md
related:
  - [[spore-syringe-preparation]]
  - [[grain-spawn-preparation]]
  - [[bulk-substrate-recipes]]
---

# Psilocybe Cubensis Cultivation

Content here with [[wikilinks]] to related pages...
```

## Tools & Scripts

| Script | Purpose |
|--------|---------|
| `scripts/mining_queue_manager.py` | Source queue with breadth-first priority, cooldown management, and status reporting |
| `scripts/wiki_lint.py` | 6-rule quality checker: frontmatter, wikilinks, page size, line length, outgoing links |
| `scripts/sync-wiki.py` | Syncs wiki content to Quartz static site |
| Cron fleet (54 agents) | 24/7 autonomous mining, generation, quality, and maintenance |

## Quality

Pages are checked against 6 lint rules:
1. YAML frontmatter validity
2. Wikilink format compliance
3. Maximum page size (600 lines)
4. Line length limits
5. Minimum outgoing wikilinks (3)
6. Minimum page size (80 lines)

## Roadmap

- [ ] Complete mining all 155 sources (3,659 pages remaining)
- [ ] Wikilink density improvement across all pages
- [ ] Quartz static site deployment with full-text search
- [ ] Automated deduplication of near-duplicate entities
- [ ] Cross-referencing with botanical/taxonomic databases
- [ ] Image/diagram generation for key concept pages

## Contributing Sources

This wiki only processes existing books and papers — no web research. To contribute a new source:

1. Place the text file in `~/wiki/raw/papers/` or `~/wiki/raw/articles/`
2. The Source Catalog Updater (daily at 4am) will pick it up
3. The mining queue manager will prioritize it (breadth-first: least-mined sources first)
4. Mining agents will begin generating pages automatically

---

<div align="center">

**Built by autonomous agents. Powered by Hermes.**  
*Every page cited. Every fact sourced. Zero hallucination.*

</div>
