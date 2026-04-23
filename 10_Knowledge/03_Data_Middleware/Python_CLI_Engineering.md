# Phase 3: Python CLI Wrappers (argparse/click)
**Track:** Data & Middleware
**Parent:** 

## 🧠 Mental Model: The Command Interface
A CLI tool is a bridge between a human (or agent) and a system. The interface must be **predictable**, **self-documenting**, and **composable**.

1. **Subcommands:** Complex tools should follow the `git <command> <subcommand>` pattern.
2. **Standard Streams:** Success goes to `stdout`, errors/logs go to `stderr`. This is non-negotiable for pipe compatibility.
3. **Exit Codes:** `0` for success, non-zero for failure. This is how scripts (and agents) detect errors.
4. **Shell Completion:** Good CLIs provide completion scripts for Bash/Zsh.

---

## 💻 Technical Deep Dive: `argparse` vs `click`

### 1. `argparse` (The Standard Library)
Robust, no dependencies, but verbose. Good for internal tools where you can't install packages.
```python
import argparse

parser = argparse.ArgumentParser(description="A standard CLI")
subparsers = parser.add_subparsers(dest="command")

# Subcommand: init
init_parser = subparsers.add_parser("init", help="Initialize project")
init_parser.add_argument("--force", action="store_true")

args = parser.parse_args()
```

### 2. `click` (The Modern Professional)
Uses decorators, handles types automatically, and provides excellent subcommand support.
```python
import click

@click.group()
def cli():
    """Master Tool for Systems Engineering"""
    pass

@cli.command()
@click.option('--name', prompt='Project name', help='Name of the project')
@click.argument('path', type=click.Path(exists=False))
def create(name, path):
    click.echo(f"Building {name} at {path}...")

if __name__ == '__main__':
    cli()
```

### 3. Piping and redirection
```python
import sys

# Reading from a pipe (e.g., cat file.txt | python tool.py)
if not sys.stdin.isatty():
    input_data = sys.stdin.read()
```

---

## ⚡ Mastery Drills: High-Pain Execution
*Goal: Build a tool that feels "native".*

1. **The Recursive CLI:** Build a tool with sub-sub-commands (e.g., `tool user permission add`).
2. **The Type Trap:** Use `click.Path` to enforce that an input file MUST exist before the script even starts.
3. **The Hidden Flag:** Implement a `--debug` flag that changes the log level of `stderr` without affecting `stdout`.
4. **The Completion Challenge:** Generate a shell completion script for your `click` tool and source it in your `.bashrc`.

---

## 📜 Execution Contract
- **Timebox:** 2 Hours.
- **Start Command:** `pip install click`
- **Completion Condition:** Successfully build a 3-level subcommand CLI that accepts piped input and returns a non-zero exit code on invalid arguments.

---
**Links:** [[AGENT_ACTIVITY|00_daily_logs/AGENT_ACTIVITY]]
