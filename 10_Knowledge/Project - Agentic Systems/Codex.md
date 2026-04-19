---
Phase: [[Phase 8]]
Project: [[Project - Agentic Systems]]
Prev: [[Gemini CLI]] | Next: [[GitHub and good skills]]
---
# Codex CLI (OpenAI)

Codex CLI is an open-source, terminal-native AI coding agent developed by OpenAI. It allows you to run a multimodal coding assistant directly in your terminal, with deep access to your local files and shell.

## 1. Core Concepts
Codex CLI operates using local execution, giving it direct access to your system. 
- **Multimodal Support:** It can process text, screenshots, or diagrams.
- **Approval Modes:** Supports "Suggest", "Auto Edit", and "Full Auto" modes for applying changes.
- **MCP Support:** It integrates with the Model Context Protocol (MCP) to access external tools and APIs.

## 2. Agent Skills Framework
Codex uses **Agent Skills** to learn specific workflows, similar to Gemini CLI. It optimizes context window usage through **Progressive Disclosure**:
1. It only loads the metadata (Name & Description) of available skills initially.
2. It fully loads the instructions within a `SKILL.md` file only if it determines the skill is relevant to the task.

### Structure of a Skill
```text
my-custom-skill/
└── SKILL.md       (Required) Name, Description, and Instructions
```

### SKILL.md Example
```markdown
# Name
api-doc-generator

# Description
Use this skill when the user wants to generate API documentation.

# Instructions
1. Read the files in the /src directory.
2. Identify all exported functions.
3. Use the 'scripts/doc-gen.sh' to format the output.
```

## 3. Configuration & Paths
- **Installation:** `npm i -g @openai/codex`
- **Skill Locations:**
  - Project Level: `.agents/skills/`
  - Global Level: `~/.codex/skills/`

## Practical Tip
Use the `/skills` command in the interactive Codex TUI to list and manage available skills, or use the `$` prefix (e.g., `$api-doc-generator`) to explicitly force the activation of a specific skill.
