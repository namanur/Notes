# GitHub and Good Skills (Phase 11)

Combining **Git** with **Skill Systems** is a powerful pattern for creating reproducible, expert-driven agents.

## 1. Git for Skill Management
Skills should be treated like code: version-controlled, modular, and collaborative.

- **Modular Repos**: Host individual specialized skills in their own Git repos.
- **Git Submodules**: Use submodules to manage a collection of skills within your main agent configuration.
- **`gemini skills install <url>`**: The Gemini CLI can directly install skills from GitHub URLs.

## 2. Defining "Good" Skills
A high-quality skill follows several principles:

### I. Descriptive Metadata
The `description` in `SKILL.md` is the "trigger" for the model. It should clearly define *what* the skill does and *when* it should be activated.

### II. Procedural Clarity
Instructions should be step-by-step and focus on *how* to perform a task, rather than just what the task is.

### III. Tool Integration
Good skills often wrap a specific tool or script (e.g., a Python audit script or a specialized CLI like `gws`).

### IV. Safety & Constraints
Always include constraints in your skills to prevent the agent from taking destructive actions without confirmation.

## 3. Recommended Skill Repositories
- [Google Workspace (GWS) Skills](https://github.com/googleworkspace/cli)
- [Gemini Community Skills](https://github.com/google-gemini/gemini-skills)
