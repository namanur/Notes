# Git Internals (The DAG & Snapshots)
Phase Phase 1 | [[Git and GitHub Setup]]

## 1. The Mental Model
**Git is NOT a list of file changes (diffs).** It is a stream of **Snapshots**.

- **The DAG (Directed Acyclic Graph):** Every commit is a "node" in a graph. Each node points back to its parent(s). 
- **The Content-Addressable Filesystem:** Git stores everything as "objects" in a key-value store (the `.git/objects` folder). The key is a SHA-1 hash of the content.
- **Pointers:** Branches and Tags are just small text files containing a commit hash. `HEAD` is just a pointer to your current branch or commit.
- **Why this helps you debug:** If you understand that a branch is just a pointer, "merging" is just moving a pointer or creating a new node. If you lose a commit, it’s still in the objects folder until garbage collected—you just lost the pointer.

## 2. Technical Deep Dive
### Modern Command Set (The "Restore/Switch" Era)
Stop using `git checkout`. It is overloaded and dangerous. Use the specific tools:

- **`git switch <branch>`**: Moves the `HEAD` pointer to a different branch.
- **`git restore <file>`**: Discards changes in your working directory.
- **`git restore --staged <file>`**: "Unstages" a file (moves it from Index back to Working Dir).
- **`git log --graph --oneline --all`**: The only way to actually see the DAG.

### The Three States
1. **Working Directory:** Files you are currently editing.
2. **Staging Area (The Index):** The "Draft Snapshot" you are building.
3. **Repository (.git):** The permanent immutable database of snapshots.

## 3. Mastery Drills
### Terminal Challenges
1. **The Object Peek:** Create a file, `git add` it, then find it inside `.git/objects` by its hash. Use `git cat-file -p <hash>` to prove Git saw the content before you even committed.
2. **Manual Branching:** Create a new branch `test`. Go to `.git/refs/heads/`. Manually edit the `test` file with a different commit hash from `git log`. Run `git switch test`. Observe what happened.

### Edge Cases (The Pain)
1. **Detached HEAD Recovery:** 
   - `git switch --detach HEAD~1` (You are now off-graph).
   - Create a commit. 
   - `git switch master`. Your commit is now "lost."
   - **Task:** Find the "lost" commit hash using `git reflog` and point a new branch `recovered` at it.
2. **The "Oops" Restore:** Stage a file, then delete it from your disk manually. Use `git restore` to bring it back from the index.

## 4. Execution Contract
- **Timebox:** 25 minutes
- **Start Command:** `mkdir git-internals-lab && cd git-internals-lab && git init`
- **Completion Condition:**
  - [ ] Successfully recovered a "lost" commit via `reflog`.
  - [ ] Demonstrated `git cat-file` on a blob object.
  - [ ] Visualized a merge commit in the DAG using `git log --graph`.
