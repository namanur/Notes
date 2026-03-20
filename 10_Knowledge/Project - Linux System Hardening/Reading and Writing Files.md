# Reading and Writing Files

## First Principles (How/Why)
In Linux, the concept of **"Everything is a File"** is powered by **Standard Streams** and **File Descriptors (FDs)**.

When a program (process) runs, it needs to communicate. Instead of talking directly to hardware, the kernel provides three "pipes" or streams by default. These are managed using integer handles called File Descriptors.

| Stream | FD | Default Behavior |
| :--- | :--- | :--- |
| **stdin** (Standard Input) | `0` | Listens for data from the keyboard. |
| **stdout** (Standard Output) | `1` | Sends normal output to the terminal screen. |
| **stderr** (Standard Error) | `2` | Sends error messages to the terminal screen. |

By separating `stdout` and `stderr`, you can log errors to a file while still seeing normal output on your screen.

---

## Technical Breakdown (The Details)

### Redirection Operators
Redirection allows you to change where these streams point:
-   `>` : Redirect `stdout` to a file (overwrites existing content).
-   `>>` : Redirect `stdout` to a file (appends to the end).
-   `2>` : Redirect `stderr` to a file.
-   `<` : Redirect a file's content into `stdin`.

### Essential Commands
1.  **`echo`**: The simplest way to write to `stdout`.
    -   `echo "Hello"` sends "Hello" to stream 1.
2.  **`cat` (Concatenate)**: Primarily used to read files and dump them to `stdout`.
    -   `cat file.txt` reads the file.
    -   `cat > newfile.txt` allows you to type directly into a new file (exit with `Ctrl+D`).
3.  **`head` & `tail`**: Used to "slice" files.
    -   `head -n 5` shows the first 5 lines.
    -   `tail -n 20` shows the last 20 lines.
    -   `tail -f` (Follow) is the industry standard for watching log files update in real-time.
4.  **`less`**: A "pager" program. Unlike `cat`, it doesn't load the whole file into RAM, making it safe for massive (GB+) log files.

---

## Claude Architect Context
As a Claude Architect, understanding streams is vital for:
-   **CLI Integration:** Running `claude -p "prompt"` uses `stdout` for the response, which can be piped to other tools.
-   **Logging:** Capturing `stderr` from your agentic scripts ensures you have a record of tool failures without cluttering the main conversation.
-   **Data Ingestion:** Using `<` to feed large documents into a CLI tool's `stdin`.

---

## Practical Implementation (Examples)

### Create and Append
```bash
echo "Phase 1: Shell Mastery" > roadmap.txt
echo "Day 2: Streams" >> roadmap.txt
```

### Slice and Filter
```bash
# Read the last 50 lines of a log and find a specific error
tail -n 50 /var/log/syslog | grep "error"
```

### The "Cat" Shortcut
```bash
# Quickly create a multi-line file
cat <<EOF > config.json
{
  "name": "Gemini-CLI",
  "version": "1.0"
}
EOF
```
