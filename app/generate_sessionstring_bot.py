from pyrogram import Client
from params import api_id, api_hash ,bot_name , bot_token

bot = Client(bot_name,api_id,api_hash,bot_token=bot_token)

with bot:
    print("bot",bot.export_session_string())
