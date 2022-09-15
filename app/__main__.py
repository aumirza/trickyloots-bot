from pyrogram import Client, filters, idle
from pyrogram.handlers import MessageHandler, EditedMessageHandler
from app.config import h1_chat, h2_chat, admins, api_id, api_hash, self_string, bot_string
from app.handlers.bot_handlers import admin_start_comm_handler, convert_comm_handler, start_comm_handler

if bot_string and self_string:

    self = Client('my_account', api_id, api_hash, session_string=self_string)
    bot = Client('tlooters_bot', api_id, api_hash,
                 session_string=bot_string)

from app.handlers.self_handlers import main_channel_handler, secondary_channel_handler

if __name__ == "__main__":

    # Self Handlers

    self.add_handler(MessageHandler(
        main_channel_handler, filters.chat(h1_chat)))

    self.add_handler(
        EditedMessageHandler(
            secondary_channel_handler,
            filters.chat(h2_chat) & filters.media
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

    self.start()
    print("Self Started", self.is_connected)
    bot.start()
    print("Bot Started", bot.is_connected)
    idle()
    self.stop()
    bot.stop()
