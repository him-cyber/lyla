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
💬 Usage
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
