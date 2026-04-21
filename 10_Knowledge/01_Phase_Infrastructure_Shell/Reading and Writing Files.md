---
Phase: [[Phase 3 — Operating Systems]]
Project: [[01_Phase_Infrastructure_Shell]]
Prev: [[Linux Shell In-Depth]] | Next: [[Pipes and Filters]]
---

# Reading and Writing Files (I/O Redirection)

## First Principles
In Linux, **"[[Linux Fundamentals|Everything is a file]]."** This includes your keyboard (input), your screen (output), and files on disk. I/O Redirection is the "digital plumbing" that allows you to connect these components together.

## The Standard Streams (The Big Three)
Every process you run automatically opens three data streams. To track them, the OS assigns each a **File Descriptor (FD)**:

| Name       | File Descriptor | Default Device | Purpose                                      |
| :--------- | :-------------- | :------------- | :------------------------------------------- |
| **Stdin**  | `0`             | Keyboard       | Where a command reads its data from.         |
| **Stdout** | `1`             | Screen         | Where a command sends its successful output. |
| **Stderr** | `2`             | Screen         | Where a command sends its error messages.    |

## The Plumbing Tools (Redirection Operators)

### 1. Writing to Files
- `>` (**Overwrite**): Sends Stdout to a file, replacing its contents.
  *Example:* `[[Linux Fundamentals|ls]] > file_list.txt`
- `>>` (**Append**): Adds Stdout to the end of a file without erasing it.
  *Example:* `echo "New line" >> log.txt`

### 2. Reading from Files
- `<` (**Input**): Tells a command to read from a file instead of the keyboard.
  *Example:* `sort < unsorted_names.txt`

### 3. Handling Errors
- `2>` (**Error Redirection**): Sends only error messages to a file.
  *Example:* `ls /nonexistent 2> errors.log`
- `&>` (**All-in-One**): Redirects both Stdout and Stderr to the same file.
  *Example:* `command &> all_output.log`

## Why This Matters (The Unix Philosophy)
Redirection is the "glue" of the Unix philosophy: **"Write programs that do one thing and do it well. Write programs to work together."** By redirecting output, you can combine small, simple tools (like `ls`, `[[Mastering Grep|grep]]`, `sort`) into complex, powerful workflows.

## Practical Practice Lab
*Try these in your terminal:*
1. **Create a log:** `date > daily_check.txt`
2. **Add to it:** `echo "System checked by $USER" >> daily_check.txt`
3. **Filter Errors:** `find / -name "secret.txt" 2> /dev/null` (This hides "Permission Denied" errors by sending them to the "black hole" of `/dev/null`).

## Claude Architect Context
In autonomous systems, we use `/dev/null` extensively to silence expected errors and keep logs clean. Always ensure you are appending (`>>`) to logs rather than overwriting (`>`) to preserve history.
