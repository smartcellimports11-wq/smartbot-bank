import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import mercadopago
import requests
from dotenv import load_dotenv
import json

load_dotenv()

# Linhas 12 e 13 corrigidas (sem os.getenv e com aspas)
TOKEN = "8681665732:AAF4yH7ZsDcbwM9AadyUwCdj9VNQ-cd6VEM"
MP_ACCESS_TOKEN = "APP_USR-868352168445767-021016-645bc4b72763e563a30ca5206b38c45c-3135843170"

# Inicializa Mercado Pago
sdk = mercadopago.SDK(MP_ACCESS_TOKEN)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("SmartBot Bank Online! Use /cobrar <valor>")

async def criar_cobranca(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        valor = float(context.args[0]) if context.args else 10.0
        payment_data = {
            "transaction_amount": valor,
            "description": "Cobrança SmartBot",
            "payment_method_id": "pix",
            "payer": {"email": "cliente@teste.com"}
        }
        result = sdk.payment().create(payment_data)
        link = result["response"]["point_of_interaction"]["transaction_data"]["qr_code"]
        await update.message.reply_text(f"Cobrança criada! Pix QR Code: {link}")
    except Exception as e:
        await update.message.reply_text(f"Erro ao gerar cobrança: {e}")

if __name__ == '__main__':
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("cobrar", criar_cobranca))
    print("Bot Iniciado com sucesso...")
    app.run_polling()
