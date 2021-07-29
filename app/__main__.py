from pyrogram import Client, filters
from pyrogram.handlers import MessageHandler
from app.config import h1_chat, h2_chat, admins, api_id, api_hash, self_string, bot_string
from app.handlers.bot_handlers import *
from app.handlers.self_handlers import *


if bot_string and self_string:

    self = Client(self_string, api_id, api_hash)
    bot = Client(bot_string, api_id, api_hash)

    bot.start()

    # Sekf Handlers
    self.add_handler(
        MessageHandler(
            main_channel_handler,
            filters.chat(h1_chat) & ~ filters.edited
        ))

    self.add_handler(
        MessageHandler(
            secondary_channel_handler,
            filters.chat(h2_chat) & filters.edited & filters.media
        ))

    # Bot handlers
    bot.add_handler(
        MessageHandler(
            admin_start_comm_handler,
            filters.user(admins) & filters.command("start")
        ))

    bot.add_handler(
        MessageHandler(
            convert_comm_handler,
            filters.user(admins) & filters.command("convert") & filters.reply
        ))

    bot.add_handler(
        MessageHandler(
            start_comm_handler,
            filters.command("start") & ~ filters.user(admins)
        ))

    self.run()
