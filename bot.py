import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import mercadopago
from dotenv import load_dotenv

load_dotenv()

# COPIE ESTAS DUAS LINHAS EXATAMENTE ASSIM:
TOKEN = "8681665732:AAF4yH7ZsDcbwM9AadyUwCdj9VNQ-cd6VEM"
MP_ACCESS_TOKEN = "APP_USR-868352168445767-021016-645bc4b72763e563a30ca5206b38c45c-3135843170"

sdk = mercadopago.SDK(MP_ACCESS_TOKEN)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Bot Online! Use /cobrar")

if __name__ == '__main__':
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    print("Bot Iniciado...")
    app.run_polling()
