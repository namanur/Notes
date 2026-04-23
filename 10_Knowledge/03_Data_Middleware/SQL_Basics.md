# 📚 SQL BASICS - From Zero to Database

*Learn SQL so SQLite & PostgreSQL feel easy*

---

## 🎯 WHAT IS SQL?

**SQL = Structured Query Language**
- Used to talk to databases
- Store, retrieve, update, delete data
- Works for both SQLite (file) and PostgreSQL (server)

---

## 🎯 BASIC CONCEPTS

### Database Structure
```
Database
  └── Table (like Excel sheet)
        └── Rows (individual records)
        └── Columns (data types/fields)
```

### Common Data Types
| Type | Use Case |
|------|----------|
| `INTEGER` | Whole numbers |
| `REAL` | Decimals |
| `TEXT` | Strings/text |
| `BLOB` | Binary (images, files) |
| `DATE` | Dates |
| `BOOLEAN` | True/False |

---

## 🎯 CORE COMMANDS

### 1. SELECT - Read Data

```sql
-- Get all data
SELECT * FROM users;

-- Get specific columns
SELECT name, email FROM users;

-- With conditions
SELECT * FROM users WHERE age > 18;

-- Order results
SELECT * FROM users ORDER BY name ASC;

-- Limit results
SELECT * FROM users LIMIT 10;
```

### 2. INSERT - Add Data

```sql
-- Add one row
INSERT INTO users (name, email, age) 
VALUES ('Naman', 'naman@email.com', 25);

-- Add multiple rows
INSERT INTO users (name, email) VALUES 
('Alice', 'alice@email.com'),
('Bob', 'bob@email.com');
```

### 3. UPDATE - Modify Data

```sql
-- Update one row
UPDATE users 
SET age = 26 
WHERE name = 'Naman';

-- Update multiple
UPDATE users 
SET status = 'active' 
WHERE age > 18;
```

### 4. DELETE - Remove Data

```sql
-- Delete with condition
DELETE FROM users WHERE name = 'Alice';

-- Delete all (careful!)
DELETE FROM users;
```

---

## 🎯 FILTERING & CONDITIONS

```sql
-- WHERE clauses
WHERE age = 25           -- equals
WHERE age > 18           -- greater than
WHERE age < 18           -- less than
WHERE age != 18          -- not equals
WHERE name LIKE 'A%'     -- starts with A
WHERE age IN (18, 21, 25) -- in list
WHERE age BETWEEN 18 AND 25 -- range

-- Multiple conditions
WHERE age > 18 AND status = 'active'
WHERE age < 18 OR role = 'admin'
```

---

## 🎯 TABLE OPERATIONS

```sql
-- Create table
CREATE TABLE users (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    email TEXT UNIQUE,
    age INTEGER,
    created_at DATE DEFAULT CURRENT_DATE
);

-- Add column
ALTER TABLE users ADD COLUMN phone TEXT;

-- Delete table
DROP TABLE users;
```

---

## 🎯 AGGREGATION

```sql
-- Count rows
SELECT COUNT(*) FROM users;

-- Sum values
SELECT SUM(price) FROM orders;

-- Average
SELECT AVG(age) FROM users;

-- Group by
SELECT role, COUNT(*) FROM users GROUP BY role;

-- Having (filter after group)
SELECT role, COUNT(*) as cnt 
FROM users 
GROUP BY role 
HAVING cnt > 1;
```

---

## 🎯 JOINS (Connecting Tables)

```sql
-- INNER JOIN - only matches
SELECT orders.id, users.name 
FROM orders 
INNER JOIN users ON orders.user_id = users.id;

-- LEFT JOIN - all from left table
SELECT * FROM users LEFT JOIN orders ON users.id = orders.user_id;
```

---

## 🆚 SQLITE vs POSTGRESQL

| Feature | SQLite | PostgreSQL |
|---------|--------|------------|
| **Type** | File-based | Server-based |
| **Best for** | Apps, learning | Production, scales |
| **Concurrent** | Limited | Full |
| **Types** | Fewer | Many (JSON, arrays) |
| **Setup** | Easy (just a file) | Need server |

### Same Commands Work In Both!
```sql
-- These work in BOTH SQLite and PostgreSQL
SELECT * FROM table;
INSERT INTO table VALUES (...);
UPDATE table SET ...;
DELETE FROM table WHERE ...;
```

---

## 📝 PRACTICE EXERCISES

### Exercise 1: Create a Tracker
```sql
CREATE TABLE learning_progress (
    id INTEGER PRIMARY KEY,
    day INTEGER,
    topic TEXT,
    completed BOOLEAN DEFAULT FALSE,
    notes TEXT
);
```

### Exercise 2: Add Daily Progress
```sql
INSERT INTO learning_progress (day, topic, completed) 
VALUES (4, 'Permissions', TRUE);

INSERT INTO learning_progress (day, topic, completed) 
VALUES (5, 'Shell Scripting', FALSE);
```

### Exercise 3: Query Progress
```sql
-- Show completed days
SELECT * FROM learning_progress WHERE completed = TRUE;

-- Count completion
SELECT COUNT(*) as completed_days 
FROM learning_progress 
WHERE completed = TRUE;
```

---

## 🚀 NEXT STEPS

1. **Day 20a:** Practice these commands in SQLite
2. **Day 20b:** Create your learning tracker DB
3. **Day 20c:** Install PostgreSQL and try same commands
4. **Day 21:** PostgreSQL-specific features

---

*Reference:  Phase 3 - SQL Track*
*See Also: [[01_SQLite_State_Management]]*