import re
from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters,
)

BOT_TOKEN = "7605778799:AAGcm7clfAliM1NLDk3jt6mUAW5rxwd9pPs"

# Simple domain regex
LINK_REGEX = re.compile(
    r"^(?:https?://)?(?:www\.)?[a-zA-Z0-9-]+\.[a-zA-Z]{2,}$"
)

async def ping(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("I'm alive master")

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.strip()

    if LINK_REGEX.match(text):
        if not text.startswith(("http://", "https://")):
            text = "https://" + text
        await update.message.reply_text(text)
    else:
        await update.message.reply_text("Invalid: it is not a link")

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
  
