#!/bin/bash

echo "🦞 Lobster AI Installation Started..."

# Create data directory
mkdir -p data

# Check if running in Termux
if [ -d "/data/data/com.termux/files/home" ]; then
    echo "📱 Termux detected. Updating packages..."
    pkg update && pkg upgrade -y
    pkg install python python-pip -y
else
    echo "💻 Linux/PC detected."
fi

# Install dependencies
echo "📦 Installing Python dependencies..."
pip install -r requirements.txt

echo ""
echo "✅ Installation Complete!"
echo "------------------------------------------------"
echo "🚀 NEXT STEPS:"
echo "1. Open 'config.py' and add your Telegram Bot Token."
echo "2. (Optional) Set AI_PROVIDER to 'openai' and add your API key."
echo "3. Run the bot using: bash run.sh"
echo "------------------------------------------------"
