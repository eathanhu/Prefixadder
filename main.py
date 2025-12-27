import re
from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters,
)

# ⚠️ Token kept as requested
BOT_TOKEN = "7605778799:AAGcm7clfAliM1NLDk3jt6mUAW5rxwd9pPs"

# Simple domain regex
LINK_REGEX = re.compile(
    r"^(?:https?://)?(?:www\.)?[a-zA-Z0-9-]+\.[a-zA-Z]{2,}$"
)

async def ping(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Works in groups only
    if update.message.chat.type == "private":
        return

    await update.message.reply_text(
        "I'm alive.\nReply to this message with a link."
    )

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message = update.message

    # 1️⃣ Ignore DMs
    if message.chat.type == "private":
        return

    # 2️⃣ Must be a reply
    if not message.reply_to_message:
        return

    # 3️⃣ Must be a reply to the bot
    if message.reply_to_message.from_user.id != context.bot.id:
        return

    text = message.text.strip()

    if LINK_REGEX.match(text):
        if not text.startswith(("http://", "https://")):
            text = "https://" + text
        await message.reply_text(text)
    else:
        await message.reply_text("❌ Invalid: it is not a link")

def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("ping", ping))
    app.add_handler(
        MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message)
    )

    print("Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()
    )

    print("Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()
  
