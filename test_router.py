from core.memory import memory_router as memory
from core.memory.utils import fill_defaults # type: ignore

entry = {
    "user_input": "Today feels like a fresh start.",
    "mood": "motivated"
}

final = fill_defaults(entry)
memory.save_log(final)
memory.log_debug_summary()
