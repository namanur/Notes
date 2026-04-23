# Git History and Diffs
Phase Phase 1 | [[Git_Internals_DAG]]

## 1. The Mental Model
Git is a content-addressable filesystem. A "commit" is a snapshot of your entire project, not a "diff" from the previous version. 
- **The Log:** A linear view of the directed acyclic graph (DAG).
- **The Diff:** A calculation performed on the fly by comparing two snapshots (blobs/trees).
- **HEAD:** A pointer to your current location in the graph.

## 2. Technical Deep Dive
### Modern Inspection
- **The Log (Readable):** `git log --oneline --graph --decorate --all`.
- **Finding "When":** `git log -S "search_string"` (The "Pickaxe" - finds when a specific string was added or removed).
- **The Diff (Surgical):**
  - `git diff`: Staging area vs. Working directory.
  - `git diff --staged`: Last commit vs. Staging area.
  - `git diff HEAD~1 HEAD`: Compare current commit with its parent.
- **Blame (Ownership):** `git blame -L 10,20 file.txt` (See who changed lines 10-20 and when).

### Pro-Tip: Patch Mode
- `git add -p`: Interactively choose which parts of a file to stage. This is how you keep commits "atomic" (focused on one change).

## 3. Mastery Drills
### Terminal Challenges
1. **The Archeologist:** Find the exact commit message and author of the person who first added a specific function name to a file, even if it was deleted 5 commits ago.
2. **The Partial Stager:** Modify 3 different functions in one file. Use `git add -p` to create 3 separate commits, one for each function change.

### Edge Cases
- **Deleted File Recovery:** If you deleted a file and committed it, find the last commit where it existed using `git rev-list -n 1 HEAD -- <file_path>` and then restore it.

## 4. Execution Contract
- **Timebox:** 30 minutes
- **Start Command:** `git init history_lab && echo "v1" > file.txt && git add . && git commit -m "initial"`
- **Completion Condition:** Successfully use `git log -S` to find a deleted line and `git show` to view the full context of that change.
