# Claude Certified Architect - Foundations Dashboard

## 📊 Preparation Overview
- **Exam Target:** Claude Certified Architect – Foundations
- **Status:** 🔴 Just Started
- **Learning Roadmap Link:** [[Topics]]
- **20-Day Curriculum Link:** [[20-Day Curriculum]]

---

## 🏛️ Domain Breakdown

### Domain 1: Agentic Architecture & Orchestration (27%)
- [ ] **1.1 Agentic Loops:** Design/implement loops, `stop_reason` handling.
- [ ] **1.2 Multi-Agent Systems:** Hub-and-spoke, coordinator-subagent patterns.
- [ ] **1.3 Subagent Invocation:** `Task` tool, context passing, `AgentDefinition`.
- [ ] **1.4 Workflows:** Programmatic enforcement (hooks) vs. prompt guidance.
- [ ] **1.5 SDK Hooks:** `PostToolUse`, data normalization, compliance rules.
- [ ] **1.6 Decomposition:** Fixed pipelines vs. dynamic adaptive plans.
- [ ] **1.7 Session Management:** Resumption (`--resume`), forking, state persistence.

### Domain 2: Tool Design & MCP Integration (18%)
- [ ] **2.1 Tool Interfaces:** Differentiated descriptions, input/output contracts.
- [ ] **2.2 Error Handling:** `isError`, `isRetryable`, structured metadata.
- [ ] **2.3 Tool Choice:** Scoped access, `tool_choice` configuration (`auto`, `any`, forced).
- [ ] **2.4 MCP Integration:** `.mcp.json` vs `~/.claude.json`, resources for catalogs.
- [ ] **2.5 Built-in Tools:** Effective use of `Grep`, `Glob`, `Read`, `Write`, `Edit`.

### Domain 3: Claude Code Configuration & Workflows (20%)
- [ ] **3.1 CLAUDE.md:** Hierarchy (user/project/directory), `@import`, `.claude/rules/`.
- [ ] **3.2 Slash Commands & Skills:** `.claude/commands/`, `SKILL.md`, `context: fork`.
- [ ] **3.3 Path-specific Rules:** Glob patterns for conditional convention loading.
- [ ] **3.4 Execution Modes:** Plan mode vs. Direct execution, `Explore` subagent.
- [ ] **3.5 Iterative Refinement:** Interview pattern, Test-driven iteration.
- [ ] **3.6 CI/CD Integration:** Non-interactive mode (`-p`), structured JSON output.

### Domain 4: Prompt Engineering & Structured Output (20%)
- [ ] **4.1 Precision:** Specific review criteria, reducing false positives.
- [ ] **4.2 Few-Shot Prompting:** Targeted examples for ambiguous scenarios.
- [ ] **4.3 JSON Schemas:** Enforcing output via `tool_use`, nullable fields.
- [ ] **4.4 Validation Loops:** Retry-with-error-feedback, self-correction.
- [ ] **4.5 Batch Processing:** Message Batches API, cost vs. latency tradeoffs.
- [ ] **4.6 Multi-Pass Architectures:** Independent review instances, cross-file analysis.

### Domain 5: Context Management & Reliability (15%)
- [ ] **5.1 Context Optimization:** "Lost in the middle," trimming verbose outputs.
- [ ] **5.2 Escalation:** Human-in-the-loop, policy gap identification.
- [ ] **5.3 Error Propagation:** Recovery decisions, distinguishing access vs. empty results.
- [ ] **5.4 Large Codebases:** Scratchpad files, `/compact` usage, crash recovery.
- [ ] **5.5 Human Review:** Confidence scoring, stratified random sampling.
- [ ] **5.6 Provenance:** Claim-source mappings, conflict annotation.

---

## 🎭 Scenario Practice Tracker
*Practice these scenarios using your Lab environment.*
1. [ ] **Scenario 1:** Customer Support Resolution Agent (MCP + Escalation)
2. [ ] **Scenario 2:** Code Generation with Claude Code (CLAUDE.md + Plan Mode)
3. [ ] **Scenario 3:** Multi-Agent Research System (Agent SDK + Subagents)
4. [ ] **Scenario 4:** Developer Productivity Tools (Built-in tools + MCP)
5. [ ] **Scenario 5:** Claude Code for CI (Pipelines + Automation)
6. [ ] **Scenario 6:** Structured Data Extraction (JSON Schema + Validation)

---

## 📂 Key Resources
- **Official Guide:** [[Calude ecam prep.pdf]]
- **My Notes:** [[Linux Fundamentals]], [[Operating Systems]]
