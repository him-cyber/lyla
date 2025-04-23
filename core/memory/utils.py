import os

_cached_voice = None

# === VOICE HANDLING ===
def set_cached_voice(voice_id):
    global _cached_voice
    _cached_voice = voice_id

def get_voice_id():
    global _cached_voice
    return _cached_voice or "21m00Tcm4TlvDq8ikWAM"

# === FILL DEFAULTS ===
def fill_defaults(entry):
    if "mood" not in entry:
        entry["mood"] = "neutral"
    if "tags" not in entry:
        entry["tags"] = []
    if "context" not in entry:
        entry["context"] = {
            "weather": None,
            "last_action": None,
            "role": None,
            "mode": None
        }
    if "metadata" not in entry:
        entry["metadata"] = {
            "vibe_rating": None,
            "session_id": None,
            "user_notes": None,
            "emotion_graph": {}
        }
    return entry
