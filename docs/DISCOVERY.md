# Auto-Discovery Pipeline

The Lyra Intel Discovery module automatically discovers, analyzes, and registers new MCP (Model Context Protocol) crypto tools from GitHub.

## Overview

The discovery pipeline consists of three main components:

1. **GitHub Scanner** - Searches GitHub for new MCP repositories related to crypto/DeFi
2. **Tool Analyzer** - Uses AI to extract tool definitions and assess quality
3. **Registry Submitter** - Submits validated tools to the Lyra Registry

## Features

- 🔍 **Automatic Discovery** - Scans GitHub daily for new MCP crypto tools
- 🤖 **AI-Powered Analysis** - Uses GPT-4/Claude to extract tool metadata
- 🛡️ **Security Scanning** - Checks for vulnerabilities before submission
- 📊 **Quality Scoring** - Rates tools based on documentation, activity, and code quality
- 🔄 **Registry Integration** - Automatically submits approved tools to Lyra Registry

## Quick Start

### CLI Usage

```bash
# Scan GitHub for new MCP repositories (last 7 days)
python -m src.discovery.cli scan --days-back 7

# Analyze a specific repository
python -m src.discovery.cli analyze https://github.com/owner/repo

# Run complete pipeline (dry run)
python -m src.discovery.cli run --days-back 7 --dry-run

# Run pipeline and submit to registry
python -m src.discovery.cli run --days-back 7 --submit --no-dry-run

# View discovery statistics
python -m src.discovery.cli stats
```

### MCP Tools

The discovery module exposes MCP tools for AI-driven discovery:

| Tool | Description |
|------|-------------|
| `discovery-scan-github` | Scan GitHub for new MCP crypto repositories |
| `discovery-analyze-repo` | Analyze a specific repository for tools |
| `discovery-submit-tool` | Submit validated tools to registry |
| `discovery-run-pipeline` | Run complete discovery pipeline |
| `discovery-get-stats` | Get discovery statistics |

### Python API

```python
from src.discovery import DiscoveryPipeline, PipelineConfig

# Configure pipeline
config = PipelineConfig(
    scanner_config=GitHubScanConfig(
        github_token="your-token",
        days_back=7,
    ),
    submitter_config=SubmitterConfig(
        registry_url="https://registry.lyra.dev/api",
        dry_run=True,
    ),
)

# Run discovery
async with DiscoveryPipeline(config) as pipeline:
    result = await pipeline.run(submit=True)
    print(result.summary())
```

## Configuration

### Environment Variables

| Variable | Description | Required |
|----------|-------------|----------|
| `GITHUB_TOKEN` | GitHub API token (for higher rate limits) | Recommended |
| `OPENAI_API_KEY` | OpenAI API key (for AI analysis) | Optional |
| `ANTHROPIC_API_KEY` | Anthropic API key (alternative AI) | Optional |
| `LYRA_REGISTRY_URL` | Registry API URL | For submission |
| `LYRA_REGISTRY_API_KEY` | Registry API key | For submission |

### Scanner Configuration

```python
from src.discovery import GitHubScanConfig

config = GitHubScanConfig(
    github_token="your-token",
    days_back=7,              # How far back to search
    min_stars=0,              # Minimum stars required
    max_total_results=100,    # Maximum repos to find
    languages=["TypeScript", "JavaScript", "Python"],
)
```

### Analyzer Configuration

```python
from src.discovery import ToolAnalysisConfig

config = ToolAnalysisConfig(
    ai_provider="openai",     # openai, anthropic, or local
    ai_model="gpt-4",
    check_security=True,
    max_file_size=100000,
)
```

### Submitter Configuration

```python
from src.discovery import SubmitterConfig

config = SubmitterConfig(
    registry_url="http://localhost:3002/api",
    min_quality_score=50.0,   # Minimum quality to submit
    min_security_score=70.0,  # Minimum security to submit
    dry_run=True,             # Don't actually submit
)
```

## Daily Automation

### GitHub Actions

The discovery pipeline can run automatically via GitHub Actions:

```yaml
# .github/workflows/daily-discovery.yml
name: Daily Discovery

on:
  schedule:
    - cron: '0 6 * * *'  # 6 AM UTC daily

jobs:
  discover:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: '3.11'
      - run: pip install -e ".[ai]"
      - run: python scripts/daily_discovery.py --submit --dry-run
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
          OPENAI_API_KEY: ${{ secrets.OPENAI_API_KEY }}
```

### Manual Script

```bash
# Run daily discovery manually
python scripts/daily_discovery.py --days-back 1 --submit --dry-run
```

## Search Queries

The scanner uses these default queries to find crypto MCP tools:

- `mcp server crypto`
- `mcp server defi`
- `mcp server blockchain`
- `mcp server ethereum`
- `mcp server solana`
- `modelcontextprotocol crypto`
- `mcp wallet`
- `mcp trading`

You can provide custom queries:

```python
repos = await scanner.scan_mcp_repos(
    queries=["mcp server nft", "mcp collectibles"],
    days_back=7,
)
```

## Quality Scoring

Repositories are scored based on:

| Factor | Weight | Description |
|--------|--------|-------------|
| Stars | 1-3 pts | More stars = higher quality |
| README | 2 pts | Has documentation |
| License | 1 pt | Has open source license |
| Activity | 1-2 pts | Recent commits |
| Package config | 1 pt | Has package.json/pyproject.toml |
| MCP files | 2 pts | Has MCP-related code |

**Quality Tiers:**
- **HIGH** (8+ points) - Well-documented, active, many stars
- **MEDIUM** (4-7 points) - Some docs, moderate activity  
- **LOW** (1-3 points) - Minimal docs, low activity

## Security Analysis

Before submission, tools are scanned for:

- Command injection vulnerabilities
- Hardcoded credentials/secrets
- Unsafe eval/exec usage
- SQL injection risks
- Insecure file operations

Tools with security score < 70 are rejected by default.

## Pipeline Results

Each pipeline run saves results to `./discovery_results/`:

```json
{
  "started_at": "2024-01-15T06:00:00Z",
  "completed_at": "2024-01-15T06:15:00Z",
  "duration_seconds": 900,
  "repos_discovered": 25,
  "repos_analyzed": 20,
  "total_tools_found": 45,
  "tools_accepted": 12,
  "tools_rejected": 33,
  "high_quality_repos": 5,
  "medium_quality_repos": 10,
  "low_quality_repos": 10
}
```

## Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                    Discovery Pipeline                        │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  ┌──────────────┐    ┌──────────────┐    ┌──────────────┐  │
│  │   GitHub     │    │    Tool      │    │   Registry   │  │
│  │   Scanner    │───▶│   Analyzer   │───▶│   Submitter  │  │
│  └──────────────┘    └──────────────┘    └──────────────┘  │
│         │                   │                    │          │
│         ▼                   ▼                    ▼          │
│    Search API          Clone Repo          Submit API       │
│    Enrich Metadata     AI Analysis         Quality Gates    │
│    Quality Score       Security Scan       Retry Logic      │
│                                                              │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
                    ┌──────────────────┐
                    │   Lyra Registry  │
                    │   (Central Hub)  │
                    └──────────────────┘
```

## Troubleshooting

### Rate Limiting

If you hit GitHub API rate limits:

```bash
# Set GitHub token for higher limits
export GITHUB_TOKEN="your-personal-access-token"
```

### AI Analysis Fails

If AI analysis fails, the system falls back to pattern-based extraction:

```python
config = ToolAnalysisConfig(
    ai_provider="local",  # Use pattern matching instead of AI
)
```

### Registry Connection

Test registry connection:

```python
async with RegistrySubmitter(config) as submitter:
    health = await submitter.check_registry_health()
    print(health)
```

## Contributing

See [CONTRIBUTING.md](../CONTRIBUTING.md) for guidelines on contributing to the discovery module.
