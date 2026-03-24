---
name: research-navigator
description: An autonomous research and curriculum navigation assistant. Use when the user wants to identify the next learning task in their curriculum, research it on the web, create structured Markdown notes, and update their progress tracking files.
---

# Research Navigator

This skill allows Gemini CLI to act as an active learning partner, moving autonomously through a structured curriculum.

## Workflow

### 1. Identify Target
- Read `10_Knowledge/20-Day Curriculum.md` to find the first checkbox that is NOT completed (`[ ]`).
- Read `99_System/Topics.md` to find the corresponding technical target.

### 2. Autonomous Research
- Use `google_web_search` and `web_fetch` to gather technical insights.
- **Priority Sources:** Official documentation (Anthropic for Claude, Linux documentation for kernel, Git docs), high-quality technical blogs (MDN, Stack Overflow, etc.).
- **Claude Certification Context:** Always check if the topic appears in the `10_Knowledge/Calude ecam prep.pdf` task statements. If it does, prioritize the exam's "Architectural Judgment" criteria.

### 3. Note Creation
- Write a Markdown file in the appropriate `10_Knowledge/Project - X` directory.
- **Format:**
    - # Topic Name
    - ## First Principles (How/Why)
    - ## Technical Breakdown (The Details)
    - ## Claude Architect Context (If applicable)
    - ## Practical Implementation (Examples/Commands)

### 4. Progress Update
- Use `replace` to mark the checkbox as `[x]` in:
    - `10_Knowledge/20-Day Curriculum.md`
    - `99_System/Topics.md`
- Ensure the Curriculum file links to the new note: `[[New Note Title]]`.

## Guardrails
- **No Hallucination:** If research is inconclusive, ask for clarification.
- **Concise Mastery:** Focus on high-signal explanations, not filler.
- **Safety:** Never execute commands that could compromise the vault without explaining first.
