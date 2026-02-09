from telebot import TeleBot
from config import TOKEN

from handlers.start import start_handler
from handlers.ram import ram_handler
from handlers.admin import admin_handler
from handlers.premium import premium_handler

bot = TeleBot(TOKEN)
bot.polling(none_stop=True)

start_handler(bot)
ram_handler(bot)
admin_handler(bot)


bot.polling()
