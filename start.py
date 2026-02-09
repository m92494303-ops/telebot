from keyboards.inline import ram_keyboard
from utils.texts import START_TEXT
from utils.users import save_user

def start_handler(bot):
    @bot.message_handler(commands=['start'])
    def start(message):
        save_user(message.from_user.id)

        bot.send_message(
            message.chat.id,
            START_TEXT,
            reply_markup=ram_keyboard(),
            parse_mode="Markdown"
        )
