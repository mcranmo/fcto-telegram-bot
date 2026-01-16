from pyrogram import Client, filters
import os

API_ID = int(os.getenv("API_ID", "0"))
API_HASH = os.getenv("API_HASH")
BOT_TOKEN = os.getenv("BOT_TOKEN")

app = Client(
    "fcto_telegram_bot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

@app.on_message(filters.command("start"))
async def start(_, message):
    await message.reply("🚀 FCTO Telegram Bot is LIVE!")

@app.on_message(filters.command("help"))
async def help_cmd(_, message):
    await message.reply("Commands:\n/start\n/help")

app.run()

