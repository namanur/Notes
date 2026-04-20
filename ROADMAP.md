# ROADMAP

**The 40-Day Execution Plan for Computational Mastery and Autonomous Systems**

This document merges the tactical daily execution model with the comprehensive "Full Learning Curve" syllabus. It replaces both the old `SYLLABUS.md` and the `20-Day Curriculum.md`.

---

## Phase 1 — Infrastructure & Shell Primitives (Days 1–10)
*Target: Mastery of the local environment and version control.*
**Project: [[Project - The Learning Machine]] & [[Project - Linux System Hardening]]**

- [x] **Day 1 — How Linux sees the world**
    - **Build:** Map the local system.
    - **Links:** [[Linux Fundamentals]], [[Personal Knowledge Management]]
- [x] **Day 2 — Reading and writing files**
    - **Build:** Data manipulation with `echo`, `cat`, `head`, `tail`.
    - **Links:** [[Reading and Writing Files]], [[Workflow and Information Capture]]
- [x] **Day 3 — Pipes and filters**
    - **Build:** Chain `grep`, `wc`, `sort`, `uniq` to extract data.
    - **Links:** [[Linux Shell In-Depth]]
- [ ] **Day 4 — Permissions and ownership**
    - **Build:** Lock down files/folders with `chmod` and `chown`.
    - **Links:** [[Linux Fundamentals]]
- [ ] **Day 5 — Shell scripting**
    - **Build:** Create a `.sh` automated logging script.
- [ ] **Day 6 — Text processing tools (Sed/Awk)**
    - **Build:** Process CSV data using `sed`, `awk`, `cut`, and `tr`.
    - **Links:** [[Mastering Sed]], [[Mastering Awk]]
- [ ] **Day 7 — What Git actually is**
    - **Build:** Initialize a repo for this vault.
    - **Links:** [[Git and GitHub Setup]]
- [ ] **Day 8 — Reading history and differences**
    - **Build:** Use `git log` and `git diff` to trace changes.
- [ ] **Day 9 — Branches and Merging**
    - **Build:** Branch, merge, and resolve a conflict.
- [ ] **Day 10 — GitHub and remotes**
    - **Build:** Push the vault to a private GitHub remote.

---

## Phase 2 — Architecture & Networking Foundations (Days 11–15)
*Target: Understanding hardware limits and internet protocols.*

- [ ] **Day 11 — Computational Thinking**
    - **Concept:** Binary, Logic Gates, and Algorithms.
- [ ] **Day 12 — Computer Architecture**
    - **Concept:** CPU, Memory Hierarchy, and Assembly Basics.
- [ ] **Day 13 — Internet Infrastructure**
    - **Concept:** TCP/IP, DNS, and Routing.
    - **Build:** Trace a request from your machine to a server.
- [ ] **Day 14 — HTTP: the language of the web**
    - **Concept:** Request/Response, Methods, Status Codes.
    - **Build:** Inspect raw HTTP traffic with `curl -v`.
- [ ] **Day 15 — JSON & Web APIs**
    - **Concept:** Key-value pairs and REST architecture.
    - **Build:** Fetch and parse remote JSON data with `jq`.

---

## Phase 3 — Data & Middleware Engineering (Days 16–22)
*Target: Building the execution and persistence layers.*
**Project: [[Project - Harness Engineering]]**

- [ ] **Day 16 — SQLite Primitives (State Management)**
    - **Build:** Create a `memory.db` for tracking learning progress.
    - **Links:** [[01_SQLite_State_Management]]
- [ ] **Day 17 — Python Fundamentals**
    - **Build:** A word frequency counter script.
- [ ] **Day 18 — Python CLI Wrappers**
    - **Build:** Write a Python script using `subprocess` to execute shell commands.
    - **Links:** [[02_Python_API_Wrappers]]
- [ ] **Day 19 — Python + SQLite (Middleware)**
    - **Build:** Build a CLI tool that logs agent "thoughts" to SQLite.
- [ ] **Day 20 — API Integration & Security**
    - **Build:** Call an external API safely using environment variables.
- [ ] **Day 21 — Servers and Virtualization**
    - **Concept:** Hosting applications and isolating environments.
- [ ] **Day 22 — Docker and Containers**
    - **Build:** Containerize your Python SQLite CLI tool.

---

## Phase 4 — Agentic Systems & Harness Construction (Days 23–30)
*Target: Building the Model Context Protocol layer and understanding AI architecture.*
**Project: [[Project - Agentic Systems]] & [[Project - Harness Engineering]]**

- [x] **Day 23 — AI Agent Foundations**
    - **Links:** [[00_Overview]], [[Claude Code]], [[Gemini CLI]], [[Codex]]
- [ ] **Day 24 — Tool Use & Planning Loops**
    - **Links:** [[Google_Cloud_AI_Agents_Strategy]], [[Startup Technical Guide - AI Agents]]
- [ ] **Day 25 — MCP Protocol Basics**
    - **Build:** Implement a basic "Hello World" MCP server in Python.
    - **Links:** [[03_MCP_Tool_Construction]]
- [ ] **Day 26 — MCP Tools (The Action Layer)**
    - **Build:** Convert your Day 19 CLI tool into an MCP Tool.
- [ ] **Day 27 — MCP Resources (The Data Layer)**
    - **Build:** Connect your vault files to an MCP Resource provider.
- [ ] **Day 28 — Integrating MCP with Agents**
    - **Build:** Run `gemini-cli` with your custom MCP server attached.
- [ ] **Day 29 — LLM Architecture Deep Dive**
    - **Concept:** Tokens, weights, and transformer models.
- [ ] **Day 30 — Automation & CI/CD**
    - **Build:** Set up Cron Jobs for automated system audits.

---

## Phase 5 — Autonomous Workflows & Skills (Days 31–40)
*Target: Designing AI systems that run complex, independent workflows.*

- [x] **Day 31 — Skill Systems Foundations**
    - **Links:** [[GitHub and good skills]]
- [ ] **Day 32 — Universal Skill Authoring**
    - **Build:** Create a "Universal Research Skill" for your vault.
- [ ] **Day 33 — Context Providers**
    - **Build:** Develop an MCP Context Provider for dynamic prompt injection.
- [ ] **Day 34 — Reasoning Chains**
    - **Concept:** Designing self-healing systems and task decomposition.
- [ ] **Day 35 — OpenSpace MCP Bridge**
    - **Build:** Link isolated framework tools to your CLI agent.
    - **Links:** [[OpenSpace MCP Bridge]]
- [ ] **Day 36 — Research Agents**
    - **Build:** Deploy an agent solely responsible for maintaining the knowledge base.
- [ ] **Day 37 — Coding Agents**
    - **Build:** Delegate a refactoring task to an agent via MCP tools.
- [ ] **Day 38 — Multi-Agent Communication**
    - **Concept:** Enabling agents to hand off tasks to specialized sub-agents.
- [ ] **Day 39 — The Full Loop (Autonomous Prototype)**
    - **Build:** Have an agent use your custom MCP tool to update its own memory in SQLite.
- [ ] **Day 40 — Final Synthesis**
    - **Build:** Refactor the entire ROADMAP based on verified agentic capabilities.
