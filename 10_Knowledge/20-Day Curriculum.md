# 20-Day Learning Curriculum
**Temporal Execution Plan for the Phase-Based Roadmap**

---

## Phase 1 — Shell & Filesystem (Days 1–6)
*Target: Mastery of the local environment.*

- [x] **Day 1 — How Linux sees the world**
    - **Concept:** Filesystem tree, inodes, absolute vs relative paths.
    - **Build:** Map the local system.
    - **Links:** [[Linux Fundamentals]], [[Operating Systems#Filesystems]]
- [x] **Day 2 — Reading and writing files**
    - **Concept:** Stdin/Stdout, file descriptors, streams.
    - **Build:** Data manipulation with `echo`, `cat`, `head`, `tail`.
    - **Links:** [[Reading and Writing Files]]
- [x] **Day 3 — Pipes and filters**
    - **Concept:** Unix philosophy (modular tools).
    - **Build:** Chain `grep`, `wc`, `sort`, `uniq` to extract data.
    - **Links:** [[Linux Shell In-Depth]]
- [ ] **Day 4 — Permissions and ownership**
    - **Concept:** Multi-user security, `rwx` bits.
    - **Build:** Lock down files/folders with `chmod` and `chown`.
    - **Links:** [[Linux Fundamentals]], [[Operating Systems#Permissions]]
- [ ] **Day 5 — Shell scripting**
    - **Concept:** Automating sequences of commands.
    - **Build:** Create a `.sh` automated logging script.
    - **Links:** [[Programming#Bash]], [[Automation#Scripts]]
- [ ] **Day 6 — Text processing tools**
    - **Concept:** Pattern matching and text manipulation.
    - **Build:** Process CSV data using `sed`, `awk`, `cut`, and `tr`.
    - **Links:** [[Automation#CLI tools]]

---

## Phase 2 — Git & Version Control (Days 7–10)
*Target: Professional history tracking.*

- [ ] **Day 7 — What Git actually is**
    - **Concept:** Snapshots vs. Backups, the `.git` directory.
    - **Build:** Initialize a repo for this vault.
    - **Links:** [[Learning Infrastructure#Version Control (Git)]]
- [ ] **Day 8 — Reading history and differences**
    - **Concept:** Diffs, the commit log as a timeline.
    - **Build:** Use `git log` and `git diff` to trace changes.
    - **Links:** [[Learning Infrastructure#Version Control (Git)]]
- [ ] **Day 9 — Branches**
    - **Concept:** Parallel timelines and feature isolation.
    - **Build:** Branch, merge, and resolve a conflict.
    - **Links:** [[Learning Infrastructure#Version Control (Git)]]
- [ ] **Day 10 — GitHub and remotes**
    - **Concept:** Distributed version control and collaboration.
    - **Build:** Push the vault to a private GitHub remote.
    - **Links:** [[Learning Infrastructure#Version Control (Git)]]

---

## Phase 3 — Networking & APIs (Days 11–16)
*Target: Understanding the connected world.*

- [ ] **Day 11 — How the internet actually works**
    - **Concept:** IP, DNS, packets, and routing.
    - **Build:** Trace a request from your machine to a server.
    - **Links:** [[Networking#DNS]]
- [ ] **Day 12 — TCP, ports, and connections**
    - **Concept:** The TCP handshake, common service ports.
    - **Build:** Audit open ports and connections with `ss`.
    - **Links:** [[Networking#TCP/IP]]
- [ ] **Day 13 — HTTP: the language of the web**
    - **Concept:** Request/Response, Methods, Status Codes.
    - **Build:** Inspect raw HTTP traffic with `curl -v`.
    - **Links:** [[Networking#HTTP]]
- [ ] **Day 14 — JSON: the universal data format**
    - **Concept:** Key-value pairs, arrays, and structure.
    - **Build:** Parse complex JSON with `jq`.
    - **Links:** [[MCP and Tool Ecosystems#JSON structures]]
- [ ] **Day 15 — Calling real APIs**
    - **Concept:** REST architecture.
    - **Build:** Interact with free APIs (Weather, Jokes) via `curl`.
    - **Links:** [[MCP and Tool Ecosystems#tool APIs]]
- [ ] **Day 16 — API keys and authentication**
    - **Concept:** Bearer tokens and Header-based auth.
    - **Build:** Authenticate a request and handle secrets safely.
    - **Links:** [[MCP and Tool Ecosystems#tool APIs]]

---

## Phase 4 — Python & Putting It Together (Days 17–20)
*Target: Scripting and programmatic integration.*

- [ ] **Day 17 — Python fundamentals**
    - **Concept:** Data types, loops, and basic logic.
    - **Build:** A word frequency counter script.
    - **Links:** [[Programming#Python]]
- [ ] **Day 18 — Python + APIs**
    - **Concept:** The `requests` library.
    - **Build:** Programmatic API client in Python.
    - **Links:** [[Programming#Python]]
- [ ] **Day 19 — Python + files + shell**
    - **Concept:** File I/O and interacting with the OS.
    - **Build:** A script that fetches API data and saves it to CSV.
    - **Links:** [[Programming#Python]], [[Automation#Scripts]]
- [ ] **Day 20 — Integration day**
    - **Concept:** End-to-end workflow synthesis.
    - **Build:** A complete data pipeline script pushed to Git.
    - **Final Reflection:** Update Obsidian with "What I understand now."

---

## Phase 5 — Cognitive Systems & Agents (Days 21–25+)
*Target: Building cognitive tools and autonomous workflows.*

- [ ] **Day 21 — AI Agent Foundations**
    - **Concept:** Agentic architectures, memory, and planning loops.
    - **Build:** [[Startup Technical Guide - AI Agents]] (Chapter 1 & 2).
    - **Links:** [[Project - Agentic Systems]], [[LLM Architecture & Tokenization]]
- [ ] **Day 22 — Tool Use & MCP**
    - **Concept:** Model Context Protocol (MCP) and digital interaction.
    - **Build:** [[Startup Technical Guide - AI Agents]] (Chapter 3).
    - **Links:** [[MCP and Tool Ecosystems]]
- [ ] **Day 23 — Autonomous Workflows**
    - **Concept:** Designing self-healing systems and task decomposition.
    - **Build:** [[Startup Technical Guide - AI Agents]] (Chapter 4).
    - **Links:** [[Automation#Advanced]]
- [ ] **Day 24 — LLM Architecture Deep Dive**
    - **Concept:** Tokens, weights, and transformer models.
    - **Build:** Summarize the core differences between Gemini, Claude, and GPT.
    - **Links:** [[AI Systems#Architecture]]
- [ ] **Day 25 — The Universal Interface**
    - **Concept:** Building skills that work across any LLM (Universal skills).
    - **Build:** Create a "Universal Research Skill" for your vault.
    - **Links:** [[Project - Agentic Systems]]

---
*Last updated on 2026-03-27. Added Phase 5 for Agentic Systems.*
