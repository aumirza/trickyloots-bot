from pyrogram import Client
from params import api_id, api_hash ,bot_name , bot_token
import os

bot = Client(bot_name,api_id,api_hash,bot_token=bot_token)

with bot:
    bot_string = bot.export_session_string()
    os.environ["BOT_STRING"] = bot_string
    print("BOT SESSION STRING",bot_string)
