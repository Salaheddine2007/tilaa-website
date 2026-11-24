import re, os
ROOT = r"C:\Users\DELL\Desktop\tilaa-v2\tools"
src = open(r"C:\Users\DELL\Desktop\basta-website\tools\layout.html", encoding="utf-8").read()

LANGS = {
 "en": dict(html="en", skip="Skip to content",
   ticker=["Finnish and Nordic TV in HD", "From €5.83/month", "No contract", "Install help on WhatsApp", "Smart TV, Fire TV, Apple TV and mobile"],
   brandlabel="Tilaa IPTV, home",
   nav=[("/en/iptv-subscription-finland/", "Plans"), ("/en/best-iptv-finland/", "Best IPTV"), ("/en/install-iptv/", "Install"), ("/en/guides/", "Guides"), ("/en/contact/", "Contact")],
   navlabel="Main menu", theme="Switch between light and dark mode", order="Order",
   foot="IPTV subscriptions with Finnish and Nordic channels in HD. Order and support on WhatsApp.",
   fnav=[("/en/iptv-subscription-finland/", "IPTV plans and prices"), ("/en/best-iptv-finland/", "Best IPTV in Finland"), ("/en/install-iptv/", "Install IPTV"), ("/en/faq/", "FAQ"),
         ("/en/guides/", "Guides"), ("/en/about/", "About us"), ("/en/contact/", "Contact"), ("/en/terms/", "Terms"), ("/en/privacy/", "Privacy policy"), ("/en/cookies/", "Cookies and statistics")],
   footnav="Footer",
   legal="Tilaa IPTV is an independent service with no affiliation to the TV companies, apps or manufacturers mentioned on this site. The channel line-up can change over time. © 2026 Tilaa IPTV",
   wa_float="Order on WhatsApp", form="Write to us", formlabel="Write to us in the contact form", stick="Order via WhatsApp", stick_s="from €5.83/month",
   consent="We would like to count visits and clicks to improve the site. No cookies, no ad trackers.", more="Read more", no="No thanks", yes="Accept", consentlabel="Statistics",
   sw_text="Suomi", sw_label="Suomeksi", sw_lang="fi", home="/en/", contact="/en/contact/", cookies="/en/cookies/", loc="en_US"),
 "fi": dict(html="fi", skip="Siirry sisältöön",
   ticker=["Suomalaiset ja pohjoismaiset kanavat HD-laadulla", "Alk. 5,83 €/kk", "Ei sitoutumista", "Asennusapu WhatsAppissa", "Smart TV, Fire TV, Apple TV ja mobiili"],
   brandlabel="Tilaa IPTV, etusivu",
   nav=[("/iptv-hinta/", "Hinnat"), ("/paras-iptv-palvelu/", "Paras IPTV"), ("/iptv-sovellus/", "Asennus"), ("/oppaat/", "Oppaat"), ("/yhteystiedot/", "Yhteys")],
   navlabel="Päävalikko", theme="Vaihda vaalean ja tumman tilan välillä", order="Tilaa",
   foot="IPTV-tilaukset suomalaisilla ja pohjoismaisilla kanavilla HD-laadulla. Tilaus ja tuki WhatsAppissa.",
   fnav=[("/iptv-hinta/", "IPTV-hinnat ja paketit"), ("/paras-iptv-palvelu/", "Paras IPTV-palvelu"), ("/iptv-kanavat/", "IPTV-kanavat"), ("/iptv-sovellus/", "IPTV-sovellus ja asennus"),
         ("/ukk/", "Usein kysytyt kysymykset"), ("/oppaat/", "Oppaat"), ("/tietoa-meista/", "Tietoa meistä"), ("/yhteystiedot/", "Yhteystiedot"),
         ("/ehdot/", "Ehdot"), ("/tietosuoja/", "Tietosuoja"), ("/evasteet/", "Evästeet ja tilastot")],
   footnav="Alatunniste",
   legal="Tilaa IPTV on riippumaton palvelu, eikä sillä ole yhteyttä sivulla mainittuihin TV-yhtiöihin, sovelluksiin tai valmistajiin. Kanavatarjonta voi muuttua ajan myötä. © 2026 Tilaa IPTV",
   wa_float="Tilaa WhatsAppissa", form="Kirjoita meille", formlabel="Kirjoita meille yhteydenottolomakkeella", stick="Tilaa WhatsAppissa", stick_s="alk. 5,83 €/kk",
   consent="Haluamme laskea käynnit ja klikkaukset sivun parantamiseksi. Ei evästeitä, ei mainosseurantaa.", more="Lue lisää", no="Ei kiitos", yes="Hyväksy", consentlabel="Tilastot",
   sw_text="English", sw_label="English version", sw_lang="en", home="/", contact="/yhteystiedot/", cookies="/evasteet/", loc="fi_FI"),
}

def mk(lang):
    L = LANGS[lang]
    s = src
    s = s.replace('<html lang="sv">', f'<html lang="{L["html"]}" data-site="tilaaiptv">')
    s = s.replace('<meta property="og:locale" content="sv_SE">', f'<meta property="og:locale" content="{L["loc"]}">')
    s = s.replace('content="BästaIPTVHD"', 'content="Tilaa IPTV"').replace("#08001A", "#050E24")
    s = s.replace("Hoppa till innehållet", L["skip"])
    t = "".join(f"<span>{x}</span>" for x in L["ticker"] * 2)
    s = re.sub(r'<div class="ticker" aria-hidden="true"><div class="ticker-in">.*?</div></div>',
               lambda m: f'<div class="ticker" aria-hidden="true"><div class="ticker-in">{t}</div></div>', s, flags=re.S)
    s = s.replace('<span class="wm"><b>Bästa</b><i>IPTV</i><sup>HD</sup></span>', '<span class="wm"><b>Tilaa</b><i>IPTV</i><sup>FI</sup></span>')
    s = s.replace('href="/" aria-label="BästaIPTVHD, startsida"', f'href="{L["home"]}" aria-label="{L["brandlabel"]}"')
    nav = "".join(f'<a href="{h}">{n}</a>' for h, n in L["nav"])
    s = re.sub(r'(<nav class="nav" aria-label=")Huvudmeny(">\s*).*?(\s*<button class="theme")',
               lambda m: m.group(1) + L["navlabel"] + m.group(2) + nav + m.group(3), s, flags=re.S)
    s = s.replace('aria-label="Byt mellan ljust och mörkt läge"', f'aria-label="{L["theme"]}"')
    sw = f'<a class="lang-sw" hreflang="{L["sw_lang"]}" lang="{L["sw_lang"]}" href="{{{{ALT}}}}" aria-label="{L["sw_label"]}">{L["sw_text"]}</a>'
    s = s.replace('</button>\n      <a class="btn btn-sm nav-cta"', '</button>\n      ' + sw + '\n      <a class="btn btn-sm nav-cta"')
    s = s.replace('rel="noopener" target="_blank">Beställ</a>', f'rel="noopener" target="_blank">{L["order"]}</a>')
    s = s.replace("Abonnemang för svensk och nordisk tv i HD. Beställning och support via WhatsApp.", L["foot"])
    fn = "".join(f'<a href="{h}">{n}</a>' for h, n in L["fnav"])
    s = re.sub(r'(<nav class="foot-nav" aria-label=")Sidfot(">\s*).*?(\s*</nav>)',
               lambda m: m.group(1) + L["footnav"] + m.group(2) + fn + m.group(3), s, flags=re.S)
    s = re.sub(r'<p class="wrap foot-legal">.*?</p>', lambda m: f'<p class="wrap foot-legal">{L["legal"]}</p>', s, flags=re.S)
    s = s.replace('aria-label="Beställ på WhatsApp"', f'aria-label="{L["wa_float"]}"').replace("</svg>Beställ på WhatsApp</a>", f'</svg>{L["wa_float"]}</a>')
    s = s.replace('href="/kontakt/" aria-label="Skriv till oss i kontaktformuläret"', f'href="{L["contact"]}" aria-label="{L["formlabel"]}"')
    s = s.replace("<span>Skriv till oss</span>", f'<span>{L["form"]}</span>')
    s = s.replace("Beställ via WhatsApp <span>från 64 kr/mån</span>", f'{L["stick"]} <span>{L["stick_s"]}</span>')
    s = s.replace('<aside aria-label="Beställ">', f'<aside aria-label="{L["order"]}">')
    s = s.replace('aria-label="Statistik"', f'aria-label="{L["consentlabel"]}"')
    s = re.sub(r"<p>Vi vill räkna.*?</p>", lambda m: f'<p>{L["consent"]} <a href="{L["cookies"]}">{L["more"]}</a></p>', s, flags=re.S)
    s = s.replace(">Nej tack<", f'>{L["no"]}<').replace(">Godkänn<", f'>{L["yes"]}<')
    return s

for l in ("en", "fi"):
    out = mk(l)
    open(os.path.join(ROOT, f"layout.{l}.html"), "w", encoding="utf-8").write(out)
    print(l, "leftover:", re.findall(r"Bästa|svensk|Beställ|Sidfot|Hoppa|Huvudmeny|Godkänn|Norway", out))
