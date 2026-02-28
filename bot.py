import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from crm import buscar_cliente
import mercadopago
import requests
from dotenv import load_dotenv
import json

load_dotenv()  # carrega variáveis do arquivo .env

TOKEN = os.getenv("TELEGRAM_TOKEN")
MP_ACCESS_TOKEN = os.getenv("MP_ACCESS_TOKEN")

# Inicializa Mercado Pago
mp = mercadopago.SDK(MP_ACCESS_TOKEN)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    cliente = buscar_cliente()
    await update.message.reply_text(f"SmartBot Bank Online!\nCliente ativo: {cliente['nome']}")

async def criar_cobranca(update: Update, context: ContextTypes.DEFAULT_TYPE):
    valor = float(context.args[0]) if context.args else 10.0
    pagamento = {
        "transaction_amount": valor,
        "description": "Cobrança SmartBot",
        "payment_method_id": "pix",
        "payer": {"email": "cliente@teste.com"}
    }
    result = mp.payment().create(pagamento)
    link = result["response"]["point_of_interaction"]["transaction_data"]["qr_code"]
    await update.message.reply_text(f"Cobrança criada! Pix QR Code: {link}")

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("cobrar", criar_cobranca))

app.run_polling()
