import os, re, subprocess

wiki = os.path.expanduser("~/wiki")
LINK_RE = r'\[\[([a-z0-9][a-z0-9\-]*)(?:\|[^\]]+)?\]\]'
dirs = ["concepts", "entities", "comparisons", "queries"]

# === BUILD PAGE SET ===
all_pages = set()
for d in dirs:
    path = os.path.join(wiki, d)
    if not os.path.exists(path): continue
    for f in os.listdir(path):
        if f.endswith(".md") and f != "index.md" and not f.startswith("index-"):
            all_pages.add(f[:-3])

print(f"Page set: {len(all_pages)} pages")

# === COLLECT ALL ISSUES ===
thin_pages = []
broken_map = {}
low_link_pages = []

for d in dirs:
    path = os.path.join(wiki, d)
    if not os.path.exists(path): continue
    for f in sorted(os.listdir(path)):
        if not f.endswith(".md") or f == "index.md" or f.startswith("index-"): continue
        fp = os.path.join(path, f)
        r = subprocess.run(["wc", "-l", fp], capture_output=True, text=True)
        lc = int(r.stdout.strip().split()[0])
        if lc < 80: thin_pages.append((d + "/" + f, lc))
        with open(fp) as fh: c = fh.read()
        links = set(re.findall(LINK_RE, c))
        if len(links) < 3:
            low_link_pages.append((d + "/" + f, len(links), c))
        for link in links:
            if link.strip() not in all_pages:
                broken_map.setdefault(link, []).append(d + "/" + f)

print(f"Thin: {len(thin_pages)}, Broken targets: {len(broken_map)}, Low-link: {len(low_link_pages)}")
