"""tilaa-v2 pages: Finnish (primary, /) - helpers + all Finnish pages."""
import json, os
V = r"C:\Users\DELL\Desktop\tilaa-v2"
SITE = json.load(open(os.path.join(V, "tools", "site.json"), encoding="utf-8"))
BASE = SITE["base"]; EUR = SITE["prices_eur"]

def save(lang, slug, meta, body):
    meta = dict(meta); meta["slug"] = slug
    if "alt" in meta and meta["alt"] is None: meta.pop("alt")
    d = os.path.join(V, "tools", "pages", lang); os.makedirs(d, exist_ok=True)
    head = "<!--" + json.dumps(meta, ensure_ascii=False).replace("\n", " ") + "-->\n"
    open(os.path.join(d, (slug or "index") + ".html"), "w", encoding="utf-8", newline="\n").write(head + body.strip() + "\n")

def faq_schema(items):
    return {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
        {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in items]}

def faq_html(items):
    return '<div class="faq center">' + "".join("<details><summary>%s</summary><p>%s</p></details>" % (q, a) for q, a in items) + "</div>"

def cards(items):
    return "".join('<div class="card c-%s"><div class="ico">{{I:%s}}</div><h3>%s</h3><p>%s</p></div>' % (c, ic, h, p) for c, ic, h, p in items)

def channels_html(items):
    return '<ul class="channels">' + "".join('<li><span class="ch-ico">{{I:%s}}</span><b>%s</b><small>%s</small></li>' % it for it in items) + "</ul>"

POSTERS = ["p-last-kingdom", "p-sonic", "p-black-adam", "p-violent-night", "p-pathaan"]
def poster_slider(eyebrow, h2, p, note):
    def lis(hidden):
        return "".join('<li%s><img src="/assets/posters/%s.webp" width="520" height="293" alt="" loading="lazy" decoding="async"></li>' % (' aria-hidden="true"' if hidden else "", f) for f in POSTERS)
    track = '<div class="marq marq-rev"><ul class="marq-track posters-row">%s%s%s%s</ul></div>' % (lis(False), lis(True), lis(True), lis(True))
    return ('<section class="sec sec-tight sl-sec" aria-labelledby="sl-h"><div class="wrap"><div class="sec-head center"><span class="eyebrow">%s</span><h2 id="sl-h">%s</h2><p>%s</p></div></div>%s'
            '<p class="wrap measure sl-note">%s</p></section>') % (eyebrow, h2, p, track, note)

def pricing_cards(lang, T):
    out = ['<div class="pricing">']
    for m in ("1", "3", "6", "12"):
        e = EUR["1"][m]
        if lang == "fi":
            p = ("%.2f" % e).replace(".", ","); pm = ("%.2f" % (e / int(m))).replace(".", ","); pt = p + " €"
            amt = '<span data-pp="%s">%s</span><small>€</small>' % (m, p); per = '= <span data-pm="%s">%s</span> €/kk' % (m, pm)
        else:
            p = "%.2f" % e; pm = "%.2f" % (e / int(m)); pt = "€" + p
            amt = '<span class="cur">€</span><span data-pp="%s">%s</span>' % (m, p); per = '= €<span data-pm="%s">%s</span>/month' % (m, pm)
        total = T["once"] if m == "1" else per
        best = m == "12"
        badge = '<span class="badge">%s</span>' % T["best"] if best else ""
        feats = "".join("<li>{{I:check}}%s</li>" % x for x in T["incl"])
        msg = T["order_msg"].format(m=T["mon"][m], d="1 " + T["screen"], p=pt)
        out.append('<div class="price%s">%s<h3>%s</h3><p class="sub">%s</p><div class="amount">%s</div><p class="total">%s</p>'
                   '<div class="p-bar" aria-hidden="true"><i style="--m:%s"></i></div><ul>%s</ul>'
                   '<a class="btn%s btn-block" data-track="buy_click" data-pwa="%s" href="{{WA:%s}}" rel="noopener" target="_blank" aria-label="%s">%s</a></div>'
                   % (" best" if best else "", badge, T["mon"][m], T["sub"][m], amt, total, m, feats, "" if best else " btn-line", m, msg,
                      T["pick"].format(m=T["mon"][m]), T["pick"].format(m=T["mon"][m])))
    out.append("</div>")
    return "".join(out)

TF = dict(mon={"1": "1 kuukausi", "3": "3 kuukautta", "6": "6 kuukautta", "12": "12 kuukautta"}, screen="näyttö", once="kertamaksu, ei automaattista uusiutumista", best="Paras hinta",
          sub={"1": "Hyvä kokeiluun", "3": "Yksi kausi", "6": "Puoli vuotta", "12": "Kokonainen vuosi"},
          incl=["Suomalaiset ja pohjoismaiset kanavat", "HD, ja 4K kun kanava lähettää sitä", "TV-opas (EPG)", "Asennusapu WhatsAppissa", "Ei automaattista uusiutumista"],
          order_msg="Hei! Haluan tilata Tilaa IPTV:n: {m}, {d} ({p}).", pick="Valitse {m}")

FAQ = [
 ("Mitä IPTV Suomi tarkoittaa?", "IPTV Suomi tarkoittaa televisiota, joka tulee internetyhteyden kautta antennin, kaapelin tai satelliitin sijaan. Tilaa IPTV:llä katsot suomalaisia ja pohjoismaisia kanavia sovelluksella televisiossa, boksissa, puhelimessa tai tietokoneella."),
 ("Tarvitsenko erillisen boksin?", "Yleensä et. Viime vuosien Samsung- ja LG-televisiot toimivat sovelluksella. Vanhemmassa televisiossa halvin tapa päästä alkuun on Fire TV Stick tai Android TV -boksi."),
 ("Mikä internetnopeus tarvitaan?", "Laske vähintään 10 Mbit/s per näyttö HD-kuvalle ja 25 Mbit/s 4K:lle. Mittaa nopeus televisiolla tai boksilla, ei puhelimella. Verkkokaapeli on lähes aina vakaampi kuin wifi."),
 ("Uusiutuuko tilaus automaattisesti?", "Ei. Emme veloita automaattisesti emmekä tallenna korttitietoja. Kun jakso lähestyy loppuaan, jatkat itse, jos haluat."),
 ("Miten maksan?", "Tilaat WhatsAppissa ja saat maksuohjeet siellä. Otamme vastaan Visan, Mastercardin, Maestron, Apple Payn, Google Payn ja PayPalin, ja muista EU-maista myös SEPA-, iDEAL-, Bancontact- ja giropay-maksut."),
 ("Voinko kokeilla ennen pidempää pakettia?", "Kyllä. Aloita yhdestä kuukaudesta hintaan 15,99 €. Se ei uusiudu itsestään, joten mitään ei tarvitse irtisanoa. Jos kaikki toimii, voit ottaa pidemmän paketin kuukauden jälkeen."),
 ("Onko IPTV laillista Suomessa?", "IPTV on vain tekniikka, ja se on laillista. Ratkaisevaa on, onko katsomillasi kanavilla oikeudet levitykseen. Emme voi antaa lakineuvoja, joten kysy meiltä, mitä paketti sisältää, ennen kuin tilaat. Vastaat itse siitä, miten palvelua käytät."),
]

def pages():
    # ------------------------------------------------------------------ HOME (iptv suomi)
    save("fi", "", {"speakable": True, "keyword": "iptv suomi", "crumb": "Etusivu", "alt": "",
        "title": "IPTV Suomi 2026: suomalaiset kanavat HD-laadulla, alk. 5,83 €",
        "desc": "IPTV Suomi kotitalouksille: suomalaiset ja pohjoismaiset kanavat HD-laadulla, TV-opas ja asennusapu WhatsAppissa. Alk. 5,83 €/kk ilman sitoutumista.",
        "og": "IPTV Suomi 2026: suomalaiset kanavat HD-laadulla alk. 5,83 € kuukaudessa",
        "img_alt": "IPTV Suomi: suomalaiset ja pohjoismaiset kanavat HD-laadulla Smart TV:ssä, boksissa ja puhelimessa",
        "images": [{"name": "fi-home-laitteet", "title": "IPTV Suomi Smart TV:ssä, Fire TV Stickissä, Android TV:ssä ja Apple TV:ssä", "alt": "IPTV Suomi Smart TV:ssä, Fire TV Stickissä, Android TV:ssä, Apple TV:ssä ja MAG-boksissa"},
                   {"name": "fi-home-askeleet", "title": "Aloita IPTV Suomi kolmessa vaiheessa", "alt": "Aloita IPTV Suomi kolmessa vaiheessa WhatsAppin kautta"}],
        "schema": [{"@context": "https://schema.org", "@type": "Product", "name": "Tilaa IPTV -tilaus", "brand": {"@type": "Brand", "name": "Tilaa IPTV"},
                    "description": "IPTV-tilaus suomalaisilla ja pohjoismaisilla kanavilla HD-laadulla Smart TV:lle, Android TV:lle, Apple TV:lle, puhelimelle ja tietokoneelle.",
                    "image": BASE + "/assets/og/fi-home.png",
                    "offers": {"@type": "AggregateOffer", "priceCurrency": "EUR", "lowPrice": "15.99", "highPrice": "169.99", "offerCount": "12", "availability": "https://schema.org/InStock", "url": BASE + "/iptv-hinta/"}},
                   faq_schema(FAQ)]},
"""
<section class="hero">
  <div class="wrap hero-in">
    <div>
      <span class="pill"><span class="dot"></span>Livenä nyt · suomalaiset ja pohjoismaiset kanavat HD-laadulla</span>
      <h1>IPTV Suomi <span class="grad-text">suomalaisille ja pohjoismaisille kanaville</span> HD-laadulla</h1>
      <p class="lead">IPTV Suomi on helppoa: <b>suomalaiset ja pohjoismaiset kanavat HD-laadulla</b> sovelluksella televisiossa, joka sinulla jo on. Tilaa IPTV:llä valitset 1, 3, 6 tai 12 kuukautta, ja autamme asennuksessa WhatsAppissa.</p>
      <div class="hero-cta">
        <a class="btn" data-track="buy_click" href="{{WA:Hei! Haluan tilata Tilaa IPTV:n.}}" rel="noopener" target="_blank">{{I:chat}} Tilaa WhatsAppissa</a>
        <a class="btn btn-ghost" href="#hinnat">Katso hinnat →</a>
      </div>
      <ul class="chips">
        <li>{{I:check}} Ei sitoutumista</li>
        <li>{{I:check}} HD, ja 4K kun saatavilla</li>
        <li>{{I:check}} Smart TV:stä puhelimeen</li>
        <li>{{I:check}} Tuki suomeksi</li>
      </ul>
    </div>
    <div class="screen-wrap" aria-hidden="true">
      <div class="browser">
        <div class="browser-bar"><i></i><i></i><i></i><span>Tilaa IPTV · Elokuvat ja sarjat</span></div>
        <div class="posters">
          <figure><img src="/assets/posters/poster-1.webp" width="1200" height="677" alt="" fetchpriority="high"><figcaption><b class="live">LIVE</b><b>HD</b></figcaption></figure>
          <figure><img src="/assets/posters/poster-2.webp" width="1200" height="677" alt="" loading="lazy"><figcaption><b>4K</b></figcaption></figure>
          <figure><img src="/assets/posters/poster-3.webp" width="900" height="508" alt="" loading="lazy"><figcaption><b>HD</b></figcaption></figure>
        </div>
      </div>
      <div class="f-badge b1"><span class="ic">{{I:shield}}</span><span>Ei sitoutumista<small>mikään ei uusiudu itsestään</small></span></div>
      <div class="f-badge b2"><span class="ic">{{I:zap}}</span><span>5,83 €/kk<small>12 kuukauden paketilla</small></span></div>
      <div class="f-badge b3"><span class="ic">{{I:spark}}</span><span>HD + 4K<small>kun kanava lähettää sitä</small></span></div>
    </div>
  </div>
</section>

<div class="wrap tiles" role="list" aria-label="Tilaa IPTV numeroina">
  <div role="listitem"><b>5,83 €</b><span>kuukaudessa 12 kuukauden paketilla</span></div>
  <div role="listitem"><b>0</b><span>päivää sitoutumista</span></div>
  <div role="listitem"><b>3</b><span>näyttöä yhtä aikaa, jos haluat</span></div>
  <div role="listitem"><b>4</b><span>pakettia, sama sisältö</span></div>
</div>

<section class="strip" aria-label="Toimii laitteilla">
  <div class="wrap">
    <p>Toimii näytöillä, jotka sinulla jo on</p>
    <ul>
      <li>{{I:tv}} Samsung</li><li>{{I:tv}} LG</li><li>{{I:box}} Android TV</li><li>{{I:box}} Fire TV Stick</li>
      <li>{{I:tv}} Apple TV</li><li>{{I:phone}} iPhone ja Android</li><li>{{I:laptop}} Windows ja Mac</li><li>{{I:box}} MAG-boksi</li>
    </ul>
  </div>
</section>

<section class="sec">
  <div class="wrap measure">
    <p>Tämä sivu on kirjoitettu sinulle, joka etsit IPTV Suomi -palvelua ja haluat tietää, mitä oikeasti saat. Käymme läpi kanavat, hinnat, toimivat laitteet ja aloittamisen. Kerromme myös, milloin emme ole oikea valinta. Haluatko lukea englanniksi? Siirry <a href="/en/" hreflang="en" lang="en">englanninkieliselle sivulle</a>.</p>
    <h2 class="center-h">Tilaa IPTV lyhyesti</h2>
    <dl class="facts">
      <div><dt>Hinta</dt><dd>15,99–169,99 €, alk. 5,83 €/kk</dd></div>
      <div><dt>Paketit</dt><dd>1, 3, 6 tai 12 kuukautta, sama sisältö</dd></div>
      <div><dt>Sitoutuminen</dt><dd>Ei, mikään ei uusiudu automaattisesti</dd></div>
      <div><dt>Kanavat</dt><dd>Suomalaiset sekä muut pohjoismaiset kanavat</dd></div>
      <div><dt>Kuva</dt><dd>HD, ja 4K kun kanava lähettää 4K:na</dd></div>
      <div><dt>Nopeus</dt><dd>10 Mbit/s per näyttö HD:lle, 25 4K:lle</dd></div>
      <div><dt>Laitteet</dt><dd>Smart TV, Fire TV, Android TV, Apple TV, puhelin, tietokone, MAG</dd></div>
      <div><dt>Tilaus</dt><dd>WhatsApp, suomeksi tai englanniksi</dd></div>
      <div><dt>Maksutavat</dt><dd>Kortti, Apple Pay, Google Pay, PayPal</dd></div>
    </dl>
    <!--TOC-->
  </div>
</section>

<section class="sec sec-tight">
  <div class="wrap measure">
    <div class="sec-head center">
      <span class="eyebrow">Mitä sisältyy</span>
      <h2>Miksi Tilaa IPTV sopii suomalaiseen kotiin</h2>
      <p>Hyvä IPTV Suomi ei tarkoita pisintä kanavalistaa. Se tarkoittaa, että televisio käynnistyy kaukosäätimen painalluksella, TV-opas näyttää oikean ohjelman ja joku vastaa, kun kysyt. Näin se toimii meillä.</p>
    </div>
  </div>
  <div class="wrap feat">
""" + cards([
 ("cyan", "globe", "Suomalaiset ja pohjoismaiset kanavat", "Uutiset, viihde, lastenkanavat ja urheilu, sekä kanavia muista Pohjoismaista. Kanavatarjonta voi muuttua ajan myötä. Kysy meiltä tietystä kanavasta ennen tilaamista, niin saat suoran vastauksen."),
 ("violet", "spark", "HD vakiona, 4K kun sitä on", "Kanavat toimitetaan HD-laadulla ja 4K:na silloin, kun kanava itse lähettää 4K:na. Kuvan terävyys kotona riippuu myös televisiosta ja yhteydestä. Lue lisää <a href=\"/oppaat/\">IPTV-oppaista</a>."),
 ("pink", "calendar", "TV-opas (EPG) sovelluksessa", "Opas näyttää, mitä kanavilla tulee nyt ja myöhemmin, kuten tavallisessa televisiossa. Juuri se saa IPTV:n tuntumaan televisiolta eikä linkkilistalta."),
 ("green", "wifi", "Vakaa kuva lauantai-iltana", "Kuvan pitää pysyä kasassa myös klo 19–22, kun kaikki käyttävät nettiä yhtä aikaa. Suurin osa pätkimisestä johtuu kotiverkosta, useimmiten wifistä, ja autamme korjaamaan sen."),
 ("blue", "chat", "Kaikki yhdessä chatissa", "Tilaus, maksu ja asennusapu hoituvat samassa WhatsApp-keskustelussa, suomeksi tai englanniksi."),
]) + """
  </div>
</section>

<section class="sec sec-night">
  <div class="wrap">
    <div class="sec-head center">
      <span class="eyebrow">Paketissa</span>
      <h2>Kanavatarjonta koko perheelle</h2>
      <p>Suomalaiset kanavat ensin, sitten muut Pohjoismaat ja kansainväliset kanavat. Kysy meiltä tietystä kanavasta ennen tilaamista.</p>
    </div>
""" + channels_html([("globe", "Suomalaiset kanavat", "Uutiset, viihde ja paikallinen sisältö"), ("tv", "Pohjoismaiset kanavat", "Ruotsi, Norja ja Tanska"), ("zap", "Urheilu", "Jalkapallo, jääkiekko ja muuta suorana"),
   ("film", "Elokuvat ja sarjat", "Elokuvakanavat ja sarjat"), ("spark", "Lapset ja perhe", "Lastenkanavat"), ("calendar", "Dokumentit ja luonto", "Tietoa, luontoa ja historiaa"),
   ("chat", "Uutiset", "Kotimaiset ja kansainväliset"), ("monitor", "Kansainväliset", "Kanavia useammasta maasta")]) + """
    <p class="price-note" style="color:var(--on-night-muted)">Kanavatarjonta voi muuttua ajan myötä.</p>
  </div>
</section>

""" + poster_slider("Näytöllä", "Suomalaisia kanavia ja isoja nimikkeitä", "Pieni maistiainen siitä, mitä suomalaiset katsojat etsivät. Kysy meiltä tietystä kanavasta ennen tilaamista.",
                    "Elokuvajulisteet on esitetty havainnollistamiseksi. Kanavatarjonta voi muuttua ajan myötä.") + """

<section class="sec sec-tight" id="hinnat">
  <div class="wrap">
    <div class="sec-head">
      <span class="eyebrow">Hinnat</span>
      <h2>Mitä IPTV Suomi maksaa: neljä pakettia, sama sisältö</h2>
      <p>Valitse, kuinka monella näytöllä katsotte yhtä aikaa, ja sitten kuinka pitkään. Kanavat ja kuvanlaatu ovat samat kaikissa paketeissa.</p>
    </div>
    <!--DEVICES-->
""" + pricing_cards("fi", TF) + """
    <div class="measure">
      <!--PRICETABLE-->
      <p class="ruler-note">Edullisin kuukausihinta on 12 kuukauden paketilla. 2 tai 3 näytöllä useampi kotitalouden jäsen voi katsoa yhtä aikaa. Maksutavat, lisänäytöt ja ehdot löydät <a href="/iptv-hinta/">IPTV-hinnat-sivulta</a>.</p>
    </div>
  </div>
</section>

<section class="sec sec-alt">
  <div class="wrap measure">
    <div class="sec-head center">
      <span class="eyebrow">Näytöt</span>
      <h2>IPTV Suomi laitteilla, jotka sinulla jo on</h2>
      <p>IPTV:n pitää toimia sillä, mitä kotona jo on. Laitteen oman sovelluskaupan sovellus riittää, ja kerromme, mikä toimii parhaiten juuri sinun mallissasi.</p>
    </div>
    <!--IMG:fi-home-laitteet-->
  </div>
  <div class="wrap devs" style="margin-top:28px">
""" + cards([
 ("cyan", "tv", "Samsung- ja LG-Smart TV", "Useimmat noin vuodesta 2018 alkaen valmistetut mallit toimivat sovelluksella. Saatavilla olevat sovellukset riippuvat mallista ja vuodesta, joten lähetä meille mallinumero."),
 ("green", "box", "Fire TV Stick ja Android TV", "Laajin sovellusvalikoima ja usein vakain kuva. Fire TV Stickillä vanhempikin televisio muuttuu älytelevisioksi kohtuuhintaan."),
 ("pink", "phone", "Apple TV, iPhone ja iPad", "IPTV-soitin App Storesta, sama sovellus kaikilla Apple-laitteillasi. Apple kertoo sovellusten asentamisesta <a href=\"https://support.apple.com/fi-fi/apple-tv\" target=\"_blank\" rel=\"noopener\">Apple TV:n tukisivuilla</a>."),
 ("amber", "laptop", "MAG-boksi ja tietokone", "MAG-boksi liitetään tiliisi boksin MAC-osoitteella, ja teemme sen asetuksen puolestasi. Tietokoneella toimivat sekä VLC että IPTV-sovellukset."),
]) + """
  </div>
</section>

<section class="sec">
  <div class="wrap">
    <div class="sec-head">
      <span class="eyebrow">Näin pääset alkuun</span>
      <h2>Aloita IPTV Suomi kolmessa vaiheessa</h2>
      <p>Useimmat katsovat jo samana iltana. Aikaa vie harvoin sovellus, vaan oikean sovelluksen löytäminen juuri sinun televisiollesi.</p>
    </div>
    <ol class="steps">
      <li><h3>Valitse kesto</h3><p>Kaikissa paketeissa on sama sisältö. Jos olet epävarma, aloita yhdestä kuukaudesta.</p></li>
      <li><h3>Kirjoita meille WhatsAppissa</h3><p>Kerro, minkä paketin haluat ja mikä televisio tai boksi sinulla on. Vastaamme maksuohjeilla ja sopivalla sovelluksella.</p></li>
      <li><h3>Kirjaudu ja katso</h3><p>Saat tunnukset ja lyhyen ohjeen omalle televisiollesi. Jos jäät jumiin, autamme keskustelussa eteenpäin.</p></li>
    </ol>
    <p style="margin-top:28px;text-align:center"><a class="btn" data-track="buy_click" href="{{WA:Hei! Haluan kokeilla Tilaa IPTV:tä yhden kuukauden (15,99 €).}}" rel="noopener" target="_blank">Kokeile yhtä kuukautta hintaan 15,99 €</a></p>
    <div class="measure" style="text-align:center"><!--IMG:fi-home-askeleet--><p>Koko ohjeen laite kerrallaan löydät oppaasta <a href="/iptv-sovellus/">IPTV-sovellus ja asennus</a>.</p></div>
  </div>
</section>

<section class="sec">
  <div class="wrap">
    <div class="sec-head center">
      <span class="eyebrow">Vertailu</span>
      <h2>IPTV verrattuna kaapeli-TV:hen ja suoratoistoon</h2>
      <p>IPTV ei sovi kaikille. Näin IPTV Suomi asettuu kaapeli-TV:n ja suoratoistopalvelujen rinnalle.</p>
    </div>
    <ul class="checks">
      <li>{{I:check}}<span>Ei 12 tai 24 kuukauden sitoumusta</span></li>
      <li>{{I:check}}<span>Ei antennia, kaapelirasiaa eikä asentajaa kotiin</span></li>
      <li>{{I:check}}<span>Sama palvelu mökillä, jos siellä on netti</span></li>
      <li>{{I:check}}<span>TV-opas ja kanavanvaihto kuten tavallisessa televisiossa</span></li>
      <li>{{I:check}}<span>Pohjoismaiset kanavat samassa paketissa</span></li>
      <li>{{I:check}}<span>Toimii televisiossa, puhelimessa ja tietokoneella</span></li>
    </ul>
    <div class="vs-wrap" tabindex="0" role="region" aria-label="Vertailu: Tilaa IPTV, kaapeli-TV ja suoratoisto"><table class="vs"><thead><tr><th scope="col">Ominaisuus</th><th scope="col" class="us"><span class="vs-logo"><img class="mark" src="/assets/icons/mark.svg" width="28" height="28" alt=""><span class="wm"><b>Tilaa</b><i>IPTV</i><sup>FI</sup></span></span></th><th scope="col">Kaapeli-TV</th><th scope="col">Suoratoisto</th></tr></thead><tbody>
      <tr><th scope="row">Suomalaiset kanavat</th><td class="us"><span class="yes">{{I:check}}<span class="sr">Kyllä</span></span></td><td><span class="yes">{{I:check}}<span class="sr">Kyllä</span></span></td><td>Osittain</td></tr>
      <tr><th scope="row">Pohjoismaiset kanavat</th><td class="us"><span class="yes">{{I:check}}<span class="sr">Kyllä</span></span></td><td>Osittain</td><td>Harvoin</td></tr>
      <tr><th scope="row">Suora TV ja TV-opas</th><td class="us"><span class="yes">{{I:check}}<span class="sr">Kyllä</span></span></td><td><span class="yes">{{I:check}}<span class="sr">Kyllä</span></span></td><td>Harvoin</td></tr>
      <tr><th scope="row">HD ja 4K</th><td class="us">HD, 4K kun lähetetään</td><td>Riippuu paketista</td><td>Riippuu palvelusta</td></tr>
      <tr><th scope="row">Hinta kuukaudessa</th><td class="us">Alk. 5,83 €</td><td>Usein useita kymmeniä euroja</td><td>Palvelukohtainen</td></tr>
      <tr><th scope="row">Sitoutuminen</th><td class="us">Ei</td><td>Usein 12–24 kuukautta</td><td>Ei</td></tr>
      <tr><th scope="row">Asennus</th><td class="us">Yksi sovellus</td><td>Rasia ja boksi</td><td>Yksi sovellus</td></tr>
      <tr><th scope="row">Toimii mökillä</th><td class="us">Jos netti on</td><td><span class="no">{{I:x}}<span class="sr">Ei</span></span></td><td>Jos netti on</td></tr>
      <tr><th scope="row">Tuki</th><td class="us">WhatsApp, suomeksi tai englanniksi</td><td>Asiakaspalvelu</td><td>Sähköposti tai chat</td></tr>
    </tbody></table></div>
    <p>Jos yhteytesi on hidas tai epätasainen, kaapeli-TV tai antenni on turvallisempi valinta. Alle 10 Mbit/s televisiolle mikään palvelu ei ole oikea IPTV Suomi -ratkaisu sinulle, olipa se kuinka hyvä tahansa.</p>
  </div>
</section>

<section class="sec sec-alt">
  <div class="wrap measure why">
    <div class="sec-head center">
      <span class="eyebrow">Miksi me</span>
      <h2>Miksi ihmiset valitsevat Tilaa IPTV:n</h2>
    </div>
    <h3>Tuki WhatsAppissa</h3>
    <p>Kirjoitat ihmiselle, et lomakkeelle. Lähetä kuva näytöstä, niin näemme heti, mistä on kyse.</p>
    <h3>Selkeät ehdot</h3>
    <p>Ei sitoutumista, ei automaattista uusiutumista ja hinnat euroina. IPTV:n pitää olla yhtä helppo lopettaa kuin aloittaa. Kaikki on <a href="/ehdot/">ehdoissamme</a>.</p>
    <h3>Jos jokin ei toimi</h3>
    <p>Kirjoita meille WhatsAppissa kuva näytöstä, niin käymme yhdessä läpi yhteyden, sovelluksen ja asetukset. Mitä ostoon sovelletaan, kerrotaan <a href="/ehdot/">ehdoissamme</a>.</p>
    <h3>Kun emme ole oikea valinta</h3>
    <p>Jos yhteytesi on alle 10 Mbit/s per näyttö tai haluat boksin, jonka asentaja asentaa kotiisi, perinteinen operaattori sopii sinulle paremmin. Silloin emme ole oikea IPTV Suomi -valinta, ja on rehellisempää sanoa se nyt kuin maksun jälkeen.</p>
  </div>
</section>

<section class="sec sec-alt">
  <div class="wrap">
    <div class="sec-head">
      <span class="eyebrow">Oppaat</span>
      <h2>Oppaita tukitiimiltämme</h2>
      <p>Asennus, sovellukset ja vianetsintä, kirjoitettu saamiemme kysymysten pohjalta.</p>
    </div>
    <ul class="checks">
      <li>{{I:check}}<span><a href="/paras-iptv-palvelu/">Paras IPTV-palvelu: 7 tarkistuskohtaa ennen valintaa</a></span></li>
      <li>{{I:check}}<span><a href="/iptv-kanavat/">IPTV-kanavat: mitä paketissa on ja mitä kannattaa kysyä</a></span></li>
      <li>{{I:check}}<span><a href="/iptv-sovellus/">IPTV-sovellus ja asennus Smart TV:hen, Fire TV:hen ja puhelimeen</a></span></li>
    </ul>
    <p><a href="/oppaat/">Kaikki IPTV-oppaat Suomeen</a></p>
  </div>
</section>

<section class="sec">
  <div class="wrap">
    <div class="sec-head">
      <span class="eyebrow">Kysymyksiä ja vastauksia</span>
      <h2>Usein kysyttyä IPTV Suomi -palvelusta</h2>
    </div>
""" + faq_html(FAQ) + """
    <p style="margin-top:24px">Lisää vastauksia löydät <a href="/ukk/">usein kysytyt kysymykset -sivulta</a>.</p>
  </div>
</section>

<section class="band">
  <div class="wrap band-in">
    <div><h2>Kokeile IPTV Suomi -palvelua omalla televisiollasi jo tänä iltana.</h2><p>Kerro, mikä televisio sinulla on, niin kerromme, mikä paketti ja sovellus sopivat.</p></div>
    <a class="btn" data-track="buy_click" href="{{WA:Hei! Minulla on kysymys ennen Tilaa IPTV:n tilaamista.}}" rel="noopener" target="_blank">{{I:chat}} Kirjoita meille WhatsAppissa</a>
  </div>
</section>
""")
    return FAQ


if __name__ == "__main__":
    pages(); print("FI home written")
