# DESIGN.md — PetTransportGlobal

> **Second bible for this project.** Read `CLAUDE.md` first for project-wide rules, then this file for anything that touches how the site *looks*. This is the single source of truth for design, templates, CSS, and the anti-AI-detection layout system.
>
> This chat (and any "design" session) is for **design edits only**. Content, regulations, routes, and copy live elsewhere. If a request is about wording or regulatory facts, it belongs in a content session, not here.
>
> *Last updated: 2026-05-22*

---

## THE ONE RULE THAT MATTERS MOST (read before any edit)

**This is a Hugo static site. Templates generate pages at build time. One template or CSS change rewrites thousands of live pages on the next build.**

There are ~5,400 route pages plus hundreds of country, airline, breed, and blog pages. None of them have hand-written HTML for layout. They all render through a small set of template files and **one editable stylesheet**. So:

- Editing `site/assets/css/main.css` can change **every page on the site** at once.
- Editing `site/layouts/_default/baseof.html` changes the wrapper (head, nav, footer, scripts) on **every page**.
- Editing one route variant partial changes **every route assigned to that variant** (roughly a fifth of all routes).

Before any change, answer one question: **"How many pages does this touch?"** If the answer is "thousands", slow down, scope it, and (per the delivery rule below) get Gareth's sign-off.

---

## THE ANTI-DETECTION SYSTEM (do not break this)

Google penalises programmatic sites where every page is structurally identical (find-and-replace pages). To avoid that, route pages are rendered through **6 different layouts** that produce **genuinely different HTML structure**, not just different colours.

### How it works

`site/layouts/routes/single.html` is a **dispatcher**. It reads `template_variant` from each page's YAML front matter and renders the matching partial:

| `template_variant` | Partial | Visual identity |
|--------------------|---------|-----------------|
| `A` | `partials/routes/route-a-fieldmanual.html` | **Field Manual** — slim dark banner, dense tables, vertical stepper, single column, no sidebar |
| `B` | `partials/routes/route-b-journey.html` | **Visual Journey** — image hero with overlay, horizontal scroll timeline, right sidebar, marketing tone |
| `C` | `partials/routes/route-c-comparison.html` | **Comparison Brief** — split origin/destination hero with centre bridge, side-by-side compare tables, left scroll-rail |
| `D` | `partials/routes/route-d-qa.html` | **Conversational Q&A** — white minimal hero, H1 as a question, Q+A blocks, no sidebar, mobile floating CTA |
| `E` | `partials/routes/route-e-data.html` | **Data-Forward** — dark stats-strip hero, Gantt timeline, invoice-style costs, tables dominate, right sidebar |
| (none / `legacy`) | `partials/routes/route-legacy.html` | **Legacy** — original template (used for all US and UK routes, kept stable) |

All six read the **same data** (`route_data`, `faqs`, `links`, `content` from front matter). The differences are purely structural and stylistic. That is the whole point: same facts, six different page shapes.

### CSS namespacing is what keeps them distinct

Each variant's CSS is scoped under its own class so styles never bleed:

- Template A → `.tpl-route-a .tpl-a-*`
- Template B → `.tpl-route-b .tpl-b-*`
- Template C → `.tpl-route-c .tpl-c-*`
- Template D → `.tpl-route-d .tpl-d-*`
- Template E → `.tpl-route-e .tpl-e-*`

The partial's outermost element carries the scope class (e.g. `<article class="tpl-route-a">`), and every rule for that variant is prefixed with it.

### The cardinal design rule

**Never make a change that causes two or more variants to converge in appearance.** If A, B, C, D, and E start looking the same, the anti-detection value is gone and the whole site is at risk.

Concretely:
- A change meant for **one** variant goes in that variant's namespace only (`.tpl-route-b ...`). Never in a shared/global block.
- A change to a **shared/global** block (see "global fixes" at the bottom of `main.css`, or `baseof.html`, or the header/footer partials) is a **cascade change** — it hits all variants and all page types. These require Gareth's explicit sign-off before pushing (see Delivery Rule).
- If you want all six to improve in the *same spirit* (e.g. "make all route tables more readable"), apply a **deliberately different** treatment per namespace, not one shared rule. Keeping them visually distinct is the job.

---

## DELIVERY RULE (how design changes ship)

Default for this chat, unless Gareth says otherwise in the moment:

1. **Scoped, single-variant or single-component change** → make it, open a **pull request on a branch** (e.g. `design/route-b-timeline-tweak`), summarise in plain English, stop. Gareth reviews and merges on GitHub.
2. **Cascade change** (anything in `main.css` global blocks, `baseof.html`, `header.html`, `footer.html`, `maincolors.css`, or `hugo.toml` design params) → **describe the change and the page-count impact first, wait for explicit "yes", then** open the PR.
3. **Never trigger a deploy.** Merging a PR does **not** publish. The site only updates when Gareth runs the GitHub Actions workflow manually. Design changes wait there until he chooses to deploy.

Per `CLAUDE.md`: pushing/merging to `main` is safe (no auto-deploy). Deleting files, rewriting history, or editing the deploy pipeline still need explicit confirmation.

---

## FILE MAP — WHERE EVERY DESIGN THING LIVES

```
site/
├── hugo.toml                         # design-relevant params: brand, colours via params, GA4, fonts
├── assets/
│   └── css/
│       └── main.css                  # ★ THE editable stylesheet. ~95% of design edits land here.
│   └── js/
│       └── main.js                   # site-specific JS (minified+fingerprinted by Hugo)
├── static/                           # served as-is at site root
│   ├── css/style.css                 # vendor template CSS — DO NOT EDIT (override in main.css)
│   ├── css/plugins.css               # vendor plugin CSS — DO NOT EDIT
│   ├── styles/maincolors.css         # template colour scheme — cascade-risk, edit with care
│   ├── vendor/bootstrap/...          # Bootstrap 5.3 — DO NOT EDIT
│   ├── js/custom.js, plugins.js …    # vendor JS — DO NOT EDIT
│   ├── img/                          # photographic backgrounds + content images
│   └── fonts/                        # Flaticon + FontAwesome icon fonts
└── layouts/
    ├── _default/
    │   ├── baseof.html               # ★ master wrapper: <head>, CSS/JS load order, body, nav+footer hooks
    │   ├── list.html                 # listing pages (route index, country index, blog index, etc.)
    │   ├── single.html               # generic single page (About, Contact, Privacy, etc.)
    │   └── thank-you.html            # post-form confirmation page
    ├── index.html                    # homepage (hero, carousels, services, testimonials)
    ├── routes/
    │   └── single.html               # ★ DISPATCHER — picks route variant A–E or legacy
    ├── partials/
    │   ├── header.html               # fixed nav + 4 megamenus + CTA (cascade: every page)
    │   ├── footer.html               # footer (cascade: every page)
    │   ├── breadcrumbs.html          # shared breadcrumb
    │   ├── faq-accordion.html        # shared FAQ block (used by routes, airlines, etc.)
    │   ├── quote-form.html           # shared lead-capture form (used site-wide)
    │   ├── route-card.html           # shared route teaser card
    │   └── routes/
    │       ├── route-a-fieldmanual.html   # variant A structure
    │       ├── route-b-journey.html       # variant B structure
    │       ├── route-c-comparison.html    # variant C structure
    │       ├── route-d-qa.html            # variant D structure
    │       ├── route-e-data.html          # variant E structure
    │       └── route-legacy.html          # legacy structure (US/UK routes)
    ├── airlines/single.html          # airline page  → uses .ptg-inner-* namespace
    ├── breeds/single.html            # breed page    → uses .ptg-inner-* namespace
    ├── countries/single.html         # country guide → uses .ptg-inner-* namespace
    └── origins/single.html           # origin hub    → uses .ptg-inner-* namespace
```

### CSS load order (in `baseof.html`, top to bottom — later wins)

1. Bootstrap 5.3 (`/vendor/bootstrap/css/bootstrap.min.css`)
2. Template `style.css` + `plugins.css` (`/css/...`)
3. `maincolors.css` (`/styles/maincolors.css`) — template colour scheme
4. **`assets/css/main.css`** (Hugo pipeline, minified + fingerprinted) — **our overrides**

Because `main.css` loads last, it's the right place to override anything from the vendor layers. **Never edit the vendor files** (`style.css`, `plugins.css`, Bootstrap). Override them in `main.css` instead. `maincolors.css` is editable but is a cascade risk — it changes the template's base palette everywhere.

---

## BRAND SYSTEM

### Colours

| Token | Hex | Use |
|-------|-----|-----|
| Primary navy | `#1e3a5f` | logo text, nav, headings, links, primary UI |
| Deep ink navy | `#1a1e2b` / `#0f1623` | dark hero banners (templates A, E), inner-page hero |
| Brand gold | `#e8913a` | accent, CTAs, logo accent, hover, section underlines |
| Gold hover | `#cf7a28` | CTA hover |
| Trust green | `#2a9d6e` / `#1a6b4a` | success, "available" status, trust ticks |
| WhatsApp green | `#25d366` | WhatsApp float + topbar link only |
| Variant-blue | `#1a53b0` | route-variant accent (B/C/D/E sidebars, tables, timelines) |
| Warn amber | `#ffc107` / `#856404` | warnings, temperature/brachy cautions |
| Danger red | `#dc3545` / `#721c24` | breed bans, critical warnings |

Greys follow Bootstrap defaults (`#495057`, `#6c757d`, `#dee2e6`, `#f8f9fa`).

### Type

- **Headings / brand:** Montserrat (400–700), loaded from Google Fonts in `baseof.html`.
- **Body:** Roboto (400/600/700).
- Headings inside route variants are deliberately re-sized smaller than the vendor template defaults (see "global fixes" block in `main.css`) so dense pages read well.

### Recurring UI components (already styled in `main.css`)

- **Top bar** (`.ptg-topbar`) — navy strip, tagline + WhatsApp + phone. Hidden under 1200px.
- **Logo** (`.ptg-logo`) — paw icon + "PetTransport**Global**".
- **Megamenu** (`.ptg-mega-*`) — full-width hover panels for Routes / Countries / Airlines / Resources.
- **Nav CTA** (`.ptg-nav-cta`) — gold "Get a Quote" button.
- **WhatsApp float** (`.ptg-wa-float`) — fixed bottom-right bubble.
- **Inner-page hero + cards** (`.ptg-inner-*`, `.ptg-policy-card`) — shared by airline/breed/country/origin pages.
- **Country feature cards** (`.country-feature-card`) — glass-dark homepage carousel cards.
- **Testimonial cards** (`.testimonial-card`) — homepage social proof.

When adding a component, follow the existing `ptg-` prefix convention for site-wide pieces, or the variant namespace for route-variant pieces.

---

## CHANGE PLAYBOOK (match the request to the right file + scope)

| Request | Where it goes | Scope / risk |
|---------|---------------|--------------|
| Tweak how **one route variant** looks (e.g. "make Template B's timeline cards wider") | that variant's partial + `.tpl-route-b` CSS in `main.css` | One variant (~1/5 of routes). Scoped — PR and go. |
| Change **airline/breed/country/origin** page styling | `.ptg-inner-*` rules in `main.css` (and the relevant `*/single.html` if structural) | All pages of those types. Cascade — sign-off. |
| Change the **nav / megamenu / logo / topbar** | `header.html` + `.ptg-*` CSS | **Every page.** Cascade — sign-off. |
| Change the **footer** | `footer.html` + CSS | **Every page.** Cascade — sign-off. |
| Change the **quote form** appearance | `quote-form.html` + `.contact-form3` / `.hero-form-card` CSS | **Every page.** Cascade — sign-off. |
| Change **homepage** hero/carousels/sections | `index.html` + homepage CSS blocks in `main.css` | Homepage only. Scoped — PR and go. |
| Change **brand colour / font** globally | `maincolors.css` and/or `main.css` tokens + `hugo.toml` params | **Every page.** Big cascade — sign-off + preview first. |
| Swap a **background image** | drop file in `static/img/`, update the `url(...)` in `main.css` | Section/site-wide depending on selector. |
| Adjust **CSS/JS load order or `<head>`** | `baseof.html` | **Every page.** Cascade — sign-off. |
| Add a **brand-new route variant (F)** | new partial + dispatcher branch in `routes/single.html` + new `.tpl-route-f` namespace + assignment logic | Structural. Plan it explicitly with Gareth first. |

### Default working method for a scoped change

1. State which file(s) and which namespace you'll touch, and the page-count impact.
2. Make the smallest change that satisfies the request. Do not refactor neighbouring CSS.
3. Keep it inside one namespace. Do not "tidy up" shared blocks while you're in there.
4. Re-read the diff: does any selector accidentally lack its `.tpl-route-x` / `.ptg-` prefix and leak globally? If so, fix before pushing.
5. PR on a branch, plain-English summary, stop.

---

## HARD CONSTRAINTS (from CLAUDE.md, repeated here because design touches them)

- **Locked stack.** Hugo + vanilla CSS/JS in the existing template. **No React, no Tailwind build step, no JS framework, no SCSS pipeline.** Plain CSS in `main.css` only.
- **Don't edit vendor files.** `style.css`, `plugins.css`, Bootstrap, and the `template-source/` reference dir are off-limits. Override in `main.css`.
- **British English** in any visible copy you add (Colour, Centre, Organise). (Vendor classnames stay as-is.)
- **No safety guarantees** in any design copy (badges, CTAs, microcopy): never "arrives safely" / "guaranteed". Allowed: "experienced handlers", "IATA-compliant crates".
- **Accessibility:** keep `aria-label`s on icon-only controls, alt text on images, visible focus states. Respect `prefers-reduced-motion` (the hero video already does).
- **Performance:** vendor scripts are `defer`/lazy by design (Task 5.6). Don't add render-blocking CSS/JS to `baseof.html` without flagging the Core Web Vitals impact.
- `site/public/` is the **build output** and is gitignored — never edit or commit it. Edit source in `site/layouts`, `site/assets`, `site/static`.

---

## WHEN STUCK

1. Re-read this file and the relevant template/partial.
2. Confirm the namespace before writing a CSS rule.
3. Confirm the page-count impact before pushing.
4. Ask Gareth one specific question rather than guessing on a cascade change.
