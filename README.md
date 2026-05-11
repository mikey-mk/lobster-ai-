# 🦞 Lobster AI Telegram Assistant

A private-first AI Telegram bot designed to run locally on your device (PC or Android via Termux). Lobster AI features a playful, slightly sarcastic personality, persistent memory, and support for both local (Ollama) and cloud (OpenAI) AI models.

---

## 🚀 Detailed Setup Guide

### Step 1: Create Your Telegram Bot
1. Open Telegram and search for **@BotFather**.
2. Send the command `/newbot`.
3. Follow the prompts to give your bot a **Name** (e.g., "My Lobster") and a **Username** (e.g., "MyLobster_AI_bot").
4. **IMPORTANT**: BotFather will give you an **API Token**. It looks like `123456789:ABCdefGHIjklMNOpqrSTUvwxYZ`. Copy this token and keep it safe.

### Step 2: Installation

#### 📱 For Android (Termux)
1. **Install Termux**: Download it from [F-Droid](https://f-droid.org/en/packages/com.termux/) (recommended) or GitHub.
2. **Open Termux** and run these commands one by one:
   ```bash
   # Update the system
   pkg update && pkg upgrade -y

   # Install Python and Git
   pkg install python git -y

   # Navigate to the project folder (assuming you've moved the files here)
   cd lobster-ai-telegram

   # Run the automated installer
   bash install.sh
   ```

#### 💻 For PC (Windows/Linux/Mac)
1. Ensure you have **Python 3.10 or higher** installed.
2. Open your terminal or command prompt.
3. Navigate to the project folder:
   ```bash
   cd lobster-ai-telegram
   ```
4. Install the required libraries:
   ```bash
   pip install -r requirements.txt
   ```

### Step 3: Configure Your Token
You must tell the bot your Telegram Token before it can start.
1. Locate the file named `config.py` in the project folder.
2. Open it with a text editor (like Notepad on Windows, or `nano config.py` in Termux).
3. Find this line:
   ```python
   TELEGRAM_TOKEN = "YOUR_TELEGRAM_BOT_TOKEN_HERE"
   ```
4. Replace `YOUR_TELEGRAM_BOT_TOKEN_HERE` with the token you got from BotFather. **Keep the quotation marks!**
   *Example:* `TELEGRAM_TOKEN = "123456789:ABCdefGHIjklMNOpqrSTUvwxYZ"`
5. Save and close the file.

### Step 4: Start the Bot
1. In your terminal (Termux or PC), run:
   ```bash
   bash run.sh
   ```
   *(On Windows, you can just run `python bot.py`)*
2. You should see: `🦞 Lobster AI is crawling...`
3. Go to Telegram, find your bot, and send `/start`.

---

## ⚙️ Advanced Configuration
You can further customize the bot in `config.py`:
- **AI_PROVIDER**: Set to `"ollama"` (default) for local AI or `"openai"` for cloud AI.
- **OLLAMA_MODEL**: If using Ollama, specify your model (e.g., `"llama3"`, `"mistral"`).
- **OPENAI_API_KEY**: If using OpenAI, paste your API key here.

## 🧠 Commands
- `/start`: Initialize the conversation.
- `/clear`: Wipe the bot's memory of your conversation.

## 🛠 Troubleshooting
- **Permission Denied**: Run `chmod +x install.sh run.sh` to give execution permissions.
- **ModuleNotFoundError**: Ensure you ran `pip install -r requirements.txt`.
- **Connection Error**: Check your internet or ensure Ollama is running if using local AI.

---
*Created by Mahatab Khan*
