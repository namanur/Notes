# 📚 SKILLS REFERENCE - Quick Access

*The 6 core skills for operating in this vault*

---

## 1. DAILY LOG (`daily_log.md`)
**Purpose:** Track daily progress

**Steps:**
1. Check `00_daily_logs/` for today's file (DD-MM-YYYY.md)
2. If not exists → copy from `Daily log template.md`
3. Fill "To Do" and "What I Did" sections

**Location:** `00_daily_logs/`

---

## 2. STRATEGY LOG (`strategy_log.md`)
**Purpose:** Document architectural decisions

**Steps:**
1. Identify the system being modified
2. Create/update `REBUILD_STRATEGY.md` in project folder
3. Document: Current state → Problem → Solution → Rationale

**Location:** Project folder (e.g., `08_Work/ProjectName/`)

---

## 3. VAULT INDEXING (`vault_indexing.md`)
**Purpose:** Keep VAULT_INDEX.md current

**Steps:**
1. Scan vault: `find . -name "*.md" -not -path "./.git/*"`
2. Open `99_System/VAULT_INDEX.md`
3. Categorize: Learning, Projects, Logs, System
4. One-sentence description per file

---

## 4. SYLLABUS BUILDER (`syllabus_builder.md`)
**Purpose:** Update learning progress

**Steps:**
1. Scan `10_Knowledge/` for notes
2. Open `ROADMAP.md` (or `SYLLABUS.md`)
3. Update status: `[x]` done, `[/]` in-progress, `[ ]` pending
4. Add one-line summaries

---

## 5. SESSION CLOSE (`session_close.md`)
**Purpose:** End session properly (triggered by `/end`)

**Steps:**
1. Scan: What files changed?
2. Write: Update `00_daily_logs/DD-MM-YYYY.md`
3. Progress: Mark completed in `ROADMAP.md`
4. Next: Update `000_START_HERE.md` with tomorrow's start

**Template sections:**
- What I did
- What I learned
- What changed
- Tomorrow starts at

---

## 6. WIKI MAINTAINER (`wiki_maintainer.md`)
**Purpose:** Compile knowledge into LLM Wiki

**Steps:**
1. Source: Find completed content in daily logs or knowledge
2. Check: Look up entity in `Documents/llm-wiki/index.md`
3. Write: Create/update wiki page with YAML metadata
4. Link: Add to index with `[[double brackets]]`
5. Log: Record in `Documents/llm-wiki/log.md`

**Wiki Location:** `Documents/llm-wiki/`

---

## 🚀 QUICK COMMANDS

```bash
# Start session - check daily log
ls ~/Documents/Notes/00_daily_logs/

# End session - run session_close skill
# 1. Update daily log
# 2. Update roadmap
# 3. Update start here

# After major changes - run vault_indexing
# Update VAULT_INDEX.md

# After learning phase - run syllabus_builder  
# Update ROADMAP.md

# Compile to wiki - run wiki_maintainer
# Add to Documents/llm-wiki/
```

---

*Reference: skills/ folder*