# Chapter 01: What Is An Agent
> Layer: L0 | Prerequisite: None
> Context injected from: UBIQUITOUS_LANGUAGE only

## [1] Concept Explanation
An **Agent** is not a chatbot; it is a state machine that operates in a continuous loop: **Perception** → **Memory** → **Reasoning** → **Action** → **Output**. 

Mechanically, this works through a feedback loop. Perception parses a system state (e.g., the output of `ls -R`). Memory stores this state (In-context for immediate use, SQLite for long-term persistence). Reasoning (the LLM) evaluates the memory against a goal and determines the next logical step. Action executes a **Tool** (e.g., `write_file`). If the tool's output is not piped back into Perception, the loop breaks, and the agent "hallucinates" because its Reasoning is decoupled from the environment's reality. Agents fail when they lose "grounding"—the direct link between Action results and the next Perception cycle.

## [2] Why This Layer Exists
If you skip the L0 definition and treat an agent as a "smart text box," you will fail to build reliable systems. You will over-rely on "vibes" rather than technical constraints. Understanding that an agent is a contractor requiring a specific **Harness** ensures you build infrastructure that provides enough context for the agent to succeed without crashing your host system.

## [3] Stack Integration
In this architecture, the **ASUS VivoBook** acts as the command center, while the **Dell Ubuntu Server** holds the state. 
- **Compute**: Handled via cloud APIs (Gemini 1.5 Pro/Flash). No local inference is attempted due to 4GB RAM limits and ERPNext stability requirements.
- **Primary Driver**: **Gemini CLI**.
- **State**: Persistent **Memory** is stored in **SQLite** on the Dell server.
- **Resilience**: If Gemini CLI hits rate limits, the system triggers `_SYSTEM/FALLBACK_CHAIN.sh` to route requests through OpenRouter (DeepSeek R1 or Qwen).
- **Communication**: The **Harness** bridges the cloud reasoning with the local bash environment via **MCP**.

## [4] What To Read / Watch / Study
- **GitHub**: Search `model-context-protocol/servers` → View `src/index.ts` in any server → Identify how "Tools" are defined as JSON schemas for the agent to perceive.
- **YouTube**: Search `LLM agents ReAct pattern mechanical explanation` → Focus on how the "Observation" (Perception) step is fed back into the prompt.
- **Google**: Search `site:anthropics.com "Computer Use" technical documentation` → Read the section on "Action Space" to understand how agents translate reasoning into mouse/keyboard/CLI events.
- **Docs**: Gemini API Documentation → "Function Calling" section → Study how the model returns a "call" instead of "text."

## [5] Hands-On Execution
Establish a "Perception-Check" using Gemini CLI to confirm the agent can see the Dell server environment. Run the following command from your VivoBook targeting the Dell server:
`gemini-cli run "List the contents of /home/naman/Documents/Notes/99_System and tell me if audit_todos.py exists."`

Proof of completion: Output of the command confirming the presence or absence of `audit_todos.py` captured in a local log file.

## [6] Validation Criteria
- [ ] Agent correctly identifies system state (files) via `ls` or `find` (Perception).
- [ ] Agent explains why local inference is banned on the Dell server (4GB RAM/Accounting stability).
- [ ] Agent executes a shell command and uses the result to form its next response (Action → Perception loop).
- [ ] SESSION_LOG.md updated with the creation of this chapter file.

## [7] Upgrade Trigger
N/A — Foundation layer.

## [8] Session Log Entry
> Confirm on disk then append to SESSION_LOG.md:
> L0_C01_What_Is_An_Agent.md | [x] | 2026-04-24 | Chapter Writer | 3450 bytes

## [9] Connections
- Previous: Start here
- Next: L0_C02_The_Harness
- Context file: GENERATED_CONTEXT/layer_context.md
- New TOPIC_MAP entries: [Agent Loop Mechanics, Cloud-Compute constraints, ReAct Pattern]
