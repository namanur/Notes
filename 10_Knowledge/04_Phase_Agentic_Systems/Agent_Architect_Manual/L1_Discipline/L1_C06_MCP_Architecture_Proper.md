# Chapter 06: MCP Architecture Proper
> Layer: L1 | Prerequisite: L1_C05_Domain_Driven_Design_For_Agents.md
> Context injected from: UBIQUITOUS_LANGUAGE only

## [1] Concept Explanation
The Model Context Protocol (MCP) is the open standard that replaces ad-hoc "hacks" with a formalized interface between the Reasoning engine (LLM) and the Action/Perception layers (Harness). It operates primarily over JSON-RPC 2.0.

- **MCP Client:** The application (e.g., Gemini CLI, Goose) that connects to servers and manages the LLM's context.
- **MCP Server:** The host process providing Tools and Resources. It maintains the "thick boundary" between the agent's reasoning and the environment.
- **Tools:** Executable functions that can modify state (Action). Defined with input schemas.
- **Resources:** Static or dynamic data providers (Perception). Read-only by default.
- **JSON-RPC Depth:** Every interaction follows a `request` -> `response` or `error` pattern. A request includes a `method`, `params`, and an `id`. A response returns a `result` mapped to that `id`. An error returns a structured object with a `code` and `message`.

## [2] Why This Layer Exists
Without MCP, agents use brittle, non-standardized scripts. Standardizing on MCP allows for:
1. **Tool Portability:** One server can serve multiple clients (Goose, Gemini CLI, Claude Desktop).
2. **Composition:** Small, domain-specific servers can be "stitched" together.
3. **Safety:** JSON-RPC enforces strict input validation and structured error reporting, preventing "hallucinated" tool calls from crashing the system.

## [3] Stack Integration
In this stack, the **Dell Ubuntu Server** acts as the primary host for MCP servers. While the **Gemini CLI** (Client) may run on the VivoBook or the Server, the MCP servers are co-located with the **SQLite** state (Memory) and **ERPNext** files. This ensures low latency between the Action layer and the data it manipulates.

## [4] What To Read / Watch / Study
- [Model Context Protocol Specification](https://modelcontextprotocol.io)
- [JSON-RPC 2.0 Specification](https://www.jsonrpc.org/specification)
- Python `mcp` SDK documentation.

## [5] Hands-On Execution
In Chapter C04, you created a raw Bash script for file manipulation. Now, wrap it in a proper MCP server using Python to enforce the protocol boundary.

**Exercise: The Python MCP Wrapper**
1. Install the MCP SDK: `pip install mcp`
2. Create `mcp_file_server.py`.
3. Define a tool `bash_execute` that takes a `command` string.
4. Implement a robust error response: if the bash command fails (non-zero exit), return a structured JSON-RPC error instead of a raw stack trace.

**Proof of Completion:**
Run the server using `npx @modelcontextprotocol/inspector python3 mcp_file_server.py`. Verify that calling the tool with an invalid command (e.g., `ls /nonexistent`) returns a proper `isError: true` response in the inspector.

## [6] Validation Criteria
- The server initializes with a `list_tools` capability.
- All tool inputs are validated against a JSON Schema.
- Errors are returned as protocol-compliant error objects, not raw text.
- The client can discover the tool dynamically without manual configuration of paths.

## [7] Upgrade Trigger
As long as your tools are standalone scripts, your agents are "silos." To reach **L3 Swarms** (Orchestrators coordinating multiple agents), your tools must be composable. If you cannot "hot-plug" a new tool into your agent loop via a protocol, you have hit the ceiling of L1.

## [8] Session Log Entry
`[DATE] | ARCH: Formalized MCP Architecture | ACTION: Wrapped C04 Bash tool in Python MCP Server | RESULT: Achieved protocol-compliant error handling and tool discovery.`

## [9] Connections
- **Backward:** [[L0_C04_Your_First_Harness]] (The raw tools we are now formalizing).
- **Forward:** [[L2_C07_SQLite_State_Management]] (Persisting tool results into long-term memory).
