# Multi-Agent Swarms
L3 | [[L3_C11_Multi_Agent_Swarms]]

## 1. The Mental Model
Multi-agent swarms represent the shift from a **"Solo Genius"** to a **"Disciplined Crew."** Instead of one complex agent trying to master every tool, we isolate roles into specific, specialized workers.

Think of a **GST Filing Department**. You don't have one person doing everything; you have:
1. **The Data Entry Clerk**: Efficiently gathers invoices and enters raw numbers.
2. **The Auditor**: Checks entries against tax laws and identifies discrepancies.
3. **The Submitter**: Finalizes the filing and handles the receipt from the portal.

In a swarm, **Role Isolation** ensures that if the Data Entry Clerk fails, the Auditor doesn't get corrupted. They operate with a **Shared Consciousness**—not through a telepathic broadcast, but through a central repository of work. Simple delegation (passing a specific baton) is always superior to complex broadcasting (shouting in a room and hoping someone listens), as it maintains clear accountability and reduces noise.

## 2. Technical Deep Dive
In our L3 architecture, we move away from passing messages in memory and transition to the **Blackboard Pattern**. 

### SQLite as the Blackboard
The **Dell Server** acts as the coordination layer, hosting a shared state database. **SQLite** serves as our 'Blackboard'—a persistent, structured space where agents read their assignments and write their results.

- **Centralized Queue**: Instead of Agent A calling Agent B, Agent A writes a task to the `blackboard` table with `status = 'pending'`.
- **Worker Polling**: Agent B (the specialist) monitors the table for tasks matching its `agent_role`.
- **State Persistence**: Even if an agent process crashes, the work state remains safe on disk, allowing for seamless recovery.

## 3. Mastery Drills
### Terminal Challenges
1. **Process Orchestration**: Launch three separate terminal sessions, each running an agent process (e.g., using `nohup` or `screen`). Use `fuser shared_state.db` to identify which process currently holds the file lock.
2. **Concurrency Test**: Attempt to have two agents update the same status row simultaneously using a script. Observe how SQLite handles the `SQLITE_BUSY` error.

### Edge Cases
- **Race Conditions**: Two agents reading the same "Pending" task at the exact same microsecond. We solve this using SQLite's `BEGIN IMMEDIATE` transactions to ensure only one agent "claims" the row by updating the `status` to `in_progress`.
- **Deadlocks**: A worker waiting for a task that an upstream agent hasn't written because it's waiting for a response from the worker.

### Grill Me Drill
*Adversarial Prompt*: "Explain a swarm of 3 agents to a business manager without using the words 'AI', 'computer', or 'automation'."
> *Response*: "Imagine a team of three specialized professionals working on a single project. One is a researcher who gathers facts and places them in a shared filing cabinet. The second is an editor who takes those facts from the cabinet, organizes them into a report, and puts the draft back in. The third is a manager who picks up the draft, signs off on it, and sends it to the client. They don't need to talk to each other directly; they only need to look at the filing cabinet to know what to do next. This ensures the project keeps moving even if one person is out of the office, as the cabinet always shows exactly where the work stands."

## 4. Execution Contract
- **Timebox:** 45 minutes
- **Start Command:** `sqlite3 shared_state.db "CREATE TABLE blackboard (id INTEGER PRIMARY KEY, agent_role TEXT, task TEXT, status TEXT);"`
- **Completion Condition:** Run the sqlite3 start command, insert one row per agent role (Data Entry, Auditor, Submitter), update one row's status from `pending` to `in_progress` using `BEGIN IMMEDIATE`, and confirm with `SELECT * FROM blackboard;` showing correct state.

## 5. System Placement
- **Manual Layer:** L3
- **Chapter it feeds:** L3_C11_Multi_Agent_Swarms.md
- **GENERATED_CONTEXT impact:** Foundation for L3 Scaling.
- **Stack grounding:** ASUS VivoBook (Orchestration Logic) / Dell Server (State Host) / SQLite.
