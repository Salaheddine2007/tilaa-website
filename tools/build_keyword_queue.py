"""Build tools/keywords.json (the posting queue) for iptvnorwayone.com from a Semrush export.

Usage: python tools/build_keyword_queue.py <export.xlsx>

Rules (the user's standing keyword policy, see tools/keyword_policy.json):
  - commercial / support intent only: NO free, m3u, playlist, reddit, apk, kodi, reviews, "iptv box", codes, forums, DIY tech
  - allowlist: every word of a kept keyword must be a generic Norwegian/English word or a device/app category,
    so other sellers' and apps' brand names are dropped even when we have never seen them
  - skip keywords already owned by a page and near-duplicates (same word set after folding synonyms/years)
  - language per keyword: Norwegian words -> "no", otherwise "en"
  - order: low difficulty first (KD <= 40), then volume
"""
import json, os, re, sys, unicodedata
import openpyxl

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
POLICY = json.load(open(os.path.join(ROOT, "tools", "keyword_policy.json"), encoding="utf-8"))
DENY = re.compile(POLICY["deny_regex"], re.I)
DENY_EXTRA = re.compile(r"crack|keygen|hack|warez|cccam|oscam|xtream|codes?|login|activation|upload|editor|github|torrent|vpn|"
                        r"\b(download|url|urls|link|links|list|lists|source|server|client|software|plugin|protocol|web|vlan|"
                        r"player|players|pro|simple|lifetime|instant|unlimited|trial|premier|league|legal|lovlig|lovlige|lovligt|ulovlig|"
                        r"lagligt|adult|adults|porn|porno|xxx|sex)\b|smart iptv|net iptv|set iptv", re.I)

NO_WORDS = set("""norge norsk norske norsken kjøp kjøpe billig billige billigste beste bra hvordan hva hvilken på i og er
abonnement kanaler kanal fotball nordisk norden pris priser tv-guide installere installer oppsett hjelp problem fungerer fungerer ikke""".split())
ALLOW = set("""
iptv tv best beste bra top cheap billig billige cheapest buy kjøp kjøpe price prices pris priser cost abonnement subscription subscriptions
provider providers service services supplier suppliers channel channels kanal kanaler sport sports fotball football live stream streaming
online watch norway norge norsk norske norwegian nordic nordisk norden scandinavia scandinavian europe
how to on for in with and of the is does work works working not hvordan hva hvilken på i og er
setup install installer installere guide test epg hd 4k uhd app apps application smart internet router wifi buffering
android windows mac macbook pc chromecast apple iphone ipad ios samsung lg sony philips xiaomi tcl hisense nvidia shield
firestick fire stick mag vlc chrome chromebook linux google digital home
""".split())

SAME = {"beste": "best", "bra": "best", "top": "best", "billig": "cheap", "billige": "cheap", "cheapest": "cheap",
        "kjop": "buy", "kjope": "buy", "prices": "price", "pris": "price", "priser": "price", "cost": "price",
        "providers": "provider", "service": "provider", "services": "provider", "supplier": "provider", "suppliers": "provider",
        "channels": "channel", "kanaler": "channel", "kanal": "channel", "subscriptions": "subscription", "abonnement": "subscription",
        "norge": "norway", "norsk": "norway", "norske": "norway", "norwegian": "norway", "apps": "app", "application": "app",
        "working": "work", "works": "work", "does": "work", "install": "setup", "installer": "setup", "installere": "setup", "football": "fotball"}
FILLER = {"i", "pa", "for", "on", "in", "with", "and", "of", "the", "is", "to", "how", "hvordan", "hva", "er", "og", "not"}

def slugify(s):
    s = unicodedata.normalize("NFKD", s).encode("ascii", "ignore").decode().lower()
    return re.sub(r"[^a-z0-9]+", "-", s).strip("-")

def core(kw):
    words = slugify(kw).replace("ip-tv", "iptv").split("-")
    return frozenset(SAME.get(w, w) for w in words if w and w not in FILLER and not re.fullmatch(r"\d{1,2}|20\d\d", w))

def owned():
    """keywords already owned by a page (focus keyword in tools/pages/*) plus the main keyword and the policy's secondaries"""
    out = {POLICY["main"], *POLICY["secondary"]}
    for lang in ("en", "no"):
        d = os.path.join(ROOT, "tools", "pages", lang)
        for fn in os.listdir(d):
            raw = open(os.path.join(d, fn), encoding="utf-8").read()
            m = re.match(r"\s*<!--(\{.*?\})-->", raw, re.S)
            if m and json.loads(m.group(1)).get("keyword"):
                out.add(json.loads(m.group(1))["keyword"])
    for lang in ("en", "no"):
        d = os.path.join(ROOT, "tools", "posts", lang)
        if os.path.isdir(d):
            for fn in os.listdir(d):
                raw = open(os.path.join(d, fn), encoding="utf-8").read()
                m = re.match(r"\s*<!--(\{.*?\})-->", raw, re.S)
                if m and json.loads(m.group(1)).get("keyword"):
                    out.add(json.loads(m.group(1))["keyword"])
    return out

def main(export):
    rows = list(openpyxl.load_workbook(export, read_only=True).active.iter_rows(values_only=True))[1:]
    seen_core = {core(k) for k in owned()}
    kept, dropped = [], {"deny": 0, "allowlist": 0, "owned/dup": 0, "volume": 0}
    for kw, intent, vol, kd, *_ in rows:
        if not kw:
            continue
        kw = str(kw).strip().lower()
        vol, kd = int(vol or 0), int(kd or 0)
        if vol < 20:
            dropped["volume"] += 1; continue
        if DENY.search(kw) or DENY_EXTRA.search(kw):
            dropped["deny"] += 1; continue
        words = re.split(r"\s+", kw)
        if any(w not in ALLOW for w in words) or "smart" in words and "tv" not in words or "iptv" not in words and "tv" not in words:
            dropped["allowlist"] += 1; continue
        c = core(kw)
        if c in seen_core or len(c) < 2:
            dropped["owned/dup"] += 1; continue
        seen_core.add(c)
        lang = "no" if any(w in NO_WORDS for w in words if w not in ("i", "og", "er", "tv", "iptv")) else "en"
        kept.append({"keyword": kw, "slug": slugify(kw), "volume": vol, "kd": kd, "intent": intent, "lang": lang})
    kept.sort(key=lambda r: (r["kd"] > 40, -r["volume"], r["kd"]))
    json.dump(kept, open(os.path.join(ROOT, "tools", "keywords.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print(f"{len(rows)} rows -> {len(kept)} queued ({sum(r['lang'] == 'no' for r in kept)} no, {sum(r['lang'] == 'en' for r in kept)} en); dropped {dropped}")
    for r in kept[:45]:
        print(f"  {r['lang']} {r['keyword']:<42} vol {r['volume']:>5} kd {r['kd']:>2}")

if __name__ == "__main__":
    main(sys.argv[1])
