# === Memory Schema Template for Lyla ===

default_memory_entry = {
    "timestamp": None,
    "user_input": "",
    "lyla_response": "",
    "mood": "",
    "tags": [],
    "context": {
        "weather": None,
        "last_action": None,
        "role": None,
        "mode": None
    },
    "metadata": {
        "vibe_rating": None,
        "session_id": None,
        "user_notes": None,
        "emotion_graph": {}
    }
}
