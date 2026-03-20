# Pipes and Filters

## First Principles (How/Why)
The **Unix Philosophy** is built on the idea that complexity should be managed by combining simple, modular tools rather than building massive, monolithic programs.

As Douglas McIlroy, the inventor of the Unix pipe, famously put it:
1.  **Write programs that do one thing and do it well.**
2.  **Write programs to work together.**
3.  **Write programs to handle text streams, because that is a universal interface.**

The **Pipe (`|`)** is the "glue" that makes this possible. It connects the `stdout` (Output) of one program directly into the `stdin` (Input) of another. This allows you to build sophisticated data pipelines on the fly.

---

## Technical Breakdown (The Details)

### The "Lego" Blocks (Core Filters)
A "filter" is a program that reads from `stdin`, performs a transformation, and writes to `stdout`.

| Tool | Role | Common Use Case |
| :--- | :--- | :--- |
| **`grep`** | The **Searcher** | `grep "error"` - Find lines containing a specific pattern. |
| **`sort`** | The **Organizer** | `sort -n` - Sort lines alphabetically or numerically. |
| **`uniq`** | The **Deduplicator** | `uniq -c` - Remove duplicates and count occurrences. |
| **`wc`** | The **Measurer** | `wc -l` - Count the total number of lines in a stream. |
| **`head` / `tail`** | The **Slicers** | `head -n 5` - Pass through only the top or bottom of a stream. |

### Chaining (The Pipeline)
You can chain as many tools as needed:
`Command A | Command B | Command C | Command D`

---

## Claude Architect Context
In agentic orchestration, pipes and filters are fundamental for:
-   **Tool Output Processing:** When an agent runs a command (like `ls` or `grep`), the output is often too large. Chaining with `head` or `grep` helps keep the context window clean.
-   **Data Extraction:** Chaining tools like `sed` or `awk` to extract structured values from raw logs for the agent to reason about.
-   **Observability:** Using `tail -f` to monitor agent logs in real-time as it works through a multi-step plan.

---

## Practical Implementation (Examples)

### Count Unique Errors in a Log
```bash
# Search for errors, sort them to group duplicates, count them, then sort by frequency
cat system.log | grep "ERROR" | sort | uniq -c | sort -nr
```

### Find the Top 5 Largest Files in a Directory
```bash
# List files with sizes, sort numerically, and take the top 5
du -sh * | sort -h | tail -n 5
```

### Quick Data Cleaning
```bash
# Convert a file to lowercase, remove duplicates, and count the total words
cat notes.txt | tr '[:upper:]' '[:lower:]' | sort | uniq | wc -w
```
