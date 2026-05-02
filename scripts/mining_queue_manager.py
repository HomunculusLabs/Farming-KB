#!/usr/bin/env python3
"""
mining_queue_manager.py — Manages the shared work queue for mining waves.

Waves READ the queue to pick sources. After mining, they UPDATE room counts.
A separate process can rebuild the queue from scratch.

Usage:
  python3 mining_queue_manager.py rebuild          # full rebuild from filesystem
  python3 mining_queue_manager.py pop N             # get next N sources to mine
  python3 mining_queue_manager.py done SOURCE       # mark source as mined (reduces room)
  python3 mining_queue_manager.py status            # show current queue state
"""

import os
import sys
import json
import time

WIKI = os.path.expanduser("~/wiki")
QUEUE_PATH = os.path.join(WIKI, "mining_queue.json")
PAPERS = os.path.join(WIKI, "raw/papers")
PAGE_DIRS = ["concepts", "entities"]

def load_queue():
    if os.path.exists(QUEUE_PATH):
        with open(QUEUE_PATH) as f:
            return json.load(f)
    return []

def save_queue(queue):
    with open(QUEUE_PATH, "w") as f:
        json.dump(queue, f, indent=2)

def rebuild():
    """Full rebuild — scan all source files and count existing pages."""
    # Get all source files
    sources = {}
    for f in sorted(os.listdir(PAPERS)):
        if not f.endswith(".md"): continue
        path = os.path.join(PAPERS, f)
        size = os.path.getsize(path)
        with open(path) as fh:
            lines = sum(1 for _ in fh)
        sources[f] = {"size": size, "lines": lines}

    # Get all page prefixes
    pages = set()
    for d in PAGE_DIRS:
        dp = os.path.join(WIKI, d)
        if not os.path.exists(dp): continue
        for f in os.listdir(dp):
            if f.endswith(".md"):
                pages.add(f[:-3])

    queue = []
    for fname, meta in sources.items():
        if meta["size"] < 5000: continue
        prefix = fname.replace(".md", "").split("-")[0]
        count = sum(1 for p in pages if p.startswith(prefix + "-") or p == prefix)
        potential = max(1, meta["lines"] // 200)
        room = max(0, potential - count)
        # Priority: least extracted pages first (breadth-first coverage)
        # Tiebreak by most room remaining (biggest untouched sources first)
        queue.append({
            "source": fname,
            "prefix": prefix,
            "size_kb": meta["size"] // 1024,
            "lines": meta["lines"],
            "have": count,
            "room": room,
            "priority": room,
            "last_mined": 0,
        })

    queue.sort(key=lambda x: (x["have"], -x["room"]))
    save_queue(queue)
    return queue

def pop(n=3, exclude_prefixes=None):
    """Get next N sources to mine, avoiding recently mined and excluded."""
    queue = load_queue()
    now = time.time()
    if exclude_prefixes is None:
        exclude_prefixes = []

    picked = []
    for item in queue:
        if len(picked) >= n:
            break
        if item["room"] <= 0:
            continue
        if item["prefix"] in exclude_prefixes:
            continue
        # Skip if mined in last 5 minutes (reduced from 15 to allow faster cycling)
        if now - item.get("last_mined", 0) < 300:
            continue
        picked.append(item)
        item["last_mined"] = now

    save_queue(queue)
    return picked

def done(source_file, pages_added=0):
    """Update room count after mining from a source."""
    queue = load_queue()
    for item in queue:
        if item["source"] == source_file:
            item["have"] += pages_added
            item["room"] = max(0, item["room"] - pages_added)
            item["priority"] = item["room"]
            break
    # Re-sort: least extracted first, tiebreak by most room
    queue.sort(key=lambda x: (x["have"], -x["room"]))
    save_queue(queue)

def status(top_n=20):
    """Show current queue state."""
    queue = load_queue()
    active = [q for q in queue if q["room"] > 0]
    print(f"Queue: {len(active)} sources with room, {sum(q['room'] for q in active)} total pages remaining")
    print(f"\n{'Room':>5}  {'Have':>5}  {'Size':>6s}  {'Source'}")
    print("-" * 80)
    for q in active[:top_n]:
        size = f"{q['size_kb']//1024}MB" if q['size_kb'] >= 1024 else f"{q['size_kb']}KB"
        print(f"{q['room']:>5d}  {q['have']:>5d}  {size:>6s}  {q['source']}")

if __name__ == "__main__":
    cmd = sys.argv[1] if len(sys.argv) > 1 else "status"
    if cmd == "rebuild":
        q = rebuild()
        print(f"Rebuilt queue: {len(q)} sources, {sum(x['room'] for x in q)} pages remaining")
    elif cmd == "pop":
        n = int(sys.argv[2]) if len(sys.argv) > 2 else 3
        exclude = sys.argv[3].split(",") if len(sys.argv) > 3 else []
        picked = pop(n, exclude)
        for p in picked:
            print(f"{p['room']:>4d} room  {p['source']}")
    elif cmd == "done":
        src = sys.argv[2] if len(sys.argv) > 2 else ""
        pages = int(sys.argv[3]) if len(sys.argv) > 3 else 0
        if src:
            done(src, pages)
            print(f"Updated: {src} (-{pages} room)")
    elif cmd == "status":
        top = int(sys.argv[2]) if len(sys.argv) > 2 else 20
        status(top)
    else:
        print(f"Unknown command: {cmd}. Use rebuild/pop/done/status")
