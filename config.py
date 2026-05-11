import os
from dotenv import load_dotenv

# Load environment variables from .env file if it exists
load_dotenv()

# Telegram Configuration
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN", "YOUR_TELEGRAM_BOT_TOKEN_HERE")

# AI Configuration
# Options: "openai" or "ollama"
AI_PROVIDER = os.getenv("AI_PROVIDER", "ollama")

# OpenAI Settings
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")
OPENAI_MODEL = os.getenv("OPENAI_MODEL", "gpt-3.5-turbo")

# Ollama Settings
OLLAMA_BASE_URL = os.getenv("OLLAMA_BASE_URL", "http://localhost:11434")
OLLAMA_MODEL = os.getenv("OLLAMA_MODEL", "llama3")

# Database Settings
DB_PATH = "data/memory.db"

# Bot Settings
MAX_MEMORY_MESSAGES = 10
BOT_NAME = "Lobster AI"
