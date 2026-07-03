# Design and Conversion Build Plan - 2026-07-02

For Sonnet to execute. Derived from the live design/conversion audit (Claude in Chrome) plus a corrected repository broken-link scan. Fixes are grounded in verified repo facts, not just the audit report.

## How to use this file

- Work top to bottom: Block 0 (critical bugs) first, then conversion, then polish, then the big consolidation.
- Every item names the file(s) to change and the specific fix. After the decisions were resolved (see "Decisions resolved" below), every item is **[SONNET]**.
- Verify every change with a real Hugo build. Hugo is not installed by default; install the pinned version via the Go proxy: `GOBIN=/tmp/gobin go install github.com/gohugoio/hugo@v0.160.1` then build with `/tmp/gobin/hugo --gc --minify --destination /tmp/out`.
- **Broken-link verification must handle minified HTML.** The minifier drops quotes around `href` values, so a regex like `href="(/...)"` matches nothing and gives a false "zero broken" result (this exact mistake was made earlier). Use `href=(?:"([^"#?]*)"|([^\s">#?]+))` and check each internal path against the set of built directories.
- Follow CLAUDE.md: no em dashes, British English, correct personas, no bulk-generation scripts (data/template normalisation is fine).
- Decisions for Gareth are collected at the foot under "Decisions needed". Ask them before doing the dependent item.

## Honest note on how this arose

A previous fix (SB4) changed the header origin links to plain slugs (`/origins/united-kingdom/`) and a broken-link check reported "zero broken". That check was faulty (the minified-href regex above), and the plain slugs do not exist. The real origin pages build to slugs like `pet-export-guide-shipping-from-united-kingdom`. So SB4 introduced 4 broken links on every page. D1 fixes this correctly and re-verifies with the corrected method.

---

## Block 0 - Critical bugs (fix first)

### D1 [SONNET] Broken internal links: 549 distinct, 42,232 instances
The corrected scan (against a fresh build) found 549 distinct broken internal targets. Categories and fixes:

1. **Header origin links (4 targets, ~6,897 instances each).** `site/layouts/partials/header.html` links to `/pet-transport/origins/{united-kingdom,united-states,australia,united-arab-emirates}/`, which 404. The real built slugs are:
   - `/pet-transport/origins/pet-export-guide-shipping-from-united-kingdom/`
   - `/pet-transport/origins/pet-export-guide-shipping-from-united-states/`
   - `/pet-transport/origins/pet-export-guide-shipping-from-australia/`
   - `/pet-transport/origins/united-arab-emirates-pet-export-guide/`  (note: different pattern from the other three)
   Fix the four hrefs to these. Confirm each builds. (This reverses the faulty SB4 change with the correct targets.)

2. **Airline links (468 distinct targets).** `site/layouts/partials/airline-breed-sidebar.html` (and `route-c-comparison.html`, `route-e-data.html`) build airline links by slugifying the airline NAME from route data (for example "KLM" to `klm`, "Emirates SkyCargo" to `emirates-skycargo`, "Lufthansa Cargo via FRA" to `lufthansa-cargo-via-fra`). Those slugs do not match the real airline page slugs (`klm-royal-dutch-airlines`, `emirates`, etc.), so ~468 distinct links 404 across tens of thousands of instances. Fix: only render the link when the target page exists, otherwise render the airline name as plain text. Use the same guard already used for upward links in `route-new-na.html`: `{{ if site.GetPage (printf "/pet-transport/airlines/%s" $slug) }}<a ...>{{ else }}<span>{{ end }}`. Apply in every template that links airlines.

3. **Breed links (15 distinct targets).** Same pattern: route templates (`route-new-na.html`, `route-b-journey.html`, `route-e-data.html`, `route-a-fieldmanual.html`, `route-legacy.html`) and `airline-breed-sidebar.html` link breed-restriction names (for example "Rottweiler (restricted)" to `rottweiler-restricted`) that have no breed page. Apply the same `site.GetPage` existence guard before linking a breed; otherwise plain text.

4. **Footer cost-calculator link (1 target, every page).** `site/layouts/partials/footer.html` links `/pet-transport/resources/pet-transport-cost-calculator/`, which does not exist. Decision D-a: remove the link, or build the page. Default: remove it.

5. **Remaining "other" (61 distinct).** After the above, re-run the corrected scan and fix or filter whatever remains (likely more slugified data links). Target: zero broken internal links, verified with the minify-aware scan.

Decision this raises: D-a (footer cost calculator: remove vs build). Model: Sonnet OK.

### D2 [SONNET] Static-page H1 shows the raw SEO title
`site/layouts/_default/single.html` renders `<h1>{{ .Title }}</h1>`, and `.Title` on the static pages is the full SEO title including the brand/keyword suffix (for example the About page H1 reads "About PetTransportGlobal | International Pet Relocation Specialists"). It looks like a leaked title tag. Fix: render a clean H1, either by stripping everything from the first " | " onward, or by adding an `h1:` front-matter field to about/contact/privacy/terms/methodology and using `{{ .Params.h1 | default .Title }}`. The `<title>` tag itself is correct and should stay. Affects about, contact, privacy, terms, and the methodology page (`pet-transport/how-we-source-route-data.md`). Model: Sonnet OK.

### D3 [SONNET] Contact page points to a non-existent email
`site/content/contact.md` tells visitors to "email us directly at the address in the site footer", but there is no email anywhere (WhatsApp and the quote form are the only channels, per Gareth). Fix the copy to direct visitors to the quote form and WhatsApp. Model: Sonnet OK.

### D4 [SONNET, after decision] Home quote form covers only ~12 countries
`site/layouts/index.html` builds the "Moving from" and "Moving to" selects with `{{ range hugo.Data.countries }}`, and `data/countries.*` holds only about 12 countries. Visitors from most countries the site actually serves cannot select their origin, which silently disqualifies them. Decision D-b: expand `data/countries` to every served country (simplest), or replace the two selects with a free-text/autocomplete input. Default: expand the data file to all served countries. Model: Sonnet OK.

---

## Block 1 - Conversion (CTA, form, WhatsApp placement)

The audit found CTA placement varies wildly by template and is weakest on route variant A. Strongest patterns to copy: the blog sidebar (quote card + WhatsApp card) and route variant E's sticky stat sub-bar.

### D5 [SONNET] Route variant A: no above-fold CTA, form buried at the bottom
`route-new-na.html`. The quote form is the last element before the footer; there is no CTA above the fold. Add an amber "Get a free quote" button in/under the hero stats, and move or duplicate the quote form to directly below the quick-answer capsule (high on the page). Add a mid-page CTA after the requirements table. Model: Sonnet OK.

### D6 [SONNET] Route variant C: hero CTA is a weak text link
`route-new-nc.html`. The hero "Get your free quote" is a small underlined text link. Replace with a proper amber button. Model: Sonnet OK.

### D7 [SONNET] Apply the blog sidebar CTA pattern to guide pages
The blog template's right sidebar (a "Moving your pet abroad?" quote card plus a "Chat on WhatsApp" card) is the best CTA setup on the site and the only place a WhatsApp CTA appears outside the float. Add the same pair of sidebar cards to `countries/single.html`, `airlines/single.html`, `breeds/single.html`, `origins/single.html`. Model: Sonnet OK.

### D8 [SONNET] Add route variant E's sticky stat sub-bar to the other route templates
Variant E (`route-new-ne.html`) has a sticky sub-bar (Lead time, Quarantine, Complexity, Airlines + "Start my quote" amber button) that is the strongest above-fold conversion mechanic. Extract it into a shared partial and include it in na/nb/nc/nd/nl. The data is already in every route hero. (If D20 consolidation is chosen, this folds into that instead.) Model: Sonnet OK.

### D9 [SONNET] WhatsApp float overlaps the quote-form submit button
On some widths the fixed WhatsApp circle (bottom-right) sits over the amber submit button. Adjust the float's position/z-index, or add bottom padding to the form area, so they never overlap. Affects the WhatsApp float (baseof) and route forms. Verify at 390px and mid widths. Model: Sonnet OK.

### D10 [SONNET] Add a mid-page CTA at the high-intent moment on guides
Country, airline, and breed guides have no CTA between the hero and the bottom form. Add an amber CTA block immediately after the key information (import requirements on country pages; airline restriction list on airline/breed pages). For brachycephalic breed pages especially, a reassurance CTA ("We specialise in snub-nosed breed transport") after the airline-ban list. Model: Sonnet OK.

---

## Block 2 - Visual polish

### D11 [SONNET, maybe decision] Missing hero images on airline and breed single pages
`airlines/single.html` and `breeds/single.html` render a dark header band with no background image, unlike route/country pages. Add a hero background image. Decision D-c: use an existing generic image from `static/images/` for all, or map per-airline/per-breed images if available. Default: one good generic hero per section. Model: Sonnet OK.

### D12 [SONNET] Blog markdown tables are unstyled
`blog/single.html` (`.ptg-blog-body .Content`). Markdown tables (cost tables in cost articles) render as unstyled run-on text. Add table CSS (borders, padding, zebra striping, responsive `overflow-x:auto` wrapper) scoped to the blog body. Model: Sonnet OK.

### D13 [SONNET] Methodology page is unstyled prose
`pet-transport/how-we-source-route-data.md` renders via `_default/single.html` with no hero and (after D2) a bare H1. It is the site's strongest trust page. Give it a branded header section and a CTA. Consider a dedicated layout or reuse the country-guide header treatment. Model: Sonnet OK.

### D14 [SONNET] Breadcrumb styling differs across route variants
Each route variant styles the hero breadcrumb differently (amber bar full width, centred, flush-left, etc.), and the full-width amber bar leaves an empty expanse on the right. Standardise into one breadcrumb component/style used by all route templates. (Folds into D20 if consolidating.) Model: Sonnet OK.

### D15 [SONNET] Inconsistent form label case
Sidebar forms in variants D/E/fallback use cold ALL-CAPS labels (PET TYPE, EMAIL); other templates use sentence case. Standardise to sentence case sitewide (`quote-form.html` and any variant-specific form markup). Model: Sonnet OK.

### D16 [SKIPPED per decision D-d] About page imagery/social proof
Gareth chose no additions to the About page. Do not change it.

### D17 [SONNET] Search page is sparse
`_default/search.html`. Add brief helper text and a set of popular-route/guide links below the search box so the page is useful before a query. Model: Sonnet OK.

### D18 [SONNET] Verify index card images
The audit reported blank card thumbnails on the routes/airlines/breeds/blog indexes, but the referenced image files DO exist in `static/images/`. Likely a lazy-load or screenshot-timing artifact, or those indexes use a different code path than `_default/list.html`. Verify in a real build whether the `<img>` renders; only fix if genuinely broken. Model: Sonnet OK.

### D19 [SONNET, decision] Thank-you page tone
`site/content/thank-you.md`. The "within the hour" response promise (decision D-e: keep, soften, or remove) and the dark departure-board footer image (swap for something reassuring). Model: Sonnet OK.

---

## Block 3 - Standardise the six route designs

### D20 [SONNET] Standardise shared components across the six route designs (keep all six)
Decision D-f: keep the six designs, do not consolidate. Goal: a visitor moving between route pages should feel they are on one brand even though the layouts differ. Build these as SHARED partials used by all six route templates (na/nb/nc/nd/ne/nl), replacing each template's bespoke version:

1. **Breadcrumb:** one shared breadcrumb partial with one consistent style (fix the full-width amber bar that leaves an empty right expanse). Absorbs D14.
2. **Primary CTA button:** one amber "Get a free quote" button component, same style and label in the hero of every variant. Fixes the weak text-link CTA on variant C (D6) and the missing hero CTA on variant A (D5).
3. **Sticky stat sub-bar:** extract variant E's sub-bar (Lead time, Quarantine, Complexity, Airlines + quote button) into a shared partial included in all six. Absorbs D8.
4. **Form label case:** one form style with sentence-case labels everywhere. Absorbs D15.
5. **WhatsApp + quote sidebar cards:** the blog sidebar pattern (D7) as a shared partial used on route and guide pages.

This is mechanical component extraction plus consistent styling: Sonnet, but do it variant by variant with a build check after each, verifying desktop and 390px. Absorbs D5, D6, D8, D14, D15.

---

## Decisions resolved (2026-07-02, by Gareth)

- **D-a (D1):** Remove the footer "Cost Calculator" link. No calculator page.
- **D-b (D4):** Expand the country data file to all served countries (no autocomplete).
- **D-c (D11):** One generic hero image per section (one for all airline pages, one for all breed pages), from the existing image library.
- **D-d (D16):** No additions to the About page. Skip D16 entirely.
- **D-e (D19):** Soften the thank-you promise to "within one business day".
- **D-f (D20):** Keep the six route designs; do NOT consolidate. Instead standardise the shared components across all six so they feel like one brand. This makes D20 a Sonnet task (no Opus needed) and absorbs D8 and D14.

## Priority order for execution

1. **D1** (broken links, 42k instances - biggest SEO/UX bug, includes reversing the SB4 error) - do first.
2. **D2, D3, D4** (title leak, fake email, home form) - quick critical fixes.
3. **D9** (WhatsApp overlap) and **D5, D6** (worst CTA placements) - fast conversion wins.
4. **D7, D8, D10** (CTA patterns sitewide).
5. **D11-D19** (visual polish), with D18 verify-only.
6. **D20** (standardise shared route components: breadcrumb, CTA, sub-bar, labels, sidebar cards) - absorbs D5, D6, D8, D14, D15.

Note: D16 (About page) is skipped per decision D-d.

## Model summary

Every item is **SONNET** (no Opus needed after decision D-f to standardise rather than consolidate the route designs). D20 remains the largest item; do it carefully, variant by variant, with a build check after each.

No em dashes were used in this document.
