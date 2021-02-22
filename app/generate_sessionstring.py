from pyrogram import Client

api_id = os.environ.get("API_ID")
api_hash = os.environ.get("API_HASH")
self = Client("my_account", api_id, api_hash)

with self:
    print(self.export_session_string())

bot_name = os.environ.get("BOT_NAME")
bot_tkn = os.environ.get("BOT_TKN")

bot = Client(bot_name,bot_token=bot_tkn)
with bot:
    print(bot.export_session_string())