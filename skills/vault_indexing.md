# Vault Indexing Skill
**Purpose:** Maintain a current, flat map of all notes in the vault with their descriptions.
**When to use:** After significant file additions, renames, or reorganizations.
**Steps:**
1. Recursively scan the vault for markdown files, ignoring `.git` and hidden folders.
2. Open `99_System/VAULT_INDEX.md`.
3. Categorize files into Learning, Projects, Logs, System, and Archive.
4. For each note, provide a concise one-sentence description.
5. Ensure all `[[Internal Links]]` in the index are accurate and resolve.
**Output:** An up-to-date, comprehensive `99_System/VAULT_INDEX.md`.
