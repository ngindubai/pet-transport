# CLAUDE.md — PetTransportGlobal

> Single source of truth for any AI assistant working on this project (Claude app, VS Code Copilot, Cursor, etc.). Read this in full at the start of every session.

---

## THE 4 LOAD-BEARING RULES (Karpathy)

1. **Ask, don't assume.** If anything is unclear, ask before writing a single line. Never make silent assumptions about intent, architecture, or requirements.
2. **Simplest solution first.** Always implement the simplest thing that could work. Do not add abstractions or flexibility that weren't explicitly requested.
3. **Don't touch unrelated code.** If a file or function is not directly part of the current task, do not modify it, even if you think it could be improved.
4. **Flag uncertainty explicitly.** If you are not confident about an approach or technical detail, say so before proceeding. Confidence without certainty causes damage.

---

## ABOUT THE USER

- **Name:** Gareth
- **Role:** Founder, PetTransportGlobal
- **Technical level:** Non-technical. Does not read code. Does not know git commands by heart. Does not know Python or Hugo internals.
- **What this means for you:**
  - Use plain English. No jargon without explanation.
  - For any manual task Gareth has to do (in a terminal, in GitHub, in Hostinger, in the Claude app), give **step-by-step click-this, type-this instructions**. Number every step.
  - Never say "just run X" without showing the exact command and explaining what it does in one line.
  - If something fails, diagnose it yourself. Do not ask Gareth to read error logs unless you've already tried to understand them.
  - When you finish a task, summarise in plain English: what changed, what's live, what's next.

---

## THE PROJECT

- **Site:** pettransportglobal.com (live, on Hostinger)
- **Type:** Programmatic SEO lead-generation site for international pet transport
- **Goal:** Capture enquiries from pet owners relocating internationally, via organic search
- **Audience:** Anxious pet owners about to ship their dog or cat overseas — needs warm, expert reassurance
- **Stack:**
  - Hugo v0.160.1-extended (static site generator)
  - Python 3.11 (route/content generators at repo root)
  - GitHub Actions (auto-build + incremental FTP deploy)
  - Hostinger (hosting, accessed via FTP)
- **Repository:** https://github.com/ngindubai/pet-transport (private)

---

## ENQUIRY TRACKING SYSTEM

### Overview

All client enquiries are tracked in a Google Sheet. When a new enquiry comes in, Gareth pastes it into this chat. Claude reads the live sheet, determines the next REF number, and produces a PowerShell command that Gareth pastes into Windows PowerShell to add the row directly to the sheet via webhook. No file downloads or uploads needed.

### Key details

- **Google Sheet:** https://docs.google.com/spreadsheets/d/1AWlrcecS7B5z_1qujwgK_bu4LKNgWM48JGrnm7Yetbk/edit
- **Sheet file ID:** `1AWlrcecS7B5z_1qujwgK_bu4LKNgWM48JGrnm7Yetbk`
- **Webhook URL:** `https://script.google.com/macros/s/AKfycby1b4a4UcMmwBqgl0AUmAzaefwR8APcnK5vfL4NZI-_t4wK9HiNwK8K44hUBEGSaSg/exec`
- **Sheet name:** `Enquiry Tracker`
- **REF format:** PTG-001, PTG-002, PTG-003... (increment from last row in sheet)

### Column order (18 columns, must match exactly)

| # | Field | Key in JSON |
|---|---|---|
| 1 | REF | `ref` |
| 2 | DATE IN | `date_in` |
| 3 | CLIENT NAME | `client_name` |
| 4 | EMAIL | `email` |
| 5 | PHONE | `phone` |
| 6 | ORIGIN | `origin` |
| 7 | DESTINATION | `destination` |
| 8 | PET TYPE | `pet_type` |
| 9 | BREED | `breed` |
| 10 | WEIGHT (KG) | `weight` |
| 11 | TRAVEL DATE | `travel_date` |
| 12 | NOTES | `notes` |
| 13 | STATUS | `status` |
| 14 | QUOTE REF | `quote_ref` |
| 15 | QUOTE VALUE | `quote_value` |
| 16 | CURRENCY | `currency` |
| 17 | NEXT ACTION | `next_action` |
| 18 | LAST UPDATED | `last_updated` |

### Status values (use exactly as written)

`New enquiry` / `Info requested` / `Awaiting quotes` / `Quote sent` / `Quote accepted` / `In progress` / `Completed` / `On hold` / `Lost / no reply`

### Process — follow this every time a new enquiry comes in

1. **Read the sheet first.** Use the Google Drive connector:
   - Tool: `Google Drive: read_file_content`, fileId: `1AWlrcecS7B5z_1qujwgK_bu4LKNgWM48JGrnm7Yetbk`
   - Find the last PTG-XXX number and increment by 1 for the new row.

2. **Build the JSON** from the enquiry details. Use today's date for `date_in` and `last_updated`. Set `status` appropriately (`New enquiry` or `Info requested` if a response has already been sent).

3. **Generate the PowerShell command** in this exact format — one block Gareth can copy and paste straight into Windows PowerShell:

```powershell
Invoke-WebRequest -Uri "https://script.google.com/macros/s/AKfycby1b4a4UcMmwBqgl0AUmAzaefwR8APcnK5vfL4NZI-_t4wK9HiNwK8K44hUBEGSaSg/exec" -Method POST -ContentType "application/json" -Body '{"ref":"PTG-00X","date_in":"DD/MM/YYYY","client_name":"...","email":"...","phone":"...","origin":"...","destination":"...","pet_type":"...","breed":"...","weight":"...","travel_date":"...","notes":"...","status":"...","quote_ref":"","quote_value":"","currency":"...","next_action":"...","last_updated":"DD/MM/YYYY"}' -UseBasicParsing
```

4. **Tell Gareth:** "Open Windows PowerShell (search for it in the Start menu), paste this command and press Enter. The row will appear in the sheet immediately."

5. **After Gareth confirms** it worked, read the sheet again to verify the row is there.

### Important notes on the webhook

- Claude cannot call the webhook directly — Google's robots.txt blocks automated requests from Claude's servers. The PowerShell command runs from Gareth's own machine and goes through fine.
- The Apps Script is deployed as "Anyone" access — no login needed.
- **Single quotes in the notes field will break the command.** If any field contains an apostrophe (e.g. "owner's dog"), remove it or replace with a space before putting it in the JSON. Write "owners dog" not "owner's dog".

---

## DEPLOY PIPELINE — INCREMENTAL FTP (ESTABLISHED 2026-05-22)

**This is the proven, working deploy method. Do not change it without explicit approval.**

### How it works

```
Push/merge to main
   ↓
GitHub Actions triggers automatically
   ↓
Hugo --gc --minify builds site/public/ (~6,200+ pages)
   ↓
python split_sitemap.py creates section sitemaps
   ↓
FTP Deploy Action checks .ftp-deploy-sync-state.json on Hostinger
   ↓
Only NEW or CHANGED files are uploaded (seconds, not hours)
   ↓
Updated state file uploaded to Hostinger
   ↓
Live on pettransportglobal.com
```

### Why incremental — DO NOT attempt full-site FTP uploads

The site has 6,200+ pages. A full FTP upload takes 2-3 hours and Hostinger's shared hosting drops the connection before it finishes. This was discovered on 2026-05-22 after multiple failed deploy attempts.

### Critical rules

- **Never delete `.ftp-deploy-sync-state.json` from Hostinger.**
- **Never set `dangerous-clean-slate: true`** in the workflow.
- **Never attempt to upload the entire `site/public/` directory manually.**
- **The `.github/workflows/deploy.yml` file cannot be edited via the MCP connector** (GitHub returns 403). Provide the complete updated file and ask Gareth to paste it via the GitHub web editor.

### Deploy speed expectations

| Change type | Expected deploy time |
|---|---|
| 1 new blog article | 30–60 seconds |
| 25 new route pages | 2–5 minutes |
| Template change (affects all pages) | 30–60 minutes |
| First deploy after state file deletion | Will fail — regenerate state file first |

---

## CURRENT STATUS (update this when it changes)

- **Quality routes built:** 5,461 of 37,830 country pairs (~14%).
- **Blog:** 411 articles. Content plan: 252 new articles Jun 2026–May 2027. Day 3 is next.
- **Deploy pipeline:** Working. Incremental FTP via GitHub Actions. Confirmed 2026-05-22.
- **Enquiry tracker:** Live. 5 enquiries logged (PTG-001 to PTG-005). Webhook deployed.
- **Live tracker:** [build_state.json](build_state.json)
- **Plan files:** [BUILD-PLAN.md](BUILD-PLAN.md), [cascading-build-plan-pet=transport.html](cascading-build-plan-pet=transport.html)

---

## COMMUNICATION DEFAULTS

- **No filler.** Never start with "Great question!", "Of course!", "Certainly!". Start with the answer.
- **Match length to task.** Simple question → short answer. Complex task → full answer. Never pad.
- **Show options before acting** on anything significant.
- **Admit uncertainty.** Do not invent plausible-sounding details. YMYL site — wrong info hurts pets.
- **Use British English** in all site content.
- **When editing files that need Gareth to paste, always provide the COMPLETE file contents.**

---

## REVIEW BEFORE PUBLISH — NON-NEGOTIABLE

Every blog article or page must be presented as a rendered HTML file for review before it is committed to the repo.

**Workflow:**
1. Write the article (markdown + YAML front matter)
2. Build standalone HTML preview using the site's actual nav/footer/CSS
3. Present as downloadable `.html` artifact for Gareth to review in a browser
4. Wait for explicit approval
5. Only after approval: commit `.md` directly to `main`

---

## AUTHOR PERSONAS — NON-NEGOTIABLE

**Never use Gareth's name as an author.** Use one of the personas below.

| Persona | Name | Title | Use for |
|---|---|---|---|
| **The Logistics Lead** | Marcus Webb | Senior Pet Relocation Consultant, PetTransportGlobal | Route guides, airline policies, cargo logistics, costs, quotes, process and timeline articles |
| **The Regulations Expert** | Dr. Sarah Okafor | International Animal Health Consultant, PetTransportGlobal | Country import/export guides, quarantine, titre tests, DEFRA/APHIS/DAFF, pet passports |
| **The Welfare Advisor** | Emma Hartley | Certified Animal Behaviourist & Pet Travel Adviser, PetTransportGlobal | Breed welfare, brachycephalic, anxiety, sedation, senior pets, welfare during transit |
| **The Planning Guide** | James Osei | Pet Transport Planning Specialist, PetTransportGlobal | Checklists, timelines, documentation, choosing a company, insurance, multi-pet, emergency moves |

---

## QUOTING SYSTEM

Full specification in **[quotedesign.md](quotedesign.md)** — read it before producing any quote.

### Key rules

- No client name on the quote. No Gareth's name or founder credit.
- Payment in full and upfront before any work begins.
- Default margin: 20% unless Gareth specifies otherwise.
- Split into two quotes when boarding is relevant.
- Quote reference format: `PTG-YYYYMMDD-NNN`. Valid 30 days.
- Currency: EUR for Turkey-origin. Local currency for other origins.
- Rendering: HTML to PDF via Playwright/Chromium. Use `render.py` and `measure.py` in `/home/claude/`.

### To produce a quote
1. Read [quotedesign.md](quotedesign.md).
2. Confirm margin, currency, services, origin/destination.
3. Calculate all figures.
4. Adapt last `quote.html`, update figures, ref, date, route.
5. Render, measure, visual check, present to Gareth.

---

## BEHAVIOR RULES

### Stay in scope
Only modify files directly related to the current task. Mention improvements elsewhere as a note — do not touch them.

### The cascading build plan is law
Never bulk-generate content. One block at a time (25 routes or equivalent). Full quality gate every time.

### Quality gate
1. Research — real regulations from data files and named sources
2. Write — load the-wordsmith.md for voice
3. Rotate templates — A to E
4. Humanise — the-chameleon.md rules
5. QA scan — the-auditor.md checks
6. HTML preview — present to Gareth for approval
7. Commit to main only after approval
8. Stop and wait for next "go"

---

## CONTENT RULES (NON-NEGOTIABLE)

1. No safety guarantees.
2. Named, dated sources for every regulatory claim.
3. Warm, expert tone.
4. No em dashes.
5. No banned vocabulary: delve, meticulous, comprehensive, tailored, navigate, leverage, seamless, robust, vital, crucial, utilize, intricate, paramount, pivotal, embark, foster, elevate, unleash, unlock, harness, streamline, holistic, realm, landscape (figurative), testament.
6. Vary sentence rhythm.
7. Use correct author persona. Never use Gareth's name.
8. British English throughout.

---

## SEO RULES (NON-NEGOTIABLE)

- Unique `title` and `description` per page.
- One `<h1>` per page containing primary keyword.
- Target keyword in first 100 words, one H2, meta description.
- Internal links: route → origin hub + destination country guide + relevant airlines.
- FAQ schema from `faqs:` front matter.
- No duplicate content.

---

## TECH STACK (LOCKED)

- Hugo v0.160.1-extended, Python 3.11, GitHub Actions, Hostinger FTP
- No JS frameworks, no React, no Next.js, no Tailwind build step

---

## DIRECTORY STRUCTURE

```
pet-transport/
├── site/content/         # All page content (routes, countries, origins, airlines, breeds, blog)
├── site/layouts/         # Hugo templates
├── site/static/          # CSS, JS, images, fonts
├── data/                 # Source JSON for generators
├── workforce/            # Worker soul files
├── CLAUDE.md             # THIS FILE
├── quotedesign.md        # PDF quote design spec
├── BUILD-PLAN.md         # Session log + remaining tasks
├── build_state.json      # Machine-readable progress
├── ERRORS.md             # Failed approaches log
└── MEMORY.md             # Decision log
```

---

## SESSION PROTOCOLS

### New enquiry comes in
1. Read the tracker sheet (Google Drive connector, fileId `1AWlrcecS7B5z_1qujwgK_bu4LKNgWM48JGrnm7Yetbk`)
2. Determine next REF number
3. Build JSON from enquiry details
4. Generate PowerShell command
5. Present to Gareth to paste into PowerShell
6. Verify row appeared in sheet

### "go" or "next block"
1. Read BUILD-PLAN.md and build_state.json
2. Write content through full quality gate
3. Present HTML preview, wait for approval
4. Commit to main, provide live URL and Actions link
5. Stop and wait

### "session end" or "wrap up"
1. Update BUILD-PLAN.md, build_state.json, MEMORY.md
2. Commit to main
3. Summarise what was built and what is next

---

## PERMANENT FACTS

- Domain: pettransportglobal.com (Hostinger). Old surge.sh references are stale.
- Slugs: lowercase, hyphen-separated, no underscores.
- Python generators at repo root, not in scripts/.
- Hugo content must live in site/content/.
- site/public/ is gitignored — never commit build output.
- Every push to main auto-deploys via incremental FTP.
- Do NOT delete .ftp-deploy-sync-state.json from Hostinger.
- FTP credentials in GitHub Secrets only — never in chat or commits.
- .github/workflows/deploy.yml cannot be edited via MCP connector (403).
- Never use Gareth's real name as author on published content.
- Quote design is locked — see quotedesign.md.
- Enquiry tracker webhook is live — see ENQUIRY TRACKING SYSTEM section.

---

## WHAT TO DO WHEN STUCK

1. Re-read this file.
2. Read MEMORY.md for prior decisions.
3. Check ERRORS.md for prior failures.
4. Ask Gareth one specific question.

---

*Last updated: 2026-05-26*
