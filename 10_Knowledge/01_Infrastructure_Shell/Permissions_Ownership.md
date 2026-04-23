# Permissions and Ownership
Phase Phase 1 | [[Linux Fundamentals]]

## 1. The Mental Model
Permissions are not just "settings"; they are bitmasks (mode bits) stored in the filesystem's inode metadata. 
- **The Triad:** Every file/directory has three scopes: **Owner (u)**, **Group (g)**, and **Others (o)**.
- **The Bits:** Read (4), Write (2), Execute (1). These are added together (7 = 4+2+1).
- **The Directory Trap:** 
  - `x` (Execute) on a directory means "search/traverse". Without it, you cannot `cd` into it, even if you can `ls` it (if `r` is set).
  - `w` (Write) on a directory means "unlink/create". If you have `w` on a directory, you can DELETE a file inside it, even if you don't own the file or have permissions on the file itself.

## 2. Technical Deep Dive
### Modern Primitive: Symbolic vs. Octal
- **Symbolic (Precise):** `chmod u+x,g-w,o=r file`
- **Octal (Bulk):** `chmod 750 dir` (Owner: rwx, Group: rx, Others: none)

### Ownership Transfer
- `chown user:group file`: The atomic way to swap both.
- `chown -R user:group dir`: Recursive (High risk).

### Advanced: Special Bits
- **Setuid (4000):** Executes as the owner (usually root). Dangerous.
- **Setgid (2000):** New files inherit the parent's group. Essential for shared team folders.
- **Sticky Bit (1000):** Only the owner can delete their own files in a shared directory (e.g., `/tmp`).

## 3. Mastery Drills
### Terminal Challenges
1. **The Ghost Directory:** Create a directory `test_dir`. Set permissions so you can `ls` the contents but cannot `cd` into it. Try to `cat` a file inside using the full path.
2. **The Shared Trap:** Create a directory owned by `root`. Give your user `rwx` on the directory. Create a file inside as `root`. Now, delete that file as your user. Explain why it worked.

### Edge Cases
- **Permission Denied despite 777:** Check the parent directory's permissions. If any parent in the path lacks `x`, the 777 file is unreachable.

## 4. Execution Contract
- **Timebox:** 20 minutes
- **Start Command:** `mkdir perm_lab && touch perm_lab/secret.txt && chmod 000 perm_lab/secret.txt`
- **Completion Condition:** Successfully configure a directory where `Group` can read files but only `Owner` can create/delete them, and `Others` are completely locked out.
