# Phase 3: PostgreSQL Basics (Setup & Security)
**Track:** Data & Middleware
**Parent:** [[ROADMAP]]

## 🧠 Mental Model: The Forking Server
Unlike SQLite, PostgreSQL is a client-server database. Every connection to the database forks a new process on the server.

1. **Process Architecture:** A single "Postmaster" process listens for connections. When you connect, it spawns a "Backend" process just for you. This is robust but uses RAM (Connection Pooling is usually needed for scaling).
2. **Cluster vs Database:** A "Cluster" is a collection of databases managed by one Postgres instance.
3. **Roles & Privileges:** Everything is a Role. A "User" is just a Role with LOGIN permission.
4. **Schemas:** A database contains Schemas (namespaces), and Schemas contain Tables. This is the primary way to isolate client data.

---

## 💻 Technical Deep Dive: Lockdown & Access

### 1. `pg_hba.conf` (The Gatekeeper)
This file controls WHO can connect and HOW. It is your first line of defense.
```conf
# TYPE  DATABASE        USER            ADDRESS                 METHOD
local   all             postgres                                peer
host    all             all             127.0.0.1/32            scram-sha-256
host    my_db           app_user        192.168.1.0/24          scram-sha-256
```

### 2. User & Role Management
Never use the `postgres` (superuser) role for your application.
```sql
-- Create a dedicated role
CREATE ROLE app_user WITH LOGIN PASSWORD 'strong_password';

-- Grant access to a database
GRANT CONNECT ON DATABASE my_db TO app_user;

-- Grant schema-level access
GRANT USAGE ON SCHEMA public TO app_user;
GRANT SELECT, INSERT, UPDATE ON ALL TABLES IN SCHEMA public TO app_user;
```

### 3. The `psql` Security Audit
```bash
# List all roles and their attributes
\du

# List database permissions
\l

# List table-level permissions
\z table_name
```

### 4. SSL Enforcement
Force encrypted connections in `postgresql.conf`:
```conf
ssl = on
ssl_cert_file = 'server.crt'
ssl_key_file = 'server.key'
```

---

## ⚡ Mastery Drills: High-Pain Execution
*Goal: Understand the cost of security errors.*

1. **The Lockdown:** Modify `pg_hba.conf` to accidentally lock yourself out of the `postgres` user. Figure out how to fix it (requires local shell access to the server).
2. **Schema Isolation:** Create two schemas (`client_a`, `client_b`). Create a user that can only see and modify tables in `client_a`. Verify they get a `Permission Denied` on `client_b`.
3. **The Role Chain:** Create a `readonly` role. Create a `dev` user and `GRANT readonly TO dev`. Observe how the `dev` user inherits the `SELECT` permissions.
4. **Process Inspection:** Use `ps -ef | grep postgres` to see the individual backend processes for each active connection.

---

## 📜 Execution Contract
- **Timebox:** 2 Hours.
- **Start Command:** `sudo -u postgres psql`
- **Completion Condition:** Successfully create a non-superuser role that can only access one specific schema and verify the restriction via `psql`.

---
**Links:** [[ROADMAP]] | [[00_daily_logs/AGENT_ACTIVITY]]
