# Phase 4: MCP Tools Development
**Track:** Agent & MCP
**Parent:** [[ROADMAP]]

## 🧠 Mental Model: The JSON-RPC Negotiation
MCP Tools are not "functions" in the traditional sense; they are **Capability Declarations**. The agent is a client that perceives the world through a schema. When an agent "calls" a tool, it is actually emitting a structured intent that a server interprets.

1. **The Schema is the Reality:** If your tool description is vague, the agent will hallucinate parameters. The schema is the only interface between the LLM's probabilistic weights and your deterministic code.
2. **Stateless Execution:** Every tool call should be treated as an atomic operation. The agent has no "memory" of previous tool outputs unless you explicitly feed them back into the context.
3. **The Loop:** Discovery (List Tools) -> Selection (Agent decides) -> Call (JSON-RPC) -> Result (Structured data).

---

## 💻 Technical Deep Dive: FastMCP & Handshakes
Focus on modern implementation using Python or TypeScript SDKs.

### 1. Tool Definition (Python FastMCP)
```python
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("SystemOptimizer")

@mcp.tool()
def optimize_process(pid: int, aggressive: bool = False) -> str:
    """
    Optimizes a system process by PID. 
    Use 'aggressive' mode only for non-critical services.
    """
    # Logic: interaction with OS primitives
    return f"Process {pid} optimized (Aggressive: {aggressive})"
```

### 2. Error Handling (The Protocol Way)
Do not just throw exceptions. Return meaningful error strings that the agent can use to "retry" or "fix" the call.
```python
if pid < 0:
    return "Error: PID must be a positive integer. Please verify the process ID and try again."
```

### 3. Testing via MCP Inspector
```bash
# Debug your server locally
npx @modelcontextprotocol/inspector python my_server.py
```

---

## ⚡ Mastery Drills: High-Pain Execution
*Goal: Force agent confusion and protocol failure.*

1. **The Vague Schema:** Write a tool with a description like "Does stuff" and parameters named `a`, `b`, and `c`. Try to get an agent to use it correctly. Experience the hallucination peak.
2. **The 50% Failure:** Write a tool that randomly returns a "Connection Timed Out" error. Watch how the agent handles (or fails to handle) the retry logic.
3. **The Dependency Trap:** Create two tools where Tool B requires the output of Tool A, but Tool A's output format is intentionally complex (e.g., nested JSON with escaped strings). Force the agent to parse and pass it.

---

## 📜 Execution Contract
- **Timebox:** 1.5 Hours.
- **Start Command:** `npx @modelcontextprotocol/inspector <your_server_command>`
- **Completion Condition:** Successfully build and register an MCP tool that performs a multi-step filesystem operation (e.g., find all .log files, zip them, and return the path) and verify it via the Inspector.

---
**Links:** [[ROADMAP]] | [[00_daily_logs/AGENT_ACTIVITY]]
