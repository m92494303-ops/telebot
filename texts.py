# 🔥 START MATN
START_TEXT = (
    "🔥 *FREE FIRE SETTINGS BOT*\n\n"
    "🎯 Headshot aniqligini oshirishga yo‘naltirilgan sozlamalar\n"
    "📱 Telefon RAM bo‘yicha moslangan\n"
    "⚙️ Max sensitivity: 200\n\n"
    "👇 RAM tanlang:"
)

# 📱 BEPUL SOZLAMALAR (≈ 70% aniqlik)
def ram_settings(ram):
    data = {
        "2": (
            "📱 *2GB RAM – Headshot Settings*\n\n"
            "🎯 Aniqlik: ~70%\n\n"
            "⚙️ Sensitivity:\n"
            "• General: 165\n"
            "• Red Dot: 150\n"
            "• 2x Scope: 135\n"
            "• 4x Scope: 120\n"
            "• AWM Scope: 90\n"
            "• Free Look: 65\n\n"
            "⚠️ Past qurilmalar uchun barqaror variant"
        ),
        "3": (
            "📱 *3GB RAM – Headshot Settings*\n\n"
            "🎯 Aniqlik: ~70%\n\n"
            "⚙️ Sensitivity:\n"
            "• General: 170\n"
            "• Red Dot: 155\n"
            "• 2x Scope: 140\n"
            "• 4x Scope: 125\n"
            "• AWM Scope: 95\n"
            "• Free Look: 70\n\n"
            "⚡ Yaxshi balans"
        ),
        "4": (
            "📱 *4GB RAM – Headshot Settings*\n\n"
            "🎯 Aniqlik: ~70%\n\n"
            "⚙️ Sensitivity:\n"
            "• General: 175\n"
            "• Red Dot: 160\n"
            "• 2x Scope: 145\n"
            "• 4x Scope: 130\n"
            "• AWM Scope: 100\n"
            "• Free Look: 75\n\n"
            "🔥 O‘rtacha va kuchli qurilmalar"
        ),
        "6": (
            "📱 *6GB RAM – Headshot Settings*\n\n"
            "🎯 Aniqlik: ~70%\n\n"
            "⚙️ Sensitivity:\n"
            "• General: 180\n"
            "• Red Dot: 165\n"
            "• 2x Scope: 150\n"
            "• 4x Scope: 135\n"
            "• AWM Scope: 105\n"
            "• Free Look: 80\n\n"
            "🚀 Tezkor o‘yin uchun mos"
        ),
        "8": (
            "📱 *8GB RAM – Headshot Settings*\n\n"
            "🎯 Aniqlik: ~70%\n\n"
            "⚙️ Sensitivity:\n"
            "• General: 185\n"
            "• Red Dot: 170\n"
            "• 2x Scope: 155\n"
            "• 4x Scope: 140\n"
            "• AWM Scope: 110\n"
            "• Free Look: 85\n\n"
            "💎 Kuchli telefonlar uchun"
        ),
    }

    return data.get(ram, "❌ Sozlama topilmadi")

# 💯 PREMIUM SOZLAMALAR (≈ 90% aniqlik)
def premium_settings():
    return (
        "💯 *100% HEADSHOT – PREMIUM FF SETTINGS*\n\n"
        "👑 Tajribali o‘yinchilar uchun maxsus\n"
        "🎯 Aniqlik: 100%\n"
        "⚡ Flick + Drag shot optimizatsiya\n\n"
        "⚙️ *PRO SENSITIVITY*\n"
        "• General: 190\n"
        "• Red Dot: 178\n"
        "• 2x Scope: 165\n"
        "• 4x Scope: 148\n"
        "• AWM Scope: 120\n"
        "• Free Look: 90\n\n"
        "🔥 Afzalliklar:\n"
        "• Yaqin jangda tez headshot\n"
        "• Red Dot bilan yuqori barqarorlik\n"
        "• Sniper sakramaydi\n\n"
        "⚠️ Tavsiya: Fire Button sozlamasi bilan birga ishlating"
    )