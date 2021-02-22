from pyrogram import Client
import os

api_id = os.environ.get("API_ID")
api_hash = os.environ.get("API_HASH")

bot_name = os.environ.get("BOT_NAME")
bot_tkn = os.environ.get("BOT_TKN")

bot = Client(bot_name,bot_token=bot_tkn)
with bot:
    print("bot",bot.export_session_string())
    
self = Client("my_account", api_id, api_hash)

with self:
    print("self",self.export_session_string())

