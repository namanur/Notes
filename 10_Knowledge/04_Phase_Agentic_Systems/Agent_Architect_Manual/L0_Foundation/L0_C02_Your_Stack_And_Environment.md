# Chapter 02: Your Stack And Environment
> Layer: L0 | Prerequisite: L0_C01
> Context injected from: UBIQUITOUS_LANGUAGE only

## [1] Concept Explanation
The "Stack" is the physical and virtual machinery that gives an **Agent** its ability to exist and act. In this architecture, we separate **Reasoning** (Cloud APIs) from **Memory** and **State** (Local Hardware).

- **Gemini CLI (Primary Harness):** This is your main interface. It operates by sending your **Context Window** (the files you are working on) to Google's servers. Mechanically, it parses your local filesystem, packages it as an API request, and streams the **Output** back to your terminal. It is restricted by free-tier quotas (typically 15 requests per minute).
- **OpenRouter & FALLBACK_CHAIN.sh:** When the Primary Harness hits a rate limit (HTTP 429), the **Reasoning** engine must switch. `FALLBACK_CHAIN.sh` is a bash script that detects failure and re-routes the prompt to OpenRouter. It follows a hierarchy: DeepSeek R1 (for complex reasoning) → Qwen3 (for speed/formatting) → Llama 4 (for general tasks).
- **Goose vs. pi-mono:** This is a choice of **Harness** complexity. 
    - **Goose** is used when you need heavy **MCP** (Model Context Protocol) integration to connect to external data sources (like your ERPNext instance). 
    - **pi-mono** is used for minimalist, direct execution where you want the lowest latency and simple file manipulation.
- **The Hardware Split:**
    - **ASUS VivoBook (The Terminal):** Used for **Perception** and input. This is where you write code and prompts.
    - **Dell Ubuntu Server (The State Host):** A headless server that holds your **Memory** (SQLite databases) and runs **Harnesses**. It does *not* do LLM inference (no local GPUs). It only manages the environment and persistent data.

## [2] Why This Layer Exists
This layer exists to enforce **Compute Liquidity** and **Hardware Discipline**. By using cloud APIs for compute and local hardware for state, you ensure that:
1. You aren't limited by your laptop's RAM/GPU.
2. Your **Memory** remains private and local on the Dell server.
3. Your system is resilient; if one API provider goes down, the **Agent** continues to function via the fallback chain.

## [3] Stack Integration
The stack connects across layers through the **Harness**:
1. **Physical Layer:** VivoBook connects to Dell Server via SSH.
2. **Data Layer:** **Resources** are served from the Dell Server to the **Agent** via **MCP**.
3. **Reasoning Layer:** Gemini CLI or OpenRouter process the logic.
4. **Action Layer:** The resulting code or command is executed back on the Dell Server.

## [4] What To Read / Watch / Study
- **Source Code:** Read `_SYSTEM/FALLBACK_CHAIN.sh` to understand how it catches exit codes.
- **Documentation:** Google AI Studio (Gemini) Rate Limits documentation.
- **Manual:** Linux `ssh` and `systemd` basics (for keeping the Dell server processes alive).
- **Concept:** "The Twelve-Factor App" methodology, specifically Factor III (Config) and Factor VI (Stateless Processes).

## [5] Hands-On Execution
1. **Connectivity Check:** Open a terminal on your VivoBook and SSH into your Dell Server.
   ```bash
   ssh naman@192.168.31.250
   ```
2. **API Heartbeat:** Run a basic prompt through the primary harness.
   ```bash
   gemini-cli "What is the current system time?"
   ```
3. **Fallback Test:** Manually trigger the fallback script to ensure OpenRouter is configured.
   ```bash
   bash _SYSTEM/FALLBACK_CHAIN.sh "This is a test of the emergency fallback system."
   ```

Proof of completion: Output of `bash _SYSTEM/validate_disk_state.sh` showing all API keys are present in `.env`.

## [6] Validation Criteria
- [ ] SSH connection to the Dell server is established in under 2 seconds.
- [ ] `gemini-cli` returns a valid response without "API Key Not Found" errors.
- [ ] `_SYSTEM/FALLBACK_CHAIN.sh` successfully calls an OpenRouter model when given a test prompt.
- [ ] SQLite is accessible on the Dell server (`sqlite3 --version`).

## [7] Upgrade Trigger
N/A — Foundation layer.

## [8] Session Log Entry
> Confirm on disk then append to SESSION_LOG.md:
> L0_C02_Your_Stack_And_Environment.md | [x] | 2026-04-24 | Chapter Writer | 4350 bytes

## [9] Connections
- Previous: L0_C01_What_Is_An_Agent
- Next: L0_C03_Context_And_Memory_Basics
- Context file: GENERATED_CONTEXT/L0_Foundation_context.md
