from telegram.ext import Updater, MessageHandler, Filters
import os

TOKEN = os.getenv("TOKEN")

def echo(update, context):
    update.message.reply_text("bot çalışıyor 🔥")

updater = Updater(TOKEN, use_context=True)

dp = updater.dispatcher
dp.add_handler(MessageHandler(Filters.text, echo))

updater.start_polling()
updater.idle()
