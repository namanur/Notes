---
Phase: [[Phase 8]]
Project: [[Project - Agentic Systems]]
Prev: [[Phase 7]] | Next: [[Claude Code]]
---
# Skill Systems Overview (Phase 11)

This module focuses on **Programmable Cognition**—the ability to extend AI agents with specialized, reusable capabilities (Skills) and external tool access (MCP).

## The Core Agents
In this setup, we focus on primary terminal-based AI agents, each with unique extension patterns:

1.  **Claude Code (Anthropic)**: Uses `Skills` (procedural) and `MCP` (tool-based).
2.  **Gemini CLI (Google)**: Uses `Agent Skills` (procedural & script-based).
3.  **Codex CLI (OpenAI)**: Uses `Agent Skills` with Progressive Disclosure and `MCP`.
4.  **Aider (Open Source)**: Uses `Custom Instructions` and `AGENTS.md` (declarative).

## Why Skills Matter
Most AI agents have a limited "pre-trained" window of instructions. Skills allow you to:
- **Codify tribal knowledge**: Define how *your* team writes code or handles deployments.
- **Isolate complexity**: Keep the main agent prompt lean while activating heavy context only when needed.
- **Standardize tools**: Use Model Context Protocol (MCP) to provide a unified way for any agent to talk to any database or API.

## Documentation Links
- [MCP (Model Context Protocol) Official Docs](https://modelcontextprotocol.io)
- [Claude Code Skills Guide](https://claude.com/docs/skills)
- [Agent Skills Standard](https://agentskills.io)
- [Aider Configuration Guide](https://aider.chat/docs/config.html)
