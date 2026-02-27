import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = os.getenv(8681665732:AAF4yH7ZsDcbwM9AadyUwCdj9VNQ-cD6VEM)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🚀 SmartBot Bank Online!")

def main():
    application = ApplicationBuilder().token(TOKEN).build()
    application.add_handler(CommandHandler("start", start))
    print("Bot iniciado...")
    application.run_polling()

if __name__ == "__main__":
    main()
