---
Phase: [[Phase 8]]
Project: [[04_Phase_Agentic_Systems]]
Prev: [[Claude Code]] | Next: [[Codex]]
---
# Gemini CLI (Agent Skills)

Gemini CLI uses a standard called **Agent Skills** (AgentSkills.io) to add specialized expertise to the model on-the-fly.

## 1. How it Works
Skills are activated based on a semantic match between your prompt and the **`description`** in the `SKILL.md` frontmatter.

### Skill Hierarchy
1. **Workspace**: `.gemini/skills/` or `.agents/skills/` (Project-specific).
2. **User**: `~/.gemini/skills/` or `~/.agents/skills/` (Global across machine).
3. **Extension**: Bundled in Gemini CLI extensions.

## 2. Structure of a Skill
```text
my-expertise/
├── SKILL.md       (Required) Instructions and metadata
├── scripts/       (Optional) Specialized tools (e.g. audit.py)
├── references/    (Optional) Context files (e.g. API docs)
└── assets/        (Optional) Output templates
```

### SKILL.md Definition
```markdown
---
name: my-expertise
description: Expert in analyzing [domain]. Trigger on [keyword].
---
# Instructions
- Adhere to X guidelines.
- Use the bundled tool in `./scripts`.
```

## 3. Configuration & Commands
In-session commands:
- `/skills list`: See what's available.
- `/skills enable <name>`: Force activation.
- `/skills reload`: Sync after editing.

Terminal management:
- `gemini skills list`
- `gemini skills install <url>`
- `gemini skills link <local-path>`

## Practical Tip
Use the **`skill-creator`** skill in Gemini CLI:
`"create a new skill called 'api-tester' for auditing endpoints"`
