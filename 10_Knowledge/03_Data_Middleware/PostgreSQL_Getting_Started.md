# 🚀 POSTGRESQL GETTING STARTED

*Why PostgreSQL? "It can be used for many things!" - From the video*

---

## 🎯 WHY POSTGRESQL?

According to the video, PostgreSQL can be used for:
- **Web Applications** - Primary database for apps
- **Data Warehousing** - Handle massive datasets
- **GIS** - Geographic (maps!) data
- **JSON** - Native JSON support
- **Full-Text Search** - Like search engines
- **Foreign Data Wrappers** - Connect to other databases
- **Replication** - High availability
- **Advanced Indexing** - Blazing fast queries

*It's not just a database - it's a platform!*

---

## 📦 INSTALLATION

### Fedora/RHEL
```bash
sudo dnf install postgresql-server postgresql
sudo systemctl start postgresql
sudo systemctl enable postgresql
```

### Setup initial database
```bash
sudo postgresql-setup --initdb
sudo systemctl restart postgresql
```

---

## 🎯 BASIC POSTGRESQL COMMANDS

### Connect to Database
```bash
# As current user
psql

# As specific user
psql -U username -d database

# Connect to specific database
psql -d myapp
```

### Common psql Commands

| Command | Action |
|---------|--------|
| `\l` | List databases |
| `\d` | List tables |
| `\d table` | Describe table |
| `\c dbname` | Connect to database |
| `\q` | Quit |
| `\h` | SQL help |
| `\x` | Expanded display |

### Create Database & Table
```sql
-- Create database
CREATE DATABASE learningDB;

-- Connect to it
\c learningDB

-- Create table
CREATE TABLE progress (
    id SERIAL PRIMARY KEY,
    day INTEGER NOT NULL,
    topic TEXT NOT NULL,
    completed BOOLEAN DEFAULT FALSE,
    notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

### CRUD Operations (Same as SQL Basics!)

```sql
-- INSERT
INSERT INTO progress (day, topic, completed) 
VALUES (4, 'Permissions', TRUE);

-- SELECT
SELECT * FROM progress;

-- UPDATE
UPDATE progress SET notes = 'Mastered chmod!' WHERE day = 4;

-- DELETE
DELETE FROM progress WHERE day = 1;
```

---

## 🔧 ADVANCED POSTGRESQL FEATURES

### JSON Type (Very Powerful!)
```sql
-- Create table with JSON
CREATE TABLE api_data (
    id SERIAL PRIMARY KEY,
    payload JSON
);

-- Insert JSON
INSERT INTO api_data (payload) VALUES 
('{"name": "Naman", "skills": ["AI", "Python"]}');

-- Query JSON
SELECT payload->>'name' FROM api_data;
SELECT payload->'skills' FROM api_data;
```

### Arrays
```sql
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    name TEXT,
    skills TEXT[]
);

INSERT INTO users (name, skills) VALUES 
('Naman', ARRAY['bash', 'python', 'sql']);
```

### Full-Text Search
```sql
-- Add search vector
ALTER TABLE progress ADD COLUMN search_vector tsvector;

-- Populate it
UPDATE progress SET search_vector = 
to_tsvector('english', topic || ' ' COALESCE(notes, ''));

-- Search
SELECT * FROM progress 
WHERE search_vector @@ to_tsquery('permissions');
```

---

## 🐘 USING POSTGRESQL WITH PYTHON

### Install Driver
```bash
pip install psycopg2-binary
```

### Connect with Python
```python
import psycopg2

conn = psycopg2.connect(
    host="localhost",
    database="learningDB",
    user="youruser",
    password="yourpass"
)

# Create cursor
cursor = conn.cursor()

# Execute query
cursor.execute("SELECT * FROM progress")

# Fetch results
for row in cursor.fetchall():
    print(row)

# Close
cursor.close()
conn.close()
```

---

## 📊 POSTGRESQL vs SQLITE

| Feature | SQLite | PostgreSQL |
|---------|--------|------------|
| **Setup** | Just a file | Server daemon |
| **Users** | No | Yes (authentication) |
| **JSON** | Limited | Full support |
| **Arrays** | No | Yes |
| **Full-text search** | Limited | Advanced |
| **Concurrency** | Locks file | Full ACID |
| **Scale** | Single user | Millions of users |

---

## 🎯 YOUR FIRST PROJECT WITH POSTGRESQL

### Build a Learning Tracker

```sql
-- Create database
CREATE DATABASE learning_tracker;

-- Connect
\c learning_tracker

-- Create tables
CREATE TABLE days (
    day_num INTEGER PRIMARY KEY,
    topic TEXT NOT NULL,
    status TEXT DEFAULT 'pending',
    notes TEXT
);

CREATE TABLE projects (
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL,
    status TEXT DEFAULT 'in_progress',
    completed_at DATE
);

-- Insert some data
INSERT INTO days (day_num, topic, status) VALUES 
(4, 'Permissions', 'in_progress'),
(5, 'Shell Scripting', 'pending'),
(6, 'Sed/Awk', 'pending');

-- Query
SELECT * FROM days WHERE status = 'in_progress';
```

---

## 📚 NEXT STEPS

1. **Install PostgreSQL** on your system
2. **Practice** basic commands in psql
3. **Build** your learning tracker database
4. **Connect** it to your MCP server (Day 26!)
5. **Scale up** when you build client projects

---

*Reference:  Day 20c-21*
*Based on: https://www.youtube.com/watch?v=3JW732GrMdg*