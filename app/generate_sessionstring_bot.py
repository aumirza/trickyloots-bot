from pyrogram import Client
import os

bot_name = os.environ.get("BOT_NAME")
bot_tkn = os.environ.get("BOT_TKN")

bot = Client(bot_name,bot_token=bot_tkn)

s_file = bot_name + ".session"

with open(s_file,"w") as f:
    with bot:
        print("bot",bot.export_session_string())
