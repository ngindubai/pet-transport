---
description: "Execute the next stage of the pet-transport website build. Reads the build plan, finds the next TODO block, loads relevant worker souls and data, generates all deliverables, marks the block DONE. Use when: building the next chunk, executing next stage, continuing the build, 'go', 'next'."
agent: "agent"
---

# Build Next Stage — PetTransportGlobal

You are executing the next build block for a programmatic SEO website targeting international pet transport route pages.

## Step 1: Read the Build Plan

Open `cascading-build-plan-pet=transport.html` and find the execution stages table. Identify the first block with a `TODO` badge.

If a block is `IN PROGRESS`, resume it instead.

Record:
- Block number (e.g. Block 22)
- Task numbers it covers (e.g. 2.1, 2.2)
- Description and expected outputs
- Dependencies and which workers are active

Also read `BUILD-PLAN.md` for the current session log and remaining checklist.

## Step 2: Load Worker Souls

Load only the workers needed for this block. Paths are relative to the repo root.

| Worker | Path | Load for blocks involving... |
|--------|------|------|
| The Builder | `workforce/development/the-builder.md` | Hugo templates, page generation, deployment |
| The Wordsmith | `workforce/content/the-wordsmith.md` | Any content writing |
| The Chameleon | `workforce/content/the-chameleon.md` | ALL content blocks (humaniser pass mandatory) |
| The Interrogator | `workforce/content/the-interrogator.md` | FAQ generation |
| The Geographer | `workforce/intelligence/the-geographer.md` | Route regulations, quarantine, country data |
| The Librarian | `workforce/development/the-librarian.md` | Route JSON assembly, data management |
| The Optimiser | `workforce/seo/the-optimiser.md` | SEO metadata, schema markup |
| The Connector | `workforce/seo/the-connector.md` | Internal linking, link graph |
| The Auditor | `workforce/leadership/the-auditor.md` | QA, YMYL compliance, regulatory accuracy |
| The Architect | `workforce/leadership/the-architect.md` | Planning, orchestration |
| The Scout | `workforce/intelligence/the-scout.md` | Keyword research |
| The Spider | `workforce/intelligence/the-spider.md` | Web scraping, regulatory data extraction |
| The Analyst | `workforce/monitoring/the-analyst.md` | Analytics, performance tracking |
| The Watchdog | `workforce/monitoring/the-watchdog.md` | Site health monitoring |

## Step 3: Load Research Data

| Data | Path | Use for |
|------|------|---------|
| Country regulations (P1) | `data/countries_pet_regulations.json` | Import/export rules, quarantine, vaccines |
| Government regulations | `data/govt_import_regulations.json` | Official regulatory data (USDA, APHA, DAFF) |
| Airline policies | `data/airline_pet_policies.json` | Cabin/cargo policies, crate requirements, breed restrictions |
| Breed restrictions | `data/breed_restrictions.json` | Country bans + brachycephalic airline data |
| Keyword matrix | `data/route_keyword_matrix.json` | Target keywords per P1 route, volumes, SERP context |
| Schema + tech stack | `data/schema_and_tech_stack.json` | Hugo architecture, schema patterns |
| Competitor analysis | `data/competitors/` | PetRelocation.com structure and gaps |

## Step 4: Mark IN PROGRESS

Update `cascading-build-plan-pet=transport.html`: change the block badge from `TODO` to `IN PROGRESS`.

## Step 5: Execute

### Content Rules
- Tone: warm, practical, expert. Pet owners are anxious. Reassure, don't alarm.
- No banned vocabulary: delve, tapestry, vibrant, crucial, comprehensive, meticulous, embark, robust, seamless, groundbreaking, leverage, synergy, transformative, paramount, multifaceted, myriad, cornerstone, reimagine, empower, catalyst, invaluable, bustling, nestled, realm
- No em dashes (zero tolerance)
- No safety guarantees. "Experienced handlers" and "IATA-compliant" only.
- Source attribution. Every regulatory claim cites a named, dated official source.
- Vary sentence rhythm. Short. Then longer ones. High burstiness.
- Route pages must feel unique — not find-and-replace.
- British English throughout.

### SEO Rules
- Unique title and meta per page
- FAQ schema JSON-LD on all route, country, airline, breed pages
- Route pages link to origin hub + destination guide + airline pages
- Minimum 2 internal links with descriptive anchor text

### File Output
- Hugo content: `site/content/[section]/[slug].md`
- Python scripts at repo root — all must use skip-if-exists logic
- Build command: `hugo --gc --minify` from `site/`
- Deploy: `surge public pettransportglobal.surge.sh` from `site/`

## Step 6: Mark DONE

1. Update `cascading-build-plan-pet=transport.html`: change block badge to `DONE`.
2. Update `BUILD-PLAN.md`: tick off the completed stage, add session log entry.
3. Run `hugo --gc --minify` from `site/` to confirm 0 errors.
4. Report what was built and any issues found.

## Important Notes
- **89 P1 routes complete.** 10x10 country pair matrix (UK, UAE, AU, USA, SG, FR, HK, SA, DE, NL).
- **23 airline pages live.** pettransportglobal.surge.sh/airlines/
- **35 breed pages live.** pettransportglobal.surge.sh/breeds/
- **Surge deploy:** Cannot handle interactive Surge login in subagent. Deploy from main terminal only.
- **Anti-template gate:** No two route pages should feel like a find-and-replace job. The Chameleon pass is mandatory.
