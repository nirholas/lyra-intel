# Lyra Intel

<div align="center">

**Complete Intelligence Infrastructure Engine for Massive-Scale Codebase Analysis**

[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/)
[![MIT License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Docker Ready](https://img.shields.io/badge/docker-ready-blue.svg)](Dockerfile)
[![Kubernetes Ready](https://img.shields.io/badge/kubernetes-ready-blue.svg)](deploy/kubernetes/)
[![Open Source](https://img.shields.io/badge/open%20source-yes-brightgreen.svg)](https://github.com/nirholas/lyra-intel)

> 📚 **[Full Documentation](docs/README.md)** | [Quick Start](QUICKSTART.md) | [Use Cases](docs/USE_CASES.md) | [API Reference](docs/API.md)

**Analyze codebases 10-100x faster with AI-powered insights, security scanning, and semantic search.**

</div>

## ⚡ Active Development

Lyra Intel is **actively being enhanced with improvements daily**. The core platform is production-ready and being used in enterprise deployments. Thank you for your contributions! 🙌

## Why Lyra Intel?

Most code analysis tools force a choice: **automation at the cost of understanding**, or **manual inspection with no scale**.

Lyra Intel is built on a different principle: **Give developers and security teams the intelligence they need to make informed decisions at scale.**

**You get:**
- ✅ **Complete visibility** - Understand your entire codebase, not just highlighted issues
- ✅ **AI-powered insights** - Get context and explanations, not just lists of problems
- ✅ **Security you control** - Run locally or in your cloud, with no data leaving your infrastructure
- ✅ **Scale without sacrifice** - Analyze 1 million lines or 1 billion lines with the same ease
- ✅ **Open source** - Full transparency, no vendor lock-in, customize for your needs

Perfect for teams that want to **own their code intelligence**.

## What is Lyra Intel?

Lyra Intel is a comprehensive, production-ready intelligence platform designed to **understand, secure, and improve codebases of any size** - from small projects to enterprise monorepos with millions of lines of code.

Unlike traditional linters or SonarQube-style tools, Lyra Intel combines:
- **Deep code analysis** (AST parsing, dependency graphs, complexity metrics)
- **AI-powered insights** (OpenAI, Anthropic, or local models)
- **Semantic code search** (ML-powered search beyond keywords)
- **Security scanning** (secrets, OWASP, CVE detection)
- **Knowledge graphs** (understand relationships in your code)
- **Forensic analysis** (find dead code, document gaps, technical debt)

### Why You Need Lyra Intel

**For Security Teams:**
- Automatically find hardcoded secrets, SQL injection risks, OWASP vulnerabilities
- Track security across massive codebases without manual scanning
- Generate compliance reports (SOC2, HIPAA, PCI-DSS ready)

**For Development Teams:**
- Understand unfamiliar codebases in hours, not weeks
- Find dead code and technical debt before they become problems
- Make data-driven architectural decisions
- Detect complex bugs that static analysis misses

**For Engineering Leaders:**
- Quantify code quality and technical debt
- Track metrics across teams and projects
- Plan migrations and upgrades with confidence
- Reduce time spent on code reviews

## What You Can Do

With 70+ specialized components, Lyra Intel enables:

| Goal | What Lyra Intel Does | Time Saved |
|------|---------------------|-----------|
| **Secure a legacy codebase** | Scan for vulnerabilities, create remediation plan | Weeks → Hours |
| **Onboard new developers** | Build searchable knowledge base, find examples | Days → Hours |
| **Plan a framework upgrade** | Analyze impact, generate step-by-step migration plan | Months → Days |
| **Understand technical debt** | Quantify debt, track trends, prioritize fixes | Ongoing → Automated |
| **Review pull requests** | AI-powered insights + security checks + complexity analysis | 30 min → 5 min |
| **Find security issues** | Scan for 50+ vulnerability patterns in real-time | Manual → Automated |

[See real-world use cases →](docs/USE_CASES.md)

## 🚀 Features

Lyra Intel includes 70+ specialized components organized by capability:

<details>
<summary><b>View All Features (70+ Components)</b></summary>

### Core Analysis - Understand Your Code

- **📁 File Crawler** - Parallel directory traversal with streaming for memory efficiency. Process millions of files without memory issues.
- **📜 Git Collector** - Complete commit history, blame analysis, contributor stats. Understand who changed what and when.
- **🔍 AST Analyzer** - Multi-language syntax tree parsing (Python, JS/TS, Go, Rust, Java, C++, C#, Ruby, PHP). Get accurate code structure.
- **🔗 Dependency Mapper** - Build complete dependency graphs with circular detection. Understand your architecture.
- **⚠️ Pattern Detector** - Find code smells, anti-patterns, security issues. Detect problems before they become expensive.

### Scalability - From Laptop to Enterprise

- **🖥️ Local Mode** - Single machine analysis for development. No setup needed, runs instantly on your machine.
- **🌐 Distributed Mode** - Multi-worker processing for larger codebases. Scale analysis to 100K+ files efficiently.
- **☁️ Cloud Massive Mode** - Auto-scaling cloud infrastructure (AWS, GCP, Azure). Analyze monorepos with millions of files.

### Storage Options - Flexibility for Any Scale

- **SQLite** - Local development and small projects. Built-in, no dependencies.
- **PostgreSQL** - Production deployments. Reliable, proven, scalable.
- **BigQuery** - Massive-scale analytics. Query 1M+ analysis results instantly.
- **Cache Layer** - Memory, File, Redis backends with TTL/LRU eviction. Speed up repeated analyses.

### 🔐 Security - Find Vulnerabilities Before They Become Breaches

- **Security Scanner** - OWASP Top 10, hardcoded secrets, SQL injection detection. Scan 50+ vulnerability patterns.
- **Vulnerability Database** - Track known CVEs and advisories. Stay updated on emerging threats.
- **Custom Rules** - Define custom security patterns. Enforce your organization's security standards.

### 🤖 AI Integration - Get Smarter Insights

- **AI Analyzer** - Code explanation, bug detection, refactoring suggestions. Understand complex code instantly.
- **Multiple Providers** - OpenAI (GPT-4/3.5), Anthropic (Claude), or Local (Ollama/llama.cpp). Choose what fits your workflow.
- **Cost Effective** - Local models for free analysis, or cloud models for maximum accuracy.

### 📊 Visualization & Reports - Communicate Results

- **Graph Generator** - Export to D3.js, Mermaid, Graphviz DOT. Visualize dependencies and architecture.
- **Report Generator** - Executive, Technical, Security, Architecture reports. Different reports for different audiences.
- **Web Dashboard** - Interactive D3.js/Cytoscape visualization. Explore your codebase visually.

### 🌐 API & Enterprise Features

- **REST API Server** - 15+ endpoints for integration. Build on top of Lyra Intel.
- **Authentication** - API Key, JWT, OAuth 2.0 (SSO), LDAP support. Secure access control.
- **RBAC** - Role-based access control. Manage permissions across your team.
- **Rate Limiting** - Protect your infrastructure. Scale safely.

### 🔬 Forensic Analysis - Find Hidden Problems

- **Forensic Analyzer** - Code↔doc bidirectional mapping. Find documentation gaps automatically.
- **Dead Code Detector** - Find unused functions, classes, imports. Clean up your codebase.
- **Complexity Analyzer** - Cyclomatic, Cognitive, Halstead metrics. Identify problematic code.

### 📋 More Capabilities

- **Code Generation** - AI-powered function/class/API generation with custom templates
- **Diff & Impact Analysis** - Understand what changed and why it matters
- **Migration Planning** - Plan framework/version upgrades with step-by-step guidance
- **Code Profiling** - Detect N+1 queries, blocking I/O, inefficient algorithms
- **Schema Analysis** - Database schema analysis from ORM models
- **Documentation Generator** - Auto-generate API docs and changelogs
- **Workflow Engine** - Define and execute multi-step analysis pipelines

</details>

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

### Real-World Workflows

- **[💼 USE_CASES.md](docs/USE_CASES.md)** - Practical workflows and best practices:
  - Securing legacy codebases
  - Pre-commit code quality gates
  - CI/CD security pipelines
  - Code review assistance
  - Monorepo migration planning
  - Technical debt tracking
  - Building team knowledge bases
  - Integration patterns
  - Performance optimization tips

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

## Quick Start (5 Minutes)

Get up and running in just a few commands. No complex setup needed.

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
python launch_dashboard.py
# Then visit http://localhost:8080
```

### What to Expect

After running `scan`, you'll see:
```
✅ Analyzing repository...
📊 Files analyzed: 156
📈 Total functions: 1,247
⚠️  Issues found: 43
🔐 Security findings: 5
```

Running `analyze` produces detailed JSON with:
- **Metrics**: Line counts, complexity, test coverage
- **Security**: Vulnerabilities, secrets detection
- **Dependencies**: Import relationships, circular deps
- **Patterns**: Code smells, anti-patterns
- **Git history**: Commit stats, contributors

[See more quick examples →](QUICKSTART.md)

## 💼 Common Use Cases

Real teams use Lyra Intel for:

### 🔒 Security Teams
**"I need to scan our 500K LOC codebase for vulnerabilities"**
- [Secure a Legacy Codebase](docs/USE_CASES.md#use-case-1-securing-a-legacy-codebase) - Full audit in 30 min
- Automatic CI/CD security gates
- Pre-commit hooks that block insecure code
- Regular scheduled security scans

### 👨‍💻 Development Teams
**"New developer is joining - how do we onboard them on 200K lines of code?"**
- [Build a Team Knowledge Base](docs/USE_CASES.md#use-case-7-team-knowledge-base) - Semantic search over your codebase
- Find similar code patterns
- Understand architecture through visualization
- Track technical debt

### 🏗️ Platform Teams
**"We need to upgrade from Node 14 to Node 18 - is it safe?"**
- [Plan a Monorepo Migration](docs/USE_CASES.md#use-case-5-monorepo-migration-planning) - Step-by-step migration plan
- Analyze impact across all packages
- Identify breaking changes
- Estimate effort per package

### 📊 Engineering Leads
**"Is our code quality improving or getting worse?"**
- [Track Technical Debt](docs/USE_CASES.md#use-case-6-technical-debt-assessment) - Monthly trend tracking
- Visualize metrics over time
- Prioritize what to fix first
- Show data-driven reports to management

### 🔍 Code Review
**"Reviews are taking too long - 30 min per PR"**
- [AI-Powered Code Review](docs/USE_CASES.md#use-case-4-code-review-assistance) - Automated insights in 30 seconds
- Security analysis
- Complexity warnings
- AI suggestions for improvements

[👉 See 7 complete workflows with code examples →](docs/USE_CASES.md)

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

## How Lyra Intel Compares

| Feature | Lyra Intel | SonarQube | Snyk | GitHub Advanced Security |
|---------|-----------|-----------|------|------------------------|
| **Open Source** | ✅ MIT | ❌ Commercial | ❌ Proprietary | ⚠️ Limited |
| **Semantic Code Search** | ✅ ML-powered | ❌ No | ❌ No | ❌ No |
| **AI Integration** | ✅ Any provider | ❌ No | ❌ No | ✅ GitHub Copilot only |
| **Monorepo Support** | ✅ Up to 1M files | ⚠️ Limited | ✅ Good | ✅ Good |
| **Self-Hosted** | ✅ Full | ⚠️ Enterprise only | ⚠️ Limited | ✅ GitHub-hosted |
| **Cost** | ✅ Free | 💰💰💰 | 💰💰 | 💰 |
| **Knowledge Graph** | ✅ Automatic | ❌ No | ❌ No | ❌ No |
| **Forensic Analysis** | ✅ Dead code, debt | ⚠️ Basic | ❌ No | ⚠️ Basic |
| **Migration Planning** | ✅ Automated steps | ❌ No | ❌ No | ❌ No |
| **Multi-Language** | ✅ 10+ languages | ✅ Many | ⚠️ JS/Python focus | ✅ Many |
| **Real-time Dashboard** | ✅ React UI | ✅ Yes | ✅ Yes | ✅ Yes |

**Bottom line**: Lyra Intel is best for teams that want deep code understanding + AI insights + full control, all open source.

## 🛣️ Roadmap

### ✅ Phase 1: Core Platform (Complete)
- Complete analysis engine with 70+ components
- Multi-language parsing (10+ languages)
- Dependency graphing and pattern detection
- Git history analysis and forensics
- Security scanning (50+ patterns)
- AI integration (OpenAI, Anthropic, Ollama)

### ✅ Phase 2: Enterprise Features (Complete)
- REST API with 15+ endpoints
- Web dashboard with interactive visualizations
- Knowledge graph and semantic search
- RBAC, SSO, and authentication
- Code generation and migration planning
- IDE plugins (VS Code, JetBrains)

### ✅ Phase 3: Scale & Performance (Complete)
- Distributed analysis for 100K+ files
- Cloud massive mode (AWS/GCP/Azure auto-scaling)
- Real-time streaming analysis
- ML-based code review
- Performance profiling and optimization
- Schema analysis and workflow engine

### 🔄 Phase 4: Advanced Features (In Progress)
- Enhanced ML models for code understanding
- Custom model fine-tuning
- Advanced compliance reporting
- Real-time dashboard improvements
- Performance benchmarking suite

### 📅 Future Phases
- Automated remediation suggestions
- Integration with more CI/CD platforms
- Mobile app for dashboard access
- Advanced visualization options
- Community plugin marketplace

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

## 🌟 Show Your Support

If you find Lyra Intel helpful, consider:

- ⭐ **Star this repository** - It helps others discover the project
- 🐛 **Report issues** - Help us improve by reporting bugs
- 💡 **Share ideas** - Suggest features and improvements
- 🤝 **Contribute** - See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines
- 📢 **Spread the word** - Share with your team and community

Every star, contribution, and mention helps grow the community!

## 🙏 Acknowledgments

Built with amazing open-source tools:
- [OpenAI](https://openai.com) & [Anthropic](https://anthropic.com) - AI models
- [FastAPI](https://fastapi.tiangolo.com) - Web framework
- [React](https://react.dev) - UI framework
- [Prometheus](https://prometheus.io) - Monitoring
- [PostgreSQL](https://postgresql.org) - Database

## 📧 Contact & Support

- **Issues & Bug Reports**: [GitHub Issues](https://github.com/nirholas/lyra-intel/issues)
- **Documentation**: [Full Documentation](docs/README.md)
- **Contributing**: See [CONTRIBUTING.md](CONTRIBUTING.md)

---

<div align="center">

Made with ❤️ for developers, security teams, and engineering leaders.

**[⬆ Back to Top](#lyra-intel)**

</div>

## 📄 License

MIT License - see [LICENSE](LICENSE) file for details.

---

**Made with❤️by [nich](https://github.com/nirholas) | [Follow me on X.com](x.com/nichxbt)**