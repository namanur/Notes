# Chapter 11: Multi-Agent Swarms
> Layer: L3 | Prerequisite: L2_C10_Deep_Modules_And_Thick_Boundaries
> Context injected from: L2_Production_context.md

## [1] Concept Explanation
A **Swarm** is a decentralized architectural pattern where a single **Orchestrator** coordinates multiple **Specialists** through a shared **Blackboard**. Unlike a monolithic agent that attempts to hold an entire project state in its **Context Window**, a Swarm enforces **Role Isolation**. 

Each Specialist is an **Agent** with a dedicated **Harness** tuned for a narrow domain (e.g., File I/O, API Research, or Code Refactoring). They do not communicate directly; instead, they perform **Actions** that update a shared **Memory** layer (SQLite). This prevents "window bloat" because specialists only ingest the specific **Resources** or state fragments required for their immediate **Reasoning** loop.

## [2] Why This Layer Exists
L2 Production established the reliability of a single agent through **Deep Modules** and **Thick Boundaries**. However, as project complexity scales, a single agent's **Perception** becomes muddied by irrelevant data, leading to reasoning failures and token exhaustion. Layer 3 (Scale) introduces Swarms to:
1.  **Decompose Reasoning:** Complex goals are broken into sub-tasks assigned to specialist LLM profiles.
2.  **State Persistence:** Using a database as a coordination layer allows the swarm to "hibernate" and resume without losing the thread of the operation.
3.  **Parallel Execution:** Multiple agents can perform **Actions** simultaneously if the domain boundaries are properly defined.

## [3] Stack Integration
The hardware environment is split to optimize for low latency and state integrity:
-   **ASUS VivoBook (Orchestration Logic):** Runs the primary Python/Bash loop that instantiates agent harnesses and manages the "Thinking Loop."
-   **Dell Ubuntu Server (State Host):** Hosts the **SQLite** database and **MCP** servers. All specialists write their **Output** and state updates to this central authority.
-   **Communication:** JSON Schema via standard pipes/HTTP defines the **Thick Boundaries** between the VivoBook (Logic) and Dell Server (State).

## [4] What To Read / Watch / Study
-   *The Blackboard Pattern in Distributed Systems*: Understanding shared-state coordination.
-   *Multi-Agent Systems (MAS) Fundamentals*: Studying emergent behavior and role assignment.
-   *SQLite JSON1 Extension*: Learning how to store and query agent state-fragments efficiently.

## [5] Hands-On Execution
**Exercise: The "Audit & Documentation" Swarm**
Create a two-agent system to solve a documentation gap in a Python project.

1.  **Agent A (The Auditor):**
    -   **Harness:** Configured for `Perception` of file structures.
    -   **Action:** Scans a directory for functions lacking docstrings.
    -   **Memory:** Writes the list of missing docstrings to `state.db` on the **Dell Server**.
2.  **Agent B (The Writer):**
    -   **Harness:** Configured for `Action` (Writing code).
    -   **Perception:** Reads the `state.db` entries created by the Auditor.
    -   **Reasoning:** Generates appropriate docstrings based on function signatures.
3.  **Orchestrator (VivoBook):**
    -   Triggers Agent A, waits for `state.db` update, then triggers Agent B.

**Proof of Completion:**
Execute `sqlite3 state.db "SELECT * FROM tasks;"` and confirm records showing `auditor_id` completion followed by `writer_id` fulfillment for the same code block.

## [6] Validation Criteria
-   **Isolation:** The Writer Agent must have zero knowledge of the file system structure until it reads the specific task from the Blackboard.
-   **Integrity:** The **Orchestrator** must verify that Agent A's output matches the schema required by Agent B before triggering the next phase.
-   **TDD:** Write a test case that mocks a failed Auditor report to ensure the Orchestrator does not trigger the Writer with invalid state.

## [7] Upgrade Trigger
**The Collision Limit:** When the Swarm scales to >3 agents, you will notice agents attempting to update the same record or overwriting shared state without locking mechanisms. This is the trigger for **L4 Leverage**, where you move from basic Swarms to **Autonomous Swarms** with ACID-compliant transaction logic and advanced conflict resolution.

## [8] Session Log Entry
```markdown
## [L3_C11] - Swarm Architecture Initialized
- **Concept:** Specialist isolation via SQLite Blackboard.
- **State Host:** Dell Ubuntu Server (192.168.31.250).
- **Orchestration:** ASUS VivoBook Python Harness.
- **Status:** Verified two-agent handoff via state.db.
```

## [9] Connections
-   **Backwards:** Uses the **Deep Modules** from L2_C10 to define specialist roles.
-   **Forwards:** Prepares for **L4_C14_Autonomous_Agent_Maintenance**, where the swarm begins to monitor and fix its own **Harness** configurations.
