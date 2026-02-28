from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from crm import exemplo_crm  

import os

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🚀 SmartBot Bank Online!")

    dados = exemplo_crm()

    await update.message.reply_text(f"CRM retornou: {dados}")
TOKEN = os.getenv("8681665732:AAF4yH7ZsDcbwM9AadyUwCdj9VNQ-cD6VEM")
app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))

app.run_polling()
