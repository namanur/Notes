Universal skills live in /skills — read SKILLS_INDEX.md before starting any structured task.
# GEMINI.md - Notes Vault Instructional Context

## Workspace Configuration
- **Vault:** `/home/naman/Documents/Notes/` (This directory)
- **Downloads:** `/home/naman/Downloads/`
- **Rule:** Whenever the user says "go to my vault", read this file (`GEMINI.md`) for the ground truth context.

## Directory Overview
This directory is an **Obsidian Vault** and **GitHub Repository** designed for tracking a long-term "Full Learning Curve" from computational basics to autonomous systems. It functions as a Personal Knowledge Management (PKM) system where learning is documented, indexed, and linked across multiple layers: runtime (daily logs), memory (knowledge base), and architecture (systems meta-layer).

- **Environment:** Linux (Fedora)
- **Primary Tool:** Obsidian (Markdown-based)
- **Version Control:** Git (GitHub Repository)
- **Workflow:** Daily logging with a "Phase-based" learning roadmap.

## Structure and Organization
The vault is organized into functional layers:

1.  **`00_daily_logs/`**: Runtime execution. Contains daily logs named `DD-MM-YYYY.md` using `Daily log template.md`.
2.  **`10_Knowledge/`**: Memory layer. Organized by the 12 learning phases defined in the roadmap.
3.  **`99_System/`**: Architecture/Meta layer. Stores the logic and configuration of the vault itself.
4.  **`08_Work/`**: Project-specific or professional documentation.

## Key Files
- **`99_System/here we go.md`**: The master strategy document defining the 12-phase learning trajectory.
- **`99_System/Topics.md`**: The active Learning Roadmap (Index) with checklists for tracking progress across phases.
- **`Starting.md`**: Historical context and the origin of the current vault structure (Fedora migration).
- **`Daily log template.md`**: The standardized structure for daily check-ins.
- **`10_Knowledge/04_Phase_Agentic_Systems/Agent_Architect_Manual/00_MANUAL_INDEX.md`**: The entry point for the Agent Architect Manual v2.2.
- **`10_Knowledge/04_Phase_Agentic_Systems/Agent_Architect_Manual/_SYSTEM/SESSION_LOG.md`**: The build ledger for the manual.

## Architectural Boundaries
- **OpenSpace Repository:** Active development/experimentation.
- **Deployment Target:** **Dell Ubuntu Server** (`192.168.31.250`) as the primary environment for the OpenSpace MCP server.
- **Resource Note:** Monitor 4GB RAM usage closely due to co-existence with ERPNext and Samba.
- **Project Scope:** All agent-built code for the manual must run on Ubuntu Server 22.04+ using free-tier APIs only (v2.2 protocol).

## Usage and Conventions
- **Renaming:** Obsidian is configured to `alwaysUpdateLinks: true`. Renaming a file will automatically update all internal links.
- **Linking:** Extensive use of `Internal Links` is encouraged to connect ideas across the 12 phases.
- **Daily Logs:** Used to track tasks ("To Do") and progress ("What I Did") on a daily basis.
- **Roadmap Tracking:** `Topics.md` serves as the high-level progress tracker; check off items as they are mastered.

## Active Learning Projects (Roadmap)
- Project: The Learning Machine (Infrastructure)
- ...
- Project: Agentic Systems (Detailed notes for Claude, Gemini, Codex, and Aider are available).
- Project: Agent Architect Manual (v2.2) — Building a layered study system for agentic engineering.

---
*This file serves as the ground truth for Gemini CLI's understanding of this workspace.*
