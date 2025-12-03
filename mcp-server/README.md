# Lyra Intel MCP Server

The Lyra Intel MCP (Model Context Protocol) server enables large language models like Claude to interact with Lyra Intel analysis capabilities directly.

## Features

- **🔍 Codebase Analysis** - Run comprehensive analysis including AST parsing, dependency mapping, and complexity metrics
- **🔎 Semantic Search** - ML-powered code search to find relevant implementations
- **📊 Complexity Metrics** - Get cyclomatic, cognitive, and Halstead complexity scores
- **🛡️ Security Scanning** - Detect vulnerabilities, secrets, and compliance issues
- **⏳ Streaming Progress** - Long-running operations stream progress updates to Claude

## Installation

### Quick Start with Claude Code

```bash
# Install globally for one-line setup
npm install -g lyra-intel-mcp

# Add to Claude Code
claude mcp add lyra-intel -- lyra-intel-mcp
```

### Claude Desktop

Add to your Claude Desktop config file:

**macOS/Linux**: `~/.config/claude/claude_desktop_config.json`
**Windows**: `%APPDATA%\Claude\claude_desktop_config.json`

```json
{
  "mcpServers": {
    "lyra-intel": {
      "command": "npx",
      "args": ["-y", "lyra-intel-mcp"]
    }
  }
}
```

Then restart Claude Desktop completely.

### Local Development

```bash
cd mcp-server
npm install
npm run build
npm start
```

## Usage with Claude

### Natural Language

```
"Analyze my project at /path/to/project for security issues"
"Search for authentication patterns in the codebase"
"Check complexity of the auth module"
```

### Tools Available

#### analyze-codebase
Comprehensive codebase analysis with AST parsing, dependency graphs, and metrics.

```
Analyze /path/to/project at deep level focusing on security and complexity
```

#### search-code
Semantic search using ML embeddings.

```
Search for "database connection handling" in src/
```

#### get-complexity
Get complexity metrics for code.

```
Show complexity metrics for src/auth/
```

#### get-security-issues
Scan for security vulnerabilities.

```
Find security issues in critical severity or higher
```

## Integration with API

The MCP server currently streams output and basic information. For full integration with the Lyra Intel REST API:

1. Set your Lyra Intel API endpoint:
```bash
export LYRA_INTEL_API_URL=http://localhost:8000
export LYRA_INTEL_API_KEY=your_api_key
```

2. Tools will automatically forward requests to the backend API

## Architecture

```
Claude/LLM Client
        ↓
    MCP Protocol
        ↓
Lyra Intel MCP Server
        ↓
Lyra Intel REST API
        ↓
Analysis Engine (Python)
```

## Troubleshooting

### "MCP server not responding"

1. Verify Node.js 16+ is installed: `node --version`
2. Check configuration file syntax (valid JSON)
3. Restart your MCP client completely
4. Enable debug logging:
   ```bash
   DEBUG=lyra-intel-mcp npm start
   ```

### Large codebase timeouts

The MCP server streams progress to prevent timeouts. If you still experience timeouts:

1. Start with "quick" analysis depth
2. Use file pattern filters to narrow scope
3. Increase MCP client timeout (check client docs)

### No results returned

Ensure:
1. Lyra Intel API is running and accessible
2. API credentials are set correctly
3. The provided path exists and is readable

## Development

### Adding New Tools

1. Create tool schema and implementation in `src/tools/analysis.ts`:

```typescript
export const myNewTool: UnifiedTool = {
  name: "tool-name",
  description: "What it does",
  zodSchema: z.object({
    param: z.string().describe("Parameter description"),
  }),
  category: 'category',
  execute: async (args, onProgress) => {
    onProgress?.("Starting...");
    return "Result";
  }
};
```

2. Add to `toolRegistry` in `src/tools/registry.ts`

3. Rebuild and restart

### Testing

```bash
npm run test
```

## Documentation

For more information about Model Context Protocol, see:
- [MCP Documentation](https://modelcontextprotocol.io/)
- [Lyra Intel API Docs](/docs/API.md)
- [Lyra Intel Architecture](/docs/ARCHITECTURE.md)

## License

MIT - See [LICENSE](../LICENSE) for details.
