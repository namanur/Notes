# Skill Systems: Modular Capability Injection

**Phase:** Phase 5 — Autonomous Workflows (Day 31)
**Links:** [[ROADMAP]] | [[AI_Agent_Foundations_Mental_Models]] | [[Tool_Use_Planning_Loops]]

---

## 🧠 Mental Model: Skill Injection & Hot-Loading

Don't build a "Do Everything" agent. Build a "Modular Host."

- **The Host:** Provides the runtime, the file system access, and the context window.
- **The Skill:** A discrete package of instructions (`SKILL.md`), scripts, and reference data.
- **Skill Injection Mechanism:** 
  - **Static Injection:** Loading a skill into the System Prompt at boot. (Slow, expensive).
  - **Dynamic Injection (Hot-Loading):** The agent "hears" a trigger word, searches its `/skills` directory, and reads the specific `SKILL.md` into its current memory.
  - **The "Capability Gap":** When an agent knows *what* to do but lacks the *tool* to do it. Skills bridge this gap by providing both the **Knowledge** (Instruction) and the **Handle** (Tool).

---

## 🛠️ Technical Deep Dive: Skill Anatomy

### 1. The Skill Manifest (`SKILL.md`)
- **Frontmatter:** Contains YAML metadata.
  - `trigger`: Semantic patterns that cause the host to load this skill.
  - `priority`: Which skill to use when two overlap.
- **The Activation Protocol:** 
  - The host reads the `description` of all skills.
  - If a match is found, it injects the *entire* `SKILL.md` into the context.

### 2. Skill-Script Coupling
- **Pattern:** Every skill should have a `/scripts` directory. 
- **Modern Pattern:** **Deterministic Execution**. The LLM should only decide *when* to run a script and with *which arguments*. The script handles the "heavy lifting" (API calls, complex regex).

---

## 🧪 Mastery Drills: High Pain

1. **The Conflict Resolution:** Create two skills with overlapping triggers (e.g., `git-helper` and `github-automator`). Give a command that fits both. Implement a "Skill Supervisor" thought process that force-picks the correct one.
2. **The Zero-Instruction Boot:** Start an agent with a blank system prompt. Provide it with a `/skills` directory. Force it to "discover" and load a skill to solve a problem without you telling it where to look.
3. **The Script Bypass:** Write a skill that *requires* a script to be safe. Deliberately try to trick the agent into doing the task manually (and dangerously) instead of using the script. Fix the `SKILL.md` to prevent this bypass.

---

## 📜 Execution Contract

- **Timebox:** 2 Hours
- **Start Command:** `gemini-cli skill list --verbose`
- **Completion Condition:** Successfully "discover" a capability gap in the agent and bridge it by creating a new 3-file skill (SKILL.md, script, reference).

---
*Last Updated: 21-04-2026*
