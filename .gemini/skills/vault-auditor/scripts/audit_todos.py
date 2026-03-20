import os
import re
from datetime import datetime

# Path Configuration
DAILY_LOGS_DIR = "00_daily_logs"
LOG_DATE_FORMAT = "%d-%m-%Y"  # DD-MM-YYYY as per the user's files

def get_today_log_path():
    """Gets the path to today's log file."""
    today_str = datetime.now().strftime(LOG_DATE_FORMAT)
    return os.path.join(DAILY_LOGS_DIR, f"{today_str}.md")

def audit_todos(file_path):
    """Parses the To Do section of the daily log."""
    if not os.path.exists(file_path):
        print(f"Audit failed: Log file for today ({os.path.basename(file_path)}) not found.")
        return

    with open(file_path, 'r') as f:
        content = f.read()

    # Find the To Do section
    # Regex searches for '## To Do' and captures everything until the next header or end of file
    match = re.search(r'## To Do(.*?)(?=\n##|$)', content, re.DOTALL)
    if not match:
        print("Audit failed: '## To Do' section not found in today's log.")
        return

    todo_content = match.group(1).strip()
    lines = todo_content.split('\n')

    pending = []
    completed = []

    for line in lines:
        line = line.strip()
        if not line:
            continue
        
        # Check for task patterns
        if line.startswith("- [ ]"):
            pending.append(line.replace("- [ ]", "").strip())
        elif line.startswith("- [x]"):
            completed.append(line.replace("- [x]", "").strip())

    # Output the audit report
    print(f"--- Daily Audit for {os.path.basename(file_path)} ---")
    if not pending and not completed:
        print("No tasks found in the To Do section.")
    else:
        print(f"Completed: {len(completed)}")
        for task in completed:
            print(f"  [x] {task}")
        
        print(f"Pending: {len(pending)}")
        for task in pending:
            print(f"  [ ] {task}")

    if not pending and (completed or lines):
        print("\nGreat job! All tasks for today are completed.")
    elif pending:
        print(f"\nYou still have {len(pending)} pending tasks for today.")

if __name__ == "__main__":
    today_log = get_today_log_path()
    audit_todos(today_log)
