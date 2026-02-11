# lyra-intel

> Lyra Intel is an intelligence platform designed to analyze repositories of any size - from small projects to enterprise monorepos with millions of lines of code. With 70+ components, it provides end-to-end analysis, security scanning, AI integration, and more. 

### Terminal Management

- **Always use background terminals** (`isBackground: true`) for every command so a terminal ID is returned
- **Always kill the terminal** after the command completes, whether it succeeds or fails — never leave terminals open
- Do not reuse foreground shell sessions — stale sessions block future terminal operations in Codespaces
- In GitHub Codespaces, agent-spawned terminals may be hidden — they still work. Do not assume a terminal is broken if you cannot see it
- If a terminal appears unresponsive, kill it and create a new one rather than retrying in the same terminal
