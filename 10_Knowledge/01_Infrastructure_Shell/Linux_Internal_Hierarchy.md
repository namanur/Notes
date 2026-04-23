# Phase 1 — Infrastructure & Shell Primitives (Day 1)
## Topic: Linux Internal Hierarchy (How Linux Sees the World)

### 🧠 Mental Model (Brutal)
Linux does not "see" files; it sees **inodes**.
- **Everything is a file:** From your SSD to your keyboard and your memory, the kernel abstracts hardware as file entries in the **Virtual File System (VFS)**.
- **Inodes are the source of truth:** An inode is a data structure on the disk that stores everything about a file *except* its name and its actual data. It stores permissions, owner, size, and pointers to data blocks.
- **Directories are just maps:** A directory is a special file containing a list of filenames and their corresponding inode numbers. Moving a file within the same filesystem only updates this map; it doesn't move the data.
- **The Hierarchy (FHS):** `/` is the root. `/etc` is for static config, `/var` for variable data (logs), `/proc` and `/sys` are windows into the kernel's brain (pseudo-filesystems).

### 🛠 Technical Deep Dive
Modern tools to inspect the hierarchy:
- `ls -i`: View the inode number of files.
- `stat <file>`: The ultimate inspection tool for file metadata and inode details.
- `df -i`: Check inode usage. Running out of inodes is as fatal as running out of disk space.
- `findmnt`: View the full mount tree, including VFS and pseudo-filesystems.
- `tree -L 2 /`: Visualize the first two levels of the root hierarchy.

### ⚡ Mastery Drills (High Pain)
1. **The Inode Ghost:** Create a file, note its inode, create a hard link, then delete the original. Observe why the data persists.
2. **The "Full" Empty Disk:** Research how to fill a filesystem's inode table without using more than a few KB of disk space. (Hint: millions of empty files).
3. **The Pseudo-Explorer:** Navigate to `/proc/self` and find the file that represents the command you just ran to get there.

### 📝 Execution Contract
- **Timebox:** 45 Minutes.
- **Start Command:** `ls -R /etc | head -n 20`
- **Completion Condition:** Successfully identify the inode of your current shell's binary without using `which`.

---
**Links:**
- 
- [[Linux Fundamentals]]
