import sys
sys.path.insert(0, r"C:\Users\DELL\AppData\Local\Temp\claude\ac5e4f4ff9d25599\1da4b7fd-101c-468b-9d88-b4a6ba448f91\scratchpad")
from gen_tilaa_fi import *

def pages2():
    # ------------------------------------------------------------------ HINTA
    pf = [("Voinko vaihtaa näyttöjen määrää myöhemmin?", "Kyllä. Kirjoita meille WhatsAppissa ennen jakson päättymistä ja kerro, montako näyttöä haluat seuraavalla kerralla. Hinta noudattaa valitsemaasi näyttötasoa."),
          ("Mitä tapahtuu, kun jakso päättyy?", "Palvelu päättyy. Mikään ei uusiudu automaattisesti, emmekä tallenna korttitietojasi. Jos haluat jatkaa, tilaat uudelleen."),
          ("Sisältävätkö hinnat arvonlisäveron?", "Tällä sivulla näkyvät hinnat ovat hintoja, jotka maksat. Hinnat on ilmoitettu euroina.")]
    save("fi", "iptv-hinta", {"keyword": "iptv hinta", "crumb": "IPTV hinta", "alt": "iptv-subscription-finland",
        "title": "IPTV hinta: 12 pakettia alkaen 15,99 € | Tilaa IPTV",
        "desc": "IPTV hinta selkeästi: 1, 3, 6 tai 12 kuukautta 1, 2 tai 3 näytölle, alk. 5,83 €/kk ilman sitoutumista. Kaikki hinnat yhdellä sivulla.",
        "og": "IPTV hinta: 12 pakettia alkaen 15,99 €",
        "tldr": "IPTV hinta Tilaa IPTV:llä on 15,99 € yhdeltä kuukaudelta ja 69,99 € kahdeltatoista kuukaudelta yhdellä näytöllä, eli 5,83 € kuukaudessa. Kahden ja kolmen näytön paketit maksavat enemmän. Mikään ei uusiudu automaattisesti.",
        "schema": [{"@context": "https://schema.org", "@type": "Product", "name": "Tilaa IPTV -tilaus", "brand": {"@type": "Brand", "name": "Tilaa IPTV"}, "image": BASE + "/assets/og/fi-iptv-hinta.png",
                    "offers": {"@type": "AggregateOffer", "priceCurrency": "EUR", "lowPrice": "15.99", "highPrice": "169.99", "offerCount": "12", "availability": "https://schema.org/InStock", "url": BASE + "/iptv-hinta/"}},
                   faq_schema(pf)]},
"""
<section class="page-head"><div class="wrap"><span class="eyebrow">Hinnat</span><h1>IPTV hinta: paketit ja hinnat</h1>
<p>Yksi palvelu, neljä kestoa ja kolme näyttötasoa. Valitse, kuinka monella näytöllä katsotte yhtä aikaa, ja sitten kuinka pitkään haluat tilata.</p></div></section>
<section class="sec sec-tight"><div class="wrap">
<!--TOC-->
<!--DEVICES-->
""" + pricing_cards("fi", TF) + """
<div class="measure">
<h2>Mitä IPTV hinta sisältää</h2>
<p>Jokaisessa paketissa IPTV hinta kattaa saman sisällön: suomalaiset ja pohjoismaiset kanavat HD-laadulla, 4K:n silloin kun kanava lähettää sitä, TV-oppaan ja asennusavun WhatsAppissa. Pakettien välillä muuttuu vain kesto ja näyttöjen määrä.</p>
<h2>Kaikki hinnat 1, 2 ja 3 näytölle</h2>
<!--PRICETABLE-->
<p>Hinta on se, jonka maksat. Pidempi paketti on aina edullisempi kuukautta kohti.</p>
<h2>Näin maksat</h2>
<p>Tilaat WhatsAppissa ja saat maksuohjeet siellä. Otamme vastaan Visan, Mastercardin, Maestron, Apple Payn, Google Payn ja PayPalin, ja muista EU-maista myös SEPA-, iDEAL-, Bancontact- ja giropay-maksut. Emme tallenna korttitietoja, eikä mikään uusiudu itsestään.</p>
<h2>Kuinka valita IPTV hinta, johon voi luottaa</h2>
<p>Kun vertailet, mitä IPTV hinta kattaa eri myyjillä, katso sitoutumista, uusiutumista ja tukea, älä vain kanavien määrää. Meillä ei ole sitoutumista eikä automaattista uusiutumista. Jos haluat tuntea kuluttajan oikeutesi ennen minkä tahansa digitaalisen palvelun ostamista, <a href="https://www.kkv.fi/" target="_blank" rel="noopener">Kilpailu- ja kuluttajavirasto</a> tarjoaa selkeitä ohjeita.</p>
<h2>Näin IPTV hinta muuttuu näyttöjen mukaan</h2>
<p>Yhdellä näytöllä kahdentoista kuukauden IPTV hinta on 69,99 euroa, eli 5,83 euroa kuukaudessa. Kahdella näytöllä sama jakso maksaa 119,99 euroa, eli 10,00 euroa kuukaudessa, ja kolmella näytöllä 169,99 euroa, eli 14,17 euroa kuukaudessa. Näytöt tarkoittavat laitteita, jotka katsovat yhtä aikaa. Sovelluksen voi asentaa useampaan laitteeseen, mutta samaan aikaan toistoon valitaan 1, 2 tai 3 näyttöä.</p>
<h2>Mikä paketti sinulle sopii?</h2>
<ul><li><strong>Epävarma vielä:</strong> yksi kuukausi. Se ei uusiudu, joten mitään ei tarvitse irtisanoa.</li><li><strong>Edullisin kuukausihinta:</strong> kaksitoista kuukautta.</li><li><strong>Useampi katsoo yhtä aikaa:</strong> valitse 2 tai 3 näytön taso.</li></ul>
<p>Etkö ole varma, mikä sopii televisiollesi? Lue ensin <a href="/iptv-sovellus/">IPTV-sovellus ja asennus</a>, vertaa <a href="/paras-iptv-palvelu/">paras IPTV-palvelu -tarkistuslistaa</a> tai palaa <a href="/">IPTV Suomi -etusivulle</a>. Ehdot löytyvät <a href="/ehdot/">ehdoista</a>.</p>
<h2>Mitä IPTV hinta ei sisällä</h2>
<p>Hintaan ei ole piilotettu lisämaksuja, eikä mikään uusiudu automaattisesti. Et kuitenkaan saa ostettua tiettyä kanavaa erikseen, koska kaikissa paketeissa on sama sisältö. Jos tarvitset jonkin tietyn kanavan, kysy siitä ennen tilausta, niin kerromme suoraan, onko se mukana.</p>
<h2>Kysymyksiä paketeista</h2>
""" + faq_html(pf) + """
</div></div></section>
<section class="band"><div class="wrap band-in"><div><h2>Valmis tilaamaan?</h2><p>Kerro paketti ja televisio, niin hoidamme loput.</p></div>
<a class="btn" data-track="buy_click" href="{{WA:Hei! Haluan tilata Tilaa IPTV:n.}}" rel="noopener" target="_blank">{{I:chat}} Tilaa WhatsAppissa</a></div></section>
""")

    # ------------------------------------------------------------------ PARAS IPTV PALVELU
    q = [("Mikä IPTV on paras Suomessa?", "Paras IPTV on se, jossa on vakaa sovellus juuri sinun televisiollesi, katsomasi kanavat ja myyjä, joka vastaa kysymyksiin. Kokeile yhtä kuukautta ennen pidempää sitoutumista."),
         ("Kannattaako valita halvin paketti?", "Ei automaattisesti. Matala hinta on hyvä vain, jos kuva on vakaa ja joku auttaa, kun ei ole. Vertaa sitoutumista, uusiutumista ja tukea, älä vain hintaa.")]
    save("fi", "paras-iptv-palvelu", {"keyword": "paras iptv palvelu", "crumb": "Paras IPTV-palvelu", "alt": "best-iptv-finland",
        "title": "Paras IPTV palvelu: 7 tarkistuskohtaa ennen valintaa",
        "desc": "Paras IPTV palvelu Suomessa: seitsemän käytännön tarkistuskohtaa vakaudelle, sovelluksille, kanaville, sitoutumiselle ja tuelle, jotta valitset sopivan.",
        "og": "Paras IPTV palvelu: 7 tarkistuskohtaa ennen valintaa", "img_alt": "Paras IPTV palvelu: seitsemän tarkistuskohtaa ennen valintaa",
        "tldr": "Paras IPTV palvelu toimii vakaasti omalla televisiollasi, sisältää katsomasi kanavat, näyttää TV-oppaan, ei sido pitkään ja antaa oikeaa tukea. Kokeile ensin yhtä kuukautta ja käy läpi tämän sivun seitsemän kohtaa.",
        "schema": [faq_schema(q)]},
"""
<section class="page-head"><div class="wrap"><span class="eyebrow">Näin valitset</span><h1>Paras IPTV palvelu: näin valitset oikean</h1>
<p>Kaikille parasta IPTV:tä ei ole. On vain paras sinun televisiollesi, nettiyhteydellesi ja tavoillesi. Nämä ovat tarkistukset, jotka tekisimme itse.</p></div></section>
<section class="sec sec-tight"><div class="wrap"><div class="measure prose">
<!--TOC-->
<p>Kun etsit parasta IPTV-palvelua, löydät pitkiä listoja isoilla luvuilla ja vähillä faktoilla. Tämä sivu tekee toisin. Se antaa seitsemän tarkistusta, jotka ehdit tehdä yhdessä illassa, riippumatta siitä, minkä palvelun lopulta valitset.</p>
<h2>Mitä paras IPTV palvelu tarkoittaa?</h2>
<p>Useimmille kotitalouksille paras IPTV on tylsää oikealla tavalla. Televisio käynnistyy, kun painat kaukosäädintä, kuva pysyy kasassa lauantai-iltana ja opas näyttää oikean ohjelman. Kanavamäärät ja isot lupaukset kertovat siitä vähän. Vakaus, sovellukset ja tuki kertovat paljon.</p>
<h2>Seitsemän tarkistusta parhaalle IPTV-palvelulle</h2>
<ol>
<li><strong>Vakaus.</strong> Testaa omalla televisiollasi, illalla, kun muut ovat netissä. Yksi kuukausi on reilu testi.</li>
<li><strong>Sovellus televisiollesi.</strong> Kysy, mikä sovellus toimii juuri sinun mallissasi, ennen kuin maksat. Samsungilla, LG:llä, Fire TV:llä, Android TV:llä ja Apple TV:llä on kullakin oma sovelluskauppansa.</li>
<li><strong>TV-opas (EPG).</strong> Sen pitää näyttää, mitä tulee nyt ja myöhemmin, ei vain kanavalistaa.</li>
<li><strong>Kanavat, joita katsot.</strong> Kysy tietyistä kanavista kirjallisesti. Tarjonta voi muuttua ajan myötä, ja rehellinen myyjä sanoo sen.</li>
<li><strong>Ei pitkää sitoumusta.</strong> Tilaus, joka päättyy itsestään, on helpompi jättää kuin sellainen, jonka joutuu irtisanomaan.</li>
<li><strong>Oikea tuki.</strong> Saatko kirjoittaa ihmiselle kuvan kanssa ja saada vastauksen? Testaa yhdellä kysymyksellä ennen ostoa.</li>
<li><strong>Avoimuus oikeuksista.</strong> Hyvä myyjä ei piilota sitä, mitä se ei voi luvata. Ole varovainen isoilla luvuilla, joita et voi tarkistaa.</li>
</ol>
<h2>Näin testaat parasta IPTV:tä ennen sitoutumista</h2>
<p>Aloita lyhimmällä paketilla. Käytä sitä viikon tavallisina iltoina. Vaihda kanavaa, avaa opas, keskeytä ja kelaa takaisin, jos sovellus sallii, ja katso suora ottelu tai uutislähetys. Jos kuva pätkii, lähetä myyjälle kuva ja katso, kuinka nopeasti ja selkeästi vastaus tulee. Tuo yksi vastaus kertoo enemmän kuin mikään lista.</p>
<h2>Paras IPTV palvelu eri kotitalouksille</h2>
<p>Yksin asuvalle paras IPTV palvelu on usein yhden näytön paketti ja yhden kuukauden koe. Pariskunnalle, joka katsoo eri ohjelmia eri huoneissa, sopii kahden näytön taso. Perheelle, jossa jokaisella on oma näyttö, kolmen näytön taso on selkein, ja kahdentoista kuukauden jakso tekee kuukausihinnasta edullisimman. Tärkeintä on, että testaat ennen pitkää sitoutumista.</p>
<h2>Mitä kysyä myyjältä ennen kuin maksat</h2>
<ul><li>Mikä sovellus toimii juuri minun televisiomallissani?</li><li>Uusiutuuko tilaus automaattisesti, ja tallennetaanko korttitietoni?</li><li>Onko kanava, jota katson, mukana, ja voiko tarjonta muuttua?</li><li>Miten tukeen saa yhteyden, ja millä kielellä siellä vastataan?</li></ul>
<p>Jos myyjä vastaa kaikkiin selkeästi ennen maksua, se on hyvä merkki. Jos vastaukset ovat vältteleviä, jatka etsimistä.</p>
<h2>Varoitusmerkkejä, kun etsit parasta IPTV:tä</h2>
<ul><li>Pyöreät luvut kuten «99,9 % käytettävyys» tai kymmeniä tuhansia kanavia ilman todisteita.</li><li>Ihmiseen ei saa yhteyttä tai ehdot ovat epäselvät.</li><li>Painostus maksaa pitkä paketti heti.</li></ul>
<p>Kilpailu- ja kuluttajavirasto antaa selkeitä neuvoja digitaalisten palvelujen ostamiseen <a href="https://www.kkv.fi/" target="_blank" rel="noopener">omilla sivuillaan</a>.</p>
<h2>Miksi kokeilu on tärkeämpi kuin vertailu</h2>
<p>Vertailulista kertoo, mitä myyjä väittää, mutta oma testi kertoo, mitä saat. Kymmenen minuuttia omalla televisiolla paljastaa enemmän kuin kymmenen verkkosivua.</p>
<h2>Mihin Tilaa IPTV asettuu</h2>
<p>Pyrimme täyttämään nämä tarkistukset, ja sinun kannattaa testata meitä samalla tavalla. Paketit alkavat 15,99 eurosta yhdeltä kuukaudelta, mikään ei uusiudu automaattisesti ja tuki on WhatsAppissa. Katso <a href="/iptv-hinta/">IPTV hinta</a>, lue miten <a href="/iptv-sovellus/">IPTV-sovellus asennetaan</a> tai palaa <a href="/">IPTV Suomi -etusivulle</a>. Tämän sivun englanninkielinen versio on <a href="/en/best-iptv-finland/" hreflang="en" lang="en">Best IPTV in Finland</a>.</p>
<h2>Kysymyksiä paremman IPTV:n valinnasta</h2>
""" + faq_html(q) + """
</div></div></section>
<section class="band"><div class="wrap band-in"><div><h2>Haluatko testata itse?</h2><p>Aloita yhdestä kuukaudesta ja arvioi se omalla televisiollasi.</p></div>
<a class="btn" data-track="buy_click" href="{{WA:Hei! Haluan kokeilla Tilaa IPTV:tä yhden kuukauden.}}" rel="noopener" target="_blank">{{I:chat}} Kirjoita meille WhatsAppissa</a></div></section>
""")

    # ------------------------------------------------------------------ KANAVAT
    qk = [("Mitä kanavia IPTV-tilaukseen kuuluu?", "Paketissa on suomalaisia kanavia sekä muita pohjoismaisia kanavia. Kanavatarjonta voi muuttua ajan myötä, joten kysy tietystä kanavasta WhatsAppissa ennen tilaamista."),
          ("Voinko kysyä tietystä kanavasta?", "Kyllä. Kirjoita meille kanavan nimi, niin kerromme suoraan, onko se paketissa.")]
    save("fi", "iptv-kanavat", {"keyword": "iptv kanavat", "crumb": "IPTV kanavat", "alt": None,
        "title": "IPTV kanavat: 5 asiaa tarkistaa ennen tilaamista | Tilaa IPTV",
        "desc": "IPTV kanavat selitettynä: suomalaiset ja pohjoismaiset kanavat, TV-opas ja mitä kannattaa kysyä ennen tilausta. Kirjoittanut tukitiimimme.",
        "og": "IPTV kanavat: 5 asiaa tarkistaa ennen tilaamista", "img_alt": "IPTV kanavat: suomalaiset ja pohjoismaiset kanavat sekä TV-opas",
        "tldr": "IPTV kanavat tulevat internetin kautta suomalaisina ja pohjoismaisina kanavina yhdessä sovelluksessa TV-oppaan kanssa. Kanavatarjonta voi muuttua ajan myötä, joten kysy tietystä kanavasta ennen tilaamista.",
        "schema": [faq_schema(qk)]},
"""
<section class="page-head"><div class="wrap"><span class="eyebrow">Kanavat</span><h1>IPTV kanavat: mitä paketissa on ja mitä kannattaa kysyä</h1>
<p>Kanavalistaa tärkeämpää on tietää, mitä kysyä. Tässä käymme läpi, miten IPTV kanavat toimivat sovelluksessa ja mitä kannattaa tarkistaa ennen tilausta.</p></div></section>
<section class="sec sec-tight"><div class="wrap"><div class="measure prose">
<!--TOC-->
<p>Kun puhutaan IPTV kanavista, tarkoitetaan televisiokanavia, jotka tulevat internetin kautta sovellukseen. Sovellus näyttää kanavat listana ja TV-oppaana, ja vaihdat kanavaa kuten tavallisella kaukosäätimellä. Mitään antennia tai kaapelirasiaa ei tarvita.</p>
<h2>Mitä IPTV kanavat sisältävät</h2>
<p>Tilaa IPTV:ssä suomalaiset kanavat ovat ensin, ja niiden jälkeen tulevat muut pohjoismaiset kanavat sekä kansainväliset kanavat. Sisältöä on uutisista ja viihteestä lastenkanaviin, urheiluun ja dokumentteihin. Kanavatarjonta voi muuttua ajan myötä, joten emme lupaa listaa, jota emme voi todistaa.</p>
<h2>TV-opas auttaa löytämään ohjelmat</h2>
<p>TV-opas (EPG) näyttää, mitä kanavilla tulee nyt ja myöhemmin. Jos jonkin ohjelman aika tai nimi näyttää väärältä, kerro meille kanava, niin tarkistamme opastiedot yhdessä kanssasi.</p>
<h2>Viisi asiaa, jotka kannattaa tarkistaa</h2>
<ol><li>Kysy tietyistä kanavista kirjallisesti ennen tilausta.</li><li>Varmista, että sovellus toimii juuri sinun televisiomallissasi.</li><li>Tarkista, että nettiyhteys riittää: 10 Mbit/s per näyttö HD:lle ja 25 Mbit/s 4K:lle.</li><li>Kysy, uusiutuuko tilaus automaattisesti.</li><li>Testaa tukea yhdellä kysymyksellä ennen pitkää pakettia.</li></ol>
<h2>Kuinka monta näyttöä tarvitset?</h2>
<p>Yksi näyttö riittää, jos katsoja on yksi kerrallaan. Valitse kaksi, jos kaksi henkilöä haluaa katsoa eri kanavia samaan aikaan, ja kolme, jos koko perheellä on omat näyttönsä. Tilaus alkaa 15,99 eurosta kuukaudelta, ja kaikki hinnat löydät sivulta <a href="/iptv-hinta/">IPTV hinta</a>.</p>
<h2>IPTV kanavat ja kuvanlaatu</h2>
<p>Kanavat toimitetaan HD-laadulla, ja 4K-kuvaa saat silloin, kun kanava itse lähettää 4K:na. Hyvä kuva vaatii riittävän nopean yhteyden: vähintään 10 Mbit/s per näyttö HD:lle ja 25 Mbit/s 4K:lle. Jos kuva pätkii, ongelma on useimmiten wifissä, ei kanavissa, ja siirtyminen verkkokaapeliin korjaa sen usein.</p>
<h2>IPTV kanavat eri laitteilla</h2>
<p>Samat IPTV kanavat toimivat Samsung- ja LG-televisioissa, Android TV:ssä, Fire TV Stickissä, Apple TV:ssä, puhelimessa ja tietokoneella. Kun vaihdat laitetta, kirjaudut samoilla tunnuksilla, ja kanavalista on valmiina. Voit siis katsoa uutiset puhelimesta keittiössä ja ottelun televisiosta olohuoneessa.</p>
<h2>Mitä IPTV kanavat eivät ole</h2>
<p>IPTV ei ole tavallinen antennitelevisio, ja kanavatarjonta voi muuttua. Emme lupaa tiettyä määrää kanavia tai tiettyä kanavaa ilman, että olemme varmistaneet sen sinulle. Siksi neuvomme kysymään tietystä kanavasta etukäteen ja aloittamaan yhdestä kuukaudesta.</p>
<h2>IPTV kanavat ja TV-opas yhdessä</h2>
<p>Kanavalista kertoo, mitä on olemassa, ja TV-opas kertoo, mitä tulee juuri nyt. Kun avaat sovelluksen, näet molemmat samassa näkymässä. Voit hypätä suoraan kanavalle tai selata opasta ja valita ohjelman. Tämä tekee IPTV kanavista käytännössä yhtä helpon kuin tavallisen television, vaikka kaikki tulee internetin kautta.</p>
<h2>Kysymyksiä, jotka kannattaa esittää</h2>
<p>Kysy ennen tilausta, onko jokin sinulle tärkeä kanava mukana, ja pyydä vastaus kirjallisesti. Kysy myös, millä laitteilla katsot, koska sovelluksen valinta riippuu televisiosta. Näin vältät ikävät yllätykset ja tiedät, mitä tilaat.</p>
<h2>Mistä aloittaa</h2>
<p>Tärkein neuvomme on yksinkertainen: kirjoita meille WhatsAppissa ne kolme tai neljä kanavaa, jotka katsot varmasti joka viikko, ja kysy, ovatko ne mukana. Vastaamme suoraan, ja sinä päätät vasta sen jälkeen. Aloita yhdestä kuukaudesta ja katso, toimivatko kanavat, jotka sinulle ovat tärkeitä. Lue myös <a href="/paras-iptv-palvelu/">paras IPTV-palvelu -tarkistuslista</a>, <a href="/iptv-sovellus/">sovellus- ja asennusopas</a> tai <a href="/">IPTV Suomi -etusivu</a>. Verkon nopeuden voit mitata esimerkiksi <a href="https://www.traficom.fi/" target="_blank" rel="noopener">Traficomin</a> ohjeiden avulla.</p>
<h2>Kuinka monta näyttöä tarvitset kanaville?</h2>
<p>Yksi näyttö riittää, kun vain yksi katsoo kerrallaan. Jos eri henkilöt haluavat katsoa eri kanavia samaan aikaan, valitse kaksi tai kolme näyttöä. Kanavat ovat samat kaikissa tasoissa, ja vain hinta muuttuu näyttöjen mukaan. Kokeile ensin yhtä kuukautta ja katso, kuinka monta näyttöä oikeasti käytätte.</p>
<h2>Kysymyksiä IPTV kanavista</h2>
""" + faq_html(qk) + """
</div></div></section>
<section class="band"><div class="wrap band-in"><div><h2>Kysymys kanavasta?</h2><p>Kirjoita, mikä kanava kiinnostaa, niin vastaamme rehellisesti.</p></div>
<a class="btn" data-track="buy_click" href="{{WA:Hei! Kysyisin yhdestä kanavasta Tilaa IPTV:ssä.}}" rel="noopener" target="_blank">{{I:chat}} Kirjoita meille WhatsAppissa</a></div></section>
""")

    # ------------------------------------------------------------------ SOVELLUS / ASENNUS
    save("fi", "iptv-sovellus", {"keyword": "iptv sovellus", "crumb": "IPTV sovellus", "alt": "install-iptv",
        "title": "IPTV sovellus: asennus 3 vaiheessa televisioon ja puhelimeen",
        "desc": "IPTV sovellus: näin asennat sen Samsung- ja LG-televisioon, Fire TV Stickiin, Android TV:hen, Apple TV:hen, iPhoneen ja tietokoneelle. Vaiheet ja tuki.",
        "og": "IPTV sovellus: asennus 3 vaiheessa televisioon ja puhelimeen",
        "tldr": "IPTV sovelluksen asennus tehdään kolmessa vaiheessa: valitse paketti, saat tunnukset WhatsAppissa ja asennat sovelluksen televisioosi, boksiisi tai puhelimeesi. Se vie muutaman minuutin, kun nopeutta on 10 Mbit/s per näyttö ja sovellus sopii malliisi."},
"""
<section class="page-head"><div class="wrap"><span class="eyebrow">Asennus</span><h1>IPTV sovellus: Smart TV, Fire TV, Apple TV ja puhelin</h1>
<p>Erikoislaitteita ei tarvita. Tarvitset sovelluksen laitteellesi, tunnuksesi ja riittävän nopean yhteyden.</p></div></section>
<section class="sec sec-tight"><div class="wrap"><div class="measure prose">
<!--TOC-->
<p>IPTV sovelluksen asennus noudattaa samoja kolmea vaihetta jokaisella laitteella. Yksityiskohdat vaihtelevat merkeittäin, ja siksi kysymme mallisi ennen kuin suosittelemme sovellusta.</p>
<h2>IPTV sovellus: mikä se on?</h2>
<p>IPTV sovellus on ohjelma, jolla katsot televisiokanavia internetin kautta. Se näyttää kanavalistan ja TV-oppaan, ja kirjaudut siihen tunnuksilla, jotka saat meiltä WhatsAppissa. Sovellus ei sisällä kanavia itsessään, vaan se on soitin, joka näyttää tilaukseesi kuuluvat kanavat.</p>
<h2>Mikä IPTV sovellus sopii televisiollesi?</h2>
<p>Oikea IPTV sovellus riippuu television merkistä, mallista ja vuodesta. Samsungilla ja LG:llä on omat sovelluskauppansa, Fire TV:llä ja Android TV:llä omansa ja Apple TV:llä App Store. Siksi kysymme mallisi ensin, ja suosittelemme sovellusta, jonka tiedämme toimivan siinä.</p>
<h2>Tarkista nettisi ennen kuin asennat IPTV sovelluksen</h2>
<p>Laske vähintään 10 Mbit/s per näyttö HD-kuvalle ja 25 Mbit/s 4K:lle. Mittaa televisiolla tai boksilla, ei puhelimella, koska televisio on usein kauempana reitittimestä. Verkkokaapeli on lähes aina vakaampi kuin wifi.</p>
<h2>Kolme vaihetta IPTV sovelluksen asennukseen</h2>
<ol><li><strong>Tilaa ja saat tunnukset.</strong> Kirjoita meille WhatsAppissa haluamasi paketti ja television tai boksin malli.</li><li><strong>Asenna sovellus.</strong> Avaa laitteen sovelluskauppa, asenna mallillesi suosittelemamme IPTV-soitin ja avaa se.</li><li><strong>Kirjaudu.</strong> Anna lähettämämme tiedot. Kanavalista ja TV-opas latautuvat minuutissa tai kahdessa.</li></ol>
<h2>Samsung- ja LG-Smart TV</h2>
<p>Useimmat noin vuodesta 2018 alkaen valmistetut mallit voivat ajaa IPTV-sovellusta television oman sovelluskaupan kautta. Saatavilla olevat sovellukset riippuvat mallista ja vuodesta, joten lähetä meille mallinumero television takana olevasta tarrasta.</p>
<h2>Fire TV Stick ja Android TV</h2>
<p>Näillä on laajin sovellusvalikoima. Avaa sovelluskauppa, etsi suosittelemamme soitin ja asenna se. Amazon selittää perusteet <a href="https://www.amazon.com/gp/help/customer/display.html?nodeId=GYXQJZZ2VAXYW9H9" target="_blank" rel="noopener">Fire TV:n ohjesivuillaan</a>.</p>
<h2>Apple TV, iPhone ja iPad</h2>
<p>Asenna IPTV-soitin App Storesta ja kirjaudu lähettämillämme tiedoilla. Apple kertoo sovellusten asentamisesta <a href="https://support.apple.com/fi-fi/apple-tv" target="_blank" rel="noopener">Apple TV:n tukisivuillaan</a>.</p>
<h2>MAG-boksi ja tietokone</h2>
<p>MAG-boksi liitetään tiliisi boksin MAC-osoitteella, ja teemme sen asetuksen puolestasi. Tietokoneella voit käyttää VLC:tä tai IPTV-sovellusta.</p>
<h2>Yleisiä ongelmia IPTV sovellus -asennuksessa</h2>
<ul><li><strong>Sovellusta ei löydy kaupasta:</strong> televisiosi voi olla liian vanha. Kerro malli, niin ehdotamme toista laitetta.</li><li><strong>Kirjautuminen ei onnistu:</strong> tarkista tunnukset ja isot ja pienet kirjaimet. Kopioi tiedot suoraan viestistä.</li><li><strong>Kanavalista on tyhjä:</strong> odota minuutti, sulje sovellus ja avaa se uudelleen.</li><li><strong>Kuva pätkii:</strong> siirry verkkokaapeliin ja tarkista nopeus.</li></ul>
<h2>IPTV sovellus ja tilaus: mitä sinun kannattaa tietää</h2>
<p>Sovelluksen lataaminen ei maksa meille mitään, eikä se tee mitään ilman tunnuksia. Tilaus alkaa 15,99 eurosta kuukaudelta, ja mikään ei uusiudu automaattisesti. Jos sovellus ei toimi televisiossasi, kerro meille malli, niin etsimme toisen vaihtoehdon ennen kuin maksat pidemmästä paketista.</p>
<h2>Kun asennus on valmis</h2>
<p>Muista, että tunnukset ovat henkilökohtaiset, joten älä jaa niitä muille. Avaa kanavalista ja tarkista, että TV-opas latautuu. Valitse sitten kanava, jota katsot eniten, ja katso sitä noin kymmenen minuuttia. Jos kuva on tasainen, kaikki on kunnossa. Jos ei, kerro meille mallisi ja kuvaile ongelma, niin autamme eteenpäin.</p>
<h2>Jos kuva pätkii asennuksen jälkeen</h2>
<p>Siirrä televisio verkkokaapeliin, käynnistä reititin uudelleen ja sulje muu suoratoisto verkossa. Jos kuva yhä pätkii, lähetä meille kuva näytöstä WhatsAppissa.</p>
<h2>Kuinka kauan IPTV sovellus -asennus kestää?</h2>
<p>Kun sovellus sopii televisiosi malliin, asennus vie yleensä muutaman minuutin. Pisimpään kestää oikean sovelluksen löytäminen, ei itse asennus. Kerro siksi mallisi ensin WhatsAppissa, niin saat suoraan oikean ohjeen ja säästät aikaa.</p>
<h2>Mitä tarvitset ennen kuin aloitat</h2>
<ul><li>Television tai boksin malli tarrasta tai asetusvalikosta.</li><li>Nettiyhteys, jossa on vähintään 10 Mbit/s per näyttö.</li><li>Tunnuksesi meiltä WhatsAppissa.</li><li>Tili laitteen sovelluskaupassa (Samsung, LG, Google, Amazon tai Apple).</li></ul>
<p>Valmis aloittamaan? Katso <a href="/iptv-hinta/">hinnat ja paketit</a>, lue <a href="/iptv-kanavat/">IPTV kanavista</a> tai palaa <a href="/">IPTV Suomi -etusivulle</a>.</p>
</div></div></section>
<section class="band"><div class="wrap band-in"><div><h2>Jäitkö jumiin vaiheessa?</h2><p>Lähetä television malli, niin kerromme, mitä tehdä.</p></div>
<a class="btn" data-track="buy_click" href="{{WA:Hei! Tarvitsen apua IPTV-sovelluksen asennuksessa.}}" rel="noopener" target="_blank">{{I:chat}} Kysy WhatsAppissa</a></div></section>
""")

    # ------------------------------------------------------------------ UKK
    save("fi", "ukk", {"crumb": "UKK", "alt": "faq",
        "title": "IPTV Suomi UKK: kysymyksiä ja vastauksia | Tilaa IPTV",
        "desc": "Vastauksia Tilaa IPTV:stä: paketit, maksutavat, nopeus, laitteet, uusiutuminen ja laillisuus. Lyhyet ja suorat vastaukset tukitiimiltämme.",
        "schema": [faq_schema(FAQ)]},
"""
<section class="page-head"><div class="wrap"><span class="eyebrow">UKK</span><h1>Usein kysyttyä IPTV:stä</h1><p>Useimmin kysytyt kysymykset, vastattuna suoraan.</p></div></section>
<section class="sec sec-tight"><div class="wrap">""" + faq_html(FAQ) + """
<p style="margin-top:24px">Puuttuuko jotain? <a href="/yhteystiedot/">Ota yhteyttä</a>, katso <a href="/iptv-hinta/">paketit</a> tai palaa <a href="/">IPTV Suomi -etusivulle</a>.</p></div></section>
""")

    # ------------------------------------------------------------------ TIETOA
    save("fi", "tietoa-meista", {"crumb": "Tietoa meistä", "alt": "about",
        "title": "Tietoa Tilaa IPTV:stä: kuka kirjoittaa oppaat ja miksi",
        "desc": "Tietoa Tilaa IPTV:stä: riippumaton IPTV-palvelu Suomeen, miten tukitiimi kirjoittaa oppaat ja mitä väitteitä emme tee. Rehellisesti ja ilman liioittelua.",
        "schema": [{"@context": "https://schema.org", "@type": "AboutPage", "name": "Tietoa meistä", "url": BASE + "/tietoa-meista/", "inLanguage": "fi"}]},
"""
<section class="page-head"><div class="wrap"><span class="eyebrow">Tietoa</span><h1>Tietoa Tilaa IPTV:stä</h1>
<p>Riippumaton IPTV-palvelu suomalaisille kotitalouksille, tuki WhatsAppissa.</p></div></section>
<section class="sec sec-tight"><div class="wrap"><div class="measure prose">
<p>Tilaa IPTV myy IPTV-tilauksia suomalaisilla ja pohjoismaisilla kanavilla. Meillä ei ole yhteyttä sivulla mainittuihin TV-yhtiöihin, sovelluksiin tai valmistajiin. Tilaus, maksu ja apu hoituvat WhatsAppissa.</p>
<h2 id="how-we-write">Näin kirjoitamme oppaat</h2>
<p>Oppaat kirjoittaa tukitiimi, samat ihmiset jotka vastaavat WhatsAppissa. Kirjoitamme kysymyksistä, joita asiakkaat oikeasti esittävät. Asetukset ja sovellusten toiminnot tarkistetaan valmistajien omilta ohjesivuilta, joihin linkitämme jokaisen oppaan alla, ja korjaamme tekstin, kun jokin muuttuu.</p>
<h2>Mitä emme väitä</h2>
<p>Emme julkaise keksittyjä lukuja, kuten käytettävyysprosentteja, arvostelupisteitä tai kanavamääriä, joita emme voi todistaa. Kun emme tiedä jotain, sanomme sen. Kanavatarjonta voi muuttua ajan myötä, joten pyydämme tarkistamaan tietyn kanavan kanssamme ennen tilaamista.</p>
<p>Lue <a href="/ehdot/">ehdot</a>, <a href="/tietosuoja/">tietosuojaseloste</a> tai siirry <a href="/yhteystiedot/">yhteystietoihin</a>.</p>
</div></div></section>
""")

    # ------------------------------------------------------------------ YHTEYS
    save("fi", "yhteystiedot", {"crumb": "Yhteystiedot", "alt": "contact",
        "title": "Ota yhteyttä Tilaa IPTV:hen: WhatsApp ja yhteydenottolomake",
        "desc": "Ota yhteyttä Tilaa IPTV:hen WhatsAppissa tilauksiin, asennukseen ja vianetsintään tai käytä lomaketta. Mitä kannattaa kertoa ensimmäisessä viestissä.",
        "schema": [{"@context": "https://schema.org", "@type": "ContactPage", "name": "Yhteystiedot", "url": BASE + "/yhteystiedot/", "inLanguage": "fi"}]},
"""
<section class="page-head"><div class="wrap"><span class="eyebrow">Yhteys</span><h1>Ota yhteyttä</h1>
<p>WhatsApp on nopein, sekä tilaukseen että asennusapuun. Kerro, mikä televisio tai boksi sinulla on, niin osaamme vastata oikeaan asiaan.</p></div></section>
<div class="wrap"><div class="prose">
<p><a class="btn" data-track="buy_click" href="{{WA:Hei! Minulla on kysymys Tilaa IPTV:stä.}}" rel="noopener" target="_blank">Kirjoita WhatsAppissa</a></p>
<div class="table-wrap"><table><tbody><tr><th scope="row">WhatsApp</th><td>""" + SITE["whatsapp_display"] + """</td></tr><tr><th scope="row">Kielet</th><td>Suomi ja englanti</td></tr></tbody></table></div>
<h2>Kerro tämä ensimmäisessä viestissä</h2>
<p>Asennusapuun kirjoita television tai boksin merkki ja malli, ja lähetä kuva näytöstä, jos näkyy virheilmoitus. Tilaukseen kirjoita haluamasi paketti. Hinnat löytyvät sivulta <a href="/iptv-hinta/">IPTV hinta</a>. Asennusvaiheet ovat oppaassa <a href="/iptv-sovellus/">IPTV sovellus</a>, ja <a href="/ehdot/">ehdot</a> kertovat, mitä tilaukseen sovelletaan.</p>
<h2>Haluatko mieluummin lomakkeen?</h2>
<p>Käytä sivun alalaidan yhteydenottolomaketta, niin vastaamme antamaasi osoitteeseen.</p>
</div></div>
""")

    # ------------------------------------------------------------------ LEGAL
    save("fi", "ehdot", {"crumb": "Ehdot", "alt": "terms",
        "title": "Tilaa IPTV:n ehdot | Paketit ja uusiutuminen",
        "desc": "Tilaa IPTV:n palveluehdot: paketit, maksu, ei automaattista uusiutumista, tuki, käyttö ja kuluttajan oikeutesi Suomessa."},
"""
<section class="page-head"><div class="wrap"><span class="eyebrow">Ehdot</span><h1>Ehdot</h1><p>Lyhyesti ja selkeästi. Päivitetty viimeksi marraskuussa 2026.</p></div></section>
<div class="wrap"><div class="prose">
<h2>Palvelu</h2><p>Tilaa IPTV myy pääsyn IPTV-palveluun suomalaisilla ja pohjoismaisilla kanavilla. Kanavatarjonta voi muuttua ajan myötä. Voit kysyä tietystä kanavasta WhatsAppissa ennen tilaamista.</p>
<h2>Paketit ja maksu</h2><p>Valitset keston (1, 3, 6 tai 12 kuukautta) ja näyttöjen määrän (1, 2 tai 3). Tilaat ja maksat WhatsAppin kautta. Hinnat ilmoitetaan euroina.</p>
<h2>Uusiutuminen</h2><p>Mikään ei uusiudu automaattisesti. Emme tallenna korttitietoja. Kun jakso päättyy, palvelu päättyy, ellet tilaa uudelleen.</p>
<h2>Tuki ja ongelmat</h2><p>Jos jokin ei toimi, kirjoita meille WhatsAppissa kuva näytöstä, niin käymme yhdessä läpi yhteyden, sovelluksen ja asetukset.</p>
<h2>Oikeutesi</h2><p>Lakisääteiset kuluttajan oikeutesi Suomen lain mukaan eivät muutu näiden ehtojen vuoksi.</p>
<h2>Käyttö</h2><p>Palvelu on tarkoitettu yksityiseen käyttöön taloudessasi. Vastaat itse siitä, miten käytät sitä, ja siitä, että noudatat sinua koskevaa lakia.</p>
<p>Kysyttävää? <a href="/yhteystiedot/">Ota yhteyttä</a>. Katso myös <a href="/tietosuoja/">tietosuojaseloste</a> ja <a href="/iptv-hinta/">paketit</a>.</p>
</div></div>
""")
    save("fi", "tietosuoja", {"crumb": "Tietosuoja", "alt": "privacy",
        "title": "Tilaa IPTV:n tietosuojaseloste | Mitä tallennamme",
        "desc": "Tilaa IPTV:n tietosuoja: mitä keräämme tilatessasi tai käyttäessäsi yhteydenottolomaketta, kuinka kauan säilytämme tiedot ja miten pyydät poistoa."},
"""
<section class="page-head"><div class="wrap"><span class="eyebrow">Tietosuoja</span><h1>Tietosuojaseloste</h1><p>Mitä tallennamme ja miksi. Päivitetty viimeksi marraskuussa 2026.</p></div></section>
<div class="wrap"><div class="prose">
<h2>Mitä keräämme</h2><p>Kun kirjoitat meille WhatsAppissa, näemme puhelinnumerosi ja lähettämäsi viestit. Kun käytät yhteydenottolomaketta, saamme kirjoittamasi nimen, yhteystiedot ja viestin. Käytämme niitä vain vastataksemme sinulle ja toimittaaksemme tilauksesi.</p>
<h2>Mitä emme tee</h2><p>Emme myy tietojasi, emme tallenna korttitietoja emmekä käytä mainosseurantaa.</p>
<h2>Tilastot</h2><p>Jos hyväksyt, laskemme sivunäytöt ja klikkaukset sivun parantamiseksi. Evästeitä ei käytetä. Jos kieltäydyt, mitään ei lasketa. Voit muuttaa valintaa <a href="/evasteet/">evästeet ja tilastot -sivulla</a>.</p>
<h2>Oikeutesi</h2><p>Voit pyytää meitä näyttämään, korjaamaan tai poistamaan sinusta tallennetut tiedot. Kirjoita meille <a href="/yhteystiedot/">yhteystietosivulla</a>.</p>
<p>Katso myös <a href="/ehdot/">ehdot</a> ja <a href="/">etusivu</a>.</p>
</div></div>
""")
    save("fi", "evasteet", {"crumb": "Evästeet ja tilastot", "alt": "cookies",
        "title": "Evästeet ja tilastot Tilaa IPTV:ssä | Sinun valintasi",
        "desc": "Tilaa IPTV ei käytä evästeitä. Valinnainen tilasto laskee käynnit ja klikkaukset vain, jos hyväksyt. Näin se toimii ja näin muutat valintaa."},
"""
<section class="page-head"><div class="wrap"><span class="eyebrow">Evästeet</span><h1>Evästeet ja tilastot</h1></div></section>
<div class="wrap"><div class="prose">
<p>Tämä sivusto ei aseta evästeitä. Valinnainen tilasto laskee sivunäytöt ja klikkaukset sivun parantamiseksi, ja se latautuu vain, jos painat Hyväksy. Kieltäytyminen on oletus.</p>
<p><button class="btn btn-sm btn-line" type="button" data-consent-reset>Muuta valintaani</button></p>
<p>Lisää <a href="/tietosuoja/">tietosuojaselosteessa</a>. Katso myös <a href="/ehdot/">ehdot</a>, <a href="/">etusivu</a> ja <a href="/yhteystiedot/">yhteystiedot</a>.</p>
</div></div>
""")
    save("fi", "404", {"crumb": "Ei löytynyt", "robots": "noindex, follow", "title": "Sivua ei löytynyt | Tilaa IPTV", "desc": "Tätä sivua ei ole. Palaa etusivulle tai katso IPTV-paketit."},
"""
<section class="page-head"><div class="wrap"><h1>Sivua ei löytynyt</h1><p>Etsimääsi sivua ei ole. Siirry <a href="/">etusivulle</a> tai katso <a href="/iptv-hinta/">paketit</a>.</p></div></section>
""")

if __name__ == "__main__":
    pages(); pages2(); print("FI pages written")
