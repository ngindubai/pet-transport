# Pet Transport Global deployment

## Single production pipeline

Production is deployed only through `.github/workflows/build-to-live.yml`:

1. A reviewed change is merged or pushed to `main`.
2. GitHub Actions validates the source, rebuilds internal links, and builds Hugo 0.160.1.
3. The rendered site is audited and published as an orphan `live` branch.
4. Hostinger Git watches `live` and deploys that branch to `public_html`.

The former FTP workflow has been removed. Do not add a second production publisher or upload build output manually, because competing deployments can leave the live site stale or partially overwritten.

## Hostinger settings

- Repository branch: `live`
- Deployment directory: `public_html`
- Automatic deployment: enabled
- PHP: supported 8.x release
- HTTPS: enabled

Configure these server-side values in the hosting environment; never commit them:

- `PTG_CRM_API_KEY`: rotated CRM API key
- `PTG_RATE_LIMIT_SALT`: long random string
- `PTG_RECIPIENT_EMAIL`: optional; defaults to `info@pettransportglobal.com`
- `PTG_SENDER_EMAIL`: optional; defaults to `noreply@pettransportglobal.com`
- `PTG_CRM_ENDPOINT`: optional; defaults to the current CRM lead endpoint

After the first deployment, submit a test enquiry and confirm both the company inbox and CRM receive one record. The exposed historical CRM key must be revoked before production testing.

## Pull-request checks

`.github/workflows/quality-gates.yml` runs the same validation, Hugo build, sitemap generation, and rendered-site audit without publishing.

## Rollback

Revert the faulty change on `main` and merge the revert. The single production workflow will rebuild `live`; Hostinger then deploys the reverted output.
