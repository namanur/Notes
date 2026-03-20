# Repository Guidelines

## Project Structure & Module Organization
This repository is an Obsidian vault for personal knowledge management, not a compiled software project. Content is organized by role:

- `00_daily_logs/`: Daily notes named `DD-MM-YYYY.md`, created from `Daily log template.md`.
- `10_Knowledge/`: Long-form knowledge notes, grouped by projects such as `Project - The Learning Machine/` and `Project - Agentic Systems/`.
- `99_System/`: Vault meta-docs, indexes, and agent instructions such as `Topics.md`, `Starting.md`, and agent-specific guidance.
- `.obsidian/`: Vault configuration, themes, and plugin settings. Edit only when intentionally changing workspace behavior.

## Build, Test, and Development Commands
There is no build pipeline or automated test suite in this vault. Common maintenance commands are lightweight:

- `rg --files`: List notes quickly.
- `rg -n "term" 10_Knowledge 99_System`: Find references before renaming or consolidating notes.
- `ls 00_daily_logs`: Review recent daily entries.

Open the vault in Obsidian for normal editing and link management.

## Coding Style & Naming Conventions
Write notes in Markdown with short sections and descriptive headings. Prefer:

- Title Case headings.
- Hyphen bullets for lists.
- Obsidian wikilinks like `[[Topics]]` for internal references.
- Folder prefixes such as `00_`, `10_`, and `99_` to preserve ordering.

Keep daily logs in `DD-MM-YYYY.md` format. For topical notes, use clear names that match the subject, for example `Claude Code.md` or `00_Overview.md`.

## Testing Guidelines
Quality checks are manual. Before committing changes:

- Verify links resolve in Obsidian after renames.
- Confirm new notes are placed in the correct folder.
- Keep roadmap updates in sync with `99_System/Topics.md` when progress changes.
- For daily notes, preserve the template structure: `To Do` and `What I Did`.

## Commit & Pull Request Guidelines
This directory is a Git repository. Use short imperative commit messages such as `Add Phase 11 skill notes` or `Update daily log template`.

Commit regularly to track progress and sync with the remote repository. Pull requests should summarize changed areas, note any renamed files, and mention whether `.obsidian/` settings were modified, since those affect all vault users.

## Agent-Specific Notes
Treat `99_System/Agents/` and related instruction files as source-of-truth guidance for AI assistants working in this vault. Keep agent docs concise, repository-specific, and aligned with actual folder structure.
