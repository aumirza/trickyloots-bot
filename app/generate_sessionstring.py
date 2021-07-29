import os
from pyrogram import Client

print("Checking session string for self...")

if os.environ["SELF_STRING"]:
    print("Session string for self is already exists")
else:
    print("Session string for self not yet generated...")
    print("Generating session string for self...")

    api_id = os.environ["API_ID"]
    api_hash = os.environ["API_HASH"]
    phone_number = os.environ["PHONE_NUMBER"]

    self = Client("my_account", api_id, api_hash, phone_number=phone_number)

    with self:
        self_string = self.export_session_string()
        print("SELF SESSION STRING:\n", self_string)


print("Checking session string for bot...")

if os.environ["BOT_STRING"]:

    print("Session string for Bot already exists")
else:

    bot_token = os.environ["BOT_TOKEN"]
    bot_name = os.environ["BOT_NAME"]

    print("Session string for bot not yet generated...")
    print("Generating session string for bot...")

    bot = Client(bot_name, api_id, api_hash, bot_token=bot_token)

    with bot:
        bot_string = bot.export_session_string()
        print("BOT SESSION STRING", bot_string)

print("Copy session strings and set it in env variables.")
