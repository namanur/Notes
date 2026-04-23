# AI Agent Foundations: Mental Models of Autonomy

**Phase:** Phase 4 — Agentic Systems (Day 23)
**Links:** [[ROADMAP]] | [[00_Overview]] | [[AI_Agent_Blueprint_Startup_Guide.png]]

---

## 🧠 Mental Model: Reactivity vs. Deliberation

Most people think agents are "smarter chatbots." They are actually **state machines** with probabilistic transition functions.

- **The Reactive Loop (System 1):** Immediate response to stimuli. The agent sees an error and tries to fix it instantly. High speed, low coherence.
- **The Deliberative Loop (System 2):** Explicit planning. The agent pauses to generate a graph of sub-tasks. High coherence, higher cost.
- **Reactivity in Agent Planning:** A "truly" autonomous agent doesn't just follow a plan; it treats the **Plan as a Live Document**. If the environment changes (e.g., a tool returns an unexpected error), the agent must perform a **Re-planning Interrupt**.

**The Autonomy Pillar:**
1.  **Identity:** Role definition (System Prompt).
2.  **Cognition:** The LLM's reasoning capability (ReAct/CoT).
3.  **Memory:** The scratchpad of previous thoughts and tool outputs.
4.  **Agency:** The ability to influence the world via tools.

---

## 🛠️ Technical Deep Dive: The Agent Lifecycle

### 1. The Reasoning Cycle (Thought -> Action -> Observation)
- **Pattern:** Use the **ReAct** (Reason + Act) pattern.
- **Modern Pattern:** **Reflexion**. The agent critiques its own previous `Thought` before issuing an `Action`. 
- **Internal Mechanism:** Logit bias and temperature control. In autonomous loops, keep `temperature` low (0.0-0.2) to prevent "hallucination drift" during long execution chains.

### 2. Context Window Management
- **The "Compressed History" Pattern:** Don't feed the agent the entire log. Feed it a **Summary of Findings** + **Current Sub-task** + **Available Tools**.
- **Observation Filtering:** If a tool returns 10,000 lines of logs, the "Agency Layer" must truncate or summarize them *before* the agent sees them, or it will drown in noise.

---

## 🧪 Mastery Drills: High Pain

1. **The Infinite Loop Test:** Create an agent with two contradictory instructions (e.g., "File must exist" and "Delete the file"). Observe how it handles the "Re-planning Interrupt." Force it to break the cycle.
2. **Temperature Drift:** Run a 10-step autonomous loop at `temperature=1.0`. Identify the exact step where the "Mental Model" of the task collapsed into gibberish.
3. **Observation Overload:** Feed a tool output that is 2x the agent's context window. Implement a middle-ware logic that extracts only the `ERROR` lines and measure the agent's success rate compared to a "dumb" truncate.

---

## 📜 Execution Contract

- **Timebox:** 2 Hours
- **Start Command:** `mcp-bridge --debug --trace-agent`
- **Completion Condition:** Trace one complete reasoning cycle where the agent *changes* its plan based on a tool failure.

---
*Last Updated: 21-04-2026*
