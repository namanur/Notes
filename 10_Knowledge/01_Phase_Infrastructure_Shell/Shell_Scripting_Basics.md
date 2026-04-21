# Shell Scripting Basics
[[Phase 1]] | [[ROADMAP]]

## 1. The Mental Model
A shell script is a sequence of commands the shell executes as if you typed them, but with **logic (if/then)** and **state (variables)**. 
- **The Shebang (`#!`):** Tells the kernel which interpreter to use. `#!/bin/bash` or `#!/usr/bin/env bash` (preferred for portability).
- **Execution Environment:** Scripts run in a **subshell**. Variables defined in a script do not persist in your main terminal unless you `source` the script.
- **Exit Codes:** Every command returns an integer (0 = Success, 1-255 = Failure). This is the heartbeat of automation.

## 2. Technical Deep Dive
### Essential Primitives
- **Variables:** `NAME="Gemini"` (No spaces around `=`). Access with `$NAME` or `"${NAME}"` (safer).
- **Arguments:** `$1, $2, ...` are the inputs. `$@` is all inputs. `$#` is the count.
- **Conditionals:**
  ```bash
  if [[ -f "$FILE" ]]; then
    echo "File exists"
  fi
  ```
- **The "Safety Header" (MANDATORY):**
  ```bash
  set -euo pipefail
  # -e: Exit on error
  # -u: Error on unset variables
  # -o pipefail: Catch errors in pipes
  ```

### Automated Logging Script
```bash
#!/usr/bin/env bash
set -euo pipefail

LOG_FILE="activity.log"
TIMESTAMP=$(date '+%Y-%m-%d %H:%M:%S')

echo "[$TIMESTAMP] Starting task..." >> "$LOG_FILE"
# Your command here
echo "[$TIMESTAMP] Task complete." >> "$LOG_FILE"
```

## 3. Mastery Drills
### Terminal Challenges
1. **The Argument Counter:** Write a script that accepts any number of arguments and prints: "You provided X arguments. The third one was Y."
2. **The Failure Catcher:** Write a script that attempts to `ls` a non-existent directory. Ensure the script exits immediately with a custom error message using `set -e` and a trap or simple `|| exit 1`.

### Edge Cases
- **Spaces in Filenames:** Always wrap variables in double quotes: `rm "$FILE"`. If you don't, `rm My File.txt` becomes `rm My` and `rm File.txt`.

## 4. Execution Contract
- **Timebox:** 30 minutes
- **Start Command:** `touch log_activity.sh && chmod +x log_activity.sh`
- **Completion Condition:** Create a script that checks if a directory exists; if not, creates it, touches a file inside, and appends the event to a log file with a timestamp.
