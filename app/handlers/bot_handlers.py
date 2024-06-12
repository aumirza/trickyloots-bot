from pyrogram.handlers import MessageHandler
from pyrogram import filters
from helpers.p1_processor import processor as p1
from config import admins

class BotHandler :
    def __init__(self, bot):
        self.bot = bot

    def add_handlers(self):
        self.bot.add_handler(
        MessageHandler(
            self.admin_start_comm_handler,
            filters.user(admins) & filters.command("start")
        ))

        self.bot.add_handler(
            MessageHandler(
                self.convert_comm_handler,
                filters.user(admins) & filters.command("convert") & filters.reply
            ))

        self.bot.add_handler(
            MessageHandler(
                self.start_comm_handler,
                filters.command("start") & ~ filters.user(admins)
            ))

    def admin_start_comm_handler(self,client, message):
        msg = f"Hi! {message.from_user.first_name}.\nThe bot is currently running."
        message.reply_text(msg)


    def convert_comm_handler(self,client, message):
        if message.media:
            msg = p1(message.reply_to_message.caption).process()
            if msg != "":
                message.reply_photo(photo=message.photo.file_id,
                                    caption=msg, quote=True)
        else:
            msg = p1(message.reply_to_message.text).process()
            if msg != "":
                message.reply_text(msg, quote=True, disable_web_page_preview=True)

    def start_comm_handler(self,client, message):
        msg = "Sorry......... \n This bot is not for you"
        message.reply_text(msg)
