# Phase 3: Python Engineering Fundamentals
**Track:** Data & Middleware
**Parent:** [[ROADMAP]]

## 🧠 Mental Model: The Bytecode Interpreter
Python is not "interpreted" line-by-line like a simple shell script. It is compiled into **Bytecode** which runs on the **Python Virtual Machine (PVM)**.

1. **The Compilation Chain:** `.py` (Source) -> Compiler -> `.pyc` (Bytecode in `__pycache__`) -> PVM (Execution).
2. **The GIL (Global Interpreter Lock):** The infamous bottleneck. Only one thread can execute Python bytecode at a time. This makes Python "single-threaded" for CPU-bound tasks, even on multi-core systems. (Solution: `multiprocessing` or `asyncio` for I/O).
3. **Memory Management:** Python uses **Reference Counting** + a **Generational Garbage Collector**. If an object's ref count hits 0, it's deleted instantly.
4. **Namespaces & Scopes (LEGB):** Local -> Enclosing -> Global -> Built-in. Understanding this prevents `UnboundLocalError`.

---

## 💻 Technical Deep Dive: Production-Grade Python
Avoid "scripting" habits. Write "Engineering" Python.

### 1. Introspection (Seeing the Bytecode)
```python
import dis

def add(a, b):
    return a + b

# See exactly what the PVM sees
dis.dis(add)
```

### 2. The Power of `__slots__`
By default, Python stores object attributes in a dictionary (`__dict__`). This is slow and uses lots of RAM.
```python
class EfficientPoint:
    __slots__ = ['x', 'y']  # Prevents __dict__ creation, massive RAM savings
    def __init__(self, x, y):
        self.x = x
        self.y = y
```

### 3. Context Managers (The Right Way)
Never manually call `.close()`. Use the protocol.
```python
from contextlib import contextmanager

@contextmanager
def system_resource():
    print("🔌 Opening Resource")
    try:
        yield "The Resource"
    finally:
        print("🧹 Cleaning Up")

with system_resource() as r:
    print(f"Using {r}")
```

### 4. Modern Type Hinting (MANDATORY)
```python
from typing import List, Optional, Dict

def process_users(user_ids: List[int]) -> Optional[Dict[str, str]]:
    # Use 'mypy' to check these before running
    pass
```

---

## ⚡ Mastery Drills: High-Pain Execution
*Goal: Break the interpreter's magic.*

1. **The Memory Leak:** Create a circular reference (A points to B, B points to A) and observe why reference counting fails to clean them up until the Garbage Collector kicks in.
2. **GIL Benchmarking:** Write a heavy mathematical function. Run it 4 times sequentially. Then run it 4 times using `threading`. Observe that it takes the same amount of time (or more). Finally, run it using `multiprocessing` and see the speedup.
3. **Bytecode Surgery:** Use the `dis` module on a list comprehension vs a `for` loop. Identify which one generates fewer instructions.
4. **Namespace Collision:** Shadow a built-in function (e.g., `list = [1, 2]`) and experience the pain of trying to call `list()` later.

---

## 📜 Execution Contract
- **Timebox:** 3 Hours.
- **Start Command:** `python3 -m py_compile my_script.py`
- **Completion Condition:** Successfully build a script that uses `__slots__`, Type Hinting, and a custom Context Manager, passing a `mypy` strict check.

---
**Links:** [[ROADMAP]] | [[00_daily_logs/AGENT_ACTIVITY]]
