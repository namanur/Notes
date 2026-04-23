# Phase 5: Context Providers Strategy
**Track:** Skills & Automation
**Parent:** [[ROADMAP]]

## 🧠 Mental Model: The Working Memory Limit
LLMs have a fixed context window. **Context Providers** are the strategy for deciding which bits of the infinite world get to sit in that precious window. It is the art of **Extreme Relevance**.

1. **The Retrieval Gap:** RAG (Retrieval-Augmented Generation) is not about "finding" data; it's about "bridging" the gap between a query and its answer.
2. **Context Density:** 1,000 irrelevant tokens are worse than 10 perfect tokens. Irrelevance introduces "noise" that degrades the model's attention mechanism.
3. **Dynamic Injection:** Context should be injected *just in time*.

---

## 💻 Technical Deep Dive: RAG and Chunking

### 1. The RAG Pipeline
- **Embedding:** Converting text into a vector (a list of numbers) that represents its semantic meaning.
- **Vector Search:** Finding the "closest" vectors in the database (Cosine Similarity).
- **Reranking:** Using a smaller, faster model to verify the top results of the vector search.

### 2. Chunking Strategies
- **Fixed Size:** Split by characters/tokens. (Fast, but breaks context).
- **Semantic:** Split where the "meaning" changes (e.g., between paragraphs).
- **Overlapping:** Ensure the end of Chunk A is the start of Chunk B to preserve continuity.

### 3. Context Windows & "Lost in the Middle"
Models are best at attending to information at the very beginning and the very end of a prompt. Important context must be placed strategically.

---

## ⚡ Mastery Drills: High-Pain Execution
*Goal: Experience retrieval failure and noise saturation.*

1. **The Needle in a Haystack:** Give a model a 50,000-word text and hide one random fact in the middle. Ask for it. Witness the attention failure.
2. **The Embedding Clash:** Find two sentences with similar words but opposite meanings (e.g., "The bank is where I keep money" vs "The river bank is muddy"). See if your vector search can distinguish them.
3. **The Junk Food Prompt:** Stuff a prompt with 80% irrelevant data and 20% relevant data. Measure the accuracy of the output compared to a "lean" version of the same prompt.
4. **Manual Chunking:** Take a technical doc and manually split it into 500-token chunks with 50-token overlap. Explain why each split point was chosen.

---

## 📜 Execution Contract
- **Timebox:** 2 Hours.
- **Start Command:** `python3 -m pip install sentence-transformers chromadb`
- **Completion Condition:** Build a local RAG script that indexes your `00_daily_logs` directory and allows you to query "What did I do on X date?" with 90% accuracy.

---
**Links:** [[ROADMAP]] | [[00_daily_logs/AGENT_ACTIVITY]]
