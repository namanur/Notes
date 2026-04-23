# Phase 4: MCP Resources Architecture
**Track:** Agent & MCP
**Parent:** [[ROADMAP]]

## 🧠 Mental Model: The Observable Universe
If Tools are the agent's hands, **Resources** are its eyes. They represent read-only data that the agent can "pull" or "subscribe" to. Unlike tools, which are action-oriented, resources are data-oriented and stateful.

1. **URI-Based Access:** Everything is a URI (`mcp://host/path`). This allows for a clean, REST-like abstraction over any data source (files, DBs, API streams).
2. **Templates vs. Static:** Static resources are fixed. Templates (`mcp://logs/{date}`) allow the agent to request specific slices of data dynamically.
3. **Implicit vs. Explicit:** The agent doesn't always know what resources exist unless they are listed during discovery.

---

## 💻 Technical Deep Dive: URIs and Subscriptions

### 1. Defining a Resource (TypeScript SDK)
```typescript
server.resource(
  "system-info",
  "mcp://system/info",
  async (uri) => ({
    contents: [{
      uri: uri.href,
      text: JSON.stringify(process.memoryUsage()),
      mimeType: "application/json"
    }]
  })
);
```

### 2. Resource Templates
Allows the agent to construct URIs based on context.
```python
@mcp.resource("mcp://git/repo/{owner}/{name}/readme")
def get_readme(owner: str, name: str) -> str:
    # Logic to fetch README from GitHub
    return f"README for {owner}/{name}"
```

### 3. Subscriptions (The "Pulse")
Some servers support notifications. When a resource changes, the server sends a `notifications/resources/updated` message. The agent can then re-read the state.

---

## ⚡ Mastery Drills: High-Pain Execution
*Goal: Force resource exhaustion and URI collision.*

1. **The Infinite Stream:** Create a resource that returns a continuous stream of random data. See how the agent handles truncated context when the resource content exceeds its token limit.
2. **The URI Collision:** Register two different resources with nearly identical URIs (e.g., `mcp://log/system` and `mcp://logs/system`). Observe if the agent picks the correct one.
3. **The Binary Block:** Expose a binary file (PNG or PDF) as a resource without setting the correct `mimeType`. Watch the agent attempt to "read" raw binary as text.

---

## 📜 Execution Contract
- **Timebox:** 1 Hour.
- **Start Command:** `mcp inspector` with a custom resource-heavy server.
- **Completion Condition:** Create a Resource Template that accepts a filename and returns its content only if the file exists in a restricted directory. Verify by having the agent "look" at three different files.

---
**Links:** [[ROADMAP]] | [[00_daily_logs/AGENT_ACTIVITY]]
