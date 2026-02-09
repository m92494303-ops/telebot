from telebot import TeleBot

from handlers.start import start_handler
from handlers.ram import ram_handler
from handlers.admin import admin_handler
from handlers.premium import premium_handler
import os

TOKEN = os.getenv("TOKEN")
ADMIN_ID = int(os.getenv("ADMIN_ID", 0))

bot = TeleBot(TOKEN)
bot.polling(none_stop=True)

start_handler(bot)
ram_handler(bot)
admin_handler(bot)


bot.polling()

