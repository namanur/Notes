import os
import json
import subprocess
from datetime import datetime

# Configuration
VAULT_ROOT = "/home/naman/Documents/Notes"
DRIVE_NOTES_FOLDER_ID = "1dGSzYsqhsZW-C8amSil5HseJfl-cHOV_"
LOG_FILE = f"{VAULT_ROOT}/00_daily_logs/sync_log.md"

# Directories to ignore
IGNORE_DIRS = {".git", ".obsidian", ".gemini"}

def run_gws_command(cmd_parts):
    """Executes a gws command and returns the JSON output."""
    try:
        result = subprocess.run(
            ["gws"] + cmd_parts,
            capture_output=True,
            text=True,
            check=True
        )
        output = result.stdout
        if "{" in output:
            output = output[output.find("{"):]
        return json.loads(output)
    except Exception as e:
        print(f"Error running gws command {' '.join(cmd_parts)}: {e}")
        return None

def get_drive_items(parent_id):
    """Lists files and folders in a Drive parent directory."""
    query = f"'{parent_id}' in parents and trashed = false"
    params = json.dumps({"q": query, "fields": "files(id, name, mimeType)"})
    result = run_gws_command(["drive", "files", "list", "--params", params])
    if result and "files" in result:
        return {item["name"]: item for item in result["files"]}
    return {}

def sync_vault():
    print(f"--- Starting Vault Sync: {datetime.now()} ---")
    
    # Track folder mappings: local_rel_path -> drive_id
    # Root mapping
    folder_map = {"": DRIVE_NOTES_FOLDER_ID}

    # Walk directories
    for root, dirs, files in os.walk(VAULT_ROOT):
        rel_path = os.path.relpath(root, VAULT_ROOT)
        if rel_path == ".":
            rel_path = ""
        
        # Skip ignored directories early
        parts = rel_path.split(os.sep)
        if any(p in IGNORE_DIRS for p in parts):
            continue

        if rel_path not in folder_map:
            print(f"Skipping {rel_path} (no parent folder ID)")
            continue

        drive_parent_id = folder_map[rel_path]
        print(f"Syncing directory: {rel_path or 'root'} (ID: {drive_parent_id})")

        # Get existing items once per folder
        existing_items = get_drive_items(drive_parent_id)

        # 1. Ensure subdirectories exist on Drive
        for d in sorted(dirs):
            if d in IGNORE_DIRS:
                continue
            
            local_dir_path = os.path.join(root, d)
            rel_dir_path = os.path.relpath(local_dir_path, VAULT_ROOT)
            
            if d in existing_items and existing_items[d]["mimeType"] == "application/vnd.google-apps.folder":
                folder_map[rel_dir_path] = existing_items[d]["id"]
            else:
                # Create the folder
                create_json = json.dumps({
                    "name": d,
                    "mimeType": "application/vnd.google-apps.folder",
                    "parents": [drive_parent_id]
                })
                result = run_gws_command(["drive", "files", "create", "--json", create_json])
                if result and "id" in result:
                    print(f"  [+] Created folder: {d}")
                    folder_map[rel_dir_path] = result["id"]
                else:
                    print(f"  [!] Failed to create folder: {d}")

        # 2. Sync files in this directory
        for f in sorted(files):
            if f.startswith("."):
                continue
            
            local_file_path = os.path.join(root, f)
            
            if f in existing_items:
                file_id = existing_items[f]["id"]
                # For safety and reliability, we'll delete and re-upload
                # This ensures we don't have metadata mismatch or duplicate name issues
                run_gws_command(["drive", "files", "delete", "--params", f'fileId={file_id}'])
                print(f"  [u] Updating: {f}")
            else:
                print(f"  [+] Uploading: {f}")

            # Use the upload command
            run_gws_command(["drive", "+upload", local_file_path, "--parent", drive_parent_id])

    print(f"--- Sync Completed: {datetime.now()} ---")

if __name__ == "__main__":
    sync_vault()
