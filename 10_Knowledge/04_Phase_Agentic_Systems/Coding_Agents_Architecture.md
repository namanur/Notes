# Phase 5: Autonomous Mastery — Coding Agents & Architecture (Day 37)

## 🧠 Mental Model: Software Engineering via Agentic Loops
Coding agents (like Claude Code, Aider, or Gemini CLI) are not just "autocomplete"; they are **autonomous executors** that operate within a Sandbox-Terminal-Editor loop.

### The Execution Loop Internals
1.  **Context Assembly:** The agent uses `grep` and `ls` to map the codebase. It doesn't read every file; it reads the *map*.
2.  **Surgical Edits:** Using precise find-and-replace or diff-based tools. 
3.  **The Validation Pillar:** The agent MUST run a compiler/test-runner immediately after an edit. If it doesn't validate, it's just "hallucinating success."
4.  **Self-Correction:** Parsing compiler errors (stderr) to backtrack and fix its own logic.

**Brutal Truth:** A coding agent is only as good as the tests you provide. If you have zero tests, the agent will gracefully destroy your codebase while assuring you that it's "optimizing" it.

---

## 💻 Technical Deep Dive: Modern Coding Patterns

### 1. The "Plan-Act-Verify" Pattern
- **Plan:** Generate a markdown task list.
- **Act:** Execute shell commands and file edits.
- **Verify:** Run `pytest`, `npm test`, or custom check scripts.

### 2. Multi-File Refactoring
Agents use "Skeleton Tracking" to understand dependencies. If they change a function signature in `auth.py`, they must proactively search for usages in `app.py`.

---

## 🛠 Mastery Drills (High Pain)

### Drill 1: The Broken Legacy
1.  Find an old, undocumented Python script that fails with a complex `ImportError` or `AttributeError`.
2.  **Task:** Use an agent to fix it and add 100% test coverage.
3.  **Constraint:** You cannot provide any hints. The agent must discover the fix via `grep` and `sys.path` inspection.

### Drill 2: The Refactor Trap
1.  Provide a codebase where two classes are tightly coupled.
2.  Task the agent: "Decouple these classes using the Strategy Pattern."
3.  **Goal:** Force the agent to handle "Import Circularity" errors that arise during the refactor.

---

## 📜 Execution Contract

- **Timebox:** 180 Minutes.
- **Start Command:** `aider --model sonnet-3.5` or `gemini "Refactor current project"`
- **Completion Condition:** Successfully implement a new feature spanning 3+ files with passing unit and integration tests, verified by a CI-style shell command.

---
**Links:**
- [[ROADMAP.md]]
- [[Claude Code]]
- [[Aider]]
- [[Codex]]
