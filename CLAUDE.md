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
  - GitHub Actions (auto-build + FTP deploy)
  - Hostinger (hosting, accessed via FTP)
- **Repository:** GitHub (user is setting this up)
- **Deploy pipeline:** Push to `main` → GitHub Actions runs `hugo --gc --minify` → FTP uploads `site/public/` to Hostinger → live within ~5-10 min

---

## CURRENT STATUS (update this when it changes)

- **Routes built:** 37,832 of 37,830 country pairs (effectively complete — May 2026)
- **Total pages live:** ~38,000+ (routes + airline pages + breed guides + country guides + blog)
- **Phase 0, 1, 2 complete.** Route generation phase finished.
- **What's next:** Quality content (blog posts, deeper country guides), enquiry form, monitoring/SEO tracking
- **Live tracker:** [build_state.json](build_state.json) — machine-readable progress
- **Plan files:** [BUILD-PLAN.md](BUILD-PLAN.md), [cascading-build-plan-pet=transport.html](cascading-build-plan-pet=transport.html)

---

## COMMUNICATION DEFAULTS

- **No filler.** Never start with "Great question!", "Of course!", "Certainly!". Start with the answer.
- **Match length to task.** Simple question → short answer. Complex task → full answer. Never pad.
- **Show options before acting** on anything significant (new feature, structural change, new file type). Give 2-3 approaches, wait for choice.
- **Admit uncertainty.** If you don't know whether a regulation, airline policy, or technical fact is current, say so. Do not invent plausible-sounding details. YMYL site — wrong info hurts pets.
- **Match Gareth's voice in any user-facing copy** (see Content Rules below).
- **Use British English** in all site content (the site targets UK/AU/NZ primarily, plus US — but voice is British).

---

## BEHAVIOR RULES

### Stay in scope
- Only modify files, functions, and lines directly related to the current task.
- Do not refactor, rename, reformat, or "improve" anything not asked for.
- If you notice something worth fixing elsewhere, mention it at the end in a note. Do not touch it.

### Confirm only for destructive actions
Auto-proceed for: writing new files, editing files in scope, running generators, committing, **pushing to `main`** (this triggers auto-deploy — that's intended).

Stop and ask explicit confirmation for:
- Deleting files or directories
- `git reset --hard`, `git push --force`, rewriting history
- Dropping data files or overwriting `data/*.json`
- Removing dependencies
- Changing deploy pipeline (`.github/workflows/deploy.yml`)
- Modifying Hostinger FTP secrets
- Mass content deletion or rewriting (>5 files of existing live content)

### Always show what changed
After any coding/content task, end with:
- **Files changed:** (list)
- **What was modified:** (one line per file)
- **Live URL impact:** (which pages will update after auto-deploy)
- **Follow-up needed:** (if any)

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
7. **Author attribution.** All route/country/airline/breed pages credit "Gareth, Founder, PetTransportGlobal". Trust signals matter.
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
- **CI/CD:** GitHub Actions
- **Deploy:** FTP to Hostinger via `SamKirkland/FTP-Deploy-Action@v4.3.5`
- **Hosting:** Hostinger shared hosting
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
├── .github/workflows/deploy.yml   # CI/CD pipeline
├── generate_*.py                  # Python generators (repo root)
├── CLAUDE.md                      # THIS FILE
├── WORKFLOW.md                    # Step-by-step session guide
├── BUILD-PLAN.md                  # Session log + remaining tasks
├── build_state.json               # Machine-readable progress
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

### When Gareth says "go" or "next task"
1. Read [BUILD-PLAN.md](BUILD-PLAN.md) and [build_state.json](build_state.json)
2. Identify the next TODO
3. State what you're about to do
4. Do it
5. Commit + push (auto-deploys)
6. Summarise in plain English

### When Gareth says "session end" or "wrap up"
1. Update [BUILD-PLAN.md](BUILD-PLAN.md) with a session log entry: date, what was done, files changed, page count, next priority
2. Update [build_state.json](build_state.json) with current counts
3. Update [MEMORY.md](MEMORY.md) if any significant decision was made
4. Commit + push
5. Summarise: what's now live, what's queued for next session

### When something takes >2 attempts
Log it. Append to `ERRORS.md` (create if missing):
- What didn't work
- What worked instead
- Note for next time

Check `ERRORS.md` before suggesting approaches to similar tasks.

### When a decision is made
Append to [MEMORY.md](MEMORY.md):
- What was decided
- Why
- What was rejected and why

Never contradict a logged decision without flagging it first.

---

## DEPLOY PIPELINE (HOW IT WORKS)

```
You / Claude edits files
   ↓
git commit + git push to main
   ↓
GitHub Actions triggers (~10 sec)
   ↓
hugo --gc --minify (builds site/public/)
   ↓
python split_sitemap.py (creates section sitemaps)
   ↓
FTP-Deploy-Action uploads site/public/ → Hostinger /public_html/
   ↓
Live on pettransportglobal.com (~5-10 min total)
```

**You do not need to run Hugo locally.** Pushing to `main` is the deploy. Full guide: [WORKFLOW.md](WORKFLOW.md).

---

## WORKER SOULS (DOMAIN EXPERTS)

Reference these files when working in their domain. Don't load them all every session — load only what's needed for the current task.

| Worker | Domain | File |
|--------|--------|------|
| The Architect | Orchestration, phase planning | [workforce/leadership/the-architect.md](workforce/leadership/the-architect.md) |
| The Auditor | YMYL compliance, QA | [workforce/leadership/the-auditor.md](workforce/leadership/the-auditor.md) |
| The Wordsmith | Copywriting, voice | [workforce/content/the-wordsmith.md](workforce/content/the-wordsmith.md) |
| The Chameleon | Anti-AI humaniser (mandatory on all content) | [workforce/content/the-chameleon.md](workforce/content/the-chameleon.md) |
| The Interrogator | FAQ generation | [workforce/content/the-interrogator.md](workforce/content/the-interrogator.md) |
| The Geographer | Country regulations, quarantine | [workforce/intelligence/the-geographer.md](workforce/intelligence/the-geographer.md) |
| The Scout | Keyword research | [workforce/intelligence/the-scout.md](workforce/intelligence/the-scout.md) |
| The Spider | Web scraping | [workforce/intelligence/the-spider.md](workforce/intelligence/the-spider.md) |
| The Builder | Hugo templates, generation | [workforce/development/the-builder.md](workforce/development/the-builder.md) |
| The Librarian | Data management | [workforce/development/the-librarian.md](workforce/development/the-librarian.md) |
| The Optimiser | On-page SEO, schema | [workforce/seo/the-optimiser.md](workforce/seo/the-optimiser.md) |
| The Connector | Internal linking | [workforce/seo/the-connector.md](workforce/seo/the-connector.md) |
| The Analyst | Performance tracking | [workforce/monitoring/the-analyst.md](workforce/monitoring/the-analyst.md) |
| The Watchdog | Site health | [workforce/monitoring/the-watchdog.md](workforce/monitoring/the-watchdog.md) |

---

## PERMANENT FACTS (ALWAYS TRUE — APPLY EVERY SESSION)

- Domain is **pettransportglobal.com** (Hostinger). Old surge.sh references in `MEMORY.md` are stale.
- Slugs are lowercase, hyphen-separated, no underscores.
- All Python generators live at the **repo root**, not in `scripts/`.
- Hugo content **must** live in `site/content/`. Anything outside is invisible to the build.
- `site/public/` is **gitignored** — never commit build output.
- `data/*.json` files are source of truth — flag before editing.
- GitHub Actions deploys on push to `main`. There is no manual upload step.
- Hostinger FTP credentials live in GitHub Secrets (`FTP_SERVER`, `FTP_USERNAME`, `FTP_PASSWORD`). Never paste these into chat or commit them.
- The site has a template originally in `template-source/`. That directory is reference only — do not edit, do not delete.

---

## WHAT TO DO WHEN YOU'RE STUCK

1. Re-read this file.
2. Read [MEMORY.md](MEMORY.md) for prior decisions.
3. Check [ERRORS.md](ERRORS.md) for prior failures on similar tasks.
4. Ask Gareth one specific question. Do not present a wall of options.

---

*Last updated: 2026-05-22*
