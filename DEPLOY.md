# PetTransportGlobal — Deployment Log

## Active workflow
`build-to-live.yml` — builds Hugo on every push to main, pushes compiled output to `live` branch. Hostinger Git OAuth watches `live` and deploys automatically.

## Previous workflow
`deploy.yml` — FTP-based, now disabled. Left in place for reference only.

## What is in the live branch
The compiled Hugo site: all HTML, CSS, JS, sitemaps. No source files, no Python scripts, no YAML.

## Route build state
See `build_state.json` for current route count and chunk progress.
