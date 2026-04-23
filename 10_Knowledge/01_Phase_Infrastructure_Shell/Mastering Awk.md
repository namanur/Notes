---
Phase: [[Phase 3]]
Project: [[01_Phase_Infrastructure_Shell]]
Prev: [[Mastering Sed]] | Next: [[Command Mastery Lab]]
---
# Mastering Awk
**Project: Linux System Hardening**

`awk` is not just a command; it is a **programming language** designed for processing **structured data** (columns). Its first principle is "Report and Calculate."

## First Principles: Fields and Records
Awk sees a file as a collection of **records** (lines) and **fields** (columns).
- `$0`: The entire line.
- `$1, $2, $3...`: The first, second, third columns.
- `NR`: Number of Records (the current line number).
- `NF`: Number of Fields (how many columns in this line).

## The Mastery Kit: The Pattern-Action Block
`awk 'pattern { action }'`
If the pattern matches, the action is executed.

| Example | What it does |
| :--- | :--- |
| `awk '{print $1}'` | Print only the first column. |
| `awk '/Error/ {print $3}'`| Find lines with "Error", print the 3rd column. |
| `awk -F"," '{print $1}'` | Use a comma (`,`) as the delimiter instead of space. |

## Practical Patterns (Recipes)

### 1. Extracting Data from Logs
Get the IP address (usually column 1) from an access log:
```bash
awk '{print $1}' access.log | sort | uniq -c
```

### 2. Basic Arithmetic (Summing Columns)
Sum the total of the second column:
```bash
awk '{sum += $2} END {print "Total:", sum}' expenses.txt
```

### 3. Conditional Filtering
Print lines where the 3rd column is greater than 100:
```bash
awk '$3 > 100' data.txt
```

### 4. Professional Formatting
Use `printf` to align your output:
```bash
awk '{printf "%-10s | %s\n", $1, $2}' data.txt
```

## Claude Architect Context
Awk is the best tool for **data extraction from JSON or CSV** when more complex logic is needed than simple [[Mastering Grep|grep]]. It is the bridge between a simple shell command and a full Python script.
