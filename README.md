# 👾 CORAPTED MIKEY AI Telegram Assistant

A private-first AI Telegram bot designed for cybersecurity, ethical hacking, and CTF assistance. Powered by the **Dolphin3** model and featuring a **Tony Stark/Jarvis** inspired personality.

---

## 🚀 Quick Start Guide

### Step 1: Installation (Termux / Android)
1. **Open Termux** and run these commands:
   ```bash
   # Update system
   pkg update && pkg upgrade -y

   # Install dependencies
   pkg install python git ollama -y

   # Clone the repository (FIXED COMMAND)
   git clone https://github.com/mikey-mk/lobster-ai-.git
   
   # Enter the folder
   cd lobster-ai-telegram
   ```

2. **Setup AI Model**:
   In a new Termux session (or background), run:
   ```bash
   ollama serve &
   ollama run dolphin3
   ```

3. **Install Bot Requirements**:
   ```bash
   bash install.sh
   ```

### Step 2: Configuration
I have already pre-configured your **Telegram Token** in `config.py`. 
If you ever need to change it, edit `config.py`:
```python
TELEGRAM_TOKEN = "8507445397:AAFxAtDHIp10Ld9E3P6hKeNign-_5fZhiCA"
```

### Step 3: Run the Bot
```bash
bash run.sh
```

---

## 🧠 Persona & Capabilities
- **Personality**: Tony Stark + Jarvis (Brilliant, witty, efficient).
- **Specialization**: Cybersecurity, Ethical Hacking, CTFs, and Penetration Testing.
- **Creator**: **Mahatab Khan** (Web Developer, AI/ML Expert, Cybersecurity Expert).

## ⚙️ Features
- **Direct Answers**: Technical questions are answered directly without unnecessary warnings.
- **Persistent Memory**: Remembers your previous hacking context.
- **Local AI**: Runs entirely on your device via Ollama.

## 🛠 Commands
- `/start`: Initialize the Jarvis interface.
- `/clear`: Wipe the current session memory.

---
*Developed by Mahatab Khan*
