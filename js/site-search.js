/*
  Pet Transport Global - client-side site search.
  Loads /index.json (built by layouts/_default/index.json) and searches it in the
  browser. No external library. Powers the /search/ page; the header box just does
  a GET to /search/?q=... so this file only loads on the search page.
*/
(function () {
  "use strict";

  var MAX_RESULTS = 60;

  // Short-code aliases so common abbreviations match full country names.
  var ALIASES = {
    uk: "united kingdom", gb: "united kingdom", britain: "united kingdom",
    usa: "united states", us: "united states", america: "united states",
    uae: "united arab emirates", emirates: "united arab emirates",
    nz: "new zealand", roi: "ireland", hk: "hong kong", sa: "south africa",
    ksa: "saudi arabia"
  };
  var STOPWORDS = { to: 1, from: 1, the: 1, a: 1, an: 1, of: 1, for: 1, and: 1, my: 1, with: 1, "in": 1 };
  var TYPE_LABELS = {
    routes: "Route", countries: "Country guide", origins: "Origin guide",
    airlines: "Airline", breeds: "Breed guide", blog: "Article", resources: "Resource"
  };

  function tokenize(q) {
    return String(q || "").toLowerCase().split(/[^a-z0-9]+/).filter(function (t) {
      return t && !STOPWORDS[t];
    });
  }

  // Each token matches if the haystack contains the token or any alias phrase.
  function tokenVariants(tok) {
    var v = [tok];
    if (ALIASES[tok]) v.push(ALIASES[tok]);
    return v;
  }

  function scoreEntry(entry, tokens) {
    var title = (entry.t || "").toLowerCase();
    var keys = (entry.k || "").toLowerCase();
    var hay = title + " " + keys + " " + (entry.s || "") + " " + (entry.d || "").toLowerCase();
    var score = 0;
    for (var i = 0; i < tokens.length; i++) {
      var variants = tokenVariants(tokens[i]);
      var matched = false, weight = 1;
      for (var j = 0; j < variants.length; j++) {
        var vv = variants[j];
        if (title.indexOf(vv) !== -1) { matched = true; weight = Math.max(weight, 3); }
        else if (keys.indexOf(vv) !== -1) { matched = true; weight = Math.max(weight, 2); }
        else if (hay.indexOf(vv) !== -1) { matched = true; }
      }
      if (!matched) return 0; // AND: every token must appear
      score += weight;
    }
    return score;
  }

  // Pure: given an index and a query, return ranked entries (used by UI and tests).
  function search(index, query, limit) {
    var tokens = tokenize(query);
    if (!tokens.length || !index) return [];
    var scored = [];
    for (var i = 0; i < index.length; i++) {
      var s = scoreEntry(index[i], tokens);
      if (s > 0) scored.push({ e: index[i], s: s });
    }
    scored.sort(function (a, b) {
      if (b.s !== a.s) return b.s - a.s;
      return (a.e.t || "").localeCompare(b.e.t || "");
    });
    var out = scored.map(function (x) { return x.e; });
    return typeof limit === "number" ? out.slice(0, limit) : out;
  }

  function escapeHtml(s) {
    return String(s || "").replace(/[&<>"']/g, function (c) {
      return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c];
    });
  }

  // ---- Browser wiring (skipped under Node/tests) ----
  if (typeof document !== "undefined") {
    var input = document.getElementById("ptg-search-input");
    var statusEl = document.getElementById("ptg-search-status");
    var resultsEl = document.getElementById("ptg-search-results");
    var form = document.getElementById("ptg-search-form");
    var popularEl = document.getElementById("ptg-search-popular");

    if (input && resultsEl) {
      var INDEX = null;

      var getQueryParam = function () {
        var m = window.location.search.match(/[?&]q=([^&]*)/);
        return m ? decodeURIComponent(m[1].replace(/\+/g, " ")) : "";
      };

      var render = function (query) {
        var tokens = tokenize(query);
        if (popularEl) { popularEl.style.display = tokens.length ? "none" : ""; }
        if (!tokens.length) {
          resultsEl.innerHTML = "";
          statusEl.textContent = INDEX ? "Type above to search " + INDEX.length + " pages." : "";
          return;
        }
        if (!INDEX) { statusEl.textContent = "Loading search index..."; return; }

        var matches = search(INDEX, query);
        var total = matches.length;
        if (!total) {
          resultsEl.innerHTML = '<li class="ptg-search-empty">No results for "' + escapeHtml(query) +
            '". Try a country name, a route like "UK to Spain", or an airline.</li>';
          statusEl.textContent = "0 results";
          return;
        }

        var shown = matches.slice(0, MAX_RESULTS);
        var html = "";
        for (var k = 0; k < shown.length; k++) {
          var e = shown[k];
          var label = TYPE_LABELS[e.s] || "Page";
          html += '<li class="ptg-result">' +
            '<a href="' + escapeHtml(e.u) + '">' + escapeHtml(e.t) + "</a>" +
            '<span class="ptg-result-type">' + escapeHtml(label) + "</span>" +
            (e.d ? '<p class="ptg-result-desc">' + escapeHtml(e.d) + "</p>" : "") +
            "</li>";
        }
        resultsEl.innerHTML = html;
        statusEl.textContent = total > MAX_RESULTS
          ? "Showing " + MAX_RESULTS + " of " + total + " results. Refine your search to narrow it down."
          : total + (total === 1 ? " result" : " results");
      };

      var debounceTimer = null;
      var onInput = function () {
        clearTimeout(debounceTimer);
        var q = input.value;
        debounceTimer = setTimeout(function () {
          if (window.history && window.history.replaceState) {
            window.history.replaceState(null, "", "/search/" + (q ? "?q=" + encodeURIComponent(q) : ""));
          }
          render(q);
        }, 180);
      };

      input.addEventListener("input", onInput);
      if (form) {
        form.addEventListener("submit", function (ev) {
          ev.preventDefault();
          clearTimeout(debounceTimer);
          render(input.value);
        });
      }

      statusEl.textContent = "Loading search index...";
      fetch("/index.json")
        .then(function (r) { return r.json(); })
        .then(function (data) {
          INDEX = data;
          var q = getQueryParam();
          if (q) { input.value = q; }
          input.focus();
          render(input.value);
        })
        .catch(function () {
          statusEl.textContent = "Search is unavailable right now. Please use the menu to browse.";
        });
    }
  }

  // ---- Test export (ignored by browsers) ----
  if (typeof module !== "undefined" && module.exports) {
    module.exports = { tokenize: tokenize, scoreEntry: scoreEntry, search: search, ALIASES: ALIASES };
  }
})();
