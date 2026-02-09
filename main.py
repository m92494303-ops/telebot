from telebot import TeleBot
import os

from bot.handlers.start import start_handler
from bot.handlers.ram import ram_handler
from bot.handlers.admin import admin_handler
from bot.handlers.premium import premium_handler

TOKEN = os.getenv("TOKEN")
ADMIN_ID = int(os.getenv("ADMIN_ID", 0))

bot = TeleBot(TOKEN)

# 🔗 handlerlarni ulaymiz
start_handler(bot)
ram_handler(bot)
admin_handler(bot)
premium_handler(bot)

# 🚀 botni ishga tushiramiz
bot.polling(none_stop=True)
