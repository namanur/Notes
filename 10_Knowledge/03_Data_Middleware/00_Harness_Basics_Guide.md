# 🎯 COMPLETE HARNESS & AGENT MASTERY GUIDE

*From Zero to Building Production-Ready AI Systems for Clients*

---

## 📖 PART 1: WHAT IS A HARNESS? (Simple Explanation)

### 🤖 The Problem Before Harnesses

Imagine you have a brilliant AI (like GPT-4) that can answer questions. But it can't:
- 📂 Read your files
- 💻 Run code on your computer  
- 📊 Access your database
- 🌐 Browse the internet

It's like having a super-smart brain trapped in a box with no arms, legs, or senses.

### 🦾 The Solution: Tools + Harness

A **Harness** is like a **suit of armor** that gives your AI:
1. **Eyes** (read files, see screen, browse internet)
2. **Hands** (write code, create files, run commands)
3. **Memory** (remember conversations, store data)
4. **Voice** (talk to other APIs, send emails)

```
┌─────────────────────────────────────────────────────────┐
│                    YOUR AI (LLM)                         │
│         "I want to build a website"                     │
└─────────────────────┬───────────────────────────────────┘
                      │
                      ▼
┌─────────────────────────────────────────────────────────┐
│                   HARNESS LAYER                          │
│  ┌─────────┐  ┌─────────┐  ┌─────────┐  ┌─────────┐     │
│  │  READ   │  │  WRITE  │  │  BASH   │  │  EDIT   │     │
│  │  tool  │  │  tool  │  │  tool   │  │  tool   │     │
│  └─────────┘  └─────────┘  └─────────┘  └─────────┘     │
└─────────────────────┬───────────────────────────────────┘
                      │
                      ▼
┌─────────────────────────────────────────────────────────┐
│                 YOUR COMPUTER                            │
│    Files, Terminal, APIs, Database, Internet            │
└─────────────────────────────────────────────────────────┘
```

### 🔧 Types of Harnesses

| Harness Type | What It Does | Example |
|--------------|--------------|---------|
| **CLI Harness** | AI talks to terminal | Pi Agent, Goose |
| **API Harness** | AI talks to web services | MCP Servers |
| **Browser Harness** | AI controls a browser | Computer Use Agent |
| **Custom Harness** | Tailored for specific tasks | Your custom tools |

---

## 📖 PART 2: THE 4 NATIVE TOOLS (What You Already Have)

Pi Agent comes with 4 built-in tools (your "basic armor"):

### 1. 🔍 **read** - The Eyes
```bash
# Read a file
read path="/home/naman/Notes/todo.md"

# Read specific lines (from line 10, max 20 lines)
read path="/home/naman/Notes/todo.md" offset=10 limit=20

# Read an image
read path="/home/naman/Pictures/screenshot.png"
```

### 2. ✏️ **write** - Creation
```bash
# Create a new file
write path="/home/naman/new_file.md" content="# Hello World\n\nThis is my first file!"

# Overwrite existing file
write path="/home/naman/old.txt" content="New content"
```

### 3. ✂️ **edit** - Modification (Find & Replace)
```bash
# Find old text, replace with new
edit path="/home/naman/file.md" oldText="old word" newText="new word"
```

### 4. 💻 **bash** - The Hands
```bash
# Run any terminal command
bash command="ls -la"

# Run a script
bash command="python3 my_script.py"

# Install something
bash command="npm install express"
```

---

## 📖 PART 3: YOUR CURRENT SETUP

### What's Already Working ✅

| Component | Status | Command to Use |
|-----------|--------|----------------|
| **Pi Agent** | ✅ Ready | `pi` or `pifallback` |
| **Goose Agent** | ✅ Ready | `goose run -t "prompt"` |
| **Ollama (MiniMax)** | ✅ Running | Via pifallback |
| **Google Gemini OAuth** | ✅ Connected | Auto via google-gemini-cli |
| **Fallback Script** | ✅ Created | `pifallback` |

### Your Config Files

```
~/.pi/agent/
├── settings.json    ← Default model, thinking level
├── models.json      ← Provider configurations  
├── auth.json        ← OAuth tokens
└── sessions/        ← Chat history

~/.config/goose/
└── config.yaml      ← Goose settings
```

---

## 📖 PART 4: BUILDING CUSTOM TOOLS & MCP

### Step 1: Simple Custom Tool (No Code)

Create a wrapper script that ai can call:

```bash
# Create a custom tool
mkdir -p ~/.pi/tools
mkdir -p ~/.pi/tools/greeting

# Create the tool script
cat > ~/.pi/tools/greeting/run.sh << 'EOF'
#!/bin/bash
NAME="${1:-World}"
echo "🎉 Hello, $NAME! Welcome to your AI harness."
EOF

chmod +x ~/.pi/tools/greeting/run.sh
```

Now pi can use it:
```bash
bash command="~/.pi/tools/greeting/run.sh Naman"
```

### Step 2: Python MCP Server (Real Tools for Clients)

This is what you'll build for actual clients - a proper MCP server:

```python
# ~/.pi/mcp/my_server.py
from mcp.server import Server
from mcp.types import Tool, TextResource
import json

# Create server
app = Server("my-custom-server")

# Define tools
@app.list_tools()
async def list_tools():
    return [
        Tool(
            name="greet",
            description="Greet someone by name",
            inputSchema={
                "type": "object",
                "properties": {
                    "name": {"type": "string", "description": "Name to greet"}
                },
                "required": ["name"]
            }
        ),
        Tool(
            name="read_database",
            description="Read data from SQLite database",
            inputSchema={
                "type": "object",
                "properties": {
                    "query": {"type": "string", "description": "SQL query"}
                },
                "required": ["query"]
            }
        )
    ]

@app.call_tool()
async def call_tool(name: str, arguments: dict):
    if name == "greet":
        return f"Hello, {arguments['name']}! 👋"
    
    elif name == "read_database":
        # Execute SQL query
        import sqlite3
        conn = sqlite3.connect("my_client.db")
        cursor = conn.cursor()
        cursor.execute(arguments["query"])
        results = cursor.fetchall()
        conn.close()
        return str(results)

# Run the server
if __name__ == "__main__":
    import mcp.server.stdio
    mcp.server.stdio.run(app)
```

---

## 📖 PART 5: YOUR LEARNING ROADMAP (Based on Your Vault)

### Phase A: Foundation (Days 1-10) - YOU ALREADY DID THIS ✅
- [x] Linux basics
- [x] File operations
- [x] Git & GitHub
- [x] Python basics

### Phase B: Harness Basics (Days 11-20)

| Day | Topic | What to Build | Command |
|-----|-------|---------------|---------|
| 11 | Python CLI | Tool wrapper script | `python3 tool.py --help` |
| 12 | Environment Variables | Secure API key handling | `echo $API_KEY` |
| 13 | JSON Handling | Parse API responses | `jq '.data'` |
| 14 | SQLite Basics | Create database | `sqlite3 db.sqlite` |
| 15 | Python + SQLite | CRUD operations | `python3 db.py` |

### Phase C: MCP Mastery (Days 21-30)

| Day | Topic | What to Build | Used By |
|-----|-------|---------------|---------|
| 21 | MCP Protocol | Understand JSON-RPC | - |
| 22 | First MCP Server | Hello World server | `pi -e server.py` |
| 23 | Tool Definition | Custom tool with schema | Clients |
| 24 | Resource Provider | Expose files as resources | Pi, Goose |
| 25 | Authentication | OAuth flow for clients | Production |

### Phase D: Building for Clients (Days 31-40)

| Day | Project | For Social Media |
|-----|---------|------------------|
| 31 | Portfolio Website Generator | 💼 Show what you build |
| 32 | Code Review Bot | 🔥 Demo thread |
| 33 | Research Agent | 🧠 Impressive capability |
| 34 | Multi-Agent System | 🤖 Complex demo |
| 35 | Client Dashboard | 💰 Real product |

---

## 📖 PART 6: SOCIAL MEDIA & PERSONAL BRAND

### 🎯 Content Strategy for X & Instagram

| Platform | Content Type | Best For |
|----------|--------------|----------|
| **X (Twitter)** | Threads, Code Demos | Devs, technical audience |
| **Instagram** | Reels, Carousels | Visual learners, broader audience |
| **LinkedIn** | Case Studies, Articles | Professional, clients |

### 📱 Quick Demo Ideas (30 seconds each)

1. **"Watch AI build..."**
   - Record screen: `pi` builds a file in real-time
   - Caption: "30 seconds with @pi_cli = a new file created"

2. **"Error → Fixed"**
   - Show error screenshot
   - Let AI fix it
   - Caption: "AI debugged my code in 5 seconds"

3. **"Before & After"**
   - Messy code screenshot
   - AI refactored screenshot
   - Caption: "Same file, different universe"

4. **"Terminal Magic"**
   - Type one command
   - AI does 10 things
   - Caption: "This one command did ALL this"

### 🚀 Building Your Portfolio (What to Show)

Create a `/home/naman/portfolio` folder with:

```
portfolio/
├── 01_hello_world/       # First MCP server
├── 02_code_reviewer/     # AI code review tool  
├── 03_research_agent/   # Research assistant
├── 04_portfolio_gen/     # Auto portfolio builder
└── README.md            # Your story
```

Each folder should have:
- `DEMO.gif` or `DEMO.mp4` - Visual demo
- `SOURCE_CODE.md` - How it works
- `SETUP.md` - How to run it

---

## 🎯 YOUR NEXT STEPS

### Immediate Actions:

1. **Test your setup:**
   ```bash
   pi -p "Hello, what 4 tools do you have?"
   ```

2. **Try the fallback:**
   ```bash
   pifallback "Hello"
   ```

3. **Test Goose:**
   ```bash
   gooserun -t "Hello"
   ```

4. **Create your first custom tool:**
   ```bash
   mkdir -p ~/.pi/tools/my_first_tool
   echo '#!/bin/bash
   echo "Hello from custom tool!"' > ~/.pi/tools/my_first_tool/run.sh
   chmod +x ~/.pi/tools/my_first_tool/run.sh
   ```

### This Week's Goals:

| Goal | Status | Evidence |
|------|--------|----------|
| Master 4 native tools | ⏳ Test each one | Screenshots |
| Build 1 custom wrapper | ⏳ Create in ~/.pi/tools | File exists |
| Document in Obsidian | ⏳ Add to vault | New note |
| Create 1 demo video | ⏳ Record 30 sec | .mp4 file |

---

## 🔗 QUICK REFERENCE COMMANDS

### Pi Agent
```bash
pi                          # Interactive mode
pi -p "prompt"              # One-shot mode
pi --model ollama/llama3    # Use specific model
pi --continue               # Resume session
pi -e /path/to/server.py    # With MCP extension
```

### Goose
```bash
goose run -t "prompt"       # One-shot
goose session               # Interactive
goose config                # Configure
```

### MCP Testing
```bash
# Test MCP server
python3 /path/to/server.py

# Connect agent to MCP
pi -e /path/to/server.py "your prompt"
```

---

*This guide builds on your existing 40-day roadmap. You're already on Day 23 (AI Agent Foundations) - keep going!*

**Next: 04_First_MCP_Server** → Build your first real MCP tool