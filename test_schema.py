from core.memory.utils import fill_defaults # type: ignore

log_data = {
    "user_input": "I'm all over the place today.",
    "mood": "scattered"
}

final = fill_defaults(log_data)
print(final)
