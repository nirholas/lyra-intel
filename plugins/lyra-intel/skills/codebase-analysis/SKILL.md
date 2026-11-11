---
name: codebase-analysis
description: Analyze a local repository with the Lyra Intel Python CLI (cli.py) for structure, complexity, dead code, hardcoded secrets and security findings. Use when asked to audit a codebase, find complexity hotspots, or produce an analysis report.
---

# Lyra Intel codebase analysis

Lyra Intel is a Python 3.10+ package with an argparse CLI in `cli.py`. It is not on PyPI, so install it from a clone. Run every command against a repository you already trust enough to read; the analysis reads files and git history but does not execute the target's code.

## Install

```bash
git clone https://github.com/nirholas/lyra-intel
cd lyra-intel
pip install -e .
python cli.py status
```

Optional extras are defined in `pyproject.toml`: `ai` (openai, anthropic, sentence-transformers), `export` (reportlab, openpyxl), `discovery` (aiohttp), `cli` (rich). Install one with `pip install -e ".[export]"`.

## Commands

Run from the clone as `python cli.py <command>`. `repo_path` is the repository to analyze.

| Command | Purpose |
|---|---|
| `scan <repo_path>` | Quick scan: file counts and structure |
| `analyze <repo_path> [--output DIR] [--mode local\|distributed\|cloud_massive] [--json]` | Full analysis |
| `search <query> <repo_path> [--regex] [--case-sensitive] [--max-results N]` | Code search |
| `query <question> <repo_path>` | Natural language question about the codebase |
| `complexity <repo_path>` | Complexity metrics |
| `dead-code <repo_path>` | Unused code detection |
| `security <repo_path> [--output FILE]` | Security scan |
| `forensic <repo_path> [--output FILE]` | Forensic analysis, JSON output |
| `commit-history <repo_path> [--branch B] [--max-commits N] [--start H] [--end H] [--output FILE] [--no-security] [--no-complexity]` | Walk commits to track when bugs entered |
| `knowledge-graph <repo_path> [--query Q] [--export FILE]` | Build and query a knowledge graph |
| `report <repo_path> [--type executive\|technical\|security\|architecture\|full] [--format markdown\|html\|json] [--output FILE]` | Written report |
| `docs <repo_path> [--type api\|readme\|architecture\|changelog] [--output FILE]` | Generate documentation |
| `serve [--port 8000] [--host H]` | Start the API server |
| `dashboard [--port 3000] [--host 127.0.0.1]` | Start the visualization dashboard |

The `security` subcommand is named `security`, not `security-scan` as one older doc has it. If a command errors, run `python cli.py <command> --help` and use what it prints.

## Worked example

Audit a project and hand back a short security-focused report:

```bash
python cli.py scan ~/work/my-service
python cli.py security ~/work/my-service --output security.json
python cli.py report ~/work/my-service --type security --format markdown --output security-report.md
```

Read `security.json` and the report, then summarize the findings by severity with file paths. Say which commands you ran and what the tool actually printed. Do not claim a finding it did not report.

## MCP server

The repo also contains `mcp-server/` (npm package `lyra-intel-mcp`). Its analysis tools (`analyze-codebase`, `search-code`, `get-complexity`, `get-security-issues`) return placeholder text and tell the caller to connect to a Lyra Intel API, so this plugin does not register it. Use the CLI above for real results.
