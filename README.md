# 💜 Lyla — Soulful AI Companion

Lyla is a CLI-based emotionally intelligent AI companion built with:  
- [OpenAI](https://openai.com/) for soulful natural language conversation  
- [ElevenLabs](https://www.elevenlabs.io/) for voice synthesis  
- MongoDB or JSON for memory persistence

Lyla isn’t just smart — she listens, remembers, and speaks gently, making technology feel human.

---

## ✨ Features
- 🔥 Talk to Lyla via command line
- 💾 Store and recall memory logs (JSON or MongoDB)
- 🎙️ Choose your favorite voice from ElevenLabs
- 🕰️ Logs timestamped interactions for introspection
- 🎯 Custom context-aware responses

---

## 🚀 Quickstart

### 1. Clone the repo
```bash
git clone https://github.com/him-cyber/lyla.git
cd lyla

## 2. Set up environment variables

Create a `.env` file or add the following to your `~/.bashrc` or `~/.zshrc`:

```bash
export OPENAI_API_KEY=your_openai_key
export ELEVEN_API_KEY=your_elevenlabs_key
export LYLA_MEMORY_BACKEND='mongo'  # or 'json'

## 3. Install dependencies

```bash
pip install -r requirements.txt

## 4. Run Lyla

```bash
python3 lyla.py "your message here"

## 💬 Examples

```bash
python3 lyla.py "I’m feeling a little overwhelmed today"
python3 lyla.py "Give me a simple chicken stir fry recipe"
python3 lyla.py "How do I focus better when studying?"

