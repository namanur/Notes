---
name: research-learning-agent
description: Automates research and progress tracking for the 20-Day Curriculum and Claude Certification. Use when the user wants to research the next topic in their index, create structured notes, and update their learning roadmap.
---

# Research Learning Agent

This skill transforms Gemini CLI into an active research and curriculum management assistant.

## Workflow

### 1. Identify the Next Task
- Read `10_Knowledge/20-Day Curriculum.md` to find the first checkbox that is NOT completed (`[ ]`).
- Read `99_System/Topics.md` to cross-reference the specific technical targets.

### 2. Research Phase
- Use `google_web_search` and `web_fetch` to find deep technical information on the target topic.
- Focus on "First Principles": How it works, why it exists, and common pitfalls.
- If the topic is part of the **Claude Certified Architect** exam, specifically look for Anthropic's official documentation or architecture patterns (Agent SDK, MCP, etc.).

### 3. Note Creation
- Create a new Markdown file in the appropriate `10_Knowledge/Project - X` directory.
- Use a structured format:
    - **Concept:** Clear explanation of the "Why".
    - **Technical Details:** In-depth "How".
    - **Claude Exam Context:** (If applicable) How this relates to agentic orchestration or reliability.
    - **Practical Examples:** Real-world usage or terminal commands.

### 4. Progress Tracking
- Use `replace` to mark the task as completed (`[x]`) in:
    - `10_Knowledge/20-Day Curriculum.md`
    - `99_System/Topics.md`
- Link the new note in the Curriculum file.

## Principles
- **Concise & High-Signal:** Don't just dump text; synthesize the best insights.
- **Auto-Navigate:** Don't ask what's next unless the index is ambiguous.
- **First Principles:** Always explain the underlying mechanism (e.g., inodes before `ls`).
