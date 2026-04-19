# Session Close & Daily Log (/end)
**Purpose:** Close the working session, capture everything, and perform vault maintenance.
**When to use:** Triggered by user command `/end` or `/end read filename.md`.
**Steps:**
1. **Scan the session**: Identify all files opened, created, or modified. Summarize accomplishments vs. unfinished tasks.
2. **Read scratch note (if provided)**: Extract useful information from the specified file, then **DELETE** it.
3. **Write daily log entry**: Update `00_daily_logs/DD-MM-YYYY.md` with sections for "What I did," "What I learned," "What changed," and "Tomorrow starts at."
4. **Update progress**: Mark completed topics in `10_Knowledge/20-Day Curriculum.md` and set tomorrow's starting point in `000_START_HERE.md`.
5. **Confirm and close**: Provide a final summary of the logged session.
**Output:** An updated daily log, progress tracking, and a clean workspace.
