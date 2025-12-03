# Lyra Intel

**Complete Intelligence Infrastructure Engine for Massive-Scale Codebase Analysis**

Lyra Intel is a comprehensive, production-ready intelligence platform designed to analyze repositories of any size - from small projects to enterprise monorepos with millions of lines of code. With **70+ components**, it provides end-to-end analysis, security scanning, AI integration, and more.

## 🚀 Features

### Core Analysis
- **📁 File Crawler** - Parallel directory traversal with streaming for memory efficiency
- **📜 Git Collector** - Complete commit history, blame analysis, contributor stats
- **🔍 AST Analyzer** - Multi-language syntax tree parsing (Python, JS/TS, Go, Rust, Java)
- **🔗 Dependency Mapper** - Build complete dependency graphs with circular detection
- **⚠️ Pattern Detector** - Find code smells, anti-patterns, security issues

### Scalability
- **🖥️ Local Mode** - Single machine analysis for development
- **🌐 Distributed Mode** - Multi-worker processing for larger codebases
- **☁️ Cloud Massive Mode** - Auto-scaling cloud infrastructure (AWS, GCP, Azure)

### Storage
- **SQLite** - Local development and small projects
- **PostgreSQL** - Production deployments
- **BigQuery** - Massive-scale analytics
- **Cache Layer** - Memory, File, Redis backends with TTL/LRU eviction

### Agent Fleet
- **Coordinator** - Task distribution, load balancing, fault tolerance
- **Workers** - Parallel analysis agents
- **Cloud Orchestrator** - Auto-scaling infrastructure management

### 🧠 Knowledge System
- **Knowledge Graph** - Semantic relationships between code elements
- **Graph Builder** - Automatically build graphs from analysis
- **Graph Query** - Natural language queries over knowledge

### 🔐 Security
- **Security Scanner** - OWASP Top 10, hardcoded secrets, SQL injection detection
- **Vulnerability Database** - Track known CVEs and advisories
- **Custom Rules** - Define custom security patterns

### 🤖 AI Integration
- **AI Analyzer** - Code explanation, bug detection, refactoring suggestions
- **OpenAI Provider** - GPT-4/GPT-3.5 support
- **Anthropic Provider** - Claude support
- **Local Provider** - Ollama/llama.cpp support

### 📊 Visualization & Reports
- **Graph Generator** - Export to D3.js, Mermaid, Graphviz DOT
- **Report Generator** - Executive, Technical, Security, Architecture reports
- **Web Dashboard** - Interactive D3.js/Cytoscape visualization

### 🌐 API & Auth
- **REST API Server** - Full HTTP API with 15+ endpoints
- **API Key Auth** - Key generation, validation, rotation
- **JWT Auth** - Token generation and validation
- **Rate Limiter** - Request throttling
- **RBAC** - Role-based access control

### 🔬 Forensic Analysis
- **Forensic Analyzer** - Complete code↔doc bidirectional mapping
- **Dead Code Detector** - Find unused functions, classes, imports
- **Complexity Analyzer** - Cyclomatic, Cognitive, Halstead metrics

### ⚙️ Code Generation
- **Code Generator** - AI-powered function/class/API generation
- **Template Engine** - Custom templates with variables and loops

### 📝 Diff & Impact
- **Diff Analyzer** - Line-level and semantic diffs
- **Impact Analyzer** - Understand change effects on codebase

### 🔧 Migration
- **Migration Planner** - Plan framework/version upgrades
- **Migration Steps** - Automated migration execution

### ⚡ Performance
- **Code Profiler** - Detect N+1 queries, blocking I/O, inefficient algorithms
- **Schema Analyzer** - Database schema analysis from ORM models

### 📖 Documentation
- **Doc Generator** - Auto-generate API docs, READMEs
- **Changelog Generator** - Generate from git history

### 🔗 Integrations
- **Integration Hub** - Central integration management
- **GitHub Integration** - Issues, PRs, comments
- **Slack Integration** - Notifications

### 🔄 Workflow
- **Workflow Engine** - Define and execute multi-step pipelines
- **Step Handlers** - Custom workflow actions

## 📚 Complete Documentation

Lyra Intel includes comprehensive documentation covering every aspect of the platform:

### Core Documentation

- **[📖 FEATURES.md](docs/FEATURES.md)** - Detailed feature documentation with code examples for:
  - Semantic Search (ML-powered code search)
  - SSO Integration (OAuth 2.0, SAML 2.0, LDAP)
  - Language Parsers (C++, C#, Ruby, PHP)
  - Plugin System
  - IDE Extensions (VS Code, JetBrains)
  - CI/CD Integrations (GitLab, Bitbucket, GitHub Actions)
  - Export Formats (PDF, SARIF, Excel, CSV)
  - WebSocket Streaming
  - Interactive CLI
  - Web Dashboard
  - Monitoring & Metrics (Prometheus, Grafana)

- **[💻 EXAMPLES.md](docs/EXAMPLES.md)** - Working code examples for:
  - Quick start (60-second analysis)
  - Core analysis workflows
  - Semantic search usage
  - SSO setup and configuration
  - Language-specific parsing
  - Custom plugin development
  - IDE extension installation
  - CI/CD pipeline integration
  - Real-time WebSocket streaming
  - Monitoring setup
  - Complete end-to-end workflows

- **[🏗️ ARCHITECTURE.md](docs/ARCHITECTURE.md)** - Technical architecture documentation:
  - System overview and design
  - Core component architecture
  - Data flow diagrams
  - Module organization
  - Extension points
  - Deployment architectures (single server, Kubernetes, AWS)
  - Performance & scalability
  - Security architecture
  - Technology stack

- **[🔌 API.md](docs/API.md)** - Complete REST API reference
- **[🚀 DEPLOYMENT.md](docs/DEPLOYMENT.md)** - Deployment guides (Docker, Kubernetes, AWS)
- **[📜 openapi.yaml](docs/openapi.yaml)** - OpenAPI 3.0 specification

### Getting Started Guides

- **[⚡ QUICKSTART.md](QUICKSTART.md)** - Get up and running in 5 minutes
- **[🔧 INSTALL.md](INSTALL.md)** - Installation instructions
- **[📚 TUTORIAL.md](docs/TUTORIAL.md)** - Step-by-step tutorials for common use cases:
  - First analysis
  - Security audit
  - Semantic search setup
  - CI/CD integration
  - Custom plugin development
  - Production deployment
  - Real-time dashboard
- **[❓ FAQ.md](docs/FAQ.md)** - Frequently asked questions
- **[🤝 CONTRIBUTING.md](CONTRIBUTING.md)** - Contribution guidelines

## Quick Start

```bash
# Clone the repo
git clone https://github.com/nirholas/lyra-intel.git
cd lyra-intel

# Install dependencies
pip install -e .

# Quick scan a repository
python cli.py scan /path/to/repo

# Full analysis
python cli.py analyze /path/to/repo --output ./results

# Check status
python cli.py status
```

## Architecture

```
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

## Processing Modes

### Local Mode
Best for development and small repositories:
```python
from src import LyraIntelEngine, EngineConfig, ProcessingMode

config = EngineConfig(mode=ProcessingMode.LOCAL, max_workers=8)
engine = LyraIntelEngine(config)
result = await engine.analyze_repository("/path/to/repo")
```

### Distributed Mode
For larger codebases with multiple workers:
```python
config = EngineConfig(
    mode=ProcessingMode.DISTRIBUTED,
    max_workers=50,
)
```

### Cloud Massive Mode
For enterprise-scale analysis:
```python
config = EngineConfig(
    mode=ProcessingMode.CLOUD_MASSIVE,
    cloud_provider="aws",
    cloud_region="us-east-1",
    max_cloud_workers=1000,
)
```

## Analysis Results

The engine produces comprehensive analysis including:

- **File metrics**: Total files, sizes, line counts by extension
- **Code structure**: Functions, classes, methods with complexity scores
- **Dependencies**: Import/export relationships, circular dependencies
- **Git history**: Commits, authors, change frequency
- **Patterns**: Code smells, anti-patterns, security issues

Results are stored in SQLite (or your configured backend) and can be exported as JSON.

## Cloud Support

Lyra Intel is designed to leverage cloud resources efficiently:

| Provider | Instance Types | Spot Support | Optimization |
|----------|---------------|--------------|----------------|
| AWS | EC2, Lambda, ECS | ✅ Supported | ~70% savings |
| GCP | Compute Engine, Cloud Run | ✅ Supported | ~70% savings |
| Azure | VMs, Functions | ✅ Supported | ~70% savings |

Auto-scaling and cost optimization features included.

## Roadmap

✅ = Complete | 🔄 = In Progress

- [x] Core analysis engine
- [x] Multi-language AST parsing
- [x] Dependency graphing
- [x] Pattern detection
- [x] Git history analysis
- [x] API server
- [x] Web dashboard
- [x] Knowledge graph
- [x] Security scanning
- [x] AI integration
- [x] Code generation
- [x] Migration planning
- [x] Performance profiling
- [x] Schema analysis
- [x] Workflow engine
- [x] External integrations
- [x] Documentation generation
- [x] IDE plugins (VS Code, JetBrains)
- [x] Real-time streaming analysis
- [x] Machine learning-based code review

## 📈 Metrics & Monitoring

Access metrics at:
- **Prometheus**: `http://localhost:9090`
- **Grafana**: `http://localhost:3000`
- **API Health**: `http://localhost:8080/api/v1/health`

Key metrics:
- `lyra_intel_requests_total` - Total API requests
- `lyra_intel_analysis_duration_seconds` - Analysis performance
- `lyra_intel_ai_tokens_total` - AI usage tracking
- `lyra_intel_cache_hits_total` - Cache efficiency

## 🤝 Contributing

We welcome contributions! Please see [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

## 🐛 Troubleshooting

Common issues and solutions:

**Database connection failed**
```bash
docker-compose restart postgres
docker-compose logs postgres
```

**High memory usage**
```bash
# Reduce workers
export WORKERS=4

# Increase memory limit
docker-compose up -d --scale api=1 --memory 4g
```

**API rate limit**
```bash
# Increase rate limits in config
export RATE_LIMIT_PER_MINUTE=1000
```

See [DEPLOYMENT.md](docs/DEPLOYMENT.md) for comprehensive troubleshooting.

## 📊 Project Status

- ✅ Core analysis engine
- ✅ Multi-language support (10+ languages)
- ✅ AI integrations (OpenAI, Anthropic, Ollama)
- ✅ Security scanning (OWASP, secrets, dependencies)
- ✅ Export formats (JSON, HTML, PDF, SARIF, CSV, Excel)
- ✅ IDE plugins (VS Code, JetBrains)
- ✅ Platform integrations (GitHub, GitLab, Bitbucket)
- ✅ Cloud deployment (AWS, Kubernetes, Docker)
- ✅ Real-time streaming (WebSocket)
- ✅ Web dashboard (React)
- ✅ Monitoring (Prometheus, Grafana)
- ✅ Enterprise features (SSO, RBAC, audit logs)

## 🙏 Acknowledgments

Built with amazing open-source tools:
- [OpenAI](https://openai.com) & [Anthropic](https://anthropic.com) - AI models
- [FastAPI](https://fastapi.tiangolo.com) - Web framework
- [React](https://react.dev) - UI framework
- [Prometheus](https://prometheus.io) - Monitoring
- [PostgreSQL](https://postgresql.org) - Database

## 📧 Contact

- **Issues**: [GitHub Issues](https://github.com/nirholas/lyra-intel/issues)
- **Docs**: [Documentation](https://github.com/nirholas/lyra-intel/docs)

## 📄 License

MIT License - see [LICENSE](LICENSE) file for details.

---

**Made with❤️by [nich](https://github.com/nirholas) | [Follow me on X.com](x.com/nichxbt)**