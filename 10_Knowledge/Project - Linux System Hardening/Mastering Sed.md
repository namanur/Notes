# Mastering Sed
**Project: Linux System Hardening**

`sed` (Stream Editor) is a **non-interactive text editor**. Its first principle is "Transform and Edit."

## First Principles: The Buffer Model
Sed reads a line into a "pattern space," applies your commands to that space, and then prints the result. It is a "one-pass" editor, making it incredibly fast for large files.

## The Mastery Kit: The `s` Command
The most common use of sed is substitution: `s/pattern/replacement/flags`.

| Command | Effect |
| :--- | :--- |
| `s/old/new/` | Replace first occurrence on each line. |
| `s/old/new/g`| Replace **every** occurrence (Global). |
| `s/old/new/p`| Only print lines where a replacement happened. |
| `d` | **Delete** the matching line. |

## Practical Patterns (Recipes)

### 1. The Global Search and Replace
Change "Phase" to "Project" in a file:
```bash
sed 's/Phase/Project/g' Topics.md
```

### 2. In-Place Editing (Saving changes)
Use `-i` to save changes directly to the file. **Warning:** Always test without `-i` first!
```bash
sed -i 's/todo/DONE/g' daily_log.md
```

### 3. Deleting Junk Lines
Remove all lines containing "TEMP" from a file:
```bash
sed '/TEMP/d' data.txt
```

### 4. The Delimiter Trick
If you are editing file paths, don't use `/`. Use `|` or `:` instead:
```bash
sed 's|/usr/local/bin|/usr/bin|g' script.sh
```

## Claude Architect Context
Sed is excellent for **automated configuration**. For example, changing a setting in a `.conf` file without opening it:
`sed -i 's/ENABLED=false/ENABLED=true/g' settings.conf`
