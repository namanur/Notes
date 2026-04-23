# Generated Context: L0 Foundation
> Auto-generated. Do not hand-edit.

## Key Concepts Established
- Agent Loop Mechanics (Perception → Memory → Reasoning → Action → Output)
- Grounding via feedback loops to prevent reasoning-environment decoupling
- Separation of Reasoning (Cloud APIs) from State/Memory (Local Hardware)
- Compute Liquidity and Resilience through provider fallback hierarchies
- Hardware Discipline: Restricting the Dell server to state management only (4GB RAM constraint)
- Mechanical Trap of LLM statelessness requiring manual context re-injection
- Token-based economy and the risks of Context Bloat on free-tier APIs
- JSON-RPC as the structural protocol for Tool Use and Action execution
- Harness as the minimal chassis/wrapper for Agent-Environment interaction

## Terms Defined
- Compute Liquidity: The ability to switch reasoning providers (e.g., via fallback scripts) without system failure or logic loss.
- Primary Harness: The main execution interface (e.g., Gemini CLI) that packages the filesystem and manages API streaming.
- Token: A mathematical chunk of text (roughly 4 characters) used as the basic unit of LLM processing.
- Mechanical Trap: The technical constraint where an LLM has no inherent memory between API calls, requiring context persistence by the harness.
- Context Bloat: The accumulation of unnecessary tokens in a window, leading to increased costs and reduced agent focus.
- JSON-RPC: The structured communication protocol used to format tool requests and responses between the reasoning engine and the harness.

## Tools / Files Built
- _SYSTEM/FALLBACK_CHAIN.sh
- _SYSTEM/validate_disk_state.sh
- 10_Knowledge/04_Phase_Agentic_Systems/Agent_Architect_Manual/STUDY_NOTES/L0_C03_Workbook.md
- ~/first_harness.sh

## Concepts That Forward-Reference Next Layer
- Orchestrators: Multi-agent coordination systems to be introduced after single-agent harnesses are mastered.
- Persistent Tool Hooks: Plans for harnesses to interact directly with SQLite for long-term memory.

## Cross-References
- Compute Liquidity implementation → _SYSTEM/FALLBACK_CHAIN.sh
- Environment validation → _SYSTEM/validate_disk_state.sh
- Token auditing source → 00_daily_logs/

## Study Notes Confirmed This Layer
- None

## Study Note Confirmed
- Topic: Domain-Driven Design (DDD)
- File: STUDY_NOTES/domain_driven_design.md
- Grill Me passed: yes
- Confirmed before: L1_C05_Domain_Driven_Design_For_Agents.md
