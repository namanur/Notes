# Chapter 07: TDD And Execution Loops
> Layer: L1 | Prerequisite: L1_C06_MCP_Architecture_Proper
> Context injected from: L0_Foundation_context.md

## [1] Concept Explanation
Test-Driven Development (TDD) for an **Agent** is not merely about verifying code logic; it is about constraining **Reasoning** to prevent drift. Because LLMs are inherently non-deterministic, the same input may yield different **Actions**. TDD for agents shifts the focus from "did the function return X?" to "did the agent reach the goal state Y via the defined protocol?".

The **Execution Loop** (Perception → Memory → Reasoning → Action → Output) is fragile. Without TDD, an agent might experience a **Mechanical Trap** where it hallucinates a successful **Action** without verifying the environment change. Agent-centric TDD follows a strict cycle:
1. **Red**: Define a failing state (e.g., a missing file or a failed SQLite check).
2. **Green**: The agent performs an **Action** to modify the environment.
3. **Refactor/Verify**: The agent (or a separate validator) runs the test script to confirm the environment matches the goal.

## [2] Why This Layer Exists
Layer 1 (Discipline) exists to impose engineering rigor on the fluid nature of agentic workflows. Without TDD, **Orchestrators** become impossible to debug because failures cascade silently. By enforcing TDD at the individual **Tool** level, we ensure that every **Action** taken by an agent is falsifiable. This layer prevents **Context Bloat** by replacing "hoping the agent understands" with "proving the agent executed."

## [3] Stack Integration
In our stack (Gemini CLI + Ubuntu Server), TDD is implemented via shell-based assertion scripts and **SQLite** state tracking.
- **Grill Me**: We use `_SYSTEM/GRILL_ME_TEMPLATE.md` to perform adversarial validation. After the agent claims completion, a separate "Adversarial Session" is launched to "Grill" the output for non-deterministic edge cases.
- **SQLite Persistence**: Unlike **In-context Memory**, SQLite is used to store the *results* of the loop, not the conversation. Store: Goal IDs, timestamps, and pass/fail status. **Do not store**: Large raw JSON logs or transient reasoning chains (keep those in markdown logs).

## [4] What To Read / Watch / Study
- *Test-Driven Development by Example* (Kent Beck) – For the core philosophy.
- *SQLite Schema Design for Agents* – Study how to model "state-at-time" rather than just "current state."
- *GRILL_ME_TEMPLATE.md* – Internalize the axes of attack (Semantic Accuracy, Executability).

## [5] Hands-On Execution
You will now guide an agent through a 3-test loop.

**Step 1: Create the Test Suite**
Create a file `L1_C07_tests.sh`:
```bash
#!/bin/bash
# Test 1: File Creation
[ -f "./target_file.txt" ] || exit 1
# Test 2: Content Accuracy
grep -q "AGENT_VERIFIED" ./target_file.txt || exit 1
# Test 3: SQLite Logging
sqlite3 state.db "SELECT count(*) FROM audit WHERE status='completed';" | grep -q "1" || exit 1
```

**Step 2: Execution**
Command your agent: *"Run L1_C07_tests.sh, observe the failures, and modify the environment until all tests pass. You must create the file, write the key phrase, and update the SQLite audit table in state.db."*

**Step 3: Grill Me**
Once passed, copy your agent's final report and paste it into a new session using the `_SYSTEM/GRILL_ME_TEMPLATE.md`.

**Proof of Completion**: `sqlite3 state.db "SELECT * FROM audit;"`

## [6] Validation Criteria
- [ ] `L1_C07_tests.sh` returns exit code 0.
- [ ] `state.db` contains a schema with an `audit` table.
- [ ] The `Grill Me` session resulted in a "PASS" verdict.
- [ ] No `In-context Memory` was used to "fake" the test results; the file exists on disk.

## [7] Upgrade Trigger
**Silent breakage on every L2 refactor.**
If you move to Layer 2 (Production) and modify your **Harness** or **Orchestrator** logic, and an L1 test fails without an explicit error message, you have triggered a "Silent Breakage." This requires immediate reversion to the L1 TDD loop to re-ground the agent.

## [8] Session Log Entry
`[DATE] | L1_C07 | TDD Implemented | 3/3 Tests Passing | Grill Me: PASS | Note: Agent struggled with SQLite write permissions on first attempt; resolved via chmod.`

## [9] Connections
- **Backward**: Uses the **JSON-RPC** protocol defined in `L1_C06` to execute the shell scripts.
- **Forward**: Prepares the state-tracking infrastructure required for **Autonomous Workflows** in Layer 2.
