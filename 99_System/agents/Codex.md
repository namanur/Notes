Universal skills live in /skills — read SKILLS_INDEX.md before starting any structured task.
# Codex Agent Configuration

## Agent Skills Framework
Codex uses Progressive Disclosure to manage token limits.

### Skill Locations
1. Workspace: `.agents/skills/`
2. User: `~/.codex/skills/`

## Configuration
- Installation: `npm i -g @openai/codex`

## Common Commands
- `codex` (Start TUI)
- `/skills` (List and manage skills)
- `/model <name>` (Switch model)
- `$<skill-name>` (Explicitly trigger a skill)
