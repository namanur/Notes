# Phase 3: PostgreSQL Mastery
**Track:** Data & Middleware
**Parent:** 

## 🧠 Mental Model: The Persistent Truth Engine
PostgreSQL is not a "file saver." It is a complex ACID-compliant state machine that prioritizes data integrity over everything else.

1. **MVCC (Multi-Version Concurrency Control):** Postgres never overwrites data in place. It creates a new version. This is why `VACUUM` exists—to clean up the "dead tuples."
2. **WAL (Write-Ahead Logging):** Every change is written to a log *before* the data file. If the power cuts, the log is the only truth.
3. **The Planner:** When you write SQL, you aren't telling the DB *how* to get data, but *what* you want. The planner uses statistics to decide between Seq Scan, Index Scan, or Bitmap Scan.
4. **JSONB:** Binary JSON. It allows schema-less flexibility with indexed performance.

---

## 💻 Technical Deep Dive: The `psql` Power User
Forget GUI tools. Real power is in the shell.

### 1. Connection and Inspection
```bash
# Connect to a database
psql -U username -d dbname

# Useful Meta-commands inside psql:
# \dt  -> List tables
# \d+ tablename -> Detailed table schema (including indices)
# \dx  -> List installed extensions (like pg_stat_statements)
# \watch 2 -> Re-run a query every 2 seconds
```

### 2. Performance Autopsy
```sql
-- The most important command for performance
EXPLAIN (ANALYZE, BUFFERS) 
SELECT * FROM users WHERE email = 'test@example.com';

-- Find slow queries (requires pg_stat_statements extension)
SELECT query, calls, total_exec_time 
FROM pg_stat_statements 
ORDER BY total_exec_time DESC LIMIT 10;
```

### 3. JSONB Operations
```sql
-- Querying a JSONB column
SELECT data->>'name' FROM events WHERE data @> '{"type": "signup"}';
```

---

## ⚡ Mastery Drills: High-Pain Execution
*Goal: Understand the cost of abstraction.*

1. **The Index Trap:** Create a table with 1 million rows of random data. Run a SELECT with a WHERE clause on an unindexed column. Record the time. Create a B-Tree index. Run it again. Compare `EXPLAIN ANALYZE` outputs.
2. **The Bloat Simulation:** Perform 10,000 updates on a single row. Check table size using `pg_total_relation_size`. Run `VACUUM FULL` and check size again. Observe the reclaimed space.
3. **The JSONB Challenge:** Insert a complex nested JSON object into a `jsonb` column. Write a query that extracts a value three levels deep and filters by it.
4. **Constraint Conflict:** Try to drop a table that has foreign key dependencies. Solve the error without using `CASCADE` first (find the children).

---

## 📜 Execution Contract
- **Timebox:** 4 Hours.
- **Start Command:** `docker run --name pg-mastery -e POSTGRES_PASSWORD=secret -d postgres`
- **Completion Condition:** Successfully optimize a query from a "Seq Scan" to an "Index Scan" and verify via `EXPLAIN ANALYZE`.

---
**Links:** [[00_daily_logs/AGENT_ACTIVITY]]
