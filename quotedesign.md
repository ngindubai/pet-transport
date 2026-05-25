# PetTransportGlobal — Quote Design Specification

> This file is the canonical reference for producing client-facing PDF quotes. Read it in full before building or modifying any quote. The design is locked. Do not change colours, fonts, layout logic, or payment terms without Gareth's explicit approval.

---

## Overview

Quotes are 3-page A4 PDF documents generated from a single HTML file rendered to PDF via Playwright/Chromium. The HTML uses embedded base64 woff2 fonts (Montserrat + Roboto) so the PDF renders correctly with no external network calls.

**Structure (always 3 pages):**
- **Page 1** — Masthead + intro paragraph + 4-cell meta grid + Quote 1 banner + first 8 transport rows + "continued" note + footer
- **Page 2** — Mini-header + Quote 1 continued (final 3 rows + subtotal row) + Quote 2 banner + boarding options + combined totals + footer
- **Page 3** — Mini-header + what's included / not included (two-col) + timeline callout + approximate timeline table + terms + next steps + footer

---

## Brand colours (from hugo.toml)

```css
--green:        #1a6b4a;   /* primary — masthead, section headings, totals */
--green-light:  #2a9d6e;   /* accents, paw watermark fill on mini-head */
--green-deep:   #145239;   /* gradient dark end */
--navy:         #1e3a5f;   /* table headers, secondary total band */
--amber:        #e8913a;   /* accent bar, CTA badges, Quote badge, arrow */
--amber-hover:  #d47e2a;   /* quote badge text */
--ink:          #1a1a2e;   /* body text */
--muted:        #5a6677;   /* notes, labels, footer text */
--line:         #e4e8ec;   /* table borders, dividers */
--surface:      #f7f9f8;   /* alternate table rows, meta grid bg */
--surface-warm: #fbf7f0;   /* subtotal row, callout bg, total-band left */
```

---

## Typography

- **Headings / labels / figures:** Montserrat (weights 600, 700, 800)
- **Body / notes / footer:** Roboto (weights 400, 500, 700)
- Both fonts are embedded as base64 woff2 in the render script — see `render.py`
- Font source: npm packages `@fontsource/montserrat` and `@fontsource/roboto`, extracted from the tarballs at `~/fonts/`

---

## Logo mark

The site's real logo is a solid Font Awesome paw print (`fa-paw`) next to the wordmark. In the PDF, replicate this with an inline SVG using the Font Awesome 6 solid paw path:

```html
<!-- Paw SVG path (Font Awesome 6 solid fa-paw) -->
<svg viewBox="0 0 512 512">
  <path d="M226.5 92.9c14.3 42.9-.3 86.2-32.6 96.8s-70.1-15.6-84.4-58.5 .3-86.2 32.6-96.8
    70.1 15.6 84.4 58.5zM100.4 198.6c18.9 32.4 14.3 70.1-10.2 84.1s-59.7-.9-78.5-33.3
    S-2.7 179.3 21.8 165.3s59.7 .9 78.5 33.3zM69.2 401.2C121.6 259.9 214.7 224 256 224
    s134.4 35.9 186.8 177.2c3.6 9.7 5.2 20.1 5.2 30.5v1.6c0 25.8-20.9 46.7-46.7 46.7
    -11.5 0-22.9-1.4-34-4.2l-88-22c-15.3-3.8-31.3-3.8-46.6 0l-88 22c-11.1 2.8-22.5 4.2
    -34 4.2C84.9 480 64 459.1 64 433.3v-1.6c0-10.4 1.6-20.8 5.2-30.5zM421.8 282.7
    c-24.5-14-29.1-51.7-10.2-84.1s54-47.3 78.5-33.3 29.1 51.7 10.2 84.1-54 47.3-78.5
    33.3zM310.1 189.7c-32.3-10.6-46.9-53.9-32.6-96.8s52.1-69.1 84.4-58.5 46.9 53.9
    32.6 96.8-52.1 69.1-84.4 58.5z"/>
</svg>
```

**Usage:**
- **Masthead glyph box:** paw SVG filled `#fff`, inside a 40×40px rounded box with rgba white border and background
- **Masthead watermark:** same paw SVG, 44×44mm, filled `#fff`, opacity 0.1, positioned top-right of the masthead
- **Mini-header (pages 2+):** paw SVG 20×20px, filled `#e8913a` (amber), sits left of the wordmark

**Wordmark text:** `PetTransport` (white) + `Global` (amber `#e8913a`), Montserrat 800, 16.5pt in masthead; 12pt in mini-header

---

## Masthead (page 1 only)

```
Background: radial-gradient (amber radial top-right, subtle) + linear-gradient(135deg, #145239 → #1a6b4a → #18553b)
Bottom edge: 5px amber gradient bar
Padding: 13mm top/bottom, 16mm left/right
Content:
  Left: glyph box + wordmark + URL in small caps
  Right: "TRANSPORT QUOTATION" kicker + ref number + issue date
  Below brand-row: route line — [Origin city large] → [Destination city large]
```

## Mini-header (pages 2 and 3)

```
Background: linear-gradient(135deg, #145239 → #1a6b4a)
Bottom edge: 3px solid amber
Padding: 7mm top/bottom, 16mm left/right
Content: amber paw + wordmark left | page description right (muted uppercase small caps)
```

---

## Page body padding

```
Left/right: 16mm
Top: 8mm (page 1) or 9mm (pages 2–3)
Bottom: 0 (foot is position:absolute)
```

---

## Key components

### Intro paragraph (page 1)
- No client name or greeting — starts directly with the document description
- Roboto 10pt, line-height 1.5, colour #34404e
- Bottom margin 4mm

### Meta grid
- 4 columns, 1 border, 10px border-radius, overflow hidden
- Labels: Montserrat 6.8pt uppercase, muted. Values: 9.5pt medium ink.

### Quote banner
- Green left border (5px), subtle green gradient background
- Numbered circle (green), bold title (Montserrat 14pt green-deep), subtitle (8.2pt muted)
- Right-aligned amber badge: "QUOTE 1 OF 2" / "QUOTE 2 OF 2"

### Line-item table
- Navy header row (Montserrat 7pt uppercase, white)
- Alternating white / `--surface` rows
- Columns: Service (description + note) | Stage (chip badge) | Amount (right-aligned navy bold)
- Row padding: 5.5px top/bottom, 12px left/right
- Subtotal row: surface-warm bg, 2px green top border, larger font

### Stage chip badges
- `chip.tr` (Turkey): green-tint bg, green-deep text
- `chip.air` (Air freight): blue-tint bg, navy text
- `chip.de` (Germany): amber-tint bg, amber-dark text
- Montserrat 6.6pt uppercase, 3px 8px padding, 20px border-radius

### Total band
- Flex row, 11px border-radius, green box-shadow
- Left: surface-warm, title + subtitle
- Right: green gradient, "TOTAL EUR" label + large figure (Montserrat 800, 20pt)
- Navy variant used for secondary/lower-priority totals

### Boarding option cards (Quote 2)
- 2-column grid, 6mm gap
- Recommended card: green border + green-tint header
- Each card: header (name + rate), body (description), foot (calc label + large figure)

### Timeline callout (page 3)
- Amber left bar (5px), amber-tint gradient bg
- Title: Montserrat 700 9.5pt, amber-dark
- Body: 8.7pt amber-dark line-height 1.55, **bold** on key waiting periods

### Timeline table (page 3)
- Surface bg header, 2px green bottom border
- Wait rows: surface-warm bg
- Flight day row: green-tint bg, bold text
- Columns: Stage | What happens | Timing (right-aligned)

### Footer (all pages)
- position:absolute, bottom 10mm, left/right 16mm
- 3px green→amber gradient rule, then one row:
  Left: **PetTransportGlobal** · International pet relocation [· pettransportglobal.com on page 3]
  Right: Ref · Date · Page X of 3

---

## Payment terms (NON-NEGOTIABLE)

Always state in the Terms & Conditions section:

> **Payment is required in full and upfront before any work begins.**

Never offer a deposit split or instalment option. The full quote amount is due before any services commence. This is because PetTransportGlobal pays suppliers in full before the work starts.

---

## Quote rules

- **No client name anywhere.** Do not open with "Dear [Name]" or reference the client by name in the body.
- **No Gareth's name or founder credit anywhere on the quote.**
- Quote reference format: `PTG-YYYYMMDD-NNN` (e.g. `PTG-20260525-001`)
- Quote valid for **30 days** from issue date.
- Currency: always **Euro (EUR)** for Turkey-origin quotes. Use local currency where applicable for other origins.
- Margin: set per-job by Gareth. Default is **20%** unless instructed otherwise.
- Boarding: always quote separately as Quote 2. Frame it as optional — the client may arrange their own.

---

## Page overflow rules (critical)

The page height is fixed at 297mm with `overflow:hidden`. Content that exceeds this is clipped, not reflowed. Measure before finalising:

```python
# In render.py / measure.py — check bodyBottom < footTop for every page
overlap = bodyBottom - footTop  # must be NEGATIVE (body ends above foot)
```

If page 1 overflows:
1. Move the last N table rows to the top of page 2 with a "continued on page 2" italic note.
2. Reduce table row padding in 0.5px steps.
3. Reduce intro `margin-bottom` in 1mm steps.
4. Never reduce font sizes — legibility is non-negotiable.

---

## File locations

| File | Purpose |
|---|---|
| `/home/claude/quote.html` | Working HTML source (runtime only, not in repo) |
| `/home/claude/quote_embedded.html` | Auto-generated by render.py with fonts injected |
| `/home/claude/render.py` | Renders HTML to PDF via Playwright |
| `/home/claude/measure.py` | Checks body/footer overlap per page |
| `/home/claude/fonts/` | woff2 font files (Montserrat 600/700/800, Roboto 400/500/700) |
| `quotedesign.md` | This file (canonical design spec, in repo) |

The font files and render scripts live in `/home/claude/` at runtime. If the environment is reset, reinstall:

```bash
# Fonts (from npm tarballs)
npm pack @fontsource/montserrat@5.0.18
npm pack @fontsource/roboto@5.0.8
tar xzf fontsource-montserrat-5.0.18.tgz && mv package pkg-mont
tar xzf fontsource-roboto-5.0.8.tgz && mv package pkg-roboto
mkdir -p fonts
cp pkg-mont/files/montserrat-latin-{600,700,800}-normal.woff2 fonts/
cp pkg-roboto/files/roboto-latin-{400,500,700}-normal.woff2 fonts/

# Playwright (chromium is at /opt/pw-browsers)
pip install playwright --break-system-packages
# No install needed — browser binary already at /opt/pw-browsers
```

To render a quote:
```bash
PLAYWRIGHT_BROWSERS_PATH=/opt/pw-browsers python3 render.py
```

---

## Producing a new quote — checklist

1. Read this file.
2. Confirm with Gareth: origin, destination, pet details, services required, margin %, currency.
3. Calculate all figures at the agreed margin. Double-check every line.
4. Copy the last `quote.html` and adapt: update ref number, date, route, meta grid, line items, amounts, totals.
5. Embed fonts and render: `PLAYWRIGHT_BROWSERS_PATH=/opt/pw-browsers python3 render.py`
6. Run `measure.py` — confirm overlap is negative on all pages.
7. Convert to preview images at 130dpi and visually check every page.
8. Present the PDF to Gareth for review.
9. Once approved, present as downloadable file.

*Last updated: 2026-05-25*
