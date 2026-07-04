# CLAUDE.md - PetTransportGlobal

> Single source of truth for any AI assistant working on this project (Claude app, VS Code Copilot, Cursor, etc.). Read this in full at the start of every session.

---

## THE 4 LOAD-BEARING RULES (Karpathy)

1. **Ask, don't assume.** If anything is unclear, ask before writing a single line. Never make silent assumptions about intent, architecture, or requirements.
2. **Simplest solution first.** Always implement the simplest thing that could work. Do not add abstractions or flexibility that weren't explicitly requested.
3. **Don't touch unrelated code.** If a file or function is not directly part of the current task, do not modify it, even if you think it could be improved.
4. **Flag uncertainty explicitly.** If you are not confident about an approach or technical detail, say so before proceeding. Confidence without certainty causes damage.

---

## EM DASH BAN - ABSOLUTE, NO EXCEPTIONS

**Never use em dashes anywhere, ever.** This applies to:
- All site content (articles, route pages, country guides, airline pages, breed guides)
- All client-facing messages (WhatsApp, email, quotes, cover letters)
- All internal documents (CLAUDE.md, BUILD-PLAN.md, MEMORY.md, quotedesign.md)
- All chat responses from Claude to Gareth

Use commas, full stops, colons, brackets, or restructure the sentence instead. There are no circumstances under which an em dash is acceptable. Not in headings, not in table cells, not in JSON, not in HTML attributes, not anywhere.

---

## DEPLOY IS AUTOMATIC + LIVE LINK REVIEW GATE - NON-NEGOTIABLE

**Confirmed 2026-06-02. This replaces the old "request to deploy" manual step. There is no manual deploy trigger any more.**

### The model

1. Push (or merge) to `main`.
2. GitHub Actions builds and deploys to Hostinger automatically. No manual "Run workflow" click.
3. **The safety gate is no longer "wait before deploying". The safety gate is REVIEW AFTER DEPLOY.**

### LIVE LINK REVIEW GATE (fires after every build batch, no exceptions)

After every job that changes or adds pages (a content block, a blog article, route pages, a template change, a fix), once the push is made Claude must:

1. Post, in the chat AND in Slack (#build-pet-transport), the **full live URL of every new or changed page** so Gareth can click and review each one.
2. **EACH PAGE MUST BE ON ITS OWN SEPARATE LINE WITH A BLANK LINE BETWEEN EACH URL.** Never group multiple URLs on one line, never use comma-separated links. One page = one line = one clickable link. In Slack, consecutive bare URLs without blank lines between them bunch together into an unclickable block. Every URL must be preceded and followed by a blank line (or use `- ` bullet prefix). This is non-negotiable.
3. **URL FORMAT IS FIXED — NEVER GUESS:** The canonical domain is non-www (`https://pettransportglobal.com/`); `www.pettransportglobal.com` redirects to it (corrected 2026-07-04, confirmed with Gareth; this section previously said www was canonical, which was wrong and contradicted the repo's own `baseURL`, schema, robots.txt and llms.txt, all of which have always been non-www). Route pages are always `https://pettransportglobal.com/pet-transport/[slug]/` (e.g. `https://pettransportglobal.com/pet-transport/denmark-to-switzerland/`). Blog articles are always `https://pettransportglobal.com/blog/[slug]/`. Country guides: `/pet-transport/countries/[slug]/`. Airlines: `/pet-transport/airlines/[slug]/`. Do NOT use `/routes/[slug]/` — that path does not exist and will 404.
4. Group the links clearly (new pages vs changed pages) and give the expected deploy time so Gareth knows when they will be live (see Deploy speed table below).
5. State plainly that these are now live and need a review, since there is no pre-publish hold.
6. If a template or sitewide change went out, name a representative sample of affected URLs (you cannot list thousands) plus the home page, so Gareth can spot-check.

**Why:** Deploy is automatic, so nothing stops thin or broken content reaching the live site except this review. Posting the live links every time is the control that catches problems fast. Skipping the link post is treated as a failed job.

### This pairs with the MANDATORY DOCS UPDATE rule below

Every build batch = (1) push content, (2) update the three docs + build_state.json in the same commit, (3) post the live review links. All three happen together, every time.

---

## MANDATORY DOCS UPDATE - EVERY COMMIT

**This rule fires on every single commit to main, no exceptions.**

Whenever content is committed (a blog article, route pages, any site file), the same commit or the immediately following commit must update all three of these files to reflect the new state:

1. **`BUILD-PLAN.md`** - add a session log row: date, what was built, new page count, what is next
2. **`build_state.json`** - update `last_updated`, `content_plan_articles_written`, the `notes` field, and reconcile the count fields. **Never type the count numbers by hand.** Run `python verify_build_state.py --write`, which recounts `routes_built`, `blog_articles` and `total_site_pages` straight from disk. Hand-incrementing these is exactly what caused the four-way count drift fixed on 2026-06-03.
3. **`MEMORY.md`** - update "Current State" block (routes, blog count, phase progress, content plan day)

The CURRENT STATUS section in **this file (CLAUDE.md)** must also be kept accurate and updated any time the numbers change.

**Anti-drift guard:** `verify_build_state.py` is the single source of truth for counts. It counts content from disk, compares to `build_state.json`, and fails if they diverge. A SessionStart hook runs `python verify_build_state.py` at the start of every web session, so drift is caught immediately. Run it before trusting any number, and `--write` to reconcile after a build.

**Why this matters:** When these docs drift from reality, the next session starts with false context and wastes time on a repo audit. Every commit is also a docs commit. **And every build batch also ends with the LIVE LINK REVIEW GATE above.**

**When committing via the MCP tool:** Bundle the content files and the three docs files into a single `push_files` call so it is one atomic commit. When a run builds a batch of several blocks, commit the WHOLE batch once (all content plus the three docs) in that single call. Never leave a dangling content commit without a matching docs update. Then post the live review links in chat.

---

## WHATSAPP AND EMAIL ACCESS RULES - NON-NEGOTIABLE

These rules govern how Claude reads and interacts with Gareth's WhatsApp and email accounts via Claude in Chrome.

### What Claude may do

- **Read** WhatsApp messages and email threads to build context
- **Draft** messages and emails for Gareth to review and send himself
- **Log** information from messages into the tracker

### What Claude must never do

- **Never send a WhatsApp message** to anyone unless Gareth explicitly instructs it in that specific conversation
- **Never send an email** to anyone unless Gareth explicitly instructs it in that specific conversation
- **Never delete** any WhatsApp message or email, ever, under any circumstances
- **Never reply** to any message or email automatically or proactively

### WhatsApp reading rules

- Claude may only read WhatsApp conversations with phone numbers that appear in the tracker spreadsheet
- Do not open, read, or reference any WhatsApp conversation with a number not in the tracker
- When Gareth says "check WhatsApp", read the conversation list and identify any messages from tracked phone numbers only
- New enquiries: Gareth will instruct Claude when to add a new number/enquiry to the tracker. Do not add new entries from WhatsApp without explicit instruction.

### Email reading rules

- Claude may read all emails in the inbox and sent items to build full context on supplier conversations
- Read threads completely so all quotes, replies, and follow-ups are captured
- Extract quote figures from any linked online quotes (Xero, Quotient, etc.) by opening the link
- Never compose or send any email without explicit instruction from Gareth

### WhatsApp access method

WhatsApp Web (web.whatsapp.com) must be open and logged in in Chrome before Claude can read it. Claude uses Claude in Chrome to read the page. Gareth keeps a tab open at web.whatsapp.com for this purpose.

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
  - When you finish a task, summarise in plain English: what changed, what's live, what's next. Always include the live review links.

---

## THE PROJECT

- **Site:** pettransportglobal.com (live, on Hostinger)
- **Type:** Programmatic SEO lead-generation site for international pet transport
- **Goal:** Capture enquiries from pet owners relocating internationally, via organic search
- **Audience:** Anxious pet owners about to ship their dog or cat overseas. Needs warm, expert reassurance
- **Stack:**
  - Hugo v0.160.1-extended (static site generator)
  - Python 3.11 (route/content generators at repo root)
  - GitHub Actions (auto-build + incremental FTP deploy)
  - Hostinger (hosting, accessed via FTP)
- **Repository:** https://github.com/ngindubai/pet-transport (private)

---

## ENQUIRY TRACKING SYSTEM

### Overview

All client enquiries are tracked in a live Google Sheet. Every client interaction must end with a tracker update. The webhook accepts two formats: POST (desktop) and GET (mobile). Always provide both.

### Key details

- **Google Sheet:** https://docs.google.com/spreadsheets/d/1AWlrcecS7B5z_1qujwgK_bu4LKNgWM48JGrnm7Yetbk/edit
- **Sheet file ID:** `1AWlrcecS7B5z_1qujwgK_bu4LKNgWM48JGrnm7Yetbk`
- **Webhook URL (v4, current):** `https://script.google.com/macros/s/AKfycbxJ0NgVVj1F3GK9K7qz5jG1OByfG3GcORJlQgxoM4jqyiwVmfArEercQ-OwAUDzv-_lIw/exec`
- **Sheet name:** `Enquiry Tracker`
- **REF format:** PTG-001, PTG-002, PTG-003... (zero-padded to 3 digits, increment from highest existing)

### Column order (18 columns - must match exactly)

| # | Field | JSON key / URL param |
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

### Process - every single client interaction, without exception

**Step 1 - Read the sheet**
Use `Google Drive: read_file_content` with fileId `1AWlrcecS7B5z_1qujwgK_bu4LKNgWM48JGrnm7Yetbk` before doing anything else.

**Step 2 - Determine what changed**
- New enquiry: assign the next PTG number (highest existing + 1)
- Existing enquiry: identify the correct PTG row, update the relevant fields

**Step 3 - Handle the enquiry**
Respond, draft messages, produce quotes, etc.

**Step 4 - End every response with BOTH update formats**

Always close with this section, providing both options every time:

---

**TRACKER UPDATE**

**Desktop (Windows PowerShell):**
```powershell
Invoke-WebRequest -Uri "https://script.google.com/macros/s/AKfycbxJ0NgVVj1F3GK9K7qz5jG1OByfG3GcORJlQgxoM4jqyiwVmfArEercQ-OwAUDzv-_lIw/exec" -Method POST -ContentType "application/json" -Body '{"ref":"PTG-00X","date_in":"DD/MM/YYYY",...all 18 fields...}' -UseBasicParsing
```

**Mobile (iPhone / iPad - tap this link):**
`https://script.google.com/macros/s/AKfycbxJ0NgVVj1F3GK9K7qz5jG1OByfG3GcORJlQgxoM4jqyiwVmfArEercQ-OwAUDzv-_lIw/exec?ref=PTG-00X&date_in=DD%2FMM%2FYYYY&...all 18 fields URL-encoded...`

---

### How the webhook works

- **POST** (PowerShell, desktop): sends JSON body. Used on Windows PC.
- **GET** (tappable link, mobile): sends same 18 fields as URL parameters. Used on iPhone/iPad.
- Both call the same upsert logic: if the REF exists in the sheet it overwrites that row; if it is new it inserts above the PIPELINE SUMMARY line.
- On first tap on a new device, Google shows a one-sentence warning page with a Dismiss button. Tap Dismiss once. It will not appear again on that device.
- A green "Tracker updated" confirmation page loads on success.

### Building the mobile link

URL-encode all field values. Key rules:
- Spaces become `+` or `%20`
- Forward slashes in dates become `%2F` (so 26/05/2026 becomes `26%2F05%2F2026`)
- Ampersands in values become `%26`
- Do not include apostrophes in any field value
- Keep notes fields concise to avoid URL length issues (under 500 chars for the notes param)

### Notes on apostrophes / single quotes

Single quotes break the PowerShell JSON body. Always replace apostrophes with a space or remove them in both formats. Example: "owners dog" not "owner's dog".

### How Claude reads the sheet

```
Tool: Google Drive: read_file_content
fileId: 1AWlrcecS7B5z_1qujwgK_bu4LKNgWM48JGrnm7Yetbk
```

Parse to find: the last PTG-XXX number, current status of any referenced client, notes, quote refs, next actions.

### Email reading via Claude in Chrome

Claude in Chrome reads Gareth's personal Outlook account (garethsomers@outlook.com) at outlook.live.com. Read all inbox and sent items for full supplier context. Open linked Xero/Quotient quotes to extract figures. Never send or delete anything.

### WhatsApp reading via Claude in Chrome

Claude in Chrome reads WhatsApp Web (web.whatsapp.com). Only read conversations with phone numbers in the tracker. Never send, delete, or reply. New enquiries added to tracker only on Gareth's explicit instruction.

---

## DEPLOY PIPELINE - AUTOMATIC ON PUSH (verified against GitHub 2026-06-04)

**Every push to main triggers the workflow automatically. No manual step required. The review step happens AFTER deploy, not before (see LIVE LINK REVIEW GATE at the top of this file).**

### How it works (ACTUAL state, verified on GitHub 2026-06-04)

```
Push/merge to main
   -> GitHub Actions triggers build-to-live.yml automatically (on: push, branches: [main])
   -> python rebuild_link_graph_v3.py wires the internal link graph
   -> Hugo --gc --minify builds site/public/ (~5,950 pages)
   -> python split_sitemap.py creates section sitemaps
   -> peaceiris/actions-gh-pages publishes site/public/ to the `live` branch (orphan)
   -> Hostinger serves the `live` branch -> live on pettransportglobal.com
   -> CLAUDE POSTS THE LIVE REVIEW LINKS IN CHAT (LIVE LINK REVIEW GATE)
```

### Which workflow is active (IMPORTANT - docs were previously backwards)

Verified on GitHub on 2026-06-04:

- **`build-to-live.yml` ("Build Hugo to live branch") is the ACTIVE pipeline.** It fires on push to main, builds Hugo, and publishes the built site to the `live` branch, which Hostinger serves. This is what actually updates the live site. It was confirmed working (the UK-to-Spain blog and the June route chunks are live via this path).
- **`deploy.yml` ("Build and Deploy to Hostinger", FTP) is DISABLED (`disabled_manually`).** It was the intended FTP-to-Hostinger pipeline but is currently switched off on GitHub. It does NOT run on push.

Earlier versions of these docs claimed the opposite (deploy.yml active, build-to-live.yml retired). That was wrong. Corrected 2026-06-04. If you want to switch the canonical pipeline back to the FTP deploy, re-enable deploy.yml in GitHub (Actions tab -> the workflow -> Enable) and disable build-to-live.yml, then update this section.

### Critical rules

- **Do not edit the `live` branch directly.** It is orphan build output, overwritten on every push to main.
- **If re-enabling the FTP deploy (deploy.yml): never delete `.ftp-deploy-sync-state.json` from Hostinger, and never set `dangerous-clean-slate: true`.**
- **Never attempt to upload the entire `site/public/` directory manually.**
- **The `.github/workflows/*.yml` files cannot be edited via the MCP connector** (GitHub returns 403). Provide the complete updated file and ask Gareth to paste it via the GitHub web editor. Enabling/disabling a workflow is done in the GitHub Actions tab, not by editing the file.

### Deploy speed expectations

| Change type | Expected deploy time |
|---|---|
| 1 new blog article | 30-60 seconds |
| 25 new route pages | 2-5 minutes |
| Template change (affects all pages) | 30-60 minutes |
| First deploy after state file deletion | Will fail. Regenerate state file first |

---

## CURRENT STATUS (keep this accurate - update on every commit)

- **Quality routes built:** 5,217 of ~37,830 country pairs (~13.8%). True on-disk count, reconciled by `verify_build_state.py`.
- **Blog articles:** 413. Content plan Days 1-5 complete. Day 6 is next (`europe-to-uk-pet-transport`).
- **Total .md source files:** 6,003 (build_state.json `total_site_pages`). Full deployed total, including Hugo taxonomy and list pages, comes from the live sitemap.xml.
- **Phase 7 route chunks:** 24 complete. Chunk 25 is next (Template C, Tier A). The 90-route P1 priority matrix is fully built; 252 score-7+ Tier A pairs remain.
- **Counts:** Never hand-edited. Run `python verify_build_state.py` to check drift, `--write` to reconcile from disk. A SessionStart hook runs the check at the start of every web session.
- **Deploy pipeline:** Automatic on push to main via `build-to-live.yml` (builds Hugo, publishes the `live` branch, Hostinger serves it). Verified on GitHub 2026-06-04. `deploy.yml` (FTP) is currently disabled. Live link review gate active.
- **GEO implementation:** All 4 phases complete (P1 Organization schema + robots, P2 universal route schema, P3 llms.txt + freshness + methodology page, P4 methodology link + airline/breed cross-links).
- **Enquiry tracker:** Live. PTG-001 to PTG-007 in sheet. Webhook v4 deployed. Both POST (desktop) and GET (mobile) confirmed working.
- **Live tracker:** [build_state.json](build_state.json)
- **Plan files:** [BUILD-PLAN.md](BUILD-PLAN.md), [cascading-build-plan-pet=transport.html](cascading-build-plan-pet=transport.html)

---

## COMMUNICATION DEFAULTS

- **No filler.** Never start with "Great question!", "Of course!", "Certainly!". Start with the answer.
- **Match length to task.** Simple question = short answer. Complex task = full answer. Never pad.
- **Show options before acting** on anything significant.
- **Admit uncertainty.** Do not invent plausible-sounding details. YMYL site. Wrong info hurts pets.
- **Use British English** in all site content.
- **When editing files that need Gareth to paste, always provide the COMPLETE file contents.**
- **No em dashes anywhere.** See EM DASH BAN section above.
- **End every build batch with the live review links.** See LIVE LINK REVIEW GATE.

---

## CLIENT COMMUNICATION TONE

All messages to clients (WhatsApp, email, cover letters) must match the tone Gareth uses: conversational, direct, warm but not cheesy. Specific rules:

- No sign-offs like "More soon", "Warm regards", "Kind regards" unless Gareth asks for them
- No filler phrases: "I wanted to flag", "I just wanted to reach out", "I hope this finds you well"
- No em dashes anywhere (see EM DASH BAN)
- Write as a person would text or email a client they have already spoken to
- Short sentences. Plain words. No fluff.

---

## REVIEW AFTER PUBLISH - NON-NEGOTIABLE

Deploy is automatic, so the review moves to after publish, not before.

**Workflow:**
1. Write the content (markdown + YAML front matter)
2. Run the full quality gate (research, voice, template rotation, humanise, QA)
3. Commit `.md` to `main` (bundled with the three docs updates)
4. Deploy fires automatically
5. **Post every new/changed live URL in chat for Gareth to review (LIVE LINK REVIEW GATE)**
6. If a problem is found on the live page, fix and re-push immediately, then post the corrected link again

(Optional, on request: for a single high-stakes article Gareth can still ask for an HTML preview before the push. Default is now push then review live.)

---

## AUTHOR PERSONAS - NON-NEGOTIABLE

**Never use Gareth's name as an author.** Use one of the personas below.

| Persona | Name | Title | Use for |
|---|---|---|---|
| **The Logistics Lead** | Marcus Webb | Senior Pet Relocation Consultant, PetTransportGlobal | Route guides, airline policies, cargo logistics, costs, quotes, process and timeline articles |
| **The Regulations Expert** | Dr. Sarah Okafor | International Animal Health Consultant, PetTransportGlobal | Country import/export guides, quarantine, titre tests, DEFRA/APHIS/DAFF, pet passports |
| **The Welfare Advisor** | Emma Hartley | Certified Animal Behaviourist & Pet Travel Adviser, PetTransportGlobal | Breed welfare, brachycephalic, anxiety, sedation, senior pets, welfare during transit |
| **The Planning Guide** | James Osei | Pet Transport Planning Specialist, PetTransportGlobal | Checklists, timelines, documentation, choosing a company, insurance, multi-pet, emergency moves |

---

## QUOTING SYSTEM

Full specification in **[quotedesign.md](quotedesign.md)** - read it before producing any quote.

### Key rules

- No client name on the quote. No Gareth's name or founder credit.
- Payment in full and upfront before any work begins.
- Default margin: 20% unless Gareth specifies otherwise.
- Split into two quotes when boarding is relevant.
- Quote reference format: `PTG-YYYYMMDD-NNN`. Valid 30 days.
- Currency: EUR for Turkey-origin. Local currency for other origins.
- Rendering: HTML to PDF via Playwright/Chromium. Use `render.py` and `measure.py` in `/home/claude/`.
- No em dashes in any quote content, ever.

### To produce a quote
1. Read [quotedesign.md](quotedesign.md).
2. Confirm margin, currency, services, origin/destination.
3. Calculate all figures.
4. Adapt last `quote.html`, update figures, ref, date, route.
5. Render, measure, visual check, present to Gareth.

---

## BEHAVIOR RULES

### Stay in scope
Only modify files directly related to the current task. Mention improvements elsewhere as a note. Do not touch them.

### The cascading build plan is law
Never bulk-generate content. One run builds a batch of 2 blocks (a block = 25 routes or one equivalent non-route unit). Floor is 1 block. Target: 50 routes per run, 100 routes per day across 2 daily runs. Each block in the batch runs the FULL quality gate independently; quality comes first, so if a run cannot finish 2 blocks cleanly it builds as many as it can do well (minimum 1), commits those, and reports the shortfall. The whole batch is committed ONCE per run (one commit, one push, one deploy). Bulk-generation scripts remain banned: a batch is still N individually quality-gated blocks, never a mass-generation script.

### Quality gate
1. Research - real regulations from data files and named sources
2. Write - load the-wordsmith.md for voice
3. Rotate templates - A to E
4. Humanise - the-chameleon.md rules
5. QA scan - the-auditor.md checks
6. Commit to main (bundled with docs update). Deploy is automatic
7. **Update BUILD-PLAN.md, build_state.json, MEMORY.md in the same commit** (see MANDATORY DOCS UPDATE)
8. **Post every new/changed live URL in chat for review, ONE LINE PER PAGE** (see LIVE LINK REVIEW GATE)
9. Stop and wait for next "go"

When a run builds a batch of 2 blocks, run the quality gate on each block, advancing the build pointer after each, then run steps 6 to 8 ONCE for the whole batch.

---

## CONTENT RULES (NON-NEGOTIABLE)

1. No safety guarantees.
2. Named, dated sources for every regulatory claim.
3. Warm, expert tone.
4. **No em dashes. Ever. Anywhere. See EM DASH BAN at the top of this file.**
5. No banned vocabulary: delve, meticulous, comprehensive, tailored, navigate, leverage, seamless, robust, vital, crucial, utilize, intricate, paramount, pivotal, embark, foster, elevate, unleash, unlock, harness, streamline, holistic, realm, landscape (figurative), testament.
6. Vary sentence rhythm.
7. Use correct author persona. Never use Gareth's name.
8. British English throughout.

---

## SEO RULES (NON-NEGOTIABLE)

- Unique `title` and `description` per page.
- One `<h1>` per page containing primary keyword.
- Target keyword in first 100 words, one H2, meta description.
- Internal links: route to origin hub + destination country guide + relevant airlines.
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
  site/content/         # All page content (routes, countries, origins, airlines, breeds, blog)
  site/layouts/         # Hugo templates
  site/static/          # CSS, JS, images, fonts
  data/                 # Source JSON for generators
  workforce/            # Worker soul files
  CLAUDE.md             # THIS FILE
  quotedesign.md        # PDF quote design spec
  BUILD-PLAN.md         # Session log + remaining tasks
  build_state.json      # Machine-readable progress
  ERRORS.md             # Failed approaches log
  MEMORY.md             # Decision log
```

---

## SESSION PROTOCOLS

### Every client enquiry interaction
1. Read the tracker sheet immediately (Google Drive connector)
2. Use sheet as source of truth for client context
3. Handle the enquiry (respond, quote, draft message, etc.)
4. End the response with BOTH the PowerShell command AND the tappable mobile link

### "go" or "next block"
1. Read BUILD-PLAN.md and build_state.json
2. Write content through full quality gate, building a batch of 2 blocks (minimum 1), advancing the build pointer after each block
3. Commit the whole batch to main once with docs update bundled in. Deploy is automatic
4. **Post every new/changed live URL in chat for review** (LIVE LINK REVIEW GATE)
5. Stop and wait

### "session end" or "wrap up"
1. Update BUILD-PLAN.md, build_state.json, MEMORY.md
2. Commit to main
3. Post the live review links for anything changed this session
4. Summarise what was built and what is next

---

## PERMANENT FACTS

- Domain: pettransportglobal.com (Hostinger). Old surge.sh references are stale.
- Slugs: lowercase, hyphen-separated, no underscores.
- Python generators at repo root, not in scripts/.
- Hugo content must live in site/content/.
- site/public/ is gitignored. Never commit build output.
- **Every push to main triggers an automatic build+publish via `build-to-live.yml` (the `live` branch, served by Hostinger). No manual trigger needed. `deploy.yml` (FTP) is currently disabled. Verified 2026-06-04.**
- **After every build batch, post the live URLs of all new/changed pages in chat for review. See LIVE LINK REVIEW GATE.**
- The active deploy workflow is build-to-live.yml (publishes the `live` branch, served by Hostinger). deploy.yml (FTP) is disabled. Verified on GitHub 2026-06-04. (Earlier docs had this backwards.)
- Do NOT delete .ftp-deploy-sync-state.json from Hostinger (only relevant if deploy.yml is re-enabled).
- FTP credentials in GitHub Secrets only. Never in chat or commits.
- .github/workflows/*.yml cannot be edited via MCP connector (403). Provide full file for Gareth to paste via GitHub web editor.
- Never use Gareth's real name as author on published content.
- Quote design is locked. See quotedesign.md.
- Enquiry tracker webhook v4 is live. Always provide both POST (desktop) and GET (mobile link) formats at the end of every client interaction.
- No em dashes anywhere, ever. See EM DASH BAN at the top of this file.
- Never send WhatsApp messages or emails without explicit instruction. Never delete anything. Read only. See WHATSAPP AND EMAIL ACCESS RULES.
- **Every commit must include a BUILD-PLAN.md + build_state.json + MEMORY.md update. See MANDATORY DOCS UPDATE.**
- **A scheduled run builds a batch of 2 blocks (minimum 1, target 50 routes = 100 per day across 2 daily runs), committed once. Bulk-generation scripts remain banned. See BEHAVIOR RULES.**

---

## WHAT TO DO WHEN STUCK

1. Re-read this file.
2. Read MEMORY.md for prior decisions.
3. Check ERRORS.md for prior failures.
4. Ask Gareth one specific question.

---

*Last updated: 2026-06-09*
