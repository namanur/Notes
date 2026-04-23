# Domain-Driven Design (DDD)
[[L1]] | [[L1_C05_Domain_Driven_Design_For_Agents]] | [[ROADMAP]]

## 1. The Mental Model
Domain-Driven Design (DDD) is not a coding style; it is a **reconciliation protocol**. 

Think of it like **GST Classification Logic**. In a ledger, if you record a transaction as "Expense" but the auditor expects "Input Tax Credit (ITC) on Capital Goods," the audit fails despite the math being correct. The failure isn't in the calculation; it's in the **taxonomy**. 

Under the hood, DDD forces the "Business Logic" and the "Execution Code" into a single, shared dictionary. Without it, agents suffer from **Semantic Drift**: the user says "Archive this," but the agent's code defines "Archive" as `rm -rf`. 

**Why it fails:** 
- **Language Dilution:** Using generic terms like `data`, `process`, or `handler` instead of domain terms like `LedgerEntry` or `Harness`.
- **Boundary Violation:** Allowing an agent designed for "Taxes" to start making "Payroll" decisions because the definitions overlap.

## 2. Technical Deep Dive
In this stack, we implement DDD through a **Grounding Source**: the `UBIQUITOUS_LANGUAGE.md` file. This file acts as the "source of truth" that Gemini CLI must ingest before any reasoning turn.

### Implementation Pattern
1. **Define the Bound:** Create `UBIQUITOUS_LANGUAGE.md` at the root of the manual layer.
2. **Inject Context:** Pass this file to the agent's context window to prevent hallucinated terminology.

### Command-Line Grounding
Verify the integrity of your domain language using standard shell tools:

```bash
# Check if current scripts/notes use non-standard terminology
grep -vE "(Agent|Harness|Perception|Memory|Reasoning|Action)" 10_Knowledge/04_Phase_Agentic_Systems/Agent_Architect_Manual/_SYSTEM/AGENT_MANIFEST.md

# Verify the language source exists before starting an execution turn
ls 10_Knowledge/04_Phase_Agentic_Systems/Agent_Architect_Manual/UBIQUITOUS_LANGUAGE.md
```

## 3. Mastery Drills
### Terminal Challenges
1. **Language Audit:** Run `grep` on your latest `SESSION_LOG.md` and identify three terms you used that are *not* in `UBIQUITOUS_LANGUAGE.md`. Map them to existing terms or update the dictionary.
2. **Boundary Check:** Use `ls -R` to map your current `L1` directory. Identify one file that "leaks" into `L2` (Scale) logic.

### Edge Cases
- **The "Tool" vs "Action" Trap:** In our language, an *Action* is the execution of a *Tool*. If you ask for an "Action" but haven't defined the "Tool," the agent will stall.
- **Scope Creep:** If `UBIQUITOUS_LANGUAGE.md` grows beyond 2 pages, your domain is too large. Split the agent.

### Grill Me Drill
*Adversarial Prompt:* "Explain DDD to an accountant without using the words 'domain', 'software', or 'modeling'."
> *Response:* "Imagine two banks trying to settle a payment. If Bank A calls a transaction a 'Reversal' and Bank B calls it a 'Refund', their ledgers will never balance. To work together, they must first sign a contract agreeing on exactly what every column header in their spreadsheet means. DDD is that contract. It ensures that when you say 'Audit', every person and calculator in the room knows exactly which tax slab and which fiscal year you are talking about."

## 4. Execution Contract
- **Timebox:** 30 minutes
- **Start Command:** ls 10_Knowledge/04_Phase_Agentic_Systems/Agent_Architect_Manual/UBIQUITOUS_LANGUAGE.md
- **Completion Condition:** Study note created and user understands why agents need a shared language.

## 5. System Placement
- **Manual Layer:** L1
- **Chapter it feeds:** L1_C05_Domain_Driven_Design_For_Agents.md
- **GENERATED_CONTEXT impact:** Strengthens L1 context.
- **Stack grounding:** Gemini CLI / Filesystem.
