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

The solution is the `.ftp-deploy-sync-state.json` file on Hostinger. This file tracks what's already deployed. The FTP Deploy Action reads it, diffs against the local build, and only uploads files that changed. A single new blog article deploys in under 60 seconds.

The state file was bootstrapped by `generate_ftp_state.py` which runs automatically on first deploy (when no state file exists on the server). After the first successful deploy, the FTP action manages the state file itself.

### Critical rules

- **Never delete `.ftp-deploy-sync-state.json` from Hostinger.** If deleted, the next deploy attempts a full upload which will fail.
- **Never set `dangerous-clean-slate: true`** in the workflow. This wipes all files on Hostinger including the state file.
- **Never attempt to upload the entire `site/public/` directory manually or via a script.** Always use the incremental FTP action via GitHub Actions.
- **The `.github/workflows/deploy.yml` file cannot be edited via the MCP connector** (GitHub returns 403). If the workflow needs changes, provide the complete updated file contents and ask Gareth to paste it via the GitHub web editor.

### Deploy speed expectations

| Change type | Expected deploy time |
|---|---|
| 1 new blog article | 30–60 seconds |
| 25 new route pages | 2–5 minutes |
| Template change (affects all pages) | 30–60 minutes (re-uploads all changed HTML) |
| First deploy after state file deletion | Will fail — regenerate state file first |

---

## CURRENT STATUS (update this when it changes)

- **Quality routes built:** 5,461 of 37,830 country pairs (~14%). Each has unique researched content, one of 5 template variants (A–E), 1,500+ words, regulatory specifics.
- **Remaining:** 32,369 routes to be built block-by-block per the cascading build plan.
- **Blog:** 411 articles (409 existing + 2 content plan articles: Day 1 and Day 2).
- **Content plan:** 252 new articles, Jun 2026 – May 2027. Days 1–2 published. Day 3 is next.
- **Deploy pipeline:** Working. Incremental FTP via GitHub Actions. Tested and confirmed 2026-05-22.
- **Live tracker:** [build_state.json](build_state.json) — machine-readable progress
- **Plan files:** [BUILD-PLAN.md](BUILD-PLAN.md), [cascading-build-plan-pet=transport.html](cascading-build-plan-pet=transport.html)

---

## COMMUNICATION DEFAULTS

- **No filler.** Never start with "Great question!", "Of course!", "Certainly!". Start with the answer.
- **Match length to task.** Simple question → short answer. Complex task → full answer. Never pad.
- **Show options before acting** on anything significant (new feature, structural change, new file type). Give 2-3 approaches, wait for choice.
- **Admit uncertainty.** If you don't know whether a regulation, airline policy, or technical fact is current, say so. Do not invent plausible-sounding details. YMYL site — wrong info hurts pets.
- **Use British English** in all site content (the site targets UK/AU/NZ primarily, plus US — but voice is British).
- **When editing files that need Gareth to paste (e.g. deploy.yml), always provide the COMPLETE file contents.** Never give partial diffs or "find and replace this line" instructions. Full file, every time.

---

## REVIEW BEFORE PUBLISH — NON-NEGOTIABLE

**Every blog article or page must be presented as a rendered HTML file for review before it is committed to the repo.**

The HTML preview must:
- Replicate the actual site design faithfully: real nav (with logo, megamenus), real footer, real CSS classes from the template
- Render the article body exactly as it will appear on the live site (h1, h2, h3, paragraphs, tables, blockquotes, author byline)
- Include the author byline block (name, title, date) styled to match the site
- Be delivered as a downloadable `.html` artifact so Gareth can open it in a browser
- Not use placeholder text or lorem ipsum anywhere

**Workflow:**
1. Write the article (markdown content + YAML front matter)
2. Build the standalone HTML preview using the site's actual nav/footer/CSS structure
3. Present the HTML file as an artifact for Gareth to open and review
4. Wait for explicit approval ("publish it" or feedback on what to change)
5. Only after approval: commit the `.md` file directly to `main` (triggers auto-deploy)

---

## AUTHOR PERSONAS — NON-NEGOTIABLE

**Never use Gareth's name as an author on any page or article.** Use one of the personas below instead, matched to the topic cluster. These are the editorial voices of PetTransportGlobal. Each has a specialism that signals topical authority.

| Persona | Name | Title | Use for |
|---|---|---|---|
| **The Logistics Lead** | Marcus Webb | Senior Pet Relocation Consultant, PetTransportGlobal | Route guides, airline policies, cargo logistics, costs and quotes, process and timeline articles |
| **The Regulations Expert** | Dr. Sarah Okafor | International Animal Health Consultant, PetTransportGlobal | Country import/export guides, quarantine rules, titre tests, DEFRA/APHIS/DAFF regulatory content, pet passports and health certificates |
| **The Welfare Advisor** | Emma Hartley | Certified Animal Behaviourist & Pet Travel Adviser, PetTransportGlobal | Breed welfare guides, brachycephalic restrictions, anxiety and sedation, senior and anxious pets, welfare during transit |
| **The Planning Guide** | James Osei | Pet Transport Planning Specialist, PetTransportGlobal | Checklists, timelines, documentation prep, choosing a transport company, insurance, multi-pet moves, emergency and urgent moves |

**Assignment rules:**
- Match the persona to the dominant topic of the article. If in doubt, use Marcus Webb (the general logistics lead).
- A single article always has one author. Do not list two personas.
- Use the full name and title in the byline: e.g. `Marcus Webb — Senior Pet Relocation Consultant, PetTransportGlobal`
- The persona name appears in the YAML front matter as `author:` and in the visible byline on the page.
- These personas are consistent across all 252 content plan articles and all future content. Do not invent new personas.

---

## BEHAVIOR RULES

### Stay in scope
- Only modify files, functions, and lines directly related to the current task.
- Do not refactor, rename, reformat, or "improve" anything not asked for.
- If you notice something worth fixing elsewhere, mention it at the end in a note. Do not touch it.

### The cascading build plan is law
- **Never bulk-generate content.** No "generate all remaining routes" scripts. No mass `for country in countries: write_page()` loops. Bulk generation is what produces thin, indistinguishable, AI-detectable content that gets the whole site penalised.
- Work happens **one block at a time**, from the cascading build plan ([cascading-build-plan-pet=transport.html](cascading-build-plan-pet=transport.html) + [BUILD-PLAN.md](BUILD-PLAN.md)).
- A **block = 25 routes** (or one equivalent unit of work for non-route blocks like a country guide, an airline policy update, a blog post).
- Each block follows the **quality gate** (see below). No shortcuts.
- When Gareth says **"go"** or **"next block"**: read the build plan, identify the next block, execute it fully through every gate, then stop and wait.

### Quality gate (every block, no exceptions)
1. **Research** — pull actual current regulations from `data/*.json` and named agency sources. If data is missing or stale, flag it and stop. Never invent.
2. **Write** — load `the-wordsmith.md` for voice. Each page is genuinely different in structure, examples, opening, and detail focus. No template-filled paragraphs.
3. **Rotate templates** — assign one of 5 variants (A–E) across the block so consecutive routes don't look identical.
4. **Humanise** — run the content mentally through `the-chameleon.md` rules (sentence rhythm, banned vocab, no em dashes, varied openings).
5. **QA scan** — `the-auditor.md` checks: YMYL claims sourced, no safety guarantees, regulatory accuracy, British English, word count threshold (1,200+ for routes).
6. **HTML preview** — build the standalone HTML preview and present it to Gareth for approval before committing.
7. **Commit directly to `main`** only after Gareth approves the preview. This triggers the incremental deploy automatically.
8. **Stop.** Do not auto-continue to the next block. Wait for Gareth's next "go".

### Confirm only for destructive actions
Auto-proceed for: writing new files, editing files in scope, committing approved content to `main`.

Stop and ask explicit confirmation for:
- Deleting files or directories
- `git reset --hard`, `git push --force`, rewriting history
- Dropping data files or overwriting `data/*.json`
- Removing dependencies
- Changing deploy pipeline (`.github/workflows/deploy.yml`)
- Modifying Hostinger FTP secrets
- Any generator script that would write more than 25 pages in one run

### Always show what changed
After any block, end with:
- **Block:** (e.g. "Blog Day 2: Cost guide" or "Routes 5,148–5,172: UK → 25 EU destinations")
- **Files changed:** (list)
- **Quality gates passed:** (research / write / template rotation / humanise / QA / HTML preview)
- **Word count range:** (e.g. 1,420 – 1,890)
- **Committed to main:** (commit SHA or link)
- **Live URL:** (the page URL on pettransportglobal.com)
- **Actions run:** (link to the GitHub Actions run to monitor deploy)
- **Next block in plan:** (preview of what "go" will do)

### Think before you write code
For architecture, debugging, or non-trivial features: work through the problem step by step before writing code. Show reasoning. Flag uncertainty. Then implement.

---

## CONTENT RULES (NON-NEGOTIABLE)

This is a **YMYL** site (Your Money or Your Life — pets). Wrong information harms animals.

1. **No safety guarantees.** Never promise an animal will arrive safely or stress-free. Allowed: "experienced handlers", "IATA-compliant crates", "reduce risk", "follow regulations".
2. **Named, dated sources for every regulatory claim.** USDA APHIS, UK APHA, Australian DAFF, EU TRACES, etc. Cite the agency.
3. **Warm, expert tone — not clinical, not corporate.** Pet owners are anxious. "Your dog needs a rabies titre test at least 3 months before travel" not "Rabies FAVN test per OIE standard required 90 days pre-export."
4. **No em dashes.** Use commas, full stops, or "and".
5. **No banned vocabulary:** delve, meticulous, comprehensive, tailored, navigate, leverage, seamless, robust, vital, crucial, utilize, intricate, paramount, pivotal, embark, foster, elevate, unleash, unlock, harness, streamline, holistic, ensure (overused), realm, landscape (figurative), testament.
6. **Vary sentence rhythm.** Mix short and long. Don't start consecutive sentences the same way. Don't use the same paragraph structure across route pages — these are 38,000 pages of pet transport routes, none should read like find-and-replace.
7. **Author attribution.** Use the correct persona from the Author Personas section above. Never use Gareth's name. Never use a real person's name that is not listed as a persona.
8. **British English.** Colour, organise, kerb, behaviour, recognise. (Quotes from US sources stay in US English.)

Full anti-AI rules: [workforce/content/the-chameleon.md](workforce/content/the-chameleon.md)
Voice guide: [workforce/content/the-wordsmith.md](workforce/content/the-wordsmith.md)

---

## SEO RULES (NON-NEGOTIABLE)

- Every page: unique `title` and `description` in YAML front matter.
- Route page title: `Pet Transport [Origin] to [Destination] | PetTransportGlobal` (rotate variants to avoid duplicates).
- Meta description: 140-160 chars, reassurance hook + call to action.
- One `<h1>` per page, contains primary keyword.
- Target keyword in: first 100 words, one H2, meta description.
- Internal links: route page → origin hub + destination country guide + relevant airlines.
- FAQ schema (JSON-LD) auto-generated by Hugo template from `faqs:` front matter.
- No duplicate content across routes.

---

## TECH STACK (LOCKED — DO NOT SUGGEST ALTERNATIVES)

- **Static site generator:** Hugo v0.160.1-extended
- **Templating:** Go templates (Hugo's native)
- **Content language:** Markdown + YAML front matter
- **Generators:** Python 3.11 (no other language)
- **CI/CD:** GitHub Actions (incremental FTP deploy)
- **Deploy:** `SamKirkland/FTP-Deploy-Action@v4.3.5` with `.ftp-deploy-sync-state.json` for incremental uploads
- **State file generator:** `generate_ftp_state.py` (bootstraps the state file on first deploy)
- **Hosting:** Hostinger shared hosting (FTP, port 21, IP in GitHub Secrets)
- **No JS frameworks. No React. No Next.js. No Tailwind build step.** Site uses the existing template's vanilla CSS/JS in `site/static/`.

If a task seems to need a different tool, flag it and explain why. Use the locked stack unless Gareth explicitly approves an addition.

---

## DIRECTORY STRUCTURE

```
pet-transport/
├── site/                          # Hugo root
│   ├── content/                   # All page content
│   │   ├── routes/                # 37,830+ route pages
│   │   ├── countries/             # Destination guides
│   │   ├── origins/               # Origin hubs
│   │   ├── airlines/              # Airline policy pages
│   │   ├── breeds/                # Breed transport guides
│   │   ├── blog/                  # Articles
│   │   └── resources/             # Resource pages
│   ├── layouts/                   # Hugo templates
│   ├── static/                    # CSS, JS, images, fonts
│   └── public/                    # Hugo build output (gitignored)
├── data/                          # Source JSON for generators
├── workforce/                     # Worker soul files (domain experts)
├── .github/workflows/deploy.yml   # CI/CD pipeline (auto-deploys on push to main)
├── generate_*.py                  # Python generators (repo root) — per-block use only
├── generate_ftp_state.py          # FTP state file bootstrapper (runs on first deploy only)
├── split_sitemap.py               # Splits Hugo sitemap into section sitemaps
├── CLAUDE.md                      # THIS FILE
├── WORKFLOW.md                    # Step-by-step session guide
├── BUILD-PLAN.md                  # Session log + remaining tasks
├── build_state.json               # Machine-readable progress
├── ERRORS.md                      # Failed approaches log
└── MEMORY.md                      # Decision log (read at session start)
```

---

## KEY DATA FILES

| File | Contents |
|------|----------|
| `data/countries_pet_regulations.json` | Pet import/export rules per country |
| `data/govt_import_regulations.json` | Official agency regulations |
| `data/airline_pet_policies.json` | 23+ airline pet cargo/cabin policies |
| `data/breed_restrictions.json` | Breed bans + brachycephalic airline rules |
| `data/route_keyword_matrix.json` | SEO keyword clusters per route |

Treat these as **source of truth**. Do not edit without explicit approval — they feed every generated page.

---

## SESSION PROTOCOLS

### When Gareth says "go" or "next block"
1. Read [BUILD-PLAN.md](BUILD-PLAN.md) and [build_state.json](build_state.json) and the content plan
2. Identify the next article or block
3. Write the content following the full quality gate
4. Build the HTML preview and present it for review. Stop and wait for approval.
5. After approval: commit directly to `main`. Deploy triggers automatically.
6. Provide the live URL and the Actions run link so Gareth can verify.
7. **Stop.** Wait for Gareth's next "go".

### When Gareth says "session end" or "wrap up"
1. Update [BUILD-PLAN.md](BUILD-PLAN.md) with a session log entry
2. Update [build_state.json](build_state.json) with current counts
3. Update [MEMORY.md](MEMORY.md) if any significant decision was made
4. Commit to main
5. Summarise: what was built, what's queued, what's next

### When something takes >2 attempts
Log it in [ERRORS.md](ERRORS.md). Check `ERRORS.md` before suggesting approaches to similar tasks.

### When a decision is made
Append to [MEMORY.md](MEMORY.md). Never contradict a logged decision without flagging it first.

---

## WORKING FROM THE CLAUDE APP (PHONE / TABLET / REMOTE)

This is the primary workflow. Gareth works from iPad, iPhone, or any device using the Claude app or claude.ai. No desktop or VS Code required.

The GitHub MCP connector is active on this project and has write access to the repo (except `.github/workflows/` which requires manual editing via GitHub web UI).

**The daily content loop:**
1. Gareth says **"go"** — Claude reads the content plan, writes the next article, produces the HTML preview
2. Gareth opens the HTML preview in a browser and reviews design + content
3. Gareth says **"publish it"** — Claude commits the `.md` directly to `main`
4. GitHub Actions builds Hugo and deploys only the new/changed files to Hostinger (under 60 seconds)
5. Claude provides the live URL and Actions link for Gareth to verify
6. Done. Say "go" again for the next article.

**No branches or PRs needed for single articles.** Commit directly to `main` for speed. The incremental deploy only uploads changed files, so a bad article can be fixed by committing a correction (which also deploys in under 60 seconds).

---

## PERMANENT FACTS (ALWAYS TRUE — APPLY EVERY SESSION)

- Domain is **pettransportglobal.com** (Hostinger). Old surge.sh references in `MEMORY.md` are stale.
- Slugs are lowercase, hyphen-separated, no underscores.
- All Python generators live at the **repo root**, not in `scripts/`.
- Hugo content **must** live in `site/content/`. Anything outside is invisible to the build.
- `site/public/` is **gitignored** — never commit build output.
- `data/*.json` files are source of truth — flag before editing.
- **Every push to `main` auto-deploys to Hostinger** via incremental FTP. Only changed files are uploaded.
- **Do NOT delete `.ftp-deploy-sync-state.json` from Hostinger.** It tracks deployed files. Deleting it forces a full re-upload which will fail.
- Hostinger FTP credentials live in GitHub Secrets (`FTP_SERVER`, `FTP_USERNAME`, `FTP_PASSWORD`). Never paste these into chat or commit them.
- **`.github/workflows/deploy.yml` cannot be edited via the MCP connector** (GitHub 403). Always provide full file contents for Gareth to paste via the GitHub web editor.
- The site has a template originally in `template-source/`. That directory is reference only — do not edit, do not delete.
- The GitHub MCP connector has write access to this repo (except workflow files).
- **Never use Gareth's real name as an author on any published content.** Use the author personas defined above.

---

## WHAT TO DO WHEN YOU'RE STUCK

1. Re-read this file.
2. Read [MEMORY.md](MEMORY.md) for prior decisions.
3. Check [ERRORS.md](ERRORS.md) for prior failures on similar tasks.
4. Ask Gareth one specific question. Do not present a wall of options.

---

*Last updated: 2026-05-22*
