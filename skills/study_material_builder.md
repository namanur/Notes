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
[[Phase X]] | [Related Note]

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
## Vault Integration — Agent Architect Manual Extension

When generating study material for any topic that maps to the Agent Architect Manual
(agentic systems, MCP, orchestration, multi-agent, DDD, TDD for agents, cloud APIs,
sandboxing, swarms), apply these additional rules on top of the base template.

### Additional Section: [5] System Placement

Add this section after the Execution Contract in every relevant note:

```markdown
## 5. System Placement
- **Manual Layer:** [L0/L1/L2/L3/L4]
- **Chapter it feeds:** [e.g., L1_C06_MCP_Architecture_Proper.md]
- **GENERATED_CONTEXT impact:** [Which context file this knowledge strengthens]
- **SESSION_LOG dependency:** [Must this be understood before a specific session?]
- **Stack grounding:** [Which component of the stack does this directly apply to —
  Gemini CLI / MCP harness / FALLBACK_CHAIN.sh / SQLite state / Dell server / VivoBook]
```

### Additional Mastery Drill Type: Grill Me Drill

In the Mastery Drills section, add a third subsection for Manual-mapped topics:

```markdown
### Grill Me Drill
[One prompt to paste into _SYSTEM/GRILL_ME_TEMPLATE.md adversarial session.
Must test whether you actually understand the concept well enough to defend it,
not just recite it. Format: "Explain [X] without using [core term]. If you cannot,
you do not understand it."]
```

### Session Log Trigger Rule

If a topic's Completion Condition is met (Execution Contract ticked), the skill
must output this line at the bottom of the note:
This tells you the study note is complete enough to support the corresponding
Chapter Writer Agent spawn in the next Gemini CLI session.

### Research Filter Extension

REJECT additionally:
- Any resource that treats MCP as optional middleware
- Any multi-agent tutorial that uses local LLM inference
- Any orchestration guide that does not address session state or context window limits

PREFER additionally:
- modelcontextprotocol.io official spec and SDK source
- Gemini API quota and rate-limit documentation (not blog summaries)
- SQLite WAL mode documentation for concurrent agent state access