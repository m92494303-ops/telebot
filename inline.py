from telebot import types

def ram_keyboard():
    kb = types.InlineKeyboardMarkup(row_width=2)

    kb.add(
        types.InlineKeyboardButton("📱 2GB", callback_data="ram_2"),
        types.InlineKeyboardButton("⚙️ 3GB", callback_data="ram_3"),
        types.InlineKeyboardButton("🚀 4GB", callback_data="ram_4"),
        types.InlineKeyboardButton("🔥 6GB", callback_data="ram_6"),
        types.InlineKeyboardButton("💎 8GB", callback_data="ram_8"),
    )

    # 🔒 PREMIUM TUGMA
    kb.add(
        types.InlineKeyboardButton(
            "💯 100% HEADSHOT (Premium)",
            callback_data="buy_premium"
        )
    )

    return kb