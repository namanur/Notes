# Phase 1 — Infrastructure & Shell Primitives (Day 2)
## Topic: File Descriptors & Redirection (The Stream Logic)

### 🧠 Mental Model (Brutal)
Every process is born with three "umbilical cords": **File Descriptors (FD)**.
- **FD 0 (stdin):** The input stream (usually your keyboard).
- **FD 1 (stdout):** The standard output (your screen).
- **FD 2 (stderr):** The standard error (also your screen, but a different lane).
- **The Table:** The kernel maintains an FD table for every process. Redirection is simply the act of pointing these FD numbers to different files or devices instead of the defaults.
- **Everything is a stream:** When you use `>`, you are telling the kernel: "Take the data heading for FD 1 and write it to this file instead."

### 🛠 Technical Deep Dive
- `> file`: Overwrite file with stdout.
- `>> file`: Append stdout to file.
- `2> file`: Redirect stderr only.
- `&> file`: Redirect both stdout and stderr to the same file.
- `/dev/null`: The "black hole". Redirect here to silence a command (`2> /dev/null`).
- `exec 3> myfile`: Open a custom FD (3) and point it to a file for the duration of the shell session.
- `tee`: A "T-junction" for streams. It writes to a file *and* stdout simultaneously.

### ⚡ Mastery Drills (High Pain)
1. **Silent Failure:** Run a command that you know will fail, but redirect stdout to a file and stderr to `/dev/null`. Verify the file is empty and nothing appeared on screen.
2. **Custom FD Logging:** Open FD 5 to a log file, send three different `echo` messages to it using `>&5`, then close it.
3. **The Mirror Loop:** Try to redirect a file's content into itself using `cat file > file`. Observe the result and explain why it wipes the file.

### 📝 Execution Contract
- **Timebox:** 60 Minutes.
- **Start Command:** `ls /nonexistent 2> error.log`
- **Completion Condition:** Create a single command that runs a script, saves its output to `output.log`, saves errors to `error.log`, and still displays the errors on the screen.

---
**Links:**
- 
- Reading and writing files
