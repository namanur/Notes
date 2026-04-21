# Phase 3: Python + SQLite (State Management)
**Track:** Data & Middleware
**Parent:** [[ROADMAP]]

## 🧠 Mental Model: The State Library
When Python talks to SQLite, it isn't "talking to a service." It's a Python process calling a C library that reads a file. 

1. **The Adapter:** `sqlite3` (Standard Lib) is the bridge. It handles type conversion (Python `str` -> SQL `TEXT`).
2. **Concurrency:** In `DELETE` mode, only one writer can exist. In `WAL` mode, writers don't block readers. However, Python's `sqlite3` module has its own transaction handling (`isolation_level`) that can be confusing.
3. **Thread Safety:** By default, a connection object can only be used in the thread that created it (`check_same_thread=True`).
4. **State as Truth:** The DB is the "Gold Source." Python objects should be ephemeral views of that truth.

---

## 💻 Technical Deep Dive: Secure & Atomic State

### 1. The Anti-Injection Pattern (MANDATORY)
Never use f-strings or `.format()` for SQL.
```python
# WRONG (Vulnerable to SQL Injection)
cursor.execute(f"SELECT * FROM users WHERE name = '{user_input}'")

# RIGHT (Parameterized Query)
cursor.execute("SELECT * FROM users WHERE name = ?", (user_input,))
```

### 2. Atomic Transactions with Context Managers
```python
import sqlite3

# Context manager handles COMMIT on success and ROLLBACK on error
with sqlite3.connect("state.db") as conn:
    cursor = conn.cursor()
    cursor.execute("UPDATE account SET balance = balance - 100 WHERE id = 1")
    cursor.execute("UPDATE account SET balance = balance + 100 WHERE id = 2")
```

### 3. Row Factories (Dictionaries vs Tuples)
By default, results are tuples. Switch to `Row` for named access.
```python
conn.row_factory = sqlite3.Row
cursor = conn.cursor()
row = cursor.execute("SELECT * FROM users").fetchone()
print(row['email'])  # Much more readable than row[2]
```

### 4. Custom Adapters
Storing complex types (like `datetime` or `json`) requires registration.
```python
import json

sqlite3.register_adapter(dict, json.dumps)
sqlite3.register_converter("JSON", json.loads)

# Now you can insert a dict directly into a column defined as JSON
```

---

## ⚡ Mastery Drills: High-Pain Execution
*Goal: Manage complex state without corruption.*

1. **The Race Condition:** Write two Python scripts that try to increment the same counter in a database 1000 times simultaneously. Watch the counter fail to reach 2000 unless you use proper locking or transactions.
2. **The JSON Store:** Implement a "Document Store" in SQLite where one column is a `TEXT` field containing JSON. Write Python functions to update specific keys within that JSON.
3. **The Migration Script:** Write a script that detects the current schema version and applies "Upgrades" (e.g., adding a column) sequentially.
4. **The WAL Benchmark:** Measure the time taken for 1000 individual `INSERT` statements in `DELETE` mode vs `WAL` mode.

---

## 📜 Execution Contract
- **Timebox:** 3 Hours.
- **Start Command:** `python3 -c "import sqlite3; print(sqlite3.version)"`
- **Completion Condition:** Successfully build a "State Manager" class that handles connection pooling (manual), parameterized queries, and schema versioning.

---
**Links:** [[ROADMAP]] | [[00_daily_logs/AGENT_ACTIVITY]]
