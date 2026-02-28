import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from crm import buscar_cliente
import mercadopago
import requests
from dotenv import load_dotenv
import json

load_dotenv()  # carrega variáveis do arquivo .env

TOKEN = os.getenv("8681665732:AAF4yH7ZsDcbwM9AadyUwCdj9VNQ-cD6VEM")
MP_ACCESS_TOKEN = os.getenv("APP_USR-868352168445767-021016-645bc4b72763e563a30ca5206b38c45c-3135843170")

# Inicializa Mercado Pago
mp = mercadopago.SDK(APP_USR-5373db61-cda1-46cb-a001-168f39260acf)

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
