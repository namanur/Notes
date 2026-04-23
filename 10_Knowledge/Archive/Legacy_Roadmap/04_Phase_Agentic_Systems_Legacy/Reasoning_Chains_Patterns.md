# Phase 5: Reasoning Chains Patterns
**Track:** Skills & Automation
**Parent:** [[ROADMAP]]

## 🧠 Mental Model: Thinking is Computation
Standard LLM responses are "Fast" (System 1). **Reasoning Chains** force the model into "Slow" (System 2) thinking. By generating a sequence of intermediate "thought" tokens, the model allocates more computation to the logical path before arriving at the final answer.

1. **Tokens as Logic:** Every token in a reasoning chain is a computational step. If the chain is too short, the logic is shallow.
2. **Path Selection:** Tree of Thoughts (ToT) allows the model to explore multiple branches and "backtrack" if a path leads to a contradiction.
3. **The Self-Correction Loop:** Reasoning isn't just forward; it's recursive. A strong chain includes a "Verify" step.

---

## 💻 Technical Deep Dive: CoT and ToT Patterns

### 1. Chain of Thought (CoT)
Simple but powerful. Force the model to "explain your reasoning step-by-step."
```text
Question: [Complex Task]
Thought: First, I need to evaluate X...
Thought: Given X, I then calculate Y...
Answer: [Final Output]
```

### 2. Reflection Pattern
Force the model to critique its own first draft.
1. **Draft:** Generate the code.
2. **Reflect:** Find 3 potential bugs or optimizations.
3. **Refine:** Output the final version incorporating the reflections.

### 3. Systematic Verification
Using "Checklists" within the reasoning block.
- "Have I checked for null values?" [YES/NO]
- "Is the variable naming idiomatic?" [YES/NO]

---

## ⚡ Mastery Drills: High-Pain Execution
*Goal: Force logical fallacies and recovery.*

1. **The Logic Trap:** Give the model a puzzle that has a common "intuitive" but wrong answer (e.g., the bat and ball problem). See if a standard prompt fails and if a CoT prompt succeeds.
2. **The Contradiction Force:** Tell the model its previous answer was wrong (even if it was right). Observe how it handles the "Reasoning Chain" to either defend itself or hallucinate a fix.
3. **Tree of Choices:** Give the model a task with 5 variables. Force it to write a reasoning chain that explores at least 3 combinations of those variables before deciding.
4. **Draft vs. Reflect:** Record the diff between an agent's "First Draft" and its "Refined Version" after a mandatory Reflection step. Quantify the improvement.

---

## 📜 Execution Contract
- **Timebox:** 1.5 Hours.
- **Start Command:** Create a `.md` system prompt that mandates a `<thought>` block before any `<answer>` block.
- **Completion Condition:** Successfully use your Reflection prompt to refactor a complex function from your own codebase, identifying at least one real edge case the model originally missed.

---
**Links:** [[ROADMAP]] | [[00_daily_logs/AGENT_ACTIVITY]]
