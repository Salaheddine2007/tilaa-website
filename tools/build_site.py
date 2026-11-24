"""Build every page of iptvnorwayone.com in two languages: English at / and Norwegian (bokmål) at /no/.

Sources:  tools/pages/<lang>/*.html   fixed pages
          tools/posts/<lang>/*.html   articles (live under /guides/<slug>/ and /no/guider/<slug>/)
Each source = JSON header in an HTML comment, then the body:
  <!--{"slug": "iptv-plans", "alt": "iptv-abonnement", "title": "...", "desc": "...", "crumb": "Plans", "keyword": "...", "tldr": "..."}-->
"alt" = slug of the same page in the other language (hreflang + language switcher). No "alt" = switcher goes to the other home page.
Body helpers: {{WA:message}} WhatsApp order link, {{I:name}} inline SVG icon, <!--DEVICES--> device picker, <!--PRICETABLE--> price table,
<!--TOC--> / <!--FIGURE--> / <!--IMG:name--> Rank Math helpers.
Writes pages, blog indexes, sitemap.xml (with hreflang), llms.txt, robots.txt and OG cards. Usage: python tools/build_site.py
"""
import hashlib, html, json, os, re, sys, unicodedata
from urllib.parse import quote

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TOOLS = os.path.join(ROOT, "tools")
sys.path.insert(0, TOOLS)
import make_og

SITE = json.load(open(os.path.join(TOOLS, "site.json"), encoding="utf-8"))
BASE = SITE["base"]

LANGS = {
    "en": dict(prefix="/en", html="en", blog="guides",
               months=["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"],
               home="Home", crumbs="Breadcrumbs", guide="Guide", guides="Guides", published="Published", updated="Updated",
               toc="Contents", kort="Short answer", sources="Sources and official help pages", prev="Previous guide", nxt="Next guide", more="More guides",
               about="About the author", how="How we write the guides", mon={"1": "1 month", "3": "3 months", "6": "6 months", "12": "12 months"},
               one="screen", many="screens", q="How many screens do you want to watch on at the same time?", caption="All prices for 1, 2 and 3 screens",
               plan="Plan", permonth="/month", order_text="Hi! I'd like to order Tilaa IPTV: {m}, {d} ({p}).", order_aria="Order {m} for {p}, {d}",
               table="Table {n}, scrollable sideways",
               idx_title="IPTV guides for Norway: apps, installation and troubleshooting",
               idx_desc="IPTV guides for Norway: pick an app, install on Smart TV and Apple TV, get 4K to run smoothly and fix buffering. Written by our support team.",
               idx_h1="IPTV guides for Norway",
               idx_p="Installation, apps, picture quality and troubleshooting. We write about the things customers actually ask us. Prices are on the <a href=\"/en/iptv-subscription-finland/\">IPTV plans page</a>.",
               blogname="Guides - Tilaa IPTV",
               org_desc="Tilaa IPTV sells IPTV subscriptions with Finnish and Nordic channels in HD to households in Finland, with ordering and support on WhatsApp.",
               wa_default="Hi! I'd like to order Tilaa IPTV.", about_slug="about", contact_slug="contact"),
    "fi": dict(prefix="", html="fi", blog="oppaat",
               months=["tammikuuta", "helmikuuta", "maaliskuuta", "huhtikuuta", "toukokuuta", "kesäkuuta", "heinäkuuta", "elokuuta", "syyskuuta", "lokakuuta", "marraskuuta", "joulukuuta"],
               home="Etusivu", crumbs="Murupolku", guide="Opas", guides="Oppaat", published="Julkaistu", updated="Päivitetty",
               toc="Sisältö", kort="Lyhyt vastaus", sources="Lähteet ja viralliset ohjesivut", prev="Edellinen opas", nxt="Seuraava opas", more="Lisää oppaita",
               about="Kirjoittajasta", how="Näin kirjoitamme oppaat", mon={"1": "1 kuukausi", "3": "3 kuukautta", "6": "6 kuukautta", "12": "12 kuukautta"},
               one="näyttö", many="näyttöä", q="Kuinka monella näytöllä katsotte yhtä aikaa?", caption="Kaikki hinnat 1, 2 ja 3 näytölle",
               plan="Paketti", permonth="/kk", order_text="Hei! Haluan tilata Tilaa IPTV:n: {m}, {d} ({p}).", order_aria="Tilaa {m} hintaan {p}, {d}",
               table="Taulukko {n}, vieritettävissä sivusuunnassa",
               idx_title="IPTV-oppaat Suomeen: sovellukset, asennus ja vianetsintä",
               idx_desc="IPTV-oppaat Suomeen: valitse sovellus, asenna Smart TV:hen ja Apple TV:hen, saa 4K toimimaan sujuvasti ja korjaa pätkimisen syyt. Tukemme kirjoittamat.",
               idx_h1="IPTV-oppaat Suomeen",
               idx_p="Asennus, sovellukset, kuvanlaatu ja vianetsintä. Kirjoitamme asioista, joita asiakkaat oikeasti kysyvät. Hinnat löytyvät <a href=\"/iptv-hinta/\">hintasivulta</a>.",
               blogname="Oppaat - Tilaa IPTV",
               org_desc="Tilaa IPTV myy IPTV-tilauksia suomalaisilla ja pohjoismaisilla kanavilla HD-laadulla suomalaisille kotitalouksille. Tilaus ja tuki WhatsAppissa.",
               wa_default="Hei! Haluan tilata Tilaa IPTV:n.", about_slug="tietoa-meista", contact_slug="yhteystiedot"),
}
OTHER = {"en": "fi", "fi": "en"}

LAYOUTS = {}
for _l in LANGS:
    _t = open(os.path.join(TOOLS, f"layout.{_l}.html"), encoding="utf-8").read()
    for _a in ("site.css", "site.js"):
        _v = hashlib.md5(open(os.path.join(ROOT, "assets", _a), "rb").read()).hexdigest()[:8]
        _t = _t.replace(f'/assets/{_a}"', f'/assets/{_a}?v={_v}"')
    LAYOUTS[_l] = _t

ICONS = {
    "check": '<path d="M20 6 9 17l-5-5"/>',
    "tv": '<rect x="2" y="7" width="20" height="15" rx="2"/><path d="m17 2-5 5-5-5"/>',
    "monitor": '<rect x="2" y="3" width="20" height="14" rx="2"/><path d="M8 21h8M12 17v4"/>',
    "phone": '<rect x="5" y="2" width="14" height="20" rx="2"/><path d="M12 18h.01"/>',
    "box": '<path d="M21 8 12 3 3 8v8l9 5 9-5z"/><path d="m3 8 9 5 9-5M12 13v8"/>',
    "globe": '<circle cx="12" cy="12" r="10"/><path d="M2 12h20M12 2a15 15 0 0 1 0 20M12 2a15 15 0 0 0 0 20"/>',
    "spark": '<path d="M12 3l1.9 5.8L20 10l-6.1 1.2L12 17l-1.9-5.8L4 10l6.1-1.2z"/>',
    "calendar": '<rect x="3" y="4" width="18" height="18" rx="2"/><path d="M16 2v4M8 2v4M3 10h18"/>',
    "film": '<rect x="3" y="3" width="18" height="18" rx="2"/><path d="M7 3v18M17 3v18M3 8h4M17 8h4M3 16h4M17 16h4"/>',
    "wifi": '<path d="M5 12.5a10 10 0 0 1 14 0M8.5 16a5 5 0 0 1 7 0M2 9a15 15 0 0 1 20 0"/><path d="M12 20h.01"/>',
    "chat": '<path d="M21 11.5a8.4 8.4 0 0 1-9 8.4 9 9 0 0 1-4-1L3 20l1.2-4.4A8.4 8.4 0 1 1 21 11.5z"/>',
    "shield": '<path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/><path d="m9 12 2 2 4-4"/>',
    "laptop": '<path d="M4 16V6a2 2 0 0 1 2-2h12a2 2 0 0 1 2 2v10M2 20h20"/>',
    "zap": '<path d="M13 2 3 14h9l-1 8 10-12h-9z"/>',
    "x": '<path d="M18 6 6 18M6 6l12 12"/>',
}

def icon(name):
    return f'<svg class="icon" viewBox="0 0 24 24" aria-hidden="true">{ICONS[name]}</svg>'

def wa(msg):
    return f"https://api.whatsapp.com/send/?phone={SITE['whatsapp']}&amp;text={quote(msg)}"

def nice_date(iso, lang):
    y, m, d = iso[:10].split("-")
    mn = LANGS[lang]["months"][int(m) - 1]
    return f"{mn} {int(d)}, {y}" if lang == "en" else f"{int(d)}. {mn} {y}"

def read_source(path):
    raw = open(path, encoding="utf-8").read()
    m = re.match(r"\s*<!--(\{.*?\})-->\s*", raw, re.S)
    return json.loads(m.group(1)), raw[m.end():]

def base_url(lang):
    return BASE + LANGS[lang]["prefix"] + "/"

def page_url(lang, slug):
    return base_url(lang) + (slug + "/" if slug else "")

def post_url(lang, slug):
    return base_url(lang) + LANGS[lang]["blog"] + "/" + slug + "/"

def blog_url(lang):
    return base_url(lang) + LANGS[lang]["blog"] + "/"

def price_data(lang):
    """every price in both currencies; the language decides which one is primary"""
    eur = SITE["prices_eur"]; nok = SITE.get("prices_local")
    out = {}
    for d in eur:
        out[d] = {}
        for m in eur[d]:
            e = eur[d][m]
            if lang == "fi":
                p, pm = f"{e:.2f}".replace(".", ","), f"{e / int(m):.2f}".replace(".", ",")
                out[d][m] = {"p": p, "pm": pm, "s": "", "pt": f"{p} €"}
            else:
                out[d][m] = {"p": f"{e:.2f}", "pm": f"{e / int(m):.2f}", "s": "", "pt": f"€{e:.2f}"}
    return out

def devices(body, lang):
    L = LANGS[lang]
    pd = price_data(lang)
    if "<!--DEVICES-->" in body:
        btns = "".join(f'<button type="button" role="radio" aria-checked="{str(d == "1").lower()}" tabindex="{0 if d == "1" else -1}" data-dev="{d}">'
                       f'<b>{d}</b> {L["one"] if d == "1" else L["many"]}</button>' for d in pd)
        cfg = {"prices": pd, "mon": L["mon"], "one": L["one"], "many": L["many"], "order": L["order_text"], "aria": L["order_aria"]}
        pick = (f'<div class="dev-pick"><p class="dev-q" id="dev-q">{L["q"]}</p>'
                f'<div class="seg" role="radiogroup" aria-labelledby="dev-q">{btns}</div></div>'
                f'<script type="application/json" id="prices">{json.dumps(cfg, ensure_ascii=False)}</script>')
        body = body.replace("<!--DEVICES-->", pick, 1)
    if "<!--PRICETABLE-->" in body:
        heads = "".join(f'<th scope="col">{d} {L["one"] if d == "1" else L["many"]}</th>' for d in pd)
        rows = "".join(f'<tr><th scope="row">{name}</th>' + "".join(
            f'<td>{pd[d][m]["pt"]}' + (f'<small>{"€" if lang == "en" else ""}{pd[d][m]["pm"]}{" €" if lang == "fi" else ""}{L["permonth"]}</small>' if m != "1" else "") + '</td>'
            for d in pd) + '</tr>' for m, name in L["mon"].items())
        table = (f'<div class="table-wrap"><table class="dev-table"><caption>{L["caption"]}</caption>'
                 f'<thead><tr><th scope="col">{L["plan"]}</th>{heads}</tr></thead><tbody>{rows}</tbody></table></div>')
        body = body.replace("<!--PRICETABLE-->", table, 1)
    return body

def org(lang):
    L = LANGS[lang]
    return {"@context": "https://schema.org", "@type": "Organization", "@id": BASE + "/#org", "name": SITE["name"], "url": BASE + "/",
            "logo": BASE + "/assets/icons/icon-512.png", "areaServed": "FI", "description": L["org_desc"],
            "knowsAbout": ["IPTV", "IPTV Suomi", "IPTV Finland", "Smart TV", "Apple TV", "Android TV", "Fire TV Stick", "EPG"],
            "contactPoint": {"@type": "ContactPoint", "contactType": "customer support", "availableLanguage": ["fi", "en"],
                             "url": page_url(lang, L["contact_slug"])}}

def website():
    return {"@context": "https://schema.org", "@type": "WebSite", "@id": BASE + "/#site", "name": SITE["name"], "url": BASE + "/",
            "inLanguage": ["fi", "en"], "publisher": {"@id": BASE + "/#org"}}

def crumbs(lang, trail):
    L = LANGS[lang]
    if not trail:
        return "", None
    full = [(L["home"], base_url(lang))] + trail
    items = "".join(
        f'<li><a href="{u}">{html.escape(n)}</a></li>' if i < len(full) - 1 else f'<li aria-current="page">{html.escape(n)}</li>'
        for i, (n, u) in enumerate(full))
    schema = {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": i + 1, "name": n, "item": u} for i, (n, u) in enumerate(full)]}
    return f'<nav class="crumbs" aria-label="{L["crumbs"]}"><ol class="wrap">{items}</ol></nav>', schema

def hreflangs(alts):
    tags = "".join(f'<link rel="alternate" hreflang="{LANGS[l]["html"]}" href="{u}">' for l, u in alts.items())
    return tags + f'<link rel="alternate" hreflang="x-default" href="{alts["fi"]}">'

def page(lang, meta, body, url, trail, og_name, extra_schema=(), og_type="website", alts=None):
    L = LANGS[lang]
    crumb_html, crumb_schema = crumbs(lang, trail)
    schema = [org(lang), website()] + ([crumb_schema] if crumb_schema else []) + list(extra_schema)
    if meta.get("tldr") or meta.get("speakable"):
        schema.append({"@context": "https://schema.org", "@type": "WebPage", "@id": url + "#webpage", "url": url, "name": meta["title"],
                       "inLanguage": L["html"], "isPartOf": {"@id": BASE + "/#site"}, "dateModified": meta.get("updated", SITE["launched"]),
                       "speakable": {"@type": "SpeakableSpecification", "cssSelector": [".kort", ".facts", "h1"]}})
    head = "\n".join(f'<script type="application/ld+json">{json.dumps(s, ensure_ascii=False)}</script>' for s in schema)
    if alts:
        head = hreflangs(alts) + "\n" + head
    alt_url = (alts or {}).get(OTHER[lang]) or base_url(OTHER[lang])
    body = devices(body, lang)
    body = re.sub(r"\{\{WA:([^}]*)\}\}", lambda m: wa(m.group(1)), body)
    body = re.sub(r"\{\{I:([a-z]+)\}\}", lambda m: icon(m.group(1)), body)
    out = LAYOUTS[lang]
    for k, v in {"TITLE": html.escape(meta["title"]), "DESC": html.escape(meta["desc"]), "URL": url, "OG_TYPE": og_type,
                 "ROBOTS": meta.get("robots", "index, follow, max-image-preview:large"), "HEAD": head,
                 "OG_IMAGE": f"{BASE}/assets/og/{og_name}.png", "CRUMBS": crumb_html, "ALT": alt_url,
                 "WA_DEFAULT": wa(L["wa_default"]), "WA_DISPLAY": SITE["whatsapp_display"], "BODY": body}.items():
        out = out.replace("{{%s}}" % k, v)
    n = iter(range(1, 99))
    out = re.sub(r'<div class="table-wrap">', lambda m: f'<div class="table-wrap" tabindex="0" role="region" aria-label="{L["table"].format(n=next(n))}">', out)
    path = "/" + url[len(BASE):].lstrip("/")
    if path != L["prefix"] + "/":
        out = out.replace(f'<a href="{path}">', f'<a href="{path}" aria-current="page">', 1)
    return out

def slug_id(text):
    t = unicodedata.normalize("NFKD", html.unescape(re.sub(r"<[^>]+>", "", text))).encode("ascii", "ignore").decode().lower()
    return re.sub(r"[^a-z0-9]+", "-", t).strip("-")[:60]

def kort(meta, lang):
    return (f'<aside class="kort" aria-label="{LANGS[lang]["kort"]}"><div class="kort-title">{LANGS[lang]["kort"]}</div>'
            f'<p>{html.escape(meta["tldr"])}</p></aside>')

def enrich(body, meta, og_name, lang):
    """ids on H2s, a short-answer box, a table of contents and a featured image whose alt text carries the keyword"""
    L = LANGS[lang]
    tldr_done = False
    if meta.get("tldr") and "<!--TOC-->" in body:
        body = body.replace("<!--TOC-->", kort(meta, lang) + "<!--TOC-->", 1); tldr_done = True
    seen = set()
    def add_id(m):
        if "id=" in m.group(1):
            return m.group(0)
        i = slug_id(m.group(2)) or "section"
        while i in seen:
            i += "-2"
        seen.add(i)
        return f'<h2{m.group(1)} id="{i}">{m.group(2)}</h2>'
    body = re.sub(r"<h2([^>]*)>(.*?)</h2>", add_id, body, flags=re.S)
    if not meta.get("keyword"):
        return body
    heads = [(i, h) for i, h in re.findall(r'<h2[^>]*id="([^"]+)"[^>]*>(.*?)</h2>', body, re.S) if "Read on" not in h and "Les videre" not in h]
    block = ""
    if meta.get("toc", True) and len(heads) >= 4:
        items = "".join(f'<li><a href="#{i}">{re.sub(r"<[^>]+>", "", t).strip()}</a></li>' for i, t in heads)
        block += f'<nav class="toc" aria-label="{L["toc"]}"><p class="toc-title">{L["toc"]}</p><ol>{items}</ol></nav>'
    fig = (f'<figure class="feature"><img src="/assets/og/{og_name}.webp" width="1200" height="630" loading="lazy" decoding="async" '
           f'alt="{html.escape(meta.get("img_alt") or meta["keyword"].capitalize() + ": " + meta.get("h1", meta["title"]))}"></figure>')
    for im in meta.get("images", []):
        body = body.replace(f"<!--IMG:{im['name']}-->",
            f'<figure class="feature"><img src="/assets/og/{im["name"]}.webp" width="1200" height="630" loading="lazy" '
            f'decoding="async" alt="{html.escape(im["alt"])}"></figure>', 1)
    if "<!--FIGURE-->" in body:
        body = body.replace("<!--FIGURE-->", fig, 1)
    else:
        block = fig + block
    if "<!--TOC-->" in body:
        return body.replace("<!--TOC-->", block, 1)
    i = body.find("</p>")
    body = body[:i + 4] + block + body[i + 4:] if i >= 0 else block + body
    return (kort(meta, lang) + body) if meta.get("tldr") and not tldr_done else body

def write(rel, text):
    path = os.path.join(ROOT, *rel.split("/"))
    os.makedirs(os.path.dirname(path), exist_ok=True)
    open(path, "w", encoding="utf-8", newline="\n").write(text)

def out_dir(lang):
    p = LANGS[lang]["prefix"].strip("/")
    return p + "/" if p else ""

def load_pages(lang):
    d = os.path.join(TOOLS, "pages", lang)
    return [read_source(os.path.join(d, fn)) for fn in sorted(os.listdir(d))] if os.path.isdir(d) else []

def load_posts(lang):
    d = os.path.join(TOOLS, "posts", lang)
    posts = []
    for fn in sorted(os.listdir(d)) if os.path.isdir(d) else []:
        meta, body = read_source(os.path.join(d, fn))
        meta["url"] = post_url(lang, meta["slug"])
        posts.append((meta, body))
    posts.sort(key=lambda p: (p[0]["date"], p[0]["slug"]))
    return posts

def article(lang, meta, body, prev, nxt):
    L = LANGS[lang]
    updated = meta.get("updated", meta["date"])
    about = page_url(lang, L["about_slug"])
    head = (f'<section class="page-head"><div class="wrap"><span class="eyebrow">{L["guide"]}</span><h1>{html.escape(meta["h1"])}</h1>'
            f'<p class="post-meta">{L["published"]} <time datetime="{meta["date"]}">{nice_date(meta["date"], lang)}</time>'
            f' · {L["updated"]} <time datetime="{updated}">{nice_date(updated, lang)}</time></p></div></section>')
    bio = SITE["author"].get("bio_" + lang, "")
    author = (f'<aside class="author" aria-label="{L["about"]}"><img class="author-pic" src="/assets/icons/mark.svg" width="56" height="56" alt=""><div>'
              f'<p><strong>{html.escape(SITE["author"]["name"])}</strong></p><p>{bio} <a href="{about}#how-we-write">{L["how"]}</a>.</p></div></aside>')
    sources = ""
    if meta.get("sources"):
        items = "".join(f'<li><a href="{html.escape(u)}" target="_blank" rel="noopener">{html.escape(n)}</a></li>' for n, u in meta["sources"])
        sources = f'<aside class="sources" aria-label="{L["sources"]}"><p class="sources-h">{L["sources"]}</p><ul>{items}</ul></aside>'
    pn = ""
    if prev or nxt:
        pn = f'<nav class="pn" aria-label="{L["more"]}">'
        if prev:
            pn += f'<a class="prev" href="{prev["url"]}" rel="prev"><small>{L["prev"]}</small>{html.escape(prev["h1"])}</a>'
        if nxt:
            pn += f'<a class="next" href="{nxt["url"]}" rel="next"><small>{L["nxt"]}</small>{html.escape(nxt["h1"])}</a>'
        pn += "</nav>"
    return f'{head}<div class="wrap"><article class="prose">{body}{sources}{author}{pn}</article></div>'

def article_schema(lang, meta):
    return {"@context": "https://schema.org", "@type": "Article", "headline": meta["h1"], "description": meta["desc"],
            "inLanguage": LANGS[lang]["html"], "datePublished": meta["date"], "dateModified": meta.get("updated", meta["date"]),
            "mainEntityOfPage": meta["url"], "image": f"{BASE}/assets/og/{lang}-blog-{meta['slug']}.png",
            "author": {"@type": SITE["author"]["type"], "name": SITE["author"]["name"], "url": page_url(lang, LANGS[lang]["about_slug"])},
            "publisher": {"@id": BASE + "/#org"}}

def blog_index(lang, posts):
    L = LANGS[lang]
    items = "".join(
        f'<li><a href="{m["url"]}"><time datetime="{m["date"]}">{nice_date(m["date"], lang)}</time>'
        f'<h2>{html.escape(m["h1"])}</h2><p>{html.escape(m["desc"])}</p></a></li>' for m, _ in reversed(posts))
    body = (f'<section class="page-head"><div class="wrap"><span class="eyebrow">{L["guides"]}</span><h1>{L["idx_h1"]}</h1><p>{L["idx_p"]}</p></div></section>'
            f'<div class="wrap"><ul class="posts">{items}</ul></div>')
    meta = {"title": L["idx_title"], "desc": L["idx_desc"]}
    if not posts:
        meta["robots"] = "noindex, follow"
    return page(lang, meta, body, blog_url(lang), [(L["guides"], blog_url(lang))], f"{lang}-blog",
                [{"@context": "https://schema.org", "@type": "Blog", "name": L["blogname"], "url": blog_url(lang), "inLanguage": L["html"]},
                 {"@context": "https://schema.org", "@type": "ItemList", "itemListElement": [
                     {"@type": "ListItem", "position": i + 1, "url": m["url"], "name": m["h1"]} for i, (m, _) in enumerate(posts)]}],
                alts={"en": blog_url("en"), "fi": blog_url("fi")})

def llms_txt(pages_by_lang, posts_by_lang):
    out = [f"# {SITE['name']}", "", "> Tilaa IPTV sells IPTV subscriptions with Finnish and Nordic channels in HD to households in Finland. "
           "Ordering, payment and installation help happen on WhatsApp. The site is available in Finnish (/) and English (/en/).", "", "## Facts", ""]
    out += [f"- {k}: {v}" for k, v in SITE.get("facts", [])]
    for lang in ("fi", "en"):
        out += ["", f"## Pages ({LANGS[lang]['html']})", ""] + [f"- [{t}]({u}): {d}" for t, u, d in pages_by_lang[lang]]
        out += ["", f"## Guides ({LANGS[lang]['html']})", ""] + [f"- [{m['h1']}]({m['url']}): {m.get('tldr') or m['desc']}" for m, _ in posts_by_lang[lang]]
    out += ["", f"Last updated: {SITE['launched']}", ""]
    return "\n".join(out)

def main():
    sitemap, og = [], []
    pages_by_lang, posts_by_lang = {}, {}
    slugs = {(lang, "page"): {m["slug"] for m, _ in load_pages(lang)} for lang in LANGS}
    slugs.update({(lang, "post"): {m["slug"] for m, _ in load_posts(lang)} for lang in LANGS})

    def alts_for(lang, kind, meta):
        if "alt" not in meta:
            return None
        other = OTHER[lang]
        if meta["alt"] not in slugs[(other, kind)]:
            raise SystemExit(f"{lang}/{kind}/{meta['slug']}: alt '{meta['alt']}' does not exist in {other}")
        mk = page_url if kind == "page" else post_url
        return {lang: mk(lang, meta["slug"]), other: mk(other, meta["alt"])}

    for lang in LANGS:
        L = LANGS[lang]
        pages_by_lang[lang] = []
        for meta, body in load_pages(lang):
            slug = meta["slug"]
            url = page_url(lang, slug)
            trail = [(meta["crumb"], url)] if slug and slug != "404" else []
            name = f"{lang}-{slug or 'home'}"
            alts = alts_for(lang, "page", meta)
            doc = page(lang, meta, enrich(body, meta, name, lang), url, trail, name, meta.get("schema", []), alts=alts)
            og.append((name, meta.get("og", meta["title"])))
            og += [(im["name"], im["title"]) for im in meta.get("images", [])]
            if slug == "404":
                write(out_dir(lang) + "404.html", doc.replace(f'<link rel="canonical" href="{url}">\n', ""))
                continue
            write(out_dir(lang) + (slug + "/" if slug else "") + "index.html", doc)
            if "noindex" not in meta.get("robots", ""):
                sitemap.append((url, meta.get("updated", SITE["launched"]), alts))
                pages_by_lang[lang].append((meta["title"], url, meta.get("tldr") or meta["desc"]))
        posts = load_posts(lang)
        posts_by_lang[lang] = posts
        for i, (meta, body) in enumerate(posts):
            prev = posts[i - 1][0] if i else None
            nxt = posts[i + 1][0] if i + 1 < len(posts) else None
            trail = [(L["guides"], blog_url(lang)), (meta["crumb"], meta["url"])]
            name = f"{lang}-blog-{meta['slug']}"
            alts = alts_for(lang, "post", meta)
            doc = page(lang, meta, article(lang, meta, enrich(body, meta, name, lang), prev, nxt), meta["url"], trail, name,
                       [article_schema(lang, meta)] + meta.get("schema", []), "article", alts=alts)
            write(f"{out_dir(lang)}{L['blog']}/{meta['slug']}/index.html", doc)
            og.append((name, meta["h1"]))
            sitemap.append((meta["url"], meta.get("updated", meta["date"]), alts))
        write(f"{out_dir(lang)}{L['blog']}/index.html", blog_index(lang, posts))
        og.append((f"{lang}-blog", L["idx_h1"]))
        if posts:
            sitemap.append((blog_url(lang), posts[-1][0]["date"], {"en": blog_url("en"), "fi": blog_url("fi")}))
    with open(os.path.join(ROOT, "sitemap.xml"), "w", encoding="utf-8", newline="\n") as f:
        f.write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml">\n')
        for u, lm, alts in sitemap:
            x = ""
            if alts:
                x = "".join(f'<xhtml:link rel="alternate" hreflang="{LANGS[l]["html"]}" href="{au}"/>' for l, au in alts.items())
                x += f'<xhtml:link rel="alternate" hreflang="x-default" href="{alts["fi"]}"/>'
            f.write(f"  <url><loc>{u}</loc><lastmod>{lm}</lastmod>{x}</url>\n")
        f.write("</urlset>\n")
    write("llms.txt", llms_txt(pages_by_lang, posts_by_lang))
    bots = "".join(f"User-agent: {b}\nAllow: /\n\n" for b in ("GPTBot", "OAI-SearchBot", "ClaudeBot", "PerplexityBot", "Google-Extended"))
    write("robots.txt", f"User-agent: *\nAllow: /\n\n{bots}Sitemap: {BASE}/sitemap.xml\n")
    made = make_og.build(os.path.join(ROOT, "assets", "og"), og)
    print(f"built {len(sitemap)} indexable urls ({sum(len(v) for v in posts_by_lang.values())} articles), 404s, sitemap, {made} new og images")

if __name__ == "__main__":
    main()
