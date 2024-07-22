import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from dotenv import load_dotenv
from news import getnew

load_dotenv()

TOKEN = os.getenv("TOKEN")


async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Xin chào {update.effective_user.first_name}')


async def news(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    news_list = getnew()
    for new in news_list:
        await update.message.reply_text(f'Tin mới: \n {new}')

app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("hello", hello))

app.add_handler(CommandHandler("news", news))

app.run_polling()
