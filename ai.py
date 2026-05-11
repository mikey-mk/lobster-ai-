import requests
import json
from config import AI_PROVIDER, OPENAI_API_KEY, OPENAI_MODEL, OLLAMA_BASE_URL, OLLAMA_MODEL
from prompt import SYSTEM_PROMPT

class AIEngine:
    def __init__(self):
        self.provider = AI_PROVIDER

    def get_response(self, history):
        messages = [{"role": "system", "content": SYSTEM_PROMPT}]
        messages.extend(history)

        if self.provider == "openai":
            return self._openai_chat(messages)
        else:
            return self._ollama_chat(messages)

    def _openai_chat(self, messages):
        if not OPENAI_API_KEY:
            return "🦞 Error: OpenAI API Key not found in config.py"
        
        url = "https://api.openai.com/v1/chat/completions"
        headers = {
            "Authorization": f"Bearer {OPENAI_API_KEY}",
            "Content-Type": "application/json"
        }
        data = {
            "model": OPENAI_MODEL,
            "messages": messages
        }
        try:
            response = requests.post(url, headers=headers, json=data)
            response.raise_for_status()
            return response.json()['choices'][0]['message']['content']
        except Exception as e:
            return f"🦞 OpenAI Error: {str(e)}"

    def _ollama_chat(self, messages):
        url = f"{OLLAMA_BASE_URL}/api/chat"
        data = {
            "model": OLLAMA_MODEL,
            "messages": messages,
            "stream": False
        }
        try:
            response = requests.post(url, json=data)
            response.raise_for_status()
            return response.json()['message']['content']
        except Exception as e:
            return f"🦞 Ollama Error: {str(e)}. Is Ollama running?"
