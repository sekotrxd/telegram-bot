from telegram.ext import Updater, MessageHandler, Filters
import os

TOKEN = os.getenv("TOKEN")

def reply(update, context):
    update.message.reply_text("🔥")

updater = Updater(TOKEN, use_context=True)

dp = updater.dispatcher
dp.add_handler(MessageHandler(Filters.text, reply))

updater.start_polling()
updater.idle()
