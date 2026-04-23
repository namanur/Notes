# Agent Manifest

## Orchestrator Agent
- Role: Coordinate the build of the Agent Architect Manual.
- Tools: Gemini CLI, bash, filesystem.
- Workflow: validate -> read session log -> check study triggers -> spawn writer -> verify -> update log.

## Chapter Writer Agent
- Role: Write individual chapters based on mandates and quality floor.
- Context Injection: Selective based on current layer.

## Context Curator Agent
- Role: Summarize a completed layer into a distilled context file.

## Index Agent
- Role: Incrementally update Topic Map and Manual Index.
