# 📚 TERMINAL MASTERY GUIDE

*Learn tmux, bash shortcuts, and productivity tricks*

---

## 🎯 TMUX - Terminal Multiplexer

### Why Tmux?
- **Multiple windows** in one terminal
- **Sessions** persist even if ssh disconnects
- **Split panes** - work on multiple things at once

### Basic Commands

| Command | Action |
|---------|--------|
| `tmux` | Start new session |
| `tmux new -s NAME` | Start named session |
| `tmux ls` | List sessions |
| `tmux attach -t NAME` | Attach to session |
| `tmux kill-session -t NAME` | Kill session |

### Keybindings (Prefix: Ctrl+b)

| Shortcut | Action |
|----------|--------|
| `Ctrl+b d` | Detach from session |
| `Ctrl+b %` | Split vertically |
| `Ctrl+b "` | Split horizontally |
| `Ctrl+b o` | Switch pane |
| `Ctrl+b x` | Close pane |
| `Ctrl+b c` | New window |
| `Ctrl+b n` | Next window |
| `Ctrl+b p` | Previous window |
| `Ctrl+b [` | Scroll mode (q to exit) |

### Advanced Tmux

```bash
# .tmux.conf basics
set -g mouse on                    # Enable mouse
set -g status-position top         # Status bar at top
bind -r j select-pane -D            # Cycle panes with j
bind -r k select-pane -U            # Cycle panes with k
```

---

## 🎯 BASH PRODUCTIVITY

### Essential Shortcuts

| Shortcut | Action |
|----------|--------|
| `Ctrl+a` | Go to beginning of line |
| `Ctrl+e` | Go to end of line |
| `Ctrl+u` | Clear line before cursor |
| `Ctrl+k` | Clear line after cursor |
| `Ctrl+w` | Delete word before |
| `Ctrl+r` | Search history ⭐ |
| `Ctrl+l` | Clear screen |
| `Ctrl+c` | Cancel command |
| `Ctrl+z` | Background process |

### History Tricks

```bash
# Search history
 Ctrl+r then type...

# Repeat last command
!!

# Repeat last command starting with "git"
!git

# Last argument of previous command
ls /long/path/to/file
cd !$

# First argument of previous command
!(command) ^

# Run previous command in background
command &
fg  # bring back
```

### Aliases (Add to ~/.bashrc)

```bash
# Shortcuts
alias ll='ls -la'
alias la='ls -a'
alias l='ls -l'
alias ..='cd ..'
alias ...='cd ../..'

# Git shortcuts
alias gs='git status'
alias ga='git add'
alias gc='git commit'
alias gp='git push'
alias gd='git diff'

# Agent shortcuts
alias pi='pi'
alias goose='goose run -t'
```

---

## 🎯 FIND & GREP

### Find Files

```bash
# Find by name
find . -name "*.txt"
find . -name "*.md"

# Find by type
find . -type d          # Directories
find . -type f          # Files

# Find by size
find . -size +10M       # Larger than 10MB

# Find and delete
find . -name "*.tmp" -delete
```

### Grep Search

```bash
# Basic search
grep "word" file.txt

# Case insensitive
grep -i "word" file.txt

# Recursive (search in folders)
grep -r "word" .

# Show line numbers
grep -n "word" file.txt

# Count matches
grep -c "word" file.txt

# Invert (show non-matches)
grep -v "word" file.txt

# Regex
grep -E "^regex" file.txt
```

---

## 🎯 PIPES & CHAINING

```bash
# Chain commands
cmd1 | cmd2 | cmd3

# Run in background
command &

# Run after previous finishes
cmd1 && cmd2

# Run if previous fails
cmd1 || cmd2

# Redirect output
command > file.txt     # overwrite
command >> file.txt    # append
command 2> errors.txt # errors only
command &> all.txt     # both
```

---

## 📝 PRACTICE EXERCISES

### Day 1: Tmux
1. Start tmux session
2. Split into 2 panes
3. Run different commands in each
4. Detach and reattach

### Day 2: Bash
1. Set up .bashrc with aliases
2. Master Ctrl+r history search
3. Practice !! and !$ 

### Day 3: Find & Grep
1. Search your vault for a word
2. Find all .md files
3. Count lines in files

---

*Reference: [[ROADMAP]] Day 4-10 supplement*