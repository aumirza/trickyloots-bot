import os
from pyrogram import Client

print("Checking session string for self...")

api_id = os.getenv("API_ID")
api_hash = os.getenv("API_HASH")

if os.getenv("SELF_STRING"):
    print("Session string for self already exists")
else:
    print("Session string for self not yet generated...")
    print("Generating session string for self...")

    phone_number = os.environ["PHONE_NUMBER"]

    self = Client("my_account", api_id, api_hash, phone_number=phone_number)

    with self:
        self_string = self.export_session_string()
        print("SELF SESSION STRING:\n", self_string)


print("Checking session string for bot...")

if os.getenv("BOT_STRING"):

    print("Session string for Bot already exists")
else:

    bot_token = os.getenv("BOT_TOKEN")
    bot_name = os.getenv("BOT_NAME")

    print("Session string for bot not yet generated...")
    print("Generating session string for bot...")

    bot = Client(bot_name, api_id, api_hash, bot_token=bot_token)

    with bot:
        bot_string = bot.export_session_string()
        print("BOT SESSION STRING", bot_string)

print("Copy session strings and set it in env variables.")
