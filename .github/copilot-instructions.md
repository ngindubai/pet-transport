# PetTransportGlobal — Copilot Instructions

## Site Identity
- This is a programmatic SEO lead generation website for international pet transport services.
- Primary goal: capture enquiries from pet owners relocating internationally, via organic search.
- Domain: pettransportglobal.surge.sh (live) / target custom domain TBD
- Tech stack: Hugo (static site generator), Python generation scripts, surge.sh deployment
- Build command: `hugo --gc --minify` from within `site/`
- Deployment: `surge public pettransportglobal.surge.sh` from within `site/`
- Live URL: pettransportglobal.surge.sh

## Project Status
- 202 pages live. Phase 0 (research), Phase 1 (P1 routes, templates, hubs, guides), and Phase 2 blocks 20-21 (airline + breed guides) are all COMPLETE.
- Do NOT restructure existing files, change naming conventions, or alter existing content unless explicitly asked.
- The primary build tracker is `cascading-build-plan-pet=transport.html`. Always check it before starting any build task.
- `BUILD-PLAN.md` mirrors remaining tasks. Both files must be updated at the end of every session.
- Next stage: Block 22 — Phase 2.1 (P2 country regulation data) + 2.2 (P2 route pages).

## Directory Structure
- Site Hugo root: `site/`
- Content files: `site/content/` (subdirs: routes/, countries/, origins/, airlines/, breeds/, blog/, resources/)
- Templates: `site/layouts/`
- Static assets: `site/static/`
- Research data (JSON): `data/`
- Python scripts (root level): `assemble_routes.py`, `generate_airline_pages.py`, `generate_breed_pages.py`, `generate_content.py`, `generate_country_content.py`, `generate_hubs.py`, etc.
- Worker soul files: `workforce/`
- Build plan: `cascading-build-plan-pet=transport.html`

## Content Rules (Non-Negotiable)
1. **YMYL compliance.** This is a Your Money or Your Life site for pets. Safety, veterinary, and regulatory claims require named, dated sources. Author attribution and trust signals are mandatory.
2. **No safety guarantees.** Never promise an animal will arrive safely or without stress. "Experienced handlers", "IATA-compliant crates", and "we reduce risk" are acceptable.
3. **Reassuring, not clinical.** Pet owners are anxious about shipping their animals. Tone is warm, practical, and expert. Not corporate, not bureaucratic. "Your dog needs a rabies titre test at least 3 months before travel" not "Rabies FAVN test per OIE standard required 90 days pre-export."
4. **Humaniser rules active.** Apply the 24 anti-AI patterns from `workforce/content/the-chameleon.md`. No banned vocabulary. No em dashes. Vary sentence rhythm.
5. **Route pages must feel unique.** With 5,000+ eventual route pages, no two pages should read like a find-and-replace job. Vary structure, anecdotes, and sentence patterns per route.
6. **Source attribution.** Every regulatory claim cites a named, dated official source (USDA APHIS, UK APHA, Australian DAFF, EU TRACES, etc.).

## SEO Requirements (Non-Negotiable)
- Every page must have a unique `title` and `description` in front matter.
- Route page title formula: `Pet Transport [Origin] to [Destination] | [Brand]` (rotate alternates to avoid duplication).
- Meta description: 140-160 characters, includes a reassurance hook and call to action.
- H1: exactly one per page, contains primary keyword (e.g. "Pet Transport from UK to Australia").
- Target keyword in: first 100 words, one H2, meta description.
- Internal links: route pages link to origin country hub + destination country guide + relevant airline pages.
- FAQ schema JSON-LD required on all route, country, airline, and breed pages.
- No duplicate content across route combinations.

## Code and Template Conventions
- Front matter: YAML format between `---` delimiters (check existing files before assuming format).
- Route pages: `site/content/routes/[origin-slug]-to-[destination-slug].md`
- Country guides: `site/content/countries/[country-slug].md`
- Origin hubs: `site/content/origins/[country-slug].md`
- Airline pages: `site/content/airlines/[airline-slug].md`
- Breed pages: `site/content/breeds/[breed-slug].md`
- All slugs: lowercase, hyphen-separated, no underscores.
- Do not extend or rewrite existing layouts without checking the current template first.
- Python scripts at the repo root generate Hugo markdown programmatically — always use skip-if-exists logic.

## Worker Souls
14 specialist workers are defined in `workforce/`. Reference them for their domain:
- The Architect (`workforce/leadership/`): orchestration and planning
- The Auditor (`workforce/leadership/`): YMYL compliance, regulatory accuracy, QA
- The Wordsmith (`workforce/content/`): copywriting, warm-expert voice
- The Chameleon (`workforce/content/`): anti-AI humanisation — reference for banned vocabulary
- The Interrogator (`workforce/content/`): FAQ generation
- The Geographer (`workforce/intelligence/`): route regulations, quarantine rules, country data
- The Scout (`workforce/intelligence/`): keyword research
- The Builder (`workforce/development/`): Hugo templates, page generation, deployment
- The Librarian (`workforce/development/`): data management, route JSON assembly
- The Optimiser (`workforce/seo/`): on-page SEO, schema markup
- The Connector (`workforce/seo/`): internal linking, link graph
- The Analyst (`workforce/monitoring/`): performance tracking
- The Watchdog (`workforce/monitoring/`): site health monitoring

## Data Files
| File | Contains |
|------|----------|
| `data/airline_pet_policies.json` | 23 airline pet cargo/cabin policies, crate reqs, breed restrictions |
| `data/breed_restrictions.json` | Breed bans per country + brachycephalic airline restrictions |
| `data/countries_pet_regulations.json` | Pet import/export rules, quarantine, vaccines for P1 countries |
| `data/govt_import_regulations.json` | Official government regulatory data (USDA, APHA, DAFF, etc.) |
| `data/route_keyword_matrix.json` | Keyword clusters per P1 route, volumes, SERP context |
| `data/schema_and_tech_stack.json` | Hugo architecture, schema patterns |
| `data/competitors/` | PetRelocation.com analysis and competitor structure |

## Deployment
- Surge.sh: `surge public pettransportglobal.surge.sh` from `site/` directory
- The subagent cannot handle interactive Surge login. Always deploy from the main terminal.

## Communication Rules
- Always state what you are about to do before doing it.
- If a task is ambiguous, ask one clarifying question before proceeding.
- When you complete a task, summarise: what was done, what files changed, and what comes next.
- **End of every session:** update `BUILD-PLAN.md` AND `cascading-build-plan-pet=transport.html` to reflect what was completed. Add a session log entry to `BUILD-PLAN.md`.
