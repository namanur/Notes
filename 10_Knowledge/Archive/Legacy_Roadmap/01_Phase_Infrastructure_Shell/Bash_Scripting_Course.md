# 📚 BASH SCRIPTING COURSE

*Complete Bash Scripting Guide*

---

## 🎥 Course Video
[The Complete Bash Scripting Course](https://youtu.be/Sx9zG7wa4FA)

---

## 📋 What You'll Learn

### Basic to Advanced:
- [ ] Bash basics & syntax
- [ ] Variables & data types
- [ ] User input
- [ ] Conditionals (if/else)
- [ ] Loops (for, while)
- [ ] Functions
- [ ] Arrays
- [ ] String manipulation
- [ ] File operations
- [ ] Exit codes
- [ ] Debugging

---

## 🎯 Practice Projects (From Course)

| Project | Description | Use Case |
|---------|-------------|----------|
| 1. Hello World | Basic script | Learn syntax |
| 2. Variables | Store data | Input/output |
| 3. Calculator | Math operations | Conditionals |
| 4. File Checker | Check file exists | Conditionals |
| 5. Loop Files | Process many files | Loops |
| 6. Backup Script | Copy files | Automation |
| 7. Menu System | Interactive menu | Functions |
| 8. Log Parser | Analyze logs | Text processing |

---

## 📝 Script Template

```bash
#!/bin/bash
# Script Name
# Description
# Author
# Date

set -e  # Exit on error

# Variables
NAME="Script"
DATE=$(date)

# Functions
function hello() {
    echo "Hello, $1!"
}

# Main
hello "World"

exit 0
```

---

## 🔧 Common Shebangs

```bash
#!/bin/bash    # Most common
#!/usr/bin/env bash  # Portable
#!/bin/sh       # POSIX (more universal)
```

---

## 📚 Related Resources

- [[Terminal_Mastery]] - tmux, shortcuts
- [[ROADMAP]] - Full 40-day plan
- [[01_SQLite_State_Management]] - Day 16

---

*Reference: [[ROADMAP]] Day 5 - Shell Scripting*