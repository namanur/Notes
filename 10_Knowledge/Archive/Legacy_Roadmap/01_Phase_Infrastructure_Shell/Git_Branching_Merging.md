# Git Branching and Merging
[[Phase 1]] | [[Git_History_Diffs]] | [[ROADMAP]]

## 1. The Mental Model
A branch is nothing more than a lightweight, movable pointer to a commit. 
- **Branching:** Creating a new pointer.
- **Merging:** Bringing two "histories" (paths in the DAG) together.
- **Fast-Forward:** If the current branch is a direct ancestor of the target branch, Git just moves the pointer forward. No new commit is created.
- **Three-Way Merge:** If the paths diverged, Git finds a common ancestor and creates a "Merge Commit" to join them.

## 2. Technical Deep Dive
### Modern Branching (switch/restore)
- **New Branch:** `git switch -c feature-name` (Replaces `git checkout -b`).
- **Swap Branch:** `git switch main`.
- **Merge:** `git merge feature-name`.
- **Abort Merge:** `git merge --abort` (The "Panic" button during conflicts).

### Conflicts: The Reality
Conflicts happen when the same line is modified in both branches. 
- Git marks the file with `<<<<<<<`, `=======`, and `>>>>>>>`.
- You must manually edit, `git add`, and `git commit`.

### Advanced: Rebase
- `git rebase main`: "Rewrites history" by moving your feature branch to the tip of main. Creates a cleaner, linear history. **Rule:** Never rebase branches that have been pushed to a shared repository.

## 3. Mastery Drills
### Terminal Challenges
1. **The Conflict Maker:** Create two branches from `main`. Modify the same line in the same file in both branches. Commit both. Merge one into `main`, then try to merge the other. Resolve the conflict.
2. **The Fast-Forward Force:** Create a feature branch, add a commit. Merge it into `main` using `--no-ff`. Observe the difference in `git log --graph` compared to a standard fast-forward.

### Edge Cases
- **Detached HEAD:** What happens if you `git switch` to a commit hash instead of a branch? (You are no longer on a branch).

## 4. Execution Contract
- **Timebox:** 40 minutes
- **Start Command:** `git init merge_lab && echo "base" > file.txt && git add . && git commit -m "base"`
- **Completion Condition:** Successfully perform a `rebase` of a feature branch onto `main` and resolve at least one conflict during the process.
