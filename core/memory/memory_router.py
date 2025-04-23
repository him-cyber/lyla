import os

# Adapter fallback logic
USE_MONGO = os.getenv("LYLA_MEMORY_BACKEND", "mongo") == "mongo"

if USE_MONGO:
    from . import mongo_adapter as adapter
else:
    from . import fallback_json as adapter

# Expose unified interface
save_log = adapter.save_log
get_last_n_logs = adapter.get_last_n_logs
search_logs_by_tag = adapter.search_logs_by_tag
clear_all_logs = adapter.clear_all_logs
log_debug_summary = adapter.log_debug_summary
