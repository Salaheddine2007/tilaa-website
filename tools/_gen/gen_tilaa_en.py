import sys
sys.path.insert(0, r"C:\Users\DELL\AppData\Local\Temp\claude\ac5e4f4ff9d25599\1da4b7fd-101c-468b-9d88-b4a6ba448f91\scratchpad")
from gen_tilaa_fi import *

TE = dict(mon={"1": "1 month", "3": "3 months", "6": "6 months", "12": "12 months"}, screen="screen", once="one-off price, no renewal", best="Best value",
          sub={"1": "Good for trying it", "3": "One season", "6": "Half a year", "12": "A full year"},
          incl=["Finnish and Nordic channels", "HD, and 4K where the channel has it", "TV guide (EPG)", "Install help on WhatsApp", "No automatic renewal"],
          order_msg="Hi! I'd like to order Tilaa IPTV: {m}, {d} ({p}).", pick="Choose {m}")

FAQE = [
 ("What is IPTV Finland?", "IPTV Finland means television delivered over your internet connection instead of an aerial, cable or dish. With Tilaa IPTV you watch Finnish and Nordic channels in an app on your TV, box, phone or computer."),
 ("Do I need to buy a box?", "Usually not. Samsung and LG TVs from recent years run IPTV with an app. On an older TV, a Fire TV Stick or an Android TV box is the cheapest way to get started."),
 ("What internet speed do I need?", "Plan for at least 10 Mbit/s per screen for HD and 25 Mbit/s for 4K. Measure on the TV or box itself, not on your phone. A network cable is almost always steadier than wifi."),
 ("Does the subscription renew automatically?", "No. We take no automatic payments and store no card details. When the period is ending you extend it yourself, if you want to."),
 ("How do I pay?", "You order on WhatsApp and get the payment details there. We accept Visa, Mastercard, Maestro, Apple Pay, Google Pay and PayPal, and from other EU countries also SEPA, iDEAL, Bancontact and giropay."),
 ("Can I try it before buying a longer plan?", "Yes. Start with one month for €15.99. It does not renew by itself, so there is nothing to cancel. If it works well, you can take a longer plan when the month is over."),
 ("Is IPTV legal in Finland?", "IPTV is just a technology, and it is legal. What matters is whether the channels you watch are licensed for distribution. We cannot give legal advice, so ask us what a plan includes before you order. You are responsible for how you use the service."),
]

def pages_en():
    save("en", "", {"speakable": True, "keyword": "iptv finland", "crumb": "Home", "alt": "",
        "title": "IPTV Finland 2026: Finnish and Nordic TV in HD from €5.83/mo",
        "desc": "IPTV Finland for households: Finnish and Nordic channels in HD, a TV guide and install help on WhatsApp. From €5.83/month, no contract. Order today.",
        "og": "IPTV Finland 2026: Finnish and Nordic TV in HD from €5.83 a month",
        "img_alt": "IPTV Finland: Finnish and Nordic TV in HD on Smart TV, box and phone",
        "images": [{"name": "en-home-devices", "title": "IPTV Finland on Smart TV, Fire TV Stick, Android TV and Apple TV", "alt": "IPTV Finland on Smart TV, Fire TV Stick, Android TV, Apple TV and MAG box"},
                   {"name": "en-home-steps", "title": "Get started with IPTV Finland in three steps", "alt": "Get started with IPTV Finland in three steps on WhatsApp"}],
        "schema": [{"@context": "https://schema.org", "@type": "Product", "name": "Tilaa IPTV subscription", "brand": {"@type": "Brand", "name": "Tilaa IPTV"},
                    "description": "IPTV subscription with Finnish and Nordic channels in HD for Smart TV, Android TV, Apple TV, phone and computer.", "image": BASE + "/assets/og/en-home.png",
                    "offers": {"@type": "AggregateOffer", "priceCurrency": "EUR", "lowPrice": "15.99", "highPrice": "169.99", "offerCount": "12", "availability": "https://schema.org/InStock", "url": BASE + "/en/iptv-subscription-finland/"}},
                   faq_schema(FAQE)]},
"""
<section class="hero">
  <div class="wrap hero-in">
    <div>
      <span class="pill"><span class="dot"></span>Live now · Finnish and Nordic TV in HD</span>
      <h1>IPTV Finland <span class="grad-text">for Finnish and Nordic TV</span> in HD</h1>
      <p class="lead">IPTV Finland should be simple: <b>Finnish and Nordic channels in HD</b>, in an app on the TV you already own. With Tilaa IPTV you pick 1, 3, 6 or 12 months and we help you install it on WhatsApp.</p>
      <div class="hero-cta">
        <a class="btn" data-track="buy_click" href="{{WA:Hi! I'd like to order Tilaa IPTV.}}" rel="noopener" target="_blank">{{I:chat}} Order on WhatsApp</a>
        <a class="btn btn-ghost" href="#pricing">See the prices →</a>
      </div>
      <ul class="chips"><li>{{I:check}} No contract</li><li>{{I:check}} HD, and 4K where available</li><li>{{I:check}} Smart TV to phone</li><li>{{I:check}} Support in English and Finnish</li></ul>
    </div>
    <div class="screen-wrap" aria-hidden="true">
      <div class="browser">
        <div class="browser-bar"><i></i><i></i><i></i><span>Tilaa IPTV · Films and series</span></div>
        <div class="posters">
          <figure><img src="/assets/posters/poster-1.webp" width="1200" height="677" alt="" fetchpriority="high"><figcaption><b class="live">LIVE</b><b>HD</b></figcaption></figure>
          <figure><img src="/assets/posters/poster-2.webp" width="1200" height="677" alt="" loading="lazy"><figcaption><b>4K</b></figcaption></figure>
          <figure><img src="/assets/posters/poster-3.webp" width="900" height="508" alt="" loading="lazy"><figcaption><b>HD</b></figcaption></figure>
        </div>
      </div>
      <div class="f-badge b1"><span class="ic">{{I:shield}}</span><span>No contract<small>nothing renews by itself</small></span></div>
      <div class="f-badge b2"><span class="ic">{{I:zap}}</span><span>€5.83/month<small>on the 12-month plan</small></span></div>
      <div class="f-badge b3"><span class="ic">{{I:spark}}</span><span>HD + 4K<small>where the channel has it</small></span></div>
    </div>
  </div>
</section>

<div class="wrap tiles" role="list" aria-label="Tilaa IPTV in numbers">
  <div role="listitem"><b>€5.83</b><span>per month on 12 months</span></div>
  <div role="listitem"><b>0</b><span>days of contract</span></div>
  <div role="listitem"><b>3</b><span>screens at the same time, if you want</span></div>
  <div role="listitem"><b>4</b><span>plans, same content</span></div>
</div>

<section class="strip" aria-label="Works on"><div class="wrap"><p>Works on the screens you already have</p><ul>
  <li>{{I:tv}} Samsung</li><li>{{I:tv}} LG</li><li>{{I:box}} Android TV</li><li>{{I:box}} Fire TV Stick</li><li>{{I:tv}} Apple TV</li><li>{{I:phone}} iPhone and Android</li><li>{{I:laptop}} Windows and Mac</li><li>{{I:box}} MAG box</li></ul></div></section>

<section class="sec">
  <div class="wrap measure">
    <p>This page is written for anyone searching for IPTV Finland who wants to know what they actually get. We go through the channels, the prices, which screens work and how to get started, and we say when we are not the right choice. Prefer Finnish? Go to the <a href="/" hreflang="fi" lang="fi">Finnish version</a>.</p>
    <h2 class="center-h">Tilaa IPTV at a glance</h2>
    <dl class="facts">
      <div><dt>Price</dt><dd>€15.99 to €169.99, from €5.83/month</dd></div>
      <div><dt>Plans</dt><dd>1, 3, 6 or 12 months, same content</dd></div>
      <div><dt>Contract</dt><dd>None, nothing renews automatically</dd></div>
      <div><dt>Channels</dt><dd>Finnish plus other Nordic channels</dd></div>
      <div><dt>Picture</dt><dd>HD, and 4K where the channel broadcasts in 4K</dd></div>
      <div><dt>Speed</dt><dd>10 Mbit/s per screen for HD, 25 for 4K</dd></div>
      <div><dt>Devices</dt><dd>Smart TV, Fire TV, Android TV, Apple TV, phone, computer, MAG</dd></div>
      <div><dt>Ordering</dt><dd>WhatsApp, in English or Finnish</dd></div>
      <div><dt>Payment</dt><dd>Card, Apple Pay, Google Pay, PayPal</dd></div>
    </dl>
    <!--TOC-->
  </div>
</section>

<section class="sec sec-tight">
  <div class="wrap measure"><div class="sec-head center"><span class="eyebrow">What is included</span><h2>Why Tilaa IPTV suits Finnish households</h2>
    <p>Good IPTV Finland is not about the longest channel list. It is about the TV starting when you press the remote, the guide showing the right programme and having someone to ask.</p></div></div>
  <div class="wrap feat">
""" + cards([
 ("cyan", "globe", "Finnish and Nordic channels", "News, entertainment, children's channels and sport, plus channels from other Nordic countries. The line-up can change over time. Ask us about a specific channel before you order and you get a straight answer."),
 ("violet", "spark", "HD as standard, 4K where it exists", "Channels are delivered in HD, and in 4K where the channel itself broadcasts in 4K. How sharp it looks at home also depends on your TV and connection."),
 ("pink", "calendar", "A TV guide (EPG) in the app", "A schedule that shows what is on now and later on every channel, like normal TV."),
 ("green", "wifi", "A steady picture on a Saturday night", "The picture should hold between 19:00 and 22:00, when everyone is online. Most things that make IPTV freeze sit inside the home, usually wifi, and we help you sort that out."),
 ("blue", "chat", "Everything in one chat", "Ordering, payment and help with the setup all happen in the same WhatsApp thread, in English or Finnish."),
]) + """
  </div>
</section>

<section class="sec sec-tight" id="pricing">
  <div class="wrap">
    <div class="sec-head"><span class="eyebrow">Prices</span><h2>What IPTV Finland costs: four plans, same content</h2>
      <p>Choose how many screens you want to watch on at the same time, then how long. Channels and picture quality are the same in every plan.</p></div>
    <!--DEVICES-->
""" + pricing_cards("en", TE) + """
    <div class="measure"><!--PRICETABLE--><p class="ruler-note">For the lowest price per month, twelve months is the right choice. Payment and terms are on the <a href="/en/iptv-subscription-finland/">IPTV subscription Finland page</a>.</p></div>
  </div>
</section>

<section class="sec sec-alt">
  <div class="wrap measure"><div class="sec-head center"><span class="eyebrow">Screens</span><h2>IPTV Finland on the screens you already have</h2>
    <p>An app from the device's own app store is enough, and we tell you which one works best on your model.</p></div><!--IMG:en-home-devices--></div>
  <div class="wrap devs" style="margin-top:28px">
""" + cards([
 ("cyan", "tv", "Samsung and LG Smart TV", "Most models from roughly 2018 and later run it with an app. Send us the model number and we tell you which app."),
 ("green", "box", "Fire TV Stick and Android TV", "The widest choice of apps and often the steadiest picture."),
 ("pink", "phone", "Apple TV, iPhone and iPad", "An IPTV player from the App Store. Apple explains how to install apps on the <a href=\"https://support.apple.com/apple-tv\" target=\"_blank\" rel=\"noopener\">Apple TV support pages</a>."),
 ("amber", "laptop", "MAG box and computer", "A MAG box is linked to your account with its MAC address, and we do that for you. On a computer both VLC and IPTV apps work."),
]) + """
  </div>
</section>

<section class="sec">
  <div class="wrap">
    <div class="sec-head"><span class="eyebrow">Getting started</span><h2>Get started with IPTV Finland in three steps</h2>
      <p>Most people are watching the same evening. What takes time is rarely the app, it is finding the right app for your TV.</p></div>
    <ol class="steps">
      <li><h3>Choose how long</h3><p>All plans have the same content. If you are unsure, start with one month.</p></li>
      <li><h3>Write to us on WhatsApp</h3><p>Tell us the plan and the TV or box you have. We reply with payment details and the right app.</p></li>
      <li><h3>Log in and watch</h3><p>You get the login and a short instruction for your TV. If you get stuck we keep helping in the chat.</p></li>
    </ol>
    <p style="margin-top:28px;text-align:center"><a class="btn" data-track="buy_click" href="{{WA:Hi! I'd like to try Tilaa IPTV for one month (€15.99).}}" rel="noopener" target="_blank">Try one month for €15.99</a></p>
    <div class="measure" style="text-align:center"><!--IMG:en-home-steps--><p>The full walkthrough is in the guide to <a href="/en/install-iptv/">installing IPTV</a>.</p></div>
  </div>
</section>

<section class="sec">
  <div class="wrap">
    <div class="sec-head center"><span class="eyebrow">Comparison</span><h2>IPTV compared with cable TV and streaming</h2><p>IPTV is not right for everyone. This is how IPTV Finland compares with cable TV and streaming services.</p></div>
    <div class="vs-wrap" tabindex="0" role="region" aria-label="Comparison: Tilaa IPTV, cable TV and streaming"><table class="vs"><thead><tr><th scope="col">Feature</th><th scope="col" class="us">Tilaa IPTV</th><th scope="col">Cable TV</th><th scope="col">Streaming</th></tr></thead><tbody>
      <tr><th scope="row">Finnish channels</th><td class="us"><span class="yes">{{I:check}}<span class="sr">Yes</span></span></td><td><span class="yes">{{I:check}}<span class="sr">Yes</span></span></td><td>Partly</td></tr>
      <tr><th scope="row">Live TV with a TV guide</th><td class="us"><span class="yes">{{I:check}}<span class="sr">Yes</span></span></td><td><span class="yes">{{I:check}}<span class="sr">Yes</span></span></td><td>Rarely</td></tr>
      <tr><th scope="row">Price per month</th><td class="us">From €5.83</td><td>Often several tens of euro</td><td>Per service</td></tr>
      <tr><th scope="row">Contract</th><td class="us">None</td><td>Often 12 to 24 months</td><td>None</td></tr>
      <tr><th scope="row">Installation</th><td class="us">One app</td><td>Outlet and box</td><td>One app</td></tr>
      <tr><th scope="row">Support</th><td class="us">WhatsApp, English or Finnish</td><td>Customer service</td><td>Email or chat</td></tr>
    </tbody></table></div>
    <p>If your connection is slow or uneven, cable TV or an aerial is the safer choice. Below 10 Mbit/s to the TV no service is the right IPTV Finland choice for you, however good it is.</p>
  </div>
</section>

<section class="sec sec-alt">
  <div class="wrap measure why">
    <div class="sec-head center"><span class="eyebrow">Why us</span><h2>Why people choose Tilaa IPTV</h2></div>
    <h3>Support on WhatsApp</h3><p>You write to a person, not a form. Send a photo of the screen and we see straight away what is going on.</p>
    <h3>Plain terms</h3><p>No contract, no automatic renewal and prices in euro. IPTV should be as easy to stop as to start. It is all in our <a href="/en/terms/">terms</a>.</p>
    <h3>When we are not the right choice</h3><p>If your connection is under 10 Mbit/s per screen, or you want a box that someone installs at your home, a traditional operator suits you better. It is more honest to say so now than after you have paid.</p>
  </div>
</section>

<section class="sec sec-alt">
  <div class="wrap">
    <div class="sec-head"><span class="eyebrow">Guides</span><h2>Guides from our support team</h2><p>Installation, apps and troubleshooting, written from the questions we get.</p></div>
    <ul class="checks">
      <li>{{I:check}}<span><a href="/en/best-iptv-finland/">Best IPTV in Finland: 7 checks before you subscribe</a></span></li>
      <li>{{I:check}}<span><a href="/en/install-iptv/">Install IPTV on Smart TV, Fire TV and phone</a></span></li>
    </ul>
    <p><a href="/en/guides/">All IPTV guides for Finland</a></p>
  </div>
</section>

<section class="sec">
  <div class="wrap">
    <div class="sec-head"><span class="eyebrow">Questions and answers</span><h2>Common questions about IPTV Finland</h2></div>
""" + faq_html(FAQE) + """
    <p style="margin-top:24px">More answers are on the <a href="/en/faq/">IPTV FAQ page</a>.</p>
  </div>
</section>

<section class="band"><div class="wrap band-in"><div><h2>Try IPTV Finland on your own TV tonight.</h2><p>Tell us which TV you have and we tell you which plan and app suit it.</p></div>
<a class="btn" data-track="buy_click" href="{{WA:Hi! I have a question before I order Tilaa IPTV.}}" rel="noopener" target="_blank">{{I:chat}} Write to us on WhatsApp</a></div></section>
""")

    pf = [("Can I change the number of screens later?", "Yes. Write to us on WhatsApp before your period ends and say how many screens you want next time."),
          ("What happens when the period is over?", "The service stops. Nothing renews automatically, and we do not store your card details. If you want to continue, you order again.")]
    save("en", "iptv-subscription-finland", {"keyword": "iptv subscription finland", "crumb": "IPTV subscription Finland", "alt": "iptv-hinta",
        "title": "IPTV Subscription Finland: 12 Plans from €15.99 | Tilaa IPTV",
        "desc": "IPTV subscription Finland: 1, 3, 6 or 12 months for 1, 2 or 3 screens, from €5.83/month with no contract. All prices on one page.",
        "og": "IPTV subscription Finland: 12 plans from €15.99",
        "tldr": "An IPTV subscription in Finland from Tilaa IPTV costs €15.99 for one month and €69.99 for twelve months on one screen, which is €5.83 a month. Two and three screens cost more. Nothing renews automatically.",
        "schema": [faq_schema(pf)]},
"""
<section class="page-head"><div class="wrap"><span class="eyebrow">Prices</span><h1>IPTV subscription Finland: plans and prices</h1>
<p>One service, four lengths and three screen tiers. Pick how many screens should work at the same time, then how long you want to subscribe.</p></div></section>
<section class="sec sec-tight"><div class="wrap">
<!--TOC-->
<!--DEVICES-->
""" + pricing_cards("en", TE) + """
<div class="measure">
<h2>What an IPTV subscription Finland plan includes</h2>
<p>Every IPTV subscription Finland plan has the same content: Finnish and Nordic channels in HD, 4K where the channel broadcasts it, a TV guide and help with the installation on WhatsApp. Only the length and the number of screens change between plans.</p>
<h2>All prices for 1, 2 and 3 screens</h2>
<!--PRICETABLE-->
<p>A longer plan always gives a lower price per month.</p>
<h2>How to pay for your IPTV subscription</h2>
<p>You order on WhatsApp and get the payment details there. We accept Visa, Mastercard, Maestro, Apple Pay, Google Pay and PayPal, and from other EU countries also SEPA, iDEAL, Bancontact and giropay. We do not store card details and nothing renews on its own.</p>
<h2>Choosing an IPTV subscription Finland households can rely on</h2>
<p>When you compare an IPTV subscription Finland sellers offer, look at the contract, the renewal and the support, not just the channel count. Our IPTV subscription Finland plans have no contract and no automatic renewal. To understand your consumer rights before you buy any digital service, the <a href="https://www.kkv.fi/en/" target="_blank" rel="noopener">Finnish Competition and Consumer Authority</a> has plain-language guides.</p>
<h2>Which plan should you choose?</h2>
<ul><li><strong>Not sure yet:</strong> one month. It does not renew, so there is nothing to cancel.</li><li><strong>Lowest cost per month:</strong> twelve months.</li><li><strong>Several people watching at once:</strong> pick the 2 or 3 screen tier.</li></ul>
<p>Not sure what suits your TV? Read how to <a href="/en/install-iptv/">install IPTV</a> first, check the <a href="/en/best-iptv-finland/">best IPTV checklist</a> or go back to <a href="/en/">IPTV Finland</a>. Terms are in our <a href="/en/terms/">terms of service</a>.</p>
<h2>Questions about plans</h2>
""" + faq_html(pf) + """
</div></div></section>
<section class="band"><div class="wrap band-in"><div><h2>Ready to order?</h2><p>Tell us the plan and the TV you have.</p></div>
<a class="btn" data-track="buy_click" href="{{WA:Hi! I'd like to order Tilaa IPTV.}}" rel="noopener" target="_blank">{{I:chat}} Order on WhatsApp</a></div></section>
""")

    q = [("Which IPTV is best for Finland?", "The best IPTV is the one that has a steady app for your exact TV, the channels you actually watch and a seller who answers questions. Test one month before you commit to a longer plan."),
         ("Should I pick the cheapest plan?", "Not automatically. A low price is only good value if the picture is steady and someone helps when it is not. Compare the contract, the renewal terms and the support, not just the price.")]
    save("en", "best-iptv-finland", {"keyword": "best iptv", "crumb": "Best IPTV in Finland", "alt": "paras-iptv-palvelu",
        "title": "Best IPTV in Finland: 7 Checks Before You Subscribe",
        "desc": "Best IPTV in Finland: seven practical checks for stability, apps, channels, contract and support, so you pick a service that suits your TV and household.",
        "og": "Best IPTV in Finland: 7 checks before you subscribe", "img_alt": "Best IPTV in Finland: seven checks before you subscribe",
        "tldr": "The best IPTV for Finland is the one that runs steadily on your own TV, has the channels you watch, shows a TV guide, has no contract and gives real support. Test one month first and check the seven points on this page.",
        "schema": [faq_schema(q)]},
"""
<section class="page-head"><div class="wrap"><span class="eyebrow">How to choose</span><h1>Best IPTV in Finland: how to choose a service</h1>
<p>There is no single best IPTV for everyone. There is the best IPTV for your TV, your internet and your habits. These are the checks we would make ourselves.</p></div></section>
<section class="sec sec-tight"><div class="wrap"><div class="measure prose">
<!--TOC-->
<p>Search for the best IPTV and you find long lists with big numbers and few facts. This page gives you seven checks you can make in an evening, whichever service you end up with.</p>
<h2>What does the best IPTV mean?</h2>
<p>For most households the best IPTV is boring in the right way. The TV starts when you press the remote, the picture holds on a Saturday night and the guide shows the right programme. Channel counts and big claims say little about that. Stability, apps and support say a lot.</p>
<h2>Seven checks for the best IPTV in Finland</h2>
<ol>
<li><strong>Stability.</strong> Test on your own TV, in the evening, with other people online. One month is a fair test.</li>
<li><strong>An app for your TV.</strong> Ask which app runs on your exact model before you pay. Samsung, LG, Fire TV, Android TV and Apple TV each have their own app stores.</li>
<li><strong>A TV guide (EPG).</strong> It should show what is on now and later, not just a list of channels.</li>
<li><strong>The channels you watch.</strong> Ask about the specific channels, in writing. A line-up can change over time, so a fair seller says so.</li>
<li><strong>No long contract.</strong> A subscription that ends by itself is easier to leave than one you have to cancel.</li>
<li><strong>Real support.</strong> Can you write to a person with a photo of the screen and get an answer? Test it with one question before you buy.</li>
<li><strong>Honesty about rights.</strong> A good seller does not hide what it cannot promise. Be careful with big numbers you cannot check.</li>
</ol>
<h2>How to test the best IPTV before you commit</h2>
<p>Start with the shortest plan. Use it for a week on your normal evenings. Switch channels, open the guide, and watch a live match or a news broadcast. If something stutters, send the seller a photo and see how fast and how clearly they reply. That single reply tells you more than any list.</p>
<h2>Warning signs when you look for the best IPTV</h2>
<ul><li>Round numbers such as "99.9% uptime" or tens of thousands of channels with nothing to back them up.</li><li>No way to reach a person, or no clear terms.</li><li>Pressure to pay for a long plan at once.</li></ul>
<p>The Finnish Competition and Consumer Authority has plain advice on buying digital services in <a href="https://www.kkv.fi/en/" target="_blank" rel="noopener">its guides</a>.</p>
<h2>Where Tilaa IPTV fits</h2>
<p>We try to meet these checks, and you should test us the same way. Plans start at €15.99 for one month, nothing renews automatically and support is on WhatsApp. See the <a href="/en/iptv-subscription-finland/">IPTV subscription Finland plans</a>, read how to <a href="/en/install-iptv/">install IPTV</a> or go back to <a href="/en/">IPTV Finland</a>. The Finnish version of this page is <a href="/paras-iptv-palvelu/" hreflang="fi" lang="fi">Paras IPTV palvelu</a>.</p>
<h2>Questions about the best IPTV</h2>
""" + faq_html(q) + """
</div></div></section>
<section class="band"><div class="wrap band-in"><div><h2>Want to test it yourself?</h2><p>Start with one month and judge it on your own TV.</p></div>
<a class="btn" data-track="buy_click" href="{{WA:Hi! I'd like to try Tilaa IPTV for one month.}}" rel="noopener" target="_blank">{{I:chat}} Write to us on WhatsApp</a></div></section>
""")

    save("en", "install-iptv", {"keyword": "install iptv", "crumb": "Install IPTV", "alt": "iptv-sovellus",
        "title": "Install IPTV in 3 Steps on Smart TV, Fire TV and Phone",
        "desc": "How to install IPTV on Samsung and LG Smart TV, Fire TV Stick, Android TV, Apple TV, iPhone and computer. Steps, speed needs and where to get help.",
        "og": "Install IPTV in 3 steps on Smart TV, Fire TV and phone",
        "tldr": "To install IPTV you pick a plan, get your login on WhatsApp and put an IPTV app on your TV, box or phone. It takes a few minutes if you have 10 Mbit/s per screen and the right app for your model."},
"""
<section class="page-head"><div class="wrap"><span class="eyebrow">Setup</span><h1>Install IPTV: Smart TV, Fire TV, Apple TV and phone</h1>
<p>You do not need special equipment. You need an app for your device, your login and a connection that is fast enough.</p></div></section>
<section class="sec sec-tight"><div class="wrap"><div class="measure prose">
<!--TOC-->
<p>To install IPTV on a TV, a box or a phone you follow the same three steps on every device. The details differ by brand, which is why we ask for your model before we recommend an app.</p>
<h2>Before you install IPTV: check your internet</h2>
<p>Plan for at least 10 Mbit/s per screen for HD and 25 Mbit/s for 4K. Measure on the TV or the box, not on your phone, because the TV is often further from the router. A network cable is almost always steadier than wifi.</p>
<h2>Three steps to install IPTV</h2>
<ol><li><strong>Order and get your login.</strong> Write to us on WhatsApp with the plan you want and your TV or box model.</li><li><strong>Install the app.</strong> Open the app store on your device, install the IPTV player we recommend for your model and open it.</li><li><strong>Log in.</strong> Enter the details we send you. The channel list and the TV guide load within a minute or two.</li></ol>
<h2>Install IPTV on Samsung and LG Smart TV</h2>
<p>Most models from roughly 2018 and later can run an IPTV app from the TV's own app store. Which apps are available depends on the model and year, so send us the model number from the label on the back.</p>
<h2>Install IPTV on Fire TV Stick and Android TV</h2>
<p>These give the widest choice of apps. Open the app store, search for the player we recommend and install it. Amazon explains the basics on its <a href="https://www.amazon.com/gp/help/customer/display.html?nodeId=GYXQJZZ2VAXYW9H9" target="_blank" rel="noopener">Fire TV help pages</a>.</p>
<h2>Install IPTV on Apple TV, iPhone and iPad</h2>
<p>Install an IPTV player from the App Store, then log in with the details we send. Apple's own <a href="https://support.apple.com/apple-tv" target="_blank" rel="noopener">Apple TV support pages</a> cover how to install apps.</p>
<h2>Install IPTV on a MAG box or a computer</h2>
<p>A MAG box is linked to your account with the box's MAC address, and we set that up for you. On a computer you can use VLC or an IPTV app.</p>
<h2>If the picture stutters after you install IPTV</h2>
<p>Move the TV to a network cable, restart the router and close other streaming on the network. If it still stutters, send us a photo of the screen on WhatsApp.</p>
<h2>Tips for a steadier picture</h2>
<p>Place the router in the same room as the TV if you can, and keep it away from thick walls. If you must use wifi, choose the 5 GHz band, which is faster over short distances than 2.4 GHz. Close other apps that stream video while you test, and restart the app once after the first login so the channel list and the guide load cleanly.</p>
<h2>How long the setup takes</h2>
<p>With the right app for your model, most people finish within a few minutes. Finding the right app takes longer than the setup itself, so tell us your model first and we point you to the right one.</p>
<h2>What you need before you start</h2>
<ul><li>Your TV or box model, from the label or the settings menu.</li><li>An internet connection of at least 10 Mbit/s per screen.</li><li>Your login from us on WhatsApp.</li><li>An account in the device's app store.</li></ul>
<p>Ready to start? See the <a href="/en/iptv-subscription-finland/">plans and prices</a>, check the <a href="/en/best-iptv-finland/">best IPTV checklist</a> or go back to <a href="/en/">IPTV Finland</a>.</p>
</div></div></section>
<section class="band"><div class="wrap band-in"><div><h2>Stuck on a step?</h2><p>Send your TV model and we tell you what to do.</p></div>
<a class="btn" data-track="buy_click" href="{{WA:Hi! I need help installing IPTV on my TV.}}" rel="noopener" target="_blank">{{I:chat}} Ask on WhatsApp</a></div></section>
""")

    save("en", "faq", {"crumb": "FAQ", "alt": "ukk", "title": "IPTV Finland FAQ: Questions and Answers | Tilaa IPTV",
        "desc": "Answers about Tilaa IPTV: plans, payment, speed, devices, renewal and legality. Short and straight, written by our support team.", "schema": [faq_schema(FAQE)]},
"""
<section class="page-head"><div class="wrap"><span class="eyebrow">FAQ</span><h1>Frequently asked questions about IPTV</h1><p>The questions we get most often, answered straight.</p></div></section>
<section class="sec sec-tight"><div class="wrap">""" + faq_html(FAQE) + """
<p style="margin-top:24px">Something missing? <a href="/en/contact/">Contact us</a>, see the <a href="/en/iptv-subscription-finland/">plans</a> or go back to <a href="/en/">IPTV Finland</a>.</p></div></section>
""")
    save("en", "about", {"crumb": "About us", "alt": "tietoa-meista", "title": "About Tilaa IPTV: Who Writes the Guides and Why",
        "desc": "About Tilaa IPTV: an independent IPTV service for Finland, how our support team writes the guides and which facts we will and will not claim.",
        "schema": [{"@context": "https://schema.org", "@type": "AboutPage", "name": "About us", "url": BASE + "/en/about/", "inLanguage": "en"}]},
"""
<section class="page-head"><div class="wrap"><span class="eyebrow">About</span><h1>About Tilaa IPTV</h1><p>An independent IPTV service for households in Finland, with support on WhatsApp.</p></div></section>
<section class="sec sec-tight"><div class="wrap"><div class="measure prose">
<p>Tilaa IPTV sells IPTV subscriptions with Finnish and Nordic channels. We have no affiliation with the TV companies, apps or manufacturers mentioned on this site. Ordering, payment and help all happen on WhatsApp.</p>
<h2 id="how-we-write">How we write the guides</h2>
<p>The guides are written by the support team, the same people who answer on WhatsApp. We write about questions customers actually ask. Settings and app features are checked against the manufacturers' own help pages, which we link under each guide, and we correct the text when something changes.</p>
<h2>What we will not claim</h2>
<p>We do not publish invented numbers such as uptime percentages, review scores or channel counts we cannot prove. When we do not know something, we say so. The channel line-up can change over time, so we ask you to check a specific channel with us before you order.</p>
<p>Read our <a href="/en/terms/">terms</a>, <a href="/en/privacy/">privacy policy</a> or go to <a href="/en/contact/">contact</a>.</p>
</div></div></section>
""")
    save("en", "contact", {"crumb": "Contact", "alt": "yhteystiedot", "title": "Contact Tilaa IPTV: WhatsApp and Contact Form",
        "desc": "Contact Tilaa IPTV on WhatsApp for orders, installation and troubleshooting, or use the contact form. What to include in your first message.",
        "schema": [{"@context": "https://schema.org", "@type": "ContactPage", "name": "Contact", "url": BASE + "/en/contact/", "inLanguage": "en"}]},
"""
<section class="page-head"><div class="wrap"><span class="eyebrow">Contact</span><h1>Contact us</h1><p>WhatsApp is fastest, for both ordering and help with the installation. Tell us which TV or box you have, so we can answer the right thing.</p></div></section>
<div class="wrap"><div class="prose">
<p><a class="btn" data-track="buy_click" href="{{WA:Hi! I have a question about Tilaa IPTV.}}" rel="noopener" target="_blank">Write on WhatsApp</a></p>
<div class="table-wrap"><table><tbody><tr><th scope="row">WhatsApp</th><td>""" + SITE["whatsapp_display"] + """</td></tr><tr><th scope="row">Languages</th><td>English and Finnish</td></tr></tbody></table></div>
<h2>Include this in your first message</h2>
<p>For help with the installation, write the brand and model of the TV or box, and send a photo of the screen if an error shows. For an order, write which plan you want. Prices are on the <a href="/en/iptv-subscription-finland/">IPTV subscription Finland page</a>, setup steps are in <a href="/en/install-iptv/">how to install IPTV</a>, and our <a href="/en/terms/">terms</a> explain what applies to an order.</p>
<h2>Prefer a form?</h2><p>Use the contact form at the bottom of the page and we reply to the address you give us.</p>
</div></div>
""")
    save("en", "terms", {"crumb": "Terms", "alt": "ehdot", "title": "Terms of Service for Tilaa IPTV | Plans and Renewal",
        "desc": "Terms of service for Tilaa IPTV: plans, payment, no automatic renewal, support, acceptable use and your rights as a consumer in Finland."},
"""
<section class="page-head"><div class="wrap"><span class="eyebrow">Terms</span><h1>Terms of service</h1><p>Short and plain. Last updated November 2026.</p></div></section>
<div class="wrap"><div class="prose">
<h2>The service</h2><p>Tilaa IPTV sells access to an IPTV service with Finnish and Nordic channels. The channel line-up can change over time. You can ask us about a specific channel on WhatsApp before you order.</p>
<h2>Plans and payment</h2><p>You choose a length (1, 3, 6 or 12 months) and a number of screens (1, 2 or 3). You order and pay through WhatsApp. Prices are shown in euro.</p>
<h2>Renewal</h2><p>Nothing renews automatically. We do not store card details. When the period ends the service stops unless you order again.</p>
<h2>Support and problems</h2><p>If something does not work, write to us on WhatsApp with a photo of the screen and we go through the connection, the app and the settings with you.</p>
<h2>Your rights</h2><p>Your statutory rights as a consumer under Finnish law are not affected by these terms.</p>
<h2>Acceptable use</h2><p>The service is for private use in your household. You are responsible for how you use it and for following the law that applies to you.</p>
<p>Questions? <a href="/en/contact/">Contact us</a>. See also the <a href="/en/privacy/">privacy policy</a> and the <a href="/en/iptv-subscription-finland/">plans</a>.</p>
</div></div>
""")
    save("en", "privacy", {"crumb": "Privacy policy", "alt": "tietosuoja", "title": "Privacy Policy for Tilaa IPTV | What We Store and Why",
        "desc": "Privacy at Tilaa IPTV: what we collect when you order or use the contact form, how long we keep it and how to ask us to delete it."},
"""
<section class="page-head"><div class="wrap"><span class="eyebrow">Privacy</span><h1>Privacy policy</h1><p>What we store and why. Last updated November 2026.</p></div></section>
<div class="wrap"><div class="prose">
<h2>What we collect</h2><p>When you write to us on WhatsApp we see your phone number and the messages you send. When you use the contact form we receive the name, contact details and message you type. We use this only to answer you and deliver your order.</p>
<h2>What we do not do</h2><p>We do not sell your data, we do not store card details and we do not use advertising trackers.</p>
<h2>Statistics</h2><p>If you accept, we count page views and clicks to improve the site. No cookies are used. If you decline, nothing is counted. You can change your choice on the <a href="/en/cookies/">cookies and statistics page</a>.</p>
<h2>Your rights</h2><p>You can ask us to show, correct or delete what we hold about you. Write to us on <a href="/en/contact/">the contact page</a>.</p>
<p>See also our <a href="/en/terms/">terms</a> and the <a href="/en/">home page</a>.</p>
</div></div>
""")
    save("en", "cookies", {"crumb": "Cookies and statistics", "alt": "evasteet", "title": "Cookies and Statistics at Tilaa IPTV | Your Choice",
        "desc": "Tilaa IPTV uses no cookies. Optional statistics count visits and clicks only if you accept. Here is how it works and how to change your choice."},
"""
<section class="page-head"><div class="wrap"><span class="eyebrow">Cookies</span><h1>Cookies and statistics</h1></div></section>
<div class="wrap"><div class="prose">
<p>This site sets no cookies. Optional statistics count page views and clicks to help us improve the site, and they only load if you press Accept. Declining is the default.</p>
<p><button class="btn btn-sm btn-line" type="button" data-consent-reset>Change my choice</button></p>
<p>More in the <a href="/en/privacy/">privacy policy</a>. See also the <a href="/en/terms/">terms</a>, the <a href="/en/">home page</a> and <a href="/en/contact/">contact</a>.</p>
</div></div>
""")
    save("en", "404", {"crumb": "Not found", "robots": "noindex, follow", "title": "Page not found | Tilaa IPTV", "desc": "This page does not exist. Go back to the home page or see the IPTV plans."},
"""
<section class="page-head"><div class="wrap"><h1>Page not found</h1><p>The page you are looking for does not exist. Go to the <a href="/en/">home page</a> or see the <a href="/en/iptv-subscription-finland/">plans</a>.</p></div></section>
""")

if __name__ == "__main__":
    pages_en(); print("EN pages written")
