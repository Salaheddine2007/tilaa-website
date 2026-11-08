"""Publish one blog post on a static (ex-WordPress) site.

Lives in each site repo as tools/publish_post.py, next to tools/site.json, tools/posts.json
and tools/post_template.html (a copy of one existing post page, used as the layout).

  python3 tools/publish_post.py --keyword "iptv suomi" --slug iptv-suomi \
      --title "Iptv Suomi" --meta-title "..." --meta-desc "..." --article /tmp/article.html

What it does (what WordPress + Rank Math used to do):
  - builds <slug>/index.html from tools/post_template.html (same header/hero/footer/design)
  - writes title, meta description, canonical, Open Graph, Twitter and JSON-LD
    (BlogPosting + BreadcrumbList, + FAQPage when the article has an FAQ section)
  - adds the URL to sitemap.xml and records it in tools/posts.json
"""
import argparse, html, json, os, re, sys
from datetime import datetime, timezone

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TOOLS = os.path.join(REPO, "tools")


def load(name):
    with open(os.path.join(TOOLS, name), encoding="utf-8") as f:
        return json.load(f)


def text_of(s):
    return html.unescape(re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", s))).strip()


def faq_pairs(article):
    m = re.search(r"<h2[^>]*>[^<]*(FAQ|Veelgestelde|Veel gestelde|Usein kysy|Kysymyks)[^<]*</h2>(.*?)(?=<h2|\Z)",
                  article, re.I | re.S)
    if not m:
        return []
    pairs = []
    for q, a in re.findall(r"<h3[^>]*>(.*?)</h3>(.*?)(?=<h3|\Z)", m.group(2), re.S):
        q, a = text_of(q), text_of(a)
        if q and a:
            pairs.append((q, a))
    return pairs


def schema(site, url, title, desc, now, article):
    org = {"@type": "Organization", "@id": f"{site['base']}/#organization", "name": site["name"], "url": site["base"]}
    graph = [
        org,
        {"@type": "WebSite", "@id": f"{site['base']}/#website", "url": site["base"], "name": site["name"],
         "publisher": {"@id": f"{site['base']}/#organization"}, "inLanguage": site["lang"]},
        {"@type": "BreadcrumbList", "@id": f"{url}#breadcrumb", "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "Home", "item": site["base"] + "/"},
            {"@type": "ListItem", "position": 2, "name": title, "item": url}]},
        {"@type": "WebPage", "@id": f"{url}#webpage", "url": url, "name": title, "datePublished": now,
         "dateModified": now, "isPartOf": {"@id": f"{site['base']}/#website"}, "inLanguage": site["lang"],
         "breadcrumb": {"@id": f"{url}#breadcrumb"}},
        {"@type": "BlogPosting", "@id": f"{url}#article", "headline": title, "description": desc,
         "datePublished": now, "dateModified": now, "author": {"@id": f"{site['base']}/#organization"},
         "publisher": {"@id": f"{site['base']}/#organization"}, "mainEntityOfPage": {"@id": f"{url}#webpage"},
         "inLanguage": site["lang"], "wordCount": len(text_of(article).split())},
    ]
    qa = faq_pairs(article)
    if qa:
        graph.append({"@type": "FAQPage", "@id": f"{url}#faq", "mainEntity": [
            {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in qa]})
    data = json.dumps({"@context": "https://schema.org", "@graph": graph}, ensure_ascii=False)
    return f'<script class="rank-math-schema" type="application/ld+json">{data}</script>', len(qa)


def set_content(doc, attr, name, value):
    """<meta content="..." name="description"/> (content first, as in these pages)"""
    pat = re.compile(r'(<meta content=")[^"]*(" %s="%s"\s*/?>)' % (attr, re.escape(name)))
    doc, n = pat.subn(lambda m: m.group(1) + value + m.group(2), doc, count=1)
    if not n:
        sys.exit(f"ERROR: template has no meta {attr}={name}")
    return doc


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--keyword", required=True); ap.add_argument("--slug", required=True)
    ap.add_argument("--title", required=True); ap.add_argument("--meta-title", required=True)
    ap.add_argument("--meta-desc", required=True); ap.add_argument("--article", default="article.html")
    a = ap.parse_args()

    site, posts = load("site.json"), load("posts.json")
    page = os.path.join(REPO, a.slug, "index.html")
    if os.path.exists(page):
        sys.exit(f"ERROR: /{a.slug}/ already exists - pick the next keyword")
    article = open(a.article, encoding="utf-8").read().strip()
    # the hero already carries the H1 -> no H1 inside the article body
    article = re.sub(r"<h1\b[^>]*>.*?</h1>\s*", "", article, flags=re.S | re.I)
    n_words = len(text_of(article).split())
    min_words = int(site.get("min_words", 2000))
    if n_words < min_words:
        sys.exit(f"ERROR: article has {n_words} words, minimum is {min_words}. Expand the article "
                 "(more depth per section, more H3 subsections, longer FAQ answers) and run this command again.")

    url = f"{site['base']}/{a.slug}/"
    now = datetime.now(timezone.utc).replace(microsecond=0).isoformat()
    title, mt, md = (html.escape(x, quote=True) for x in (a.title, a.meta_title, a.meta_desc))
    doc = open(os.path.join(TOOLS, "post_template.html"), encoding="utf-8").read()

    # ---- head ----
    doc, n = re.subn(r"<title>.*?</title>", lambda m: f"<title>{mt}</title>", doc, count=1, flags=re.S)
    if not n:
        sys.exit("ERROR: template has no <title>")
    doc = set_content(doc, "name", "description", md)
    doc, n = re.subn(r'<link href="[^"]*" rel="canonical"\s*/?>', lambda m: f'<link href="{url}" rel="canonical"/>', doc, count=1)
    if not n:
        sys.exit("ERROR: template has no canonical link")
    for attr, name, val in (("property", "og:title", mt), ("property", "og:description", md), ("property", "og:url", url),
                            ("name", "twitter:title", mt), ("name", "twitter:description", md),
                            ("property", "article:published_time", now)):
        doc = set_content(doc, attr, name, val)
    doc = re.sub(r'(<meta content=")[^"]*(" property="(?:og:updated_time|article:modified_time)"\s*/?>)',
                 lambda m: m.group(1) + now + m.group(2), doc)
    doc = re.sub(r'<meta content="[^"]*" property="og:image[^"]*"\s*/?>\s*', "", doc)
    doc = re.sub(r'<meta content="[^"]*" name="twitter:image"\s*/?>\s*', "", doc)
    ld, n_faq = schema(site, url, a.title, a.meta_desc, now, article)
    doc, n = re.subn(r'<script class="rank-math-schema" type="application/ld\+json">.*?</script>', lambda m: ld, doc, count=1, flags=re.S)
    if not n:
        sys.exit("ERROR: template has no rank-math JSON-LD block")

    # ---- body: hero H1, date line, article ----
    body_at = doc.index("<body")
    head, body = doc[:body_at], doc[body_at:]
    body, n = re.subn(r"(<h1\b[^>]*>).*?(</h1>)", lambda m: m.group(1) + title + m.group(2), body, count=1, flags=re.S)
    if not n:
        sys.exit("ERROR: template has no <h1>")
    d = datetime.now(timezone.utc)
    meta_line = f"{d.strftime('%d.%m.%Y')} · ~{max(1, round(n_words / 220))} {site['read_label']}"
    body = re.sub(r'(<span class="(?:post-meta|tp-post-meta)">)[^<]*(</span>)', lambda m: m.group(1) + meta_line + m.group(2), body, count=1)
    body, n = re.subn(r'(<article class="%s">).*?(</article>)' % re.escape(site["article_class"]),
                      lambda m: m.group(1) + "\n" + article + "\n" + m.group(2), body, count=1, flags=re.S)
    if not n:
        sys.exit("ERROR: template has no <article> block")
    # the template's "related posts" box points at the template post's neighbours -> drop it
    body = re.sub(r'<section class="post-related">.*?</section>', "", body, count=1, flags=re.S)
    os.makedirs(os.path.dirname(page), exist_ok=True)
    open(page, "w", encoding="utf-8").write(head + body)

    # ---- sitemap + registry ----
    sm_path = os.path.join(REPO, "sitemap.xml")
    sm = open(sm_path, encoding="utf-8").read()
    if url not in sm:
        sm = sm.replace("</urlset>", f"  <url><loc>{url}</loc><lastmod>{now[:10]}</lastmod></url>\n</urlset>")
        open(sm_path, "w", encoding="utf-8").write(sm)
    posts.append({"slug": a.slug, "url": url, "title": a.title, "keyword": a.keyword, "date": now[:10]})
    with open(os.path.join(TOOLS, "posts.json"), "w", encoding="utf-8") as f:
        json.dump(posts, f, ensure_ascii=False, indent=1)
    print(f"PUBLISHED {url} | words={n_words} | faq_schema={n_faq}")


if __name__ == "__main__":
    main()
