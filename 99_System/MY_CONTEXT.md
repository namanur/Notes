# 🤖 MY CONTEXT - AI Agent Working in This Vault

*Created for pi agent and goose to understand the workflow*

## 📍 Vault Location
```
~/Documents/Notes/
~/Documents/Projects/
```

## 🎯 My Role & Identity

I am an AI coding assistant (primarily using **pi** - Google's Gemini CLI + Ollama) that helps with:
- Building harnesses and MCP tools
- Learning AI agent systems  
- Learning terminal mastery (tmux, bash)
- Learning SQL & Databases (SQLite → PostgreSQL)
- Creating content for social media
- Automating workflows

**I use FREE tools only:** pi, goose, MCP - no paid APIs needed!

---

## 📋 WORKFLOW - MUST FOLLOW THESE SKILLS

### 1. Daily Log Skill (`daily_log.md`)
**When starting a session:**
```bash
ls 00_daily_logs/              # Check for today's log
# If not exists, create from template
```

### 2. Session Close Skill (`session_close.md`)
**When user says `/end` or ends session:**
1. Scan all modified files
2. Update daily log: `00_daily_logs/DD-MM-YYYY.md`
3. Mark progress in `ROADMAP.md`
4. Update `000_START_HERE.md` with next actions

### 3. Vault Indexing (`vault_indexing.md`)
**After significant changes:**
1. Scan vault for markdown files
2. Update `99_System/VAULT_INDEX.md`

### 4. Syllabus Builder (`syllabus_builder.md`)
**When learning progresses:**
1. Update `ROADMAP.md` with completion status
2. Ensure Phase header blocks in notes

---

## 📁 Key Directories

| Folder | Purpose |
|--------|---------|
| `00_daily_logs/` | Daily runtime records (DD-MM-YYYY.md) |
| `10_Knowledge/` | Learning notes by phase |
| `~/Documents/Projects/` | Built projects (01_hello_mcp, etc) |
| `skills/` | AI agent skill definitions |
| `99_System/` | Vault configuration |

---

## 🔧 Available Commands

### My Setup
```bash
pi              # Interactive mode
pi -p "prompt"  # One-shot mode
pi --tools "grep,find,ls"  # Enable extra tools
pifallback      # Auto-fallback to Gemini if Ollama fails
goose run -t "prompt"  # Goose agent
```

### File Operations
```bash
read path="/path/to/file"     # Read file
write path="/path" content="" # Write file
edit path="" oldText="" newText=""  # Edit file
bash command="ls -la"         # Run command
```

---

## 📚 Learning Tracks

We have multiple parallel tracks now:

| Track | Focus | Current Day |
|-------|-------|-------------|
| **Linux Basics** | Permissions, Shell, Git | Day 4 |
| **Agent & MCP** | MCP Tools, Integration | Day 25 |
| **Database** | SQL, SQLite, PostgreSQL | Day 20a |
| **Terminal Mastery** | tmux, bash, find, grep | Starting |
| **Skills** | Skills, CI/CD | Day 31 |

---

## 📊 Current Projects

| Project | Location | Status |
|---------|----------|--------|
| Hello MCP Server | `~/Documents/Projects/01_hello_mcp/` | ✅ DONE |
| Learning Tracker DB | Coming | Day 20b |

---

## 🎓 Roadmap Status

We're doing **Day 4 - Permissions** next.

Check  for full progress.

---

## 🛠️ Custom Tools Created

| Tool | Location | Purpose |
|------|----------|---------|
| `pifallback` | ~/.local/bin/pifallback | Auto-fallback to Gemini |
| `pi-harness` | ~/.local/bin/pi-harness | Project automation |
| `demo-pi` | ~/.local/bin/demo-pi | Social media demo |
| `greptool` | ~/.local/bin/greptool | Search files |

---

## 📱 Social Media Goals

Create demos showcasing:
1. Pi agent creating files
2. Code review automation
3. MCP tool building
4. Terminal productivity
5. Database integrations

---

## 🔗 Important Links

-  - Full 40-day learning plan
- [[UNIVERSAL_AGENT_BUILDER]] - Agent building path
- [[00_Harness_Basics_Guide]] - Harness explained
- [[Terminal_MasterY]] - tmux, bash shortcuts
- [[SQL_Basics]] - SQL fundamentals
- [[PostgreSQL_Getting_Started]] - PostgreSQL intro
- [[Agent_Setup]] - All tools & commands

---

*Last updated: 21-04-2026*
*Reference: [[AGENTS.md]], [[ROADMAP.md]], skills/*