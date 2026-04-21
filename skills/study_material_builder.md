# Study Material Builder Skill (The Thinking Enforcement System)
**Purpose:** Transform roadmap topics into high-signal, execution-focused study notes.
**When to use:** When the user requests notes or study material for any topic in the ROADMAP.

**Core Mandates:**
1. **Mental Model (Brutal):** Focus on how the system *actually* works to enable debugging. 
2. **Technical Deep Dive (No Noise):** Only commands you will actually use. Modern primitives only (e.g., `git switch` over `checkout`).
3. **Mastery Drills (High Pain):** Force mistakes and edge cases. If it's easy, it's useless.
4. **Execution Contract:** Every note MUST end with a Timebox, Start Command, and Completion Condition.
5. **Vault Integration (Deterministic):**
   - Correct Phase Header.
   - Link `ROADMAP.md` and related notes.
   - Update `99_System/Topics.md` (Mark as partial/complete).

**Research Filter:**
- REJECT: Outdated commands (`git checkout` for branching), "beginner" blogs with no internals.
- PREFER: Official docs, recent dev-focused deep dives, internal architecture diagrams.

**Note Template:**
```markdown
# [Topic Name]
[[Phase X]] | [Related Note] | [[ROADMAP]]

## 1. The Mental Model
[How it works under the hood. Why it fails.]

## 2. Technical Deep Dive
[Modern commands, critical differences, pro-tips.]

## 3. Mastery Drills
### Terminal Challenges
[Painful tasks.]
### Edge Cases
[Recovery scenarios.]

## 4. Execution Contract
- **Timebox:** [X minutes]
- **Start Command:** [One-liner to begin]
- **Completion Condition:** [Objective proof of mastery]
```
