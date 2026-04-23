# 🤖 Agent Setup & Reference

*Your AI agents configured and ready*

## Quick Start Commands

| Agent | Command | Description |
|-------|---------|-------------|
| **Pi (Ollama)** | `pi` | Interactive |
| **Pi (Fallback)** | `pifallback` | Auto-switch to Gemini |
| **Pi (One-shot)** | `pi -p "prompt"` | Single command |
| **Goose** | `goose run -t "prompt"` | One-shot |
| **Goose (Interactive)** | `goose session` | Chat mode |

## Tools Available

### Pi Agent - 4 Native Tools (Always On)
```
read   - Read files
write  - Create/overwrite files
edit   - Find & replace
bash   - Run commands
```

### Pi Agent - Read-Only Tools (Enable with --tools)
```
grep   - Search in files      ← ADDED
find   - Find files by pattern
ls     - List directory
```

### Enable Extra Tools
```bash
# Enable grep, find, ls
pi -p --tools "grep,find,ls" "Search for TODO in files"
```

---

## Models Available

| Provider | Model | Context | Use Case |
|----------|-------|---------|----------|
| Ollama | minimax-m2.5:cloud | 204K | Fast, local |
| Google | gemini-2.5-flash | 1M | Fallback |
| Google | gemini-3-flash-preview | 1M | Latest |

---

## Custom Tools Created

| Tool | Location | Purpose |
|------|----------|---------|
| `pifallback` | ~/.local/bin/pifallback | Auto-fallback to Gemini |
| `pi-harness` | ~/.local/bin/pi-harness | Project automation |
| `demo-pi` | ~/.local/bin/demo-pi | Social media demo |
| `greptool` | ~/.local/bin/greptool | Search files |

---

## Terminal Tools (Your System)

| Tool | Command | Purpose |
|------|---------|---------|
| **tmux** | `tmux new -s name` | Terminal sessions |
| **grep** | `grep -r "term" .` | Search files |
| **find** | `find . -name "*.md"` | Find files |

---

## Configuration Files

```
~/.pi/agent/
├── settings.json    # Default model, thinking level
├── models.json      # Provider configs
├── auth.json        # OAuth tokens
└── sessions/        # Chat history

~/.config/goose/
└── config.yaml      # Goose settings
```

---

## Examples

### Code Review with Grep
```bash
pi -p --tools "grep,read" "Find all TODO comments in this project"
```

### Find Files
```bash
pi -p --tools "find" "Find all Python files"
```

### Create Project with MCP
```bash
cd ~/Documents/Projects/01_hello_mcp
goose run -t "Add a new tool" --with-extension "python3 hello_mcp.py"
```

---

## New Tracks Added

Based on your learning:

### Terminal Mastery
- [[Terminal_Mastery]] - tmux, bash shortcuts, find, grep

### SQL Track
- [[SQL_Basics]] - SELECT, INSERT, UPDATE, DELETE
- [[01_SQLite_State_Management]] - SQLite deep dive
- [[PostgreSQL_Getting_Started]] - PostgreSQL setup

---

## Links

- [[00_Harness_Basics_Guide]] - Full harness guide
- [[03_MCP_Tool_Construction]] - Build custom tools
- [[SKILLS_INDEX|skills/SKILLS_INDEX]] - Your skills system
-  - Full learning roadmap