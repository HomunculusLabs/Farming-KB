# LLM Farming Wiki

A comprehensive knowledge base covering mycology, cannabis cultivation, herbal medicine, permaculture, psychedelic compounds, and regenerative agriculture. Built from curated books, papers, and texts — no web scraping.

## Structure

```
concepts/     — Topic-specific concept pages (9,500+)
entities/     — Species, strains, people, chemicals (1,300+)
comparisons/  — "X vs Y" comparison pages (400+)
queries/      — FAQ-style question-answer pages (460+)
topics/       — Long-form Wikipedia-style topic pages (170+)
```

## Stats

Generated and maintained by autonomous cron agents. See `index.md` for the full page catalog.

## Source

All content derives from the raw text library at `~/wiki/raw/` — books, papers, and reference texts. No web research, no LLM hallucination — every page is grounded in cited sources.

## Tools

- `mining_queue_manager.py` — Source queue with breadth-first mining priority
- `wiki_lint.py` — Page quality and link hygiene checks
- Cron fleet — 50+ autonomous agents mining, generating, and maintaining pages 24/7
