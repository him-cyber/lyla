from core.memory import mongo_adapter as memory

memory.save_log({
    "user_input": "I'm feeling spaced out today.",
    "lyla_response": "That’s okay. Let’s anchor ourselves.",
    "mood": "spaced out",
    "tags": ["mood:drift", "reflective"],
    "context": {
        "last_action": "stared at the ceiling",
        "weather": "cloudy evening"
    }
})

memory.log_debug_summary()
