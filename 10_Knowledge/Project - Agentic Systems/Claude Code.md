---
Phase: [[Phase 8]]
Project: [[Project - Agentic Systems]]
Prev: [[00_Overview]] | Next: [[Gemini CLI]]
---
# Claude Code (Skills & MCP)

Claude Code v2 uses a two-pronged approach to extension: **Skills** for procedural logic and **Model Context Protocol (MCP)** for external data/tools.

## 1. Claude Skills
Skills are reusable instructions stored in `.md` files. Claude auto-activates them based on your request.

### File Structure
- **Global:** `~/.claude/skills/`
- **Project:** `.claude/skills/`

```text
my-skill/
├── SKILL.md       (Required) Instructions and metadata
├── template.md    (Optional) Output formatting
└── scripts/       (Optional) Executable scripts
```

### SKILL.md Frontmatter
```yaml
---
name: my-skill
description: Triggers when user asks to [action].
agent: Plan (or general-purpose)
context: fork (isolates logic)
---
# Instructions
When active, do X, then Y.
```

## 2. Model Context Protocol (MCP)
MCP connects Claude to the "real world" (GitHub, Google Calendar, local DBs).

### Configuration
Managed in `.mcp.json` (Project) or `~/.claude/mcp.json` (Global).

### Adding a Server
```bash
claude mcp add my-tool --command "npx -y @modelcontextprotocol/server-github"
```

## Practical Tip
Use the **`skill-creator`** built-in skill:
`claude /skill-creator "Create a skill for [your specific task]"`
