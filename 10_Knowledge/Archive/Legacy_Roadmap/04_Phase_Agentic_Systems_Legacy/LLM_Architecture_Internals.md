# Phase 4: LLM Architecture Internals
**Track:** Agent & MCP
**Parent:** [[ROADMAP]]

## 🧠 Mental Model: The Stochastic Mirror
An LLM is not a database. It is a **High-Dimensional Probability Map**. It does not "search" for facts; it calculates the most likely sequence of tokens based on the mathematical geometry of its training data.

1. **Tokens, not Words:** The model sees integers representing fragments of text. "Stochastic" might be one token; "learning" another. Meaning is derived from the **Vector Embedding** of these integers.
2. **Attention is Focus:** The "Transformer" architecture works by calculating **Self-Attention**. For every token, the model asks: "Which other tokens in this sequence are most relevant to my meaning right now?"
3. **KV Cache (The Memory Pipe):** In inference, the model stores the "Key" and "Value" vectors of previous tokens to avoid re-calculating them. This is why long context is expensive and slows down over time.

---

## 💻 Technical Deep Dive: Tokens and Inference

### 1. Tokenization (BPE - Byte Pair Encoding)
Modern models use BPE to handle rare words and emojis efficiently.
```python
# Conceptual view of tokenization
text = "Agentic Systems 🤖"
tokens = [2432, 876, 12, 54321] # Different for every model (Llama vs GPT-4)
```

### 2. Inference Parameters (The Knobs)
- **Temperature:** Scales the logits (raw probabilities). `0.0` = Deterministic (Greedy); `1.0` = Natural; `2.0` = Creative Chaos.
- **Top-P (Nucleus Sampling):** Only considers the top $P$ percentage of the probability mass. Filters out the "tail" of unlikely tokens.
- **Top-K:** Limits the vocabulary to the top $K$ most likely next tokens.

### 3. Quantization (The Shrinkage)
Running huge models on consumer hardware requires **Quantization** (e.g., 4-bit, 8-bit). This converts 32-bit floating point weights into lower precision, trading small accuracy drops for massive speed/VRAM gains.

---

## ⚡ Mastery Drills: High-Pain Execution
*Goal: Break the illusion of "intelligence."*

1. **The Temperature Stress Test:** Ask a model to solve a math problem with Temperature 0.0. Repeat with Temperature 1.8. Observe where the logic fractures.
2. **Token Math:** Take a complex sentence and manually predict how many tokens it will be. Check your work using a tokenizer (e.g., `tiktoken` for OpenAI or `llama.cpp` for local).
3. **Prompt Injection 101:** Try to get a model to ignore its system instructions using the "ignore all previous instructions" pattern. Analyze why it works (Attention priority).
4. **Local Inference:** Set up `ollama` and run a model. Use `curl` to send a raw JSON request to its API, manually setting `top_p` and `repeat_penalty`.

---

## 📜 Execution Contract
- **Timebox:** 2 Hours.
- **Start Command:** `ollama run llama3.1`
- **Completion Condition:** Successfully identify the "System Prompt" of a public LLM via adversarial probing, and then recreate a similar instruction set for a local model.

---
**Links:** [[ROADMAP]] | [[00_daily_logs/AGENT_ACTIVITY]]
