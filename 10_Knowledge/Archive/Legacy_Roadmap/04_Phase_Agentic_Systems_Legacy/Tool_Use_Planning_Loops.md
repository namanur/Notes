# Tool Use & Planning Loops: The Agent’s Heartbeat

**Phase:** Phase 4 — Agentic Systems (Day 24)
**Links:** [[ROADMAP]] | [[AI_Agent_Foundations_Mental_Models]] | [[MCP_Tools_Development]]

---

## 🧠 Mental Model: The ReAct Loop vs. Plan-and-Execute

Autonomy is not a single decision; it is a **Chain of Validations**.

- **The ReAct Loop:** `Thought -> Action -> Observation -> Thought...`
  - **Internal Logic:** The agent doesn't know what it's doing next until it sees the result of the current step. It is "locally optimal."
- **The Planning Loop (Outer Loop):** `Goal -> Plan -> Execute All -> Review`.
  - **Internal Logic:** The agent sets a high-level strategy (e.g., "Implement the Auth flow"). It breaks this into sub-tasks and passes them to the ReAct loop.
- **The "Broken" Loop:** When an agent gets stuck repeating the same failed command. This happens when the **Observation** doesn't provide enough "negative signal" to update the **Thought**.

---

## 🛠️ Technical Deep Dive: Tool Selection & Validation

### 1. Function Calling Internals
- **Mechanism:** The agent doesn't "click a button." It generates a JSON object.
- **Modern Pattern:** **Tool Choice Enforcement**. Forcing the agent to call a specific tool (e.g., `list_directory`) before it's allowed to guess a file path.
- **Command:** `DEBUG=tools node agent.js` (Monitor the raw JSON exchange).

### 2. The Planning State Machine
- **Pattern:** **Task Decomposition**.
  - *Bad:* "Build a website."
  - *Good:* "1. Create index.html, 2. Style with CSS, 3. Add JS."
- **Internal Mechanism:** **State Persistence**. If the agent crashes at Step 2, the "Environment" must hold the state so it can resume.

---

## 🧪 Mastery Drills: High Pain

1. **The Tool Failure Chain:** Disable a core tool (e.g., rename `ls` to `ls_broken`) and give the agent a task that requires it. Observe if its "Planning Loop" can derive an alternative (e.g., using `echo *` or `find .`) or if it collapses into a retry-loop.
2. **Ambiguous Goal Torture:** Give the agent a goal with 3 possible interpretations. Do not allow it to ask for clarification. Observe how it "bets" on one path and if it can "Re-plan" when the bet fails.
3. **JSON Validation Stress:** Feed the agent a tool that returns invalid JSON. Implement a "Validator" middleware that yells at the agent until it fixes the tool-calling syntax.

---

## 📜 Execution Contract

- **Timebox:** 3 Hours
- **Start Command:** `agent-runner --plan-only "Refactor the database layer"`
- **Completion Condition:** Successfully generate a 5-step plan where Step 4 depends on the specific output of Step 1.

---
*Last Updated: 21-04-2026*
