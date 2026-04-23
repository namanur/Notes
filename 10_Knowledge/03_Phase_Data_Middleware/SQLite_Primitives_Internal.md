# Phase 3: SQLite Primitives & Internals
**Track:** Data & Middleware
**Parent:** [[ROADMAP]]

## 🧠 Mental Model: The B-Tree Pager
SQLite is not a "server." It is a library that manages a single cross-platform file. Its "engine" is a B-Tree implementation that treats your disk as a collection of fixed-size pages.

1. **The Pager Layer:** This is the heart. It reads/writes chunks (usually 4KB) from disk. It manages the **Page Cache** (RAM) to avoid disk I/O.
2. **B-Trees:** Tables are "Table B-Trees" (Key=RowID, Data=Columns). Indices are "Index B-Trees" (Key=Columns, Data=RowID).
3. **Journaling (The Safety Net):**
    - **Rollback Journal:** The old way. It copies original pages to a `.journal` file *before* modifying the main DB. Slow because it locks the whole file.
    - **WAL (Write-Ahead Log):** The modern way. Changes are appended to a `.wal` file. Readers can read the main DB while writers append to the WAL. This enables high concurrency.
4. **Manifest/Header:** The first 100 bytes of a SQLite file contain the "Magic String" (`SQLite format 3`) and critical metadata like page size and file format versions.

---

## 💻 Technical Deep Dive: CLI Mastery & Optimization
Stop using GUI browsers. The `sqlite3` CLI is the only way to understand the state.

### 1. The WAL Switch
```sql
-- Check current journaling mode
PRAGMA journal_mode;

-- Enable WAL (Write-Ahead Logging) - MANDATORY for production/agentic use
PRAGMA journal_mode=WAL;

-- Synchronous levels (off, normal, full, extra)
-- 'Normal' is often the sweet spot for WAL mode
PRAGMA synchronous=NORMAL;
```

### 2. Schema Inspection & Internal Tables
```sql
-- List all tables and their SQL definitions
.schema

-- See the master catalog table
SELECT * FROM sqlite_master;

-- Check page statistics (requires looking at internals)
.stats on
SELECT * FROM table_name;
```

### 3. Vacuum and Auto-cleanup
SQLite doesn't reclaim space automatically when you delete rows; it just marks pages as "free."
```sql
-- Rebuild the database file to reclaim space and defragment
VACUUM;

-- Check for corruption
PRAGMA integrity_check;
```

---

## ⚡ Mastery Drills: High-Pain Execution
*Goal: Understand the "In-Process" limitations.*

1. **The WAL Lockout:** Open two terminal sessions. In Session A, start a long-running transaction (`BEGIN; UPDATE...`). In Session B, try to `DROP TABLE`. Observe the `database is locked` error. Now, switch to WAL mode and see how `SELECT` still works in Session B while Session A is writing.
2. **Hex Header Hack:** Use `xxd` or a hex editor to read the first 100 bytes of a `.db` file. Identify the page size (bytes 16-17).
3. **The Index Paradox:** Create a table with 500k rows. Search for a string without an index. Time it. Add an index. Time it again. Check the file size increase.
4. **Atomic Failure:** Write a script that crashes midway through a transaction. Verify that the database remains in its pre-transaction state (Atomicity).

---

## 📜 Execution Contract
- **Timebox:** 2 Hours.
- **Start Command:** `sqlite3 internal_test.db`
- **Completion Condition:** Successfully migrate a database from `DELETE` mode to `WAL` mode and prove concurrent read/write via two separate shell sessions.

---
**Links:** [[ROADMAP]] | [[00_daily_logs/AGENT_ACTIVITY]]
