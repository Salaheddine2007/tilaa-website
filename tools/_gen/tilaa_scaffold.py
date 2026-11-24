"""Turn the Norway reference into the tilaa-v2 base: Finnish primary at /, English at /en/, single currency (EUR)."""
import re, json, os
V = r"C:\Users\DELL\Desktop\tilaa-v2"
def rd(p): return open(p, encoding="utf-8").read()
def wr(p, s): open(p, "w", encoding="utf-8", newline="\n").write(s)

FI = '''    "fi": dict(prefix="", html="fi", blog="oppaat",
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
               idx_p="Asennus, sovellukset, kuvanlaatu ja vianetsintä. Kirjoitamme asioista, joita asiakkaat oikeasti kysyvät. Hinnat löytyvät <a href=\\"/iptv-hinta/\\">hintasivulta</a>.",
               blogname="Oppaat - Tilaa IPTV",
               org_desc="Tilaa IPTV myy IPTV-tilauksia suomalaisilla ja pohjoismaisilla kanavilla HD-laadulla suomalaisille kotitalouksille. Tilaus ja tuki WhatsAppissa.",
               wa_default="Hei! Haluan tilata Tilaa IPTV:n.", about_slug="tietoa-meista", contact_slug="yhteystiedot"),
'''
s = rd(f"{V}\\tools\\build_site.py")
a = s.index('    "no": dict(prefix=""'); b = s.index("\n}\nOTHER", a)
s = s[:a] + FI.rstrip("\n").rstrip(",") + "," + s[b:] if False else s[:a] + FI.rstrip("\n") + s[b:]
s = s.replace('OTHER = {"en": "no", "no": "en"}', 'OTHER = {"en": "fi", "fi": "en"}')
s = s.replace('"inLanguage": ["nb", "en"]', '"inLanguage": ["fi", "en"]').replace('"availableLanguage": ["en", "nb"]', '"availableLanguage": ["fi", "en"]')
s = s.replace('"areaServed": "NO"', '"areaServed": "FI"').replace('"IPTV", "IPTV Norway", "IPTV Norge", "IPTV Nordic"', '"IPTV", "IPTV Suomi", "IPTV Finland"')
s = s.replace('for lang in ("no", "en"):\n        out += ["", f"## Pages', 'for lang in ("fi", "en"):\n        out += ["", f"## Pages')
s = s.replace("Norwegian and Nordic channels in HD to households in Norway", "Finnish and Nordic channels in HD to households in Finland")
s = s.replace("The site is available in Norwegian (/) and English (/en/).", "The site is available in Finnish (/) and English (/en/).")
s = s.replace('alts["no"]', 'alts["fi"]').replace('"no": blog_url("no")', '"fi": blog_url("fi")').replace('{"en": blog_url("en"), "no": blog_url("no")}', '{"en": blog_url("en"), "fi": blog_url("fi")}')
s = s.replace("for lang in ('en', 'no')", "for lang in ('en', 'fi')").replace('("en", "no")', '("en", "fi")')
s = s.replace("IPTV Norway One", "Tilaa IPTV")
# single currency: no secondary amount when site.json has no prices_local
s = s.replace('''    eur, nok = SITE["prices_eur"], SITE["prices_nok"]''', '''    eur = SITE["prices_eur"]; nok = SITE.get("prices_local")''')
s = s.replace('''            e, n = eur[d][m], nok[d][m]
            if lang == "en":
                p, pm, s = f"{e:.2f}", f"{e / int(m):.2f}", f"≈ {n} kr"
            else:
                p, pm, s = str(n), str(round(n / int(m))), f"≈ €{e:.2f}"
            out[d][m] = {"p": p, "pm": pm, "s": s, "pt": (f"€{p}" if lang == "en" else f"{p} kr")}''', '''            e = eur[d][m]
            out[d][m] = {"p": f"{e:.2f}", "pm": f"{e / int(m):.2f}", "s": "", "pt": f"{e:.2f} €"}''')
s = s.replace('''f'<td>{pd[d][m]["pt"]}<small>{pd[d][m]["s"]}' + (f' · {pd[d][m]["pm"]}{L["permonth"]}' if m != "1" else "") + '</small></td>\'''', '''f'<td>{pd[d][m]["pt"]}' + (f'<small>{pd[d][m]["pm"]} €{L["permonth"]}</small>' if m != "1" else "") + '</td>\'''')
wr(f"{V}\\tools\\build_site.py", s)

q = rd(f"{V}\\tools\\qa.py")
q = q.replace('(("en", "/en/", "/en/guides/"), ("no", "/", "/guider/"))', '(("en", "/en/", "/en/guides/"), ("fi", "/", "/oppaat/"))').replace('url not in ("/", "/en/")', 'url not in ("/", "/en/")')
q = q.replace('url not in ("/guider/", "/en/guides/")', 'url not in ("/oppaat/", "/en/guides/")').replace('("/guider/", "/en/guides/")', '("/oppaat/", "/en/guides/")')
q = q.replace("iptvnorwayone\\.com", "tilaaiptv\\.com")
q = q.replace('sømløs\\w*|banebrytende|revolusjonerende|lås opp|i dagens raske|uansett om du er|', 'saumaton|mullistava|avaa|nykypäivän kiireisessä|riippumatta siitä oletko|')
wr(f"{V}\\tools\\qa.py", q)

p = rd(f"{V}\\tools\\publish_post.py")
p = p.replace('TRUNK = {"en": \'/en/\', "no": \'/\'}', 'TRUNK = {"en": \'/en/\', "fi": \'/\'}').replace('PLANS = {"en": "/en/iptv-subscription-norway/", "no": "/iptv-norway-abonnement/"}', 'PLANS = {"en": "/en/iptv-subscription-finland/", "fi": "/iptv-hinta/"}')
p = p.replace('BLOG = {"en": "/en/guides/", "no": "/guider/"}', 'BLOG = {"en": "/en/guides/", "fi": "/oppaat/"}').replace('if a.lang not in ("en", "no")', 'if a.lang not in ("en", "fi")').replace("--lang must be en or no", "--lang must be en or fi").replace("iptvnorwayone\\.com", "tilaaiptv\\.com")
p = p.replace("(en: href=\"/en/\", no: href=\"/\")", "(en: href=\"/en/\", fi: href=\"/\")")
wr(f"{V}\\tools\\publish_post.py", p)

site = json.load(open(f"{V}\\tools\\site.json", encoding="utf-8"))
eur = {"1": {"1": 15.99, "3": 30.99, "6": 45.99, "12": 69.99}, "2": {"1": 23.99, "3": 49.99, "6": 69.99, "12": 119.99}, "3": {"1": 32.99, "3": 69.99, "6": 94.99, "12": 169.99}}
import secrets
site.update({"base": "https://tilaaiptv.com", "name": "Tilaa IPTV", "site_id": "tilaaiptv", "launched": "2026-11-25", "indexnow_key": secrets.token_hex(16),
             "prices_eur": eur, "author": {"type": "Organization", "name": "Tilaa IPTV:n tukitiimi",
             "bio_fi": "Oppaat kirjoittaa Tilaa IPTV:n tukitiimi, samat ihmiset jotka vastaavat WhatsAppissa. Asetukset ja sovellusten toiminnot tarkistetaan valmistajien omilta ohjesivuilta, ja korjaamme tekstin, kun jokin muuttuu.",
             "bio_en": "The guides are written by the Tilaa IPTV support team, the same people who answer on WhatsApp. Settings and app features are checked against the manufacturers' own help pages, and we correct the text when something changes."}})
site.pop("prices_nok", None); site.pop("nok_rate", None)
site["facts"] = [["Price (1 screen)", "EUR 15.99 for 1 month, 30.99 for 3 months, 45.99 for 6 months, 69.99 for 12 months (5.83/month)"],
                 ["Screens", "1, 2 or 3 screens at the same time. 2 screens: 23.99, 49.99, 69.99 or 119.99. 3 screens: 32.99, 69.99, 94.99 or 169.99 (1, 3, 6 or 12 months)"],
                 ["Contract", "None. The subscription does not renew automatically"],
                 ["Channels", "Finnish channels plus other Nordic channels. The line-up can change over time"],
                 ["Picture", "HD, and 4K where the channel broadcasts in 4K"],
                 ["Devices", "Samsung and LG Smart TV, Android TV, Google TV, Fire TV Stick, Apple TV, iPhone, iPad, Android, Windows, Mac and MAG box"],
                 ["Internet speed", "At least 10 Mbit/s per screen for HD, 25 Mbit/s for 4K"],
                 ["Ordering and support", "Via WhatsApp, in Finnish and English"],
                 ["Payment", "Visa, Mastercard, Maestro, Apple Pay, Google Pay, PayPal; from other EU countries also SEPA, iDEAL, Bancontact, giropay"]]
json.dump(site, open(f"{V}\\tools\\site.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
wr(f"{V}\\{site['indexnow_key']}.txt", site["indexnow_key"])
print("scaffold ok; key", site["indexnow_key"])
