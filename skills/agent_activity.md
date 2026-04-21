# Agent Activity Logging Procedure

## Purpose
This skill outlines the mandatory procedure for all AI agents working within this vault to log their activity. The goal is to maintain a clear, chronological record of changes, ensuring continuity and understanding across different agent sessions.

## Procedure

### Step 1: Read the Agent Activity Log
Upon starting a new session or receiving a task, the agent MUST first read `00_daily_logs/AGENT_ACTIVITY.md` to understand the most recent activities and context left by previous agents or the user.

### Step 2: Prepare Your Log Entry
Before making any changes or concluding your session, prepare a log entry that adheres to the following markdown format. This entry will be appended to `00_daily_logs/AGENT_ACTIVITY.md`.

#### Log Entry Format:
```markdown
### [[YYYY-MM-DD]] - [Agent Name] - [HH:MM]

**Goal:** [Briefly state the primary objective of your session.]

**Changes Made:**
- [Summarize the significant changes you made to files, folders, or content within the vault.]
- [Be specific but concise. Include file paths where appropriate.]
- [Example: Created 10_Knowledge/New Topic.md, Edited 99_System/Topics.md to add link.]

**Next Steps/Recommendations:**
- [Outline any unfinished tasks, recommendations for the next agent, or areas that require further attention.]
- [Example: Next, verify internal links in New Topic.md. Consider consolidating XYZ notes.]

---
```

### Step 3: Append Your Log Entry
Once your session is complete or you are about to hand over control, append your prepared log entry to the end of `00_daily_logs/AGENT_ACTIVITY.md`. Ensure the new entry is added *below* the previous entries.

### Step 4: Confirm Logging
(Optional but Recommended for Manual Agents): After appending, briefly re-read the last few lines of `00_daily_logs/AGENT_ACTIVITY.md` to ensure your entry was correctly added.

## Guidelines for Content:
- **Agent Name**: Clearly identify yourself (e.g., "Pi Agent", "Gemini CLI Agent", "Claude").
- **Timestamp**: Use the `YYYY-MM-DD` and `HH:MM` format for consistency.
- **Goal**: Focus on the *why* of your session.
- **Changes Made**: Focus on the *what* and *where* of your actions.
- **Next Steps**: Focus on the *how to proceed* for future agents or yourself.
- **Wikilinks**: Use `[[wikilinks]]` for internal references where appropriate.

## Example of a Log Entry:
```markdown
### [[2026-04-21]] - Pi Agent - 14:30

**Goal:** Add "Understanding YAML" to learning notes and set up agent activity logging.

**Changes Made:**
- Created `10_Knowledge/Understanding YAML.md` with an overview of YAML.
- Created `00_daily_logs/AGENT_ACTIVITY.md` as the central activity log.
- Created `skills/agent_activity.md` detailing this logging procedure.
- Updated `skills/SKILLS_INDEX.md` to include `[[agent_activity]]`.

**Next Steps/Recommendations:**
- User to manually install the Gemini CLI skill for automated logging.
- Future agents to read `[[agent_activity]]` skill and `[[AGENT_ACTIVITY]]` log upon starting.
- Monitor `AGENT_ACTIVITY.md` for consistency and adherence to format.

---
```
