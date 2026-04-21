# Universal Skill Authoring: Architecting for Portability

**Phase:** Phase 5 — Autonomous Workflows (Day 32)
**Links:** [[ROADMAP]] | [[Skill_Systems_Architecture]] | [[GitHub and good skills]]

---

## 🧠 Mental Model: The "Agent-Agnostic" Instruction

A skill should work whether the host is Gemini, Claude, or a custom Python script.

- **The Core Constraint:** You are writing for an **Intelligence**, not a **Program**.
- **Instructional Rigor:** If you tell an agent to "Fix the code," it will guess. If you write a Universal Skill, you specify the **Protocol**: "1. Search for X, 2. Validate Y, 3. Use tool Z to apply the fix."
- **The "Capability Handle" Abstraction:** Instead of hardcoding `npm test`, use `{{test_command}}`. This allows the host to provide the environment-specific implementation while the skill provides the logical flow.

---

## 🛠️ Technical Deep Dive: High-Signal Authoring Patterns

### 1. The "Pushy" Metadata Pattern
- **Pattern:** The `description` field in the skill's YAML is its **trigger condition**.
- **Bad Description:** "A skill for git."
- **Universal Description:** "ACTIVATE whenever the user wants to perform complex git operations involving rebase, cherry-pick, or history cleanup. Use this over standard git commands for safety."

### 2. Context Economy (The 80/20 Rule)
- **Pattern:** Keep the `SKILL.md` under 1,000 tokens. 
- **Mechanism:** Move 80% of the "data" (examples, docs, complex logic) into the `/references` or `/scripts` folder. The agent should only load these via `read_file` when the primary instructions trigger the need.

### 3. Error-Proofing with "Guardrail Thoughts"
- **Pattern:** Explicitly define "Fail States" in the skill.
- **Example:** "If tool `X` returns `Permission Denied`, do NOT attempt to sudo. Instead, stop and inform the user about the security boundary defined in [[System_Architecture_Scaling]]."

---

## 🧪 Mastery Drills: High Pain

1. **The Language Swap:** Author a skill in English and verify it works when the agent's system prompt is in a different language (e.g., Spanish or Python comments). If it fails, identify the semantic ambiguity.
2. **The Tool-less Logic:** Write a skill that guides an agent through a complex mental process (e.g., threat modeling) without providing any executable tools. Measure the agent's consistency across 5 separate runs.
3. **The Migration Test:** Take a skill written for `Aider` and port it to `Gemini CLI`. Identify the exact lines that were "Host-Specific" and refactor them into a "Universal Protocol."

---

## 📜 Execution Contract

- **Timebox:** 2 Hours
- **Start Command:** `init-skill --name universal-evaluator`
- **Completion Condition:** Successfully author a skill that can be loaded by two different agent environments and achieves the same outcome in both.

---
*Last Updated: 21-04-2026*
