import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes
from config import TELEGRAM_TOKEN
from ai import AIEngine
from memory import Memory

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

ai_engine = AIEngine()
memory = Memory()

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    welcome_text = "🦞 Hey human, I'm Lobster AI! What's cooking?"
    await update.message.reply_text(welcome_text)
    memory.add_message(user_id, "assistant", welcome_text)

async def clear(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    memory.clear_history(user_id)
    await update.message.reply_text("🦞 Memory wiped. Who are you again?")

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    user_text = update.message.text

    # Add user message to memory
    memory.add_message(user_id, "user", user_text)

    # Get history for context
    history = memory.get_history(user_id)

    # Get AI response
    response = ai_engine.get_response(history)

    # Add bot response to memory
    memory.add_message(user_id, "assistant", response)

    # Send response
    await update.message.reply_text(response)

if __name__ == '__main__':
    if TELEGRAM_TOKEN == "YOUR_TELEGRAM_BOT_TOKEN_HERE":
        print("❌ Error: Please set your TELEGRAM_TOKEN in config.py or .env file")
    else:
        application = ApplicationBuilder().token(TELEGRAM_TOKEN).build()
        
        start_handler = CommandHandler('start', start)
        clear_handler = CommandHandler('clear', clear)
        msg_handler = MessageHandler(filters.TEXT & (~filters.COMMAND), handle_message)
        
        application.add_handler(start_handler)
        application.add_handler(clear_handler)
        application.add_handler(msg_handler)
        
        print("🦞 Lobster AI is crawling...")
        application.run_polling()
