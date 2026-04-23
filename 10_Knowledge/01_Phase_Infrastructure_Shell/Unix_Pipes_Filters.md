# Phase 1 — Infrastructure & Shell Primitives (Day 3)
## Topic: Unix Pipes & Filters (The Modular Mindset)

### 🧠 Mental Model (Brutal)
Pipes are **kernel-managed buffers** that connect the `stdout` of one process directly to the `stdin` of another.
- **The Unix Philosophy:** Write programs that do one thing and do it well. Write programs to work together. Write programs to handle text streams, because that is a universal interface.
- **Producer-Consumer:** The first command (producer) fills a 64KB kernel buffer. If it's full, the producer blocks. The second command (consumer) reads from it. If it's empty, the consumer blocks.
- **Modular Power:** Complex problems are solved by chaining simple tools.

### 🛠 Technical Deep Dive
- `|`: The pipe operator.
- `grep`: The filter. Use `-v` to invert, `-E` for regex, `-r` for recursive.
- `sort`: Order your data. Use `-n` for numeric, `-u` for unique.
- `uniq -c`: Count occurrences of adjacent identical lines (always sort first!).
- `xargs`: Convert stdin into command-line arguments for the next command. Use `-I{}` for placeholders.
- `awk '{print $1}'`: Extract specific columns from text streams.

### ⚡ Mastery Drills (High Pain)
1. **The Log Cruncher:** Find the top 5 most frequent IP addresses in a log file using `grep`, `sort`, `uniq`, and `head`.
2. **Batch Renaming:** Use `find` and `xargs` to add the prefix `OLD_` to every `.txt` file in a directory.
3. **The Process Sniper:** Use `ps aux`, `grep`, `awk`, and `xargs kill` to find and kill a specific process by name (Careful!).

### 📝 Execution Contract
- **Timebox:** 90 Minutes.
- **Start Command:** `cat /etc/passwd | cut -d: -f1 | sort`
- **Completion Condition:** Construct a one-liner that finds all files larger than 1MB in `/var/log`, sorts them by size, and saves the list to `large_logs.txt`.

---
**Links:**
- 
- [[Pipes and Filters]]
