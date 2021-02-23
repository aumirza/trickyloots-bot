from pyrogram import Client
from .params import bot_name , bot_token

bot = Client(bot_name,bot_token=bot_token)

with bot:
    print("bot",bot.export_session_string())
