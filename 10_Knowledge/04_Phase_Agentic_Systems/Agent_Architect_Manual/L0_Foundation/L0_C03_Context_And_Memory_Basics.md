# Chapter 03: Context And Memory Basics
> Layer: L0 | Prerequisite: L0_C02
> Context injected from: UBIQUITOUS_LANGUAGE only

## [1] Concept Explanation
Mechanically, **Memory** in an **Agent** is divided into two distinct physical domains: the **Context Window** (In-context memory) and **Persistent Storage** (External memory, specifically **SQLite**).

The **Context Window** is the transient "workbench" of the LLM. It is measured in **Tokens**—mathematical chunks of text (roughly 4 characters or 0.75 words). Every time you send a prompt, the entire history of that conversation, plus any **Resources** attached via **MCP**, must fit within this window. 
- **The Mechanical Trap:** LLMs do not "remember" between calls. If you send a message, then another, the **Harness** (Gemini CLI) must re-send the first message + the second message to the API. 
- **Context Bloat:** As the conversation grows, you are re-sending thousands of tokens you have already paid for. On free-tier APIs, this leads to hitting Rate Limits (TPM/RPM) faster and causes "Needle in a Haystack" issues where the agent loses focus on the goal.

**SQLite (Persistent Memory)** is the "filing cabinet" on your Dell Server. Unlike the Context Window, which clears when the process ends, SQLite stores data in a structured table format. 
- **The Distinction:** You use the Context Window for **Reasoning** (the active logic of the task) and SQLite for **Knowledge** (historical facts, GSTIN numbers, accounting logs). 
- **The Workflow:** The agent uses a **Tool** to "query" SQLite, brings only the *relevant* row into the Context Window, processes it, and then discards it. This keeps the window lean and the free-tier usage sustainable.

## [2] Why This Layer Exists
This layer exists to prevent "Memory Exhaustion." Beginners often try to feed an entire 500-page accounting ledger into a single prompt. This is technically possible with Gemini's 2M context window but economically disastrous for a self-taught architect on a budget. Mastering the mechanical split between "What I am thinking about now" (Context) and "What I know" (SQLite) is the difference between a toy and a production-grade **Agentic System**.

## [3] Stack Integration
- **Gemini CLI:** Manages the active **Context Window**. It tracks your current session history and sends it to the Cloud API.
- **Ubuntu Server (Dell):** Acts as the host for the **SQLite** database files. The server does not run the LLM (no inference); it only manages the state.
- **MCP (Model Context Protocol):** The bridge. An MCP server on your Dell machine allows the Gemini CLI to "reach out" and pull specific data from SQLite into the context window only when needed.

## [4] What To Read / Watch / Study
- **Google AI Studio Documentation:** Search for "Gemini Tokenization" to understand how your text is sliced.
- **SQLite Official "Introduction to SQL":** Focus on `SELECT`, `INSERT`, and `WHERE` clauses. You don't need to be a DBA, just a data retriever.
- **Anthropic/Google Blogs:** Look for "Context Window Management" or "RAG (Retrieval-Augmented Generation) vs. Long Context."

## [5] Hands-On Execution
Since this is a mental model chapter, your execution is architectural design:
1. **Token Audit:** Take a previous conversation log from `00_daily_logs/`. Copy it into a free online "Tokenizer" (e.g., OpenAI Tokenizer or Google's equivalent). Note the difference between word count and token count.
2. **Memory Schema Design:** Open a new file `10_Knowledge/04_Phase_Agentic_Systems/Agent_Architect_Manual/STUDY_NOTES/L0_C03_Workbook.md`.
3. **Task:** Design a 3-column SQLite table for a "GST Filing Agent." 
    - Column 1: Client_Name
    - Column 2: GSTIN
    - Column 3: Last_Filing_Date
4. **Analysis:** Write 2 sentences explaining why the GSTIN should stay in SQLite and only enter the Context Window when a filing is actually being performed.

Proof of completion: `10_Knowledge/04_Phase_Agentic_Systems/Agent_Architect_Manual/STUDY_NOTES/L0_C03_Workbook.md`

## [6] Validation Criteria
- [ ] You can explain why sending a 10MB PDF in every prompt is a bad idea for a free-tier user.
- [ ] You can define a **Token** without using the word "word."
- [ ] You can identify the specific physical location of your **Persistent Memory** (The Dell Server).
- [ ] You can explain the "Mechanical Trap" (LLMs have no native memory between API calls).

## [7] Upgrade Trigger
N/A — Foundation layer.

## [8] Session Log Entry
> Confirm on disk then append to SESSION_LOG.md:
> L0_C03_Context_And_Memory_Basics.md | [x] | 2026-04-24 | Chapter Writer | 4250 bytes

## [9] Connections
- Previous: L0_C02_Your_Stack_And_Environment
- Next: L0_C04_Your_First_Harness
- Context file: GENERATED_CONTEXT/L0_Foundation_context.md
