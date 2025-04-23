import os
import json
from datetime import datetime

DATA_DIR = "lyla_data"
LOG_FILE = os.path.join(DATA_DIR, "memory_logs.json")

# Ensure data folder exists
os.makedirs(DATA_DIR, exist_ok=True)

# === UTILS ===

def _load_logs():
    if not os.path.exists(LOG_FILE):
        return []
    with open(LOG_FILE, "r") as f:
        return json.load(f)

def _save_logs(logs):
    with open(LOG_FILE, "w") as f:
        json.dump(logs, f, indent=2)

# === PUBLIC INTERFACE ===

def save_log(entry):
    logs = _load_logs()
    if "timestamp" not in entry:
        entry["timestamp"] = datetime.utcnow().isoformat()
    logs.append(entry)
    _save_logs(logs)
    return len(logs)

MAX_LOG_RETURN = 100

def get_last_n_logs(n=3):
    n = min(n, MAX_LOG_RETURN)
    logs = _load_logs()
    return logs[-n:]

def search_logs_by_tag(tag):
    logs = _load_logs()
    return [log for log in logs if tag in log.get("tags", [])]

def clear_all_logs():
    _save_logs([])

def log_debug_summary():
    logs = _load_logs()
    count = len(logs)
    print(f"📁 Local memory count: {count}")
    if count > 0:
        print(f"🕒 Last entry at: {logs[-1]['timestamp']}")
