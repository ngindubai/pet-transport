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

All client enquiries are tracked in a live Google Sheet. Every time Gareth pastes a new enquiry or an update on an existing client into this chat, Claude must:

1. **Read the sheet first** — always, without being asked
2. **Use the sheet as the source of truth** for all client context (status, notes, quote refs, next actions)
3. **Respond to the enquiry** using the context from the sheet
4. **End every response** with a PowerShell command that updates the sheet to reflect what just happened

This is non-negotiable. Every client interaction ends with a PowerShell command. No exceptions.

### Key details

- **Google Sheet:** https://docs.google.com/spreadsheets/d/1AWlrcecS7B5z_1qujwgK_bu4LKNgWM48JGrnm7Yetbk/edit
- **Sheet file ID:** `1AWlrcecS7B5z_1qujwgK_bu4LKNgWM48JGrnm7Yetbk`
- **Webhook URL (v2 — current):** `https://script.google.com/macros/s/AKfycbxJ0NgVVj1F3GK9K7qz5jG1OByfG3GcORJlQgxoM4jqyiwVmfArEercQ-OwAUDzv-_lIw/exec`
- **Sheet name:** `Enquiry Tracker`
- **REF format:** PTG-001, PTG-002, PTG-003... (zero-padded to 3 digits, increment from last data row)

### Column order (18 columns — must match exactly)

| # | Field | JSON key |
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

### Process — every single client interaction, without exception

**Step 1 — Read the sheet**
Use `Google Drive: read_file_content` with fileId `1AWlrcecS7B5z_1qujwgK_bu4LKNgWM48JGrnm7Yetbk` before doing anything else. This gives the current state of all enquiries: who they are, what stage they are at, what has already been sent or said.

**Step 2 — Determine what changed**
- New enquiry: assign the next PTG number (highest existing + 1), build a full new row
- Existing enquiry update: identify the correct PTG row, update the relevant fields (status, notes, next action, last updated, quote ref/value if a quote was sent)

**Step 3 — Handle the enquiry**
Respond, draft emails, produce quotes, etc. as required.

**Step 4 — End every response with a PowerShell command**
Always close with a clearly labelled section:

---
**📋 UPDATE THE TRACKER — paste this into Windows PowerShell and press Enter:**

```powershell
Invoke-WebRequest -Uri "https://script.google.com/macros/s/AKfycbxJ0NgVVj1F3GK9K7qz5jG1OByfG3GcORJlQgxoM4jqyiwVmfArEercQ-OwAUDzv-_lIw/exec" -Method POST -ContentType "application/json" -Body '{ ...full JSON... }' -UseBasicParsing
```
---

For **new rows**: the webhook appends the row above the PIPELINE SUMMARY line.
For **updates to existing rows**: the webhook currently only adds rows, so generate the PowerShell to add an updated version. Note in the command description that the old row should be manually deleted after the new one lands. (Future: update script to support row editing by REF.)

### Notes on apostrophes / single quotes

Single quotes inside the JSON body will break the PowerShell command. Always replace apostrophes in any field value with a space or remove them. Example: "owner's dog" becomes "owners dog".

### How Claude reads the sheet

```
Tool: Google Drive: read_file_content
fileId: 1AWlrcecS7B5z_1qujwgK_bu4LKNgWM48JGrnm7Yetbk
```

This returns a markdown table of all rows. Parse it to find: the last PTG-XXX number, the current status of any referenced client, their notes, quote refs, and next actions.

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
- **Enquiry tracker:** Live. PTG-001 to PTG-005 in sheet. Webhook v2 deployed and confirmed working.
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

### Every client enquiry interaction
1. Read the tracker sheet immediately (Google Drive connector)
2. Use sheet as source of truth for client context
3. Handle the enquiry (respond, quote, draft email, etc.)
4. End the response with a PowerShell command to update the sheet

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
- Enquiry tracker webhook v2 is live — see ENQUIRY TRACKING SYSTEM section. Always read the sheet before responding to any client enquiry.

---

## WHAT TO DO WHEN STUCK

1. Re-read this file.
2. Read MEMORY.md for prior decisions.
3. Check ERRORS.md for prior failures.
4. Ask Gareth one specific question.

---

*Last updated: 2026-05-26*
