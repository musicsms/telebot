import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from dotenv import load_dotenv
from news import getnew
import logging

load_dotenv()

TOKEN = os.getenv("TOKEN")

# Enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
# set higher logging level for httpx to avoid all GET and POST requests being logged
logging.getLogger("httpx").setLevel(logging.WARNING)

logger = logging.getLogger(__name__)


async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /start is issued."""
    user = update.effective_user
    await update.message.reply_html(
        rf"Hi {user.mention_html()}!"
    )


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /help is issued."""
    await update.message.reply_text("Help!")


async def news(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    news_list = getnew()
    for new in news_list:
        await update.message.reply_text(f'Tin mới: \n {new}')


def main() -> None:
    """Start the bot."""
    # Create the Application and pass it your bot's token.
    app = ApplicationBuilder().token(TOKEN).build()
    # on different commands - answer in Telegram
    app.add_handler(CommandHandler("start", hello))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("news", news))

    # Run the bot until the user presses Ctrl-C
    app.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    main()
