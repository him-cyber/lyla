import os
from openai import OpenAI
from datetime import datetime
import tempfile
import subprocess
from elevenlabs.client import ElevenLabs
from core.memory.memory_router import save_log, log_debug_summary
from core.memory.utils import fill_defaults, get_voice_id, set_cached_voice

# === CONFIG ===
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
VOICE_ID = get_voice_id()
CONTEXT_FILE = "lyla_context.json"

# === SETUP ELEVEN CLIENT ===
eleven_client = ElevenLabs(api_key=os.getenv("ELEVEN_API_KEY"))

# === CHOOSE LYLA'S VOICE ===
def choose_voice():
    available_voices = eleven_client.voices.get_all()
    print("\n🎤 Available Voices:")
    for i, v in enumerate(available_voices.voices):
        print(f"{i+1}. {v.name} ({v.voice_id})")

    use_previous = input("\nUse your last chosen voice? (Y/n): ").strip().lower()
    if use_previous in ["", "y", "yes"]:
        return VOICE_ID

    try:
        choice = int(input("\nChoose a voice (number): ")) - 1
        selected = available_voices.voices[choice].voice_id
        set_cached_voice(selected)
        return selected
    except (IndexError, ValueError):
        print("❌ Invalid choice. Using default voice.")
        return VOICE_ID  # fallback

# === HELPERS ===
def speak(text, voice_id=VOICE_ID):
    try:
        audio_stream = eleven_client.generate(
            text=text,
            voice=voice_id,
            model="eleven_monolingual_v1"
        )
        with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as temp_audio:
            for chunk in audio_stream:
                temp_audio.write(chunk)
            temp_audio_path = temp_audio.name

        subprocess.run(["mpg123", temp_audio_path])
    except Exception as e:
        print("🎵 Failed to play audio:", e)


def generate_response(user_input, context):
    system_msg = "You are Lyla, a soulful, emotionally intelligent AI companion. Generate a short, warm response."
    prompt = f"Context: {context}\nInput: {user_input}"

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": system_msg},
            {"role": "user", "content": prompt}
        ]
    )
    reply = response.choices[0].message.content.strip()
    return reply

HELP_MSG = """
🧠 Lyla CLI — Your soulful AI companion

Usage:
  python3 lyla.py "your message here"

Examples:
  python3 lyla.py "I’m feeling a little overwhelmed today"
  python3 lyla.py "give me a simple chicken stir fry recipe"
  python3 lyla.py "how do I focus better when studying?"

Environment Variables:
  OPENAI_API_KEY       Your OpenAI API key
  ELEVEN_API_KEY       Your ElevenLabs voice API key
  LYLA_MEMORY_BACKEND  'mongo' or 'json'

Optional:
  --help, -h           Show this help message

💜 Built for human moments.
"""

# === RUN ===
def main():
    import json
    import sys

    if len(sys.argv) < 2 or sys.argv[1] in ["--help", "-h"]:
        print(HELP_MSG)
        return

    if os.path.exists(CONTEXT_FILE):
        with open(CONTEXT_FILE, "r") as f:
            context = json.load(f)
    else:
        context = {}

    voice_id = choose_voice()
    user_input = sys.argv[1]
    reply = generate_response(user_input, context)

    print("🧠 Lyla:", reply)
    speak(reply, voice_id)

    log = {
        "timestamp": datetime.now().isoformat(),
        "user_input": user_input,
        "lyla_response": reply,
        "context": context
    }
    save_log(log)
    log_debug_summary()

if __name__ == "__main__":
    main()
