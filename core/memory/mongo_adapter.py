from pymongo import MongoClient # type: ignore
from datetime import datetime
import os

# === CONFIG ===
MONGO_URI = os.getenv("LYLA_MONGO_URI", "mongodb://localhost:27017")
DB_NAME = "lyla_db"
COLLECTION_NAME = "memory_logs"

# === CONNECTION ===
client = MongoClient(MONGO_URI)
db = client[DB_NAME]
collection = db[COLLECTION_NAME]

# === CORE FUNCTIONS ===

def save_log(entry):
    if "timestamp" not in entry:
        entry["timestamp"] = datetime.utcnow().isoformat()
    result = collection.insert_one(entry)
    return str(result.inserted_id)

MAX_LOG_RETURN = 100

def get_last_n_logs(n=3):
    """
    Securely return the latest `n` memory logs.
    Prevents abuse by enforcing a max cap.
    """
    try:
        n = int(n)
    except ValueError:
        n = 3  # fallback if weird input

    n = max(1, min(n, MAX_LOG_RETURN))  # enforce bounds

    logs = collection.find().sort("timestamp", -1).limit(n)
    return list(logs)


def search_logs_by_tag(tag):
    return list(collection.find({"tags": tag}).sort("timestamp", -1))

def clear_all_logs():
    collection.delete_many({})

def log_debug_summary():
    count = collection.count_documents({})
    last = collection.find_one(sort=[("timestamp", -1)])
    print(f"🧠 Memory count: {count}")
    if last:
        print(f"🕒 Last entry at: {last['timestamp']}")
