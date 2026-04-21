Universal skills live in /skills — read SKILLS_INDEX.md before starting any structured task.
## Wiki Integration Mandate
- **Distillation**: Every significant technical synthesis in  must be cross-referenced or distilled into a permanent entity/concept page in .
- **Compounding**: Prioritize updating existing wiki pages over creating duplicate notes in the vault.
- **Verification**: Use the  skill to automate the ingestion and interlinking process.

## Repository Guidelines
This repository is an Obsidian vault for personal knowledge management, not a compiled software project. Content is organized by role:

- : Daily notes named , created from .
- : Long-form knowledge notes, grouped by projects such as  and .
- : Vault meta-docs, indexes, and agent instructions such as , , , and agent-specific guidance.
- : Vault configuration, themes, and plugin settings. Edit only when intentionally changing workspace behavior.

## Build, Test, and Development Commands
There is no build pipeline or automated test suite in this vault. Common maintenance commands are lightweight:

- agent_log_gemini_skill_content.md
date.txt
projects/peak-protocol/manifesto.md
projects/peak-protocol/founding-interview.md
control center.base
VAULT_INDEX.md
ROADMAP.md
README.md
LICENSE
AGENTS.md
GEMINI.md
skills/study_material_builder.md
skills/web_browse.md
skills/agent_activity.md
skills/wiki_maintainer.md
skills/session_close.md
skills/SKILLS_INDEX.md
skills/strategy_log.md
skills/syllabus_builder.md
skills/vault_indexing.md
skills/daily_log.md
000_START_HERE.md
10_Knowledge/02_Phase_Architecture_Networking/Network_Fundamentals.md
10_Knowledge/Understanding YAML.md
10_Knowledge/03_Phase_Data_Middleware/PostgreSQL_Basics_Security.md
10_Knowledge/03_Phase_Data_Middleware/Python_SQLite_State_Management.md
10_Knowledge/03_Phase_Data_Middleware/Python_CLI_Engineering.md
10_Knowledge/03_Phase_Data_Middleware/Python_Engineering_Fundamentals.md
10_Knowledge/03_Phase_Data_Middleware/SQLite_Primitives_Internal.md
10_Knowledge/03_Phase_Data_Middleware/Docker_Containerization.md
10_Knowledge/03_Phase_Data_Middleware/PostgreSQL_Mastery.md
10_Knowledge/03_Phase_Data_Middleware/PostgreSQL_Getting_Started.md
10_Knowledge/03_Phase_Data_Middleware/SQL_Basics.md
10_Knowledge/03_Phase_Data_Middleware/00_Harness_Basics_Guide.md
10_Knowledge/03_Phase_Data_Middleware/03_MCP_Tool_Construction.md
10_Knowledge/03_Phase_Data_Middleware/02_Python_API_Wrappers.md
10_Knowledge/03_Phase_Data_Middleware/01_SQLite_State_Management.md
10_Knowledge/04_Phase_Agentic_Systems/Reasoning_Chains_Patterns.md
10_Knowledge/04_Phase_Agentic_Systems/Context_Providers_Strategy.md
10_Knowledge/04_Phase_Agentic_Systems/LLM_Architecture_Internals.md
10_Knowledge/04_Phase_Agentic_Systems/MCP_Resources_Architecture.md
10_Knowledge/04_Phase_Agentic_Systems/MCP_Tools_Development.md
10_Knowledge/04_Phase_Agentic_Systems/UNIVERSAL_AGENT_BUILDER.md
10_Knowledge/04_Phase_Agentic_Systems/CERTIFICATION_STATUS.md
10_Knowledge/04_Phase_Agentic_Systems/CERTIFICATION_TRACKER.md
10_Knowledge/04_Phase_Agentic_Systems/Startup Technical Guide - AI Agents.md
10_Knowledge/04_Phase_Agentic_Systems/Resources/startup_technical_guide_ai_agents_final.pdf
10_Knowledge/04_Phase_Agentic_Systems/AI_Agent_Blueprint_Startup_Guide.png
10_Knowledge/04_Phase_Agentic_Systems/Google_Cloud_AI_Agents_Strategy.md
10_Knowledge/04_Phase_Agentic_Systems/GitHub and good skills.md
10_Knowledge/04_Phase_Agentic_Systems/Codex.md
10_Knowledge/04_Phase_Agentic_Systems/Gemini CLI.md
10_Knowledge/04_Phase_Agentic_Systems/Claude Code.md
10_Knowledge/04_Phase_Agentic_Systems/00_Overview.md
10_Knowledge/01_Phase_Infrastructure_Shell/GitHub_Remotes.md
10_Knowledge/01_Phase_Infrastructure_Shell/Git_Branching_Merging.md
10_Knowledge/01_Phase_Infrastructure_Shell/Git_History_Diffs.md
10_Knowledge/01_Phase_Infrastructure_Shell/Sed_Awk_Mastery.md
10_Knowledge/01_Phase_Infrastructure_Shell/Shell_Scripting_Basics.md
10_Knowledge/01_Phase_Infrastructure_Shell/Permissions_Ownership.md
10_Knowledge/01_Phase_Infrastructure_Shell/Git_Internals_DAG.md
10_Knowledge/01_Phase_Infrastructure_Shell/Bash_Scripting_Course.md
10_Knowledge/01_Phase_Infrastructure_Shell/Terminal_Mastery.md
10_Knowledge/01_Phase_Infrastructure_Shell/Mastering Awk.md
10_Knowledge/01_Phase_Infrastructure_Shell/Mastering Sed.md
10_Knowledge/01_Phase_Infrastructure_Shell/Mastering Grep.md
10_Knowledge/01_Phase_Infrastructure_Shell/Command Mastery Lab.md
10_Knowledge/01_Phase_Infrastructure_Shell/Linux Shell In-Depth.md
10_Knowledge/01_Phase_Infrastructure_Shell/Pipes and Filters.md
10_Knowledge/01_Phase_Infrastructure_Shell/Reading and Writing Files.md
10_Knowledge/01_Phase_Infrastructure_Shell/Linux Fundamentals.md
10_Knowledge/01_Phase_Infrastructure_Shell/Workflow and Information Capture.md
10_Knowledge/01_Phase_Infrastructure_Shell/Personal Knowledge Management.md
10_Knowledge/01_Phase_Infrastructure_Shell/Git and GitHub Setup.md
99_System/SKILLS_REFERENCE.md
99_System/MY_CONTEXT.md
99_System/Agent_Setup.md
99_System/SYLLABUS.md
99_System/audit_todos.py
99_System/here we go.md
99_System/sync_to_drive.py
99_System/Topics.md
99_System/Archive/Logs/sync_log.md
99_System/agents/Claude.md
99_System/agents/Gemini.md
99_System/agents/Aider.md
99_System/agents/Codex.md
00_daily_logs/13-03-2026.md
00_daily_logs/audit_log.md
00_daily_logs/sync_log.md
00_daily_logs/20-03-2026.md
00_daily_logs/18-03-2026.md
00_daily_logs/Daily log template.md
00_daily_logs/20-04-2026.md
00_daily_logs/31-03-2026.md
00_daily_logs/AGENT_ACTIVITY.md
00_daily_logs/21-04-2026.md: List notes quickly.
- 99_System/MY_CONTEXT.md:16:- Learning terminal mastery (tmux, bash)
99_System/Agent_Setup.md:66:| **grep** | `grep -r "term" .` | Search files |
10_Knowledge/04_Phase_Agentic_Systems/Reasoning_Chains_Patterns.md:6:Standard LLM responses are "Fast" (System 1). **Reasoning Chains** force the model into "Slow" (System 2) thinking. By generating a sequence of intermediate "thought" tokens, the model allocates more computation to the logical path before arriving at the final answer.
10_Knowledge/04_Phase_Agentic_Systems/LLM_Architecture_Internals.md:25:- **Temperature:** Scales the logits (raw probabilities). `0.0` = Deterministic (Greedy); `1.0` = Natural; `2.0` = Creative Chaos.
10_Knowledge/03_Phase_Data_Middleware/SQLite_Primitives_Internal.md:61:1. **The WAL Lockout:** Open two terminal sessions. In Session A, start a long-running transaction (`BEGIN; UPDATE...`). In Session B, try to `DROP TABLE`. Observe the `database is locked` error. Now, switch to WAL mode and see how `SELECT` still works in Session B while Session A is writing.
10_Knowledge/04_Phase_Agentic_Systems/MCP_Tools_Development.md:8:1. **The Schema is the Reality:** If your tool description is vague, the agent will hallucinate parameters. The schema is the only interface between the LLM's probabilistic weights and your deterministic code.
10_Knowledge/03_Phase_Data_Middleware/00_Harness_Basics_Guide.md:53:| **CLI Harness** | AI talks to terminal | Pi Agent, Goose |
10_Knowledge/03_Phase_Data_Middleware/00_Harness_Basics_Guide.md:93:# Run any terminal command
10_Knowledge/04_Phase_Agentic_Systems/Codex.md:8:Codex CLI is an open-source, terminal-native AI coding agent developed by OpenAI. It allows you to run a multimodal coding assistant directly in your terminal, with deep access to your local files and shell.
10_Knowledge/04_Phase_Agentic_Systems/Codex.md:19:2. It fully loads the instructions within a `SKILL.md` file only if it determines the skill is relevant to the task.
10_Knowledge/03_Phase_Data_Middleware/01_SQLite_State_Management.md:5:Summary: Building the persistence layer for agent state and long-term memory.
10_Knowledge/04_Phase_Agentic_Systems/00_Overview.md:11:In this setup, we focus on primary terminal-based AI agents, each with unique extension patterns:
10_Knowledge/04_Phase_Agentic_Systems/Google_Cloud_AI_Agents_Strategy.md:29:*   **Orchestration frameworks (like ReAct)**: Orchestration acts as the agent's executive function, guiding it through multi-step tasks by determining which tools to use and in what sequence.
10_Knowledge/04_Phase_Agentic_Systems/Google_Cloud_AI_Agents_Strategy.md:32:    *   Frameworks like the ADK facilitate this via specific agent architectures, including LlmAgents for flexible non-deterministic reasoning, and workflow agents (Sequential, Parallel, Loop) for structured, deterministic control.
10_Knowledge/04_Phase_Agentic_Systems/Google_Cloud_AI_Agents_Strategy.md:34:    *   **Long-term knowledge base (Grounding/Retrieval)**: Uses services like Vertex AI Search for unstructured data, Firestore for conversational history and state management, Cloud Storage as a raw data lake, and BigQuery for analytical queries.
10_Knowledge/01_Phase_Infrastructure_Shell/Personal Knowledge Management.md:35:- **Precision of Thought**: Writing forces you to define terms and logic clearly, which is essential for engineering.
10_Knowledge/01_Phase_Infrastructure_Shell/Terminal_Mastery.md:10:- **Multiple windows** in one terminal
10_Knowledge/01_Phase_Infrastructure_Shell/Shell_Scripting_Basics.md:7:- **Execution Environment:** Scripts run in a **subshell**. Variables defined in a script do not persist in your main terminal unless you `source` the script.
10_Knowledge/01_Phase_Infrastructure_Shell/Mastering Grep.md:28:Search for multiple terms at once:
10_Knowledge/01_Phase_Infrastructure_Shell/Command Mastery Lab.md:41:| `tee` | Splits a stream (saves to file AND shows in terminal). | `ls | tee output.txt` |
10_Knowledge/01_Phase_Infrastructure_Shell/Command Mastery Lab.md:47:*Run these in your terminal to see the "Unix Philosophy" in action:*
10_Knowledge/01_Phase_Infrastructure_Shell/Command Mastery Lab.md:62:   List your files, see them in the terminal, but also save them to a file:
10_Knowledge/01_Phase_Infrastructure_Shell/Reading and Writing Files.md:43:*Try these in your terminal:*
10_Knowledge/01_Phase_Infrastructure_Shell/Linux Shell In-Depth.md:17:- **Stdout (1):** Standard Output (default: terminal screen)
10_Knowledge/01_Phase_Infrastructure_Shell/Linux Shell In-Depth.md:18:- **Stderr (2):** Standard Error (default: terminal screen)
10_Knowledge/01_Phase_Infrastructure_Shell/Linux Fundamentals.md:15:Every other program (terminal, browser, Python) runs on top and asks the kernel for permission. When using the terminal, you're talking to a **[[Linux Shell In-Depth|shell]]** (like [[Linux Shell In-Depth|bash]]), which is a program that makes requests to the kernel for you.: Find references before renaming or consolidating notes.
- 13-03-2026.md
18-03-2026.md
20-03-2026.md
20-04-2026.md
21-04-2026.md
31-03-2026.md
AGENT_ACTIVITY.md
audit_log.md
Daily log template.md
sync_log.md: Review recent daily entries.

Open the vault in Obsidian for normal editing and link management.

## Coding Style & Naming Conventions
Write notes in Markdown with short sections and descriptive headings. Prefer:

- Title Case headings.
- Hyphen bullets for lists.
- Obsidian wikilinks like  for internal references.
- Folder prefixes such as , , and  to preserve ordering.

Keep daily logs in  format. For topical notes, use clear names that match the subject, for example  or .

## Testing Guidelines
Quality checks are manual. Before committing changes:

- Verify links resolve in Obsidian after renames.
- Confirm new notes are placed in the correct folder.
- Keep roadmap updates in sync with  when progress changes.
- For daily notes, preserve the template structure:  and .

## Commit & Pull Request Guidelines
This directory is a Git repository. Use short imperative commit messages such as  or .

Commit regularly to track progress and sync with the remote repository. Pull requests should summarize changed areas, note any renamed files, and mention whether  settings were modified, since those affect all vault users.

## Agent-Specific Notes
Treat  and related instruction files as source-of-truth guidance for AI assistants working in this vault. Keep agent docs concise, repository-specific, and aligned with actual folder structure.

