/* IPTV Norway One: theme toggle, statistics consent, pricing ruler reveal. No dependencies. */
(function () {
  var root = document.documentElement;
  function store(k, v) { try { v === undefined ? localStorage.removeItem(k) : localStorage.setItem(k, v); } catch (e) {} }
  function read(k) { try { return localStorage.getItem(k); } catch (e) { return null; } }

  // light / dark: dark by default, the visitor can switch
  var toggle = document.querySelector("[data-theme-toggle]");
  if (toggle) toggle.addEventListener("click", function () {
    root.dataset.theme = root.dataset.theme === "light" ? "dark" : "light";  // dark is the default brand look
    store("theme", root.dataset.theme);
  });

  // statistics only load after "Accept"; declining is the default
  function loadStats() {
    var s = document.createElement("script");
    s.src = "https://admin-hub.eddinesalah2007.workers.dev/track.js";
    s.setAttribute("data-site", root.dataset.site || "iptvnorwayone");
    document.body.appendChild(s);
  }
  var box = document.querySelector("[data-consent]");
  var choice = read("stats-consent");
  if (choice === "yes") loadStats();
  else if (choice !== "no" && box) box.hidden = false;
  if (box) box.addEventListener("click", function (e) {
    var b = e.target.closest("[data-consent-choice]");
    if (!b) return;
    store("stats-consent", b.dataset.consentChoice);
    box.hidden = true;
    if (b.dataset.consentChoice === "yes") loadStats();
  });
  var reset = document.querySelector("[data-consent-reset]");
  if (reset) reset.addEventListener("click", function () { store("stats-consent"); if (box) box.hidden = false; });

  // grow the pricing bars when the ruler scrolls into view
  var ruler = document.querySelector("[data-ruler]");
  if (ruler) {
    if (!("IntersectionObserver" in window)) ruler.classList.add("in");
    else new IntersectionObserver(function (e, o) {
      if (e[0].isIntersecting) { ruler.classList.add("in"); o.disconnect(); }
    }, { threshold: 0.3 }).observe(ruler);
  }
  // contact form: load it for everyone (it sends nothing until submitted, unlike the statistics)
  var lead = document.createElement("script");
  lead.src = "https://admin-hub.eddinesalah2007.workers.dev/form.js";
  lead.async = true;
  lead.setAttribute("data-site", root.dataset.site || "iptvnorwayone");
  document.head.appendChild(lead);

  // floating "Write to us": jump to the form above the footer, hide it while the form is on screen
  var jump = document.querySelector("[data-form-jump]");
  if (jump) {
    var watched = false;
    var watch = function () {
      var host = document.getElementById("ah-lead");
      if (!host || watched || !("IntersectionObserver" in window)) return;
      watched = true;
      new IntersectionObserver(function (e) { jump.classList.toggle("away", e[0].isIntersecting); }, { threshold: 0.2 }).observe(host);
    };
    var poll = setInterval(function () { watch(); if (watched) clearInterval(poll); }, 500);
    setTimeout(function () { clearInterval(poll); }, 15000);
    jump.addEventListener("click", function (e) {
      var host = document.getElementById("ah-lead");
      if (!host) return;                       // form not loaded: fall back to the contact page
      e.preventDefault();
      var still = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
      host.scrollIntoView({ behavior: still ? "auto" : "smooth", block: "start" });
      var first = (host.shadowRoot || host).querySelector("input, textarea");
      if (first) setTimeout(function () { first.focus({ preventScroll: true }); }, still ? 0 : 600);
    });
  }

  // device picker: swap prices, price per month, the other-currency hint and the WhatsApp order text for 1, 2 or 3 screens
  var priceData = document.getElementById("prices");
  if (priceData) {
    var cfg = JSON.parse(priceData.textContent), prices = cfg.prices, months = cfg.mon;
    var radios = document.querySelectorAll("[data-dev]");
    var each = function (sel, fn) { Array.prototype.forEach.call(document.querySelectorAll(sel), fn); };
    var setDev = function (d) {
      var row = prices[d], unit = " " + (d === "1" ? cfg.one : cfg.many);
      each("[data-pp]", function (el) { el.textContent = row[el.dataset.pp].p; });
      each("[data-pm]", function (el) { el.textContent = row[el.dataset.pm].pm; });
      each("[data-ps]", function (el) { el.textContent = row[el.dataset.ps].s; });
      each("[data-pwa]", function (a) {
        var m = a.dataset.pwa, u = new URL(a.href), fill = function (t) { return t.replace("{m}", months[m]).replace("{d}", d + unit).replace("{p}", row[m].pt); };
        u.searchParams.set("text", fill(cfg.order));
        a.href = u.toString();
        a.setAttribute("aria-label", fill(cfg.aria));
      });
      Array.prototype.forEach.call(radios, function (b) {
        var on = b.dataset.dev === d;
        b.setAttribute("aria-checked", on); b.tabIndex = on ? 0 : -1;
      });
    };
    Array.prototype.forEach.call(radios, function (b, i) {
      b.addEventListener("click", function () { setDev(b.dataset.dev); });
      b.addEventListener("keydown", function (e) {      // arrow keys move within the radio group
        var step = e.key === "ArrowRight" || e.key === "ArrowDown" ? 1 : e.key === "ArrowLeft" || e.key === "ArrowUp" ? -1 : 0;
        if (!step) return;
        e.preventDefault();
        var next = radios[(i + step + radios.length) % radios.length];
        setDev(next.dataset.dev); next.focus();
      });
    });
  }
})();
