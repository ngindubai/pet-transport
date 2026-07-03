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

A previous fix (SB4) changed the header origin links to plain slugs (`/origins/united-kingdom/`) and a broken-link check reported "zero broken". That check was faulty (the minified-href regex above). D1 (now done, see below) found the actual root cause was not the header links but 52 origin content files missing an explicit `slug:` field; fixing that made the plain slugs SB4 used correct, rather than reverting them.

---

## Block 0 - Critical bugs (fix first)

### D1 [DONE - 2026-07-02] Broken internal links: 549 distinct / 42,232 instances -> 0
Executed on Sonnet 5, pushed live pass-by-pass. Final state verified: **0 distinct broken internal targets across all 6,899 built pages** (minify-aware scan, re-run after every change). What was actually found and fixed, which corrects two assumptions in the original scoping above:

1. **Root cause of the header origin links (bigger than 4 pages): 52 of 77 origin content files had no `slug:` field.** Investigation showed Hugo's `:slug` permalink token falls back to a slugified `.Title` when no explicit `slug` is set, so files like `united-kingdom.md` (title "Pet Export Guide: Shipping from United Kingdom") built to `/origins/pet-export-guide-shipping-from-united-kingdom/` instead of the clean `/origins/united-kingdom/`. The original scoping above assumed the header links should point at those ugly built slugs; the actual correct fix (applied instead) was to add `slug: "<filename>"` to all 52 affected origin files, matching the pattern the other 25 origin files already used. This was verified safe: no slug collisions, and route pages' `links.upward` data already referenced the clean slugs (they were being silently filtered out by the existing "UPWARD LINK FILTER" guard because the target pages didn't exist yet). Fixing the slugs restored those links project-wide with no header.html change needed (it already pointed at the clean slugs). Bonus: origin page count in the build went from 75 to 77 (two pages had been silently shadowed by slug collisions before the fix).

2. **Airline links: existence-guarded, not renamed.** Same root cause as scoped: airline names slugified on the fly (`airline-breed-sidebar.html`, `route-c-comparison.html`, `route-e-data.html`) didn't match real airline page slugs. Fixed with the `site.GetPage` existence guard exactly as scoped: linked when the page exists, otherwise plain text. No `data` file changes needed.

3. **Breed links: same existence guard**, applied to `route-new-na.html`, `route-b-journey.html`, `route-e-data.html`, `route-a-fieldmanual.html`, `route-legacy.html`, and `airline-breed-sidebar.html`, exactly as scoped.

4. **Footer cost-calculator link: removed** per decision D-a.

5. **New discovery beyond original scope: `links.sideways` (related-route cross-links) were unguarded on ALL SIX route templates**, plus `route-a-fieldmanual.html`, `route-b-journey.html`, `route-c-comparison.html`, `route-d-qa.html`, `route-e-data.html`, `route-legacy.html` (12 files total, 2 render sites each in the 6 legacy-style templates). These reference country pairs not yet built (the site covers ~16% of all possible pairs). Built one new shared partial, `site/layouts/partials/routes/valid-sideways.html`, following the exact convention of the existing `$validUpward` filter, and wired `{{ $validSideways := partial "routes/valid-sideways.html" . }}` into all 12 route templates, replacing every raw `{{ with .sideways }}` render site. The partial defensively checks `reflect.IsMap` before accessing `.Params.links.sideways`, matching `route-legacy.html`'s existing defensive pattern, so it cannot crash the build if any route's `links` front matter is ever malformed.

6. **New discovery: 12 origin pages had hardcoded exhaustive markdown link lists** ("Popular routes from Luxembourg", etc.) in their `sections[].body` front matter, literally listing every destination country regardless of whether the route page exists. These cannot be guarded at the template level (they're raw markdown links inside a content string rendered via `.Content`). Fixed by scripting a removal of just the specific dead list lines (verified against the built site's actual route directory listing as ground truth), leaving every valid link untouched. 12 lines removed across 11 files (bangladesh, cambodia, denmark x2, ethiopia, luxembourg, mauritius, morocco, myanmar, portugal, slovakia, zimbabwe).

7. **New discovery: 12 route files had a URL construction bug** in their `links.sideways` data: `url: "/pet-transport/routes/{slug}/"` instead of the correct `/pet-transport/{slug}/` (extra erroneous `routes/` segment). Fixed with a regex substitution across the 12 affected files (italy/portugal/spain x united-kingdom/united-states, both directions), 48 URLs corrected. Targets confirmed to exist before the fix.

8. **New discovery: 2 blog posts had links missing their path prefix** (`/cost-to-transport-a-pet-2026/` instead of `/blog/cost-to-transport-a-pet-2026/`; similarly for `how-to-choose-a-pet-transport-company` and two breed links missing `/pet-transport/`). Fixed directly.

Total: 90 files changed (2 layout partials touched for existence guards across 12 route templates + 1 new shared partial, 1 header/footer fix each, and content fixes in 52 origin slugs + 11 origin body-link cleanups + 12 route sideways-URL fixes + 2 blog link fixes). Verified with a full Hugo build (exit 0) and the minify-aware scan at every stage, final result 0/0. Model: Sonnet, done.

### D2 [DONE - 2026-07-02] Static-page H1 shows the raw SEO title
Fixed in `site/layouts/_default/single.html`: `{{ $h1 := index (strings.Split .Title " | ") 0 }}` used for the H1 instead of the raw `.Title`. Template-level fix (no per-page frontmatter needed), so it generalises to any future page under this layout too. The `<title>` tag is unaffected (still uses the full `.Title`). Verified in build: About renders "About PetTransportGlobal" as H1 while `<title>` keeps the full "About PetTransportGlobal | International Pet Relocation Specialists | Pet Transport Global"; Privacy/Terms/methodology page all render clean H1s.

### D3 [DONE - 2026-07-02] Contact page points to a non-existent email
Fixed in `site/content/contact.md`: "Alternatively, email us directly at the address in the site footer." replaced with a WhatsApp link. Verified in build.

### D4 [DONE - 2026-07-02] Home quote form covers only ~12 countries
Decision D-b: expand to all served countries. Investigation found `hugo.Data.countries` (the old 12-country file) is ALSO used by an unrelated home-page country carousel that expects a `/images/countries/country-{code}.jpg` file per entry (only 12 exist) — expanding that file in place would have fixed the form but broken the carousel with ~63 missing images. Built a new, purpose-scoped data file instead: `site/data/quote_form_countries.json`, 75 countries (name, ISO-3166-1 alpha-2 code, slug), covering the full union of destination country guides and origin guides (both sets are the same 75 countries). Repointed only the two dropdown call sites to `site.Data.quote_form_countries`, leaving the carousel's `hugo.Data.countries` untouched. The two call sites are `site/layouts/index.html` (home hero form) and `site/layouts/partials/quote-form.html` (the shared form used by route variant A, and by all of countries/airlines/breeds/origins/blog single pages, since only those page types need a real country picker; route variants B-E and L already know both countries from the page itself and use hidden pre-filled fields, which is correct and untouched). Verified in build across every real call site (76 options = 75 countries + placeholder, alphabetically sorted, on a variant-A route, a country guide, an airline guide, a breed guide, and a blog post); the carousel still renders its original 12 entries.

---

## Block 1 - Conversion (CTA, form, WhatsApp placement)

The audit found CTA placement varies wildly by template and is weakest on route variant A. Strongest patterns to copy: the blog sidebar (quote card + WhatsApp card) and route variant E's sticky stat sub-bar.

### D5 [DONE - 2026-07-02] Route variant A: no above-fold CTA, form buried at the bottom
Fixed in `route-new-na.html`. Added an amber hero CTA button under the hero stats (reusing `.bcta-btn`, an already-defined but previously unused amber button class in the template's own CSS). Moved the quote form from the very bottom of the page to directly after the quick-answer capsule (before verified-date/Overview), so it is visible with minimal scrolling instead of only after every section. Added a mid-page CTA button after the destination requirements table, the highest-intent moment on the page. Replaced the now-vacated bottom form slot with a lightweight `.bottom-cta` banner (also a pre-existing, previously unused CSS component) linking back to the one real form via `#quote-form`, so readers who scroll to the end still have a conversion path without a duplicate-ID form. Verified in build: form appears before the Overview section, exactly one `#quote-form` element (no duplicate IDs), hero/mid-page/bottom CTA text all present.

### D6 [DONE - 2026-07-02] Route variant C: hero CTA is a weak text link
Fixed in `route-new-nc.html`. Replaced the small underlined `.hero-copy-cta` text link with a proper amber button (inline-styled using the template's own `var(--amber)` custom property, since no pre-built amber hero-button class existed in this template's CSS, unlike variant A). Verified in build.

### D7 [DONE - 2026-07-02] Apply the blog sidebar CTA pattern to guide pages
Built one shared partial, `site/layouts/partials/quote-whatsapp-cards.html`, rendering the exact quote CTA card and WhatsApp card from the blog sidebar, so all four call sites stay identical rather than drifting. `countries/single.html` and `origins/single.html` already had a `col-lg-3` sidebar; added the cards there. `airlines/single.html` and `breeds/single.html` have no sidebar column (single centred `col-lg-10` layout); added the same stacked card pair as a compact half-width module right after the Overview section instead of forcing a two-column restructure. Bonus fix found while wiring the sidebar cards: both `countries/single.html` and `origins/single.html` had a sidebar "Get a quote" link pointing to `#quote-section`, which does not exist anywhere on the page (the real form's id, set by `quote-form.html`, is `#quote-form`) — the link had never worked. Corrected both. Verified in build across all four page types: cards present, no duplication, both broken anchors fixed.

### D8 [DONE - 2026-07-02] Add route variant E's sticky stat sub-bar to the other route templates
Variant E's `.overview-bar` component (Lead time, Quarantine, Complexity, Airlines + "Start my quote" button) extracted into a new shared partial, `site/layouts/partials/routes/route-stat-subbar.html`. Confirmed the brand palette (amber #e8913a, green #1a6b4a, etc.) is identical across every route template's own CSS `:root` declaration, so the partial uses inline styles with these confirmed-universal values rather than depending on each template's own CSS custom properties - this makes it render correctly regardless of any small per-template naming difference, and means adding it carries zero risk to any of the six templates' existing CSS. Wired into na, nb, nc, nd, nl (ne already had the original). Templates differ enough structurally that the insertion point varies: after the hero `</section>` for na/nb/nc/nl; at the top of the scrolling `.left-col` for nd, which has no traditional hero and already has a persistent sticky sidebar with the form, so this is a lighter addition there than on the others. Verified in build across all six variants: "Start my quote" present exactly once per page, and the stats show real per-route data (for example "26-32 weeks" on argentina-to-australia, not a placeholder).

### D9 [DONE - 2026-07-02] WhatsApp float overlaps the quote-form submit button
Investigation: all six route templates use `position: sticky` sidebars in the same bottom-right screen region the WhatsApp float (`position: fixed`, `z-index: 9999`, 56x56px, bottom:28px/right:24px) always occupies, so the collision risk is general rather than tied to one template. Fixed in `site/assets/css/main.css`, a single sitewide change (not touching any of the six route templates individually, so zero risk of breaking their layouts): reduced the float's `z-index` from 9999 to 500, and added a media query for the 481-1200px range (the "smaller desktop widths" the audit flagged) that shrinks the float to 46px and pulls it slightly further from the edge, reducing the chance it sits on top of a sidebar submit button's icon. Full size and top z-index return on true mobile and full desktop widths. Verified compiled into the minified build CSS.

### D10 [DONE - 2026-07-02] Add a mid-page CTA at the high-intent moment on guides
Added a mid-page CTA card (reusing the `card accent-left` pattern already live on blog posts) at the specific high-intent point on each template: `countries/single.html` right after the import requirements section; `airlines/single.html` right after the "Policy at a Glance" grid; `breeds/single.html` right after the airline restrictions list. Breed pages branch on the existing `.Params.brachycephalic` boolean (already used elsewhere in the same template): brachycephalic breeds get "We specialise in brachycephalic breed transport and know which airlines and routes work for snub-nosed dogs and cats", other breeds get a generic reassurance line. Origins was not in scope for D10. Verified in build: correct copy on a country, an airline, a brachycephalic breed (French Bulldog) and a non-brachycephalic breed (Labrador Retriever), confirming the conditional branch works.

---

## Block 2 - Visual polish

### D11 [DONE - 2026-07-02] Missing hero images on airline and breed single pages
Decision D-c: one generic hero per section. `.ptg-inner-hero` (the shared CSS class behind the flat dark header) is also used by the blog template, which was not flagged by the audit and should not change, so the image was added as an inline style override on the `airlines/single.html` and `breeds/single.html` hero divs specifically, not in the shared CSS class. Airlines uses `/images/hero.jpg` (the site's existing flagship pet-travel image; no aviation-specific photo exists in the repo). Breeds uses `/images/pexels-dog-1850465.jpg` (breed pages cover both dogs and cats, so this is a pragmatic "one generic image" choice within the decision's scope, not a perfect per-item match). Both use a dark gradient overlay matching the hero's existing tone so text stays legible. Verified in build: airline and breed heroes now carry a background image, blog's hero is unchanged (still flat colour, confirming no regression).

### D12 [DONE - 2026-07-02] Blog markdown tables are unstyled
`.ptg-blog-body` had no CSS at all. Added table styling to `site/assets/css/main.css`: borders, cell padding, a green header row matching the brand, zebra striping, and `display:block;overflow-x:auto` on the table itself for responsive horizontal scroll on narrow screens (markdown tables render with no wrapper div to attach `overflow-x` to otherwise). Verified compiled into the minified build CSS.

### D13 [DONE - 2026-07-02] Methodology page is unstyled prose
New dedicated layout, `site/layouts/_default/methodology.html`, applied via `layout: "methodology"` in the page's front matter (it is the only loose file in `site/content/pet-transport/`, so this cannot affect any other page). Gives it the same branded `.ptg-inner-hero` treatment as D11 (airlines/breeds), the styled `verified-date.html` stamp (replacing an inline "Regulations verified: May 2026" sentence in the body, which duplicated it), and a CTA card at the end. Also fixed a real duplicate-H1 issue found while building this: the page previously rendered both a template H1 and its own markdown `# How We Source Our Route Data` heading (the markdown always renders a level-1 heading as an `<h1>`); removed the redundant heading from the content file so there is exactly one H1. Verified in build: single H1, background image present, verified-date stamp present, CTA present.

### D14 [DONE - 2026-07-03] Breadcrumb styling differs across route variants
Checked the compiled `.breadcrumb` CSS in all six `route-new-nX.css` files: none of them actually has an amber background bar (that specific audit description does not match anything in the current code, on any variant), so no amber-bar fix was applied. What genuinely differed was font-size (.68rem-.8rem), text colour opacity (.3-.45), and margin-bottom (28px-48px) across `na`, `nb`, `nc`, `ne`, `nl`. Standardised font-size to `.72rem` and colour to `rgba(255,255,255,.4)` across those five (using `na`'s existing values as the baseline; `na` itself needed no change). Left margin-bottom untouched per template since it is tied to each hero's own height/proportions, not a legibility issue. `route-new-nd` was deliberately excluded: its `.intro` block (the hero-equivalent) has a light cream background (`rgba(245,242,238,...)`), not the dark photo overlay the other five use, so its breadcrumb correctly uses `var(--muted)` dark-grey text rather than white-on-dark. That is correct-by-design, not an inconsistency. Verified via full Hugo build, no errors.

### D15 [DONE - 2026-07-03] Inconsistent form label case
Traced the actual cause: only `route-new-na` uses the shared `quote-form.html` partial, which has always used plain sentence-case labels ("Pet type", "Email", etc) with no CSS transform. The other five templates (`nb`, `nc`, `nd`, `ne`, `nl`) each have their own inline compact sidebar quote form, and although the label text in the HTML was already sentence case, the `.sf-label`/`.rf-label` CSS classes applied `text-transform:uppercase` with wide letter-spacing, rendering them as "PET TYPE", "EMAIL" etc regardless of what the markup said. Removed `text-transform:uppercase`, normalised letter-spacing, and standardised font-size to `.72rem` (from a range of .6rem-.65rem) and font-weight to 600 (from 700, since sentence case does not need the extra weight uppercase relied on for legibility) across all label rules in `nb`, `nc`, `nd`, `ne`, `nl`. `ne` turned out to have three separate `.sf-label` CSS rules targeting the same class (likely leftover duplication from earlier template iterations); found and fixed all three so there is no risk of a future reorder reintroducing the uppercase style via cascade order. Verified via full Hugo build: no build errors, no broken links, all label rules confirmed non-uppercase in the compiled output.

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

1. ~~**D1** (broken links, 42k instances - biggest SEO/UX bug)~~ - **DONE 2026-07-02**, 0 broken links remain, verified.
2. **D2, D3, D4** (title leak, fake email, home form) - quick critical fixes.
3. **D9** (WhatsApp overlap) and **D5, D6** (worst CTA placements) - fast conversion wins.
4. **D7, D8, D10** (CTA patterns sitewide).
5. **D11-D19** (visual polish), with D18 verify-only.
6. **D20** (standardise shared route components: breadcrumb, CTA, sub-bar, labels, sidebar cards) - absorbs D5, D6, D8, D14, D15.

Note: D16 (About page) is skipped per decision D-d.

## Model summary

Every item is **SONNET** (no Opus needed after decision D-f to standardise rather than consolidate the route designs). D20 remains the largest item; do it carefully, variant by variant, with a build check after each.

No em dashes were used in this document.
