"""Site QA: run after tools/build_site.py. Exit code 1 if anything is wrong.
Checks every built page for title/description length, canonical, exactly one H1, OG tags, valid JSON-LD,
3+ internal links, broken internal links, orphan pages, banned phrases, and lists [PLACEHOLDER]s.
Usage: python tools/qa.py [--placeholders]
"""
import html, json, os, re, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE = json.load(open(os.path.join(ROOT, "tools", "site.json"), encoding="utf-8"))["base"]
# brief section 5 + Swedish equivalents
BANNED = re.compile(r"\b(delve|unlock|elevate|seamless|robust|game[- ]changer|look no further|cutting[- ]edge|unleash|"
                     r"dive into|tapestry|landscape|embark|"
                     r"sömlös\w*|banbrytande|revolutionerande|lås upp|i dagens snabba|oavsett om du är|saumaton|mullistava|nykypäivän kiireisessä|riippumatta siitä oletko|"
                     r"leta inte längre|let ikke lenger|det är viktigt att notera|sammanfattningsvis|dyk in|dyka ner i|"
                     r"spjutspets\w*|nästa nivå|skräddarsydd\w*|oöverträffad\w*)\b", re.I)

def pages():
    for dp, dirs, files in os.walk(ROOT):
        dirs[:] = [d for d in dirs if d not in (".git", "tools", "assets")]
        for f in files:
            if f.endswith(".html"):
                p = os.path.join(dp, f)
                rel = os.path.relpath(p, ROOT).replace(os.sep, "/")
                url = "/" + ("" if rel == "index.html" else rel[:-len("index.html")]) if rel.endswith("index.html") else "/" + rel
                yield url, open(p, encoding="utf-8").read()

def sources():
    """url -> source meta (focus keyword etc.) from tools/pages/<lang> and tools/posts/<lang>"""
    out = {}
    for lang, pre, blog in (("en", "/en/", "/en/guides/"), ("fi", "/", "/oppaat/")):
        for sub, prefix in (("pages", pre), ("posts", blog)):
            d = os.path.join(ROOT, "tools", sub, lang)
            if not os.path.isdir(d): continue
            for fn in os.listdir(d):
                raw = open(os.path.join(d, fn), encoding="utf-8").read()
                meta = json.loads(re.match(r"\s*<!--(\{.*?\})-->", raw, re.S).group(1))
                slug = meta["slug"]
                out[prefix + (slug + "/" if slug else "")] = meta
    return out

def slugify(s):
    import unicodedata
    return re.sub(r"[^a-z0-9]+", "-", unicodedata.normalize("NFKD", s).encode("ascii", "ignore").decode().lower()).strip("-")

def rank_math(url, doc, meta, bad):
    """the Rank Math content checks that apply to a static page (focus keyword = meta["keyword"])"""
    kw = meta["keyword"].lower()
    title = html.unescape(re.search(r"<title>(.*?)</title>", doc, re.S).group(1)).lower()
    desc = html.unescape(re.search(r'<meta name="description" content="([^"]*)"', doc).group(1)).lower()
    main_part = doc[doc.find("<main"):doc.find("</main>")]
    text = html.unescape(re.sub(r"<[^>]+>", " ", re.sub(r"<(script|style|nav)\b.*?</\1>", " ", main_part, flags=re.S))).lower()
    words = text.split()
    count = len(re.findall(r"(?<!\w)" + re.escape(kw) + r"(?!\w)", " ".join(words)))
    density = 100 * count / max(len(words), 1)
    pos = title.find(kw)
    if pos < 0 or pos > len(title) / 2: bad(f"RM: keyword '{kw}' not near the start of the title")
    if not re.search(r"\d", title): bad("RM: no number in title")
    if kw not in desc: bad("RM: keyword missing from meta description")
    if url not in ("/", "/en/") and slugify(kw) not in url: bad(f"RM: keyword not in URL ({slugify(kw)})")
    if kw not in " ".join(words[:max(len(words) // 10, 60)]): bad("RM: keyword not in the first 10% of the content")
    if not any(kw in html.unescape(re.sub(r"<[^>]+>", "", h)).lower() for h in re.findall(r"<h[23][^>]*>(.*?)</h[23]>", main_part, re.S)):
        bad("RM: keyword not in any H2/H3")
    if not any(kw in html.unescape(a).lower() for a in re.findall(r'<img[^>]*alt="([^"]*)"', main_part)): bad("RM: no image with keyword in alt")
    if not 0.75 <= density <= 2.0: bad(f"RM: keyword density {density:.2f}% ({count}x in {len(words)} words), aim 1–1.5%")
    if not 600 <= len(words) <= 2600: bad(f"RM: {len(words)} words, aim 600–2500")
    ext = [a for a in re.findall(r"<a\b[^>]*>", main_part) if re.search(r'href="https?://(?!(www\.)?tilaaiptv\.com|api\.whatsapp)', a)]
    if not any("nofollow" not in a for a in ext): bad("RM: no dofollow external link")
    if 'class="toc"' not in main_part: bad("RM: no table of contents")
    return density, count, len(words)

POLICY = json.load(open(os.path.join(ROOT, "tools", "keyword_policy.json"), encoding="utf-8"))
DENY = re.compile(POLICY["deny_regex"], re.I)

def main():
    problems, linked, exists, ph = [], {}, set(), []
    all_pages = {u: d for u, d in pages() if 'http-equiv="refresh"' not in d}  # skip redirect stubs
    exists = set(all_pages)
    src = sources()
    report = []
    for url, doc in all_pages.items():
        def bad(msg): problems.append(f"{url}: {msg}")
        if src.get(url, {}).get("keyword"):
            d, c, w = rank_math(url, doc, src[url], bad)
            report.append(f"  {url:<32} '{src[url]['keyword']}' {c}x / {w} words = {d:.2f}%")
        title = html.unescape(re.search(r"<title>(.*?)</title>", doc, re.S).group(1))
        desc = html.unescape(re.search(r'<meta name="description" content="([^"]*)"', doc).group(1))
        if not url.endswith("/404.html"):
            if not 40 <= len(title) <= 62: bad(f"title {len(title)} chars: {title}")
            if not 120 <= len(desc) <= 160: bad(f"description {len(desc)} chars")
            if '<link rel="canonical"' not in doc: bad("no canonical")
        n_h1 = len(re.findall(r"<h1[\s>]", doc))
        if n_h1 != 1: bad(f"{n_h1} H1")
        for tag in ("og:title", "og:description", "og:image", "og:url"):
            if f'property="{tag}"' not in doc: bad(f"missing {tag}")
        og = re.search(r'property="og:image" content="([^"]+)"', doc).group(1)
        if not os.path.exists(os.path.join(ROOT, og[len(BASE) + 1:])): bad(f"og image missing {og}")
        for block in re.findall(r'<script type="application/ld\+json">(.*?)</script>', doc, re.S):
            try: json.loads(block)
            except ValueError as e: bad(f"JSON-LD invalid: {e}")
        main_part = doc[doc.find("<main"):doc.find("</main>")]
        heads_txt = " ".join(re.sub(r"<[^>]+>", " ", h) for h in re.findall(r"<h[1-3][^>]*>(.*?)</h[1-3]>", main_part, re.S))
        for label, txt in (("title", title), ("description", desc), ("headings", heads_txt), ("url", url), ("focus keyword", src.get(url, {}).get("keyword", ""))):
            m = DENY.search(txt)
            if m: bad(f"keyword policy: '{m.group(0)}' in {label} (commercial-intent keywords only)")
        text = re.sub(r"<[^>]+>", " ", re.sub(r"<script.*?</script>", " ", main_part, flags=re.S))
        for m in BANNED.finditer(text): bad(f"banned phrase: {m.group(0)}")
        ph += [(url, p) for p in re.findall(r"\[PLACEHOLDER:[^\]]*\]", doc)]
        internal = set()
        for href in re.findall(r'href="([^"#?]+)', doc):
            if href.startswith(BASE): href = href[len(BASE):] or "/"
            if not href.startswith("/") or href.startswith("//") or href.startswith("/assets") or "." in href.rsplit("/", 1)[-1]:
                continue
            if href not in exists: bad(f"broken link {href}")
            if href != url: internal.add(href)
        body_links = {h for h in re.findall(r'href="((?:%s)?/[^"#?]*)"' % re.escape(BASE), main_part)}
        if not url.endswith("/404.html") and "noindex" not in doc[:4000] and url not in ("/oppaat/", "/en/guides/") and len(body_links) < 3: bad(f"only {len(body_links)} internal links in content")
        for h in internal: linked.setdefault(h, set()).add(url)
    # AI-search readiness: crawlers allowed, llms.txt present, a quotable answer on every keyword page
    robots = open(os.path.join(ROOT, "robots.txt"), encoding="utf-8").read()
    for bot in ("GPTBot", "OAI-SearchBot", "ClaudeBot", "PerplexityBot", "Google-Extended"):
        if bot not in robots: problems.append(f"robots.txt: {bot} not explicitly allowed")
    if not os.path.exists(os.path.join(ROOT, "llms.txt")): problems.append("llms.txt missing")
    for url, m in src.items():
        if m.get("keyword") and url not in ("/", "/en/") and 'class="kort"' not in all_pages.get(url, ""):
            problems.append(f"{url}: GEO: no 'Kort svar' answer box")
    for home in ("/", "/en/"):
        if 'class="facts"' not in all_pages.get(home, ""): problems.append(f"{home}: GEO: no facts list")
    for url in exists:
        if url not in ("/", "/en/", "/404.html", "/en/404.html") and not linked.get(url):
            problems.append(f"{url}: orphan (no page links to it)")
    print(f"{len(exists)} pages checked, {len(problems)} problems, {len(ph)} placeholders")
    if "--rm" in sys.argv:
        print("\n".join(sorted(report)))
    for p in problems: print("  FAIL", p)
    if "--placeholders" in sys.argv:
        seen = {}
        for u, p in ph: seen.setdefault(p, set()).add(u)
        for p, us in seen.items(): print(f"  {p}  ->  {', '.join(sorted(us))}")
    sys.exit(1 if problems else 0)

if __name__ == "__main__":
    main()
