# lyra-intel examples

[](https://www.python.org/) [](Dockerfile) [](deploy/kubernetes/) [](https://github.com/nirholas/lyra-intel)

## Example 1

```bash
# 1. Clone the repository
git clone https://github.com/nirholas/lyra-intel.git
cd lyra-intel

# 2. Install (requires Python 3.9+)
pip install -e .

# 3. Quick scan - see what Lyra Intel finds in 30 seconds
python cli.py scan /path/to/any/code

# 4. Full analysis - comprehensive report
python cli.py analyze /path/to/code --output ./results.json

# 5. View results
cat results.json | jq .  # Pretty print the JSON

# 6. (Optional) Start the web dashboard
python scripts/launch_dashboard.py
# Then visit http://localhost:8080
```

## Example 2

```text
✅ Analyzing repository...
📊 Files analyzed: 156
📈 Total functions: 1,247
⚠️  Issues found: 43
🔐 Security findings: 5
```

## Example 3

```bash
# Claude Code - one command
npx lyra-intel-mcp

# Claude Desktop - add to config
{
  "mcpServers": {
    "lyra-intel": {
      "command": "npx",
      "args": ["-y", "lyra-intel-mcp"]
    }
  }
}
```

## Example 4

```text
"Analyze my project at ~/code/myapp for security issues"
"Search for authentication patterns in the codebase"
"Scan GitHub for new MCP crypto tools from the last 7 days"
"Run the discovery pipeline and submit approved tools"
```

## Example 5

```text
lyra-intel/
├── src/
│   ├── core/           # Main engine orchestration
│   ├── collectors/     # Data collection (files, git)
│   ├── analyzers/      # Code analysis (AST, dependencies, patterns)
│   ├── storage/        # Database and persistence
│   ├── agents/         # Multi-agent system
│   ├── search/         # Code and semantic search
│   ├── query/          # Natural language queries
│   ├── visualizers/    # Graph generation
│   ├── reports/        # Report generation
│   ├── web/            # Web dashboard
│   ├── api/            # REST API server
│   ├── auth/           # Authentication and authorization
│   ├── plugins/        # Plugin system
│   ├── ai/             # AI integration
│   ├── metrics/        # Metrics collection
│   ├── events/         # Event system
│   ├── notifications/  # Notifications and alerts
│   ├── forensics/      # Forensic analysis
│   ├── cache/          # Caching layer
│   ├── pipeline/       # Streaming pipeline
│   ├── testing/        # Testing infrastructure
│   ├── knowledge/      # Knowledge graph system
│   ├── diff/           # Diff and impact analysis
│   ├── generation/     # Code generation
│   ├── security/       # Security scanning
│   ├── migration/      # Migration planning
│   ├── profiler/       # Performance profiling
│   ├── schema/         # Schema analysis
│   ├── docgen/         # Documentation generation
│   ├── integrations/   # External integrations
│   └── workflow/       # Workflow engine
├── config/             # Configuration files
├── scripts/            # Utility scripts
├── Dockerfile          # Container build
├── docker-compose.yml  # Multi-service deployment
└── cli.py              # Command-line interface
```

## Example 6

```bash
docker-compose restart postgres
docker-compose logs postgres
```

## Example 7

```bash
# Reduce workers
export WORKERS=4

# Increase memory limit
docker-compose up -d --scale api=1 --memory 4g
```

## Example 8

```bash
# Increase rate limits in config
export RATE_LIMIT_PER_MINUTE=1000
```


Every snippet above is taken from the [repository documentation](https://github.com/nirholas/lyra-intel#readme).
