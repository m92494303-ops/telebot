from config import ADMIN_ID
from utils.stats import premium_count, total_stars
from utils.users import load_users


def admin_handler(bot):

    # 👑 Admin panel
    @bot.message_handler(commands=['admin'])
    def admin_panel(message):
        if message.from_user.id != ADMIN_ID:
            return

        bot.send_message(
            message.chat.id,
            "👑 *Admin Panel*\n\n"
            "/users – foydalanuvchilar soni\n"
            "/stats – premium statistika\n"
            "/broadcast – hammaga xabar",
            parse_mode="Markdown"
        )

    # 👥 Foydalanuvchilar soni
    @bot.message_handler(commands=['users'])
    def users_count(message):
        if message.from_user.id != ADMIN_ID:
            return

        users = load_users()
        bot.send_message(
            message.chat.id,
            f"👥 Jami foydalanuvchilar: *{len(users)}*",
            parse_mode="Markdown"
        )

    # 📊 Premium statistika
    @bot.message_handler(commands=['stats'])
    def stats(message):
        if message.from_user.id != ADMIN_ID:
            return

        bot.send_message(
            message.chat.id,
            f"📊 *Premium statistika*\n\n"
            f"👑 Premium foydalanuvchilar: {premium_count()}\n"
            f"⭐ Yig‘ilgan Stars: {total_stars()}",
            parse_mode="Markdown"
        )

    # 📢 Broadcast boshlash
    @bot.message_handler(commands=['broadcast'])
    def broadcast_start(message):
        if message.from_user.id != ADMIN_ID:
            return

        msg = bot.send_message(
            message.chat.id,
            "✍️ Yubormoqchi bo‘lgan xabaringni yoz:"
        )
        bot.register_next_step_handler(msg, send_broadcast)

    # 📤 Broadcast yuborish
    def send_broadcast(message):
        users = load_users()
        success = 0

        for user_id in users:
            try:
                bot.send_message(user_id, message.text)
                success += 1
            except:
                pass

        bot.send_message(
            message.chat.id,
            f"✅ Xabar {success} ta foydalanuvchiga yuborildi."
        )