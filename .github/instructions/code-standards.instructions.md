---
applyTo: "**/*.py, **/*.md"
---

# Code Standards — PetTransportGlobal

## Python Generation Scripts
- All scripts at repo root (e.g. `assemble_routes.py`, `generate_breed_pages.py`)
- Every script must use skip-if-exists logic: `if os.path.exists(path): continue`
- Output goes to `site/content/[section]/`
- After running any script, run `hugo --gc --minify` from `site/` to verify 0 errors before deploying

## Hugo Content
- Front matter: YAML between `---` delimiters
- Slugs: lowercase, hyphen-separated, no underscores, no spaces
- Route slug pattern: `[origin-country]-to-[destination-country]` e.g. `uk-to-australia`
- Always check an existing file in the same section before creating new content

## Hugo Layouts
- Extend existing layouts in `site/layouts/` — do not rewrite base templates
- No inline CSS — use existing CSS classes from `site/static/css/`
- Do not create new top-level directories without asking first

## General
- Do NOT restructure existing files or change conventions already in use
- Do NOT add features beyond what was asked
- Do NOT rename files that already exist and are deployed
