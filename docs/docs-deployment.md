# Documentation Site Deployment

The documentation at [lyra-intel.modelcontextprotocol.name](https://lyra-intel.modelcontextprotocol.name) is a MkDocs Material site hosted on Cloudflare Pages.

| Item | Value |
|------|-------|
| Host | Cloudflare Pages, project `lyra-intel-docs` |
| Production URL | `https://lyra-intel.modelcontextprotocol.name` |
| Security headers | `docs/_headers` (copied into the build) |
| DNS | Proxied CNAME in the `modelcontextprotocol.name` Cloudflare zone, pointing to `lyra-intel-docs.pages.dev` |

## Build

```bash
pip install mkdocs-material pymdown-extensions
mkdocs build            # output: site/
```

## Deploy

Export `CLOUDFLARE_API_TOKEN` and `CLOUDFLARE_ACCOUNT_ID`, then run from the repository root:

```bash
npx wrangler@4 pages deploy site --project-name=lyra-intel-docs --branch=main
```

Deploys are manual. GitHub Actions is not used for this site.

## Verify

```bash
curl -sI https://lyra-intel.modelcontextprotocol.name | head -1   # HTTP/2 200
```

## Rollback

In the Cloudflare dashboard, open **Workers & Pages → lyra-intel-docs → Deployments**.
Pick an earlier production deployment and select **Rollback to this deployment**.

## API server

The REST API (`lyra-intel serve`, routes in `src/api/server.py`) runs on Google Cloud Run as service `lyra-intel` in `us-central1`. The `lyra-intel-api-proxy` Cloudflare Worker serves it at `https://lyra-intel-api.modelcontextprotocol.name`.

```bash
gcloud run deploy lyra-intel --source . --region us-central1 \
  --args=cli.py,serve,--port,8000,--host,0.0.0.0 --port 8000
curl -s https://lyra-intel-api.modelcontextprotocol.name/health
```
