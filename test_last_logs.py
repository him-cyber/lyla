from core.memory import memory_router as memory
from core.memory.utils import fill_defaults

# Save a few entries (optional if you already have some)
for i in range(5):
    entry = {
        "user_input": f"Test message {i}",
        "tags": ["test"]
    }
    memory.save_log(fill_defaults(entry))

# Test: requesting normal and oversized values
print("🧪 Getting last 3 logs:")
for log in memory.get_last_n_logs(3):
    print(log["user_input"])

print("\n🧪 Getting last 999 logs (should cap at 100):")
logs = memory.get_last_n_logs(999)
print(f"Returned {len(logs)} logs (capped).")
