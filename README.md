# Lyla — Soulful AI Companion 💜

Lyla is a voice-powered AI assistant built using OpenAI and ElevenLabs. She responds emotionally and intelligently, logs memory, and adapts to your vibe.

### ✨ Features

- 🎙️ Speaks with realistic AI voice (ElevenLabs)
- 🧠 GPT-4 or GPT-3.5-based emotional replies
- 🪵 Memory logging (MongoDB or JSON fallback)
- 🎭 Remembers your preferred voice

### ⚙️ Setup

```bash
git clone https://github.com/yourusername/lyla.git
cd lyla
pip install -r requirements.txt
Add your keys:

bash
Copy
Edit
export OPENAI_API_KEY=your_key_here
export ELEVEN_API_KEY=your_key_here
💬 Usage# 💜 Lyla — Your Soulful AI Companion

Lyla is a CLI-based emotionally intelligent AI companion built with:
- [OpenAI](https://openai.com/) for soulful natural language conversation
- [ElevenLabs](https://www.elevenlabs.io/) for voice synthesis
- MongoDB or JSON for memory persistence

Lyla isn't just smart — she listens, remembers, and speaks gently, making technology feel human.

---

## 🧠 Features

- 🔥 Talk to Lyla via command line
- 💾 Store and recall memory logs (JSON or MongoDB)
- 🎤 Choose your favorite voice from ElevenLabs
- 📡 Logs timestamped interactions for introspection
- 💬 Custom context-aware responses

---

## 🚀 Quickstart

### 1. Clone the repo

```bash
git clone https://github.com/him-cyber/lyla.git
cd lyla
2. Set up environment variables
Create a .env file or add to your .bashrc / .zshrc:

bash
Copy
Edit
export OPENAI_API_KEY=your_openai_key
export ELEVEN_API_KEY=your_elevenlabs_key
export LYLA_MEMORY_BACKEND=mongo  # or 'json'
🧪 Ensure mpg123 is installed (for Linux audio playback):

bash
Copy
Edit
sudo apt install mpg123
3. Install dependencies
bash
Copy
Edit
pip install -r requirements.txt
💬 Usage
bash
Copy
Edit
python3 lyla.py "your message here"
Examples:
bash
Copy
Edit
python3 lyla.py "I’m feeling a little overwhelmed today"
python3 lyla.py "give me a simple chicken stir fry recipe"
python3 lyla.py "how do I focus better when studying?"
📁 Project Structure
pgsql
Copy
Edit
lyla/
├── core/
│   └── memory/
│       ├── memory_router.py
│       ├── mongo_adapter.py
│       ├── fallback_json.py
│       ├── schemas.py
│       └── utils.py
├── lyla.py
├── lyla_context.json
├── lyla_data/
│   └── memory_logs.json
✨ Inspiration
Lyla was born from the idea that AI should feel soulful — responding not only with facts, but with warmth and presence.

📜 License
MIT – use it freely, remix it with care.

yaml
Copy
Edit

---

Let me know if you want:
- A `requirements.txt` auto-generated
- Badge icons (Python version, license, etc.)
- Demo GIF or CLI session log  
- A one-liner install script

Push this file with:

```bash
git add README.md
git commit -m "Add soulful README for Lyla"
git push
bash
Copy
Edit
python3 lyla.py "your message here"
Crafted with care by Himaneesh Mishra

yaml
Copy
Edit

---

### 4. **Initialize & Push to GitHub**

```bash
git init
git add .
git commit -m "Initial commit: Lyla voice assistant with GPT and ElevenLabs"
git branch -M main
git remote add origin https://github.com/yourusername/lyla.git
git push -u origin main
