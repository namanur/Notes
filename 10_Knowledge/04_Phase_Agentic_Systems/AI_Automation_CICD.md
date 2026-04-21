# Phase 4: Agentic Systems — Automation & CI/CD for AI (Day 30)

## 🧠 Mental Model: Testing Non-Determinism
Traditional CI/CD assumes `Input A -> Function -> Output B`. In AI Systems, `Input A -> Agent -> Output ~B`.
Automating AI systems requires a shift from **Exact Matching** to **Distributional Validation**.

### The Evaluator Loop
You don't test the agent; you test the *output* using a more capable model (LLM-as-a-Judge).
1.  **Run Agent:** Generate output on a test dataset (Gold Dataset).
2.  **Evaluate:** Pass output + ground truth to an Evaluator Model.
3.  **Score:** The Evaluator provides a pass/fail or a score based on a rubric (e.g., Accuracy, Safety, Format).

---

## 💻 Technical Deep Dive: Modern Patterns

### 1. Snapshot Testing for Agent Traces
Don't just test the final answer; test the **Reasoning Path**. 
Capture the list of tool calls made by the agent. If the tools called change, the snapshot fails, alerting you to a "reasoning regression."

### 2. CI/CD Pipeline (GitHub Actions Example)
```yaml
jobs:
  eval:
    runs-on: ubuntu-latest
    steps:
      - name: Run Evals
        run: |
          npm run eval -- --model gemini-2.0-flash
      - name: Check Pass Rate
        run: |
          python check_threshold.py --threshold 0.95
```

### 3. Red-Teaming Automation
Automate the discovery of failure modes by using a "Hacker Agent" to probe your system's prompts in CI.
- **Pattern:** `Attacker Agent` -> `Your System` -> `Safety Evaluator`.

---

## 🛠 Mastery Drills (High Pain)

### Drill 1: The Non-Deterministic Flaky Test
1.  Create a test case that passes 80% of the time.
2.  **Goal:** Implement a "Retry with Temperature 0" strategy in your test runner to stabilize the result.
3.  **Constraint:** You cannot change the prompt.

### Drill 2: The Evaluator Rubric
1.  Write a prompt that generates a summary of a technical document.
2.  Create an Evaluator prompt that checks for 3 specific facts.
3.  **Goal:** Deliberately feed it a summary that is "good" but misses one fact. The Evaluator MUST catch it.

---

## 📜 Execution Contract

- **Timebox:** 120 Minutes.
- **Start Command:** `pytest tests/evals/ --verbose`
- **Completion Condition:** A CI pipeline that runs an agent against 5 test cases, evaluates them using a second LLM, and fails the build if the aggregate score is below 90%.

---
**Links:**
- [[ROADMAP.md]]
- [[LLM_Architecture_Internals]]
- [[Reasoning_Chains_Patterns]]
