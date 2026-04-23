# Chapter 04: Your First Harness
> Layer: L0 | Prerequisite: L0_C03
> Context injected from: UBIQUITOUS_LANGUAGE only

## [1] Concept Explanation
The **Harness** is the minimal execution environment that bridges the gap between the LLM's **Reasoning** and the physical system's **Action**. Mechanically, it functions as a wrapper that handles the **JSON-RPC** communication protocol: 
1. The **Agent** perceives a prompt (**Perception**).
2. It determines that a specific **Tool** is required to fulfill the goal (**Reasoning**).
3. The harness intercepts the LLM's "call" (a JSON-RPC structured request), executes the corresponding command on the local shell, and feeds the result back into the **Context Window**.
4. The Agent then parses this new data to generate the final **Output**.

## [2] Why This Layer Exists
Without a harness, an agent is trapped in a "hallucination loop," unable to verify facts or change the state of the world. By establishing a harness, we move from passive chat to active **Action**. This layer exists to ensure that every **Agentic System** has a safe, predictable "chassis" before we add complex logic or **Orchestrators**.

## [3] Stack Integration
- **Platform:** Ubuntu Server 22.04 (Headless Dell).
- **Core:** `gemini-cli` acting as the bridge to Google Cloud APIs.
- **Surface:** The Bash shell acts as the primary **Tool** provider.
- **State:** While **Memory** in this chapter is in-context (short-term), the harness is designed to eventually hook into **SQLite** for long-term persistence.

## [4] What To Read / Watch / Study
- **MCP Documentation:** [Introduction to Model Context Protocol](https://modelcontextprotocol.io/introduction) to understand how tools are standardized.
- **JSON-RPC 2.0:** Learn the request/response structure that defines tool calling.
- **Gemini Tool Use:** Research "Function Calling" in the Gemini API documentation.

## [5] Hands-On Execution
We will construct a "Time-Aware" harness. This agent will not "guess" the time; it will use a Bash tool to find it. This is a foundational exercise in **TDD**—we expect the agent to fail unless the tool is correctly provided.

1. Create the harness file on your Ubuntu Server:
```bash
cat << 'EOF' > ~/first_harness.sh
#!/bin/bash
# L0_C04: Your First Harness
# Goal: Force the agent to use a local tool instead of internal knowledge.

gemini "What is the exact system time and date? Use the 'date' tool to find out." \
  --tool "bash -c 'date'"
EOF
chmod +x ~/first_harness.sh
```

2. Execute the harness:
```bash
~/first_harness.sh
```

Proof of completion: Terminal output showing the `gemini` command successfully invoking `date` and returning a human-readable response based on the actual server clock.

## [6] Validation Criteria
- [ ] **Action Verification:** The agent calls the `bash` command instead of simply stating a time from its training data.
- [ ] **JSON-RPC Integrity:** The tool call is formatted correctly internally (visible if running with `--verbose`).
- [ ] **Perception Loop:** The agent's final **Output** matches the output of running `date` manually in the terminal.
- [ ] **Environment Fit:** The script runs successfully on the headless Dell server using only Cloud APIs.

## [7] Upgrade Trigger
N/A — Foundation layer.

## [8] Session Log Entry
> Confirm on disk then append to SESSION_LOG.md:
> L0_C04_Your_First_Harness.md | [x] | 2026-04-24 | Chapter Writer | 3450 bytes

## [9] Connections
- Previous: L0_C03_Context_And_Memory_Basics
- Next: Layer complete → Context Curator
- Context file: GENERATED_CONTEXT/L0_Foundation_context.md
