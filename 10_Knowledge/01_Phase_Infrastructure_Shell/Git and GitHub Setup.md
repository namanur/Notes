---
Phase: [[Phase 0 — Learning Infrastructure]]
Project: [[01_Phase_Infrastructure_Shell]]
Prev: [[Workflow and Information Capture]] | Next: 
---

# Git and GitHub Setup (SSH)

This document logs the process of initializing the vault as a Git repository and connecting it to GitHub using SSH for secure, passwordless updates.

## 1. Initializing Local Git
To start tracking changes in the vault:
```bash
git init
git add .
git commit -m "Initial commit: Vault structure and learning roadmap"
```

## 2. Generating SSH Keys
To connect to GitHub securely without entering a password every time:
1. **Generate the key**:
   ```bash
   ssh-keygen -t ed25519 -C "your_email@example.com"
   ```
   *(Pressed Enter to accept default location and skipped passphrase for ease of use in this setup).*

2. **Start the ssh-agent**:
   ```bash
   eval "$(ssh-agent -s)"
   ```

3. **Add key to agent**:
   ```bash
   ssh-add ~/.ssh/id_ed25519
   ```

## 3. Adding Key to GitHub
1. **Copy the public key**:
   ```bash
   cat ~/.ssh/id_ed25519.pub
   ```
2. **On GitHub**: Go to **Settings > SSH and GPG keys > New SSH key** and paste the content.
3. **Test Connection**:
   ```bash
   ssh -T git@github.com
   ```

## 4. Connecting to GitHub
Created a new repository on GitHub and linked it:
```bash
git remote add origin git@github.com:your-username/your-repo-name.git
git branch -M master
git push -u origin master
```

## 5. Ongoing Workflow (Updating GitHub)
To keep the "second brain" synced:
1. **Check status**: `git status`
2. **Stage changes**: `git add .`
3. **Commit**: `git commit -m "Daily update: [Topic]"`
4. **Push**: `git push`

---
*Note: Ensure `.gitignore` is set up to exclude `.obsidian/workspace.json` and other transient files to avoid merge conflicts.*
