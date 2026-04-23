# Vault Indexing Skill
**Purpose:** Maintain a current, flat map of all notes in the vault with their
descriptions. Stay in sync with the Agent Architect Manual v2.2 build state
across all sessions — not just Session 1.

**When to use:**
- After every Agent Architect Manual session (mandatory — runs after Index Agent)
- After any file addition, rename, or reorganization outside the manual build
- Whenever SESSION_LOG.md has entries marked [x] that haven't been reflected
  in VAULT_INDEX.md yet

---

## Core Rule
This skill is a mirror of disk state. It reflects what exists, not what is
planned. It runs AFTER the Index Agent (Template C) in every session — never
before. The Index Agent updates 00_MANUAL_INDEX.md and TOPIC_MAP.md. This
skill updates VAULT_INDEX.md. They are separate jobs.

---

## Steps

### 1. Run Disk Validation First
Every time, no exceptions:
```bash
bash /home/naman/Documents/Notes/10_Knowledge/04_Phase_Agentic_Systems/Agent_Architect_Manual/_SYSTEM/validate_disk_state.sh
```
Read the output before touching anything.
- File shows OK → eligible for indexing
- File shows MISSING but marked [x] in SESSION_LOG.md → ghost entry
  — clear the [x] in SESSION_LOG.md, add note in Session History
  — do NOT index it
- File shows MISSING and not marked [x] → not yet spawned, ignore

### 2. Determine What Is New Since Last Index Run
Read the last `VAULT_INDEX updated:` line in SESSION_LOG.md. Only files
written or confirmed after that timestamp need to be processed. Do not
re-read the entire vault on every run — append and prune only.

### 3. Scan for New Files
Check these locations for files added since last index run:
```
L0_Foundation/         → after Session 1
L1_Discipline/         → after Session 2
L2_Production/         → after Session 3
L3_Scale/              → after Session 4
L4_Leverage/           → after Session 5
GENERATED_CONTEXT/     → after each layer's Context Curator run
STUDY_NOTES/           → only confirmed notes (STUDY_NOTE_DONE in SESSION_LOG)
_SYSTEM/               → after bootstrap and any system file additions
```
Also check root files: UBIQUITOUS_LANGUAGE.md, 00_MANUAL_INDEX.md, TOPIC_MAP.md

### 4. Open `99_System/VAULT_INDEX.md`
Append new entries. Prune entries whose files no longer exist on disk.
Never rewrite the entire file.

### 5. Categorize Using These Buckets

| Bucket | What Goes Here |
|---|---|
| Learning | All L0–L4 chapter files (C01–C15) |
| Generated Context | All GENERATED_CONTEXT/*.md files |
| Study Notes | Confirmed STUDY_NOTES/ files only |
| System | All _SYSTEM/ files + UBIQUITOUS_LANGUAGE.md |
| Navigation | 00_MANUAL_INDEX.md + TOPIC_MAP.md |
| Logs | SESSION_LOG.md |
| Projects | Any non-manual project notes |
| Archive | Superseded drafts, old prompt versions |

### 6. Per-Note Entry Format
```
- [[Note Name]] — [one sentence: what this file contains, which layer it
  belongs to, and what it enables] | Layer: [L0–L4 or System] |
  Session: [which session wrote it] | Status: [complete/partial/failed] |
  Bytes: [from disk check]
```

For FAILED entries from SESSION_LOG.md:
```
- [[Note Name]] — FAILED: [chapter mandate summary] | Layer: [L0–L4] |
  Session: [session number] | Status: failed — re-queue next session
```

### 7. Session-by-Session Index Gates
After each session, verify these entries exist before closing:

**After Session 1 (Bootstrap + L0):**
```
[ ] UBIQUITOUS_LANGUAGE.md — System
[ ] _SYSTEM/FALLBACK_CHAIN.sh — System
[ ] _SYSTEM/SESSION_LOG.md — Logs
[ ] _SYSTEM/GRILL_ME_TEMPLATE.md — System
[ ] L0_C01 through L0_C04 — Learning (all four)
[ ] GENERATED_CONTEXT/L0_Foundation_context.md — Generated Context
[ ] TOPIC_MAP.md — Navigation
[ ] 00_MANUAL_INDEX.md — Navigation
```

**After Session 2 (L1):**
```
[ ] L1_C05, L1_C06, L1_C07 — Learning
[ ] GENERATED_CONTEXT/L1_Discipline_context.md — Generated Context
[ ] Any STUDY_NOTES confirmed before L1 chapters — Study Notes
```

**After Session 3 (L2):**
```
[ ] L2_C08, L2_C09, L2_C10 — Learning
[ ] GENERATED_CONTEXT/L2_Production_context.md — Generated Context
[ ] Any STUDY_NOTES confirmed before L2 chapters — Study Notes
```

**After Session 4 (L3):**
```
[ ] L3_C11, L3_C12 — Learning
[ ] GENERATED_CONTEXT/L3_Scale_context.md — Generated Context
[ ] Any STUDY_NOTES confirmed before L3 chapters — Study Notes
```

**After Session 5 (L4):**
```
[ ] L4_C13, L4_C14, L4_C15 — Learning
[ ] GENERATED_CONTEXT/L4_Leverage_context.md — Generated Context
[ ] Any STUDY_NOTES confirmed before L4 chapters — Study Notes
```

**Final vault state (all sessions complete):**
```
[ ] All 15 chapter files — Learning
[ ] All 5 context files — Generated Context
[ ] All confirmed study notes — Study Notes
[ ] All _SYSTEM/ files — System
[ ] UBIQUITOUS_LANGUAGE.md — System
[ ] TOPIC_MAP.md and 00_MANUAL_INDEX.md — Navigation
[ ] SESSION_LOG.md — Logs
[ ] Zero ghost entries
[ ] Zero planned-only links in VAULT_INDEX.md
```

### 8. Study Notes — Confirmation Gate
A study note is only indexed after "STUDY_NOTE_DONE: [topic]" appears in
SESSION_LOG.md. Until then it is a draft. Drafts are never indexed.

Format for confirmed study note entry:
```
- [[STUDY_NOTES/topic_slug]] — Study note for [topic]: confirmed before
  [chapter filename], Grill Me passed: [yes/no] | Layer: [L0–L4] |
  Status: confirmed
```

### 9. Soft Failure Alignment
If SESSION_LOG.md contains FAILED entries for any chapter:
- Index the failure as a Learning entry with Status: failed
- Do not leave a gap — a logged failure is still vault state
- The entry reminds you to re-queue it next session

### 10. Internal Link Validation
All `[[Internal Links]]` in VAULT_INDEX.md must resolve to files on disk.
Tag any link pointing to a planned-but-unspawned file:
```
| Status: planned — not yet spawned | Session: [target session]
```

### 11. Update SESSION_LOG.md
Append to the current session's history entry:
```
VAULT_INDEX updated: [timestamp] | New entries: [count] |
Removed: [count] | Ghost entries resolved: [count or "none"] |
Failed entries indexed: [count or "none"]
```

---

## What This Skill Does NOT Do
- Does not write or modify chapter files
- Does not modify 00_MANUAL_INDEX.md or TOPIC_MAP.md (Index Agent owns those)
- Does not run before the Index Agent in any session
- Does not index unconfirmed STUDY_NOTES drafts
- Does not rebuild VAULT_INDEX.md from scratch
- Does not mark SESSION_LOG.md entries [x] — only appends the index
  confirmation line

---

## Output
An up-to-date `99_System/VAULT_INDEX.md` that mirrors exact disk state across
all 5 sessions of the v2.2 build, with every file categorized, every failure
logged, every ghost entry resolved, and a SESSION_LOG.md confirmation line
written before the skill exits.
