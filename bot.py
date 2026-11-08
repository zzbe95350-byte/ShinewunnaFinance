import os
import logging
from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters
)

logging.basicConfig(level=logging.INFO)

TOKEN = os.environ["BOT_TOKEN"]
OWNER_ID = int(os.environ["OWNER_ID"])

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_user.id != OWNER_ID:
        return

    await update.message.reply_text(
        "မင်္ဂလာပါ။ Ying Finance Bot မှ ကြိုဆိုပါတယ်။\n\n"
        "🧾 Receipt ပို့ပြီး ငွေစာရင်း မှတ်တမ်းတင်နိုင်ပါမယ်။\n"
        "/help - အကူအညီ"
    )

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_user.id != OWNER_ID:
        return

    await update.message.reply_text(
        "Ying Finance Bot\n"
        "/start - စတင်ရန်\n"
        "/help - အကူအညီ\n"
        "Receipt ပို့ခြင်းကို နောက်အဆင့်မှာ ဖွင့်ပေးပါမယ်။"
    )

def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.run_polling()

if __name__ == "__main__":
    main()
