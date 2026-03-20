---
name: vault-auditor
description: Audit the vault for daily todos and progress. Use this to check if tasks are completed for the current day.
---

# Vault Auditor

This skill allows the agent to audit the status of tasks in your daily logs. 

## Instructions
- When the user asks to "audit", "check todos", or "see if my list is done", run the `audit_todos.py` script in `./scripts/`.
- Report the results clearly, showing completed and pending tasks.

## Tools
- `python3 ./scripts/audit_todos.py`
