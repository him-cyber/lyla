from core.memory import memory_router as memory
from core.memory.utils import fill_defaults # type: ignore

entry = {
    "user_input": "No internet today, but still logging.",
    "mood": "focused",
    "tags": ["offline", "solo"]
}

final = fill_defaults(entry)
memory.save_log(final)
memory.log_debug_summary()
