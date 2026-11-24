"""Publish one article: writes tools/posts/<lang>/<slug>.html, rebuilds the site and runs QA.

Usage:
  python tools/publish_post.py --lang en --keyword "iptv on chromebook" --slug iptv-on-chromebook \
      --h1 "IPTV on Chromebook: ..." --title "<= 62 chars, keyword first, one number" --desc "120-160 chars with the keyword" \
      --crumb "Short name" --tldr "2-3 sentence answer" --source "Label|https://official-help-page" --article /tmp/article.html [--alt other-lang-slug]

The article file is the body only (no <html>, no <h1>; the H1 comes from --h1). English posts live under /en/guides/<slug>/,
Norwegian posts under /guider/<slug>/.
Refuses (exit 1, nothing written) when: slug exists, fewer than site.json min_words, no link to the home trunk
(en: href="/en/", fi: href="/"), no link to the plans page, no external link, an <h1> in the body, the keyword in too many
headings, an unverifiable claim, a keyword-policy violation (free / playlist / review / box / ...), or QA fails after the build.
Prints "PUBLISHED <url> | words=N" on success.
"""
import argparse, json, os, re, subprocess, sys
from datetime import date

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TOOLS = os.path.join(ROOT, "tools")
SITE = json.load(open(os.path.join(TOOLS, "site.json"), encoding="utf-8"))
POLICY = json.load(open(os.path.join(TOOLS, "keyword_policy.json"), encoding="utf-8"))
DENY = re.compile(POLICY["deny_regex"], re.I)
TRUNK = {"en": '/en/', "fi": '/'}
PLANS = {"en": "/en/iptv-subscription-finland/", "fi": "/iptv-hinta/"}
BLOG = {"en": "/en/guides/", "fi": "/oppaat/"}
CLAIMS = re.compile(
    r"(?i)most (?:of our )?customers|our customers (?:use|choose|say|prefer)|within \d+ minutes|in under \d+ minutes|same[- ]day|"
    r"\d+ ?% of (?:our|all)|guaranteed|99[.,]9|"
    r"de fleste (?:av )?(?:våre )?kunde|kundene våre (?:bruker|velger|sier)|innen \d+ minutter|på under \d+ minutter|samme dag|"
    r"\d+ ?% av (?:våre|alle)|garantert|"
    r"\b(?:fully |100% )?licensed\b|\blisensiert\b|\bNRK\b.{0,40}(?:included|inkludert|med i)|(?:included|inkludert).{0,40}\bNRK\b")

def fail(msg):
    print("ERROR:", msg)
    sys.exit(1)

def main():
    ap = argparse.ArgumentParser()
    for a in ("lang", "keyword", "slug", "h1", "title", "desc", "crumb", "tldr", "article"):
        ap.add_argument("--" + a, required=True)
    ap.add_argument("--alt", default=None, help="slug of the same article in the other language, if it exists")
    ap.add_argument("--source", action="append", default=[], help='"Label|https://url", repeat 1-4 times')
    a = ap.parse_args()
    if a.lang not in ("en", "fi"):
        fail("--lang must be en or fi")
    if not re.fullmatch(r"[a-z0-9]+(-[a-z0-9]+)*", a.slug):
        fail(f"bad slug {a.slug!r}")
    src = os.path.join(TOOLS, "posts", a.lang, a.slug + ".html")
    if os.path.exists(src) or os.path.exists(os.path.join(TOOLS, "pages", a.lang, a.slug + ".html")):
        fail(f"slug {a.slug} already exists")
    body = open(a.article, encoding="utf-8").read().strip()
    body = re.sub(r"(?is)^.*?<body[^>]*>|</body>.*$", "", body)
    # attribute values in single quotes -> double quotes, so the link checks below and tools/qa.py see every href
    body = re.sub(r"<[^>]*>", lambda m: re.sub(r"(\s[\w:-]+)='([^'\"]*)'", lambda a: a.group(1) + '="' + a.group(2) + '"', m.group(0)), body)
    if re.search(r"<h1[\s>]", body, re.I):
        fail("article body must not contain <h1> (pass it with --h1)")
    words = len(re.sub(r"<[^>]+>", " ", body).split())
    if words < SITE["min_words"]:
        fail(f"only {words} words, minimum is {SITE['min_words']}")
    trunk = TRUNK[a.lang]
    if not re.search(r'href="(?:%s)?%s"' % (re.escape(SITE["base"]), re.escape(trunk)), body):
        fail(f'no link to the home trunk (href="{trunk}", anchor text with the focus keyword)')
    if PLANS[a.lang] not in body:
        fail(f"no link to {PLANS[a.lang]}")
    if not re.search(r'href="https?://(?!(www\.)?tilaaiptv\.com|api\.whatsapp)', body):
        fail("no external link (link to an official help page)")
    heads = [re.sub(r"<[^>]+>", "", h).lower() for h in re.findall(r"<h[23][^>]*>(.*?)</h[23]>", body, re.S)]
    kw_heads = sum(a.keyword.lower() in h for h in heads)
    if kw_heads > max(3, len(heads) // 4):
        fail(f"keyword in {kw_heads} of {len(heads)} headings - keep it in 2-3, write the rest naturally")
    if not any(a.keyword.lower() in h for h in heads):
        fail("keyword must appear in at least one H2/H3")
    claims = CLAIMS.findall(body)
    if claims:
        fail(f"unverifiable claim(s): {claims} - only use confirmed facts (see site.json facts)")
    for label, txt in (("keyword", a.keyword), ("slug", a.slug), ("title", a.title), ("description", a.desc), ("h1", a.h1), ("headings", " ".join(heads))):
        m = DENY.search(txt)
        if m:
            fail(f"keyword policy: '{m.group(0)}' in {label}. Commercial-intent keywords only (no free/playlist/review/box/...)")
    sources = []
    for s in a.source:
        label, _, url = s.partition("|")
        if not (label.strip() and re.match(r"https://", url.strip())):
            fail(f'bad --source {s!r}, use "Label|https://url"')
        sources.append([label.strip(), url.strip()])
    today = date.today().isoformat()
    meta = {"slug": a.slug, "tldr": a.tldr, "crumb": a.crumb, "keyword": a.keyword, "date": today, "updated": today,
            "h1": a.h1, "title": a.title, "desc": a.desc}
    if a.alt:
        meta["alt"] = a.alt
    if sources:
        meta["sources"] = sources
    os.makedirs(os.path.dirname(src), exist_ok=True)
    open(src, "w", encoding="utf-8", newline="\n").write("<!--" + json.dumps(meta, ensure_ascii=False) + "-->\n" + body + "\n")
    build = subprocess.run([sys.executable, os.path.join(TOOLS, "build_site.py")], capture_output=True, text=True)
    qa = subprocess.run([sys.executable, os.path.join(TOOLS, "qa.py")], capture_output=True, text=True)
    if build.returncode or qa.returncode:
        os.remove(src)
        subprocess.run([sys.executable, os.path.join(TOOLS, "build_site.py")], capture_output=True)
        fail("build/QA failed, post removed:\n" + build.stdout + build.stderr + qa.stdout + qa.stderr)
    print(f"PUBLISHED {SITE['base']}{BLOG[a.lang]}{a.slug}/ | words={words}")

if __name__ == "__main__":
    main()
