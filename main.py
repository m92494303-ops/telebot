import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from telebot import TeleBot

from start import start_handler
from ram import ram_handler
from admin import admin_handler
from premium import premium_handler

TOKEN = os.getenv("TOKEN")
ADMIN_ID = int(os.getenv("ADMIN_ID", 0))

bot = TeleBot(TOKEN)

start_handler(bot)
ram_handler(bot)
admin_handler(bot)
premium_handler(bot)

bot.polling(none_stop=True)
