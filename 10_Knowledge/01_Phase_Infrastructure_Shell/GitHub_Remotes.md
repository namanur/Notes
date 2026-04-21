# GitHub and Remotes
[[Phase 1]] | [[Git_Branching_Merging]] | [[ROADMAP]]

## 1. The Mental Model
Remotes are just versions of your project hosted elsewhere (e.g., GitHub, a local server). 
- **Origin:** The default name for the primary remote.
- **Tracking Branch:** A local branch that "knows" about its remote counterpart (e.g., `origin/main`).
- **Push/Pull:** Synchronizing snapshots between your local DAG and the remote DAG.

## 2. Technical Deep Dive
### Setup and Auth
- **SSH over HTTPS:** Always use SSH keys. `ssh-keygen -t ed25519`.
- **Add Remote:** `git remote add origin git@github.com:user/repo.git`.
- **Set Upstream:** `git push -u origin main` (Links your local `main` to the remote `main`).

### Synchronizing
- **Fetch:** `git fetch origin` (Downloads new data but doesn't touch your working files). Safest.
- **Pull:** `git pull` (Fetch + Merge). Risky if your history has diverged.
- **Push:** `git push`.

### Pro-Tip: Force Push (Safety First)
- `git push --force-with-lease`: Overwrites the remote only if no one else has added commits in the meantime. Much safer than raw `--force`.

## 3. Mastery Drills
### Terminal Challenges
1. **The Remote Swap:** Create a repository. Add a local remote (another folder on your disk). Push to it. Then, rename that folder and update your `git remote` URL to match.
2. **The Sync War:** Clone your own repo to a different directory. Add a commit in `dir_a` and push. Add a commit in `dir_b` (without pulling) and try to push. Observe the rejection. Fix it by fetching and rebasing.

### Edge Cases
- **Changing Remotes:** `git remote set-url origin <new_url>`.

## 4. Execution Contract
- **Timebox:** 25 minutes
- **Start Command:** `ssh -T git@github.com` (Verify connection)
- **Completion Condition:** Successfully push a local repository to GitHub, delete the local folder, and re-clone it to verify everything is intact.
