from telebot import types
from utils.check_sub import is_subscribed
from utils.texts import ram_settings, premium_settings
from utils.premium import is_premium, add_premium
from config import CHANNEL

PRICE_STARS = 5  # ⭐ Telegram Stars

def ram_handler(bot):

    # 📱 RAM TUGMALARI
    @bot.callback_query_handler(func=lambda call: call.data.startswith("ram_"))
    def ram_callback(call):
        user_id = call.from_user.id
        ram = call.data.split("_")[1]

        if not is_subscribed(bot, user_id):
            kb = types.InlineKeyboardMarkup()
            kb.add(
                types.InlineKeyboardButton(
                    "📢 Kanalga obuna bo‘lish",
                    url=f"https://t.me/{CHANNEL[1:]}"
                ),
                types.InlineKeyboardButton(
                    "✅ Obuna bo‘ldim",
                    callback_data=f"check_{ram}"
                )
            )

            bot.send_message(
                call.message.chat.id,
                "❌ Avval kanalga obuna bo‘ling!",
                reply_markup=kb
            )
            return

        bot.send_message(
            call.message.chat.id,
            ram_settings(ram),
            parse_mode="Markdown"
        )

    # 🔁 OBUNA QAYTA TEKSHIRUV
    @bot.callback_query_handler(func=lambda call: call.data.startswith("check_"))
    def check_sub(call):
        ram = call.data.split("_")[1]
        user_id = call.from_user.id

        if is_subscribed(bot, user_id):
            bot.send_message(
                call.message.chat.id,
                ram_settings(ram),
                parse_mode="Markdown"
            )
        else:
            bot.answer_callback_query(
                call.id,
                "❌ Hali obuna emassiz!",
                show_alert=True
            )

    # 💯 PREMIUM TUGMA
    @bot.callback_query_handler(func=lambda call: call.data == "buy_premium")
    def buy_premium(call):
        bot.send_invoice(
    call.message.chat.id,
    "💯 100% Headshot Premium",
    "🎯 Maxsus headshot sensitivity\n"
    "🚀 Ultra FPS optimizatsiya\n"
    "👑 Premium sozlamalar\n\n"
    "💳 To‘lov: 5 ⭐ Telegram Stars",
    "premium_headshot",
    "",
    "XTR",
    [types.LabeledPrice("Premium", PRICE_STARS)],
)


    # ⭐ TO‘LOVDAN OLDIN
    @bot.pre_checkout_query_handler(func=lambda q: True)
    def checkout(pre_checkout_query):
        bot.answer_pre_checkout_query(pre_checkout_query.id, ok=True)

    # ✅ TO‘LOV MUVAFFAQIYATLI BO‘LGACH
    @bot.message_handler(content_types=['successful_payment'])
    def got_payment(message):
        if message.successful_payment.invoice_payload == "premium_headshot":
            bot.send_message(
                message.chat.id,
                premium_settings(),
                parse_mode="Markdown"
            )