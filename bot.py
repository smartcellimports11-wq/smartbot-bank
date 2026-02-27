import telebot

TOKEN = "COLOQUE_SEU_TOKEN_AQUI"

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(
        message,
        "🤖 SmartBot Bank Ativo!\n\nUse:\n/cobrar 100 João"
    )

@bot.message_handler(commands=['cobrar'])
def cobrar(message):
    try:
        partes = message.text.split()
        valor = partes[1]
        cliente = " ".join(partes[2:])

        resposta = f"""
💳 NOVA COBRANÇA

👤 Cliente: {cliente}
💰 Valor: R$ {valor}

📌 Chave PIX:
smartcellimports11@gmail.com

Envie o comprovante após o pagamento.
"""
        bot.reply_to(message, resposta)
    except:
        bot.reply_to(message, "❌ Use assim:\n/cobrar 100 João")

print("Bot rodando...")
bot.polling()
8681665732:AAF4yH7ZsDcbwM9AadyUwCdj9VNQ-cD6VEM
