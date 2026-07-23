# Claude handoff prompt — Pet Transport Global

You are taking over a completed SEO, security, content-quality, performance, and deployment remediation for the `ngindubai/pet-transport` repository.

## Objective

Safely publish the supplied fixed source tree to GitHub, review it through a pull request, and deploy it using the repository's single supported production path:

`main` → GitHub Actions `build-to-live.yml` → orphan `live` branch → Hostinger Git deployment

Do not restore or create a second production workflow, and do not manually upload `site/public` to Hostinger.

## Starting state

- Original repository: `https://github.com/ngindubai/pet-transport`
- Original audited commit: `427b2e651bf22cf3c85c071ada05923b5710400e`
- Fixed local branch: `fix/full-seo-code-audit`
- Fixed commit produced by Codex: `be0d8d4464c7`
- The ZIP contains the committed fixed tree but intentionally excludes `.git` and generated `site/public` output.
- The remediation touched 8,386 tracked files: 7,783 modifications, 595 deletions, 7 additions, and 1 rename. Most content edits normalize company attribution and repair generated route content.

## Important owner decisions

- The Hostinger `live` branch deployment is the only production pipeline.
- Until real named experts are verified, all editorial attribution must remain `Pet Transport Global Editorial Team` and structured data must use an Organization—not invented Person authors.
- Legal operator supplied by the owner:
  - Global Solutions Ltd
  - 71–75 Shelton Street, Covent Garden, London, WC2H 9JQ
  - info@pettransportglobal.com
  - Governing law and jurisdiction: England and Wales
- Do not publish company number `9897762` or `09897762`. Companies House assigns `09897762` to a different, dissolved company. Ask the owner for the correct eight-digit registration number, verify it against the official Companies House record, and only then add it to the privacy policy, terms, and Organization schema.

## Security requirements

1. A CRM API key was previously exposed in browser JavaScript. It has been removed from the supplied tree and CRM submission now happens server-side through `site/static/submit.php`.
2. Do not reuse, print, commit, or request the old key in chat. Have the owner rotate it in the CRM and configure the replacement on Hostinger as `PTG_CRM_API_KEY`.
3. Configure Hostinger environment variables described in `DEPLOY.md`; never hard-code secrets.
4. Customer invoice files and personal data were removed from the current tree. They still exist in old Git history until a separate destructive history rewrite is approved.
5. Do not rewrite or force-push repository history without explicit owner approval. If approved, first enumerate all affected branches and tags, revoke the exposed credential, create a recoverable backup, purge both the invoices and old key from every ref, force-push the exact approved refs, and provide resynchronization instructions for Hostinger and existing clones.

## Publishing procedure

1. Work in an authenticated clone of `ngindubai/pet-transport` at original commit `427b2e6` or the current equivalent base.
2. Create or reset a working branch named `fix/full-seo-code-audit` from the intended base.
3. Copy the ZIP contents into the clone without overwriting `.git`. Ensure deletions from the fixed tree are also reflected; do not merely copy files on top and leave obsolete files behind.
4. Inspect the full diff. Preserve all supplied remediation unless a validation failure proves a change is wrong.
5. Commit with a clear message such as `fix: harden production and correct sitewide SEO`.
6. Push the branch and open a draft pull request into `main`. Do not merge without owner review.
7. After approval and merge, verify `build-to-live.yml` succeeds, the `live` branch contains only the built production artifact, and Hostinger is configured to deploy that branch.

## Required validation

Use Hugo Extended 0.160.1 or a compatible version. From the repository root, run:

```bash
python scripts/validate_site.py
node --check site/assets/js/main.js
python -m py_compile scripts/validate_site.py scripts/audit_build.py split_sitemap.py rebuild_link_graph_v3.py
hugo --gc --minify --cleanDestinationDir --source site
python split_sitemap.py
python -u scripts/audit_build.py
git diff --check
```

Expected baseline:

- Source validator: 6,971 route pages; 4,978 without a recorded verification date; pass.
- Hugo: approximately 7,783 pages plus 159 paginator pages; build succeeds.
- Rendered audit: approximately 7,946 HTML files; zero metadata warnings; pass.
- Sitemap split: 1,993 routes, 365 hubs, 430 blog URLs, and 11 general pages.
- Undated route pages remain `noindex,follow`, have no fabricated `dateModified`, and are excluded from the route sitemap.
- All 7,749 content author fields remain `Pet Transport Global Editorial Team`.
- No public company number appears until the correct number is verified.
- No CRM API credential or customer invoice remains in the current tree.

The exact total can move slightly only if the owner explicitly requests additional content changes. Investigate any unexpected difference before publishing.

## Remediation that must not be regressed

- Consent-aware Google Analytics and conversion tracking.
- Server-side form validation, honeypot, timing check, rate limiting, idempotency, CRM delivery, and email fallback.
- Security and caching headers in `site/static/.htaccess`.
- Honest verification dates and methodology language; no build-date freshness fabrication.
- Company editorial attribution instead of fictional writers or reviewers.
- Corrected route contradictions, duplicate wording, placeholder authorities, and quarantine-facility claims.
- Paginated route directory, unique pagination metadata, canonical handling, and lighter asset loading.
- Custom sitemap excluding undated route pages.
- Single GitHub production workflow plus non-publishing quality gates.
- Removal of customer invoices, unused raw media, editable PSD files, the legacy template bundle, PHPMailer duplicates, LayerSlider assets, and public internal reports.

## Final report to the owner

Report the draft PR URL, branch and commit SHA, validation results, deployment status, and any remaining owner actions. The expected remaining actions are the correct Companies House number, CRM key rotation/Hostinger secret configuration, and a yes/no decision on the destructive Git-history purge.
