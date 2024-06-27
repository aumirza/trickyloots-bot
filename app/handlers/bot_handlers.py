from pyrogram.handlers import MessageHandler
from pyrogram import filters
from helpers.p1_processor import processor as p1
from config import admins
from helpers.globalvar import *

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
        
        self.bot.add_handler(
            MessageHandler(
                self.add_blockword_handler,
                filters.command("addBlockword") &  filters.user(admins)
            ))

        self.bot.add_handler(
            MessageHandler(
                self.add_blockline_handler,
                filters.command("addBlockline") &  filters.user(admins)
            ))
        
        self.bot.add_handler(
            MessageHandler(
                self.add_blockmessage_handler,
                filters.command("addBlockmessage") &  filters.user(admins)
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

    def add_blockword_handler(self,client, message):
        command, *text_parts = message.text.split(maxsplit=1)
        if text_parts:
            text = text_parts[0]

            add_blockword(text)
            update_blockwords() 
            msg = f"Added {text} to blockwords."
            message.reply_text(msg)
        else:
            msg = "Please enter a word to add to blockwords."
            message.reply_text(msg)

    def add_blockline_handler(self, client, message):
        command, *text_parts = message.text.split(maxsplit=1)
        if text_parts:
            text = text_parts[0]

            add_blockline(text)
            update_blocklines()
            msg = f"Added {text} to blocklines."
            message.reply_text(msg)
        else:
            msg = "Please enter a word to add to blocklines."
            message.reply_text(msg)

    def add_blockmessage_handler(self, client, message):
        command, *text_parts = message.text.split(maxsplit=1)
        if text_parts:
            text = text_parts[0]

            add_blockmessage(text)
            update_blockmessages()
            msg = f"Added {text} to blockmessages."
            message.reply_text(msg)
        else:
            msg = "Please enter a word to add to blockmessages."
            message.reply_text(msg)