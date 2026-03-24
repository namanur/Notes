# Mastering Grep
**Project: Linux System Hardening**

`grep` (Global Regular Expression Print) is the primary tool for **pattern matching**. Its first principle is "Search and Extract."

## First Principles: How Grep Sees Text
Grep processes text **line-by-line**. It doesn't care about columns or structures; it only cares if a specific pattern of characters exists within a sequence of bytes.

## The Mastery Kit: Common Flags
| Flag | Name | Why use it? |
| :--- | :--- | :--- |
| `-i` | Ignore Case | Search for "Error" and catch "error", "ERROR", etc. |
| `-r` | Recursive | Search through an entire directory tree (your whole vault). |
| `-v` | Invert | Show everything *except* the pattern (great for filtering logs). |
| `-n` | Line Number | Tells you exactly where the match is. |
| `-E` | Extended Regex | Supports complex logic like `(this|that)` or `[0-9]+`. |
| `-c` | Count | Just give me the number of matches, not the text. |
| `-C 2`| Context | Show 2 lines before and 2 lines after the match. |

## Practical Patterns (Recipes)

### 1. The Multi-Search (OR Logic)
Search for multiple terms at once:
```bash
grep -E "Failed|Error|Critical" /var/log/syslog
```

### 2. The Exclusion Filter
Show all active config lines (remove comments and empty lines):
```bash
grep -vE "^#|^$" config.conf
```
*Note: `^#` means starts with #, `^$` means empty line.*

### 3. Finding Files, Not Lines
Find every file in your vault that mentions "Claude":
```bash
grep -rl "Claude" .
```

## Claude Architect Context
In automated systems, use `grep -q` (quiet mode). It returns an **exit code** (0 if found, 1 if not) without printing anything. This is perfect for `if` statements in scripts.
