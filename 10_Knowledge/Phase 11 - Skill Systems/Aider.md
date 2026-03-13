# Aider (Custom Instructions & AGENTS.md)

Aider uses a declarative approach to extension through configuration files and dedicated documentation files.

## 1. Persistent Configuration
Aider's behavior is managed via **`.aider.conf.yml`**.

### Lookup Order
1. Current Directory
2. Git Root
3. Home Directory (`~`)

### Example `.aider.conf.yml`
```yaml
model: gpt-4o
read: [CONVENTIONS.md, AGENTS.md]
auto-commits: true
dark-mode: true
```

## 2. Project Conventions (AGENTS.md)
The emerging **`AGENTS.md`** standard is a "README for AI agents".

### What to Include
- **Build/Test Commands**: How the agent can verify its work.
- **Architectural Rules**: "Use functional patterns", "No global state".
- **Formatting**: "No semicolons", "Use 2 spaces".

## 3. In-Chat Logic
- `/read <file>`: Use for read-only documentation (prevents editing).
- `/add <file>`: Give Aider permission to modify the file.
- `/model <name>`: Switch the LLM for specialized tasks.

## Practical Tip
Create a **`CONVENTIONS.md`** file in your project root and add it to your `.aider.conf.yml` to ensure Aider always follows your specific coding style without being reminded.
