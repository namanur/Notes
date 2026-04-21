---
Phase: [[Phase 3]]
Project: [[01_Phase_Infrastructure_Shell]]
Prev: [[Mastering Awk]] | Next: [[Permissions Audit]]
---
# Command Mastery Lab
**Project: Linux System Hardening**

This is a living ledger of commands explored during this curriculum. Mastery comes from understanding the *data flow* each command facilitates.

## 1. The Explorers (System Navigation)
| Command | What it actually does | Key Flag to Practice |
| :--- | :--- | :--- |
| `ls` | Lists directory contents. | `ls -la` (Long format, including hidden files) |
| `pwd` | Prints current working directory. | N/A |
| `cd` | Changes the shell's current location. | `cd -` (Toggle back to previous directory) |
| `find` | Searches for files in a directory hierarchy. | `find . -name "*.md"` (Find all markdown files) |

## 2. The Readers (File Content)
| Command | What it actually does | Key Flag to Practice |
| :--- | :--- | :--- |
| `cat` | Concatenates and displays file content. | `cat -n` (Number the lines) |
| `head` | Outputs the start of a file. | `head -n 20` (See first 20 lines) |
| `tail` | Outputs the end of a file. | `tail -f` (Follow a file in real-time — great for logs) |
| `less` | View file content one page at a time. | `/pattern` (Search for text inside `less`) |

## 3. The Surgeons (Data Manipulation)
| Command | What it actually does | Key Flag to Practice |
| :--- | :--- | :--- |
| `grep` | Filters text using patterns. | `[[Mastering Grep|grep]] -i "text"` (Case-insensitive search) |
| `awk` | Scans and processes columns of data. | `[[Mastering Awk|awk]] '{print $1}'` (Print only the first column) |
| `sed` | Stream editor for finding/replacing text. | `[[Mastering Sed|sed]] 's/old/new/g'` (Global replacement) |
| `sort` | Reorders lines of text. | `sort -n` (Sort numerically instead of alphabetically) |
| `uniq` | Filters out duplicate lines. | `uniq -c` (Count occurrences of each line) |
| `wc` | Word, line, and character count. | `wc -l` (Count only the lines) |

## 4. The Orchestrators (Pipes & Glue)
| Command | What it actually does | Key Flag to Practice |
| :--- | :--- | :--- |
| `xargs` | Converts Stdin into command arguments. | `echo "file.txt" | xargs rm` |
| `tee` | Splits a stream (saves to file AND shows in terminal). | `ls | tee output.txt` |
| `alias` | Creates a shortcut for a command. | `alias gs='git status'` |

---

## 🛠 Practice Lab: Try These Challenges
*Run these in your terminal to see the "Unix Philosophy" in action:*

1. **The Error Hunter:**
   Find all "404" errors in a mock log and count them:
   `cat access.log | [[Mastering Grep|grep]] "404" | wc -l`

2. **The Clean Sweep:**
   Find every markdown file in your vault and count the total lines of knowledge:
   `find . -name "*.md" | xargs wc -l`

3. **The Duplicate Detector:**
   Sort a list of names and see which ones appear most often:
   `sort names.txt | uniq -c | sort -nr`

4. **The Safe Write:**
   List your files, see them in the terminal, but also save them to a file:
   `ls -la | tee my_files.txt`

## Claude Architect Note
In autonomous systems, we prefer `find ... -print0 | xargs -0 ...` to handle filenames with spaces safely. Always aim for **idempotency**: commands that can be run multiple times without breaking the system.
