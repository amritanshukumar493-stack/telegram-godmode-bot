import telebot
import time
import random
from datetime import datetime

TOKEN = "8561603354:AAHwuFqStB3ZLzIHwW1PM4ZiWYoQHYow"
ADMIN_IDS = [6165952964]

bot = telebot.TeleBot(TOKEN)

REPLIES = [
    "⚠ SYSTEM ALERT ⚠\nYour message is under surveillance.\nWait for admin.",
    "🔐 ENCRYPTION ENABLED\nMessage logged.",
    "📡 Secure channel active...\nStand by.",
    "🕶 Access detected.\nDo not spam."
]

NIGHT_REPLY = "🌙 NIGHT MODE\nAdmin offline."

def log(msg):
    with open("logs.txt", "a") as f:
        f.write(f"{datetime.now()} | {msg}\n")

@bot.message_handler(func=lambda m: True)
def handle(m):
    if m.from_user.id in ADMIN_IDS:
        return

    bot.send_chat_action(m.chat.id, 'typing')
    time.sleep(random.randint(2,5))

    hour = datetime.now().hour
    reply = NIGHT_REPLY if 0 <= hour <= 6 else random.choice(REPLIES)

    bot.reply_to(m, reply)
    log(m.text)

print("🔥 GOD MODE AUTO-REPLY LIVE 🔥")
bot.infinity_polling()
