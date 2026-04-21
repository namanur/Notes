---
Phase: [[Phase 3 — Operating Systems]]
Project: [[01_Phase_Infrastructure_Shell]]
Prev:  | Next: [[Linux Shell In-Depth]]
---

# Linux Fundamentals

## What Linux Actually Is
Linux is a **kernel**. One program that sits between hardware and everything else. Its job is to manage:
1.  **CPU:** Who gets to use it and when.
2.  **Memory:** Allocation and protection.
3.  **Storage:** Access to the disk.

Every other program (terminal, browser, Python) runs on top and asks the kernel for permission. When using the terminal, you're talking to a **[[Linux Shell In-Depth|shell]]** (like [[Linux Shell In-Depth|bash]]), which is a program that makes requests to the kernel for you.

---

## Core Concept: Everything is a File
In Linux, everything is represented as a file. This includes:
-   **Hardware:** Hard drives, keyboards, USB devices (found in `/dev`).
-   **Processes:** Running programs (found in `/proc`).
-   **Network:** Sockets and connections.

### The Filesystem Tree
Everything starts at `/` (root). There are no separate drive letters (like C: or D:). Everything mounts into this single tree.

| Directory | Purpose |
| :--- | :--- |
| `/home` | User directories (e.g., `/home/naman`). |
| `/etc` | System configuration files (text-based). |
| `/dev` | Hardware devices represented as files. |
| `/proc` | Live process information (virtual filesystem in memory). |
| `/bin`, `/usr/bin` | Essential and user programs. |
| `/var` | Logs and variable data. |
| `/tmp` | Temporary files. |

---

## Permissions
Linux is a **multi-user system**. Every file has:
1.  **Owner**
2.  **Group**
3.  **Everyone Else**

Each group has three permissions: **Read (r)**, **Write (w)**, and **Execute (x)**.

Example: `-rwxr-xr--`
-   `owner`: rwx (Full access)
-   `group`: r-x (Read and Execute)
-   `others`: r-- (Read only)

*Note: Execute permission on a directory is required to `cd` into it.*

---

## The Process Model
Every running program is a **process** with a unique **PID** (Process ID).
-   **PID 1 (systemd):** The first process started by the kernel. Every other process is a child of PID 1.
-   **Process Tree:** Every process has a parent.
-   **`/proc`:** You can see a process's state by reading files in `/proc/[PID]/status`.
-   `$$` in bash gives you the PID of your current shell.

---

## Essential Commands
-   `pwd`: Print working directory.
-   `cd`: Change directory (`.` = current, `..` = parent, `~` = home).
-   `ls`: List contents (`-la` for all details and hidden files).
-   `cat`: Read and print file contents.
-   `echo`: Print text to stdout.
-   `|` (pipe): Send the output of one command as input to another.
